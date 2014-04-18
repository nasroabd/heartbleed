import csv
import os

mycsv = csv.reader(open("./list.csv"))
for row in mycsv:
   print row[1]
   os.system("python exploit.py "+row[1])

