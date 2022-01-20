import random

vardi = ["LIETUSSARGS", "SPOGULIS", "ZILONIS", "MELLENE", "STĀRĶIS", "PAVASARIS", "MĀKONIS"]
vards = random.choice(vardi)

liekieBurti = int(len(vards)/1.5)
sleptieBurti = []
for x in range(liekieBurti):
  pozicija = random.randrange(0, len(vards))
  if not vards[pozicija] in sleptieBurti:
    sleptieBurti.append(vards[pozicija])

minamaisVards = vards
for x in sleptieBurti:
  minamaisVards = minamaisVards.replace(x, "_")

#VĀRDA MINĒŠANA
print("***UZMINI VĀRDU***")

minamaisVardsSarakstaa = []
for burts in minamaisVards:
  minamaisVardsSarakstaa.append(burts)

while "_" in minamaisVardsSarakstaa:
  
  def drukaaVardu():
    for burts in minamaisVardsSarakstaa:
      print(burts, end="")
  drukaaVardu()

  burts = input("\nEnter your guess!")
  burts = burts.upper()
  if burts in sleptieBurti:
    for x in range(len(vards)):
      if burts == vards[x]:
        minamaisVardsSarakstaa[x] = burts
else:
  drukaaVardu()
  print("\nVārds atminēts!")