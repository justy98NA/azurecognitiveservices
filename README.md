# Step by step explanation of implementing enterprise chatbot using ChatGPT and Azure

## Requirements 
- Azure Cognitive Search Service

    `az search service create --name <mysearch> --resource-group <mysearch-rg> --sku free --location westus`

    - Authentication:
      - `az search admin-key show --service-name searchdemochatgpt --resource-group demo-langchain`
      - admin: read-write
      - query: read-only

- python > 3.7
- azure-search-documents

