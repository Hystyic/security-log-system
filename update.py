import datetime
import pandas as pd
import streamlit as st
from database import view_all_data, view_only_resident_names, get_details, edit_details


def update(table):
    if table=='resident':
        result = view_all_data()
        st.table(result)
        # st.write(result)
        df = pd.DataFrame(result, columns=['resident_id','Fname','Lname','Mob_no','block_id','house_id'])
        with st.expander("Current residents"):
            st.dataframe(df)
        list_of_resident = [i[0] for i in view_only_resident_names()]
        selected_resident = st.selectbox("resident to Edit", list_of_resident)
        selected_result = get_details(selected_resident)
        # st.write(selected_result)
        if selected_result:
            resident_id = selected_result[0][0]
            Fname = selected_result[0][1]
            Lname = selected_result[0][2]
            Mob_no= selected_result[0][3]
            block_id = selected_result[0][5]
            house_id = selected_result[0][5]

            # Layout of Create

            col1, col2 ,col3= st.columns(3)
            with col1:
                new_resident_ID = st.text_input("resident_id:",resident_id)
                new_FName = st.text_input("Fname:",Fname)
                new_LName= st.text_input("Lname:",Lname)
            with col2:
                new_PH_NO = st.text_input("Mob_no:",Mob_no)
            with col3:
                new_block_id = st.text_input("block_id:",block_id)
                
                new_resident_id= st.text_input("house_id:",house_id) 
        

            if st.button("Update resident"):
                edit_details(new_resident_ID,new_FName,new_LName,new_PH_NO, new_block_id,  new_resident_id,resident_id,Fname,Lname,Mob_no,block_id,house_id)
                st.success("Successfully updated:: {} to ::{}".format(Fname, new_FName))

        result2 = view_all_data()
        df2 = pd.DataFrame(result2, columns=['resident_id','Fname','Lname','Mob_no','block_id','house_id'])
        with st.expander("Updated data"):
            st.dataframe(df2)
