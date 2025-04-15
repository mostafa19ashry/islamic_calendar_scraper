from scraper import get_prayer_times, get_monthly_prayer_times, get_prayer_times_by_date
from csv_saver import save_to_csv
from utils import normalize_input, ask_user_to_save, ask_day_or_month, format_prayer_times_output, get_current_month_and_year

def main():
    print("📅 Welcome to Islamic Prayer Times App")
    
    city = normalize_input(input("Enter city name: "))
    country = normalize_input(input("Enter country name: "))
    
    mode = ask_day_or_month()

    if mode == 'today':
        custom_date = input("Do you want to enter a specific date? (yes/no): ").strip().lower()
        if custom_date == 'yes':
            date_str = input("Enter date in format YYYY-MM-DD: ").strip()
            timings = get_prayer_times_by_date(city, country, date_str)
            display_date = date_str
        else:
            timings = get_prayer_times(city, country)
            display_date = 'Today'

        if timings:
            print(format_prayer_times_output(city, country, timings, date=display_date))
            if ask_user_to_save():
                prayer_data = [{
                    'date': display_date,
                    'fajr': timings['Fajr'],
                    'dhuhr': timings['Dhuhr'],
                    'asr': timings['Asr'],
                    'maghrib': timings['Maghrib'],
                    'isha': timings['Isha']
                }]
                save_to_csv(prayer_data)
        else:
            print("❌ Could not fetch prayer times.")

    elif mode == 'month':
        month, year = get_current_month_and_year()
        data = get_monthly_prayer_times(city, country, month, year)

        if data:
            prayer_data = []
            for day_info in data:
                date = day_info['date']['gregorian']['date']
                timings = day_info['timings']
                prayer_data.append({
                    'date': date,
                    'fajr': timings['Fajr'].split(' ')[0],
                    'dhuhr': timings['Dhuhr'].split(' ')[0],
                    'asr': timings['Asr'].split(' ')[0],
                    'maghrib': timings['Maghrib'].split(' ')[0],
                    'isha': timings['Isha'].split(' ')[0]
                })
            
            print(f"\n📆 Prayer times for {city}, {country} - {month}/{year}")
            print("-" * 40)
            print(f"Total Days: {len(prayer_data)}")
            print("-" * 40)

            if ask_user_to_save():
                save_to_csv(prayer_data, filename="monthly_prayer_times.csv")
        else:
            print("❌ Could not fetch prayer times for the month.")
    else:
        print("⚠️ Invalid choice. Please enter 'today' or 'month'.")

if __name__ == "__main__":
    main()
