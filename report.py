import matplotlib.pyplot as plt
import streamlit as st

def plot_comparison_chart(model1, ratings1, model2, ratings2):
    categories = ["Clarity", "Conciseness", "Accuracy"]
    values1 = [ratings1["clarity"], ratings1["conciseness"], ratings1["accuracy"]]
    values2 = [ratings2["clarity"], ratings2["conciseness"], ratings2["accuracy"]]

    fig, ax = plt.subplots()
    x = range(len(categories))
    ax.bar(x, values1, width=0.4, label=model1, align='center')
    ax.bar([p + 0.4 for p in x], values2, width=0.4, label=model2, align='center')
    ax.set_xticks([p + 0.2 for p in x])
    ax.set_xticklabels(categories)
    ax.set_ylim([0, 5])
    ax.set_ylabel("Score (1-5)")
    ax.set_title("Model Comparison")
    ax.legend()
    st.pyplot(fig)
