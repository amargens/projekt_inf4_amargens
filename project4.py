#Tabeli tegemise koodi sain siit: http://askubuntu.com/questions/741966/listbox-with-tkinter-treeview-how-to-avoid-empty-rows-at-the-end
#Ise oleks tahtnud proovida ka Plotly'ga teha, aga tekkisid komplikatsioonid "online" saamisega.
import itertools
from random import randint
from string import Formatter
import tkinter as tk
import tkinter.ttk as ttk

#---------------Funktsioonid---------------------
#Pakib itertool'sist saadud enniku lahti listiks.
def pakkimine(tuubel):
    uuslist = []
    uuslist = list(itertools.chain(*tuubel))
    return uuslist

#Loeb sisse tekstifaili ja saame sealt nimed ja tiimi overall'i, kui on paaritu arv tiime, siis lisab ühe ajutise tiimi juurde, mis on random overall'iga
def loefail(failinimi):
    tiimid = {}
    f = open(failinimi)
    for rida in f:
        osad = rida.strip().split(":")
        tiim = osad[0]
        osad[1]=int(osad[1])
        tiimid[tiim] = osad[1]
    f.close()
    if len(tiimid) % 2 == 0:
        return tiimid
    else:
        tiimid["Ajutine_tiim"] = randint(1,100)
        return tiimid

#Algeline skoorimine, kus võrreldakse tiimi overall'i, kui on suurem, siis on võimalus, et tiim lööb rohkem väravaid ja teine tiim lööb vähem.
def skoorimine(tiim1, tiim2, sõnastik):
    skoor1 = 0
    skoor2 = 0
    for k,v in sõnastik.items():
        if sõnastik[tiim1] > sõnastik[tiim2]:
            skoor1 = randint(0,4)
            skoor2 = randint(0,2)
        else:
            skoor1 = randint(0,2)
            skoor2 = randint(0,4)
    return skoor1, skoor2

#Siit teen sõnastiku väärtustest listi, et neid kasutada saaks.
def sõnast_list(sõnastik):
    listikas = list(sõnastik.values())
    return listikas

#-------------------Põhiline kood-----------------------------
#Algab siit, kus kasutan funktsiooni, et saada kätte tiimid.
tiim_sõnastik = loefail("tiimid.txt")
print(tiim_sõnastik)
print()
#Siin tulevad vastasseisud
paarid = list(itertools.combinations(loefail("tiimid.txt"), 2))
print(paarid)
#pakib ennikud lahti listiks.
õhuke_paar = pakkimine(paarid)
print()

#Siit saame kätte skoorid.
skoorid = []
for i in range(0, len(õhuke_paar), 2):
    pakk = skoorimine(õhuke_paar[i], õhuke_paar[i+1], tiim_sõnastik)
    skoorid.append(pakk)
#Pakime skoorid lahti listiks
y = list(itertools.chain(*skoorid))

#Tühjad sõnastikud selleks, et näha, palju tiim punkte sai jne.
punktid = {}
löödud_väravad = {}
lastud_väravad = {}
vahe = {}

#Siit saan punktid, löödud väravad, lastud väravad ja väravate vahe.
for i in range(0, len(õhuke_paar), 2):
    if y[i] > y[i+1]:
        print(õhuke_paar[i], "võitis", õhuke_paar[i+1]+"t", "kodus skooriga:".ljust(20)+"||", y[i],"-",y[i+1],"||")
        punktid[õhuke_paar[i]] = punktid.get(õhuke_paar[i], 0) + 3
        punktid[õhuke_paar[i+1]] = punktid.get(õhuke_paar[i+1], 0) + 0
        löödud_väravad[õhuke_paar[i]] = löödud_väravad.get(õhuke_paar[i], 0) + y[i]
        löödud_väravad[õhuke_paar[i+1]] = löödud_väravad.get(õhuke_paar[i+1], 0) + y[i+1]
        lastud_väravad[õhuke_paar[i]] = lastud_väravad.get(õhuke_paar[i], 0) + y[i+1]
        lastud_väravad[õhuke_paar[i+1]] = lastud_väravad.get(õhuke_paar[i+1], 0) + y[i]
        vahe[õhuke_paar[i]] = vahe.get(õhuke_paar[i], 0) + y[i] - y[i+1]
        vahe[õhuke_paar[i+1]] = vahe.get(õhuke_paar[i+1], 0) + y[i+1] - y[i]
    elif y[i+1] > y[i]:
        print(õhuke_paar[i+1], "võitis", õhuke_paar[i]+"t", "võõrsil skooriga:".ljust(20)+"||", y[i+1],"-",y[i],"||")
        punktid[õhuke_paar[i+1]] = punktid.get(õhuke_paar[i+1], 0) + 3
        punktid[õhuke_paar[i]] = punktid.get(õhuke_paar[i], 0) + 0
        löödud_väravad[õhuke_paar[i+1]] = löödud_väravad.get(õhuke_paar[i+1], 0) + y[i+1]
        löödud_väravad[õhuke_paar[i]] = löödud_väravad.get(õhuke_paar[i], 0) + y[i]
        lastud_väravad[õhuke_paar[i]] = lastud_väravad.get(õhuke_paar[i], 0) + y[i+1]
        lastud_väravad[õhuke_paar[i+1]] = lastud_väravad.get(õhuke_paar[i+1], 0) + y[i]
        vahe[õhuke_paar[i]] = vahe.get(õhuke_paar[i], 0) + y[i] - y[i+1]
        vahe[õhuke_paar[i+1]] = vahe.get(õhuke_paar[i+1], 0) + y[i+1] - y[i]
    else:
        print("Viik", õhuke_paar[i], "ja", õhuke_paar[i+1], "vahel, skoor:".ljust(19)+"||", y[i],"-",y[i+1],"||")
        punktid[õhuke_paar[i+1]] = punktid.get(õhuke_paar[i], 0) + 1
        punktid[õhuke_paar[i]] = punktid.get(õhuke_paar[i], 0) + 1
        löödud_väravad[õhuke_paar[i+1]] = löödud_väravad.get(õhuke_paar[i+1], 0) + y[i+1]
        löödud_väravad[õhuke_paar[i]] = löödud_väravad.get(õhuke_paar[i], 0) + y[i]
        lastud_väravad[õhuke_paar[i]] = lastud_väravad.get(õhuke_paar[i], 0) + y[i+1]
        lastud_väravad[õhuke_paar[i+1]] = lastud_väravad.get(õhuke_paar[i+1], 0) + y[i]
        vahe[õhuke_paar[i]] = vahe.get(õhuke_paar[i], 0) + y[i] - y[i+1]
        vahe[õhuke_paar[i+1]] = vahe.get(õhuke_paar[i+1], 0) + y[i+1] - y[i]

print()
#Prindin siin välja sõnastikud, et oleks hea ülevaade.
print("Punktid: ")
print(punktid)
print("Löödud väravad: ")
print(löödud_väravad)
print("Lastud väravad: ")
print(lastud_väravad)
print("Väravate vahe: ")
print(vahe)

#Siin võtan sõnastiku väärtused ja teen listi, mille sees on need väärtused ennikuna selleks, et saaks tabelisse panna arvud.
tühi_list = []
võtmed = list(punktid.keys())
võtmed.insert(0,"")
list_punkt = sõnast_list(punktid)
list_punkt.insert(0,"Punktid")
list_löödud = sõnast_list(löödud_väravad)
list_löödud.insert(0,"Löödud väravad")
list_lastud = sõnast_list(lastud_väravad)
list_lastud.insert(0,"Lastud väravad")
list_vahe = sõnast_list(vahe)
list_vahe.insert(0,"Väravate vahe")
tühi_list.append(list_punkt)
tühi_list.append(list_löödud)
tühi_list.append(list_lastud)
tühi_list.append(list_vahe)
tühja_tuple = [tuple(l) for l in tühi_list]

#-----------------Tabeli tegemine--------------------------
laius = 200*len(võtmed)
class AppBase:
    def __init__(self):
        self.mywin = tk.Tk()
        self.mywin.geometry("%dx%d+%d+%d" % (laius, 105, 0, 350))
        self.frame1 = tk.Frame(self.mywin)
        self.frame1.pack()

        lb_header = võtmed
        lb_list = tühja_tuple

        self.tree = ttk.Treeview(columns=lb_header, show="headings", height=len(lb_list))
        self.tree.grid(in_=self.frame1)

        for col in lb_header:
            self.tree.heading(col, text=col.title())
        for item in lb_list:
            self.tree.insert('', 'end', values=item)

    def start(self):
        self.mywin.mainloop()

app=AppBase()
app.start()