import sys
for linea in sys.stdin:
    if linea == "\n":
        break
    lista =list(map(int,linea.split()))
    print(max(lista[1:]))
