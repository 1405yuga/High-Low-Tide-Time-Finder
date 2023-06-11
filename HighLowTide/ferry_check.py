from .models import ferrytime

def ferry(place1,place2):
    #1
    if((place1=="Gorai Jetty" and place2 =="Borivali Jetty") or(place1=="Borivali Jetty" and place2 =="Gorai Jetty")):
        ob1=ferrytime()
        if(place1=="Gorai Jetty" and place2 =="Borivali Jetty"):
            ob1.first="5.30 AM"
            ob1.last="11.45 PM"
        else:
            ob1.first="5.45 AM"
            ob1.last="12.00 AM"
        ob1.frequency="5 min"
        ob1.journeytime=5
        ob1.fare=10
        ob1.carrybike="Yes"
        ob1.avail="365 days"
        return ob1

    #3
    if((place1=="Borivali Jetty" and place2=="Essel World") or (place1=="Essel World" and place2=="Borivali Jetty")):
        ob1=ferrytime()
        if(place1=="Borivali Jetty" and place2=="Essel World"):
            ob1.first="9.40 AM"
            ob1.last="5.35 PM"
        else:
            ob1.first="10.00 AM"
            ob1.last="7.35 PM"
        ob1.frequency="30 min"
        ob1.journeytime=20
        ob1.fare=25
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1


    #5
    if((place1=="Marve" and place2=="Manori") or (place1=="Manori" and place2=="Marve")):
        ob1=ferrytime()
        if(place1=="Marve" and place2=="Manori"):
            ob1.first="5.30 AM"
            ob1.last="12.20 PM"
        else:
            ob1.first="5.15 AM"
            ob1.last="12.00 PM"
        ob1.frequency="15 min"
        ob1.journeytime=5
        ob1.fare=10
        ob1.carrybike="Yes"
        ob1.avail="365 days"
        return ob1


    #7
    if((place1=="Essel World" and place2=="Marve") or (place1=="Marve" and place2=="Essel World")):
        ob1=ferrytime()
        if(place1=="Essel World" and place2=="Marve"):
            ob1.first="10.00 AM"
            ob1.last="7.35 PM"
        else:
            ob1.first="9.35 AM"
            ob1.last="5.00 PM"
        ob1.frequency="40 min"
        ob1.journeytime=25
        ob1.fare=25
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1


    #9
    if((place1=="Versova" and place2=="Madh") or (place1=="Madh" and place2=="Versova")):
        ob1=ferrytime()
        if(place1=="Versova" and place2=="Madh"):
            ob1.first="5.00 AM"
            ob1.last="1.15 PM"
        else:
            ob1.first="5.15 AM"
            ob1.last="1.30 PM"
        ob1.frequency="15 min"
        ob1.journeytime=5
        ob1.fare=3
        ob1.carrybike="Yes"
        ob1.avail="365 days"
        return ob1

    #11
    if((place1=="Panju Island" and place2=="Naigaon Jetty") or (place1=="Naigaon Jetty" and place2=="Panju Island")):
        ob1=ferrytime()
        if(place1=="Panju Island" and place2=="Naigaon Jetty"):
            ob1.first="6.00 AM"
            ob1.last="9.55 PM"
        else:
            ob1.first="6.00 AM"
            ob1.last="9.55 PM"
        ob1.frequency="30 min"
        ob1.journeytime=5
        ob1.fare=10
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1


    #13
    if((place1=="Arnala" and place2=="Arnala Fort") or (place1=="Arnala Fort" and place2=="Arnala")):
        ob1=ferrytime()
        if(place1=="Arnala" and place2=="Arnala Fort"):
            ob1.first="6.00 AM"
            ob1.last="6.15 PM"
        else:
            ob1.first="6.15 AM"
            ob1.last="6.30 PM"
        ob1.frequency="15 min"
        ob1.journeytime=5
        ob1.fare=5
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1


    #15
    if((place1=="Navapur" and place2=="Dandi") or (place1=="Dandi" and place2=="Navapur")):
        ob1=ferrytime()
        if(place1=="Navapur" and place2=="Dandi"):
            ob1.first="6.00 AM"
            ob1.last="6.45 PM"
        else:
            ob1.first="6.15 AM"
            ob1.last="7.00 PM"
        ob1.frequency="15 min"
        ob1.journeytime=5
        ob1.fare=1
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1

    #17
    if(place1=="Murbe" and place2=="Satpati") or (place1=="Satpati" and place2=="Murbe"):
        ob1=ferrytime()
        if(place1=="Murbe" and place2=="Satpati"):
            ob1.first="7.30 AM"
            ob1.last="7.15 PM"
        else:
            ob1.first="7.45 AM"
            ob1.last="7.30 PM"
        ob1.frequency="15 min"
        ob1.journeytime=5
        ob1.fare=1
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1


    #19
    if(place1=="Murbe" and place2=="Kharekuran") or (place1=="Kharekuran" and place2=="Murbe"):
        ob1=ferrytime()
        if(place1=="Murbe" and place2=="Kharekuran"):
            ob1.first="7.30 AM"
            ob1.last="6.15 PM"
        else:
            ob1.first="7.45 AM"
            ob1.last="6.30 PM"
        ob1.frequency="15 min"
        ob1.journeytime=5
        ob1.fare=1
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1

  

    #21
    if(place1=="Karanja" and place2=="Rewas") or (place1=="Rewas" and place2=="Karanja"):
        ob1=ferrytime()
        if(place1=="Karanja" and place2=="Rewas"):
            ob1.first="7.30 AM"
            ob1.last="6.30 PM"
        else:
            ob1.first="7.15 AM"
            ob1.last="6.00 PM"
        ob1.frequency="15 min"
        ob1.journeytime=14
        ob1.fare=1
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1


    #21
    if(place1=="Belapur" and place2=="Elephanta") or (place1=="Elephanta" and place2=="Belapur"):
        ob1=ferrytime()
        if(place1=="Belapur" and place2=="Elephanta"):
            ob1.first="9.30 AM"
            ob1.last="9.30 PM"
        else:
            ob1.first="1.00 PM"
            ob1.last="5.30 PM"
        ob1.frequency="Depends on availability of passengers"
        ob1.journeytime=30
        ob1.fare=400
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1



    #23
    if(place1=="Elephanta" and place2=="Gateway") or (place1=="Gateway" and place2=="Elephanta"):
        ob1=ferrytime()
        if(place1=="Elephanta" and place2=="Gateway"):
            ob1.first="12.00 AM"
            ob1.last="5.30 PM"
        else:
            ob1.first="9.00 AM"
            ob1.last="2.00 PM"
        ob1.frequency="30 min"
        ob1.journeytime=60
        ob1.fare=110
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1


    #25
    if(place1=="Gateway" and place2=="Mandwa(Alibaug)") or (place1=="Mandwa(Alibaug)" and place2=="Gateway"):
        ob1=ferrytime()
        if(place1=="Gateway" and place2=="Mandwa(Alibaug)"):
            ob1.first="6.15 AM"
            ob1.last="8.15 PM"
        else:
            ob1.first="7.10 AM"
            ob1.last="7.30 PM"
        ob1.frequency="1 hour"
        ob1.journeytime=60
        ob1.fare=130
        ob1.carrybike="No"
        ob1.avail="Closed in Monsoon"
        return ob1

    
    #27
    if(place1=="Bhaucha Dhakka" and place2=="Rewas") or (place1=="Rewas" and place2=="Bhaucha Dhakka"):
        ob1=ferrytime()
        if(place1=="Bhaucha Dhakka" and place2=="Rewas"):
            ob1.first="6.00 AM"
            ob1.last="5.00 PM"
        else:
            ob1.first="7.45 AM"
            ob1.last="6.30 PM"
        ob1.frequency="1 hour"
        ob1.journeytime=150
        ob1.fare=73
        ob1.carrybike="Yes"
        ob1.avail="Closed in Monsoon"
        return ob1


    #29
    if(place1=="Mora" and place2=="Bhaucha Dhakka") or (place1=="Bhaucha Dhakka" and place2=="Mora"):
        ob1=ferrytime()
        if(place1=="Mora" and place2=="Bhaucha Dhakka"):
            ob1.first="7.30 AM"
            ob1.last="8.00 PM"
        else:
            ob1.first="6.00 AM"
            ob1.last="8.15 PM"
        ob1.frequency="1 hour"
        ob1.journeytime=60
        ob1.fare=55
        ob1.carrybike="Yes"
        ob1.avail="365 days"
        return ob1

    #31
    if(place1=="Bhaucha Dhakka" and place2=="Elephanta") or (place1=="Elephanta" and place2=="Bhaucha Dhakka"):
        ob1=ferrytime()
        ob1.first="Depends on availability of passengers"
        ob1.last="Depends on availability of passengers"
        ob1.frequency="Depends on availability of passengers"
        ob1.journeytime=150
        ob1.fare=160
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1
        

    #33
    if(place1=="Elephanta" and place2=="Mora") or (place1=="Mora" and place2=="Elephanta"):
        ob1=ferrytime()
        if(place1=="Elephanta" and place2=="Mora"):
            ob1.first="7.15 AM"
            ob1.last="5.15 PM"
        else:
            ob1.first="6.30 AM"
            ob1.last="4.30 PM"
        ob1.frequency="1 hour"
        ob1.journeytime=45
        ob1.fare=25
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1


    #35
    if(place1=="Mora" and place2=="Sassoon Dock") or (place1=="Sassoon Dock" and place2=="Mora"):
        ob1=ferrytime()
        if(place1=="Mora" and place2=="Sassoon Dock"):
            ob1.first="4.30 AM"
            ob1.last="6.00 PM"
        else:
            ob1.first="5.30 AM"
            ob1.last="7.00 PM"
        ob1.frequency="1 hour"
        ob1.journeytime=60
        ob1.fare=50
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1

    #37
    if(place1=="Rajpuri" and place2=="Dighi") or (place1=="Dighi" and place2=="Rajpuri"):
        ob1=ferrytime()
        if(place1=="Rajpuri" and place2=="Dighi"):
            ob1.first="7.00 AM"
            ob1.last="5.30 PM"
        else:
            ob1.first="7.30 AM"
            ob1.last="6.00 PM"
        ob1.frequency="1 hour"
        ob1.journeytime=25
        ob1.fare=22
        ob1.carrybike="No"
        ob1.avail="Closed in Monsoon"
        return ob1


    #39
    if(place1=="Dighi" and place2=="Janjira Fort") or (place1=="Janjira Fort" and place2=="Dighi"):
        ob1=ferrytime()
        if(place1=="Dighi" and place2=="Janjira Fort"):
            ob1.first="7.00 AM"
            ob1.last="4.30 PM"
        else:
            ob1.first="7.30 AM"
            ob1.last="5.00 PM"
        ob1.frequency="Depends on availability of passengers"
        ob1.journeytime=30
        ob1.fare=100
        ob1.carrybike="No"
        ob1.avail="Closed in Monsoon"
        return ob1


    #41
    if(place1=="Janjira Fort" and place2=="Rajpuri") or (place1=="Rajpuri" and place2=="Janjira Fort"):
        ob1=ferrytime()
        if(place1=="Janjira Fort" and place2=="Rajpuri"):
            ob1.first="8.00 AM"
            ob1.last="4.45 PM"
        else:
            ob1.first="8.15 AM"
            ob1.last="5.00 PM"
        ob1.frequency="Depends on availability of passengers"
        ob1.journeytime=15
        ob1.fare=60
        ob1.carrybike="No"
        ob1.avail="Closed in Monsoon"
        return ob1


    #43
    if(place1=="Dighi" and place2=="Agardanda") or (place1=="Agardanda" and place2=="Dighi"):
        ob1=ferrytime()
        if(place1=="Dighi" and place2=="Agardanda"):
            ob1.first="7.30 AM"
            ob1.last="6.00 PM"
        else:
            ob1.first="7.45 AM"
            ob1.last="6.30 PM"
        ob1.frequency="1 hour 30 mins"
        ob1.journeytime=20
        ob1.fare=15
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1


    #45
    if(place1=="Dabhol" and place2=="Dhopawe") or (place1=="Dhopawe" and place2=="Dabhol"):
        ob1=ferrytime()
        if(place1=="Dabhol" and place2=="Dhopawe"):
            ob1.first="6.30 AM"
            ob1.last="10.00 PM"
        else:
            ob1.first="6.45 AM"
            ob1.last="10.10 PM"
        ob1.frequency="1 hour"
        ob1.journeytime=10
        ob1.fare=15
        ob1.carrybike="Yes"
        ob1.avail="365 days"
        return ob1


    #47
    if(place1=="Veshvi" and place2=="Bagmandla") or (place1=="Bagmandla" and place2=="Veshvi"):
        ob1=ferrytime()
        if(place1=="Veshvi" and place2=="Bagmandla"):
            ob1.first="6.00 AM"
            ob1.last="10.00 PM"
        else:
            ob1.first="7.30 AM"
            ob1.last="10.10 PM"
        ob1.frequency="1 hour"
        ob1.journeytime=10
        ob1.fare=11
        ob1.carrybike="Yes"
        ob1.avail="365 days"
        return ob1


    #49
    if(place1=="Jaigad" and place2=="Tavsal") or (place1=="Tavsal" and place2=="Jaigad"):
        ob1=ferrytime()
        if(place1=="Jaigad" and place2=="Tavsal"):
            ob1.first="7.00 AM"
            ob1.last="10.15 PM"
        else:
            ob1.first="6.45 AM"
            ob1.last="10.00 PM"
        ob1.frequency="Depends on availability of passengers"
        ob1.journeytime=15
        ob1.fare=20
        ob1.carrybike="Yes"
        ob1.avail="365 days"
        return ob1



    #51
    if(place1=="Malvan" and place2=="Sindhudurg Fort") or (place1=="Sindhudurg Fort" and place2=="Malvan"):
        ob1=ferrytime()
        if(place1=="Malvan" and place2=="Sindhudurg Fort"):
            ob1.first="6.00 AM"
            ob1.last="5.50 PM"
        else:
            ob1.first="7.30 AM"
            ob1.last="6.30 PM"
        ob1.frequency="Depends on availability of passengers"
        ob1.journeytime=10
        ob1.fare=35
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1

    
    #53
    if(place1=="Agardanda" and place2=="Rohini") or (place1=="Rohini" and place2=="Agardanda"):
        ob1=ferrytime()
        if(place1=="Agardanda" and place2=="Rohini"):
            ob1.first="7.30 AM"
            ob1.last="9.00 PM"
        else:
            ob1.first="6.00 AM"
            ob1.last="9.30 PM"
        ob1.frequency="Depends on availability of passengers"
        ob1.journeytime=10
        ob1.fare=35
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1

    #54
    if(place1=="Kulaba Fort" and place2=="Alibaug beach") or (place1=="Alibaug beach" and place2=="Kulaba Fort"):
        ob1=ferrytime()
        if(place1=="Kulaba Fort" and place2=="Alibaug beach") :
            ob1.first="10.00 AM"
            ob1.last="5.00 PM"
        else:
            ob1.first="10.15 AM"
            ob1.last="5.15 PM"
        ob1.frequency="Depends on availability of passengers"
        ob1.journeytime=5
        ob1.fare=5
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1

    #55
    if(place1=="Suvarnadurga Fort" and place2=="Harnai") or (place1=="Harnai" and place2=="Suvarnadurga Fort"):
        ob1=ferrytime()
        if(place1=="Suvarnadurga Fort" and place2=="Harnai"):
            ob1.first="10.00 AM"
            ob1.last="5.00 PM"
        else:
            ob1.first="10.15 AM"
            ob1.last="5.15 PM"
        ob1.frequency="Depends on availability of passengers"
        ob1.journeytime=15
        ob1.fare=150
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1

    #56
    if(place1=="Underi Fort" and place2=="Thal") or (place1=="Thal" and place2=="Underi Fort"):
        ob1=ferrytime()
        if(place1=="Suvarnadurga Fort" and place2=="Harnai"):
            ob1.first="10.00 AM"
            ob1.last="5.00 PM"
        else:
            ob1.first="10.15 AM"
            ob1.last="5.15 PM"
        ob1.frequency="Depends on availability of passengers"
        ob1.journeytime=15
        ob1.fare=100
        ob1.carrybike="No"
        ob1.avail="365 days"
        return ob1
