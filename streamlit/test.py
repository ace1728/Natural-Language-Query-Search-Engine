import json
from turtle import color
import re
from colorama import colorama_text,Fore
import streamlit as st
import requests


import pandas as pd
st.set_page_config(layout="wide")

st.markdown(
         f"""
        
         <style>
         .stApp {{
             background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3Av9L1CcoQ11NRjWu0QVpqbt4CKUC4WA75Q&usqp=CAU");
             background-attachment: fixed;
             background-size: cover
            font-family: "Allerta Stencil", Sans-serif;
         }}
         
         </style>
         """,
         unsafe_allow_html=True
     )
kc=0
#st.columns(spec, *, gap="small")
d1,e2,c1=st.columns((3000,20,980))
with d1:
    original_title = '  <h1 style="font-family:Tahoma, sans-serif; color:White; "> Natural Language Query Processing</h1>'
    st.markdown(original_title, unsafe_allow_html=True)
    query=0
    with st.container():
        query=st.text_input("",max_chars=200,placeholder="Enter Your query")
        
    

col1, e1,col2 = st.columns((3000,20,980))

with col1:
    
    original_title = '  <p style="font-family:Tahoma, sans-serif; color:white; font-size: 20px;"> Query :'+query+'</p>'
    st.markdown(original_title, unsafe_allow_html=True)

  
  
    
    if(query):
        
        response = requests.get("http://127.0.0.1:8000/api/articles/"+query)
        result = re.sub(r'http\S+', '', response.text)
        df=pd.read_json(result, orient='records')
        st.write('total '+str(df.size)+' records found,displaying top 5.')
        j=0
        for index, row in df.iterrows():
            if j > 4:
                break
            #st.write(index)
            #st.write(row['title'])
            #st.write(row['abstract'])
            #st.write("*****************************************************")
            yol= "style.html"
            f = open(yol,'r') 
            contents = f.read()
            f.close()
            contents= contents.replace('index',str(index+1))
            contents= contents.replace('title',row['title'])
            contents= contents.replace('content',row['abstract'])
            contents= contents.replace('score',"Similarity : "+str(row['score']))
            
            st.markdown(contents, unsafe_allow_html=True)
            j=j+1
        
    







with c1:
    with st.container():
        result=[]
        response = requests.get("http://127.0.0.1:8000/api/queries/"+query)
        result = re.sub(r'http\S+', '', response.text)
        yol= "style1.html"
        f = open(yol,'r') 
        contents = f.read()
        f.close()
            
        
       
        y="Similar Queries <br>"
        if(query):
            df=pd.read_json(result, orient='records')
            for index, row in df.iterrows():
                y+=row[0]+'<br>'
            contents= contents.replace('content',y)
            st.markdown(contents, unsafe_allow_html=True)

        
      