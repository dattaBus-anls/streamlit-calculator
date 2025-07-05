import streamlit as st  # Import the Streamlit library for building the web app

# App Title
st.title("🧮 Streamlit Calculator")  # Display the main title at the top

# Create two equal-sized columns to separate input and operation selection
left_col, right_col = st.columns([1, 1])

# Left Column: Number Inputs
with left_col:
    st.header("🔢 Enter Two Numbers")  # Subheading for input section
    number1 = st.number_input("First Number", key="num1")  # Input box for the first number
    number2 = st.number_input("Second Number", key="num2")  # Input box for the second number

# Right Column: Operation Selection
with right_col:
    st.header("➕ Select Operation")  # Subheading for operation selection
    # Radio button to select one operation at a time
    operation = st.radio("Choose an operation:", 
                         ["Addition", "Subtraction", "Multiplication", "Division", "Modulo"])

# Result Section
st.header("📊 Result")  # Subheading for results

# Perform calculation based on selected operation
if operation == "Addition":
    result = number1 + number2  # Perform addition
    st.success(f"Result: {result}")  # Display result in green success box

elif operation == "Subtraction":
    result = number1 - number2  # Perform subtraction
    st.success(f"Result: {result}")  # Display result

elif operation == "Multiplication":
    result = number1 * number2  # Perform multiplication
    st.success(f"Result: {result}")  # Display result

elif operation == "Division":
    if number2 != 0:  # Prevent divide-by-zero error
        result = number1 / number2  # Perform division
        st.success(f"Result: {result}")  # Display result
    else:
        st.error("❌ Division by zero is not allowed.")  # Display error if second number is 0

elif operation == "Modulo":
    if number2 != 0:  # Prevent modulo-by-zero error
        result = number1 % number2  # Perform modulo (remainder)
        st.success(f"Result: {result}")  # Display result
    else:
        st.error("❌ Modulo by zero is not allowed.")  # Display error if second number is 0