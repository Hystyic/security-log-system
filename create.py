import streamlit as st
from database import add_data,add_data_visitor,add_data_security_manager


def create(table):
    if table=='resident':
        col1, col2 ,col3= st.columns(3)
        with col1:
            resident_id = st.text_input("Resident ID:")
            Fname = st.text_input("First Name:")
            Lname= st.text_input("Last Name:")
        with col2:
            Mob_no = st.text_input("Mobile number:")
        with col3:
            block_id = st.text_input("Block ID:")
            house_id= st.text_input("House ID:") 
        
        if st.button("Add"):
            add_data(resident_id,Fname,Lname,Mob_no,block_id,house_id)
            st.success("Successfully added visitor: {}".format(resident_id))


    elif table=='visitor':
        col1, col2 = st.columns(2)
        with col1:
            visitor_id = st.text_input("Visitor ID:")
            in_time = st.text_input("In Time:")
            out_time= st.text_input("Out Time:")
        with col2:
            name = st.text_input("Name:")
            resident_id = st.text_input("Resident ID:")
            
        
        if st.button("Add"):
            add_data_visitor(visitor_id,in_time,out_time,NAME,resident_id)
            st.success("Successfully added VISITOR: {}".format(visitor_id))


    elif table=='security_manager':
        col1, col2 ,col3= st.columns(3)
        with col1:
            manager_id = st.text_input(" Security Manager ID:")
            username = st.text_input("username:")
            Fname= st.text_input("First Name:")
        with col2:
            Lname = st.text_input("Last Name:")
            Mob_no = st.text_input("Mobile Number:")
            block_id = st.text_input("Block ID:")
        with col3:
            password = st.text_input("Password:")
            
            is_admin = st.selectbox("Does security manager have admin acces 1 FOR YES, 0 FOR NO ", ["1", "0"])
        
        if st.button("Add"):
            add_data_security_manager(manager_id,username,Fname,Lname,Mob_no,block_id,password,is_admin)
            st.success("Successfully added Security manager: {}".format(manager_id))