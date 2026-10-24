import ollama

from rag.retriever import retrieve


def ask_llm(question):

    results = retrieve(question, n_results=3)

    context = "\n\n".join(results["documents"][0])

    prompt = f"""
You are a helpful satellite image analysis assistant.

Answer the user's question using the context provided below.

Context:
{context}

User Question:
{question}

Answer clearly and concisely.
"""

    response = ollama.chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":

    print("Satellite RAG Chatbot")
    print("Type 'exit' to stop.\n")

    while True:

        question = input("You: ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        answer = ask_llm(question)

        print("\nAI:", answer)
        print()