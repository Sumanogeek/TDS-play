import streamlit as st

def calc(a,b,op):
  if op == '+':
    return (a+b)
  elif op == '-':
    return (a-b)
  elif op == '*':
    return (a*b)
  elif op == '/':
    return (a/b)
  return ('operation not listed')
    

st.title("Model Caclulator")
a = st.number_input('Insert 1st number: ')
b = st.number_input('Insert 2nd number: ')
op = st.text_input('Insert operation (+ or - or * or / ): ')

value = calc(a,b,op)  
st.write(value)
