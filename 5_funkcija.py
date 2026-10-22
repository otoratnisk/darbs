def cena_ar_atlaidi(cena, atlaide=10):
    return cena - (cena * atlaide / 100)


print(cena_ar_atlaidi(100))


print(cena_ar_atlaidi(100, 25))