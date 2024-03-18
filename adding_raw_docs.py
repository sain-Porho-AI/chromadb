import chromadb


client = chromadb.Client()
neo_collection = client.create_collection(name="neo")

# Adding raw documents

neo_collection.add(
    documents=["I know kung fu.", "There is no spoon"], ids=["quote_1", "quote_2"],
    )


item_count = neo_collection.count()
print(f"Count of items in collection: {item_count}")

items = neo_collection.get()
print(items)

# Or we can use the peek methos

neo_collection.peek(limit=5)