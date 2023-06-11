from django.urls import path

from . import views

urlpatterns=[
    #input pages
    path('',views.index,name='index'),
    path('Tide-timings',views.tidein,name='tidein'),
    path('Ferry-timings',views.ferryin,name='ferryin'),
    path('Picnic-Beaches',views.beachesin,name='beachesin'),
    path('Sea-Forts',views.fortsin,name='fortsin'),

    #tidetimings output
    path('Time-result',views.tideout,name='tideout'),

    #ferrytime output
    path('Ferry-details',views.ferryout,name="ferryout"),

    #picnic beaches output
    path('Alibaug',views.alibaug,name='alibaug'),
    path('Awas',views.awas,name='awas'),
    path('Bhatye',views.bhatye,name='bhatye'),
    path('Divegar',views.divegar,name='divegar'),
    path('Ganpatipule',views.ganpatipule,name='ganpatipule'),
    path('Gorai',views.gorai,name='gorai'),
    path('Guhagar',views.guhagar,name='guhagar'),
    path('Harihareshwar',views.harihareshwar,name='harihareshwar'),
    path('Hedvi',views.hedvi,name='hedvi'),
    path('Juhu',views.juhu,name='juhu'),
    path('Kashid',views.kashid,name='kashid'),
    path('Kelwa',views.kelwa,name='kelwa'),
    path('Malvan',views.malvan,name='malvan'),
    path('Manori',views.manori,name='manori'),
    path('Murud',views.murud,name='murud'),
    path('Shrivardhan',views.shrivardhan,name='shrivardhan'),
    path('Suruchi',views.suruchi,name='suruchi'),
    path('Tarkarli',views.tarkarli,name='tarkarli'),
    path('Varsoli',views.varsoli,name='varsoli'),
    path('Velneshwar',views.velneshwar,name='velneshwar'),

    #picnic forts
    path('Arnala-fort',views.arnalaf,name='arnalaf'),
    path('Kulaba-fort',views.kulabaf,name='kulabaf'),
    path('Murud-Janjira-fort',views.murudf,name='murudf'),
    path('Suvarnadurg-fort',views.suvarnadurgf,name='suvarnadurgf'),
    path('Sindhudurg-fort',views.sindhudurgf,name='sindhudurgf'),
    path('Vijaydurg-fort',views.vijaydurgf,name='vijaydurgf'),
    path('Underi-fort',views.underif,name='underif'),
    path('Vasai-fort',views.vasaif,name='vasaif')

]