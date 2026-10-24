from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(text):
    embedding = model.encode(text)

    return embedding


if __name__ == "__main__":

    text = "NDVI is used to analyze vegetation health."

    embedding = create_embedding(text)

    print("Embedding created successfully!")
    print("Vector size:", len(embedding))
    print("First 10 values:", embedding[:10])