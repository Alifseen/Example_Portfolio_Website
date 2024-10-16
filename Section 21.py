"""Portfolio Website
- This app wont have a backend since we are not processing data through code, we already have the data in csv and we are only displaying it

"""
import streamlit as st

st.set_page_config(layout="wide")

left, right = st.columns(2, vertical_alignment="top", gap="medium", )

## Introduction Element Left Column
left.image("Files/Images/photo.png")

## Introduction Element Right Column
right.title("Name Here")
description = """
Description here
"""
right.info(description)
