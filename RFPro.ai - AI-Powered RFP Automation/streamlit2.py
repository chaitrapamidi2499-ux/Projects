import streamlit as st
import os
from answering import query_rag_with_varag  # ✅ Uses VARAG logic from answering.py

# ✅ Streamlit UI Setup
st.set_page_config(page_title="📜 RFP Chatbot", layout="centered")
st.title("📜 AI-Powered RFP Chatbot")
st.caption("Ask questions from your RFP PDFs (text, tables, images, OCR). Answers are grounded in documents only.")

# ✅ Ask a question
user_query = st.text_input("🔹 Ask a question:")

if st.button("Ask AI") and user_query.strip():
    with st.spinner("💡 Thinking..."):
        answer, images = query_rag_with_varag(user_query)

        # ✅ Show the answer
        st.subheader("🤖 Gemini Answer")
        st.write(answer)

        # ✅ Show retrieved images
        if images:
            st.subheader("🖼️ Supporting Images")
            for img in images:
                if os.path.exists(img):
                    st.image(img, use_column_width=True)
                else:
                    st.warning(f"⚠️ Missing image: {img}")

# ✅ Optional debug toggle
with st.expander("🛠 Debug Info"):
    st.markdown("- This version uses Gemini + Reranked Retrieval (VARAG)")
    st.markdown("- If you get 'Not enough information', try more specific phrasing.")
