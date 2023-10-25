import pandas as pd

csv_path = 'path_to_csv_cartel'
csv_cartel = 'path_to_csv_file'
csv_in_file_name = 'in.csv'
csv_in_file = '%s/%s/%s' %(csv_path, csv_cartel, csv_in_file_name)

excel_out_file = '%s/%s/out.xlsx' %(csv_path, csv_cartel)

read_file = pd.read_csv(csv_in_file)
read_file.to_excel(excel_out_file, index=None, header=True)
