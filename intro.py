import chromadb


# Initailize  the ChromaDB clinet
client = chromadb.Client()


# Test if the service is up and running 
print(client.heartbeat())