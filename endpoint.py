import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = ''
# If the service is authenticated, set the key or token
key = ''

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "job_blue-collar": 0,
            "job_entrepreneur": 0,
            "job_housemaid": 0,
            "job_management": 1,
            "job_retired": 0,
            "job_self-employed": 0,
            "job_services": 0,
            "job_student": 0,
            "job_technician": 0,
            "job_unemployed": 0,
            "job_unknown": 0,
            "marital_married": 1,
            "marital_single": 0,
            "marital_unknown": 0,
            "education_basic_6y": 0,
            "education_basic_9y": 0,
            "education_high_school": 0,
            "education_illiterate": 0,
            "education_professional_course": 0,
            "education_university_degree": 1,
            "education_unknown": 0,
            "default_unknown": 1,
            "default_yes": 0,
            "housing_unknown": 0,
            "housing_yes": 1,
            "loan_unknown": 0,
            "loan_yes": 1,
            "contact_telephone": 0,
            "month_aug": 0,
            "month_dec": 1,
            "month_jul": 0,
            "month_jun": 0,
            "month_mar": 0,
            "month_may": 0,
            "month_nov": 0,
            "month_oct": 0,
            "month_sep": 0,
            "day_of_week_mon": 1,
            "day_of_week_thu": 0,
            "day_of_week_tue": 0,
            "day_of_week_wed": 0,
            "poutcome_nonexistent": 0,
            "poutcome_success": 1,
            "age": 0.5,
            "duration": 0.8,
            "campaign": 0,
            "pdays": 0.7,
            "previous": 0.9,
            "emp_var_rate": 0.1,
            "cons_price_idx": 0.6,
            "cons_conf_idx": 0.2,
            "euribor3m": 0.1,
            "nr_employed": 0.5
          },
          {
            "job_blue-collar": 1,
            "job_entrepreneur": 0,
            "job_housemaid": 0,
            "job_management": 0,
            "job_retired": 0,
            "job_self-employed": 0,
            "job_services": 0,
            "job_student": 0,
            "job_technician": 0,
            "job_unemployed": 0,
            "job_unknown": 0,
            "marital_married": 0,
            "marital_single": 1,
            "marital_unknown": 0,
            "education_basic_6y": 0,
            "education_basic_9y": 0,
            "education_high_school": 0,
            "education_illiterate": 0,
            "education_professional_course": 0,
            "education_university_degree": 1,
            "education_unknown": 0,
            "default_unknown": 1,
            "default_yes": 0,
            "housing_unknown": 1,
            "housing_yes": 0,
            "loan_unknown": 1,
            "loan_yes": 0,
            "contact_telephone": 0,
            "month_aug": 0,
            "month_dec": 0,
            "month_jul": 0,
            "month_jun": 0,
            "month_mar": 0,
            "month_may": 1,
            "month_nov": 0,
            "month_oct": 0,
            "month_sep": 0,
            "day_of_week_mon": 0,
            "day_of_week_thu": 0,
            "day_of_week_tue": 1,
            "day_of_week_wed": 0,
            "poutcome_nonexistent": 1,
            "poutcome_success": 0,
            "age": 0.4,
            "duration": 0.3,
            "campaign": 0.9,
            "pdays": 0.3,
            "previous": 0.8,
            "emp_var_rate": 0.7,
            "cons_price_idx": 0.2,
            "cons_conf_idx": 0.2,
            "euribor3m": 0.7,
            "nr_employed": 0.8
          },
      ]
    }

# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())


