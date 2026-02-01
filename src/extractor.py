import re
import pandas as pd

def extract_allocations(text: str) -> pd.DataFrame:
    pattern = re.compile(
        r"MINISTRY OF ([A-Z ,&\\-]+)\\s+([\\d,]+\\.\\d+)\\s+([\\d,]+\\.\\d+)\\s+([\\d,]+\\.\\d+)"
    )

    rows = []
    for m in pattern.finditer(text):
        rows.append({
            "Ministry": m.group(1).title(),
            "Revenue (₹ Cr)": float(m.group(2).replace(",", "")),
            "Capital (₹ Cr)": float(m.group(3).replace(",", "")),
            "Total Allocation (₹ Cr)": float(m.group(4).replace(",", ""))
        })

    return pd.DataFrame(rows)
