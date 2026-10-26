import re
from urllib.parse import urlparse

SUSPICIOUS_WORDS = ["login", "verify", "update", "secure",
                    "account", "bank", "confirm", "password"]


def extract_features(url):
    if not url.startswith(("http://", "https://")):
        url = "http://" + url
    parsed = urlparse(url)
    host = parsed.hostname or ""

    return {
        "url_length": len(url),
        "dot_count": host.count("."),
        "hyphen_count": host.count("-"),
        "has_at_symbol": "@" in url,
        "has_ip_address": bool(re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}", host)),
        "uses_https": parsed.scheme == "https",
        "digit_count": sum(c.isdigit() for c in url),
        "suspicious_words": sum(w in url.lower() for w in SUSPICIOUS_WORDS),
    }


def risk_score(f):
    score = 0
    if f["url_length"] > 75:
        score += 1
    if f["dot_count"] > 3:
        score += 1
    if f["hyphen_count"] > 1:
        score += 1
    if f["has_at_symbol"]:
        score += 2
    if f["has_ip_address"]:
        score += 2
    if not f["uses_https"]:
        score += 1
    if f["digit_count"] > 8:
        score += 1
    score += min(f["suspicious_words"], 3)
    return score


def verdict(score):
    if score >= 6:
        return "HIGH RISK"
    if score >= 3:
        return "SUSPICIOUS"
    return "LOOKS OK"


print("URL Risk Checker (type q to quit)")

while True:
    url = input("\nEnter a URL: ").strip()
    if url.lower() == "q":
        print("Goodbye!")
        break
    if not url:
        continue

    features = extract_features(url)
    for name, value in features.items():
        print(f"  {name}: {value}")

    score = risk_score(features)
    print(f"Risk score: {score} -> {verdict(score)}")
