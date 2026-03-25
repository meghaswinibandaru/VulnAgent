import pandas as pd
from typing import Dict, List

def build_solution_map(df: pd.DataFrame) -> Dict[str, List[str]]:
    """
    Returns { vulnerability_solution: [list of unique server IPs] }
    for all rows where the same solution applies to multiple IPs.
    """
    sol_map: Dict[str, set] = {}
    for _, row in df.iterrows():
        sol = str(row["Vulnerability Solution"]).strip()
        ip  = str(row["Server IP"]).strip()
        sol_map.setdefault(sol, set()).add(ip)
    return {sol: sorted(ips) for sol, ips in sol_map.items() if len(ips) > 1}