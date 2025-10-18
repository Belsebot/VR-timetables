import requests
import sys
from datetime import timedelta
import datetime

def get_train(mista,mihin):                                                                              #Function to get timetable information from net service
	url = "http://rata.digitraffic.fi/api/v1/live-trains/station/{}/{}?limit=3".format(mista,mihin)        #address for timetable information
	data = requests.get(url)

	return data.json()

def main(mista_,mihin_):                                                                                 #Main function which get wanted stations and shows timetable information

	if (mista_ == mihin_):                                                                                 #Checks if entered stations are same and then sets stations to default value
		mista_ = "toijala"
		mihin_ = "tampere"

	match mista_:                                                                                          #Convert entered station to code which can send to net service
		case "toijala":
			mista_ = "Toijala"
			mista = "TL"
		case "viiala":
			mista_ = "Viiala"
			mista = "VIA"
		case "lempaala":
			mista_ = "Lempaala"
			mista = "LPÄ"
		case "tampere":
			mista_ = "Tampere"
			mista = "TPE"
		case "helsinki":
			mista_ = "Helsinki"
			mista = "HKI"
		case "hameenlinna":
			mista_ = "Hameenlinna"
			mista = "HL"
		case "oulu":
			mista_ = "Oulu"
			mista = "OL"
		case "rovaniemi":
			mista_ = "Rovaniemi"
			mista = "ROI"
		case "pasila":
			mista_ = "Pasila"
			mista = "PSL"
		case "tikkurila":
			mista_ = "Tikkurila"
			mista = "TKL"
		case "jyvaskyla":
			mista_ = "Jyvaskyla"
			mista = "JY"
		case "riihimaki":
			mista_ = "Riihimaki"
			mista = "RI"
		case "turku":
			mista_ = "Turku"
			mista = "TKU"
		case "turkusatama":
			mista_ = "Turku Satama"
			mista = "TUS"
		case _:                                                                                    #if not found entered station use default values
			mista_ = "Toijala"
			mista = "TL"
			mihin_ = "tampere"

	match mihin_:
		case "toijala":
			mihin_ = "Toijala"
			mihin = "TL"
		case "viiala":
			mihin_ = "Viiala"
			mihin = "VIA"
		case "lempaala":
			mihin_ = "Lempaala"
			mihin = "LPÄ"
		case "tampere":
			mihin_ = "Tampere"
			mihin = "TPE"
		case "helsinki":
			mihin_ = "Helsinki"
			mihin = "HKI"
		case "hameenlinna":
			mihin_ = "Hameenlinna"
			mihin = "HL"
    	case "oulu":
      		mihin_ = "Oulu"
      		mihin = "OL"
    	case "rovaniemi":
      		mihin_ = "Rovaniemi"
      		mihin = "ROI"
    	case "pasila":
      		mihin_ = "Pasila"
      		mihin = "PSL"
    	case "tikkurila":
      		mihin_ = "Tikkurila"
      		mihin = "TKL"
    	case "jyvaskyla":
      		mihin_ = "Jyvaskyla"
      		mihin = "JY"
    	case "riihimaki":
      		mihin_ = "Riihimaki"
      		mihin = "RI"
		case "turku":
			mihin_ = "Turku"
			mihin = "TKU"
		case "turkusatama":
			mihin_ = "Turku Satama"
			mihin = "TUS"
		case _:                                                                                #if not found entered station use default values
			mihin_ = "Tampere"
			mihin = "TPE"
			mista_ = "Toijala"
			mista = "TL"

	print ("Junat {} {}".format(mista_,mihin_))                                              #Print stations where to where
	junat=get_train(mista,mihin)                                                              #get trains which are running through wanted stations

	for a in range(0,3):
		juna=(junat[a]['trainNumber'])                                                            #get train number

		luku=len(junat[a]['timeTableRows'])                                                    #get size of timetable

		for b in range(0,luku):

			asema=(junat[a]['timeTableRows'][b]['stationShortCode'])                              #Get station
			tyyppi=(junat[a]['timeTableRows'][b]['type'])                                          #Get status which informs is train arriving or departuring
			pysahtyy=(junat[a]['timeTableRows'][b]['trainStopping'])                                #get information is train stopping at wanted station
			raide=(junat[a]['timeTableRows'][b]['commercialTrack'])                                  #get track number
			aika=(junat[a]['timeTableRows'][b]['scheduledTime'])                                       #get time when train is arriving or departuring

			aika_asetus=datetime.datetime.strptime(aika,'%Y-%m-%dT%H:%M:%S.%fZ')                        #convert time to correct format
			offset=datetime.datetime.now().astimezone().utcoffset()                                      #get offset for UTC time
			local_aika=aika_asetus + offset                                                              #sets correct time

			kello=local_aika.strftime("%H:%M")

			if (asema==mista and tyyppi=="DEPARTURE" and pysahtyy==True):                              #When train is leaving from wanted station
				print ("Juna: {:5} Lahtee: {} Raiteelta: {}".format(juna,kello,raide))                    #shows train number, time and track number

			if (asema==mihin and tyyppi=="ARRIVAL" and pysahtyy==True):                                #When train is arriving to wanted station
				print ("Juna: {:5} Saapuu: {} Raiteelle: {}".format(juna,kello,raide))                    #shows train number, time and track number
				break

if __name__ == '__main__':                                                      #Main

	temp=sys.argv[1:]                                                            #Get stations entered by user

	if (len(temp)==2):                                                          #If correct amount stations entered
		main(temp[0],temp[1])                                                     #Then run main program
	else:                                                                       #Else show instructions
		print ("Enter stations where to where")
	x=datetime.datetime.now()                                                    #Get date and time
	time=x.strftime("%A %H:%M")
	print(time)                                                                  #shows Time
