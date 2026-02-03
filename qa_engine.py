from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.document_loaders import PyPDFLoader
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def setup_rag_system():
    loader = PyPDFLoader("data/sample.pdf")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    document_chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

    vector_store = FAISS.from_documents(
        document_chunks,
        embeddings
    )

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

    return retriever


async def get_rag_response(query: str):
    retriever = setup_rag_system()

    retrieved_docs = retriever.invoke(query)

    context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    llm = ChatOpenAI(
        api_key=OPENAI_API_KEY,
        temperature=0
    )

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{query}
"""

    response = llm.predict(prompt)

    return {
        "answer": response,
        "sources": [doc.metadata for doc in retrieved_docs]
    }
