from fastapi import APIRouter
from app.agent_controller import run_agent
from loguru import logger 
from app.rag.chunking import chunk_documents
from app.rag.document_loader import load_pdf
from app.rag.vector_store import store_documents
router = APIRouter() 


@router.post("/upload_pdf")
def upload_pdf(file_path: str):

    logger.info(f"File path received: {file_path}")

    docs = load_pdf(file_path)
    logger.info(f"Docs loaded: {len(docs)}")

    chunks = chunk_documents(docs)
    logger.info(f"Chunks created: {len(chunks)}")

    store_documents(chunks)

    return {"message": "PDF ingested successfully"}
@router.post("/ask")
def ask_agent(question: str):

    
    logger.info(f"Received question: {question}")

    try:

        answer = run_agent(question)

        return {
            "question": question,
            "answer": answer
        }

    except Exception as e:

        logger.error(f"API error: {e}")

        return {
            "error": "Something went wrong"
        }