import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import numpy as np
import math


'''
# Welcome to app :blue[Find DS Company]!

Welcome to our app, where we assist you in finding your ideal company as a data scientist. 

To begin the process, we kindly ask you to input three keywords that reflect your preferences and assign each a value from 1 to 10. These keywords will help our algorithm identify the best matching companies for you based on your specified criteria.

The higher the value, the more important the keyword is to you.
'''
# Variable 1 Slider
variable1 = st.slider('Select Rating of Criteria 1:', 1, 10, 1)
# Variable 2 Slider
variable2 = st.slider('Select Rating of Criteria 2:', 1, 10, 1)
# Variable 3 Slider
variable3 = st.slider('Select Rating of Criteria 3:', 1, 10, 1)
# Variable 4 Slider
variable4 = st.slider('Select Rating of Criteria 4:', 1, 10, 1)
# Variable 5 Slider
variable5 = st.slider('Select Rating of Criteria 5:', 1, 10, 1)

# Google Cloud Run URL
#url = 'https://bestcompany-nrfshmhfmq-ew.a.run.app/predict'

url = 'https://bestcompany-nrfshmhfmq-ew.a.run.app/predict'

dict_input = {'variable1': int(variable1), 'variable2': int(variable2),
              'variable3': int(variable3),
              'variable4': int(variable4),
              'variable5': int(variable5)}


response = requests.get(url, params=dict_input)

if response.status_code != 200:
    print('Error')

'''
st.divider() 

HOW THIS WORKS?

Once you've provided the necessary information, our advanced algorithm will analyze your data and generate a list of companies that align with  your preferences. You'll receive valuable insights about each company's  work-life balance, career growth opportunities, and collaborative  environment, enabling you to make an informed decision about your future workplace as a data scientist.

st.divider() 

Please find the overview of your ideal company as a data scientist as follows:

'''

st.write('Your ranking is:')
st.write(response.json())

