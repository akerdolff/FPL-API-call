# API call out test

import requests

def get_FPL_guidelines(year, state, household_size):
    base_url = "https://aspe.hhs.gov/topics/poverty-economic-mobility/poverty-guidelines/api/"
    url = f"{base_url}{year}/{state}/{household_size}"
    response = requests.get(url)
    
    if response.status_code == 200:
        FPL_data = response.json()
        return FPL_data
    else:
        print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")

state = "us"
year = int(input("Enter the year"))
household_size = int(input("Enter the household size (1 to 8)"))

FPL_threshold = get_FPL_guidelines(year, state, household_size)

if FPL_threshold:
    income = int(FPL_threshold['data']['income'])
    print(f"{year} Federal Poverty Threshold for a {household_size} person household in the continental united states: ${income:,}")




