import streamlit as st

st.set_page_config(page_title="Streamlit Calculator App", page_icon="🧮")

st.title("Calculator App")
st.write("Perform addition, subtraction, multiplication, and division.")

with st.form("calculator_form"):
    first_number = st.text_input("First Number", value="2")
    second_number = st.text_input("Second Number", value="2")
    operation = st.selectbox(
        "Select Operation",
        ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"]
    )
    submitted = st.form_submit_button("Calculate")

if submitted:
    try:
        first = float(first_number)
        second = float(second_number)

        if operation == "Addition (+)":
            result = first + second
        elif operation == "Subtraction (-)":
            result = first - second
        elif operation == "Multiplication (*)":
            result = first * second
        elif operation == "Division (/)":
            if second == 0:
                st.error("Division by zero is not allowed.")
                st.stop()
            result = first / second

        st.success(f"The result is: {result}")

    except ValueError:
        st.error("Invalid input. Please enter valid numbers.")