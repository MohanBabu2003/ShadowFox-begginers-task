def find_country(city_name):
    australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
    uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
    india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
    city_to_country = {
        **dict.fromkeys(australia, "Australia"),
        **dict.fromkeys(uae, "UAE"),
        **dict.fromkeys(india, "India")
    }
    country = city_to_country.get(city_name)
    
    if country:
        return f"{city_name} is in {country}"
    else:
        return f"{city_name} is not found in the predefined lists"
city_name = input("Enter a city name: ")
city_name = "Abu Dhabi"
result = find_country(city_name)
print(result)
