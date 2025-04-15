import requests

def get_prayer_times(city, country):
    url = "http://api.aladhan.com/v1/timingsByCity"
    params = {
        'city': city,
        'country': country,
        'method': 2
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['code'] == 200:
            return data['data']['timings']
    else:
        print(f"Error: Status code {response.status_code}")
    return None


def get_prayer_times_by_date(city, country, date_str):  # YYYY-MM-DD
    url = f"http://api.aladhan.com/v1/timingsByCity/{date_str}"
    params = {
        'city': city,
        'country': country,
        'method': 2
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['code'] == 200:
            return data['data']['timings']
        else:
            print("Error: Could not retrieve prayer times.")
    else:
        print(f"Error: Status code {response.status_code}")
    return None


def get_monthly_prayer_times(city, country, month, year):
    url = "http://api.aladhan.com/v1/calendarByCity"
    params = {
        'city': city,
        'country': country,
        'method': 2,
        'month': month,
        'year': year
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['code'] == 200:
            return data['data']
    else:
        print(f"Error: Status code {response.status_code}")
    return None
