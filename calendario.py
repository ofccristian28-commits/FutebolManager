from competicoes import ESTADUAIS, REGIONAIS, NACIONAIS

def calendario_clube(clube, estado):
    estadual = ESTADUAIS.get(estado)
    print("\n=== CALENDÁRIO ===")
    if estadual:
        print("🏆", estadual)
    print("🏆 Brasileirão")
    print("🏆 Copa do Brasil")
    print("🏆 Copa do Nordeste" if estado in ["PE","CE","BA","AL","SE","PB","RN","PI","MA"] else "")
    print("\nClube:", clube)
