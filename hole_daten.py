#!/usr/bin/env python
# encoding: utf-8

from pprint import pprint
from mendeley_client import *
import os, sys, json


mendeley = create_client()


# aufgabe 1: Wie verteilen sich die in Mendeley abgelegten Publikationen auf die letzten 10 Jahre?
# (Dafür müssen nicht alle Publikationen heruntergeladen werden!)
print "Papers:\n"
publikationen10 = {}
for jahr in range(2003,2013): # letzte zehn jahre: von 2003 bis 2012 (trotzdem in range 2013 angeben)
    response = mendeley.search('year:'+str(jahr))
    print str(jahr) + ":"
    print "    "+str(response['total_results'])+" Publikationen"
    publikationen10[jahr]=response['total_results']
with open("aufgabe1.json", "w") as json_output:
    json.dump(publikationen10, json_output)
print "\n ---------------------- \n"


# aufgabe 2: Was sind die Top20-Tags in der Kategorie „Computer and Information Science“?
# hole die top 20 tags aus der kategorie "computer and information science"
response = mendeley.tag_stats(6) # 6 ist die kategorie-id
print "Top 20 Tags in Kategorie 'Computer and information science'\n"
top20 = {}
for tag in response:
    top20[tag['name']]=tag['count']
    print tag['name'] +": "+ str(tag['count']) + " mal"
with open("aufgabe2.json", "w") as json_output:
    json.dump(top20, json_output)
print "\n ---------------------- \n"


# aufgabe 3: Was sind die 10 populärsten Publikationen die in der Zeitschrift „Nature“ erschienen sind?
# das ist sehr schwierig. paper_stats gibt die 50 populärsten Zeitschriften aus,
# allerdings ist da nur eine publikation aus Nature dabei.
# wir könnten über search danach suchen, haben dann aber kein ranking nach popularität
response = mendeley.search('published_in:Nature', items=100)
print "Top 10 Publikationen in Zeitschrift 'Nature'\n"
#pprint(response)
print "anfrage muss noch verbessert werden"
print "\n ---------------------- \n"


# aufgabe 4: Auflistung aller Publikationen von Prof. Wolfgang G. Stock
# (Extrahiere diese Daten automatisch mit Hilfe von Python!)
response = mendeley.authored('"Wolfgang G Stock"', items=500)
print "Publikationen von Stock\n"
for publikation in response['documents']:
    print str(publikation['year']) + ": " + publikation['title']
    print "    Autoren:"
    for autor in publikation['authors']:
        print "            " + autor['forename'] + " " + autor['surname']
    print "\n"
print "\n ---------------------- \n"


# aufgabe 5: Suche nach dem Tag „ontology“ und bestimme die Häufigkeit für jede Kategorie in Mendeley für das Jahr 2011.
# erster schritt: liste mit allen kategorien holen:
cat_response = mendeley.categories()
print "Häufigket des Tags 'ontology' in Kategorien (noch ohne Jahresfilter)\n"
for eintrag in cat_response: # jede kategorie durchgehen
    response = mendeley.tagged('ontology', cat=eintrag['id'])
    print eintrag['name'] + " (ID " + str(eintrag['id']) + "): "
    print "    "+ str(response['total_results']) + " Ergebnisse\n" 
print "\n ---------------------- \n"
