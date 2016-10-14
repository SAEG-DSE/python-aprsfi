#python-aprsfi
###To install
***

>pip install aprsfi

###Basic usage:
***

####Basic location query using JSON
	
	from aprsfi import API

	aprfi_api = API("your_api_key")
  	response = aprfi_api.loc("OH7RDA")
  	response.result #return 'ok'
	response.entries # list of all entries returned
	print(response.entries[0].fields)
	['lng', 'class',  'path',  'time',  'comment',  'lat',  'phg',  'type',   'srccall',  'lasttime',  'name',  'dstcall',  'symbol']
	first_entry = response.entries[0]
	#you can call all fields as follows:
	first_entry.lat
	>'63.06717'
	first_entry.lng
	>'27.66050'
	
####Querying multiple targets using a single request

	from aprsfi import API
	
	aprfi_api = API("your_api_key")
  	response = aprfi_api.loc("OH7RDA","OH7AA")
	len(response.entries)
	>2
	
####Querying weather data
	
	from aprsfi import API

	aprfi_api = API("your_api_key")
  	response = aprfi_api.loc("OH2TI")
  	response.result #return 'ok'
	response.entries # list of all entries returned
	print(response.entries[0].fields
        ["name","time","temp","pressure","humidity","wind_direction",
   	"wind_speed"]
	first_entry = response.entries[0]
	#you can call all intro fields as follows:
	first_entry.temp
	>"2.8"
	first_entry,pressure
	>"1022.1"
