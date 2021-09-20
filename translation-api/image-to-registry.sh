docker build -t translation-api-image:latest ./translation-api

docker login <region>.ocir.io -u='<Object Storage Namespace>/oracleidentitycloudservice/<user>' -p='<Auth Token>'
docker tag translation-api-image:latest <region>.ocir.io/<Object Storage Namespace>/nlp-translation:latest
docker push <region>.ocir.io/<Object Storage Namespace>/nlp-translation:latest
