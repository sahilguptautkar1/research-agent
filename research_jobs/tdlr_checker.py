import pandas as pd

def check_licenses(profiles):
    try:
        df = pd.read_csv("TDLR_license_file.csv")
    except FileNotFoundError:
        for p in profiles:
            p['lic_active'] = False
            p['lic_number'] = None
        return profiles

    for p in profiles:
        match = df[df['Business Name'].str.contains(p['name'], na=False, case=False)]
        p['lic_active'] = not match.empty
        p['lic_number'] = match.iloc[0]['License Number'] if not match.empty else None
    return profiles