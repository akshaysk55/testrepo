import requests

class CountryLookupService:
    def __init__(self):
        self.api_url = "https://www.travel-advisory.info/api"
        
    def get_country_name(self, country_code):
        params = {"countrycode": country_code}
        response = requests.get(self.api_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            country_name = data["data"][country_code]["name"]
            return country_name
        else:
            return "Country not found"

def main():
    lookup_service = CountryLookupService()
    
    while True:
        country_code = input("Enter a country code (or 'exit' to quit): ").strip()
        
        if country_code.lower() == "exit":
            break
        
        country_name = lookup_service.get_country_name(country_code)
        print(f"The country with code {country_code} is {country_name}")

if __name__ == "__main__":
    main()
