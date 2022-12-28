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

## DNA nucleotide count
st.header('OUTPUT (Nucleotide Count)')

def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    
    return d

### Ways to show the results

# 1. Print dictionary
X = DNA_nucleotide_count(sequence)
X_label, X_values = list(X), list(X.values())

X

# 2. Print text
st.subheader('2. Print text')
st.text(f'There are {str(X["A"])} adenine (A)')
st.text(f'There are {str(X["T"])} adenine (T)')
st.text(f'There are {str(X["G"])} adenine (G)')
st.text(f'There are {str(X["C"])} adenine (C)')

# 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index': 'nucleotide'})

st.write(df)

# 4. Display Bar Chart using Altair

