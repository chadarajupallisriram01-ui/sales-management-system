import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import streamlit as st
import pandas as pd
from Database import get_connection

st.set_page_config(page_title="Developer", layout="wide")

conn = get_connection()

c1,c2 = st.columns(2)
def Emp_view():
    st.title("Welcome to Developer - Employee_View")
    cur = conn.cursor()
    cur.execute("Select E.Name,count(*) as total_sales from Employee E inner join Sales S on E.Mobile = S.Mobile group by E.Name order by total_sales Desc")
    f3 = cur.fetchall()
    st.subheader("Employees and their Total Sales")
    st.dataframe(f3,st.columns=["Employee","Sales"])
    cur.execute("select * from Employee")
    f= cur.fetchall()
    st.subheader("Employee Table View")
    st.dataframe(f)

def Sales_View():
    st.title("Welcome to Developer - Sales_View")
    cur = conn.cursor()
    cur.execute("Select count(*),sum(Profit) as Total_Sales from Sales")
    f2 = cur.fetchall()
    st.subheader("Sales and Total No.of Sales")
    st.dataframe(f2)
    cur.execute("Select * from Sales")
    f1 = cur.fetchall()
    st.subheader("Sales-View")
    st.dataframe(f1)
    

