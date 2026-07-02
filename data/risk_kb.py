"""
Knowledge base documents for RAG retrieval.
In production this would be RBI MCC risk guidelines, PCI-DSS docs, etc.
For MVP: curated summaries covering real categories used by payment processors.
"""

RISK_KB_DOCS = [
    {
        "id": "mcc_high_risk_1",
        "text": "High-risk merchant category codes (MCC) include: cryptocurrency exchanges (6051), online gambling (7995), pharmaceuticals without license verification (5122), adult content (5967), multi-level marketing (5960), and forex trading (6211). These categories require enhanced due diligence per RBI and card network guidelines due to elevated chargeback rates and regulatory scrutiny."
    },
    {
        "id": "mcc_high_risk_2",
        "text": "Businesses selling weight-loss supplements, CBD products, or subscription-based 'free trial' offers show disproportionately high chargeback rates (often above 1%, which is the Visa/Mastercard risk threshold). Free trial and continuity billing models are flagged because customers frequently forget to cancel and dispute charges."
    },
    {
        "id": "website_legitimacy_1",
        "text": "Legitimate e-commerce merchants typically have: a valid SSL certificate, a physical business address, a working customer support contact (phone or email, not just a contact form), a clear refund/return policy, and a privacy policy compliant with data protection norms. Absence of these on a business's primary domain is a red flag for underwriting review."
    },
    {
        "id": "website_legitimacy_2",
        "text": "Domain age is a meaningful signal: legitimate businesses typically operate on domains older than 6 months. Newly registered domains combined with urgency-driven sales copy (e.g. limited time, act now) are correlated with short-lived fraudulent storefronts, sometimes called 'bust-out' merchants."
    },
    {
        "id": "content_red_flags_1",
        "text": "Red flags in merchant website content include: guaranteed unrealistic returns (common in investment scams), absence of any company registration number, stock images used for 'our team' sections, prices significantly below market rate for branded goods (counterfeit signal), and payment methods restricted to bank transfer or crypto only, avoiding card networks that offer buyer protection."
    },
    {
        "id": "underwriting_process_1",
        "text": "Standard merchant underwriting at payment processors evaluates: business legitimacy (registration, address, digital footprint), MCC category risk tier, expected transaction volume and average ticket size, historical chargeback data if available, and website content compliance. Underwriters typically assign a risk tier: Low, Medium, High, or Decline, with specific documented reasons for the decision, since this decision may be subject to compliance audit."
    },
    {
        "id": "underwriting_process_2",
        "text": "Merchants in Medium or High risk tiers are not automatically rejected; they are typically onboarded with additional controls such as reserve holds on transactions, lower initial transaction limits, or manual review of the first N transactions before full account activation."
    },
]
