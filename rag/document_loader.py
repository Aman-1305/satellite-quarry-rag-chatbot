from pathlib import Path


DOCUMENTS_PATH = Path("data/documents")


def load_documents():
    documents = []

    for file_path in DOCUMENTS_PATH.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        documents.append({
            "filename": file_path.name,
            "text": text
        })

    return documents


if __name__ == "__main__":
    documents = load_documents()

    print(f"Loaded {len(documents)} document(s)")

    for document in documents:
        print("\n---", document["filename"], "---")
        print(document["text"][:500])