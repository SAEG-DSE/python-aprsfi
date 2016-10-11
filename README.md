# pyaprsfi
###Installation
***

>pip install aprsfi

###Basic usage:
	from aprsfi import API

	aprfi_api = API("your_api_key")
  response = aprfi_api.loc("OH7RDA")
  response.result #return 'ok'
	response.entries # list of all entries returned
	print(response.entries[0].fields)
	['lng', 'class',  'path',  'time',  'comment',  'lat',  'phg',  'type',
   'srccall',  'lasttime',  'name',  'dstcall',  'symbol']
	#you can call all intro fields as follows:
	first_entry = response.entries[0]
	first_entry.lat
	'63.06717'
	first_entry.lng
	'27.66050'
