import streamlit as st
import mysql.connector

# Initialize connection.
# Uses st.cache_resource to only run once.

st.write(st.secrets['mysql']['host'])
# mydb = mysql.connector.connect(
#         host=st.secrets['mysql']['host'],
#         user=st.secrets['mysql']['user'],
#         password=st.secrets['mysql']['password'],
#         database= st.secrets['mysql']['database'],
#         port = st.secrets['mysql']['port']
#     )
st.write("Lewat")
st.error("error")
# mycursor = mydb.cursor()
def init_connection():
    mydb = mysql.connector.connect(**st.secrets["mysql"])


st.write(init_connection())
st.write("bisa")

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.

