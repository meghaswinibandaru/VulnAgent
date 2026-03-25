import pandas as pd

def filter_by_ip(df: pd.DataFrame, prefixes: list) -> pd.DataFrame:
    """Keep only rows whose Server IP starts with one of the selected prefixes."""
    mask = df["Server IP"].apply(
        lambda ip: any(str(ip).startswith(p) for p in prefixes)
    )
    return df[mask].reset_index(drop=True)