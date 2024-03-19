import chromadb
from chromadb.utils import embedding_functions
import os
from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY: str = os.getenv('GOOGLE_API_KEY')
import google.generativeai as genai
genai.configure(api_key=GOOGLE_API_KEY)


# client = chromadb.Client()


# openai_ef = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
#     api_key=GOOGLE_API_KEY
# )
# # Create the collection with the OpenAI embedding function
# matrix_collection = client.create_collection(
#     name="matrix",
#     embedding_function=openai_ef,
# )

# # Add the raw documents
# matrix_collection.add(
#     documents=[
#         "The Matrix is all around us.",
#         "What you know you can't explain, but you feel it",
#         "There is a difference between knowing the path and walking the path",
#     ],
#     ids=["quote_1", "quote_2", "quote_3"],
# )

# # Querying by a set of query_texts
# results = matrix_collection.query(query_texts=["What is the Matrix?"], n_results=2,)

# print(results)



import chromadb
from chromadb.utils import embedding_functions
import os
from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY: str = os.getenv('GOOGLE_API_KEY')
import google.generativeai as genai
genai.configure(api_key=GOOGLE_API_KEY)


client = chromadb.Client()


def create_embedding_from_file(file_path, collection_name):
  """
  Reads a text file and creates embeddings for each line, adding them to the collection.
  """
  openai_ef = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
      api_key=GOOGLE_API_KEY
  )
  # Create the collection with the OpenAI embedding function
  matrix_collection = client.create_collection(
      name=collection_name,
      embedding_function=openai_ef
  )

  # Read the book content line by line
  with open(file_path, 'r') as book_file:
    for line_number, line in enumerate(book_file):
      # Skip empty lines
      if not line.strip():
        continue
      document_id = f"line_{line_number}"  # Create unique ID for each line
      matrix_collection.add(
          documents=[line],
          ids=[document_id]
      )

  print(f"Embeddings for book.md saved to collection: {collection_name}")


# Specify the path to your book.md file and desired collection name
book_path = "book.md"
collection_name = "book_embeddings"

create_embedding_from_file(book_path, collection_name)

# This part remains unchanged for querying (optional)
# results = matrix_collection.query(query_texts=["What is the Matrix?"], n_results=2,)
# print(results)
