import streamlit as st

st.set_page_config(page_title="Streamlit Calculator App", page_icon="🧮")

st.title("Calculator App")
st.write("Perform addition, subtraction, multiplication, and division.")

# --- Initialize session state ---
if "first" not in st.session_state:
    st.session_state.first = ""
if "second" not in st.session_state:
    st.session_state.second = ""
if "result" not in st.session_state:
    st.session_state.result = ""

# --- Form ---
with st.form("calculator_form"):
    first_number = st.text_input(
        "First Number",
        value=st.session_state.first,
        placeholder="Enter number"
    )
    second_number = st.text_input(
        "Second Number",
        value=st.session_state.second,
        placeholder="Enter number"
    )

    operation = st.selectbox(
        "Select Operation",
        ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"]
    )

    col1, col2, col3 = st.columns(3)

    calculate = col1.form_submit_button("Calculate")
    clear = col2.form_submit_button("Clear")
    exit_app = col3.form_submit_button("Exit")

# --- Button logic ---

# Clear button
if clear:
    st.session_state.first = ""
    st.session_state.second = ""
    st.session_state.result = ""
    st.rerun()

# Exit button (simulated)
if exit_app:
    st.warning("Application session ended. You can close the browser tab.")
    st.stop()

# Calculate button
if calculate:
    try:
        if not first_number or not second_number:
            st.error("Please enter both numbers.")
            st.stop()

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

        st.session_state.result = result

    except ValueError:
        st.error("Invalid input. Please enter valid numbers.")

# --- Display result ---
if st.session_state.result != "":
    st.success(f"The result is: {st.session_state.result}")