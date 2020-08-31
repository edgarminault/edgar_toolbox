import streamlit as st
import pandas as pd
import numpy as np
from edgar_toolbox.lib import weather_forecast

user_input = st.text_input("Which city?")

forecast_df = weather_forecast(user_input)
st.dataframe(forecast_df[['applicable_date', 'max_temp', 'weather_state_name']])
