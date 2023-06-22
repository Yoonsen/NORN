import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO


st.set_page_config(page_title="NORN", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

st.title("Metadata for NORN")
st.write('---')

@st.cache_data()
def meta():
    return pd.read_excel("konsensuskorpus_master.xlsx", index_col = 0).fillna('')

corpus = meta() 

#imag.year = imag.year.astype(int)
#imag.index = imag.index.astype(int)

fcol, valcol,_ = st.columns([2,2,4])
with fcol:
    colname = st.selectbox('Søk i kolonne', options = list(corpus.columns), index=list(corpus.columns).index('Forfatter'))

with valcol:
    value = st.text_input('Verdi', "")

sub = corpus
if value != '':
    try:
        sub = corpus[corpus[colname].astype(str).str.contains(value, regex=True)]
        st.write(f'lengde på delkorpus {len(sub)}')
    except AttributeError:
        st.write('Noe gikk galt...')

    
#edited_df = st.experimental_data_editor(sub, num_rows = 'dynamic')
st.dataframe(sub, use_container_width=True)

st.write('---')
st.bar_chart(sub.groupby('Utgivelsesår').count()['oaiid/URN'])
