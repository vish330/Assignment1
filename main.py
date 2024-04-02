import zipfile
import os
import pandas as pd
from datetime import datetime

def extract_time(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        timestamp_str = os.path.basename(zip_file_path).split('_')[0]
        load_time = datetime.strptime(timestamp_str, '%Y%m%d%H%M%S%f')
        return load_time

def new_csv(csv_filename, load_time):
    df = pd.read_csv(csv_filename)
    df['load_time'] = load_time
    return df

zip_file_path = '/home/nineleaps/Downloads/20240305124003123456_Extract 2.zip'
obj1 = ['/home/nineleaps/Desktop/sample.csv', '/home/nineleaps/Desktop/sample2.csv']

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall()

load_time = extract_time(zip_file_path)

for new_file in obj1:
    csv_file_path = os.path.join(os.getcwd(), os.path.normpath(new_file))
    df = new_csv(csv_file_path, load_time)
    output_filename = os.path.splitext(new_file)[0] + '_new.csv'
    df.to_csv(output_filename, index=False)

print("Done")
