import argparse
from pathlib import Path
import pandas as pd

from pdf_reader import read_pdf
from extractor import extract_allocations
from sector_mapping import map_sector
from efficiency_scoring import add_efficiency_score
from optimality_report import generate_report
from exporter import export_excel, export_ppt

parser = argparse.ArgumentParser(description="Budget Allocation Analytics Engine")

parser.add_argument("--pdf", type=str, help="Path to Budget PDF")
parser.add_argument("--csv", type=str, help="Path to Budget CSV")
args = parser.parse_args()

if not args.pdf and not args.csv:
    raise ValueError("Provide either --pdf or --csv")

# ---------------- LOAD DATA ----------------
if args.pdf:
    print("📄 Reading PDF...")
    text = read_pdf(Path(args.pdf))
    df = extract_allocations(text)
else:
    print("📊 Loading CSV...")
    df = pd.read_csv(args.csv)

# ---------------- PROCESS ----------------
df["Sector"] = df["Ministry"].apply(map_sector)
df = add_efficiency_score(df)

df = df.sort_values("Total Allocation (₹ Cr)", ascending=False)

# ---------------- EXPORT ----------------
Path("outputs").mkdir(exist_ok=True)

df.to_csv("outputs/final_budget_analysis.csv", index=False)

report = generate_report(df)
export_excel(df, "outputs/budget_dashboard.xlsx")
export_ppt(report, "outputs/policy_report.pptx")

print("✅ Pipeline completed successfully")
