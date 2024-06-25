import csv
import pandas as pd
import os

# Set the data type for each column
dtype_spec = {
    'tow': int,
    'wn': int,
    'sv': int,
    'hexdata': str
}

def process_csv(input_file, output_file):
    data = pd.read_csv(input_file, header=None, names=['tow', 'wn', 'sv', 'hexdata'], dtype=dtype_spec)
    #found = False
    new_data = []
    flag = 0
    for index, row in data.iterrows():
        wn = row['wn']
        tow = row['tow']
        sv = row['sv']
        hexdata = row['hexdata']
        if tow % 30 == 25 and hexdata[11]=='0':
            print("original hexdata: ", hexdata)
            # modify IONO
            hexdata = hexdata[0:11]+'1'+hexdata[12:]
            print("update hexdata: ", hexdata)

        new_data.append({'tow': tow, 'wn': wn, 'sv': sv, 'hexdata': hexdata})
    CSVProcess(new_data, output_file)

def CSVProcess(data,output_file):
    new_df = pd.DataFrame(data)
    new_df.to_csv(output_file, index=False, header=False)


def process_all_csv_files(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            input_file = os.path.join(folder_path, file_name)
            output_file = os.path.join(output_folder, file_name)
            process_csv(input_file, output_file)


folder_path = '.\CSVForINAV\CSVForSvid'
output_folder = 'ModifyGST'


process_all_csv_files(folder_path, output_folder)