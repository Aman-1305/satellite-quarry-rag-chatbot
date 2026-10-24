def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


if __name__ == "__main__":

    sample_text = """
    NDVI stands for Normalized Difference Vegetation Index.
    It is commonly used in satellite image processing to analyze vegetation health.
    NDVI uses Near Infrared and Red bands.
    """

    chunks = chunk_text(sample_text)

    print(f"Number of chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i + 1} ---")
        print(chunk)