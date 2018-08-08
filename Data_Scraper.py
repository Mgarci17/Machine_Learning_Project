# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 22:02:18 2018

@author: PrimarisUser
"""

import urllib
from lxml import html
import requests


url='http://money.cnn.com/quote/forecast/forecast.html?symb=mbrx'
page=requests.get(url)
tree=html.fromstring(page.content)

Site=urllib.urlopen(url)
data=Site.read()
Site.info()['date']
#with open(data,'r') as datafile:
#f=open(data)
#f.write(data)
#f.close()
#with open(''.format(url.split('/')[2]),'wb'))
#    f.write(data)
 
'''
    Not quite what we're looking for yet
    but this will take shape
    
    Either way, we can probably make this
    a low priority due to our ability
    to get this information elsewhere
    
'''
#%%

def Site(Symb):
    """
        Right now, this can give us the current price of any symbol that we want
        to search for. however, that's about all we can do
    """
    Check=[]
    if type(Symb) != type(Check):
        return ValueError("Expected type list, recieved {}".format(type(Symb)))
    
    for item in Symb:
        url='http://money.cnn.com/quote/forecast/forecast.html?symb={0}'.format(item)
        Site=urllib.urlopen(url)
        data=Site.read()
        price=DecipherPrice(data)
        Date=Site.info()['date']
        
        print '{0} : {1}'.format(price,Date)
        return data
        
def DecipherPrice(dataIn):
    DataSpit=[]
    
    SiftData=dataIn.split('/')
    for item in SiftData:
        if 'price' in item:
            DataSpit.append(item)
    
    return DataSpit
        
        
        