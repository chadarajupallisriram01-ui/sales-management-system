from Database import get_connection
import hashlib
import streamlit as st
def has_pas(p):
    return hashlib.sha256(p.encode()).hexdigest()
def Register(n,a,b,c,now):
    import re
    if not re.search(r'^[6-9]\d{9}$',a):
        return "Mobile number starts with 6,7,8,9 only and contains be 10 digits"
    elif b.__len__()<8:
        return "Password contains minimum 8 Characters"
    elif not re.search(r"[A-Z]",b):
        return "Password contains atleast one Upper case character"
    elif not re.search(r"[a-z]",b):
        return "Password contains atleast one Lower case character"
    elif not re.search(r"[0-9]",b):
        return "Password contains atleast one number"
    elif not re.search(r"[~!#$%^&*()?/>.<,=+_]",b):
        return "Password contains atleast one special Chacter(Sybmol)"
    elif c == "--Select--":
            return "❌ Please select the Role"
    else:
        conn = get_connection()
        cur = conn.cursor()
        h=has_pas(b)
        cur.execute("""Insert or Ignore into Employee(
                    Name,mobile,Password,Role,created_at
                    )values(?,?,?,?,?)""",(n,a,h,c,now))
        conn.commit()
        conn.close()
        return "You are Registered Successfully.."
def login(a,b):
    import re
    if not re.search(r'^[6-9]\d{9}$',a):
        return "Mobile number starts with 6,7,8,9 only and contains be 10 digits"
    elif b.__len__()<8:
        return "Password contains minimum 8 Characters"
    elif not re.search(r"[A-Z]",b):
        return "Password contains atleast one Upper case character"
    elif not re.search(r"[a-z]",b):
        return "Password contains atleast one Lower case character"
    elif not re.search(r"[0-9]",b):
        return "Password contains atleast one number"
    elif not re.search(r"[~!#$%^&*()?/>.<,=+-_]",b):
        return "Password contains atleast one special Chacter(Sybmol)"
    else:
        return "You are Logged_in Successfully.."
    
