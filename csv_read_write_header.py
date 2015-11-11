import csv
import os

inputFileName = "users.csv"
outputFileName = os.path.splitext(inputFileName)[0] + "   "

with open(inputFileName, newline='') as inFile, open(outputFileName, 'w', newline='') as outfile:
    r = csv.reader(inFile)
    w = csv.writer(outfile)

    next(r, None)  # skip the first row from the reader, the old header
    # write new header
    w.writerow(['id', 'firstname', 'lastname', 'email'])

    # copy the rest
    for row in r:
        w.writerow(row)
