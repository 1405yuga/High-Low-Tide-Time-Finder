# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from .models import timetype
import arrow
import requests

def api_data(latitude,longitude):
  start = arrow.now().floor('day')
  end = arrow.now().shift(days=1).floor('day')

  response = requests.get(
    'https://api.stormglass.io/v2/tide/extremes/point',
    params={
      'lat': latitude,
      'lng': longitude,
      'start': start.to('UTC').timestamp,  # Convert to UTC timestamp
      'end': end.to('UTC').timestamp,  # Convert to UTC timestam
    },
    headers={
      'Authorization': '5c6aaa4e-00a8-11eb-9025-0242ac130002-5c6aaba2-00a8-11eb-9025-0242ac130002'
    }
  )

  # Do something with response data.
  json_data = response.json()
  x=json_data['data']
  
  result=[]
  for i in range(len(x)):
      #Getting data from json
      t=x[i]['time']
      typ=x[i]['type']
      t=t[11:16]
      tym=t.split(":")
      
      #converting to ist from utc
      hour=int(tym[0])+5
      minute=int(tym[1])+30
      
      if(typ=="high"):
          if(minute<10):
              minute=minute+60-10
              if(hour<1):
                  hour=23
              else:
                  hour=hour-1
          else:
              minute=minute-10

      if(minute>=60):
          minute=minute-60
          hour=hour+1
      if(hour>=24):
          hour=hour-24
      if(minute<10):   
        minute="0"+str(minute)
      else:
        minute=str(minute)

    #am-pm settings
      AMPM="AM"
      if(hour>=12):
        hour=hour-12
        AMPM="PM"

      #collection of objects
      time=str(hour)+":"+str(minute)
      t=timetype(time,typ,AMPM)
      result.append(t)
      #print("time= "+time+" type="+typ)
  return result

