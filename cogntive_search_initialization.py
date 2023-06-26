import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import SearchIndex, ScoringProfile, SimpleField, CorsOptions
from secrets import Secrets

# Credentials
endpoint = Secrets.endpoint
key = Secrets.key

credential = AzureKeyCredential(key)

# Create an index client 
client = SearchIndexClient(endpoint=endpoint, credential=credential)

def create_index():
    name = "demo-index"
    fields = [
        SimpleField(name="id", type="Edm.String", key=True),
        SimpleField(name="title", type="Edm.String", searchable=True),
        SimpleField(name="context", type="Edm.String", searchable=True)]
    cors_options = CorsOptions(allowed_origins=["*"], max_age_in_seconds=60)
    scoring_profiles = []
    index = SearchIndex(name=name, fields=fields, scoring_profiles=scoring_profiles, cors_options=cors_options)
    result = client.create_index(index)
    print(result)

create_index()