import json
import os
import random

SAVE = "save.json"

CLUBES = {
    "Flamengo": ["A","RJ",88],
    "Palmeiras": ["A","SP",88],
    "Corinthians": ["A","SP",79],
    "São Paulo": ["A","SP",82],
    "Santos": ["A","SP",78],
    "Fluminense": ["A","RJ",83],
    "Vasco": ["A","RJ",78],
    "Botafogo": ["A","RJ",81],
    "Atlético-MG": ["A","MG",84],
    "Cruzeiro": ["A","MG",81],
    "Grêmio": ["A","RS",80],
    "Internacional": ["A","RS",81],
    "Bahia": ["A","BA",78],
    "Vitória": ["A","BA",73],
    "Athletico-PR": ["A","PR",79],
    "Coritiba": ["A","PR",75],
    "Bragantino": ["A","SP",76],
    "Mirassol": ["A","SP",73],
    "Chapecoense": ["A","SC",71],
    "Remo": ["A","PA",70],

    "Sport": ["B","PE",76],
    "Ceará": ["B","CE",76],
    "Fortaleza": ["B","CE",78],
    "Juventude": ["B","RS",75],
    "Goiás": ["B","GO",74],
    "Vila Nova": ["B","GO",72],
    "Criciúma": ["B","SC",74],
    "Avaí": ["B","SC",72],
    "Cuiabá": ["B","MT",75],
    "América-MG": ["B","MG",75],
    "CRB": ["B","AL",70],
    "Atlético-GO": ["B","GO",73],
    "Operário-PR": ["B","PR",70],
    "Novorizontino": ["B","SP",71],
    "Ponte Preta": ["B","SP",70],
    "Botafogo-SP": ["B","SP",68],
    "Londrina": ["B","PR",67],
    "São Bernardo": ["B","SP",68],
    "Náutico": ["B","PE",69],
    "Athletic": ["B","MG",67],

    "Botafogo-PB": ["C","PB",66],
    "Brusque": ["C","SC",66],
    "Ferroviária": ["C","SP",65],
    "Maringá": ["C","PR",64],
    "Floresta": ["C","CE",61],
    "Inter de Limeira": ["C","SP",63],
    "Paysandu": ["C","PA",68],
    "Amazonas": ["C","AM",64],
    "Figueirense": ["C","SC",65],
    "Guarani": ["C","SP",66],
    "Caxias": ["C","RS",64],
    "Volta Redonda": ["C","RJ",64],
    "Ypiranga-RS": ["C","RS",63],
    "Ituano": ["C","SP",63],
    "Anápolis": ["C","GO",61],
    "Maranhão": ["C","MA",60],
    "Itabaiana": ["C","SE",59],
    "Confiança": ["C","SE",60],
    "Barra-SC": ["C","SC",59],
    "Santa Cruz": ["C","PE",67],

    "Retrô": ["D","PE",60],
    "Central": ["D","PE",58],
    "Sousa": ["D","PB",59],
    "Treze": ["D","PB",57],
    "ASA": ["D","AL",57],
    "Sergipe": ["D","SE",56],
    "Juazeirense": ["D","BA",58],
    "Itabuna": ["D","BA",55],
    "Porto-PE": ["D","PE",54],
    "Maguary": ["D","PE",53],
    "Altos": ["D","PI",57],
    "River-PI": ["D","PI",54],
    "Potiguar": ["D","RN",55],
    "América-RN": ["D","RN",60],
    "São Raimundo-RR": ["D","RR",52]
}

def salvar(jogo):
    with open(SAVE, "w", encoding="utf-8") as f:
        json.dump(jogo, f, ensure_ascii=False, indent=2)

def carregar():
    if not os.path.exists(SAVE):
        return None
    try:
        with open(SAVE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return None

def divisao(d):
    return [nome for nome, dados in CLUBES.items() if dados[0] == d]

def partida(a, b):
    fa = CLUBES[a][2]
    fb = CLUBES[b][2]

    ga = 0
    gb = 0

    for _ in range(5):
        if random.randint(1, 100) <= max(8, fa - 55):
            ga += 1
        if random.randint(1, 100) <= max(8, fb - 55):
            gb += 1

    return ga, gb

def criar_tabela(times):
    return {
        t: {
            "p": 0,
            "j": 0,
            "v": 0,
            "e": 0,
            "d": 0,
            "gp": 0,
            "gc": 0,
            "sg": 0
        }
        for t in times
    }

def registrar(tab, casa, fora, gcasa, gfora):
    tab[casa]["j"] += 1
    tab[fora]["j"] += 1

    tab[casa]["gp"] += gcasa
    tab[casa]["gc"] += gfora

    tab[fora]["gp"] += gfora
    tab[fora]["gc"] += gcasa

    if gcasa > gfora:
        tab[casa]["p"] += 3
        tab[casa]["v"] += 1
        tab[fora]["d"] += 1
    elif gfora > gcasa:
        tab[fora]["p"] += 3
        tab[fora]["v"] += 1
        tab[casa]["d"] += 1
    else:
        tab[casa]["p"] += 1
        tab[fora]["p"] += 1
        tab[casa]["e"] += 1
        tab[fora]["e"] += 1

    tab[casa]["sg"] = tab[casa]["gp"] - tab[casa]["gc"]
    tab[fora]["sg"] = tab[fora]["gp"] - tab[fora]["gc"]

def ordenar(tab):
    return sorted(
        tab.items(),
        key=lambda x: (
            -x[1]["p"],
            -x[1]["v"],
            -x[1]["sg"],
            -x[1]["gp"]
        )
    )

def mostrar_tabela(tab, titulo):
    print("\n" + "=" * 65)
    print(titulo)
    print("=" * 65)

    print(
        f"{'#':>2} {'CLUBE':<23} "
        f"{'P':>3} {'J':>3} {'V':>3} "
        f"{'E':>3} {'D':>3} {'SG':>4}"
    )

    print("-" * 65)

    for pos, (nome, dados) in enumerate(ordenar(tab), 1):
        print(
            f"{pos:>2} {nome:<23} "
            f"{dados['p']:>3} "
            f"{dados['j']:>3} "
            f"{dados['v']:>3} "
            f"{dados['e']:>3} "
            f"{dados['d']:>3} "
            f"{dados['sg']:>4}"
        )

def campeonato(jogo, serie):
    import partida as motor
    import elencos
    times = divisao(serie)

    if len(times) < 2:
        print("Não há clubes suficientes.")
        return

    tab = criar_tabela(times)

    print("\n" + "=" * 60)
    print("CAMPEONATO BRASILEIRO - SÉRIE", serie)
    print("=" * 60)

    # V1: 19 rodadas de ida + 19 de volta.
    for rodada in range(1, 39):
        lista = times[:]
        random.shuffle(lista)

        print(f"\nRODADA {rodada}/38")

        for i in range(0, len(lista) - 1, 2):
            a = lista[i]
            b = lista[i + 1]

            if a == jogo["clube"] or b == jogo["clube"]:
                meu = jogo["clube"]
                adv = b if a == meu else a
                elenco = elencos.ELENCOS.get(meu, [])
                placar = motor.jogar_partida(meu, adv, elenco)
                ga, gb = (placar[0], placar[1]) if a == meu else (placar[1], placar[0])
            else:
                ga, gb = partida(a, b)
            registrar(tab, a, b, ga, gb)

            if a == jogo["clube"] or b == jogo["clube"]:
                print(f"{a} {ga} x {gb} {b}")

        input("ENTER para ir para a próxima rodada...")
        input("ENTER para ir para a próxima rodada...")
    mostrar_tabela(tab, "CLASSIFICAÇÃO FINAL - SÉRIE " + serie)

    jogo["tabelas"][serie] = tab
    salvar(jogo)

def escolher_clube():
    nomes = list(CLUBES.keys())

    print("\n" + "=" * 60)
    print("BRASIL FUTEBOL MANAGER")
    print("=" * 60)
    print("\nESCOLHA SEU CLUBE:\n")

    for i, nome in enumerate(nomes, 1):
        print(
            f"{i:>3} - {nome:<23} "
            f"Série {CLUBES[nome][0]} - {CLUBES[nome][1]}"
        )

    while True:
        try:
            numero = int(input("\nNúmero do clube: "))

            if 1 <= numero <= len(nomes):
                return nomes[numero - 1]
        except:
            pass

        print("Número inválido.")

def menu(jogo):
    while True:
        print("\n" + "=" * 60)
        print("          BRASIL FUTEBOL MANAGER")
        print("=" * 60)
        print("Temporada:", jogo["ano"])
        print("Clube:", jogo["clube"])
        print("Série:", CLUBES[jogo["clube"]][0])
        print("=" * 60)

        print("1 - Jogar Série A")
        print("2 - Jogar Série B")
        print("3 - Jogar Série C")
        print("4 - Jogar Série D")
        print("5 - Ver tabela")
        print("6 - Salvar")
        print("7 - Ver elenco")
        print("8 - Substituir jogador")
        print("0 - Sair")

        op = input("\nEscolha: ").strip()

        if op == "7":
            import elenco
            elenco.mostrar()
        elif op == "8":
            import elenco
            elenco.trocar()
        elif op == "9":
            print("Formação: 4-4-2")
        if op == "1":
            campeonato(jogo, "A")
        elif op == "2":
            campeonato(jogo, "B")
        elif op == "3":
            campeonato(jogo, "C")
        elif op == "4":
            campeonato(jogo, "D")
        elif op == "5":
            for serie, tab in jogo["tabelas"].items():
                if tab:
                    mostrar_tabela(tab, "SÉRIE " + serie)
        elif op == "6":
            salvar(jogo)
            print("Save salvo.")
        elif op == "0":
            salvar(jogo)
            print("Save salvo.")
            break
        else:
            print("Opção inválida.")

def iniciar():
    jogo = carregar()

    if jogo:
        print("\nSAVE ENCONTRADO")
        print("Clube:", jogo["clube"])
        print("Temporada:", jogo["ano"])

        resposta = input("Continuar? [S/n]: ").strip().lower()

        if resposta not in ("", "s"):
            jogo = None

    if not jogo:
        clube = escolher_clube()

        jogo = {
            "ano": 2026,
            "clube": clube,
            "tabelas": {
                "A": None,
                "B": None,
                "C": None,
                "D": None
            }
        }

        salvar(jogo)

        print("\nVocê escolheu:", clube)

    menu(jogo)

if __name__ == "__main__":
    iniciar()

from serie_d_2026 import SERIE_D_2026
