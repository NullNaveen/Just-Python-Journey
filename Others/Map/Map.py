import googlemaps

gmaps = googlemaps.Client(key='YOUR_API_KEY')

locations = [
    'New York, NY, United States',
    'Palo Alto, CA, United States',
    'Wilmington, DE, United States',
    'Plano, TX, United States'
]

for location in locations:
    geocode_result = gmaps.geocode(location)
    print(f"Latitude: {geocode_result[0]['geometry']['location']['lat']}, Longitude: {geocode_result[0]['geometry']['location']['lng']}")