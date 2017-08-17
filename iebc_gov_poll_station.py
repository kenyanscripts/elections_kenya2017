
import datetime
import json
import urllib.request as ur
import urllib.parse as par
import csv


nowfile=(datetime.datetime.now().strftime("%Y%m%d_%H%M%S")) + ".csv"

with open("iebc/gov_pollst_" + nowfile, 'w', newline='') as csvfile: # Give optional directory in which to create csv
   
    resultwriter = csv.writer(csvfile, dialect='excel')
    resultwriter.writerow(["CountyCode","CountyName","StationCode","StationName","CandidateName", "Position", "Party",	"VoteCount", "Percentage",
	"Disputed", "Valid", "Rejected","Objected","Registered","TimeStamp"])
#    with open('in.csv') as csvfile:
    with open('PollingStationCodes.csv') as csvfile:    
        readCSV = csv.reader(csvfile, delimiter='|')
        next (readCSV)
        for row in readCSV:      
            county = row[0]
            county_name = row[1]
            st_cd = row[2]
            st_name = row[3]

            print ("Processing " + str(st_cd)   + " - " + st_name)
            url_base = "https://public.rts.iebc.or.ke/jsons/round1/results/Kenya_Elections_Governor/1/"
            st_cd1 = "1" + str(st_cd)
            st_cd_url = st_cd1[0:0+4] + "/" + st_cd1[0:0+7] + "/" + st_cd1[0:0+11] + "/" + st_cd1[0:0+14] + "/" + st_cd1[0:0+16]
            
            url_suffix = "/info.json"
            url = url_base + st_cd_url + url_suffix
#            print (url)
            dlim = "|"
            html = ur.urlopen(url).read()
            try:
                data = json.loads(html.decode('utf-8'))
            except ValueError:
                print ("Error: " + str(st_cd)   + " - " + st_name)
                continue
            tstamp = data['timestamp']
            dtime = ""
            if(len(str(tstamp))==13):
                dtime = datetime.datetime.fromtimestamp(
                    int(str(tstamp)[:-3])
                ).strftime('%Y-%m-%d %H:%M:%S')
            
            parties = data['results']['parties']
            disputed = data['results']['abstention']
            valid = data['results']['blank']
            rejected = data['results']['null']
            objected = data['results']['census']
            registered = data['results']['participation'][0]['value']
            
            for i in parties:
                candidate_name = i['name']
                candidate_pos = i['ord']
                cand_votes = i['votes']['presential']
                cand_perc = i['votes']['percent']
                party = i['acronym']
                resultwriter.writerow([str(county), county_name, "'" + str(st_cd),st_name,candidate_name, candidate_pos, party, cand_votes, cand_perc, 
				disputed, valid , rejected , objected, registered, dtime ])
                #print (str(county) + dlim + county_name[x-1] + dlim + candidate_name + dlim + str(cand_votes) + dlim  + str(cand_perc) + dlim + dtime )
