import csv
import os

def splitCSVByColumn(file_path, path_out, columName):
    if (not os.path.isdir(path_out)):
        os.mkdir(path_out)
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        headers = next(reader)

        nomFile = ""
        for row in reader:
            if (nomFile != row[columName]):
                nomFile = row[columName]
                if 'fou' in locals():
                    if fou is not None:
                        fou.close()
                fou = open(path_out + nomFile + '.csv','w',newline='')
                current_out_writer = csv.DictWriter(fou, delimiter=';', fieldnames=headers)
                current_out_writer.writeheader()
            current_out_writer.writerow(row)
        if 'fou' in locals():
            if fou is not None:
                fou.close()
    return

file_path = 'inputFile.csv'
path_out = './output_dir/'
columName = 'COLUMNAME'

splitCSVByColumn(file_path, path_out, columName)