import chromadb
from chromadb.utils import embedding_functions
from langchain.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
import os
import shutil
from langchain.vectorstores import Chroma

DATA_PATH = "data/books"
CHROMA_PATH = "chroma"

GOOGLE_API_KEY: str = os.getenv('GOOGLE_API_KEY')  # Load your API key from environment

def main():
    generate_data_store()

def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents


def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=300,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks


def save_to_chroma(chunks: list[Document]):
    # Clear out the database first (optional)
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create a ChromaDB client
    client = chromadb.Client()

    # Create a collection with Google Gemini Pro embeddings
    book_collection = client.create_collection(
        name="book_collection",
        embedding_function=embedding_functions.GoogleGenerativeAiEmbeddingFunction(
            api_key=GOOGLE_API_KEY
        )
    )

    # Generate unique IDs for each chunk
    chunk_ids = [f"chunk_{i}" for i in range(len(chunks))]

    # Add the chunks with their corresponding IDs
    book_collection.add(documents=[chunk.page_content for chunk in chunks], ids=chunk_ids)

    # Persist the collection to ChromaDB
    book_collection.persist(persist_directory=CHROMA_PATH)
    print(f"Saved documents with Google Gemini Pro embeddings to {CHROMA_PATH}")


if __name__ == "__main__":
    main()
