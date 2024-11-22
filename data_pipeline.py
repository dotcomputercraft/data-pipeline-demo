from functions import *
import time
import datetime


print("Starting data pipeline at ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print("----------------------------------------------")

# Step 0: load ETL job config

CONFIG_PATH = "configs/config.json"
config = load_config(CONFIG_PATH)
print("Step o: Done")


# Step 1: extract video IDs
t0 = time.time()
data = extract(config["input_file"])
print(f"extract data: {data}")
t1 = time.time()
print("Step 1: Done")
print("---> Extracts data from a JSON file in", str(t1-t0), "seconds", "\n")

# Step 2: Transform data
t0 = time.time()
transformed_data = transform(data, config["transformation_multiplier"])
t1 = time.time()
print("Step 2: Done")
print("---> Transforms the data by multiplying each number in", str(t1-t0), "seconds", "\n")

# Step 3: Loads transformed data into a JSON file
t0 = time.time()
load(transformed_data, config["output_file"])
t1 = time.time()
print("Step 3: Done")
print("---> Loads transformed data into a JSON file in", str(t1-t0), "seconds", "\n")

print("Step 4: Done")
print(f"Transformed data: {transformed_data}")
print("---> transformed data in", str(t1-t0), "seconds", "\n")