import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt


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
**HOW THIS WORKS?**
Once you've provided the necessary information, our advanced algorithm will analyze your data and generate a list of companies that align with  your preferences. You'll receive valuable insights about each company's  work-life balance, career growth opportunities, and collaborative  environment, enabling you to make an informed decision about your future workplace as a data scientist.

## :trophy: RESULTS :trophy: 

##### Please find the overview of your ideal company as a data scientist as follows:
'''
st.write('1) First of all, your ideal company is:')
st.write(response.json())

'''
The input you provided us:
Work-Life Balance: 8/10
Career Growth Opportunities: 6/10
Collaborative Environment: 4/10

2) Meta is known for its exceptional work-life balance, offering you the flexibility and support you need to maintain a healthy work-life integration. You'll have the freedom to pursue personal interests while excelling in your professional responsibilities.
'''

companies = ['meta', 'apple', 'google', 'amazon', 'microsoft']

ratings = {
    'meta': [0.027, 0.050, 0.164, 0.301, 0.457],
    'apple': [0.039, 0.020, 0.122, 0.291, 0.528],
    'google': [0.005, 0.014, 0.043, 0.271, 0.667],
    'amazon': [0.063, 0.048, 0.104, 0.348, 0.437],
    'microsoft': [0.016, 0.013, 0.120, 0.301, 0.550],
}

ratings['total'] = [sum(ratings[company]) for company in companies]

plt.figure(figsize=(8, 6))
plt.bar(companies, ratings['total'])
plt.xlabel('Companies')
plt.ylabel('Total Ratings')
plt.title('Total Ratings for Companies')
plt.show()

'''
3) Wordcloud per company. 

4) Rating with chart.

5) 3 most highly-valued cons/pros per company.

6) Interviews 
'''


