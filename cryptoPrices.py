import requests
import json

def jprint(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)
    
    return text

def jload(obj):

    loaded_json = json.loads(formatted_json)

    return loaded_json
    

def get_crypto_json():

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    if (response.status_code == 200):

        print ("Successful Request")

        return response.json()

    else :

        print ("Unsuccessful Request with error code :"+response.status_code)

        return None

crypto_json = get_crypto_json()

formatted_json = jprint(crypto_json)

loaded_json = jload(crypto_json)

euro_rate = loaded_json['bpi']['EUR']['rate']

usd_rate = loaded_json['bpi']['USD']['rate']

gbp_rate = loaded_json['bpi']['GBP']['rate']

updated_on_time = loaded_json['time']['updated']

print ('Last update on:',updated_on_time)

print ('1 BTC = '+euro_rate+' €')

print ('1 BTC = '+usd_rate+' $')

print ('1 BTC = '+gbp_rate+' £')
