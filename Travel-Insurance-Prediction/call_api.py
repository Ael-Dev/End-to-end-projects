import requests

search_api_url = "http://127.0.0.1:8000/prediction" # endpoint

# case 1: response 1

input_data = {
  "Age": 34,
  "Employment_Type": 1,
  "GraduateOrNot": 1,
  "AnnualIncome": 500000,
  "FamilyMembers": 3,
  "ChronicDiseases": 1,
  "FrequentFlyer": 0,
  "EverTravelledAbroad": 0
}

res = requests.post(search_api_url, json=input_data)
print(res.json())