import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from secrets import Secrets

# Credentials
endpoint = Secrets.endpoint
key = Secrets.key

credential = AzureKeyCredential(key)
