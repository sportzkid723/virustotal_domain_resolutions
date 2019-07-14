from urllib.request import urlopen
import json

#Create your own txt file, save it to same directory as code, and put its name in lieu of "domains.txt"
f = open("domains.txt", "w")

#Put your own api key here
api_key = 'xxxx'

def search(query):
    url = 'https://www.virustotal.com/vtapi/v2/ip-address/report?apikey=' + api_key
    ip_addr = query
    final_url = url + "&ip=" + ip_addr
    json_obj = urlopen(final_url)
    data = json.load(json_obj)

    for item in data['resolutions']:
        resolved = str(item['last_resolved'])
        f.write(resolved[:10]+ "\t" + item['hostname'] + "\n")

#Put the IP address you're testing here
search('149.56.18.177')
f.close()