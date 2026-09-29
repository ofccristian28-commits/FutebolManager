ESTADUAIS = {
"PE":"Pernambucano","SP":"Paulista","RJ":"Carioca","MG":"Mineiro",
"BA":"Baiano","CE":"Cearense","RS":"Gaúcho","PR":"Paranaense",
"SC":"Catarinense","GO":"Goiano","PA":"Paraense","PB":"Paraibano",
"AL":"Alagoano","RN":"Potiguar","SE":"Sergipano","PI":"Piauiense",
"MA":"Maranhense","ES":"Capixaba","DF":"Brasiliense","MT":"Mato-Grossense",
"MS":"Sul-Mato-Grossense","AM":"Amazonense","RO":"Rondoniense",
"AC":"Acreano","AP":"Amapaense","RR":"Roraimense","TO":"Tocantinense"
}

REGIONAIS = [
"Copa do Nordeste",
"Copa Verde"
]

NACIONAIS = [
"Brasileirão Série A",
"Brasileirão Série B",
"Brasileirão Série C",
"Brasileirão Série D",
"Copa do Brasil"
]

def mostrar_competicoes():
    print("\n=== COMPETIÇÕES ===")
    print("\nEstaduais:")
    for nome in ESTADUAIS.values():
        print("-", nome)
    print("\nRegionais:")
    for nome in REGIONAIS:
        print("-", nome)
    print("\nNacionais:")
    for nome in NACIONAIS:
        print("-", nome)
