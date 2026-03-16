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
        role = st.selectbox("Role",["--Select--","Admin","Employee","Developer"])
        submit = st.form_submit_button("Login")
    if submit:
        st.session_state.emp = mobile
        if mobile.strip()=="" or Password.strip()=="":
            st.toast("❌ No Spaces Allowed Fill the Details")
        elif((mobile == "8465024633" and Password == "$riRam1234" and role == "Admin") or (mobile == "7382945321" and role == "Developer" and Password == "$riRam098")):
                st.success("Click the button Once again")
        elif Password:
            if login(mobile,Password) != "You are Logged_in Successfully..":
                st.warning(login(mobile,Password))
            
            else:
                a = has_pas(Password)
                conn = get_connection()
                cur = conn.cursor()

                cur.execute("select Password from Employee where Mobile = ?",(mobile,))
                data = cur.fetchone()
                if data:
                    if  a == data[0]:
                        if role == "Employee":
                            st.success("Login Successful..")
                        else:
                            st.warning("Select role as Employee")
                    else:
                        st.error("Wrong Password..")
                else:
                    st.warning("User not found")
                st.session_state.Logged_in = True
                if role == "Admin" and mobile=="8465024633" and Password=="$riRam1234":
                    st.session_state.page = "dashboard"
                    st.session_state.User_name = "Prameela"
                    st.session_state.role = "Admin"
                elif role == "Employee" and (a==data[0] if data else False):
                    st.session_state.page = "sales"
                    st.session_state.User_name = "Sales-boy"
                    st.session_state.role = "Employee"
                elif role == "Developer" and mobile == "7382945321" and Password == "$riRam098":
                    st.session_state.page = "developer"
                    st.session_state.User_name = "Sriram"
                    st.session_state.role = "Developer"
                else:
                    st.session_state.role = None
                    st.write("Select Role as Employee")
                    st.session_state.Logged_in = True
