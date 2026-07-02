RED_FLAG_PHRASES = [
    "guaranteed returns", "risk free", "double your money", "act now",
    "limited time offer", "no questions asked refund", "bank transfer only",
    "crypto only", "wire transfer only"
]

def check_content_red_flags(page_text: str) -> dict:
    """Scans scraped page text for scam-pattern language."""
    text_lower = page_text.lower()
    found = [p for p in RED_FLAG_PHRASES if p in text_lower]
    return {"red_flags_found": found, "flag_count": len(found)}
