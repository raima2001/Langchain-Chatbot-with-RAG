from pinecone import Pinecone
import os
from pinecone import ServerlessSpec
import time
from dotenv import load_dotenv  

load_dotenv()
pinecone_api_key = os.getenv("PINECONE_API_KEY")


pc = Pinecone(api_key=pinecone_api_key)

spec = ServerlessSpec(
    cloud="aws", region="us-east-1"
)

index_name = 'raima-isla-code-exercise'
existing_indexes = [
    index_info["name"] for index_info in pc.list_indexes()
]


if index_name not in existing_indexes:
    
    pc.create_index(
        index_name,
        dimension= 768,  
        metric='dotproduct',
        spec=spec
    )
    
    while not pc.describe_index(index_name).status['ready']:
        time.sleep(1)


index = pc.Index(index_name)
time.sleep(1)

# print(index.describe_index_stats())

