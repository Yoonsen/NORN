import pandas as pd
import streamlit as st
import dhlab as dh


@st.cache_data
def load_corpus(path):
    df = pd.read_excel(path)
    
    if not "urn" in df.columns:
        raise ValueError("URN column not found in CSV file.")
    
    if path.endswith("konsensus-korpus.xlsx"):
        df["urn"] = df.urn.str.split('/').str[-1]
    
    
    c = dh.Corpus()
    c.extend_from_identifiers(df["urn"])
    
    return c


def gh_button(link):
    element = st.markdown(
    f'<a href="{link}" target="_blank">'
    '<button style="margin-top: 10px;">Go to GitHub Repo</button></a>', 
    unsafe_allow_html=True
)
    return element
