import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st

# Adjust the width of the Streamlit page
st.set_page_config(page_title="Ecobalyse Suivi des modifs", layout="wide")

# Add Title
st.title("Ecobalyse Suivi des modifs")

# Import your data
df = pd.read_csv("textile_consolidated.csv")

# Generate the HTML using Pygwalker
pyg_html = pyg.to_html(df)

# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)
