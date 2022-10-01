# Get the Score from ESG Enterprise Website

import requests
import json

# Change the security token to your own.
security_token = '5951b3f9107fa3ec19dd2efcb5e6d495'
url = 'https://tf689y3hbj.execute-api.us-east-1.amazonaws.com/prod/authorization/search?q='

def get_environment_information_for_company(company_name):
    r = requests.get(url + company_name + '&token=' + security_token)
    data = r.json()
    environment_score = data[0]['environment_score']
    environment_grade = data[0]['environment_grade']
    environment_level = data[0]['environment_level']
    return (environment_score, environment_grade, environment_level)

print(get_environment_information_for_company("Microsoft"))