export OCI_CLI_SUPPRESS_FILE_PERMISSIONS_WARNING=True
<access cluster>
kubectl create secret docker-registry ocirsecret --docker-server=<region>-1.ocir.io --docker-username='<Object Storage Namespace>/<user>' --docker-password='Auth Token>' --docker-email='<user>'
kubectl create -f translation-api/k8s-deployment.yaml || (kubectl delete -f translation-api/k8s-deployment.yaml && kubectl create -f translation-api/k8s-deployment.yaml)
