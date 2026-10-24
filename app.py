import streamlit as st
from chatbot.llm import ask_llm

st.set_page_config(
    page_title="Quarry Satellite RAG Chatbot",
    page_icon="🛰️",
    layout="centered"
)

st.title("🛰️ Quarry Satellite RAG Chatbot")
st.write(
    "Ask questions about stone quarry detection, "
    "satellite imagery, Sentinel-2 bands, NDVI and change detection."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask about quarry satellite detection...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching knowledge base and generating answer..."):
            try:
                answer = ask_llm(question)
                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })
            except Exception as e:
                st.error(f"Something went wrong: {e}")