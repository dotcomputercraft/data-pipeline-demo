from functions import *
import time
import datetime

CONFIG_PATH = "configs/config.json"
config = load_config(CONFIG_PATH)

print("Starting data pipeline at ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print("----------------------------------------------")

# Step 1: extract video IDs
t0 = time.time()
data = extract(config["input_file"])
t1 = time.time()
print("Step 1: Done")
print("---> Video IDs downloaded in", str(t1-t0), "seconds", "\n")

# Step 2: extract transcripts for videos
t0 = time.time()
transformed_data = transform(data, config["transformation_multiplier"])
t1 = time.time()
print("Step 2: Done")
print("---> Transcripts downloaded in", str(t1-t0), "seconds", "\n")

# Step 3: Transform data
t0 = time.time()
load(transformed_data, config["output_file"])
t1 = time.time()
print("Step 3: Done")
print("---> Data transformed in", str(t1-t0), "seconds", "\n")

print("Step 4: Done")
print("---> Embeddings generated in", str(t1-t0), "seconds", "\n")