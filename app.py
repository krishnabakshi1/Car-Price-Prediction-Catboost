# Import Libraries
import numpy as np
import pandas as pd
import pickle
import streamlit as st 

sellingprice = open("sellingprice.pkl","rb")
regressor = pickle.load(sellingprice)

carnames = open("carname.pkl","rb")
names = pickle.load(carnames)



def predict_car_price(name,year,km_driven,fuel,seller_type,transmission,mileage,engine,max_power,seats,new_torque) :
    prediction = regressor.predict([name,year,km_driven,fuel,seller_type,transmission,mileage,engine,max_power,seats,new_torque])
    print(prediction)
    return prediction 

def main():
    st.title("Car Price Prediction using CatBoostRegressor (Demo)")
    st.subheader("Get a Current Market Value for Your Car!(For South Asian Market)")
    name  = st.selectbox("Select or Type Car name", names)
    year  = st.slider("Select Car Year", 1994,2020,2012)
    km_driven = st.slider("Enter Miles Driven" ,1,500000,1)
    fuel  = st.selectbox("Select Fuel Type",("Petrol","Diesel","CNG","LPG"))
    seller_type  = st.selectbox("Select Seller Type" ,("Individual","Dealer","Trustmark Dealer"))
    transmission =  st.radio("Select Transmission", ("Automatic","Manual"))
    mileage =  st.slider("Enter Mileage" ,0,42,0)
    engine =  st.slider("Select Engine Capacity" , 600,3700,600)
    max_power =  st.slider("Select Max Power", 30,400,30)
    seats =  st.slider("Select Number of Seats", 2,10,2)
    new_torque =  st.slider("Select RPM" , 400,45000,40)

    result = ""
    if st.button("Calculate Estimated Car Price"):
        result = predict_car_price(name,year,km_driven,fuel,seller_type,transmission,mileage,engine,max_power,seats,new_torque)
        st.balloons()     
    st.success('Estimated Car Price in INR = {}'.format(result))
   
if __name__ ==  '__main__':
    main()
