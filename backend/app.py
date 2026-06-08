# pyrefly: ignore [missing-import]

import streamlit as st
import pandas as pd
import plotly.express as px

from main import generate_insights

# ==========================
# GEMINI API KEY
# ==========================

API_KEY = "your api key"

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(page_title="InsightAI")

st.title("📊 InsightAI")
st.subheader("AI Data Analyst Agent")

# ==========================
# FILE UPLOAD
# ==========================

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

# ==========================
# DATA ANALYSIS
# ==========================

if uploaded_file:

    st.success("File Uploaded Successfully!")

    df = pd.read_csv(uploaded_file)

    # --------------------------
    # Dataset Preview
    # --------------------------

    st.subheader("📋 Dataset Preview")
    st.dataframe(df.head())

    # --------------------------
    # Quality Report
    # --------------------------

    st.subheader("📊 Quality Report")

    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])
    st.write("Missing Values:", df.isnull().sum().sum())
    st.write("Duplicates:", df.duplicated().sum())

    # --------------------------
    # Dataset Information
    # --------------------------

    st.subheader("📑 Dataset Information")

    st.write("Columns:")
    st.dataframe(
        pd.DataFrame({
            "Columns": df.columns
        })
    )

    st.write("Data Types:")
    st.dataframe(
        df.dtypes.astype(str).reset_index()
    )

    # --------------------------
    # Statistical Summary
    # --------------------------

    st.subheader("📈 Statistical Summary")

    try:
        st.dataframe(df.describe())
    except:
        st.info("No numerical columns available.")

    # --------------------------
    # Auto Chart
    # --------------------------

    numeric_cols = df.select_dtypes(include=["number"]).columns
    categorical_cols = df.select_dtypes(include=["object"]).columns

    if len(numeric_cols) > 0 and len(categorical_cols) > 0:

        st.subheader("📊 Data Visualization")

        x_col = categorical_cols[0]
        y_col = numeric_cols[0]

        fig = px.bar(
            df,
            x=x_col,
            y=y_col,
            title=f"{y_col} by {x_col}"
        )

        st.plotly_chart(fig, use_container_width=True)

    # --------------------------
    # AI Insights
    # --------------------------

    st.subheader("🧠 AI Insights")

    if st.button("Generate AI Insights"):

        with st.spinner("Analyzing Dataset..."):

            insights = generate_insights(
                df,
                API_KEY
            )

        st.success("Analysis Complete!")

        st.write(insights)