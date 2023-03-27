import streamlit as st

st.title("Weather forecast for the next couple of days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days for the forecasted days")
option = st.selectbox("Select Data to view", ("Temperature", "Sky"))
sub = st.subheader(f"{option} for the next {days} days in {place}")