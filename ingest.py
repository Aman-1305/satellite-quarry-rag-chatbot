from rag.document_loader import load_documents
from rag.chunker import chunk_text
from rag.embeddings import create_embedding
from rag.vector_db import add_document


documents = load_documents()

print(f"Loaded {len(documents)} document(s)")

chunk_count = 0


for document in documents:

    chunks = chunk_text(document["text"])

    print(f"\nProcessing: {document['filename']}")
    print(f"Created {len(chunks)} chunk(s)")

    for i, chunk in enumerate(chunks):

        embedding = create_embedding(chunk)

        chunk_id = f"{document['filename']}_{i}"

        add_document(
            chunk=chunk,
            embedding=embedding,
            chunk_id=chunk_id
        )

        chunk_count += 1


print(f"\nSuccessfully stored {chunk_count} chunk(s) in ChromaDB!")