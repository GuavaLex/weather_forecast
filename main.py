import streamlit as st
import plotly.express as px
from backened import get_data

st.title("Weather forecast for the next couple of days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days for the forecasted days")
option = st.selectbox("Select Data to view", ("Temperature", "Sky"))
sub = st.subheader(f"{option} for the next {days} days in {place}")

if place:

    filtered_data = get_data(place, days)

    if option == "Temperature":
        tempertures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"]for  dict in filtered_data]
        figure = px.line(x=dates, y=tempertures, labels={"x": "Dates", "y": "temperature"})
        st.plotly_chart(figure)
    if option == "Sky":
        images = {"Clear":"images/clear.png","Clouds":"images/cloud.png","Rain":"images/rain.png","Snow":"images/snow.png"}
        sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_condition]
        st.image(image_paths, width=115)
