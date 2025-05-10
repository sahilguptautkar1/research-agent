import asyncio
from .search import find_candidate_websites
from .scraper import extract_profiles
from .tdlr_checker import check_licenses
from .scorer import rank_candidates
from .store import save_results

async def run_research_job(req, job_id):
    print(f"\n🔍 Starting research job {job_id}...")
    try:
        websites = await find_candidate_websites(req)
        print(f"✅ Found {len(websites)} websites")

        profiles = await extract_profiles(websites)
        print(f"🔎 Extracted {len(profiles)} profiles")

        checked = check_licenses(profiles)  # FIXED: no await here
        print("🔐 License check completed")

        scored = rank_candidates(checked, req)
        print("📊 Scoring complete")

        save_results(job_id, scored)
        print(f"💾 Results saved for job {job_id}")

    except Exception as e:
        print(f"❌ Error in background job {job_id}: {e}")
