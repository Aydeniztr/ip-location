from urllib.request import urlopen
from sys import argv
import json 

banner = r'''

    ________    __ __  __    ____  _________  ______________  _   __
   /  _/ __ \__/ // /_/ /   / __ \/ ____/   |/_  __/  _/ __ \/ | / /
   / // /_/ /_  _  __/ /   / / / / /   / /| | / /  / // / / /  |/ / 
 _/ // ____/_  _  __/ /___/ /_/ / /___/ ___ |/ / _/ // /_/ / /|  /  
/___/_/     /_//_/ /_____/\____/\____/_/  |_/_/ /___/\____/_/ |_/   
                                                                                                    
                                        [by Ahmet Yigit AYDENIZ]
usage:

python3 ip.py <"ip_adress">

example:

python3 ip.py "24.48.0.1"

'''

# ip_adress = "24.48.0.1"

if len(argv) <= 1:
	print(banner)
else:
	ip_adress = argv[1]
	text = ("http://ip-api.com/json/"+ip_adress)
	data = urlopen(text)
	pdata = json.loads(data.read())

	try:
		print("\n")	
		print("-"*40)
		print("query:",pdata["query"])
		print("status:",pdata["status"])
		print("country:",pdata["country"])
		print("country_code",pdata["countryCode"])
		print("region:",pdata["region"])
		print("region_name:",pdata["regionName"])
		print("city:",pdata["city"])
		print("zip:",pdata["zip"])
		print("lat:",pdata["lat"])
		print("lon:",pdata["lon"])
		print("timezone:",pdata["timezone"])
		print("isp:",pdata["isp"])
		print("org:",pdata["org"])
		print("as:",pdata["as"])
		print("-"*40)
		print("\n")
		exit()
	except Exception:
		print("ip_adress not valid")
		print("-"*40)
		print("\n")
		exit()