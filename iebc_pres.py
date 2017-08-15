
import datetime
import json
import urllib.request as ur
import urllib.parse as par
import csv

# 

county_name = ['Mombasa']
county_name.append("Kwale")
county_name.append("Kilifi")
county_name.append("TanaRiver")
county_name.append("Lamu")
county_name.append("Taita-Taveta")
county_name.append("Garissa")
county_name.append("wajir")
county_name.append("Mandera")
county_name.append("Marsabit")
county_name.append("Isiolo")
county_name.append("Meru")
county_name.append("Tharaka-Nithi")
county_name.append("Embu")
county_name.append("Kitui")
county_name.append("Machakos")
county_name.append("Makueni")
county_name.append("Nyandarua")
county_name.append("Nyeri")
county_name.append("Kirinyaga")
county_name.append("Murang'a")
county_name.append("Kiambu")
county_name.append("Turkana")
county_name.append("WestPokot")
county_name.append("Samburu")
county_name.append("TransNzoia")
county_name.append("UasinGishu")
county_name.append("Elgeyo-Marakwet")
county_name.append("Nandi")
county_name.append("Baringo")
county_name.append("Laikipia")
county_name.append("Nakuru")
county_name.append("Narok")
county_name.append("Kajiado")
county_name.append("Kericho")
county_name.append("Bomet")
county_name.append("Kakamega")
county_name.append("Vihiga")
county_name.append("Bungoma")
county_name.append("Busia")
county_name.append("Siaya")
county_name.append("Kisumu")
county_name.append("HomaBay")
county_name.append("Migori")
county_name.append("Kisii")
county_name.append("Nyamira")
county_name.append("NairobiCity")
county_name.append("Diaspora")
county_name.append("Prisons")

nowfile=(datetime.datetime.now().strftime("%Y%m%d_%H%M%S")) + ".csv"

with open("c:\\temp\\iebc\\pres_" + nowfile, 'w', newline='') as csvfile: # Change as appropriate to directory in which to create csv

    resultwriter = csv.writer(csvfile, dialect='excel')
    resultwriter.writerow(["CountyCode","CountyName", "CandidateName","Position",  "Party",	"TotalVotes", "Percentage",
                           "Disputed", "Valid", "Rejected","Objected","Registered", "TimeStamp"])
    for x in range(1,50):
        county = str(x).zfill(2) 
        print ("Processing " + county + " - " + county_name[x-1])
        url_base = "https://public.rts.iebc.or.ke/jsons/round1/results/Kenya_Elections_Presidential/1/10"
        url_suffix = "/info.json"
        url = url_base + str(county) + url_suffix
       # print (url)
        dlim = "|"
        html = ur.urlopen(url).read()
        data = json.loads(html.decode('utf-8'))
        tstamp = data['timestamp']

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
                        
            resultwriter.writerow([str(county),county_name[x-1],candidate_name,candidate_pos, party, cand_votes, cand_perc,
                                   disputed, valid , rejected , objected, registered, dtime ])            
    
