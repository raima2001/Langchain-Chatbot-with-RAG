from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.interfaces.dto import EasyRAGRequest, EasyIndexRequest

router = APIRouter()


@router.post("/do-an-easy-index", dependencies=[])
async def index_website_controller(request: EasyIndexRequest):
    return JSONResponse(
        content={
            "result": "In future, here will be successful message for indexing a website."
        },
        status_code=200,
    )


@router.post("/do-an-easy-rag", dependencies=[])
async def rag_controller(request: EasyRAGRequest):
    return JSONResponse(
        content={"result": "In future, here will be the answer from RAG."},
        status_code=200,
    )
