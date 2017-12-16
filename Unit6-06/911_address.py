# Created by: Julie Nguyen
# Created on: Dec 2017
# Created for: ICS3U
# This program returns the 911 street address

from enum import Enum

class MailAddress():
    def __init__(self, house_number, street_name, street_type):
        self.house_number = house_number
        self.street_name = street_name
        self.street_type = street_type

    def address(self):
        # returns user info in 911 address form
        
        self.information_string = "\n" + str(a_mailing_address.house_number) + " " + a_mailing_address.street_name + " " + str(a_mailing_address.street_type)
        
        return self.information_string

Street_Type = Enum('Avenue', 'Boulevard', 'Crescent', 'Lane', 'Road')
print("Types of Streets: \n")
for street_kinds in Street_Type:
    print(street_kinds)
print("")

route_type = raw_input("Street Type: ")
while route_type not in Street_Type:
    route_type = raw_input("Please input a valid street type: ")
route_type = route_type

address_number = int(input("House Number:"))
while address_number < 0:
    address_number = int(input("Please input an actual house number: "))
address_number = address_number

a_mailing_address = MailAddress(address_number, raw_input("Street Name: "), route_type)

print(a_mailing_address.address())
