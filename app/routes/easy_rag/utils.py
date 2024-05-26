from app.routes.easy_rag.setup.chunk_and_upsert import embed_and_upsert_website
from app.routes.easy_rag.rag_pipeline import initialize_qa_system, ask_question


async def easy_index_utils(website: str):
        embed_and_upsert_website(website)
        return "Upserted Successfully!"
        

async def easy_rag_utils(query: str):
    initialize_qa_system()
    response = ask_question(query)
    return response.get("result")
