import json

single_name_location_success = lambda: {
	"command":"get",
	"result":"ok",
	"what":"loc",
	"found":1,
	"entries": [
		{
			"name":"OH7RDA",
			"type":"l",
			"time":"1267445689",
			"lasttime":"1270580127",
			"lat":"63.06717",
			"lng":"27.66050",
			"symbol":"\/#",
			"srccall":"OH7RDA",
			"dstcall":"APND12",
			"phg":"44603",
			"comment":"\/R,W,Wn,Tn Siilinjarvi",
			"path":"WIDE2-2,qAR,OH7AA"
		}
	]
}

another_single_name_location_success = lambda: {
	"command":"get",
	"result":"ok",
	"what":"loc",
	"found":1,
	"entries": [
		{
			"name":"OH7RDB",
			"type":"l",
			"time":"1267445689",
			"lasttime":"1270580127",
			"lat":"63.06717",
			"lng":"27.66050",
			"symbol":"\/#",
			"srccall":"OH7RDA",
			"dstcall":"APND12",
			"phg":"44603",
			"comment":"\/R,W,Wn,Tn Siilinjarvi",
			"path":"WIDE2-2,qAR,OH7AA"
		}
	]
}


many_names_locations_success = lambda: {
	"command":"get",
	"result":"ok",
	"what":"loc",
	"found":2,
	"entries": [
		{
			"name":"OH7RDA",
			"type":"l",
			"time":"1267445689",
			"lasttime":"1270580127",
			"lat":"63.06717",
			"lng":"27.66050",
			"symbol":"\/#",
			"srccall":"OH7RDA",
			"dstcall":"APND12",
			"phg":"44603",
			"comment":"\/R,W,Wn,Tn Siilinjarvi",
			"path":"WIDE2-2,qAR,OH7AA"
		},
		{
			"name":"OH7RDB",
			"type":"l",
			"time":"1267445689",
			"lasttime":"1270580127",
			"lat":"63.06717",
			"lng":"27.66050",
			"symbol":"\/#",
			"srccall":"OH7RDA",
			"dstcall":"APND12",
			"phg":"44603",
			"comment":"\/R,W,Wn,Tn Siilinjarvi",
			"path":"WIDE2-2,qAR,OH7AA"
		}
	]
}

fail_request = lambda: {
	"command":"get",
	"result":"fail",
	"description":"authentication failed: wrong API key"
}

single_name_wx_success = lambda: {
	"command":"get",
	"result":"ok",
	"what":"wx",
	"found":1,
	"entries": [
		{
			"name":"OH2TI",
			"time":"1270580978",
			"temp":"2.8",
			"pressure":"1022.1",
			"humidity":"88",
			"wind_direction":"270",
			"wind_speed":"2.7"
		}
	]
}

many_names_wxs_success = lambda: {
	"command":"get",
	"result":"ok",
	"what":"wx",
	"found":2,
	"entries": [
		{
			"name":"OH2TI",
			"time":"1270580978",
			"temp":"2.8",
			"pressure":"1022.1",
			"humidity":"88",
			"wind_direction":"270",
			"wind_speed":"2.7"
		},
		{
		"name":"OH2TE",
		"time":"1270580978",
		"temp":"2.8",
		"pressure":"1022.1",
		"humidity":"88",
		"wind_direction":"270",
		"wind_speed":"2.7"
		}
	]
}
