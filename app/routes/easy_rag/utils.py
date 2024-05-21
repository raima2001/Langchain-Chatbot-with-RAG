import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
from app.routes.easy_rag.pinecone_store import index
from tqdm.auto import tqdm
from app.routes.easy_rag.sentence_t_model import embed_texts
from app.routes.easy_rag.retrival_info import ask_question, initialize_qa_system




def save_to_dataframe(texts, domain):
    if not os.path.exists("data"):
        os.makedirs("data")

    df = pd.DataFrame(texts, columns=['text', 'url'])
    df.to_csv(f"data/{domain}_scraped.csv", index=False)
    return df

def process_scraped_data(website: str, text_content: str):
    domain = website.replace("https://", "").replace("http://", "").split("/")[0]
    texts = [(text_content, website)]
    return save_to_dataframe(texts, domain)

def embed_and_upsert(df):
    batch_size = 100

    for i in tqdm(range(0, len(df), batch_size)):
        i_end = min(len(df), i + batch_size)
        batch = df.iloc[i:i_end]

        # Generate unique ids for each chunk
        ids = [f"{i}-{j}" for j in range(i, i_end)]

        # Get text to embed
        texts = batch['text'].tolist()

        # Embed text
        embeds = embed_texts(texts)
        print(embeds)

        # Prepare metadata for Pinecone
        metadata = [{'text': text, 'url': url} for text, url in zip(batch['text'], batch['url'])]
        

        # Upsert to Pinecone
        vectors = list(zip(ids, embeds, metadata))
        index.upsert(vectors)



async def easy_index_utils(website: str):
    try:
        response = requests.get(website)
        response.raise_for_status()  

        soup = BeautifulSoup(response.content, 'html.parser')

        text_content = soup.get_text()
        df = process_scraped_data(website, text_content)
        embed_and_upsert(df)
        print("Data embedded and upserted to Pinecone successfully.")

        print(index.describe_index_stats())

        return {"result": df.to_dict()}  

    except requests.RequestException as e:
        return {"error": f"Failed to retrieve website: {str(e)}"}
    except Exception as e:
        return {"error": str(e)}
        


    


######################
async def easy_rag_utils(query: str):
    initialize_qa_system()
    response = ask_question(query)
    return {"result": response}
