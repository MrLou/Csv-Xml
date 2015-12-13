# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# NOTE: Folders cannot contain spaces because it will split argv!!!
# First row of the csv file(s) must be the header!

import glob
import os
import sys

delimiter = "," # "\t" "|" # delimiters typically used 

#  command-line arg optionally accepts a path or a file
#  Warning: does not handle SPACE_IN_PATH

print len(sys.argv) # debugging
if len(sys.argv) == 2:
    arg = sys.argv[1].lower()
    if arg.endswith('.csv'): # if a file (not a directory) then convert only that file
        csvFiles = [arg]
    else: # otherwise, assume it's a directory and convert all files within
        os.chdir(arg)
        csvFiles = glob.glob('*.csv')
# default to convert all CSV files in the CWD
elif len(sys.argv) == 1:
    csvFiles = glob.glob('*.csv')
else:
    print ("abort 1")
    os._exit(1)
    
for csvFileName in csvFiles:
    xmlFile = csvFileName[:-4] + '.xml'
    # read the CSV file as binary data in case there are non-ASCII characters
    csvFile = open(csvFileName, 'rb')
    csvData = csvFile.readlines()
    csvFile.close()
    tags = csvData.pop(0).strip().replace(' ', '_').split(delimiter)
    xmlData = open(xmlFile, 'w')
    xmlData.write('<?xml version="1.0"?>' + "\n")
    # there must be only one top-level tag
    xmlData.write('<csv_data>' + "\n")
    for row in csvData:
        rowData = row.strip().split(delimiter)
        xmlData.write('<row>' + "\n")
        for i in range(len(tags)):
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + rowData[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('</row>' + "\n")                
    xmlData.write('</csv_data>' + "\n")
    xmlData.close()

print ('Done!') 

#now testing IDE handlling exceptions
#pass example

try:
    pass
except Exception:
    pass

#fail example

try:
    pass
except Exception as e:
    print (e)
    pass