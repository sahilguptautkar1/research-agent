# Research Agent (FastAPI + Web Scraping)

A web-based research agent that helps preconstruction teams identify and rank subcontractors based on trade, location, bonding capacity, and project history — using real-time internet scraping and license validation.

Live Demo (Loom): https://www.loom.com/share/450f5f14b6694e429e6f0e81b21197f1

Hosted Link: https://research-agent-cjai.onrender.com

---

## Features

- Accepts structured research requests
- Scrapes real contractor websites
- Validates license status via TDLR
- Scores candidates on relevance and experience
- Returns ranked JSON results with source evidence

---

## Getting Started Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/research-agent.git
cd research-agent
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash
uvicorn main:app --reload
```

Visit: http://localhost:8000/docs

---

## API Usage

### POST /research-jobs

Send a JSON request like:

```json
{
  "trade": "mechanical",
  "city": "Austin",
  "state": "TX",
  "min_bond": 5000000,
  "keywords": ["hotel", "commercial"]
}
```

Response:

```json
{ "job_id": "abc1234-uuid" }
```

---

### GET /research-jobs/{job_id}

- While processing:

```json
{ "status": "RUNNING" }
```

- When finished:

```json
{
  "status": "SUCCEEDED",
  "results": [
    {
      "name": "XYZ Mechanical Contractors",
      "website": "https://xyzmech.com",
      "city": "Austin",
      "state": "TX",
      "lic_active": true,
      "lic_number": "TX12345678",
      "bond_amount": 6000000,
      "tx_projects_past_5yrs": 4,
      "score": 92,
      "evidence_url": "https://xyzmech.com/about",
      "evidence_text": "Bonded up to $6 million. Projects include Hilton Austin, 2022...",
      "last_checked": "2025-05-09"
    }
  ]
}
```

---

## Scoring Logic

| Metric                            | Weight |
|----------------------------------|--------|
| Bond Capacity ≥ Required         | 30     |
| Valid TX License                 | 20     |
| City/Geo Match                   | 20     |
| TX Projects (5 pts per project) | 30 max |

---

## Deployment on Render

1. Push code to GitHub
2. Go to https://render.com
3. Click "New Web Service"
4. Connect your GitHub repo
5. Configure:
   - Runtime: Python
   - Start Command: uvicorn main:app --host 0.0.0.0 --port 10000
   - Plan: Free

6. Your API will be live.

---

## Project Structure

```
research-agent/
├── main.py
├── schemas.py
├── models.py
├── requirements.txt
├── README.md
├── results/
│   └── job_<uuid>.json
├── research_jobs/
│   ├── __init__.py
│   ├── engine.py
│   ├── scorer.py
│   ├── scraper.py
│   ├── search.py
│   ├── store.py
│   └── tdlr_checker.py
```

---

Built by Sahil Gupta
