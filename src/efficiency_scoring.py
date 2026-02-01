def add_efficiency_score(df):
    df["Capital Ratio"] = df["Capital (₹ Cr)"] / df["Total Allocation (₹ Cr)"]
    df["Revenue Ratio"] = df["Revenue (₹ Cr)"] / df["Total Allocation (₹ Cr)"]

    df["Efficiency Score"] = (
        0.6 * df["Capital Ratio"] +
        0.4 * df["Revenue Ratio"]
    ) * 100

    return df.round(2)
