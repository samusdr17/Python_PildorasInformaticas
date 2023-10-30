miDiccionario={"Alemania":"Berlín","Francia":"París","Reino Unido":"Londres", "España":"Madrid"}
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)    
miDiccionario["Italia"]="Roma"
print(miDiccionario)
del miDiccionario["Reino Unido"]
print(miDiccionario)


miDiccionario2={"Alemania":"Berlín", 23:"Jordan", "Mosqueteros":3}
print(miDiccionario2)


miTupla=("España", "Francia", "Reino Unido", "Alemania")
miDiccionario3={miTupla[0]:"Madrid", miTupla[1]:"París", miTupla[2]:"Londres", miTupla[3]:"Berlín"}
print(miDiccionario3)


miDiccionario4={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionario4.keys())
print(miDiccionario4.values())
print(len(miDiccionario4))
print(miDiccionario4)