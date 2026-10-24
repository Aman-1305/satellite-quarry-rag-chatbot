import chromadb


client = chromadb.PersistentClient(path="chroma_db")


collection = client.get_or_create_collection(
    name="satellite_documents"
)


def add_document(chunk, embedding, chunk_id):
    collection.add(
        ids=[chunk_id],
        documents=[chunk],
        embeddings=[embedding]
    )


def search_documents(query_embedding, n_results=3):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results


if __name__ == "__main__":
    print("ChromaDB is working!")
    print("Collection:", collection.name)