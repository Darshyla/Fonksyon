import random
import re
#from slugify import slugify

print("1-Jenere yon kod aleyatwa ki gen n karaktè alfabetik san repetisyon")
print("Konbyen karaktè pou kod la genyen? n<=26")
n=input()
while int(n)>26 or int(n)<1:
    print("Antre yon valè ki pa depase 26 e ki pa pi piti ke 1")
    n=input()
alfabe="abcdefghijklmnopqrstuvwxyz"
kod_alfa= lambda alfa, kantite: "".join(random.sample(alfa,kantite))
kod=kod_alfa(alfabe, int(n))
print("Kod la se: ",kod,"\n\n")

print("2-Jenere yon kod aleyatwa ki gen 13 karaktè alfanimerik san repetisyon")
print("Konbyen karaktè pou kod la genyen?")
n=input()
while int(n)<1 or int(n)>35:
    print("Antre yon valè ant 1 ak 35")
    n=input()
alfanimerik="abcdefghijklmnopqrstuvwxyz0123456789"
kod_alfanimerik= lambda alfa, kantite: "".join(random.sample(alfa, kantite))
kod=kod_alfanimerik(alfanimerik, int(n))
print("Kod la se:", kod,"\n\n")
                                               
#print("3-Jenere yon SLUG a pati yon chèn karaktè")
#print("Antre yon chèn karaktè")
#n=input()
#slug = lambda chen: slugify(chen)
#print("Karaktè ki se SLUG nan chèn sa se:",slug(n), "\n\n")

print("4-Separe chak lèt nan yon mo pa yon vigil")
print("Antre yon chèn karaktè")
n=input()
separasyon= lambda mo: ",".join(list(mo))
print("Aprè separasyon:", separasyon(n), "\n\n")

      
print("5-kripte yon mo ak endèks li nan alfabè a")
n=input("Antre yon chèn karaktè: ")
kripte=lambda mo: "-".join([str(ord(elt)-97) for elt in mo.lower()])
print(kripte(n),"\n\n")
                           

print("6-Dekripte yon mo ki fèt ak endèks chak lèt nan alfabè a")
n=input("Antre yon chèn karaktè: ")
dekripte= lambda mo: "".join(chr(int(elt)+97)for elt in re.findall(r'\d+',mo))
print(dekripte(n), "\n\n")

print("7Pèmite 2 varyab")
def pemite():
    a=input("Antre premye varyab la: ")
    b=input("Antre 2èm varyab la: ")
    c=a
    a=b
    b=c
    print(a, b)
pemite()

print("\n\n8-Afiche inisyal chak mo")
n=input("Antre fraz wap ekri a: ")
inisyal= lambda fraz:"-".join([n[0] for n in fraz.replace("-"," ").split()])
print(inisyal(n),"\n\n")

inisyal(n)
        
    

