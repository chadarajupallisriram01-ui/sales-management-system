import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import streamlit as st
from Roles.Flexible_data import Employee,Sales

def instant():
    st.title("Instant Data Entry")
    st.subheader("First Run Employee then Sales")
    with st.form("Data"):
        locaction = st.text_input("Where you want to Insert Data [Sales,Employee]")
        rows = st.text_input("How many Records you want to Insert Into Db")
        submit = st.form_submit_button("Submit")
    if submit:
        if locaction.strip()=="" or rows == "":
            st.toast("No Spaces Allowed")
        elif locaction.lower() == "sales":
            row = int(rows)
            st.session_state.page = "Sales"
        elif locaction.lower()== "employee":
            row1 = int(rows)
            st.session_state.page = "employee"

        if "page" not in st.session_state:
            st.session_state.page = "instant"

        if st.session_state.page == "employee":
            Employee(row1)
        if st.session_state.page == "Sales":
            Sales(row)

