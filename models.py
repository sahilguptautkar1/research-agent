from typing import Optional

class SubcontractorProfile:
    def __init__(self, name: str, website: str, city: Optional[str], state: Optional[str],
                 lic_active: Optional[bool], lic_number: Optional[str], bond_amount: Optional[int],
                 tx_projects_past_5yrs: Optional[int], score: int, email: Optional[str],
                 phone_number: Optional[str], evidence_url: str, evidence_text: str,
                 last_checked: str):
        self.name = name
        self.website = website
        self.city = city
        self.state = state
        self.lic_active = lic_active
        self.lic_number = lic_number
        self.bond_amount = bond_amount
        self.tx_projects_past_5yrs = tx_projects_past_5yrs
        self.score = score
        self.email = email
        self.phone_number = phone_number
        self.evidence_url = evidence_url
        self.evidence_text = evidence_text
        self.last_checked = last_checked