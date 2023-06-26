# Step by step explanation of implementing Azure Cognitive Search 

### 1. Create Azure Cognitive Search
- 
    `az search service create --name <mysearch> --resource-group <mysearch-rg> --sku free --location westus`

- Authentication:
    - `az search admin-key show --service-name searchdemochatgpt --resource-group demo-langchain`
    - admin: read-write
    - query: read-only

### 2. Create/update/delete an index/indexer/documents
- [Link to Pythons SDK samples on GitHub](https://github.com/Azure/azure-sdk-for-python/tree/main)
- [Link to Microsoft learn overview](https://learn.microsoft.com/en-us/azure/search/samples-python)




