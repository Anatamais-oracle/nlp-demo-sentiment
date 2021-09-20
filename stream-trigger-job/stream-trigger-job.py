import oci
import time
import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

from base64 import b64decode

ociMessageEndpoint = os.environ['OCI_MESSAGE_ENDPOINT']  
ociStreamOcid = os.environ['OCI_STREAM_OCID']
ociConfigFilePath = os.environ['OCI_CONFIG_FILE_PATH']
ociProfileName = os.environ['OCI_PROFILE_NAME']


def get_cursor_by_group(sc, sid, group_name, instance_name):
    print(" Creating a cursor for group {}, instance {}".format(group_name, instance_name))
    cursor_details = oci.streaming.models.CreateGroupCursorDetails(group_name=group_name, instance_name=instance_name,
                                                                   type=oci.streaming.models.
                                                                   CreateGroupCursorDetails.TYPE_TRIM_HORIZON,
                                                                   commit_on_get=True)
    response = sc.create_group_cursor(sid, cursor_details)
    return response.data.value

def simple_message_loop(client, stream_id, initial_cursor):

    cursor = initial_cursor
    while True:
        get_response = client.get_messages(stream_id, cursor, limit=1000)
        # No messages to process. return.
        #if not get_response.data:
        #    return

        # Process the messages
        print(" Read {} messages".format(len(get_response.data)))
        for message in get_response.data:
            if message.key is None:
                key = "Null"
            else:
                key = b64decode(message.key.encode()).decode()
                value = b64decode(message.value.encode()).decode()
                url = f"http://{os.environ['PREDICTSENTIMENT_LB_IP']}:8082/predict"
    
                headers = {
                           "Content-Type": "application/json",
                           "authorization": os.environ['AUTH_TOKEN_PREDICTSENTIMENT']
                          }
                
                requests.post(url, json=json.dumps(json.loads(value)), headers=headers)


        # get_messages is a throttled method; clients should retrieve sufficiently large message
        # batches, as to avoid too many http requests.
        time.sleep(1)
        # use the next-cursor for iteration
        cursor = get_response.headers["opc-next-cursor"]


config_oci = oci.config.from_file(ociConfigFilePath, ociProfileName)
stream_client = oci.streaming.StreamClient(config_oci, service_endpoint=ociMessageEndpoint)

# A cursor can be created as part of a consumer group.
# Committed offsets are managed for the group, and partitions
# are dynamically balanced amongst consumers in the group.
group_cursor = get_cursor_by_group(stream_client, ociStreamOcid, "example-group", "example-instance-1")
simple_message_loop(stream_client, ociStreamOcid, group_cursor)
