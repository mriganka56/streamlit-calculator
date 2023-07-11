import streamlit as st
import math

def add(a, b):
  return a + b
def sub(a, b):
  return a - b
def mul(a, b):
  return a * b
def div(a, b):
  return a / b

def sin(x):
  return math.sin(x)

def cos(x):
  return math.cos(x)

def tan(x):
  return math.tan(x)

def log(x):
  return math.log(x)



def main():
  st.title("Streamlit Calculator")
  st.write("This is a calculator app made using Streamlit")

  st.write('<p style="font-size:26px; color:blue;">Main Operations:</p>', unsafe_allow_html=True)
  a=st.number_input("Enter first number")   
  b=st.number_input("Enter second number")
  operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])
  if operation == "Add":
    st.write(add(a, b))
  elif operation == "Subtract":
    st.write(sub(a, b))
  elif operation == "Multiply":
    st.write(mul(a, b))
  elif operation == "Divide":
    st.write(div(a, b))

  st.write('<p style="font-size:26px; color:blue;">Other Operations:</p>', unsafe_allow_html=True)
  x=st.number_input("Enter the number")
  operation = st.selectbox("Select Operation", ["Sin", "Cos", "Tan", "Log"])
  if operation == "Sin":
    st.write(sin(x))
  elif operation == "Cos":
    st.write(cos(x))
  elif operation == "Tan":
    st.write(tan(x))
  elif operation == "Log":
    st.write(log(x))

if __name__ == '__main__':
 main()


