import streamlit as st
import mysql.connector

# Initialize connection.
# Uses st.cache_resource to only run once.

st.write(['mysql']['host'])
mydb = mysql.connector.connect(
        host=['mysql']['host'],
        user=['mysql']['user'],
        password=['mysql']['password'],
        database= ['mysql']['database'],
        port = ['mysql']['port']
    )

mycursor = mydb.cursor()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.

