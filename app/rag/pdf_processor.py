import fitz  # PyMuPDF
import os
from app.utils.logger import logger
import camelot
from langchain_core.documents import Document


def extract_images(pdf_path, output_folder="data/images"):

    os.makedirs(output_folder, exist_ok=True)

    doc = fitz.open(pdf_path)

    image_paths = []

    for page_index in range(len(doc)):

        page = doc.load_page(page_index)

        images = page.get_images(full=True)

        for img_index, img in enumerate(images):

            xref = img[0]
            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            image_name = f"page{page_index+1}_img{img_index}.{image_ext}"

            image_path = os.path.join(output_folder, image_name)

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(image_path)

    logger.info(f"Extracted {len(image_paths)} images")

    return image_paths


def extract_tables(pdf_path):

    tables = camelot.read_pdf(pdf_path, pages="all", flavor="stream")

    table_data = []

    for table in tables:
        table_data.append(table.df.to_markdown())

    return table_data


def tables_to_documents(tables):

    docs = []

    for table in tables:

        docs.append(
            Document(
                page_content=table,
                metadata={"source": "table"}
            )
        )

    return docs
