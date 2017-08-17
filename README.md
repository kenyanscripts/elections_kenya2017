# elections_kenya2017
Scripts to download results for the 2017 elections


The scripts require python3 to run. The directory setup is for unix platforms. To run on a Windows platform you'll need to install Pytho3 and amend the scripts to your preferred download directory

eg, in unix, with open("iebc/mca_pollst_" + nowfile, 'w', newline='') as csvfile:
needs to be changed to with open("windows\directory\mca_pollst_" + nowfile, 'w', newline='') as csvfile:

The PollingStationCodes.csv file just contains the listing of all 40,883 gazetted polling stations 
