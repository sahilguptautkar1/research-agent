from fastapi import FastAPI, BackgroundTasks
from schemas import ResearchRequest
from research_jobs.engine import run_research_job
import uuid
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/research-jobs")
async def start_research(req: ResearchRequest, background_tasks: BackgroundTasks):
    job_id = str(uuid.uuid4())
    background_tasks.add_task(run_research_job, req, job_id)
    return {"job_id": job_id}

@app.get("/research-jobs/{job_id}")
def get_results(job_id: str):
    import os, json
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    job_id = job_id.strip()
    filepath = os.path.join(BASE_DIR, "results", f"job_{job_id}.json")
    print(f"Looking for file at: {filepath}")

    file_exists = os.path.exists(filepath)
    print(f"File exists? {file_exists}")

    if not file_exists:
        return {"status": "RUNNING"}

    with open(filepath, "r") as f:
        return json.load(f)

