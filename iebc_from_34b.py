import datetime

import requests
import csv

dlm = "_"
dest_folder = "iebc/34b/"
# dest_folder = "iebc\\34b\\" # For windows

url_base = 'https://forms.iebc.or.ke/downloadf34b/'

failed_stations = "failed_34b_" + (datetime.datetime.now().strftime("%Y%m%d_%H%M%S")) + ".csv"
rec_no = 0


def write_failed_stations(row_line, rec_no, error_reason):
    out_line = row_line[0] + "|" + row_line[1] + "|" + row_line[2] + "|" + "|" + error_reason
    with open(failed_stations, 'a') as the_file:
        if rec_no == 1:
            the_file.write("County Code|County Name|Constituency Code|Error_Reason\n")

        the_file.write(out_line + '\n')

with open('ConstituencyCodes.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='|')
    next(readCSV)
    for row in readCSV:
        county = row[0]
        county_name = row[1]
        const_code = row[2]
        
        print("Downloading form 34A from constituency " + str(const_code) + " in " + county_name)
        
        fileName = const_code + "-1_1_" + county + dlm + const_code + ".pdf"
        url = url_base + fileName
        dest = dest_folder + fileName
        print (url)

        try:
            req = requests.get(url)
            if req.status_code == 500:
                rec_no += 1
                write_failed_stations(row, rec_no, "HTTP 500 error: Probably form not uploaded yet")
                continue

            file = open(dest, 'wb')
            for chunk in req.iter_content(100000):
                file.write(chunk)
            file.close()
        except ConnectionError:
            rec_no += 1
            write_failed_stations(row, rec_no, "ConnectionError: Check connection to IEBC server")

        except FileNotFoundError:
            rec_no += 1
            write_failed_stations(row, rec_no, "FileNotFoundError: Check destination path")

        except IOError:
            rec_no += 1
            write_failed_stations(row, rec_no, "IOError: Probably space/permission issue")


