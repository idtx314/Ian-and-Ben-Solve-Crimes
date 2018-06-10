#!/usr/bin/env python

import sys
from mx import DateTime
import enum


'''
TODO
remove duplicate entries
change script to continue until end of file


USAGE
./counting.py input_file output_file


'''
class DoW(enum.Enum):
    Mon=0
    Tues=1
    Weds=2
    Thurs=3
    Fri=4
    Sat=5
    Sun=6


def main(args):
    if(len(args) < 3):
        print "Usage: 'counting.py input_file output_file'"
        sys.exit()

    f1 = open(args[1],'r')
    f2 = open(args[2],'w')

    # DEBUG these are for getting code and location lists
    iucrList = []
    locationList = []
    s = ""

    scrublist = [0, 1, 2, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22]
    scrublist.sort(reverse=True)

    # Write the header of the new file
    # @attribute Day {Mon,Tues,Weds,Thurs,Fri,Sat,Sun}
    # @attribute Time {Morning, Afternoon, Evening, Night}
    # @attribute Moon {Full, Not_Full}
    msg = '@relation 2001_2004\n\n@attribute Date date "MM/dd/yyy hh:mm:ss aa"\n@attribute IUCR {0840,2825,1752,0841,0266,5007,0890,1753,1754,0910,0810,1563,1130,0843,1150,1562,1120,0460,0263,0842,0610,2820,0281,5002,1750,142A,0920,1195,1140,0930,0265,0261,0484,2840,1822,1811,1661,2017,1506,2027,2230,1812,2050,2014,2093,2092,2024,2022,0820,2826,0497,0860,0486,1152,1751,1122,1544,1582,3730,1565,0620,1320,1310,1564,0915,1790,5000,0275,0560,0580,1025,1110,0850,1206,1330,1135,4510,1305,1590,1576,1210,0110,5001,0917,051A,0313,4650,1570,1580,0545,0530,1153,1156,1154,1535,4255,0430,143A,2850,0630,1090,0420,0554,0320,031A,0520,0326,1821,2095,2091,2090,4387,1220,0440,1792,033A,0337,2250,0453,0325,1245,1340,041A,3800,0312,1200,1020,1626,5004,0470,141C,1360,2900,1121,1350,0454,4651,1460,1710,0334,2210,0291,5005,3960,141A,0340,1525,5011,4388,4230,2111,2012,1513,4220,4310,051B,2860,2830,2011,0330,0450,0925,041B,4210,2851,0880,1365,2028,1345,1010,0870,502P,2013,3710,1170,502R,1155,033B,0553,0262,0264,0935,141B,1240,031B,1610,143B,0550,3920,2870,143C,2110,2029,0492,1791,2026,9901,0273,2025,2023,0483,0452,1505,1235,2030,1627,1510,1651,2040,2010,1540,0493,1720,2021,3100,1515,1151,0552,1900,2016,1670,2240,0581,1520,0271,0480,0937,1205,1507,2015,5003,1512,1370,1680,2020,1585,2018,3760,3750,0482,0551,1530,1631,1511,1780,0274,142B,1536,1440,3910,3400,2019,1611,1549,1566,1030,1650,1477,501A,1541,1261,0496,3731,4625,2170,5111,2034,0650,2031,2032,0462,1435,3300,5130,0498,0495,4386,0918,2220,0331,0479,1242,502T,5093,500N,2890,0488,3970,0557,0558,1755,5110,0555,0895,0485,1050,4389,5131,4652,5114,0583,0865,1335,1850,2070,1375,1480,5112,0584,2080,1185,2160,1260,1265,1055,3975,5121,1682,5009,1537,5113,1725,1479,0461,0475,3751,4860,5094,3610,1478,0142,5132,1255,500E,4240,5008,501H,1241,4810,2094,0938,0927,2895,1624,4800,0481,0489,1476,0451,2251,1035,0556,3966,3740,1840,1715,1450,3200,2120,1574,3720,3000,1521}\n@attribute Location_Description {RESIDENCE,OTHER,APARTMENT,RESIDENCE_PORCH/HALLWAY,GAS_STATION,COMMERCIAL_/_BUSINESS_OFFICE,STREET,BANK,SMALL_RETAIL_STORE,DEPARTMENT_STORE,SIDEWALK,APPLIANCE_STORE,HOTEL/MOTEL,MEDICAL/DENTAL_OFFICE,PARKING_LOT/GARAGE(NON.RESID.),ALLEY,CHURCH/SYNAGOGUE/PLACE_OF_WORSHIP,DAY_CARE_CENTER,RESTAURANT,COLLEGE/UNIVERSITY_GROUNDS,SCHOOL__PUBLIC__BUILDING,HOSPITAL_BUILDING/GROUNDS,WAREHOUSE,FACTORY/MANUFACTURING_BUILDING,SCHOOL__PRIVATE__GROUNDS,GROCERY_FOOD_STORE,CHA_APARTMENT,SCHOOL__PUBLIC__GROUNDS,VEHICLE_NON-COMMERCIAL,GOVERNMENT_BUILDING/PROPERTY,AIRPORT/AIRCRAFT,ATM_(AUTOMATIC_TELLER_MACHINE),VACANT_LOT/LAND,POLICE_FACILITY/VEH_PARKING_LOT,TAVERN/LIQUOR_STORE,CHA_HALLWAY/STAIRWELL/ELEVATOR,RESIDENCE-GARAGE,PARK_PROPERTY,CHA_PARKING_LOT/GROUNDS,ABANDONED_BUILDING,SCHOOL__PRIVATE__BUILDING,CURRENCY_EXCHANGE,BARBERSHOP,NURSING_HOME/RETIREMENT_HOME,CHA_STAIRWELL,AUTO,BASEMENT,ANIMAL_HOSPITAL,RESIDENTIAL_YARD_(FRONT/BACK),JAIL_/_LOCK-UP_FACILITY,RETAIL_STORE,TAVERN,GAS_STATION_DRIVE/PROP.,FEDERAL_BUILDING,HOTEL,HALLWAY,TRUCK,GANGWAY,POOL_ROOM,PARKING_LOT,HOUSE,COACH_HOUSE,PORCH,CLUB,VACANT_LOT,ATHLETIC_CLUB,YARD,AIRPORT_BUILDING_NON-TERMINAL_-_SECURE_AREA,CAR_WASH,CHA_PARKING_LOT,LOADING_DOCK,CHA_ELEVATOR,LAKE,RAILROAD_PROPERTY,CTA_GARAGE_/_OTHER_PROPERTY,VESTIBULE,CHA_HALLWAY,AIRPORT_TERMINAL_UPPER_LEVEL_-_SECURE_AREA,DUMPSTER,GARAGE,FOREST_PRESERVE,BAR_OR_TAVERN,COLLEGE/UNIVERSITY_RESIDENCE_HALL,CHA_PLAY_LOT,CHA_GROUNDS,HOSPITAL,RIVER,FIRE_STATION,DRUG_STORE,CTA_BUS,CTA_PLATFORM,HIGHWAY/EXPRESSWAY,CLEANING_STORE,DRIVEWAY_-_RESIDENTIAL,OTHER_RAILROAD_PROP_/_TRAIN_DEPOT,CTA_TRAIN,VEHICLE-COMMERCIAL,OTHER_COMMERCIAL_TRANSPORTATION,LIBRARY,DELIVERY_TRUCK,CEMETARY,CONSTRUCTION_SITE,BOAT/WATERCRAFT,SPORTS_ARENA/STADIUM,LAKEFRONT/WATERFRONT/RIVERBANK,TAXICAB,WOODED_AREA,COUNTY_JAIL,STAIRWELL,YMCA,CHURCH_PROPERTY,MOVIE_HOUSE/THEATER,BOWLING_ALLEY,COIN_OPERATED_MACHINE,SAVINGS_AND_LOAN,SEWER,LIVERY_STAND_OFFICE,GARAGE/AUTO_REPAIR,CREDIT_UNION,CHURCH,CHA_BREEZEWAY,NEWSSTAND,BRIDGE,CHA_LOBBY,?,CONVENIENCE_STORE,CTA_STATION,AIRPORT_TERMINAL_LOWER_LEVEL_-_NON-SECURE_AREA,VEHICLE_-_OTHER_RIDE_SERVICE,CTA_BUS_STOP,PAWN_SHOP,AIRPORT_EXTERIOR_-_NON-SECURE_AREA,AIRPORT_BUILDING_NON-TERMINAL_-_NON-SECURE_AREA,VEHICLE_-_DELIVERY_TRUCK,AIRPORT_PARKING_LOT,AIRPORT_VENDING_ESTABLISHMENT,AIRPORT_TERMINAL_MEZZANINE_-_NON-SECURE_AREA,AIRPORT_TERMINAL_LOWER_LEVEL_-_SECURE_AREA,AIRPORT_EXTERIOR_-_SECURE_AREA,AIRCRAFT,AIRPORT_TERMINAL_UPPER_LEVEL_-_NON-SECURE_AREA,BARBER_SHOP/BEAUTY_SALON,AIRPORT_TRANSPORTATION_SYSTEM_(ATS),CTA_TRACKS_-_RIGHT_OF_WAY,ROOMING_HOUSE,SCHOOL_YARD,CTA_PROPERTY}\n@attribute Latitude numeric\n@attribute Longitude numeric\n\n@data\n'
    f2.write(msg)


    # Throw away the first line
    f1.readline()
    i=0     # DEBUG
    # Until the number of lines processed reaches max
    while(i < 10):
        # DEBUG Keep a count of the number of lines processed
        i+=1
        print i

        # Get a line from the file
        attstr = f1.readline()

        # Split the line at any double quotes
        attlist = attstr.split('"')

        # For each item that was between double quotes, remove any commas
        for index in range(1,len(attlist),2):
            attlist[index] = attlist[index].replace(","," ")

        # Rejoin the split items into a line, replacing the double quotes with nothing
        attstr = ''.join(attlist)

        # Produces a list of attributes from the line
        attlist = attstr.split(',')

        # Break the loop if the list is ['']
        if(len(attlist) == 1):
            print "Done!"
            break
        # Print the list and break the loop if the list is too short.
        if(len(attlist) < 23):
            print attstr
            print attlist
            break

        # If attributes are missing, replace them with question marks
        for index in range(len(attlist)):
            if(attlist[index] == ''):
                attlist[index] = '?'

        # If there are spaces in location, remove them
        attlist[8] = attlist[8].replace(" ","_")

        # Debug: If the code or location is not in list of possible values, add it
        if attlist[5] not in iucrList:
            iucrList.append(attlist[5])
        if attlist[8] not in locationList:
            locationList.append(attlist[8])

        # Remove the unwanted attributes from last to first
        for index in scrublist:
            attlist.pop(index)

        # [Date,IUCR,Location_Description,Latitude,Longitude]

        # Get the day.name, the day of the week as a string
        date_list = attlist[0].split(' ')
        y = int(date_list[0][6:10])
        m = int(date_list[0][0:2])
        d = int(date_list[0][3:5])
        date = DateTime.Date(y,m,d)
        day = DoW(date.day_of_week)

        print day.name


        # TODO: Add the moon field and fill it appropriately by date

        # TODO: Split the date into two fields, day of week and time of day

        # TODO: Convert time into a general time of day


        # Form a new comma separated string
        msg = ','.join(attlist)

        # Write joined string to a new line of the output file
        f2.write(msg)
        f2.write("\n")


    # These lines can be used to print out the lists containing the locations and crime codes in the set
    # for iucr in iucrList:
    #     s = s + "'" + str(iucr) + "'" + ','
    # print s
    # s = ""
    # for location in locationList:
    #     s = s + "'" + str(location) + "'" + ','
    # print s

    f1.close()
    f2.close()

    # These snippets are useful for combining multiple lists of locations and crime codes
    # for place in k:
    # if place not in l:
    #     l.append(place)

    # s=''
    # for place in l:
    #    s = s + str(place) + ','











if __name__ == '__main__':
    main(sys.argv)
