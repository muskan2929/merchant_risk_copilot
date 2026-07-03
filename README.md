# 🛡️ Merchant Onboarding Risk Copilot

An AI-powered underwriting assistant that automates merchant risk screening for online businesses. It uses a LangChain tool-calling agent with RAG to analyze merchant websites, retrieve underwriting guidelines, and generate a structured risk assessment.

🔗 **Live Demo:** https://huggingface.co/spaces/muskan2929/merchant-risk-copilot

---

## Why I Built This

Payment companies manually verify merchants before allowing them to accept payments. This project explores how AI agents can automate that workflow by combining multiple tools with Retrieval-Augmented Generation (RAG).

---

## Features

- Website legitimacy checks
- Domain age verification
- Business category risk detection
- Scam-language detection
- RAG-based underwriting guideline retrieval
- Structured underwriting report

---

## Tech Stack

- **Python**
- **LangChain**
- **Groq (Llama 3.3 70B)**
- **ChromaDB**
- **Sentence Transformers**
- **BeautifulSoup**
- **python-whois**
- **Streamlit**
- **Docker**
- **Hugging Face Spaces**

---

## Project Structure

```text
merchant-risk-copilot/
├── src/
│   ├── app.py
│   ├── agent.py
│   ├── tools/
│   ├── data/
│   └── eval/
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Run Locally

```bash
git clone https://github.com/muskan2929/merchant-risk-copilot.git
cd merchant-risk-copilot

pip install -r requirements.txt

# Linux/Mac
export GROQ_API_KEY="your_api_key"

# Windows PowerShell
$env:GROQ_API_KEY="your_api_key"

streamlit run src/app.py
```

---

## RAG Evaluation

Run the evaluation script:

```bash
python -m src.eval.rag_eval
```

It measures:
- Precision@k
- Faithfulness

---

## Future Improvements

- Threat intelligence APIs
- Batch merchant screening
- Improved risk scoring
- Fine-tuned category classifier

---

## Disclaimer

This project is an educational MVP created to demonstrate Agentic AI and RAG for merchant underwriting. It is not intended for production risk decisions.

---

## Author

**Muskan Bishnoi**

