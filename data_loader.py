from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from azure.storage.blob import ContainerClient
from langchain_community.document_loaders import AzureBlobStorageContainerLoader
import yaml

# load the config file
with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

# connection
container_client = ContainerClient.from_connection_string(
    config['Secure_Connection_String'], container_name=config['Containers']['chromadbtest'])
loader = AzureBlobStorageContainerLoader(config['Secure_Connection_String'], config['Containers']['chromadbtest'])


# create the text loader
def load_text(container_name):
    loader = AzureBlobStorageContainerLoader(config['Secure_Connection_String'], config['Containers'][f'{container_name}'])
    docs = loader.load()
    txt_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
    docs = txt_splitter.split_documents(docs)
    return docs