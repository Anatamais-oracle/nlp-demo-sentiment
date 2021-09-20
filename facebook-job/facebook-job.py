import requests
import pandas as pd
import datetime
import pytz
import oci
from base64 import b64encode 
import json
import os

from dotenv import load_dotenv
load_dotenv()


def fb_settings():
    days = datetime.timedelta(5)
    minutes = datetime.timedelta(minutes=60)
    utc=pytz.UTC
    page_id = os.environ['PAGE_ID']
    access_token = os.environ['ACCESS_TOKEN_FB']
    return days, minutes, utc, page_id, access_token


def get_fb_posts(days, utc, page_id, access_token):
    url= f'https://graph.facebook.com/{page_id}/posts?access_token={access_token}&order=reverse_chronological'
    response = requests.get(url)
    data = response.json()
    df_posts = pd.DataFrame(data['data'])

    while len(data['data']) != 0 and datetime.datetime.strptime(data['data'][-1]['created_time'], "%Y-%m-%dT%H:%M:%S%z") >= datetime.datetime.now(tz=utc) - days:
        url = f"https://graph.facebook.com/{page_id}/posts?access_token={access_token}&after={data['paging']['cursors']['after']}"
        response = requests.get(url)
        data = response.json()
        if len(data['data']) == 0:
            break
        df_posts = pd.concat([df_posts, pd.DataFrame(data['data'])])
        
    return df_posts


def get_fb_comments(df_posts, minutes, utc, page_id, access_token):
    if len(df_posts) == 0:
        return pd.DataFrame({})
    for i, post in df_posts.iterrows():
        post_id = post['id']
        url = f'https://graph.facebook.com/{post_id}/comments?access_token={access_token}&order=reverse_chronological'
        response = requests.get(url)
        data = response.json()
        try:
            df_comments = pd.concat([df_comments, pd.DataFrame([{**post, **{'post_id':post_id}} for post in data['data']])])
        except:
            df_comments = pd.DataFrame([{**post, **{'post_id':post_id}} for post in data['data']])
        
        while len(data['data']) != 0 and datetime.datetime.strptime(data['data'][-1]['created_time'], "%Y-%m-%dT%H:%M:%S%z") >= datetime.datetime.now(tz=utc) - minutes:
            url = f"https://graph.facebook.com/{post_id}/comments?access_token={access_token}&order=reverse_chronological&after={data['paging']['cursors']['after']}"
            response = requests.get(url)
            data = response.json()
            if len(data['data']) == 0:
                break
            df_comments = pd.concat([df_comments, pd.DataFrame([{**post, **{'post_id':post_id}} for post in data['data']])])
        if len(df_comments) > 0:
            df_comments = df_comments[df_comments['created_time'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%dT%H:%M:%S%z")) >= datetime.datetime.now(tz=utc) - minutes]
            
    return df_comments

def get_fb_threads(df_comments, minutes, utc, page_id, access_token):
    if len(df_comments) == 0:
        return pd.DataFrame({})
    for i, comment in df_comments.iterrows():
        comment_id = comment['id']
        url = f'https://graph.facebook.com/{comment_id}/comments?access_token={access_token}&order=reverse_chronological'
        response = requests.get(url)
        data = response.json()
        try:
            df_threads = pd.concat([df_threads, pd.DataFrame([{**comment, **{'comment_id':comment_id}} for comment in data['data']])])
        except:
            df_threads = pd.DataFrame([{**comment, **{'comment_id':comment_id}} for comment in data['data']])
        
        while len(data['data']) != 0 and datetime.datetime.strptime(data['data'][-1]['created_time'], "%Y-%m-%dT%H:%M:%S%z") >= datetime.datetime.now(tz=utc) - minutes:
            url = f"https://graph.facebook.com/{comment_id}/comments?access_token={access_token}&order=reverse_chronological&after={data['paging']['cursors']['after']}"
            response = requests.get(url)
            data = response.json()
            if len(data['data']) == 0:
                break
            df_threads = pd.concat([df_threads, pd.DataFrame([{**comment, **{'comment_id':comment_id}} for comment in data['data']])])
        if len(df_threads) > 0:
            df_threads = df_threads[df_threads['created_time'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%dT%H:%M:%S%z")) >= datetime.datetime.now(tz=utc) - minutes]
            
    return df_threads

def send_to_stream(df_comments):
    ociMessageEndpoint = os.environ['OCI_MESSAGE_ENDPOINT'] 
    ociStreamOcid = os.environ['OCI_STREAM_OCID']
    ociConfigFilePath = os.environ['OCI_CONFIG_FILE_PATH']
    ociProfileName = os.environ['OCI_PROFILE_NAME']

    config = oci.config.from_file(ociConfigFilePath, ociProfileName) 
    stream_client = oci.streaming.StreamClient(config, service_endpoint=ociMessageEndpoint) 

    message_list = [oci.streaming.models.PutMessagesDetailsEntry(key=b64encode(row['id'].encode()).decode(), 
                                                                 value=b64encode(json.dumps(row.to_dict()).encode()).decode()
                                                                ) for i, row in df_comments.iterrows()]
    messages = oci.streaming.models.PutMessagesDetails(messages=message_list)  
    put_message_result = stream_client.put_messages(ociStreamOcid, messages)  
    
    
def main():
    days, minutes, utc, page_id, access_token = fb_settings()
    df_posts = get_fb_posts(days, utc, page_id, access_token)
    df_comments = get_fb_comments(df_posts, minutes, utc, page_id, access_token)
    #df_threads = get_fb_threads(df_comments, minutes, utc, page_id, access_token)
    if len(df_comments) > 0:
        send_to_stream(df_comments)
    
if __name__ == "__main__":
    main()
