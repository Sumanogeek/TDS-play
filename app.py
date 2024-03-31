import streamlit as st

def addition(a,b):
  return (a+b)

st.title("Model Caclulator")
a = st.input("enter a: ")
b = st.input("enter b: ")

value = addition(a,b)
st.write(value)
