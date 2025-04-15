import csv

def save_to_csv(data, filename='prayer_times.csv'):
    if not data:
        print("⚠️ No data to save.")
        return

    keys = data[0].keys()
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        print(f"✅ Data saved to {filename}")
    except Exception as e:
        print(f"❌ Error saving to CSV: {e}")
