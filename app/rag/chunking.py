from langchain_text_splitters import RecursiveCharacterTextSplitter 
from app.utils.logger import logger 

def chunk_documents(docs):

    logger.info("Starting document chunking")

    try:

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

        chunks = splitter.split_documents(docs)

        logger.info(f"Created {len(chunks)} chunks")

        return chunks

    except Exception as e:

        logger.error(f"Chunking error: {e}")

        return []
    
    
if __name__ == "__main__":

    from app.rag.document_loader import load_pdf

    docs = load_pdf("data/sample-report.pdf")

    chunks = chunk_documents(docs)

    print(f"Total chunks: {len(chunks)}")

    print(chunks[0].page_content[:300])