from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.routes.easy_rag.setup.pinecone_store import index
from app.routes.easy_rag.setup.embedding import embed_texts
from tqdm import tqdm

def embed_and_upsert_website(website_url):
    # Load the document from the provided website URL
    loader = WebBaseLoader([website_url])
    wb_loader_doc = loader.load()

    # Initialize the text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=50,
        length_function=len,
        is_separator_regex=False,
    )

    # Split the document into chunks
    wb_chunks = text_splitter.split_documents(wb_loader_doc)
    print(wb_chunks)

    # Extract metadata and text content from each chunk
    wb_chunks_text = [{'title': doc.metadata.get('title', ''), 'source': doc.metadata.get('source', ''), 'page_content': doc.page_content} for doc in wb_chunks]

    # Embed and upsert each chunk
    for i, chunk in tqdm(enumerate(wb_chunks_text)):
        id = f"chunk_{i}"
        text = chunk['page_content']
        embed = embed_texts([text])[0]
        metadata = {
            'text': chunk['page_content'],
            'source': chunk['source'],
            'title': chunk['title']
        }
        index.upsert(vectors=[(id, embed, metadata)])
        




