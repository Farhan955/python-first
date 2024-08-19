import json
import csv

# Define the path to your GeoJSON file and the output CSV file
geojson_file = 'E:\\python_projects\\FirstProject\\data\\snohomish.geojson'
csv_file = 'E:\\python_projects\\FirstProject\\data\\snohomish_parcel_numbers.csv'

# Initialize an empty list to store pid values
pids = []

# Read the GeoJSON file line by line
with open(geojson_file, 'r') as f:
    for line in f:
        if line.strip():  # Skip empty lines
            try:
                feature = json.loads(line)
                pid = feature['properties']['pid']
                pids.append(pid)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
            except KeyError as e:
                print(f"Key error: {e}")

# Sort the pid values while preserving leading zeros
pids.sort(key=lambda x: (len(x), x))

# Write the sorted pid values to a CSV file
with open(csv_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['pid'])  # Write the header
    for pid in pids:
        csvwriter.writerow([pid])

print(f'Extracted pids have been written to {csv_file}')
