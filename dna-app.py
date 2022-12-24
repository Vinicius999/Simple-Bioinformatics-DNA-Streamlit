import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('images/dna-logo.png')

st.image(image, use_column_width = True)

st.write('''
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

---
''')