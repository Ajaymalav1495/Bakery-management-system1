import pandas as pd
import uuid
import streamlit as st
from datetime import datetime
import mysql.connector
from mypackage import mymodule as md

def billing_page():
    st.title("Billing Page")
    st.write("---")
    a = st.text_input("a")
    if a.lower() == 'stop':
        st.write(a)
        st.end()
    st.write("---")

billing_page()
