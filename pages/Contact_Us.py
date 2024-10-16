import streamlit as st
from EmailSender import send_email  ## 6. We import the module we just created to send email on form submit. Make sure it is in the same folder as the file that is calling it.

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
    ## 7. We add subject, and the email body to the send email function
    send_email(
        subject="Someone Wants to contact you from your portfolio website",
        body=f"""
Their email is {userEmail}
Their Message:
{userMessage}
"""
    )

    ## 8. Add a notification for visitor that their email was sent successfully
    st.info("Your Message was sent successfully")