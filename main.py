import streamlit as st
import plotly.express as px

st.title("Weather forecast for the next couple of days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days for the forecasted days")
option = st.selectbox("Select Data to view", ("Temperature", "Sky"))
sub = st.subheader(f"{option} for the next {days} days in {place}")

dates = ["2022-25-20", "2022-26-20", "2022-27-20"]
temperature = [10,11,12]
figure = px.line(x=dates,y=temperature,labels={"x":"Dates","y":"temperature"})
st.plotly_chart(figure)