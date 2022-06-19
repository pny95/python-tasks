# 1.feladat
maxpont = int(input("Kérem a maximális pontszámot: "))
elertpont = int(input("Kérem az elért pontszámot: "))
ponthatar = maxpont * 0.25

if elertpont >= ponthatar:
    print("A vizsga sikeres")
else:
    print('A vizsga sikertelen')
if elertpont > 90:
    print("Gratulálok, szép teljesítmény!")

# 2.feladat
be = int(input("Magasságok:"))
magassagok=[]
magasak=[]
alacsonyak=[]
while be != 0:
    magassagok.append(be)
    if be >= 180:
        magasak.append(be)
    else:
        alacsonyak.append(be)
    be =int(input())
print("Alacsonyak:", end=" ")
for a in alacsonyak:
    print(a, end=" ")
print()
print("Magasak:", end=" ")
for m in magasak:
    print(m, end=" ")
print()
print("A tanulók átlagmagassága: {0:.2f}".format(sum(magassagok)/len(magassagok)),"cm")
print("A legmagasabb alacsony tanuló magassága:",max(alacsonyak),"cm")

# 3.feladat
class Busz:
    def __init__(self, sor):
        seged = sor.strip().split(";")
        self.rendszam = seged[0]
        self.tavolsag = int(seged[1])
        self.fogyasztas = float(seged[2])

fogyasztas=[]
f = open("fogyasztas.txt", "r", encoding="utf-8")
for sor in f:
    akt = Busz(sor.strip())
    fogyasztas.append(akt)
f.close()
print("A beolvasott buszok száma:",len(fogyasztas))

maxtavolsag = 0
maxrendszam = []
for f in fogyasztas:
    if f.tavolsag > maxtavolsag:
        maxtavolsag = f.tavolsag
        maxrendszam = f.rendszam
print("A legnagyobb távolságot megtett busz rendszáma:", maxrendszam )

def atlagfogyasztas( tavolsag, fogyasztas ):
    return (fogyasztas / tavolsag) * 100

fbuszok= []
ftavolsag =0
ffogyasztas= 0
for f in fogyasztas:
    if atlagfogyasztas(f.tavolsag,f.fogyasztas) > 9:
        fbuszok = f.rendszam
        ftavolsag = f.tavolsag
        ffogyasztas = f.fogyasztas
print("A 9 liternél többet fogyasztó buszok listája: {0:.2f}".format(atlagfogyasztas(ftavolsag,ffogyasztas)),fbuszok)


