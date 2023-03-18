import streamlit as st
import pandas as pd

df = pd.read_csv(st.secrets['public_gsheet_csv'])

# Print results.
for row in df.itertuples():
    st.write("ID :",row.id," Dengan Nama :", row.nama)