from turtle import color
from colorama import colorama_text,Fore
import streamlit as st
import requests
import pandas as pd
st.set_page_config(layout="wide")
kc=0
st.title('Neural Application')

with st.container():
    dummy0,search_bar, dummy = st.columns((1,3,1))
    with search_bar:
        st.text_input("Enter Your query",max_chars=200)
    

dummy2,col1,dummy3, col2 = st.columns((980,3000,20,1000))

with col1:
    
    st.write("Document/paragraph 1")
    st.write("Document/paragraph 2")
    st.write("Document/paragraph 3")
    response = requests.get("http://127.0.0.1:8000/api/articles")
    df = pd.read_json(response.text, orient ='values')
    df.drop(df.columns[[0]], axis = 1, inplace = True)
    kc=df.shape[0]
    

    st.dataframe(df,width=3700)

with dummy3:
    yol= "style.html"
    f = open(yol,'r') 
    contents = f.read()
    f.close()
    contents= contents.replace('smth','|<br>'*(kc+10))
    st.markdown(contents, unsafe_allow_html=True)


with col2:
    with st.container():

        
            st.write("Similar queries")
            st.write("query 1")
            st.write("query 2")
            st.write("query 3")

