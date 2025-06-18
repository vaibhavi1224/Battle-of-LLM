import streamlit as st
from summarize import summarize_text
from ratings import display_rating_form
from report import plot_comparison_chart
from text import SAMPLE_ARTICLE

st.set_page_config("LLM Summarizer Showdown", layout="wide")

st.title("🤖 Battle of the LLMs: Summarizer Showdown")
st.write("Compare summaries from open-source and closed-source LLMs. Rate and decide the winner!")

# --- Model Selection ---
col1, col2 = st.columns(2)
with col1:
    closed_model = st.selectbox("🔐 Closed-source LLM", ["gpt-3.5-turbo", "gpt-4o-mini"])
with col2:
    open_model = st.selectbox("🛠️ Open-source LLM", ["facebook/bart-large-cnn", "google/pegasus-xsum", "mistralai/Mixtral"])

# --- Text Input ---
text_input = st.text_area("📄 Paste or edit article below:", SAMPLE_ARTICLE, height=300)

# --- Compare Button ---
if st.button("Compare Summaries"):
    with st.spinner("⏳ Generating summaries..."):
        closed_summary = summarize_text(text_input, closed_model, closed=True)
        open_summary = summarize_text(text_input, open_model, closed=False)

    st.markdown("### 🔍 Side-by-Side Summaries")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"{closed_model}")
        st.write(closed_summary)
    with col2:
        st.subheader(f"{open_model}")
        st.write(open_summary)

    st.markdown("---")
    st.markdown("### 🗳️ Rate Each Model")
    closed_ratings = display_rating_form(closed_model)
    open_ratings = display_rating_form(open_model)

    st.markdown("### 📊 Results")
    plot_comparison_chart(closed_model, closed_ratings, open_model, open_ratings)
