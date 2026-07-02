"""
RAG Evaluation: measures retrieval relevance against a labeled test set.
Metrics: Retrieval Precision@k, and LLM-judged Faithfulness.
"""
import sys
sys.path.append("/content")
from merchant_risk_copilot.tools.rag_retriever import retriever
from langchain_groq import ChatGroq

# Labeled test set: query -> expected relevant doc id(s)
TEST_SET = [
    {"query": "Is a crypto exchange considered high risk?", "expected_ids": ["mcc_high_risk_1"]},
    {"query": "What subscription business models cause chargebacks?", "expected_ids": ["mcc_high_risk_2"]},
    {"query": "What does a legitimate merchant website need?", "expected_ids": ["website_legitimacy_1"]},
    {"query": "Is a newly registered domain risky?", "expected_ids": ["website_legitimacy_2"]},
    {"query": "What are common scam signals in website content?", "expected_ids": ["content_red_flags_1"]},
    {"query": "What risk tiers does underwriting use?", "expected_ids": ["underwriting_process_1"]},
    {"query": "Can medium risk merchants still be onboarded?", "expected_ids": ["underwriting_process_2"]},
]

from merchant_risk_copilot.data.risk_kb import RISK_KB_DOCS
ID_TO_TEXT = {d["id"]: d["text"] for d in RISK_KB_DOCS}

def evaluate_retrieval_precision(k=3):
    """Checks if the expected doc appears in top-k retrieved results."""
    hits = 0
    for item in TEST_SET:
        retrieved_texts = retriever.retrieve(item["query"], k=k)
        expected_texts = [ID_TO_TEXT[i] for i in item["expected_ids"]]
        hit = any(exp in retrieved_texts for exp in expected_texts)
        hits += int(hit)
        print(f"Query: {item['query'][:50]}... | Hit: {hit}")
    precision = hits / len(TEST_SET)
    print(f"\nRetrieval Precision@{k}: {precision:.2f}")
    return precision

def evaluate_faithfulness_llm_judge():
    """Uses LLM-as-judge to check if retrieved context actually supports a generated answer."""
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
    scores = []
    for item in TEST_SET:
        context = "\n".join(retriever.retrieve(item["query"], k=3))
        judge_prompt = f"""Context: {context}

Question: {item['query']}

Does the context contain sufficient information to answer this question faithfully?
Answer with only one word: YES or NO."""
        response = llm.invoke(judge_prompt).content.strip().upper()
        is_faithful = "YES" in response
        scores.append(int(is_faithful))
        print(f"Query: {item['query'][:50]}... | Faithful: {is_faithful}")
    faithfulness_score = sum(scores) / len(scores)
    print(f"\nFaithfulness Score: {faithfulness_score:.2f}")
    return faithfulness_score

if __name__ == "__main__":
    print("=== Retrieval Precision Eval ===")
    evaluate_retrieval_precision()
    print("\n=== Faithfulness Eval ===")
    evaluate_faithfulness_llm_judge()
