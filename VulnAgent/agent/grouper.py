import pandas as pd
from typing import Dict, Tuple

def group_data(df: pd.DataFrame) -> Dict[Tuple[str, str], pd.DataFrame]:
    """
    Returns a dict keyed by (server_name, class) → sub-DataFrame.
    Example key: ("ORA", "prod")
    """
    groups = {}
    for server in df["Server Name"].unique():
        s_df = df[df["Server Name"] == server]
        for cls in s_df["Class"].unique():
            sub = s_df[s_df["Class"] == cls].reset_index(drop=True)
            groups[(server, cls)] = sub
    return groups