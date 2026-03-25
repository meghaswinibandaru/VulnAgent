from excel.reader import load_excel
from excel.writer import write_output
from agent.filters import filter_by_ip
from agent.grouper import group_data
from agent.deduplicator import build_solution_map
import os, uuid

def run_agent(input_path: str, ip_prefixes: list) -> tuple:
    df = load_excel(input_path)

    # Step 1 — filter by selected IPs
    filtered = filter_by_ip(df, ip_prefixes)

    # Step 2 & 3 — group by server name → class
    groups = group_data(filtered)

    # Step 4 — dedup vuln solutions → IP mapping
    sol_map = build_solution_map(filtered)

    # Step 5 — write output Excel
    os.makedirs("outputs", exist_ok=True)
    output_path = os.path.join("outputs", f"grouped_{uuid.uuid4().hex[:8]}.xlsx")
    write_output(output_path, groups, sol_map)

    summary = {
        "total_rows_after_filter": len(filtered),
        "server_groups": len(groups),
        "unique_solutions_shared": len(sol_map),
    }
    return output_path, summary