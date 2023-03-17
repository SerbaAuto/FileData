import streamlit as st
import pandas as pd
import numpy as np

import mysql.connector


st.write("DB username:",st.secrets["mysql"]["host"])
# st.cache_resource
# def init_connection():
#     return mysql.connector.connect(st.secrets["mysql"])

# conn = init_connection()
# st.cache_data(ttl=600)

# st.write("Work")