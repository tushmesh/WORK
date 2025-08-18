import phonenumbers
x = phonenumbers.parse("+38631645383", "SI")

# Extract country code and national number
country_code = x.country_code
national_number = "{:010}".format(x.national_number)  # Add leading zeros

# Print the extracted information
print("Country Code:", country_code, "National Number:", national_number)

# x = phonenumbers.parse("+38631645383", "SI")
#
# # Extract country code and national number
# country_code = x.country_code
# national_number = str(x.national_number)
#
# # Add leading zero if necessary
# if len(national_number) < 9:  # Assuming the national number should be 9 digits long
#     national_number = "0" + national_number

# Print the extracted information
# print("Country Code:", country_code, "National Number:", national_number)