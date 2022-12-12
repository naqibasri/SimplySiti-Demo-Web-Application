import streamlit as st
import pandas as pd

data = pd.read_csv("SimplySiti Data.csv")
data = data.dropna()
data['phonenum'] = data['phonenum'].astype('int64')
data['Age'] = data['Age'].astype('int64')
data['Number of purchases in the last 1 year'] = data['Number of purchases in the last 1 year'].astype('int64')
data['Number of purchases in 3 years'] = data['Number of purchases in 3 years'].astype('int64')
blankIndex = [''] * len(data)
data.index = data['phonenum']               #017918
st.image("Picture1.png")
st.title("SimplySiti Customer Database")
phone = st.selectbox("Please enter the customer's phone number in the format 601XXXXXXXXX", data['phonenum'])
if phone != "":
    if int(phone) in list(data['phonenum']):
        st.subheader("Customer Data")
        st.table(data=data[data['phonenum']==int(phone)][['Name','Gender','Age','State','Ethnicity','Income group','House ownership']].T)
        
        st.subheader('Purchasing History')  
        pursHis = pd.DataFrame(data=data[data['phonenum']==int(phone)][['2022','2021','2020','2019','2018']].T)       
        pursHis.columns = ['Total spent(RM)']   
        pursHis['Year'] = pursHis.index
        st.line_chart(data=pursHis, x = 'Year', y= 'Total spent(RM)', width=0, height=0, use_container_width=True)

        st.subheader('History of purchased products') 
        prodHis = pd.DataFrame(data=data[data['phonenum']==int(phone)][['Diamond Series','Pearl Series','Lips','Face','Eyes','Rosehip','Clear Solution Purifying','Luminous White Lite','Dermagic Luxe', 'Aqua for Men', 'Fragrance']].T)       
        prodHis.columns = ['Total units purchased']
        prodHis['Product'] = prodHis.index
        st.bar_chart(prodHis, x='Product', y='Total units purchased', width=0, height=0, use_container_width=True)
        
        st.subheader('Sales by Site') 
        platHis = pd.DataFrame(data=data[data['phonenum']==int(phone)][['SimplySiti','Shopee','BeauSiti']].T)       
        platHis.columns = ['Total sales(RM)']
        platHis['Site'] = platHis.index
        st.bar_chart(platHis, x='Site', y='Total sales(RM)', width=0, height=0, use_container_width=True)
        
    else:
        st.caption('Invalid number')    
else:
    pass
