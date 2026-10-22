pirsk = int(input("iedod 1 sk: "))
otrsk = int(input("iedod 2 sk: "))
tresk = int(input("iedod 3 sk: "))

if pirsk>otrsk and pirsk>tresk:
    print(pirsk)
elif otrsk>pirsk and otrsk>tresk:
    print(otrsk)
else:
    print(tresk)