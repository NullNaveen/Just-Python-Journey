import folium

locations = [
    ('New York, NY, United States', 40.7128, -74.0060),
    ('Palo Alto, CA, United States', 37.4419, -122.1419),
    ('Wilmington, DE, United States', 39.7392, -75.5444),
    ('Plano, TX, United States', 33.0537, -96.6989)
]

m = folium.Map(location=[40, -100], zoom_start=4)

for location, lat, lon in locations:
    folium.Marker([lat, lon], popup=location).add_to(m)

m.save('map.html')