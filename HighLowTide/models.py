from django.db import models

# Create your models here.
class timetype():
    def __init__(self,time,typ,AMPM):
        self.time=time
        self.typ=typ
        self.AMPM=AMPM


class ferrytime():
        first:str
        last:str
        frequency:str
        journeytime:int
        fare:int
        carrybike:str
        avail:str