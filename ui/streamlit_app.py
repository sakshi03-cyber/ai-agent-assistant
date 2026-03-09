import streamlit as st
import requests
import os
import re   # added

st.title("AI Agent Assistant")
st.write("Ask anything from documents, math, or the web.")
st.write("Upload a PDF and ask questions about it.")

os.makedirs("data", exist_ok=True)

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

save_path = None

if uploaded_file is not None:

    # sanitize filename (ONLY FIX)
    safe_name = re.sub(r"[^\w_.-]", "_", uploaded_file.name)

    save_path = os.path.abspath(f"data/{safe_name}")
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully!")

    if st.button("Process PDF"):

        response = requests.post(
            "http://127.0.0.1:8000/upload_pdf",
            params={"file_path": save_path}
        )

        if response.status_code == 200:
            st.success("PDF processed and stored in knowledge base.")
        else:
            st.error("Error processing PDF.")

st.divider()

question = st.text_input("Enter your question:")

if st.button("Ask Agent"):

    if question:

        response = requests.post(
            "http://127.0.0.1:8000/ask",
            params={"question": question}
        )

        data = response.json()

        st.write("**Answer:**")
        st.write(data["answer"])

        if "tool" in data:
            st.write("### Tool Used")
            st.write(data["tool"])