import random

def jogar_partida(clube, adversario, elenco):
    placar=[0,0]
    formacao="4-4-2"
    titulares=elenco[:11]

    print(f"\n⚽ {clube} x {adversario}")
    input("ENTER para iniciar o 1º tempo...")

    for minuto in [15,30,45]:
        if random.random()<0.18:
            placar[random.randrange(2)]+=1
            print(f"\n⚽ GOL! {minuto}'")
        print(f"{minuto}' - {clube} {placar[0]} x {placar[1]} {adversario}")

    print("\n========== INTERVALO ==========")
    print(f"Placar: {placar[0]} x {placar[1]}")
    print("Formação:",formacao)
    print("1 - Continuar")
    print("2 - Substituir")
    print("3 - Mudar formação")

    op=input("Escolha: ")

    if op=="2" and len(elenco)>11:
        print("\nTitulares:")
        for i,j in enumerate(titulares,1): print(i,j)
        n=int(input("Número do titular: "))-1
        print("\nBanco:")
        for i,j in enumerate(elenco[11:],1): print(i,j)
        b=int(input("Número do reserva: "))-1
        titulares[n]=elenco[11+b]
        print("Substituição feita!")

    elif op=="3":
        formacao=input("Nova formação (ex: 4-3-3): ")
        print("Formação alterada para",formacao)

    print("\n========== 2º TEMPO ==========")
    for minuto in [60,75,90]:
        if random.random()<0.18:
            placar[random.randrange(2)]+=1
            print(f"\n⚽ GOL! {minuto}'")
        print(f"{minuto}' - {clube} {placar[0]} x {placar[1]} {adversario}")

    print("\n========== FIM ==========")
    print(f"{clube} {placar[0]} x {placar[1]} {adversario}")
    return placar
