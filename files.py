import csv
import json
# import os
import tempfile
import  shutil
# os.path usage
import os
# pathlib usage (modern alternative)
from pathlib import Path


# Writing to a JSON file
data = {"name": "John", "age": 30}
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Reading from a JSON file
with open("data.json", "r") as json_file:
    data = json.load(json_file)
    print(data)

# Create a temporary file
with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_file.write(b"Temporary content")
    print(f"Temporary file created at: {temp_file.name}")

# Writing to a CSV file
header = ["Name", "Age", "City"]
rows = [["John", 30, "New York"], ["Alice", 25, "Los Angeles"]]
with open("people.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)  # Write header
    writer.writerows(rows)  # Write rows

# Reading from a CSV file
with open("people.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
