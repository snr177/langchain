import chatbot 
import streamlit as st
st.title("MYGPT") # type: ignore
prompt = st.text_area("ASK ANYTHING: ") # type: ignore
if prompt:
    response = chatbot.main(prompt=prompt)
    st.text(response.content)# type: ignore