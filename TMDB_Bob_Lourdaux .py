#Importeren van bibliotheken
import requests
import urllib.parse
import json
from prettytable import PrettyTable
from requests.structures import CaseInsensitiveDict
headers = CaseInsensitiveDict()

#APIv4 key
APIv4 = input("Geef uw APIv4 auth key: ")

#API url
url_themoviedb = "https://api.themoviedb.org/3/search/movie?"

#Starten van een while lus
while True:    
    naam = input("Geef de naam van je film (Stop met quit of q ): ") #Input vragen van de user

    if naam == "quit" or naam == "q": #Een gebruiker kan midde in het programma stoppen door q of suit te typen
        break

    elif naam != "quit" or naam != "q": #Als er niet wordt afgesloten         
        headers["Accept"] = "application/json" #Onze gegevens uit de API worden als json teruggegeven
        headers["Authorization"] = "Bearer "+ APIv4 #Onze bearer authentication header        
        url = url_themoviedb + urllib.parse.urlencode({"query":naam}) #De volledige URL waar we naar zoeken
        json_data = requests.get(url, headers=headers) #Opvragen van json data

    json_data = json_data.content #Laden van de Json data
    json_data = json.loads(json_data)

    Tabel = PrettyTable(["Title" ,"Datum van publicatie","Beoordeling"]) #Aanmaken van tabel met titels
    
    for film in json_data["results"]: #For lus over alle gevonden informatie       
        Tabel.add_row([film["title"],film["release_date"],film["vote_average"]]) #Gegevens toevoegen aan Tabel       
        
    print(Tabel) #Afdrukken van tabel
    break    