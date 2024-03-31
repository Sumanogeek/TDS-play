import streamlit as st

def addition(a,b):
  return (a+b)

st.title("Model Caclulator")
a = st.number_input('Insert 1st number: ')
b = st.number_input('Insert 2nd number: ')

value = addition(a,b)
st.write(value)
