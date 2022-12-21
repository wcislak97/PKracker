import pyrebase
import sys
from globalConfigs import *

#1 Inicjalizacja z app.py + uzycie funkcji
#self.dbConn = dbConn()
# dbConn.PushSlownik(self.dbConn)


class dbConn:

    try:
        firebase = pyrebase.initialize_app(firebaseConfig)
        db = firebase.database()
    except:
        print("db problem 0")


    #PushSlownik
    #dodaje liste slow do istniejącego lub nowego slownika
    #liste dodaje sie w metodzie
    #tworzy nowy slownik jesli nazwaSlownika nie istnieje i dodaje liste slow. jesli slownik istnieje to dodaje po prostu liste slow
    def PushSlownik(self,nazwaSlownika):
        data=["ble","bla"]
        try:
            for val in data:
                self.db.child("slownik").child(nazwaSlownika).child("words").push(val)
        except:
            print("db problem 1")


    #PushSlownikFromFile
    #tak samo jak PushSlownik tylko lista slow jest z pliku
    #usage from app.py: dbConn.PushSlownikFromFile(self.dbConn,"testSlownik","C:\\Users\\agata\\Desktop\\slownik.txt")
    def PushSlownikFromFile(self,nazwaSlownika,pathWithFile):
        data=[]
        with open(pathWithFile) as file:
            for line in file:
               data.append(line.rstrip())

        try:
            for val in data:
                self.db.child("slownik").child(nazwaSlownika).child("words").push(val)
        except:
            print("db problem 1")




    #PushMetody
    #dodaje metody z listy data do bazy pod metody -> tu itemy z listy
    def PushMetody(self):
        data = ['Brute force', 'Słownikowa']
        try:
            for val in data:
                self.db.child("metody").push(val)
        except:
            print("db problem 5")


    #PushAlgorytmy
    #dodaje algorytmy z listy data do bazy pod algorytmy -> tu itemy z listy
    def PushAlgorytmy(self):
        data=['MD5']
        try:
            for val in data:
                self.db.child("algorytmy").push(val)
        except:
            print("db problem 6")


    #GetSlowaZSlownik
    #zwraca liste slow z wybranego slownika
    def GetSlowaZeSlownik(self,nazwaSlownika):
        lista=[]
        try:
            slownik=self.db.child("slownik").child(nazwaSlownika).child("words").get()
            for slowo in slownik.each():
                lista.append(slowo.val())
        except:
            print("db problem 2")
        print(lista)
        return lista


    #GetWszystkieSlowniki
    #zwraca liste wszystkich slownikow
    def GetWszystkieSlowniki(self):
        lista=[]
        try:
            slowniki=self.db.child("slownik").get()
            for slownik in slowniki.each():
                lista.append(slownik.key())
        except:
            print("db problem 3")
        print(lista)
        return lista


    #GetWszystkieMetody
    #zwraca liste wszystkich metod
    def GetWszystkieMetody(self):
        lista=[]
        try:
            metody=self.db.child("metody").get()
            for metoda in metody.each():
                lista.append(metoda.val())
        except:
            print("db problem 3")
        print(lista)
        return lista


    #GetWszystkieAlgorytmy
    #zwraca liste wszystkich algorytmow
    def GetWszystkieAlgorytmy(self):
        lista=[]
        try:
            algorytmy=self.db.child("algorytmy").get()
            for algorytm in algorytmy.each():
                lista.append(algorytm.val())
        except:
            print("db problem 3")
        print(lista)
        return lista


    #DeleteSlownik
    #usuwa wybrany slownik
    def DeleteSlownik(self,nazwaSlownika):
        try:
            self.db.child("slownik").child(nazwaSlownika).remove()
        except:
            print("db problem 4")


