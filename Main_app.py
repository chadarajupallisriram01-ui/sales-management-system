import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import streamlit as st

st.set_page_config(
    page_title="Sales Management System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "page" not in st.session_state:
    st.session_state.page = "home"

if "role" not in st.session_state:
    st.session_state.role = None

if "Logged_in" not in st.session_state:
    st.session_state.Logged_in = False

if "Employee_Activity" not in st.session_state:
    st.session_state.Employee_Activity = False

if "Back_stack" not in st.session_state:
    st.session_state.Back_stack = []

if "Forward_stack" not in st.session_state:
    st.session_state.Forward_stack = []

from Auth.Registration_form import Reg
from Auth.Login import Login
from Modules.sales import sales
from Modules.Dashboard import Dashboard,emp_act
from Roles.Developer import Emp_view,Sales_View
# from utils.navigation import go_to
from Roles.instant_data import instant
from Roles.Flexible_data import delete,delete1

if st.session_state.page == "home":

    st.title("Welcome to Sales Management System")
    st.balloons()

    st.markdown("""<h4 style="color:orange">Hello, I am Developer of this application, My name is Sriram. I want to Share few words with you about this Application</h4>
                <b style="font-size : 20px"><u>Point-1 :</u></b> If you are stucked in this app just click on <b>Logout Button</b>, I Bring you back to <b>Home Page</b> <br>
                <b style="font-size : 20px"><u>Point-2 :</u></b> It is System Style Application that means Registration and Loing buttons works on <b>Double Click</b><br>
                <b style="font-size : 20px"><u>Point-3 :</u></b> Remaining buttons are Working as <b>One click for Validation</b> and <b>Another click is for Navigation</b><br>
                <b style="font-size : 20px"><u>Point-4 :</u></b> System Designed Navigations <b>Employee ->Login->Sales</b> are <b>Admin ->Login->Dashboard & View</b><br><p>If you got any error ignore it and move forward</p>
                <b style="font-size : 20px">Point -5 :</b> If Mobile Number not found Re-enter the Number<br><b style="font-size : 20px;align-item:center;">Thankyou for Visiting , Visit again you are always welcome</b><hr>
                """,unsafe_allow_html=True)
    
    if st.checkbox("I, agree above rules I, read those points and I Understood"):
        st.success(" ✅ You are Ready to Use this app, you can Proceed")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Register"):
            st.session_state.page = "register"

    with col2:
        if st.button("Login"):
            st.session_state.page = "login"
            
    
    st.divider()
    st.subheader("Developer Contact details | Mobile : +918465024633 | email : cram84650@gmail.com")


elif st.session_state.page == "register":
    Reg()

elif st.session_state.page == "login":
    Login()

elif st.session_state.page == "sales":
    sales()

elif st.session_state.page == "dashboard":
    Dashboard()

elif st.session_state.page == "instant":
    instant()

elif st.session_state.page == "delete_emp":
    delete()

elif st.session_state.page == "delete_sales":
    delete1()

elif st.session_state.page == "Employee_view":
    Emp_view()

elif st.session_state.page == "Sales_view":
    Sales_View()
elif st.session_state.page == "emp_act":
    emp_act()

if "dev_Panel" not in st.session_state:
    st.session_state.dev_Panel = False

 
with st.sidebar:

    st.title("📊 Sales Management")

    st.markdown("---")

    st.markdown("### 👤 User info")

    st.write("User_name :", st.session_state.User_name)

    st.write("Role :", st.session_state.role)

    st.divider()

    def admin():
        if "Admin_option" not in st.session_state:
            st.session_state.Admin_option = "Dashboard"

        option = st.radio("Select Option",("Dashboard","Employee_activity"),key = "Admin_option")

        if option == "Dashboard" and st.session_state.page != "dashboard":
            st.session_state.page = "dashboard"
            st.rerun()
        elif option == "Employee_activity" and st.session_state.page != "emp_act":
            st.session_state.page = "emp_act"
            st.rerun()

    if st.session_state.role == "Developer":
        if st.button("🛠 Developer Panel",key = "dev"):
            st.session_state.page = "Developer"
            st.session_state.dev_Panel = not st.session_state.dev_Panel
            st.rerun()

    def dev_panel():
        if  st.session_state.dev_Panel == True:
            opp = st.selectbox("Developer Opp",["--Select--","Dynamic_Data_Entry","Delete_Emp_Data","Delete_Sales_Data","Employee_view","Sales_view"])
            if opp == "Dynamic_Data_Entry":
                st.session_state.page = "instant"
                st.rerun()

            elif opp == "Delete_Emp_Data":
                st.session_state.page = "delete_emp"
                st.rerun()

            elif opp == "Delete_Sales_Data":
                st.session_state.page = "delete_sales"
                st.rerun()

            elif opp == "Employee_view":
                st.session_state.page = "Employee_view"
                st.rerun()

            elif opp == "Sales_view":
                st.session_state.page = "Sales_view"
                st.rerun()

    if st.session_state.role == "Admin":
        admin()

    if st.session_state.page == "Developer":
        dev_panel()

    st.markdown("---")

    if st.button("Logout"):
        st.session_state.Logged_in = False
        st.session_state.page = "home"
        st.session_state.role = None
        st.session_state.User_name = None
        st.rerun()

if st.session_state.page == "Developer":
    st.title("🙏 Welcome to Developer Page 🙏")
    st.subheader("Click on Developer Options/Panel Button in the left sidebar")

if st.session_state.page == "Developer" and st.session_state.page == "delete_emp":
    st.success("✅ Employee Data Delected Successfully..")
    st.error("❌ Employee Table is Empty")

elif st.session_state.page == "delete_Sales":
    st.success("✅ Sales Data Delected Successfully..")
    st.error("❌ Sales Table is Empty")
