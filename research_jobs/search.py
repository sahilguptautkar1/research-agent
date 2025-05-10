import asyncio

async def find_candidate_websites(req):
    query = f"{req.trade} contractors {req.city} {req.state} " + " ".join(req.keywords)
    candidates = []
    try:
        from duckduckgo_search import DDGS
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=30):
                if r.get("href"):
                    candidates.append(r["href"])
                    await asyncio.sleep(1)  # <-- Add 1 second pause per result
    except Exception as e:
        print(f"❌ DuckDuckGo search failed: {e}")
    return list(set(candidates))
