import streamlit as st

def display_rating_form(model_name):
    st.subheader(f"Ratings for {model_name}")
    clarity = st.slider(f"Clarity ({model_name})", 1, 5, 3)
    conciseness = st.slider(f"Conciseness ({model_name})", 1, 5, 3)
    accuracy = st.slider(f"Accuracy ({model_name})", 1, 5, 3)
    preference = st.radio(f"Preferred Summary?", [model_name, "Other"], key=model_name)
    return {
        "clarity": clarity,
        "conciseness": conciseness,
        "accuracy": accuracy,
        "preferred": preference
    }
