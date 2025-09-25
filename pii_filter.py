import re
from typing import List, Tuple

# Patterns for common PII
EMAIL_RE = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
PHONE_RE = re.compile(r"(?:\+\d{1,3}[\s-]?)?(?:\d{2,4}[\s-]?){2,4}\d{2,4}")
# Very simple address heuristics (US-centric fragment). Tweak per locale.
ADDRESS_RE = re.compile(r"\d{1,5}\s+\w+\s+(Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr)\b", re.IGNORECASE)

PII_PATTERNS = [("email", EMAIL_RE), ("phone", PHONE_RE), ("address", ADDRESS_RE)]


def detect_pii(text: str) -> List[Tuple[str, str]]:
    """Return list of (type, match) found in text."""
    found = []
    for name, pat in PII_PATTERNS:
        for m in pat.finditer(text):
            found.append((name, m.group(0)))
    return found


def contains_pii(text: str) -> bool:
    return len(detect_pii(text)) > 0


if __name__ == '__main__':
    sample = "Contact me at john.doe@example.com or call +1 415-555-1234."
    print(detect_pii(sample))
