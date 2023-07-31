import streamlit as st
import pickle
import numpy as np
import base64
import warnings
warnings.filterwarnings('ignore')
st.set_page_config(layout='wide')

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )
add_bg_from_local('Images/bg1.jpg')

head1,head2,head3=st.columns([1.5,3,1.5])
with head2:
    #st.title('Industrial Copper Modeling')
    st.markdown("<h2 style= 'color: #F4511E;font-size: 48px;font-weight :900'><b>INDUSTRIAL COPPER MODELING</b></h2>",
                unsafe_allow_html=True)
model=pickle.load(open('model.pkl','rb'))
scaler=pickle.load(open('scale.pkl','rb'))
try:
    col1,col2,col3=st.columns([2,1,2])
    with col1:
        st.markdown('#')
        st.markdown('#')
        quantity_tons=st.number_input('Enter the Quantity Tons')
        customer=st.number_input('Enter the Customer')
        country=st.number_input('Enter the Country')
        status=st.selectbox('Enter the Status',['Won','Lost'])
        item_type=st.selectbox('Enter the Item Type',['W','WI','S','Others','PL','IPL','SLAWR'])
        application=st.number_input('Enter the Application')
    with col3:
        st.markdown('#')
        st.markdown('#')
        thickness=st.number_input('Enter the Thickness')
        width=st.number_input('Enter the Width')
        prod_ref=st.number_input('Enter the Product Reference')
        ovr_month=st.number_input('Enter the Overall Month')
        ovr_year=st.number_input('Enter the Overall Year')

    # Encode
    if status=='Won':
        status=1
    else:
        status=0

    if item_type=='W':
        item_type=0
    elif item_type=='WI':
        item_type=1
    elif item_type=='S':
        item_type=2
    elif item_type=='Others':
        item_type=3
    elif item_type=='PL':
        item_type=4
    elif item_type=='IPL':
        item_type=5
    elif item_type=='SLAWR':
        item_type=6

    customer=np.log(customer)
    country=np.log(country)
    application=np.log(application)
    thickness=np.log(thickness)
    width=np.log(width)
    prod_ref=np.log(prod_ref)
    btn1,btn2,btn3=st.columns([2.6,1,2])
    with btn2:
        st.markdown('#')
        predict=st.button('Predict')
        if predict==True:
            scale=scaler.transform([[quantity_tons,customer,country,status,item_type,application,thickness,width,prod_ref,ovr_month,ovr_year]])
            result=model.predict(scale)
    res1,res2,res3=st.columns([2,1,2])
    with res2:
        st.markdown('#')
        st.markdown("<h2 style= 'color: white;font-size: 44px;'>Price - {}</h2>".format(round(result[0],ndigits=3)),
                        unsafe_allow_html=True)

except:
    st.warning('Enter the Input')