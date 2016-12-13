import itertools
from random import randint
from string import Formatter

#Pakib itertool'sist saadud enniku lahti listiks.
def pakkimine(tuubel):
    uuslist = []
    uuslist = list(itertools.chain(*tuubel))
    return uuslist
#Loeb sisse tekstifaili ja saame sealt nimed ja tiimi overall'i
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
#Algeline skoorimine, kus võrreldakse tiimi overall'i
def skoorimine(tiim1, tiim2, sõnastik):
    skoor1 = 0
    skoor2 = 0
    for k,v in sõnastik.items():
        if sõnastik[tiim1] > sõnastik[tiim2]:
            skoor1 = randint(0,4)
            skoor2 = randint(0,3)
        else:
            skoor1 = randint(0,2)
            skoor2 = randint(0,4)
    return skoor1, skoor2

#Algab siit, kus kasutan funktsiooni, et saada kätte tiimid.
tiim_sõnastik = loefail("tiimid.txt")
print(tiim_sõnastik)

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

#Sõnastikud
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

print("Punktid: ")
print(punktid)
print("Löödud väravad: ")
print(löödud_väravad)
print("Lastud väravad: ")
print(lastud_väravad)
print("Väravate vahe: ")
print(vahe)