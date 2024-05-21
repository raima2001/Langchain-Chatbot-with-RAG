from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.interfaces.dto import EasyIndexRequest, EasyRAGRequest
from app.routes.easy_rag.utils import easy_index_utils, easy_rag_utils

router = APIRouter()

@router.post("/do-an-easy-index", dependencies=[])
async def index_website_controller(request: EasyIndexRequest):
    result = await easy_index_utils('https://www.syllotips.com/')
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return JSONResponse(content=result, status_code=200)




@router.post("/do-an-easy-rag", dependencies=[])
async def rag_controller(request: EasyRAGRequest):
    query = request.query  
    try:
        result = await easy_rag_utils(query)
        return JSONResponse(content=result, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))