### ✅ `README.md`

# 🤖 Battle of the LLMs: Summarizer Showdown

An interactive Streamlit web app that lets users compare the summarization capabilities of closed-source and open-source Large Language Models (LLMs). Choose two different models, input long-form text (article/blog/transcript), and compare the summaries side-by-side. Rate each model on clarity, accuracy, and conciseness — and decide which one you prefer!

---

## 🔧 Features

- ✅ Choose from popular LLMs (OpenAI GPT-4, GPT-3.5, BART, Pegasus, Mixtral)
- ✅ Input or upload long-form text (~500–1000 words)
- ✅ Generate summaries from both selected models
- ✅ Side-by-side comparison of summaries
- ✅ Rate each model on:
  - Clarity
  - Conciseness
  - Correctness
- ✅ Visual report card with model-wise ratings

## 🧠 Models Used

### 🔐 Closed-Source (via OpenAI API)
- `gpt-3.5-turbo`
- `gpt-4-mini`

### 🌐 Open-Source (via Hugging Face Inference API)
- `facebook/bart-large-cnn`
- `google/pegasus-xsum`
- `mistralai/Mixtral-8x7B-Instruct-v0.1` *(optional)*

---

## 📁 Folder Structure

```

Battle-of-LLM/
├── app.py               # Streamlit main app
├── summarize.py         # Handles LLM summarization
├── ratings.py           # Renders rating form & logic
├── text.py              # Sample article input
├── requirements.txt
└── README.md

````

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/vaibhavi1224/Battle-of-LLM.git
cd Battle-of_LLM
````

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Keys

You'll need:

1. **OpenAI API Key** — for GPT-3.5 / GPT-4
2. **Hugging Face API Token** — for using open-source models via HF Inference API

You can either:

* Put your keys directly in `summarize.py` (not recommended for production), or
* Create a `.env` file like this:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
HF_API_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

And update the code to load from `os.environ`.

---

## 🚀 Run the App

```bash
streamlit run app.py
```

Then open your browser:
📍 `http://localhost:8501`

---

## 📸 Screenshots

![image](https://github.com/user-attachments/assets/9234bc91-dcda-4147-aac2-7f4fb862c308)


## ✅ To Do

* [ ] Save user ratings to backend
* [ ] Add more summarization models
* [ ] Export comparison results as PDF/CSV

---

## 🛡️ License

MIT License

---

## 🤝 Contributors

* Vaibhavi Kapse — [@vaibhavi1224](https://github.com/vaibhavi1224)

