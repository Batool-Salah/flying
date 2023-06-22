import streamlit as st
import pandas as pd
import joblib

Inputs = joblib.load("Inputs.pkl")
Model = joblib.load("Model.pkl")
#Airline	Source	Destination	Total_Stops	Journey_day	Journey_month	Journey_year	Duration_Hour	
#Duration_Minute	no_of_cities	arrival_month	arrival_day	arrival_minute	
#arrival_hour	Dep_hour	Dep_min	Big Diff	AirLineEnc	SourceEnc	DestinationEnc	arrivalmonthEnc	ArrivDayEnc
def prediction(Total_Stops, Journey_month, Journey_day, Dep_hour,Dep_Min,arrival_hour,arrival_minute,Duration_Minute,
               AirLine,Source,Destination):
    test_df = pd.DataFrame(columns=Inputs)
    test_df.at[0,"Total_Stops"] = Total_Stops
    test_df.at[0,"Journey_month"] = Journey_month
    test_df.at[0,"Journey_day"] = Journey_day
    test_df.at[0,"Dep_hour"] = Dep_hour
    test_df.at[0,"Dep_Min"] = Dep_Min
    test_df.at[0,"arrival_hour"] = arrival_hour
    test_df.at[0,"arrival_minute"] = arrival_minute
    test_df.at[0,"Duration_Minute"] = Duration_Minute
    test_df.at[0,"AirLine"] = AirLine
    test_df.at[0,"Source"] = Source
    test_df.at[0,"Destination"] = Destination
    st.dataframe(test_df)
    result = Model.predict(test_df)[0]
    return result
Attachment file type: Desktop
message.txt
2.48 KB
def main():
    st.title("Bangolre Airlines")
    Total_Stops = st.selectbox("Total_Stops" , [0, 1, 2, 3, 4])
    Month_of_Journey = st.selectbox("Journey_month" , [1,2,3,4,5,6,7,8,9,10,11,12])
    Day_of_Journey = st.selectbox("Journey_day" , [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31])
    Dep_Hour = st.selectbox("Dep_hour" , [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
    Dep_Min = st.selectbox("Dep_Min" ,[0,5,10,15,20,25,30,35,40,45,50,55,60])
    Arrival_Hour = st.slider("arrival_hour" , min_value=1, max_value=24, value=0, step=1)
    Arrival_Min = st.slider("arrival_minute" , min_value=1, max_value=60, value=0, step=1)
    Duration_by_minute = st.slider("Duration_Minute" , min_value=75, max_value=2860, value=0, step=1)
    AirLine = st.selectbox("AirLine" , ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
       'Vistara Premium economy', 'Jet Airways Business',
       'Multiple carriers Premium economy', 'Trujet'])
    Source = st.selectbox("Source" , ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])
    Destination = st.selectbox("Destination" , ['New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'])

    if st.button("predict"):
        result = prediction(Total_Stops, Journey_month, Journey_day,
                            Dep_hour,Dep_Min,arrival_hour,arrival_minute,Duration_Minute,AirLine,Source,Destination)
        label = ["0"]
        st.text(f"The Price will {result}")

if name == 'main':
    main()
