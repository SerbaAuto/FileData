import streamlit as st
import pandas as pd
import numpy as np

import mysql.connector

def init_connection():
    return mysql.connector.connect(**st.secrets[""])

conn = init_connection()

st.write("Work")