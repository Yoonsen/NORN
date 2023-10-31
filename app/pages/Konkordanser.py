import streamlit as st
import sys
sys.path.append('..')
from utils import load_corpus
from config import corpus_dict


def main():
    st.title('Konkordanser')
    st.write('### Velg korpus')
    
    
    
    corpus_options = corpus_dict.keys()
    selected_corpus = st.selectbox("Select a Corpus:", corpus_options)
        
    c = load_corpus(corpus_dict[selected_corpus])

    user_input = st.text_input("Input your text:")
    if user_input is not "":        
        conc = c.conc(user_input)
        df = conc.frame

        
        html_table = df.to_html(escape=False)
        st.markdown(html_table, unsafe_allow_html=True)
        
        #st.dataframe(df)
    

    st.write('Here will be your concordance search results.')


if __name__ == "__main__":
    main()