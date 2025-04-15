from datetime import datetime

def normalize_input(text):
    return text.strip().title()

def ask_user_to_save():
    choice = input("Do you want to save the prayer times to a CSV file? (yes/no): ")
    return choice.strip().lower() == 'yes'

def ask_day_or_month():
    choice = input("Do you want prayer times for today or the whole month? (today/month): ")
    return choice.strip().lower()

def format_prayer_times_output(city, country, timings, date='Today'):
    output = f"\n🕌 Prayer Times for {city}, {country} - {date}:\n"
    output += "-" * 40 + "\n"
    for prayer, time in timings.items():
        output += f"{prayer:<10}: {time}\n"
    output += "-" * 40 + "\n"
    return output

def get_current_month_and_year():
    now = datetime.now()
    return now.month, now.year
