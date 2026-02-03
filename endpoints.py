from fastapi import APIRouter, HTTPException
from qa_engine import get_rag_response

router = APIRouter()

@router.get("/query/")
async def query_rag_system(query: str):
    try:
        # Call the RAG system to process the query and get a response
        response = await get_rag_response(query)
        if "error" in response:
            return response

        return {
    "query": query,
    "answer": response["answer"],
    "sources": response["sources"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

