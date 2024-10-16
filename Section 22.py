"""Portfolio Website
- This app wont have a backend since we are not processing data through code, we already have the data in csv and we are only displaying it

"""
import streamlit as st
import pandas as pd ## 7. Import pandas

## 4. Increase page width
st.set_page_config(layout="wide")

## 1. Create Columns
left, right = st.columns(2, vertical_alignment="top", gap="medium", )

## 2. Introduction Element Left Column
left.image("Files/Images/photo.png")

## 3. Introduction Element Right Column
right.title("Ardit the Python Wiz")
description = """
Ardit is a german who lives in australia and has done masters in science, some sort of cross section between computer science and natural science. 
"""
right.info(description)

## 5. Text below the columns.
st.subheader("Below you can find some of the Apps I have built in Python")
textline = """
Feel Free to reach out using the contact form on Contact Page
"""
st.write(textline)

## 6. Columns for showcase projects
appColLeft, appColRight = st.columns(2)

## 8. Read the data CSV by defining the seperator
dataFrame = pd.read_csv("Files/data.csv", sep=";")

## Instructor uses context manager to add elements to columns
with appColLeft:
    ## 9. Iterate over the data.csv file
    for index, rows in dataFrame.iterrows():
        ## 10. Since we want half the content on right and other half on left, we will use modulo operator for even and odd index numbers, in this case, even rows in left, odd rows in right column
        if index % 2 == 0:
            ## 11. We add title
            appTitle = rows["title"]
            st.subheader(appTitle)

            ## 12. We add description in docstring
            appDescription = f"""{rows["description"]}"""
            st.info(appDescription)

            ## 13. We add images
            appThumbnailFilePath = f"Files/images/{rows["image"]}"
            st.image(appThumbnailFilePath, width=500)

            ## 14. We add links to source code
            appSourceCodeLink = rows["url"]
            st.page_link(appSourceCodeLink, label="Source Code")

## 15. We repeat the same process for right column
with appColRight:
    for index, rows in dataFrame.iterrows():
        if index % 2 != 0:
            appTitle = rows["title"]
            st.subheader(appTitle)

            appDescription = f"""{rows["description"]}"""
            st.info(appDescription)

            appThumbnailFilePath = f"Files/images/{rows["image"]}"
            st.image(appThumbnailFilePath, width=500)

            appSourceCodeLink = rows["url"]
            st.page_link(appSourceCodeLink, label="Source Code")
            ## Alternatively you can use the st.write method as follows:
            # st.write(f"[Source Code]({appSourceCodeLink})")




## Note: You can also use list slicing instead of step 10 by using the "dataFrame[:10].iterrows()" in the left column for loop for first 10 apps, and "dataFrame[10:].iterrows()" for last 10 apps in right column. Remember to remove the modulo if else statement.