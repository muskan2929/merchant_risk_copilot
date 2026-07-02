import chromadb
from chromadb.utils import embedding_functions
from merchant_risk_copilot.data.risk_kb import RISK_KB_DOCS

class RiskKnowledgeRetriever:
    def __init__(self):
        self.client = chromadb.Client()
        self.embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        self.collection = self.client.create_collection(
            name="merchant_risk_kb",
            embedding_function=self.embed_fn
        )
        self._load_docs()

    def _load_docs(self):
        self.collection.add(
            documents=[d["text"] for d in RISK_KB_DOCS],
            ids=[d["id"] for d in RISK_KB_DOCS]
        )

    def retrieve(self, query: str, k: int = 3):
        results = self.collection.query(query_texts=[query], n_results=k)
        return results["documents"][0]

retriever = RiskKnowledgeRetriever()
