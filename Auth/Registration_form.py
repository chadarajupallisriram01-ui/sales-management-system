import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from Database import get_connection
import streamlit as st
from datetime import datetime as dt
from Auth.auth import Register
import string as s

now = dt.now().strftime("%y-%m-%D %H:%M:%S")

def Reg():
    st.subheader("Registeration Form")
    with st.form("Application"):
        name = st.text_input("Enter your Name:",key = "name")
        mobile = st.text_input("Enter your Respected Mobile Number : ",max_chars=10)
        Password = st.text_input("Enter your Password : ",type= "password")
        confirm = st.text_input("Confirm Password : ",type = "password")
        Role = st.selectbox("Role",["Admin","Employee","Developer"])
        submit = st.form_submit_button("Submit")
    if submit:
        if name.strip()== "" or mobile.strip()=="" or Password.strip()=="" or confirm.strip()=="" or  (any(char in s.punctuation for char in name)) or (any(i in s.digits for i in name)):
            st.toast("❌ No Spaces Allowed and No symbols and Numbers are allowed")
        elif Password != confirm:
            st.error("❌ Password Not matched to Confirm Password")
        elif not Role:
            st.warning("Please, Select Role")
        else:
            if Register(name,mobile,Password,now) == "You are Registered Successfully..":
                st.success(Register(name,mobile,Password,now))
            else:
                st.warning(Register(name,mobile,Password,now))
