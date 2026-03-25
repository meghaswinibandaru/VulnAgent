import pandas as pd

REQUIRED_COLS = ["S.No","Vuln Age (Days)","Vuln Severity","Server Name",
                 "Server IP","Class","CVE","Vulnerability Title",
                 "Vulnerability Solution","Vulnerability Proof (File Path)"]

def load_excel(path: str) -> pd.DataFrame:
    df = pd.read_excel(path, dtype=str)
    df.columns = [c.strip() for c in df.columns]
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return df