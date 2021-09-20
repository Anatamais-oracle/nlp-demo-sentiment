until [[ `kubectl get svc translation-api-minikube-service -o yaml | grep  ip | cut -d ":" -f2 | tr -d " \t\n\r"` != "" ]]
do
  sleep 5s
done

docker build -t predict-sentiment-api-image ./predict-sentiment-api

docker login <region>.ocir.io -u='<Object Storage Namespace>/oracleidentitycloudservice/<user>' -p='<Auth Token>'
docker tag predict-sentiment-api-image:latest <region>.ocir.io/<Object Storage Namespace>/predict-sentiment:latest
docker push <region>.ocir.io/<Object Storage Namespace>/predict-sentiment:latest
