import argparse
from pathlib import Path
import pandas as pd
import sys

from pdf_reader import read_pdf
from extractor import extract_allocations
from sector_mapping import map_sector
from efficiency_scoring import add_efficiency_score
from optimality_report import generate_report
from exporter import export_excel, export_ppt


def run_pipeline(df):
    df["Sector"] = df["Ministry"].apply(map_sector)
    df = add_efficiency_score(df)
    df = df.sort_values("Total Allocation (₹ Cr)", ascending=False)

    Path("outputs").mkdir(exist_ok=True)

    df.to_csv("outputs/final_budget_analysis.csv", index=False)

    report = generate_report(df)
    export_excel(df, "outputs/budget_dashboard.xlsx")
    export_ppt(report, "outputs/policy_report.pptx")

    return df, report


# ---------------- STREAMLIT MODE ----------------
if "streamlit" in sys.argv[0]:
    import streamlit as st

    st.title("📊 Budget Allocation Analytics Engine")

    uploaded_file = st.file_uploader(
        "Upload Budget PDF or CSV",
        type=["pdf", "csv"]
    )

    if uploaded_file:
        if uploaded_file.name.endswith(".pdf"):
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.read())

            text = read_pdf(Path("temp.pdf"))
            df = extract_allocations(text)

        else:
            df = pd.read_csv(uploaded_file)

        df, report = run_pipeline(df)

        st.success("Analysis completed successfully")

        st.dataframe(df.head(10))

        st.download_button(
            "Download Final CSV",
            df.to_csv(index=False),
            "final_budget_analysis.csv"
        )

        st.text_area("AI Policy Report", report, height=300)

    st.stop()


# -------
