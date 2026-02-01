def generate_report(df):
    lines = []

    for _, r in df.iterrows():
        if r["Efficiency Score"] >= 65:
            verdict = "Highly Optimal"
        elif r["Efficiency Score"] >= 50:
            verdict = "Moderately Optimal"
        else:
            verdict = "Needs Review"

        lines.append(
            f"{r['Ministry']} ({r['Sector']}): {verdict} | "
            f"Capital Ratio: {r['Capital Ratio']:.2f}"
        )

    return "\n".join(lines)
