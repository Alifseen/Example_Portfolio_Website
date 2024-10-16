import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("The Best Company")

textContentHeroSection = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum
"""
st.write(textContentHeroSection)

st.subheader("Our Team")

left, empty_col, mid, empty_col, right, empty_col = st.columns(6)

df = pd.read_csv("Exercises/Files/data.csv")

with left:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image(f"Exercises/Files/images/{row["image"]}", width=300)

with mid:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image(f"Exercises/Files/images/{row["image"]}", width=300)

with right:
    for index, row in df[8:11].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image(f"Exercises/Files/images/{row["image"]}", width=300)