import phonenumbers
from test import num
import folium
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

key = '3ea2c07643f24da1b0ded0ef057a9d16'

#getting country name
ch_number = phonenumbers.parse(num,"CH")
location=geocoder.description_for_number(ch_number,"en")
print(location)

#getting service provider
service_num = phonenumbers.parse(num,"RO")
print(carrier.name_for_number(service_num,"en"))

geocoder = OpenCageGeocode(key)

query= str(location)

res= geocoder.geocode(query)
##print(res)

lat=res[0]['geometry']['lat']

lng=res[0]['geometry']['lng']

print(lat,lng)
myMap=folium.Map(location= [lat,lng],zoom_start= 9)
folium.Marker([lat,lng],popup= location).add_to(myMap)

#saving in HTML file

myMap.save("myLocation.html")