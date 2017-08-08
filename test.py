#!/usr/bin/python3

import requests



def mk_search(responsive='true',
              destination='orlando_fl',
              startDate='09/15/2017',
              endDate='09/17/2017',
              adults='2',
              lodging='motel,condo,hotel,apartment,villa,hotelResort,townhouse,bedBreakfast,cabin,hostel,houseBoat,inn,cottage',
              sort='price',
              page='1',
              timezoneOffset='-14400000',
              siteId='1',
              langId='1033',
              hsrIdentifier='HSR'):

   req_data = {
      'responsive' : responsive,
      'destination' : destination,
      'startDate' : startDate,
      'endDate' : endDate,
      'adults' : adults,
      'lodging' : lodging,
      'sort' : sort,
      'page' : page,
      'timezoneOffset' : timezoneOffset,
      'siteid' : siteId,
      'langId' : langId,
      'hsrIdentifier' : hsrIdentifier
   }

   r = requests.post('https://www.expedia.com/Hotel-Search-Data',
                     req_data)
   return r.text

i = 0
while i < 20:
   with open('data/f' + str(i), 'w') as f:
      x = mk_search(page=str(i))
      f.write(x)
   i += 1



