import streamlit as st
import mysql.connector

from create import create
from database import create_table,quer
from delete import delete
from read import read
from update import update

def main():
    st.title("Security log system")
    menu = ["Add ", "View ", "Edit", "Remove ","Query"]
    choice = st.sidebar.selectbox("Menu", menu)
    table_names=["security_manager","resident","visitor"]
    table=st.sidebar.selectbox("table", table_names)

    create_table()
    if choice == "Add ":
        if table=='security_manager':
            st.subheader("Enter warden Details:")
            create(table)
        elif table=='resident':
            st.subheader("Enter resident Details:")
            create(table)
        elif table=='visitor':
            st.subheader("Enter visitor Details:")
            create(table)
    elif choice == "View ":
        if table=='security_manager':
            st.subheader("Enter warden Details:")
            read(table)
        elif table=='resident':
            st.subheader("Enter resident Details:")
            read(table)
        elif table=='visitor':
            st.subheader("Enter visitor Details:")
            read(table)

    elif choice == "Edit":
        if table=='visitor':
            st.subheader("Enter visitor Details:")
            update(table)

    elif choice == "Remove ":
        if table=='security_manager':
            st.subheader("Enter warden Details:")
            delete(table)
        elif table=='resident':
            st.subheader("Enter resident Details:")
            delete(table)
        elif table=='visitor':
            st.subheader("Enter visitor Details:")
            delete(table)

    elif choice=='Query':
        st.subheader("Enter the Query:")
        quer()

if __name__ == '__main__':
    main()