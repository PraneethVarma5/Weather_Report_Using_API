import requests,json

def kelvin_to_celsius(kelvin):
    return kelvin - 273

#kelvin_value = 300
#celsius_value = kelvin_to_celsius(kelvin_value)
#print(f"{kelvin_value} Kelvin is equal to {celsius_value:.2f} Celsius

###MYAPIKEY 09bca9ba57bcfc8925d1287a3bf6e603 ###
apikey="7040ea904442a45d6950ba584410ce59"#Youtube APIKEY
baseURL ="https://api.openweathermap.org/data/2.5/weather?q="
cityName=input("Enter your city:")
completeURL=baseURL+cityName+"&appid="+apikey
response=requests.get(completeURL)
data=response.json()
ct=data["main"]["temp"]
ctC=kelvin_to_celsius(ct)
fl=data["main"]["feels_like"]
flC=kelvin_to_celsius(fl)
ma=data["main"]["temp_max"]
maC=kelvin_to_celsius(ma)
mi=data["main"]["temp_min"]
miC=kelvin_to_celsius(mi)
#print(f"Current Temperature:{ctC:.2f}")
print(f"Current Temperature Feels like{flC:.2f}")
print(f"Maximum Temperature{maC:.2f}")
print(f"Minimum Temperature{miC:.2f}")