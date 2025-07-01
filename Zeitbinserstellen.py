import streamlit as st
import pandas as pd
import plotly.express as px

def load_excel_file(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)
        return df
    except Exception as e:
        st.error(f"Fehler beim Laden der Datei: {e}")
        return None

st.set_page_config(page_title="Zeitbins erstellen", layout="wide")
st.title("Zeitbins erstellen")

uploaded_file = st.file_uploader("📁 Bereinigte Excel-Datei hochladen", type=["xlsx", "xls"])

if uploaded_file is not None:
    df = load_excel_file(uploaded_file)

    if df is not None:
        st.subheader("Originaldaten")
        df['Datum'] = pd.to_datetime(df['Zeitstempel'], errors='coerce')

        df['Monat'] = df['Datum'].dt.month
        df['Tag'] = df['Datum'].dt.day
        df['Stunde'] = df['Datum'].dt.hour

        st.write(df)
