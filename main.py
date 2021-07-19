import phonenumbers
from phonenumbers import geocoder, carrier

def get_details(phone_number):
	# get country where the phone number is registered
	country_ch = phonenumbers.parse(phone_number, 'CH')
	country = geocoder.description_for_number(country_ch, 'en')
	if country == "":
		country = "Unknown"
	print(f"Country:  {country}")

	# get service provider for the phone number
	service_provider = phonenumbers.parse(phone_number, "RO")
	service_provider_name = carrier.name_for_number(service_provider, "en")
	if service_provider_name == '':
		service_provider_name = 'Unknown'
	print(f"Service Provider:  {service_provider_name}")
	print('')
	print('')

while True:
	print("Phone number MUST begin with country code")
	print('')
	phone_number = input("Enter phone number: ")

	if phone_number[0] != '+':
		print('Invalid phone number. Please try again')
		print('')
		phone_number = input("Enter phone number: ")
		if phone_number[0] == '+':
			get_details(phone_number)
	else:
		get_details(phone_number)
		
	choice = input('Run program again (y/n): ')
	if choice.lower() == "n" or choice.lower() == "no":
		break