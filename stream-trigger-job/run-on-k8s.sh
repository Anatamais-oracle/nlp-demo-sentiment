export OCI_CLI_SUPPRESS_FILE_PERMISSIONS_WARNING=True
export PREDICTSENTIMENT_LB_IP=`kubectl get svc predict-sentiment-api-minikube-service -o yaml | grep  ip | cut -d ":" -f2 | tr -d " \t\n\r"`
envsubst "`printf '${%s} ' $(sh -c "env|cut -d'=' -f1")`" < stream-trigger-job/k8s-deployment.yaml > stream-trigger-job/k8s-deployment-deploy.yaml
<access cluster>
kubectl create secret docker-registry ocirsecret --docker-server=<region>.ocir.io --docker-username='<Object Storage Namespace>/<user>' --docker-password='<Auth Token>' --docker-email='<user>'
kubectl create -f stream-trigger-job/k8s-deployment-deploy.yaml || (kubectl delete -f stream-trigger-job/k8s-deployment-deploy.yaml && kubectl create -f stream-trigger-job/k8s-deployment-deploy.yaml)
rm stream-trigger-job/k8s-deployment-deploy.yaml
