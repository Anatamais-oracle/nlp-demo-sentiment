docker build -t facebook-job-image:test ./facebook-job

docker login <region>.ocir.io -u='<Object Storage Namespace>/oracleidentitycloudservice/<user>' -p='Auth Token<>'
docker tag facebook-job-image:test <region>.ocir.io/<Object Storage Namespace>/facebook-job:test
docker push <region>.ocir.io/<Object Storage Namespace>/facebook-job:test
