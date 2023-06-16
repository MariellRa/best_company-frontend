import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import numpy as np
import math

keyword1 = 'Work-Life Balance'
keyword2 = 'Salary'
keyword3 = 'Benefits'
keyword4 = 'Company Size'
keyword5 = 'Good Management'


'''
# Welcome to app :blue[Find DS Company]!

Welcome to our app, where we assist you in finding your ideal company as a data scientist. 

To begin the process, we kindly ask you to input three keywords that reflect your preferences and assign each a value from 1 to 10. These keywords will help our algorithm identify the best matching companies for you based on your specified criteria.

The higher the value, the more important the keyword is to you.

'''
# Variable 1 Slider
variable1 = st.slider(f'Select Rating of {keyword1}', 1, 10, 1)
# Variable 2 Slider
variable2 = st.slider(f'Select Rating of {keyword2}:', 1, 10, 1)
# Variable 3 Slider
variable3 = st.slider(f'Select Rating of {keyword3}:', 1, 10, 1)
# Variable 4 Slider
variable4 = st.slider(f'Select Rating of {keyword4}:', 1, 10, 1)
# Variable 5 Slider
variable5 = st.slider(f'Select Rating of {keyword5}:', 1, 10, 1)

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
st.write(list(response.json()['Sorted_Company'])[-1])

'''
The input you provided us:
Work-Life Balance: 8/10
Career Growth Opportunities: 6/10
Collaborative Environment: 4/10

2) Meta is known for its exceptional work-life balance, offering you the flexibility and support you need to maintain a healthy work-life integration. You'll have the freedom to pursue personal interests while excelling in your professional responsibilities.
'''

# Company Dashboard
company = list(response.json()['Sorted_Company'])[-1]

company_name = f'{company}'

meta = [0.027,0.050,0.164,0.301,0.457]

apple = [0.039,0.020,0.122,0.291,0.528]

google = [0.005,0.014,0.043,0.271,0.667]

amazon = [0.063,0.048,0.104,0.348,0.437]

microsoft = [0.016,0.013,0.120,0.301,0.550]

total = [0.030, 0.029, 0.111, 0.302, 0.528]


variable_dict = {keyword1: variable1, keyword2: variable2, keyword3: variable3,
                 keyword4: variable4, keyword5: variable5}

sorted_variable_dict = sorted(variable_dict.items(), key=lambda x:x[1])

#st.write(sorted_variable_dict)

work_life_intro = f'{company_name} is know for good {keyword1}'

if company == 'Apple':
    'Here is some info about Apple'

if company == 'Meta':
    st.write('Meta Platforms, Inc., formerly named Facebook, Inc., and TheFacebook, Inc., is an American multinational technology conglomerate based in Menlo Park, California. The company owns Facebook, Instagram, and WhatsApp, among other products and services.')
    for i in range(2):
        if list(variable_dict)[i] == keyword1:
            X = f'{company_name} is best know for having a great work-life balance...'
        if list(variable_dict)[i] == keyword2:
            X = f'{company_name} is best know for having a great salary...'
        if list(variable_dict)[i] == keyword3:
            X = f'{company_name} is best know for having great Benefits...'
        if list(variable_dict)[i] == keyword4:
            X = f'{company_name} is best know for having a great company size...'
        if list(variable_dict)[i] == keyword5:
            X = f'{company_name} is best know for having a great management...'
    for i in range(2):
        if list(variable_dict)[i] == keyword1:
            Y = f'In addition to this...{company_name} is best know for having a great work-life balance...'
        if list(variable_dict)[i] == keyword2:
            Y = f'In addition to this...{company_name} is best know for having a great salary...'
        if list(variable_dict)[i] == keyword3:
            Y = f'In addition to this...{company_name} is best know for having great Benefits...'
        if list(variable_dict)[i] == keyword4:
            Y = f'In addition to this...{company_name} is best know for having a great company size...'
        if list(variable_dict)[i] == keyword5:
            Y = f'In addition to this...{company_name} is best know for having a great management...'
    st.write(X + Y)

if company == 'Microsoft':
    st.write('Microsoft Corporation is an American multinational technology corporation headquartered in Redmond, Washington. Microsofts best-known software products are the Windows line of operating systems, the Microsoft Office suite, and the Internet Explorer and Edge web browsers.')
    for i in range(2):
        if list(variable_dict)[i] == keyword1:
            X = f'{company_name} is best know for having a great work-life balance...'
        if list(variable_dict)[i] == keyword2:
            X = f'{company_name} is best know for having a great salary...'
        if list(variable_dict)[i] == keyword3:
            X = f'{company_name} is best know for having great Benefits...'
        if list(variable_dict)[i] == keyword4:
            X = f'{company_name} is best know for having a great company size...'
        if list(variable_dict)[i] == keyword5:
            X = f'{company_name} is best know for having a great management...'
    for i in range(2):
        if list(variable_dict)[i] == keyword1:
            Y = f'In addition to this...{company_name} is best know for having a great work-life balance...'
        if list(variable_dict)[i] == keyword2:
            Y = f'In addition to this...{company_name} is best know for having a great salary...'
        if list(variable_dict)[i] == keyword3:
            Y = f'In addition to this...{company_name} is best know for having great Benefits...'
        if list(variable_dict)[i] == keyword4:
            Y = f'In addition to this...{company_name} is best know for having a great company size...'
        if list(variable_dict)[i] == keyword5:
            Y = f'In addition to this...{company_name} is best know for having a great management...'
    st.write(X + Y)

if company == 'Amazon':
    st.write('Amazon.com, Inc. is an American multinational technology company focusing on e-commerce, cloud computing, online advertising, digital streaming, and artificial intelligence.')
    for i in range(2):
        if list(variable_dict)[i] == keyword1:
            X = f'{company_name} is best know for having a great work-life balance...'
        if list(variable_dict)[i] == keyword2:
            X = f'{company_name} is best know for having a great salary...'
        if list(variable_dict)[i] == keyword3:
            X = f'{company_name} is best know for having great Benefits...'
        if list(variable_dict)[i] == keyword4:
            X = f'{company_name} is best know for having a great company size...'
        if list(variable_dict)[i] == keyword5:
            X = f'{company_name} is best know for having a great management...'
    for i in range(2):
        if list(variable_dict)[i] == keyword1:
            Y = f'In addition to this...{company_name} is best know for having a great work-life balance...'
        if list(variable_dict)[i] == keyword2:
            Y = f'In addition to this...{company_name} is best know for having a great salary...'
        if list(variable_dict)[i] == keyword3:
            Y = f'In addition to this...{company_name} is best know for having great Benefits...'
        if list(variable_dict)[i] == keyword4:
            Y = f'In addition to this...{company_name} is best know for having a great company size...'
        if list(variable_dict)[i] == keyword5:
            Y = f'In addition to this...{company_name} is best know for having a great management...'
    st.write(X + Y)

if company == 'Google':
    st.write('Google LLC is an American multinational technology company focusing on artificial intelligence, online advertising, search engine technology, cloud computing, computer software, quantum computing, e-commerce, and consumer electronics.')
    for i in range(2):
        if list(variable_dict)[i] == keyword1:
            X = f'{company_name} is best know for having a great work-life balance...'
        if list(variable_dict)[i] == keyword2:
            X = f'{company_name} is best know for having a great salary...'
        if list(variable_dict)[i] == keyword3:
            X = f'{company_name} is best know for having great Benefits...'
        if list(variable_dict)[i] == keyword4:
            X = f'{company_name} is best know for having a great company size...'
        if list(variable_dict)[i] == keyword5:
            X = f'{company_name} is best know for having a great management...'
    for i in range(2):
        if list(variable_dict)[i] == keyword1:
            Y = f'In addition to this...{company_name} is best know for having a great work-life balance...'
        if list(variable_dict)[i] == keyword2:
            Y = f'In addition to this...{company_name} is best know for having a great salary...'
        if list(variable_dict)[i] == keyword3:
            Y = f'In addition to this...{company_name} is best know for having great Benefits...'
        if list(variable_dict)[i] == keyword4:
            Y = f'In addition to this...{company_name} is best know for having a great company size...'
        if list(variable_dict)[i] == keyword5:
            Y = f'In addition to this...{company_name} is best know for having a great management...'
    st.write(X + Y)

'''
3) Wordcloud per company. 

4) Rating with chart.

5) 3 most highly-valued cons/pros per company.

6) Interviews 
'''


