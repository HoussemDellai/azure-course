# create a resource group
az group create --name rg-servicebus --location swedencentral

# create a service bus namespace with SKU standard
az servicebus namespace create -g rg-servicebus -n sb-namespace-sncf --location swedencentral --sku Standard

# create a service bus queue with duplicate detection enabled
az servicebus queue create -g rg-servicebus --namespace-name sb-namespace-sncf -n sb-queue --enable-duplicate-detection true --duplicate-detection-history-time-window P1D

# get the connection string
az servicebus namespace authorization-rule keys list -g rg-servicebus --namespace-name sb-namespace-sncf -n RootManageSharedAccessKey --query primaryConnectionString --output tsv

# install the required packages
pip install azure-identity azure-servicebus azure-mgmt-servicebus azure.mgmt.servicebus datetime logging