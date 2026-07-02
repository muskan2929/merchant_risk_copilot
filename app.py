import streamlit as st
import sys
sys.path.append(".")
from agent import run_underwriting

st.set_page_config(page_title="Merchant Onboarding Risk Copilot", page_icon="🛡️", layout="centered")

st.title("🛡️ Merchant Onboarding Risk Copilot")
st.caption("AI-powered merchant underwriting assistant — mirrors real payment-processor risk review workflows.")

with st.form("merchant_form"):
    business_name = st.text_input("Business Name", placeholder="e.g. QuickCrypto Trades")
    url = st.text_input("Website URL", placeholder="https://example.com")
    description = st.text_area("Business Description", placeholder="What does this business sell/offer?")
    submitted = st.form_submit_button("Run Underwriting Review")

if submitted:
    if not (business_name and url and description):
        st.warning("Please fill all fields.")
    else:
        with st.spinner("Running underwriting checks..."):
            try:
                result = run_underwriting(business_name, url, description)
                st.success("Review complete")
                st.markdown("### Underwriting Memo")
                st.markdown(result)
            except Exception as e:
                st.error(f"Error: {e}")

st.divider()
st.caption("Built with LangChain + Groq (llama-3.3-70b) + ChromaDB RAG | MVP demo, not production underwriting advice.")
