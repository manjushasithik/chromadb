from langchain_community.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
import yaml
from data_loader import load_text


# load the config file
with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

# create the open-source embedding function
def create_vector_db(container_name):
    embedding_function = SentenceTransformerEmbeddings(model_name=config['Model'])
    data_text = load_text(config['Containers'][f'{container_name}'])
    vector_db = Chroma.from_documents(documents=data_text, persist_directory="db/", embedding=embedding_function)
    return True

