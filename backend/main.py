import pandas as pd
import google.generativeai as genai


# ----------------------
# Load Dataset
# ----------------------

def load_data(file_path):

    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)

    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)

    else:
        raise ValueError("Unsupported file format")


# ----------------------
# Data Quality Report
# ----------------------

def data_quality_report(df):

    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicates": int(df.duplicated().sum())
    }


# ----------------------
# Dataset Summary
# ----------------------

def dataset_summary(df):

    return {
        "Columns": list(df.columns),
        "Data Types": df.dtypes.astype(str).to_dict()
    }


# ----------------------
# AI Insights
# ----------------------

def generate_insights(df, api_key):

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    You are an expert Data Analyst.

    Analyze this dataset:

    Columns:
    {list(df.columns)}

    Dataset Statistics:
    {df.describe(include='all').to_string()}

    Provide:

    1. Key Insights
    2. Important Trends
    3. Business Recommendations
    4. Potential Risks
    """

    response = model.generate_content(prompt)

    return response.text


# ----------------------
# Ask Questions
# ----------------------

def ask_question(df, question, api_key):

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    You are an expert Data Analyst.

    Dataset Columns:
    {list(df.columns)}

    Dataset Summary:
    {df.describe(include='all').to_string()}

    User Question:
    {question}

    Answer clearly and professionally.
    """

    response = model.generate_content(prompt)

    return response.text