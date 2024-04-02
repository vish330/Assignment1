import zipfile
import os
import pandas as pd
from datetime import datetime

def extract_load_timestamp(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        timestamp_str = os.path.basename(zip_file_path).split('_')[0]
        load_timestamp = datetime.strptime(timestamp_str, '%Y%m%d%H%M%S%f')
        return load_timestamp

def process_csv(csv_filename, load_timestamp):
    df = pd.read_csv(csv_filename)
    df['load_timestamp'] = load_timestamp
    return df

zip_filename = '/home/nineleaps/Downloads/20240305124003123456_Extract 2.zip'
csv_files = ['/home/nineleaps/Desktop/sample.csv', '/home/nineleaps/Desktop/sample2.csv']

load_timestamp = extract_load_timestamp(zip_filename)

with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extractall()

for csv_file in csv_files:
    csv_file_path = os.path.join(os.getcwd(), os.path.normpath(csv_file))
    df = process_csv(csv_file_path, load_timestamp)
    output_filename = os.path.splitext(csv_file)[0] + '_new.csv'
    df.to_csv(output_filename, index=False)

print("Task completed successfully.")
