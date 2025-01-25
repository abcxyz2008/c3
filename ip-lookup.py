import requests
import time
import sys
ip = sys.argv[1]
def ur_dady():
	try:
		response  = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query")
		data = response.json()		
		print(f"~ IP :{data['query']}")
		print(f"~ Status : {data['status']}")
		print(f"~ Country : {data['country']}")
		print(f"~ Region : {data['region']}")
		print(f"~ RegionName : {data['regionName']}")
		
		print(f"~ City : {data['city']}")
		print(f"~ Latitude : {data['lat']}")
		print(f"~ Longitude : {data['lon']}")
		print(f"~ Continent : {data['continent']}")
		print(f"~ Continent Code : {data['continentCode']}")
		print(f"~ Offset : {data['offset']}")
		print(f"~ Currency : {data['currency']}")
		print(f"~ Isp : {data['isp']}")
		
		print(f"~ Zipcode : {data['zip']}")
		print(f"~ Org : {data['org']}")
		print(f"~ TimeZone : {data['timezone']}")
		print(f"~ As : {data['as']}")
		print(f"~ AsName : {data['asname']}")
		print(f"~ Reverse : {data['reverse']}")
		print(f"~ Mobile : {data['mobile']}")
		print(f"~ Proxy : {data['proxy']}")
		print(f"~ Hosting : {data['hosting']}")
		
	except Exception as e:
		print (f"Wrong IP V4/V6 format please try again: {e}")
ur_dady();	

