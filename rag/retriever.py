from rag.embeddings import create_embedding
from rag.vector_db import search_documents


def retrieve(query, n_results=3):

    query_embedding = create_embedding(query)

    results = search_documents(
        query_embedding=query_embedding,
        n_results=n_results
    )

    return results


if __name__ == "__main__":

    query = "What is NDVI?"

    results = retrieve(query, n_results=3)

    print("\nRetrieved documents:")

    for document in results["documents"][0]:
        print("\n---")
        print(document)