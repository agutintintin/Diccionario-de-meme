meme = {
"CRINGE": "Algo excepcionalmente raro o embarazoso",
"LOL": "Una respuesta común a algo gracioso",
"ROFL": "una respuesta a una broma",
"SHEESH": "ligera desaprobación",
"CREEPY": "aterrador, siniestro",
"AGGRO": "ponerse agresivo/enojado",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

while True:
    
    if word in meme.keys():
        print(word, "esta palabra significa", meme[word])
        word = input("¿quieres buscar algo mas?)"
                     
    else:
        print("No se a encontrado esta palabra")
        word = input("¿quieres buscar algo mas?)"
