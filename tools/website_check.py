import requests
from bs4 import BeautifulSoup
import ssl
import socket
from urllib.parse import urlparse

def check_website_legitimacy(url: str) -> dict:
    """Checks SSL, contact info, policy pages on a merchant website."""
    result = {"url": url, "has_ssl": False, "has_contact": False,
              "has_privacy_policy": False, "has_refund_policy": False, "error": None}
    try:
        parsed = urlparse(url if url.startswith("http") else f"https://{url}")
        hostname = parsed.hostname

        # SSL check
        try:
            ctx = ssl.create_default_context()
            with socket.create_connection((hostname, 443), timeout=5) as sock:
                with ctx.wrap_socket(sock, server_hostname=hostname) as ssock:
                    result["has_ssl"] = True
        except Exception:
            result["has_ssl"] = False

        # Content check
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        text = soup.get_text().lower()

        result["has_contact"] = any(k in text for k in ["contact us", "support@", "customer care", "helpline"])
        result["has_privacy_policy"] = "privacy policy" in text
        result["has_refund_policy"] = any(k in text for k in ["refund policy", "return policy"])
        result["page_title"] = soup.title.string if soup.title else "N/A"

    except Exception as e:
        result["error"] = str(e)

    return result
