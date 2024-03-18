import chromadb

# initialize the ChromaDB client
client = chromadb.Client()

neo_collection = client.create_collection(
    name="neo",
)


# inspecting a collection in the ChromaDB
print(neo_collection)

# changing the collectoin name  and inspecting it again
neo_collection.modify(
    name="mr_anderson",
)
print(neo_collection)

# Counting items in a collection 
item_count = neo_collection.count() 
print(f"Count of items in collection: {item_count}")


trinity_collection = client.get_or_create_collection(
    name="trinity", metadata={"hnsw:space": "cosine"},
)

print(trinity_collection)

 # Deleting a collection 
try: 
     client.delete_collection(name="mr_anderson") 
     print("Mr. Anderson collection deleted.") 
except ValueError as e: 
     print(f"Error: {e}") 