HIGH_RISK_KEYWORDS = {
    "crypto": "cryptocurrency/forex trading",
    "forex": "cryptocurrency/forex trading",
    "gambling": "online gambling",
    "casino": "online gambling",
    "bet": "online gambling",
    "pharma": "pharmaceuticals",
    "supplement": "weight-loss/supplements",
    "cbd": "CBD/supplements",
    "adult": "adult content",
    "mlm": "multi-level marketing",
    "investment": "investment/guaranteed returns",
    "loan": "lending/credit",
}

def check_business_category_risk(business_description: str) -> dict:
    """Maps business description to known high-risk MCC categories."""
    desc_lower = business_description.lower()
    matched = [v for k, v in HIGH_RISK_KEYWORDS.items() if k in desc_lower]
    risk_tier = "High" if matched else "Standard"
    return {"matched_categories": list(set(matched)), "risk_tier": risk_tier}
