import json
import os
from datetime import date

def save_results(job_id, candidates):
    try:
        final = []
        for c in candidates:
            final.append({
                "name": c.get("name"),
                "website": c.get("website"),
                "city": c.get("city"),
                "state": c.get("state"),
                "lic_active": c.get("lic_active"),
                "lic_number": c.get("lic_number"),
                "bond_amount": c.get("bond_amount"),
                "tx_projects_past_5yrs": c.get("tx_projects_past_5yrs"),
                "score": c.get("score"),
                "evidence_url": c.get("evidence_url"),
                "evidence_text": c.get("evidence_text"),
                "last_checked": date.today().isoformat()
            })
        os.makedirs("results", exist_ok=True)
        with open(f"results/job_{job_id}.json", "w") as f:
            json.dump({ "status": "SUCCEEDED", "results": final }, f, indent=2)
        print(f"✅ Results saved to results/job_{job_id}.json")
    except Exception as e:
        print(f"❌ Failed to save results for job {job_id}: {e}")
