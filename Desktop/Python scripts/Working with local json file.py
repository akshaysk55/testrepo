import requests
import json

class CountryLookupService:
    def __init__(self):
        self.data = self._load_data_from_file()
        print("loaded")

    def _load_data_from_file(self):
        try:
            with open("data.json", "r") as json_file:
                print("Opened")
                data = json.load(json_file)
                #print(data)
            return data
        except FileNotFoundError:
            return {}

    def get_country_name(self, country_code):
        print("aaaa")
        #print(self.data['data'])
        if country_code in self.data['data']:
            print("Yes")
            return self.data["data"][country_code]["name"]
        else:
            return "Country not found"

def save_data_to_json():
    api_url = "https://www.travel-advisory.info/api"
    print("fetching")
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        with open("data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        print("Data saved to data.json successfully.")
    else:
        print("Failed to fetch data.")

def main():
    save_data_to_json()
    
    lookup_service = CountryLookupService()
    
    while True:
        country_code = input("Enter a country code (or 'exit' to quit): ").strip()
        
        if country_code.lower() == "exit":
            break
        
        country_name = lookup_service.get_country_name(country_code)
        print(f"The country with code {country_code} is {country_name}")

if __name__ == "__main__":
    main()
