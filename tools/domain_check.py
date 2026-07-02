import whois
from datetime import datetime

def check_domain_age(url: str) -> dict:
    """Checks domain registration age via WHOIS."""
    from urllib.parse import urlparse
    try:
        hostname = urlparse(url if url.startswith("http") else f"https://{url}").hostname
        w = whois.whois(hostname)
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if creation_date:
            age_days = (datetime.now() - creation_date).days
            return {"domain_age_days": age_days, "creation_date": str(creation_date), "error": None}
        return {"domain_age_days": None, "error": "No creation date found"}
    except Exception as e:
        return {"domain_age_days": None, "error": str(e)}
