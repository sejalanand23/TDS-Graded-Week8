import streamlit as st

st.write("""
# Addition of two numbers

This application gives the sum of two numbers.
""")

st.header('Input Numbers')

def user_input():
    number1 = st.number_input('Number_1')
    number2 = st.number_input('Number_2')

    return number1, number2

num1, num2 = user_input()

st.write(""" 
Sum of two numbers is 
""")
st.write(num1 + num2)