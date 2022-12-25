import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('images/dna-logo.png')

st.image(image, use_column_width = True)

#######################
# Page Title
#######################
st.write('''
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

---
''')


#######################
# Input Text Box
#######################
st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area('Sequence input', sequence_input, height=150)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skip the sequence name (first line)
sequence = ''.join(sequence) # Concatenate list to string

st.write('''
---
''')

st.header('INPUT (DNA Query)')
sequence
