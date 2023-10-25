csv_path = 'path_to_csv'
csv_cartel = 'psth_to_dir'
csv_file_name = 'file.csv'
csv_out_file_name = 'file_out.csv'
csv_file = '%s/%s/%s' %(csv_path, csv_cartel, csv_file_name)
csv_out_file = '%s/%s/%s' %(csv_path, csv_cartel, csv_out_file_name)

infile=open(csv_file,"r")
outfile=open(csv_out_file,"w")
text=infile.readlines() 
for i in text:
    outfile.write(i.replace('object1_to_remove','').replace('object2_to_remove',''))
infile.close()
outfile.close()
