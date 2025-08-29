
from langchain_openai import ChatOpenAI
import streamlit as st

st.title("Ask Anything")

with st.sidebar:
    st.title("Provide the APi key")
    OPENAI_API_KEY = st.text_input("enter your API Key",type="password")

if not OPENAI_API_KEY:
    st.info(" you need to enter the API key to continue")
    st.stop()

llm=ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)


question = st.text_input("Enter the question:")

if question:
    response = llm.invoke(question)
    st.write(response.content)