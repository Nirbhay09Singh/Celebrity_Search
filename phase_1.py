import os

from constant import openai_key

from langchain.llms import OpenAI

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework

st.title('Search With OPENAI API')
input_text=st.text_input("Search whatever you want")

## OPENAI LLM
llm=OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))