from pinecone import Pinecone
import os
from sentence_transformers import SentenceTransformer
from pinecone import ServerlessSpec
import time
from tqdm.auto import tqdm

# initialize connection to pinecone
api_key = os.getenv("049f0927-0d19-4e1b-9142-81b515f08787") or "049f0927-0d19-4e1b-9142-81b515f08787"

# configure client
pc = Pinecone(api_key=api_key)

#index specification 


spec = ServerlessSpec(
    cloud="aws", region="us-east-1"
)



index_name = 'raima-isla-code-exercise'
existing_indexes = [
    index_info["name"] for index_info in pc.list_indexes()
]

# check if index already exists (it shouldn't if this is first time)
if index_name not in existing_indexes:
    # if does not exist, create index
    pc.create_index(
        index_name,
        dimension= 768,  # dimensionality of multilingual e5
        metric='dotproduct',
        spec=spec
    )
    # wait for index to be initialized
    while not pc.describe_index(index_name).status['ready']:
        time.sleep(1)

# connect to index
index = pc.Index(index_name)
time.sleep(1)
# # view index stats
# print(index.describe_index_stats())

# model_path = "models/multilingual-e5-base"
# model = SentenceTransformer(model_path)