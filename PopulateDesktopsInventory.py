import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'rentWare.settings'

import django
django.setup()

#from django.db import models

#from bs4 import BeautifulSoup
import requests
import json
# from rentWareApp.models import Webscrape
#from django.contrib.postgres.fields import JSONField

from rentWareApp.models import Webscrape, Inventory, Category, Specification, Rate
#from django.contrib.auth.models import User

import itertools

a = Webscrape.objects.get(name='DesktopMain')

#print(a.data.keys())

for akey in a.data.values():
    for dd in akey[0]:
        pass
#        print("break")
#        print(dd)



cat = Category.objects.get(name='Desktops')

c1=1

inv = Inventory.objects.all()
rat = Rate.objects.all()
spec = Specification.objects.all()

for d in inv:
    d.delete()

for d in rat:
    d.delete()

for d in spec:
    d.delete()


def create_spec(data, akey, dat, val):
    for k in itertools.islice(data[akey], 1, None):
        spec = Specification()
        spec.name=k
        spec.inventory=dat
#        spec.partID=c2
        spec.save()

#    print(akey)
#    dictemp1['PROFESSIONAL DESKTOP COMPUTER']=data['PROFESSIONAL DESKTOP COMPUTER'][0]
#    dictemp2['PROFESSIONAL DESKTOP COMPUTER']=data['PROFESSIONAL DESKTOP COMPUTER']
#    print(data['PROFESSIONAL DESKTOP COMPUTER'][0])
#    print(dictemp1)
#    print(dictemp2)
    #dictemp3 = dictemp2 - dictemp1
#    dictemp3 = dict(set(dictemp2) - set(dictemp1))
#    print(dictemp3)
#dict(set(a.items()) - set(b.items()))


#        spec = Specification()
#        spec.inventory=dat
#        spec.name=c
#        spec.save()
#        print("item")
#        print(dat.pk)
#        print(c)

#islice('ABCDEFG', 1, None) --> C D E F G

def create_rate(dat, val):
#    c1=0
#    for k, c in itertools.islice(val[0].items(), 1, None):
    for k, c in val[0].items():
#        c1+=1
#        if (c1 > 1):
        inst = Rate()
        inst.inventory=dat
        inst.name=k
        inst.amount=c
        inst.save()
#        c1=0

#    print('-------')
#    for c in val:
#        print("item")
#        print(dat.pk)
#        print(c)


#    print(val)
#    inst = Rate()
#    inst.inventory=dat
#    inst.name=val[0]
#    inst.save()

    #print(type(dat))


#for mm in a.data:
#    print(mm)

for akey, val in a.data.items():
    c1+=12
#    print(akey)
    dat = Inventory()
    dat.category=cat
    dat.name=akey
    dat.partID=c1
    dat.save()
    create_spec(a.data, akey, dat, val)
    create_rate(dat, val)


#rat = Specification.objects.all()
#print(rat)



"""
res = requests.get('http://rentware.co.za/cape-town-computer-rentals/')

soup = BeautifulSoup(res.text, 'lxml')

items = soup.find('div', id='post-3056').find_all('ul')

embeddict={}
adict={}
c1=0
for ul in items:
    c1+=1
    alist=[]
    for li in ul.findAll('li'):
        alist.append(li.getText().strip())

    key1=ul.find_previous('h3').getText().strip()
    tbl1=ul.find_next("table")
    cols = tbl1.findAll('td')
    first_item = str(cols[0].find(text=True))
    second_item = str(cols[1].find(text=True))
    third_item = str(cols[2].find(text=True))
    forth_item = str(cols[3].find(text=True))
    fith_item = str(cols[4].find(text=True))

    labels = tbl1.findAll('th')
    first_label = str(labels[0].find(text=True))
    second_label = str(labels[1].find(text=True))
    third_label = str(labels[2].find(text=True))
    forth_label = str(labels[3].find(text=True))
    fith_label = str(labels[4].find(text=True))

    embeddict[c1]={third_label: third_item, first_label: first_item, forth_label: forth_item, second_label: second_item, fith_label: fith_item}

    #adict[key1]=embeddict
    adict[key1]=alist
    adict[key1][0]=embeddict[c1]

"""
#print(json.dumps(adict, ensure_ascii=False))
