from langchain_groq import ChatGroq
from langchain_classic.agents import (
    create_tool_calling_agent,
    AgentExecutor,
)
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate
import requests

from merchant_risk_copilot.tools.website_check import check_website_legitimacy
from merchant_risk_copilot.tools.domain_check import check_domain_age
from merchant_risk_copilot.tools.category_risk import check_business_category_risk
from merchant_risk_copilot.tools.content_flags import check_content_red_flags
from merchant_risk_copilot.tools.rag_retriever import retriever

@tool
def website_legitimacy_tool(url: str) -> dict:
    """Check if a merchant website has SSL, contact info, and policy pages."""
    return check_website_legitimacy(url)

@tool
def domain_age_tool(url: str) -> dict:
    """Check how old the merchant's domain is via WHOIS."""
    return check_domain_age(url)

@tool
def category_risk_tool(business_description: str) -> dict:
    """Check if the business category is high-risk (crypto, gambling, pharma, etc)."""
    return check_business_category_risk(business_description)

@tool
def content_red_flags_tool(url: str) -> dict:
    """Scrape website text and check for scam-pattern language."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        from bs4 import BeautifulSoup
        text = BeautifulSoup(resp.text, "html.parser").get_text()
        return check_content_red_flags(text)
    except Exception as e:
        return {"error": str(e)}

@tool
def retrieve_underwriting_guidelines(query: str) -> str:
    """Retrieve relevant underwriting/risk guidelines from the knowledge base."""
    docs = retriever.retrieve(query, k=3)
    return "\n\n".join(docs)

TOOLS = [website_legitimacy_tool, domain_age_tool, category_risk_tool,
         content_red_flags_tool, retrieve_underwriting_guidelines]

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

SYSTEM_PROMPT = """You are a senior merchant underwriting analyst at a payment processing company (like Razorpay/Stripe).
Given a merchant's business name, website URL, and business description, you must:
1. Use the tools to check website legitimacy, domain age, category risk, and content red flags.
2. Retrieve relevant underwriting guidelines from the knowledge base to justify your reasoning.
3. Produce a structured underwriting memo with:
   - Merchant Name
   - Risk Tier (Low / Medium / High / Decline)
   - Key Findings (bullet points, each citing which tool/check supports it)
   - Recommended Action (approve / approve with reserve hold / manual review / decline)
Be specific and cite the guideline you retrieved when justifying the risk tier."""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, TOOLS, prompt)
agent_executor = AgentExecutor(agent=agent, tools=TOOLS, verbose=True)

def run_underwriting(business_name: str, url: str, description: str) -> str:
    input_text = f"Business Name: {business_name}\nWebsite: {url}\nDescription: {description}"
    result = agent_executor.invoke({"input": input_text})
    return result["output"]
