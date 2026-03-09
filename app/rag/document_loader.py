from langchain_community.document_loaders import PyPDFLoader
from app.utils.logger import logger

def load_pdf(file_path: str):

    logger.info(f"Loading PDF: {file_path}")

    try:

        loader = PyPDFLoader(file_path)

        documents = loader.load()

        logger.info(f"Loaded {len(documents)} pages")

        return documents

    except Exception as e:

        logger.error(f"Error loading PDF: {e}")

        return []

if __name__ == "__main__":

    docs = load_pdf("data/sample-report.pdf")

    print(f"Total pages loaded: {len(docs)}")

    print(docs[0].page_content[:500])