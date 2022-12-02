import mysql.connector
import pandas as pd
import streamlit as st
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="security"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS `resident` ( `resident_id` varchar(255) NOT NULL,`Fname` varchar(255) NOT NULL,`Lname` varchar(255) NOT NULL,`Mob_no` varchar(255) NOT NULL,`block_id` int(10) DEFAULT NULL,`house_id` int(10) DEFAULT NULL, PRIMARY KEY (`resident_id`),KEY `block_id` (`block_id`), KEY `house_id` (`house_id`),FOREIGN KEY (`block_id`) REFERENCES `Hostel` (`block_id`) on delete cascade on  update cascade,FOREIGN KEY (`house_id`) REFERENCES `Room` (`house_id`) on  delete cascade on  update cascade);')
    c.execute("CREATE TABLE IF NOT EXISTS `security_manager` ( `manager_id` int(10) NOT NULL AUTO_INCREMENT,`username` varchar(255) NOT NULL,`Fname` varchar(255) NOT NULL,`Lname` varchar(255) NOT NULL,`Mob_no` varchar(255) NOT NULL,`block_id` int(10) NOT NULL,`password` LONGTEXT NOT NULL,`is_admin` tinyint(1) DEFAULT '0',PRIMARY KEY (`manager_id`),UNIQUE (`username`),KEY `block_id` (`block_id`),FOREIGN KEY (`block_id`) REFERENCES `Hostel` (`block_id`) on delete cascade on  update cascade);")
    c.execute('CREATE TABLE IF NOT EXISTS `visitor` ( visitor_id INT NOT NULL,in_time DATETIME,out_time DATETIME,NAME VARCHAR(20),resident_id VARCHAR(20),PRIMARY KEY  (visitor_id),FOREIGN KEY (resident_id) REFERENCES visitor(resident_id) on  delete  cascade on  update cascade );')
    

def add_data(resident_id,Fname,Lname,Mob_no,block_id,house_id):
    c.execute('INSERT INTO resident (`resident_id`,`Fname`,`Lname`,`Mob_no`,`block_id`,`house_id`) VALUES (%s,%s,%s,%s,%s,%s);',
              (resident_id,Fname,Lname,Mob_no,block_id,house_id))
    mydb.commit()
def add_data_visitor(visitor_id,in_time,out_time,NAME,resident_id):
    c.execute('INSERT INTO visitor (visitor_id,in_time,out_time,NAME,resident_id) VALUES (%s,%s,%s,%s,%s);',
              (visitor_id,in_time,out_time,NAME,resident_id))
    mydb.commit()
def add_data_security_manager(manager_id,username,Fname,Lname,Mob_no,block_id,password,is_admin):
    c.execute('INSERT INTO security_manager (manager_id,username,Fname,Lname,Mob_no,block_id,password,is_admin) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);',
              (manager_id,username,Fname,Lname,Mob_no,block_id,password,is_admin))
    mydb.commit()

def view_all_data():
    c.execute('SELECT * FROM resident')
    data = c.fetchall()
    return data

def view_all_manager():
    c.execute('SELECT * FROM security_manager')
    data = c.fetchall()
    return data
def view_all_visitor():
    c.execute('SELECT * FROM visitor')
    data = c.fetchall()
    return data

def view_only_resident_names():
    c.execute('SELECT Fname FROM resident')
    data = c.fetchall()
    return data
def view_only_manager():
    c.execute('SELECT manager_id FROM security_manager')
    data = c.fetchall()
    return data
def view_only_visitor():
    c.execute('SELECT visitor_id FROM visitor')
    data = c.fetchall()
    return data

def get_details(resident_id):
    c.execute('SELECT * FROM resident WHERE Fname="{}"'.format(resident_id))
    data = c.fetchall()
    return data



def edit_details(new_resident_ID,new_FName,new_LName,new_PH_NO, new_block_id,  new_resident_id,resident_id,Fname,Lname,Mob_no,block_id,house_id):
    c.execute("UPDATE resident SET resident_id=%s, Fname=%s, Lname=%s, Mob_no=%s,block_id=%s,house_id=%s WHERE "
              "resident_id=%s and Fname=%s and Lname=%s and Mob_no=%s and block_id=%s and house_id=%s" , (new_resident_ID,new_FName,new_LName,new_PH_NO, new_block_id, new_resident_id,resident_id,Fname,Lname,Mob_no,block_id,house_id))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(resident_id):
    c.execute('DELETE FROM resident WHERE Fname="{}"'.format(resident_id))
    mydb.commit()
def delete_data_hostel_manager(manager_id):
    c.execute('DELETE FROM resident_details WHERE manager_id="{}"'.format(manager_id))
    mydb.commit()
def delete_visitor(visitor_id):
    c.execute('DELETE FROM car_category WHERE visitor_id="{}"'.format(visitor_id))
    mydb.commit()
    
def quer():  
    with st.form(key="form1"):
        str1=st.text_area("Enter the query here:")
        submit=st.form_submit_button("Submit")
        if(submit):
            try:
                c.execute(str1)
                df=pd.DataFrame(c.fetchall())
                st.table(df)
            except mysql.connector.Error as e:
                st.warning(e)