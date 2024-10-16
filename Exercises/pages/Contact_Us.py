import streamlit as st
import pandas as pd
from EmailSender import send_email

df = pd.read_csv("Exercises/Files/topics.csv")


with st.form(key="contact_form"):
    email = st.text_input("Your Email Address")
    topic = st.selectbox("What topic do you want to discuss?", options=df)
    message = st.text_area("Text")
    button = st.form_submit_button("Submit")

if button:
    send_email(
        subject = "You have new Form Submission",
        body = f"""
        From: {email}
        Topic: {topic}
        Message: {message}
        """
    )