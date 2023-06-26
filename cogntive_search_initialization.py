import os
import PyPDF2
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import SearchIndex, ScoringProfile, SimpleField, CorsOptions, SearchableField
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

def update_index():
    name = "demo-index"
    fields = [
        SimpleField(name="id", type="Edm.String", key=True),
        SimpleField(name="title", type="Edm.String", searchable=True),
        SimpleField(name="context", type="Edm.String", searchable=True),
        SearchableField(name="content", type="Edm.String", searchable=True)]
    cors_options = CorsOptions(allowed_origins=["*"], max_age_in_seconds=60)
    scoring_profiles = []
    index = SearchIndex(name=name, fields=fields, scoring_profiles=scoring_profiles, cors_options=cors_options)
    result = client.create_or_update_index(index)
    print(result)

# Check if index exists before crating 
index_exists = client.list_index_names()
if "demo-index" in index_exists:
    print("Index already exists")
    #update_index()
else:
    print("Creating index")
    create_index()

def delete_document(filepath):
    index_name = "demo-index"
    search_client = SearchClient(endpoint=endpoint, index_name=index_name, credential=credential)
    result = search_client.delete_documents([{"id": filepath.split("/")[-1].split(".")[0]}])
    print(result)

# Read file from local directory and add it to the index
def upload_document(filepath):
    index_name = "demo-index"
    search_client = SearchClient(endpoint=endpoint, index_name=index_name, credential=credential)
    with open(filepath, 'rb') as f:
        # Read pdf file into a string
        data = open(filepath, 'rb')
        pdfReader = PyPDF2.PdfReader(data)
        content = ""
        for i in range(len(pdfReader.pages)):
            content += pdfReader.pages[i].extract_text()
        data.close()
        #data = base64.b64decode(f.read()).decode("utf-8")
    
    print(content)
    doc = {
        "id": filepath.split("/")[-1].split(".")[0],
        "title": filepath.split("/")[-1],
        "context": "",
        "content": content
    }
    result = search_client.upload_documents(documents=[doc])
    print(result)

# Get all files from subdirectory
def get_files():
    path = os.getcwd() + "/data"
    files = os.listdir(path)
    for file in files:
        filepath = os.path.join(path, file)
        upload_document(filepath)

#get_files()

path = os.getcwd() + "/data/cinderella.pdf"
delete_document(path)
