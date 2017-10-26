# This script downloads the images of the Form 34A for the presidential election from each of the participating polling station
# Place polling station list in the same folder as the script. Script loops through each station
# The images are downloaded to the defined directory
# Make sure the ./iebc/images folder exists before running the script

import requests
import csv

dlm = "_"
dest_folder = "iebc/images/"
url_base = 'https://forms.iebc.or.ke/download/39696-1_1_'

with open('PollingStationCodes.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='|')
    next (readCSV)
    for row in readCSV:      
        county = row[0]
        county_name = row[1]
        st_cd = row[2]
        st_name = row[3]

        print ("Downloading form 34A from " + str(st_cd)   + " - " + st_name)
        fileName = str(st_cd[0:0+3]) + dlm + str(st_cd[3:3+3]) + dlm + str(st_cd[6:6+4]) + dlm + str(st_cd[10:10+3]) + dlm + str(st_cd[13:13+2]) + ".jpeg"
        url = url_base + fileName
        
        dest = dest_folder + fileName

        req = requests.get(url)
        file = open(dest, 'wb')
        for chunk in req.iter_content(100000):
            file.write(chunk)
        file.close()
