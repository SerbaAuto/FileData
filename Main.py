import streamlit as st
import pandas as pd

@st.cache_data(ttl=600)

def load_data(sheet_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

#df = load_data(st.secrets["public_gsheets_url"])

df = pd.read_csv(st.secrets['public_gsheet_csv'])

# Print results.
for row in df.itertuples():
    st.write(row.id,row.name)