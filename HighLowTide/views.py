from django.shortcuts import render
from .api_check1 import api_data
from .GetLatLong import lat,lon
from .ferry_check import ferry
# Create your views here.

#input pages
def index(request):
    return render(request,'HOME PAGE.html')

def tidein(request):
    return render(request,'tide_input.html')

def ferryin(request):
    return render(request,'ferry_in.html')

def beachesin(request):
    return render(request,'beaches_in.html')

def fortsin(request):
    return render(request,'forts_in.html')

#output pages

#tide timings
def tideout(request):
    results=request.GET.get("BOX")
    '''
    if(results==""):
        return render(request,'testTide.html',{'loc':'NOT'})
    '''
    lati=lat(results)
    longi=lon(results)
    tt=api_data(lati,longi)
    return render(request,'tide_output.html',{'tt':tt})

#ferry output
def ferryout(request):
    place1=request.GET['drop']
    place2=request.GET.get("BOX")
    ob=ferry(place1,place2)
    return render(request,'ferry_output.html',{'place1':place1,'place2':place2,'ob':ob})
    

#picnic spot beaches
def alibaug(request):
    return render(request,'maps5.html')

def awas(request):
    return render(request,'maps10.html')

def bhatye(request):
    return render(request,'maps20.html')

def divegar(request):
    return render(request,'maps16.html')

def ganpatipule(request):
    return render(request,'maps3.html')

def gorai(request):
    return render(request,'maps19.html')

def guhagar(request):
    return render(request,'maps4.html')

def harihareshwar(request):
    return render(request,'maps6.html')

def hedvi(request):
    return render(request,'maps14.html')

def juhu(request):
    return render(request,'maps.html')

def kashid(request):
    return render(request,'maps11.html')

def kelwa(request):
    return render(request,'maps8.html')

def malvan(request):
    return render(request,'maps12.html')

def manori(request):
    return render(request,'maps15.html')

def murud(request):
    return render(request,'maps13.html')

def shrivardhan(request):
    return render(request,'maps17.html')

def suruchi(request):
    return render(request,'maps2.html')

def tarkarli(request):
    return render(request,'maps9.html')

def varsoli(request):
    return render(request,'maps18.html')

def velneshwar(request):
    return render(request,'maps7.html')

#picnic spots-forts
def arnalaf(request):
    return render(request,'1.html')

def kulabaf(request):
    return render(request,'2.html')

def murudf(request):
    return render(request,'3.html')

def suvarnadurgf(request):
    return render(request,'4.html')

def sindhudurgf(request):
    return render(request,'5.html')

def vijaydurgf(request):
    return render(request,'6.html')

def underif(request):
    return render(request,'7.html')

def vasaif(request):
    return render(request,'8.html')