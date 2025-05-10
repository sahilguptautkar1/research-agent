from bs4 import BeautifulSoup
import httpx
import re

async def extract_profiles(urls):
    results = []
    async with httpx.AsyncClient(timeout=10) as client:
        for url in urls:
            try:
                r = await client.get(url)
                soup = BeautifulSoup(r.text, "lxml")
                text = soup.get_text()
                results.append({
                    "name": soup.title.string if soup.title else None,
                    "website": url,
                    "city": extract_city(text),
                    "state": extract_state(text),
                    "email": parse_email(text),
                    "phone_number": parse_phone(text),
                    "bond_amount": parse_bond(text),
                    "tx_projects_past_5yrs": count_tx_projects(text),
                    "evidence_url": url,
                    "evidence_text": extract_evidence(text),
                })
            except Exception as e:
                print(f"Error scraping {url}: {e}")
                continue
    return results

def parse_bond(text):
    match = re.search(r"bond(ed)? (up to )?\$?([0-9,.]+)( million)?", text, re.I)
    if match:
        number = match.group(3).replace(",", "")
        try:
            amount = float(number)
            return int(amount * 1_000_000 if match.group(4) else amount)
        except ValueError:
            return 0
    return 0

def parse_phone(text):
    match = re.search(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text)
    return match.group(0) if match else None

def parse_email(text):
    match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match.group(0) if match else None

def extract_city(text):
    return "Austin" if "Austin" in text else None

def extract_state(text):
    return "TX" if "Texas" in text or "Austin, TX" in text else None

def extract_evidence(text):
    return next((line for line in text.split('\n') if 'bonded' in line.lower()), "")

def count_tx_projects(text):
    return len(re.findall(r"(Austin|Texas).*?20[1-2][0-9]", text, re.I))