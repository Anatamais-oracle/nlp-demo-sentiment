until [[ `kubectl get svc predict-sentiment-api-minikube-service -o yaml | grep  ip | cut -d ":" -f2 | tr -d " \t\n\r"` != "" ]]
do
  sleep 5s
done

docker build -t translation-api-image ./stream-trigger-job

docker login <region>.ocir.io -u='<Object Storage Namespace>/oracleidentitycloudservice/<user>' -p='<Auth Token>'
docker tag translation-api-image:latest <region>.ocir.io/<Object Storage Namespace>/stream-trigger-job:latest
docker push <region>.ocir.io/<Object Storage Namespace>/stream-trigger-job:latest
