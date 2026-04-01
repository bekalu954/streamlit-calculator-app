import streamlit as st

st.set_page_config(page_title="Adder Calculator", page_icon="➕")

st.title("Adder Calculator")
st.write("This app adds two numbers.")

with st.form("adder_form"):
    first_number = st.text_input("First Number", value="2")
    second_number = st.text_input("Second Number", value="2")
    submitted = st.form_submit_button("Add numbers")

if submitted:
    try:
        first = float(first_number)
        second = float(second_number)
        result = first + second
        st.success(f"The result is: {result}")
    except ValueError:
        st.error("Invalid input. Please enter valid numbers.")
