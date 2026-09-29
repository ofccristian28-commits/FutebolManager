JOGADORES=["Thiago Couto","Brenno","Denis","Adriano","Marcelo Ajul","Benevenuto","Patrick","Kayky","Habraao","Augusto Pucci","Felipinho","Rafinha","Claudinho","Edson Lucas","Biel","Adriel","Murilo Rhikman","Pedro Martins","Patrick de Paula","Ze Gabriel","Willian Oliveira","Diego Hernandez","Juan Alano","Carlos de Pena","Chrystian Barletta","Dudu Teodora","Pedro Perotti","Marlon Douglas","Clayson","Neto Pessoa"]
TITULARES=list(range(11))
def mostrar():
    print("\n=== ELENCO DO SPORT ===")
    for i,n in enumerate(JOGADORES,1):
        print(i,n,"-","TITULAR" if i-1 in TITULARES else "BANCO")
def trocar():
    mostrar()
    a=int(input("Sai: "))-1
    b=int(input("Entra: "))-1
    if a in TITULARES and b not in TITULARES:
        TITULARES[TITULARES.index(a)]=b
        print("Substituicao feita!")
