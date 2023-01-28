import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
phone_num = phonenumbers.parse("+918778748955")

print("PHONE NUMBER LOCATION AREA")

print(geocoder.description_for_number(phone_num,"en"))


from phonenumbers import carrier
service_number= phonenumbers.parse(ph, "ro")
print(carrier.name_for_number(service_number, "en"))