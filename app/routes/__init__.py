from fastapi import APIRouter
from .easy_rag import easy_rag

router = APIRouter(dependencies=[])

"""
Here we can insert all the routers in the application.
"""

router.include_router(easy_rag.router, prefix="/easy_rag")
