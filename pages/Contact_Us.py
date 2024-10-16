import streamlit as st

st.header("Contact Me")

## 1. Create a form with context manager
with st.form(key="contact form"):
    ## 2. Create a text input box and store the value in a variable
    userEmail = st.text_input("Your Emails Address")

    ## 3. Create a text input area and store the value in a variable
    userMessage = st.text_area("Your Message")

    ## 4. Create a form submit button and store the Boolean value of whether it was pressed of not in a variable
    formButton  = st.form_submit_button("Submit")

## 5. Test the button by printing out a statement
if formButton:
    print("pressed")