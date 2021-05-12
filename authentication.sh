az login
az extension add -n azure-cli-ml
az ad sp create-for-rbac --sdk-auth --name ml-auth
az ad sp show --id [CLIENT ID]

az ml workspace share \
-w [WORKSPACE] \
-g [RESOURCE GROUP] \
--user [OBJECT ID] \
--role owner