import json

# Explore the structure of data.
filename = 'data/eq_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# Make a list of all earthquakes.
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

# Extract magnitude and location data.
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])
