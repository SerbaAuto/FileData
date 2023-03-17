import streamlit as st
import pandas as pd
import numpy as np

import mysql.connector


#st.write("DB username:",st.secrets["mysql"]["host"])
#st.cache_resource
def init_connection():
    st.write("Lewat")
    return mysql.connector.connect(user = st.secrets['mysql']['user'],password=st.secrets['mysql']['password'],host=st.secrets['mysql']['host'],database=st.secrets['mysql']['database'])
conn = init_connection()
#st.cache_data(ttl=600)

st.write("Work")