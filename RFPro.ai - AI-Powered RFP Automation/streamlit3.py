import streamlit as st
import pandas as pd
import os
from answering import query_rag_with_varag  # Ensure it's using VARAG logic

# Page setup
st.set_page_config(page_title="📜 AI-Powered RFP Chatbot", layout="centered")
st.title("📜 AI-Powered RFP Chatbot")
st.caption("Ask any question — document-based or general. Gemini + VARAG retrieves and answers.")

# Sidebar options
st.sidebar.header("🛠️ Developer Settings")
mode = st.sidebar.radio("Choose input mode:", ["🧠 Type a question", "📁 Select from evaluation list"])
show_chunks = st.sidebar.checkbox("🔍 Show Retrieved Chunks")
show_rephrased = st.sidebar.checkbox("🔁 Show Rephrased Query")
show_prompt = st.sidebar.checkbox("🧾 Show Final Gemini Prompt")

# Path to questions
CSV_PATH = r"E:\Capstone\rag_answers_output2.csv"

# Load evaluation questions
if mode == "📁 Select from evaluation list":
    try:
        df = pd.read_csv(CSV_PATH)
        questions = df["Question"].dropna().tolist()
        selected_question = st.selectbox("📋 Choose a question:", questions)
        user_query = selected_question
    except Exception as e:
        st.error(f"⚠️ Failed to load CSV: {e}")
        user_query = ""
else:
    user_query = st.text_input("💬 Type your question:")

# Ask button
if st.button("🚀 Ask AI") and user_query.strip():
    with st.spinner("🔍 Thinking..."):
        answer, images, debug_info = query_rag_with_varag(user_query, return_debug=True)

    st.subheader("🤖 Answer")
    st.write(answer)

    # Optional: Debugging info
    if show_rephrased and debug_info.get("rephrased"):
        st.markdown("### 🔁 Rephrased Query")
        st.code(debug_info["rephrased"])

    if show_chunks and debug_info.get("chunks"):
        st.markdown("### 🧩 Retrieved Chunks")
        for i, chunk in enumerate(debug_info["chunks"]):
            st.code(f"Chunk {i+1}:\n{chunk}")

    if show_prompt and debug_info.get("prompt"):
        st.markdown("### 🧾 Final Prompt Sent to Gemini")
        st.code(debug_info["prompt"])

    if images:
        st.subheader("🖼️ Supporting Images")
        for img in images:
            if os.path.exists(img):
                st.image(img, use_column_width=True)
            else:
                st.warning(f"⚠️ Missing image: {img}")
