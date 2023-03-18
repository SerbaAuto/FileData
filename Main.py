import streamlit as st
import mysql.connector

# Initialize connection.
# Uses st.cache_resource to only run once.


mydb = mysql.connector.connect(
        host=['mysql']['localhost'],
        user=['mysql']['user'],
        password=['mysql']['password'],
        database= ['mysql']['database']
    )

mycursor = mydb.cursor()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.

