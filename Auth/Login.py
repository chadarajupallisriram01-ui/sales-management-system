import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from Database import get_connection
import streamlit as st 
from Auth.auth import has_pas,login

st.set_page_config(layout="wide")

if "emp" not in st.session_state:
    st.session_state.emp = None

if "User_name" not in st.session_state:
    st.session_state.User_name = None

def Login():
    st.title("Login")
    with st.form("Login"):
        mobile = st.text_input("Enter your Registered Mobile Number :",max_chars=10,key = "Mobile")
        Password = st.text_input("Enter your Registered Password :",type = "password")
        submit = st.form_submit_button("Login")
    if submit:
        st.session_state.emp = mobile
        if mobile.strip()=="" or Password.strip()=="":
            st.toast("❌ No Spaces Allowed Fill the Details")
        elif Password:
            if login(mobile,Password) != "You are Logged_in Successfully..":
                st.warning(login(mobile,Password))
            else:
                a = has_pas(Password)
                conn = get_connection()
                cur = conn.cursor()

                cur.execute("select * from Employee where Mobile = ?",(mobile,))
                data = cur.fetchone()
                
                # st.session_state.Logged_in = True
                if data:
                    if data[3] == "Admin":
                        st.success("Admin Login Successful..,   please, Click the Login button again")
                        st.session_state.page = "dashboard"
                        st.session_state.User_name = data[1]
                        st.session_state.role = data[3]
                    elif data[3] == "Employee":
                        st.success("Employee Login Successful..,   please, Click the Login button again")
                        st.session_state.page = "sales"
                        st.session_state.User_name = data[1]
                        st.session_state.role = data[3]
                    elif data[3] == "Developer":
                        st.success("Developer Login Successful..,   please, Click the Login button again")
                        st.session_state.page = "developer"
                        st.session_state.User_name = data[1]
                        st.session_state.role = data[3]
                    else:
                        st.session_state.role = None
                        st.session_state.Logged_in = True
                else:
                    st.warning("Mobile number not found")
                
