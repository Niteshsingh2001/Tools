import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder, carrier

# Check Phone Number

def check(country_code,phone_no) -> None:

    user_no = f"+{country_code}{phone_no}"
    phoneNumber = phonenumbers.parse(user_no)
    valid = phonenumbers.is_valid_number(phoneNumber)

    if valid : 
        timeZone = timezone.time_zones_for_number(phoneNumber)
        Carrier = carrier.name_for_number(phoneNumber, 'en')
        Region = geocoder.description_for_number(phoneNumber, 'en')
        return f"Number : {phoneNumber}\nTime Zone : {timeZone}\nCarrier : {Carrier}\nLocation : {Region}"
    else:
        return("Please enter a valid number")
    
    
print(check(91,445))

    

