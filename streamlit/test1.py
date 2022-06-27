import streamlit as st

col1, col2  = st.columns(2)
with col1:
    yol= "style.html"
    f = open(yol,'r') 
    contents = f.read()
    f.close()
    contents= contents.replace('smth','replaced content')
    st.markdown(contents, unsafe_allow_html=True)
 
