from datetime import datetime
import time

class loginInfo:
    #login info je klasa koja nam sluzi za cuvanje lozinki i korisnickih imena
    #koristimo staticke promenljive brojStudenata i brojProfesora kako bismo
    #odrzali redosled - prvo su upisani svi studenti, zatim svi profesori, pa
    #onda svi administratori
    brojStudenata = 0
    brojProfesora = 0
    brojAdmina = 0
    def __init__(self, userName, password, userType):
        self.userName = userName
        self.password = password
        self.userType = userType
    def generateNew(userName, password, userType):
        newLoginInfo = loginInfo(userName, password, userType)
        return newLoginInfo    
    def generateFromText(line):
        if line == "":
            return ""
        args = line.split("|")
        argUserName = args[0]
        argPassword = args[1]
        argUserType = args[2]
        generatedLoginInfo = loginInfo(argUserName, argPassword, argUserType)
        return generatedLoginInfo
    def __str__(self):
        line = self.userName + "|" + self.password + "|" + self.userType
        return line      
    def ukupnoKorisnika():
        return loginInfo.brojStudenata + loginInfo.brojAdmina + loginInfo.brojProfesora
    def findByUsername(givenUserName):
        c = 0
        for i in LoginInformacije:
            if i.userName == givenUserName:
                return c
            c = c +1
        return -1    

class Indeks:
    #objekti tipa indeks cuvaju skup ocena, predstavljen kao dve
    #paralelne liste, gde se na istom indeksu lista cuvaju
    #u jednoj ocena, a u drugoj predmet iz kog je dobijena
    def __init__(self, newBrojneVrednosti,newImenaPredmeta):
        self.brojneVrednosti=[]
        self.imenaPredmeta=[]
        for vrednost in newBrojneVrednosti:
            self.brojneVrednosti.append(vrednost)
        for ime in newImenaPredmeta:
            self.imenaPredmeta.append(ime)    
    def generateNew():
        NewIndeks = Indeks([],[])
        return NewIndeks
    def generateFromText(line1, line2):
        if line1 == "":
            return ""
        newBrojneVrednosti = line1.split(",")
        newImenaPredmeta = line2.split(",")
        newIndeks = Indeks(newBrojneVrednosti, newImenaPredmeta)
        return newIndeks
    def prosecnaOcena(self):
       sum = 0 
       for i in range(0,len(self.brojneVrednosti)):
           sum = sum + int(self.brojneVrednosti[i])
       return sum/(i+1) 

    #zbog specificnosti cuvanja (dve linije u fajlu umesto jedne), za objekat indeks
    #umesto predefinisanja metode __str__ koristimo posebnu metodu stringify
    def stringify(self):
        c = len(self.brojneVrednosti)
        line1 = ""
        line2 = ""
        for i in range(0,c):
            line1 = line1 + str(self.brojneVrednosti[i])
            if i<c-1:
                line1 = line1+","
        for i in range(0,c):
            line2 = line2 + self.imenaPredmeta[i]
            if(i<c-1):
                line2 = line2+","        
        return line1.strip(), line2.strip()
    def findByIndeks(trazeniIndeks):
        counter = 0
        for trazeniStudent in Studenti:
            if str(trazeniIndeks.strip()) == str(Studenti[counter].brojIndeksa.strip()):
                return counter
            counter = counter +1
        return -1
    def upisiOcenu(self, predmet, novaOcena):
        (self.brojneVrednosti).append(novaOcena)
        (self.imenaPredmeta).append(predmet)


class Student:
    #Klasa student cuva indeks, ime i prezime studenta
    #Studentu na i-toj poziciji odgovaraju indeks i loginInfo na i-tim pozicijama
    def __init__(self, NewIme, NewPrezime, newBrojIndeksa):
        #self.ID = newID
        self.Ime = NewIme
        self.Prezime = NewPrezime
        self.brojIndeksa = newBrojIndeksa
    def generateNew(NewIme,NewPrezime, newBrojIndeksa):
        newStudent = Student(NewIme, NewPrezime, newBrojIndeksa)
        return newStudent
    def generateFromText(line):
        if line == "":
            return ""
        args = line.split("|")
        argIme = args[0]
        argPrezime = args[1]
        argBrojIndeksa = args[2]
        newStudent = Student(argIme, argPrezime, argBrojIndeksa)
        return newStudent
    def __str__(self):
        line = self.Ime + "|" + self.Prezime + "|" + self.brojIndeksa
        return line
         
    

class PredstojeciIspiti:
    #objekat tipa predstojeci ispiti cuva predstojece ispite, predstavljene
    #preko naziva predmeta, datuma, i referenci na jednog profesora koji drzi ispit
    #i potencijalno vise studenata koji ga polazu
    def __init__(self,newIme, newDatumPolaganja, newProfesor, newStudenti):
        self.Ime = newIme
        self.DatumPolaganja = newDatumPolaganja
        self.Profesor = newProfesor
        self.Studenti = newStudenti
    def generateNew(newIme, newDatumPolaganja, newProfesor, newStudenti):
        NewPredstojeciIspit = PredstojeciIspiti(newIme, newDatumPolaganja, newProfesor, newStudenti)
        return NewPredstojeciIspit
    def generateFromText(line):
        if line == "":
            return ""
        args = line.split("|")
        argIme = args[0]
        argDatum = datetime.strptime(args[1],"%d.%m.%Y" )
        argProfesor = int(args[2])
        argStudenti = args[3].split(",")
        NewPredstojeciIspit = PredstojeciIspiti(argIme, argDatum, argProfesor, argStudenti)
        return NewPredstojeciIspit
    def __str__(self):
        pomLista = ""
        for i in range (0, len(self.Studenti)):
            pomLista = pomLista + str(self.Studenti[i])
            if i<len(self.Studenti)-1:
                pomLista = pomLista + ","        
        pomDatum = self.DatumPolaganja.strftime("%d.%m.%Y")
        line = self.Ime + "|" + pomDatum + "|" + str(self.Profesor) + "|" + pomLista +"\n"
        return line
    def findForStudents(pos):
        pomocniNiz = []
        row = 0
        for ispit in Ispiti:
            for i in range(0, len(ispit.Studenti)):
                print(pos, ispit.Studenti[i])
                if ispit.Studenti[i] == str(pos):
                    pomocniNiz.append(row)
            row = row +1
            print(pomocniNiz)
        return pomocniNiz
    def findForProfesors(pos):
        pomocniNiz = []
        row = 0
        for ispit in Ispiti:
            if int(ispit.Profesor) == pos:
                pomocniNiz.append(row)
            row = row +1
        return pomocniNiz
    def findByImeIspita(currentImeIspita):
        counter = 0
        for iterator in Ispiti:
            if(iterator.Ime.strip() == currentImeIspita.strip()):
                return counter
            counter = counter +1
        return -1    
    def prijaviStudenta(self, brojIndeksa):
        if not brojIndeksa in self.Studenti:
            self.Studenti.append(brojIndeksa)
    def ukloniStudenta(self, redniBroj):
        if redniBroj in self.Studenti:
            del(redniBroj)        

class Profesor:
    #profesor je jednostavna klasa koja pamti samo ime i prezime
    #i-tom profesoru odgovara i+n-ti red u loginInfo, gde je n broj objekata tipa Student
    def __init__(self,newIme, newPrezime):
        self.Ime = newIme
        self.Prezime = newPrezime
    def generateNew(newIme, newPrezime):
        newProfesor = Profesor(newIme, newPrezime)
        return newProfesor
    def generateFromText(line):
        if line == "":
            return ""
        args = line.split("|")
        argIme = args[0]
        argPrezime = args[1]
        newProfesor = Profesor(argIme, argPrezime)
        return newProfesor
    def __str__(self):
        line = self.Ime + "|" + self.Prezime
        return line
    def findByImePrezime(currentIme, currentPrezime):
        counter = 0
        for iterator in Profesori:
            if(iterator.Ime.strip() == currentIme.strip() and iterator.Prezime.strip() == currentPrezime):
                return counter
            counter = counter + 1
        return -1    

class Administrator:
    #slicno klasi profesor, klasa administrator pamti samo ime i prezime
    #i-tom Administratoru odgovara i+m-ti red u loginInfo
    #gde je m zbir broja objekata Tipa student i Profesor
    def __init__(self, newIme, newPrezime):
        self.Ime = newIme
        self.Prezime = newPrezime
    def generateNew(newIme, newPrezime):
        newAdministrator = Administrator(newIme, newPrezime)
        return newAdministrator
    def generateFromText(line):
        if line == "":
            return ""
        args = line.split("|")
        argIme = args[0]
        argPrezime = args[1]
        newAdministrator = Administrator(argIme, argPrezime)
        return newAdministrator
    def __str__(self):
        line = self.Ime + "|" + self.Prezime
        return line
    def findByImePrezime(currentIme, currentPrezime):
        counter = 0
        for iterator in Admini:
            if(iterator.Ime.strip() == currentIme.strip() and iterator.Prezime.strip() == currentPrezime):
                return counter
            counter = counter + 1
        return -1   

LoginInformacije = []
Studenti = []
Profesori = []
Admini = []
Ispiti = []
Indeksi = []

def rangLista():
    nerangirani = []
    for iterator in Studenti:
        if Indeks.findByIndeks(iterator.brojIndeksa)!=-1:
            nerangirani.append(Indeksi[iterator.brojIndeksa])
    rangirani = nerangirani.sort(self.prosecnaOcena())
    return rangirani

def alert(broj, tip):
    if tip[0]=="s":
        incoming = PredstojeciIspiti.findForStudents(broj)
        for iterator in incoming:
            tmp = (Ispiti[iterator].DatumPolaganja - datetime.now())
            if int(tmp.days) < 7:
                print("imate ispit iz " +Ispiti[iterator].Ime + " za manje od 7 dana")
    if tip[0]=="p":
        incoming = PredstojeciIspiti.findForProfesors(broj)
        for iterator in incoming:
            tmp = (Ispiti[iterator].DatumPolaganja - datetime.now())
            if int(tmp.days) < 7:
                print("imate ispit iz " +Ispiti[iterator].Ime + " za manje od 7 dana")               
def loadPeople(LoginInfoTable, StudentiTable, ProfesoriTable, AdminiTable):
    #load People inicijalizuje nizove Studenti, Profesori, Admini, i LoginInformacije
    #tokom rada programa operisemo direktno sa ovim nizovima, pazljivo prateci promene
    #sve promene nad njima se zaista propagiraju na nase .txt fajlove tek pozivom metoda
    #unload na kraju programa
    loginInfoReader = open(LoginInfoTable, "r+")
    for line in loginInfoReader:
        currentLoginInfo = loginInfo.generateFromText(line)
        LoginInformacije.append(currentLoginInfo)
        if currentLoginInfo.userType[0] == 's':
            loginInfo.brojStudenata = loginInfo.brojStudenata+1
        elif currentLoginInfo.userType[0] == 'p':
            loginInfo.brojProfesora = loginInfo.brojProfesora+1
        if currentLoginInfo.userType[0] == 'a':
            loginInfo.brojAdmina = loginInfo.brojAdmina+1

    StudentReader = open(StudentiTable, "r+")
    for line in StudentReader:
        Studenti.append(Student.generateFromText(line))

    ProfesoriReader = open(ProfesoriTable, "r+")
    for line in ProfesoriReader:
        Profesori.append(Profesor.generateFromText(line))
   
    AdminiReader = open(AdminiTable, "r+")
    for line in AdminiReader:
        Admini.append(Administrator.generateFromText(line))

    loginInfoReader.close()
    StudentReader.close()    
    ProfesoriReader.close()    
    AdminiReader.close()        

def loadBirokratija(ispitiTable, indeksiTable):
    #ova metoda inicijalizuje nizove ispiti i indeksi
    #kao i sa ostalima, sa ovim nizovima operisemo direktno, a promene se propagiraju na fajlove
    #tek pri gasenju programa
    IspitReader = open(ispitiTable, "r+")
    for line in IspitReader:
        Ispiti.append(PredstojeciIspiti.generateFromText(line))
    
    IndeksReader = open(indeksiTable, "r+")
    IndeksLines = IndeksReader.readlines()
    i=0
    while(i<len(IndeksLines)):
        Indeksi.append(Indeks.generateFromText(IndeksLines[i].strip(),IndeksLines[i+1].strip()))
        i = i+2

    IspitReader.close()    
    IndeksReader.close()        
        
def unload(LoginInfoTable, StudentiTable, ProfesoriTable, AdminiTable, ispitiTable, indeksiTable):
    #unload je nasa metoda koja "cuva" stanje promenljivih van rada programa
    loginInfoReader = open(LoginInfoTable, "w")    
    for i in range(0, len(LoginInformacije)):
        loginInfoReader.write(str(LoginInformacije[i]).strip()+"\n")
    StudentReader = open(StudentiTable, "w")
    for i in range (0, len(Studenti)):
        StudentReader.write(str(Studenti[i]).strip()+"\n")

    ProfesoriReader = open(ProfesoriTable, "w")
    for i in range (0, len(Profesori)):
        ProfesoriReader.write(str(Profesori[i]).strip()+"\n")

    AdminiReader = open(AdminiTable, "w")
    for i in range (0, len(Admini)):
        AdminiReader.write(str(Admini[i]).strip()+"\n")

    IspitReader = open(ispitiTable, "w")
    for i in range (0, len(Ispiti)):
        IspitReader.write(str(Ispiti[i]).strip()+"\n")

    IndeksReader = open(indeksiTable, "w")
    i = 0
    while(i<len(Indeksi)):
        firstline, secondline = Indeksi[i].stringify()
        IndeksReader.write(firstline.strip()+"\n")
        IndeksReader.write(secondline.strip()+"\n")
        i = i+ 2

    loginInfoReader.close()
    StudentReader.close()    
    ProfesoriReader.close()    
    AdminiReader.close()
    IspitReader.close()    
    IndeksReader.close()    

def StudentLoop(pos):
    #metoda iz koje ce student pristupati radnom okruzenju
    print("pozdrav," + Studenti[pos].Ime)
    alert(pos, "s")
    control = ""
    while(control != "e"):
        print("za pregled predstojecih ispita, unesite karakter i")
        print("za pregled polozenih ispita, unesite karakter p")
        print("za odjavu sa sistema, unesite karakter e")
        control = input()[0]
        if(control == 'i'):
            predstojeciIspiti = PredstojeciIspiti.findForStudents(pos)
            if len(predstojeciIspiti)!= 0:
                for i in predstojeciIspiti:
                    print("na dan " + Ispiti[i].DatumPolaganja.strftime("%d.%m.%Y") + "imate ispit iz predmeta " + Ispiti[i].Ime)
            else:
                print("nemate predstojecih ispita")
        if(control == 'p'):
            currentIndeks = Indeksi[pos]
            if len(currentIndeks.brojneVrednosti) == 0:
                print("niste jos polozili nijedan ispit")
            else:
                for i in range(0, len(currentIndeks.brojneVrednosti)):
                    print(currentIndeks.imenaPredmeta[i] + " - " + currentIndeks.brojneVrednosti[i])
                print("zajedno, to daje prosek " + str(currentIndeks.prosecnaOcena()))    
               
def ProfesorLoop(pos):
    #metoda iz koje ce profesor pristupati radnom okruzenju
    print("pozdrav,profesore " + Profesori[pos].Ime)
    alert(pos, "p")
    control = ""
    while(control != "e"):
        print("za pregled predstojecih ispita, unesite karakter i")
        print("za zakazivanje novog ispita, unesite karakter p")
        print("za upisivanje ocene, unesite karakter o")
        print("za odjavu sa sistema, unesite karakter e")
        #print("za pregled rang liste, unesite karakter r")
        control = input()[0]
        if(control == 'i'):
            predstojeciIspiti = PredstojeciIspiti.findForProfesors(pos)
            if len(predstojeciIspiti)!= 0:
                for i in predstojeciIspiti:
                    print("na dan " + Ispiti[i].DatumPolaganja.strftime("%d.%m.%Y") + "imate ispit iz predmeta " + Ispiti[i].Ime)
            else:
                print("nemate predstojecih ispita")
        if(control == "p"):
            print("unesite ime predmeta iz kog zakazujete ispit")
            currentImeIspita = input()
            print("unesite datum polaganja ispita u formatu dd mm YYYY")
            currentDatumString = input()
            currentDatum = datetime.strptime(currentDatumString, "%d %m %Y")
            Ispiti.append(PredstojeciIspiti.generateNew(currentImeIspita, currentDatum, pos, []))
        if(control == "o"):
            print("unesite indeks studenta kom upisujete ocenu")
            currentIndeks = input()
            c = Indeks.findByIndeks(currentIndeks)
            if c!=-1:
                print("unesite predmet iz kog upisujete ocenu")
                currentPredmet = input()
                print("unesite ocenu")
                currentOcena = eval(input())
                Indeksi[c].upisiOcenu(currentPredmet.strip(), currentOcena)
            else:
                print("ne postoji student sa tim indeksom")                 

def AdminLoop(pos):
    #metoda iz koje ce admin pristupati radnom okruzenju
    print("pozdrav,admine " + Admini[pos].Ime)
    control = '-1'
    while(control!='e'):
        print("za zakazivanje novog ispita, unesite karakter p")
        print("za prijavljivanje ispita studentu, unesite karakter i")
        print("za brisanje osobe sa sistema, unesite karakter b")
        print("za brisanje ispita sa sistema, unesite karakter c")
        print("za dodavanje studenta, unesite karakter s")
        print("za dodavanje profesora, unesite karakter f")
        print("za dodavanje administratora, unesite karakter a")
        print("za odjavu sa sistema, unesite karakter e")
        control = input()[0]
        if(control =='p'):
            print("unesite ime profesora koji ce drzati ispit")
            currentIme = input()
            print("unesite prezime profesora koji ce drzati ispit")
            currentPrezime = input()
            c = Profesor.findByImePrezime(currentIme, currentPrezime)
            if(c == "-1"):
                print("ne postoji taj profesor")
            else:
                print("unesite naziv predmeta")
                currentPredmet = input()
                print("unesite datum polaganja ispita u formatu dd mm YYYY")
                currentDatumString = input()
                currentDatum = datetime.strptime(currentDatumString, "%d %m %Y")
                Ispiti.append(PredstojeciIspiti.generateNew(currentPredmet, currentDatum, c, []))                
        if control =='i':
            print("unesite indeks studenta kom prijavljujete ispit")
            currentIndeks = input()
            c = Indeks.findByIndeks(currentIndeks)
            if c == '-1':
                print("nema studenta sa tim indeksom")
            else:
                print("unesite ime ispita za koji ga prijavljujete")
                currentImeIspita = input()
                i = PredstojeciIspiti.findByImeIspita(currentImeIspita)
                if(i == '-1'):
                    print("nema tog ispita - molimo zakazite ga")
                else:
                    Ispiti[i].prijaviStudenta(c)    

        if control =='b':
            typecontrol ='-1'
            print("unesite tip korisnika kog brisete - s, p, ili a")
            typecontrol = input()[0]
            if(typecontrol == 's'):
                print("unesite broj indeksa studenta kog brisete")
                currentIndeks = input()
                c = Indeks.findByIndeks(currentIndeks)
                if(c=='-1'):
                    print("nema studenta sa tim indeksom")
                else:
                    loginInfo.brojStudenata = loginInfo.brojStudenata-1
                    for iterator in Ispiti:
                        iterator.ukloniStudenta(c)
                    del(Studenti[c])
                    del(Indeksi[c])
                    del(LoginInformacije[c])
            elif(typecontrol == 'p'): 
                print("unesite ime profesora kog brisete")
                currentIme = input()
                print("unesite prezime profesora kog brisete")
                currentPrezime = input()
                c = Profesor.findByImePrezime(currentIme, currentPrezime)
                if(c == "-1"):
                    print("ne postoji taj profesor")
                else:
                    loginInfo.brojProfesora = loginInfo.brojProfesora-1
                    i=0
                    for iterator in Ispiti:
                        if iterator.Profesor == c:
                            del(Ispiti[i])
                        i=i+1
                    del(LoginInformacije[c + loginInfo.brojStudenata])
                    del(Profesori[c])        
            elif(typecontrol == 'a'):
                print("unesite ime admina kog brisete")
                currentIme = input()
                print("unesite prezime admina kog brisete")
                currentPrezime = input()
                c = Administrator.findByImePrezime(currentIme, currentPrezime)
                if(c == "-1"):
                    print("ne postoji taj profesor")
                else:
                    loginInfo.brojAdmina = loginInfo.brojAdmina-1
                    del(LoginInformacije[c+loginInfo.brojStudenata+loginInfo.brojProfesora])
                    del(Admini[c])   
        if control =='c':
            print("unesite ime ispita koji brisete")
            currentIspit = input()
            c = PredstojeciIspiti.findByImeIspita(currentIspit)
            if(c=='-1'):
                print("ne postoji taj ispit")
            else:
                del(Ispiti[c])    
        if control =='s':
            print("unesite ime, prezime, broj indeksa, username i pass za novog studenta")
            currentIme = input()
            currentPrezime = input()
            currentBrojIndeksa = input()
            currentUserName = input()
            currentPass = input()
            Studenti.append(Student.generateNew(currentIme, currentPrezime, currentBrojIndeksa))
            LoginInformacije.insert(loginInfo.brojStudenata, loginInfo.generateNew(currentUserName, currentPass, "s"))
            loginInfo.brojStudenata = loginInfo.brojStudenata+1
        if control =='f':
            print("unesite ime, prezime,username i pass za novog profesora")
            currentIme=input()
            currentPrezime=input()
            currentUserName=input()
            currentPass=input()
            Profesori.append(Profesor.generateNew(currentIme, currentPrezime))
            LoginInformacije.insert(loginInfo.brojStudenata + loginInfo.brojProfesora, loginInfo.generateNew(currentUserName, currentPass, "p"))
            loginInfo.brojProfesora = loginInfo.brojProfesora+1

        if control =='a':
            print("unesite ime, prezime,username i pass za novog admina")
            currentIme=input()
            currentPrezime=input()
            currentUserName=input()
            currentPass=input()
            Admini.append(Administrator.generateNew(currentIme, currentPrezime))
            LoginInformacije.insert(loginInfo.brojStudenata + loginInfo.brojProfesora+loginInfo.brojAdmina, loginInfo.generateNew(currentUserName, currentPass, "a"))
            loginInfo.brojAdmina = loginInfo.brojAdmina+1



def main():
    loadPeople("loginInfo.txt", "Studenti.txt", "Profesori.txt", "Administratori.txt")
    loadBirokratija("Ispiti.txt", "Indeksi.txt")
    if(len(LoginInformacije)) == 0:
        LoginInformacije.append(loginInfo.generateNew("admin","admin","a"))
        Admini.append(Administrator.generateNew("admin","admin"))
    print("unesite korisnicko ime")
    curentUserName = input()
    c = loginInfo.findByUsername(curentUserName)
    if c != -1:
        currentUser = LoginInformacije[c]
    else:
        print("uneli ste nekorektno korisnicko ime. Bicete izbaceni sa sistema")
        return
    print("unesite lozinku")
    currentPass = input()
    if(currentPass) != currentUser.password:
        print("uneli ste nekorektnu lozinku. Bicete izbaceni sa sistema")
    elif(currentUser.userType[0]=="s"):
        StudentLoop(c)
    elif(currentUser.userType[0]=="p"):
        ProfesorLoop(c-loginInfo.brojStudenata)
    elif(currentUser.userType[0]=="a"):
        AdminLoop(c-loginInfo.brojStudenata-loginInfo.brojProfesora)                  


    unload("loginInfo.txt", "Studenti.txt", "Profesori.txt", "Administratori.txt","Ispiti.txt", "Indeksi.txt")

if __name__ == '__main__':
    main()    

