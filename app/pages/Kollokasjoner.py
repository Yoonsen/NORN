import streamlit as st
import sys
sys.path.append('..')
from utils import load_corpus
from config import corpus_dict


def main():
    st.set_page_config(
        layout="wide",
        page_title="Norn kollokasjoner",
        page_icon="📚",
        initial_sidebar_state="expanded",
    )
    
    
    st.title('Kollokasjoner')
    st.write('### Corpus Selection')
    
    # Add your corpus selection logic here
    
    
    corpus_options = corpus_dict.keys()
    selected_corpus = st.selectbox("Select a Corpus:", corpus_options)
        
    c = load_corpus(corpus_dict[selected_corpus])

    user_input = st.text_input("Input your text:")
    if user_input is not "":        
        conc = c.coll(user_input)
        df = conc.frame.sort_values(by="counts", ascending=False)

        st.dataframe(df)
    

    st.write('Here will be your collocations search results.')

if __name__ == "__main__":
    main()
