import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import streamlit as st
from Database import get_connection
from datetime import datetime as dt
from Auth.Login import *

st.set_page_config(layout="centered")

# if not st.session_state.get("Logged_in",False):
#     st.warning("⚠️ Please Login first")
#     st.stop()
# else:

now = dt.now().strftime("%Y-%m-%d %H:%M:%S")

def sales():

    st.subheader("Sales")

    with st.form(key="Sales_Entry_form"):

        p_id = st.text_input("Enter Product Id : ")
        p_name = st.text_input("Enter Product Name : ")
        P_Cat = st.text_input("Enter Product Category : ")

        Qua = st.number_input("Enter Sales Quantity", min_value=0, step=1)

        usp = st.number_input("Enter Unit Selling Price :", min_value=0)
        ucp = st.number_input("Enter Unit Cost price :", min_value=0)

        emp = st.text_input("Mobile",value=st.session_state.emp,disabled=True)

        submit = st.form_submit_button("Submit")

    if submit:

        if p_id.strip()=="" or p_name.strip()=="" or P_Cat.strip()=="" or emp.strip()=="":
            st.warning("No empty fields allowed ❌")
            return

        # calculations
        tsp = Qua * usp
        tcp = Qua * ucp
        rent = tsp * 0.4
        exp = tsp * 0.6
        gsp = tcp + rent + exp
        pro = gsp - exp

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO Sales
        (Product_id,Product_Name,Product_Category,Quantity,Usp,Ucp,Tsp,tcp,Revenue,Rent,Expenditure,Gsp,profit,Mobile,created_at)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,
        (p_id,p_name,P_Cat,Qua,usp,ucp,tsp,tcp,tsp,rent,exp,gsp,pro,emp,now))

        conn.commit()
        conn.close()

        st.success("Data inserted Successfully ✅")

