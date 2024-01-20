from langchain_community.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
import yaml

# load the config file
with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

# create the open-source embedding function
embedding_function = SentenceTransformerEmbeddings(model_name=config['Model'])

# start the vector database retrieval engine
def retrieve_vector_db(query):
    db_vector = Chroma(persist_directory="./db", embedding_function=embedding_function)
    results = db_vector.similarity_search(query, k=10)
    return results
