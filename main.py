import langchain_helper as lch
import streamlit as st
st.title("GLAM_AI")
skin_type=st.sidebar.selectbox("skin type",("dry","oily","combination"))
color=st.sidebar.text_area(label="your skin color?",max_chars=15)
if color:
    response=lch.generate_response(skin_type,color)
    st.text(response)
