def rank_candidates(candidates, req):
    for c in candidates:
        score = 0
        if c.get('bond_amount', 0) >= req.min_bond:
            score += 30
        if c.get('lic_active'):
            score += 20
        if req.city.lower() in (c.get('text', '') or '').lower():
            score += 20
        score += min(30, c.get('tx_projects_past_5yrs', 0) * 5)
        c['score'] = score
    return sorted(candidates, key=lambda x: x['score'], reverse=True)