
flag = True
notas_guardadas = []

def prom():
    suma = sum(notas_guardadas)
    prom = suma/len(notas_guardadas)
    print(prom)


while flag == True:
    nota = int(input("ingrese su nota: "))
    if nota >= 0 and nota <= 100:
        print("nota guardada")
        notas_guardadas.append(nota)
    elif nota == -1 and len(notas_guardadas) != 0:
        print(notas_guardadas)
        prom()
        flag = False
    else:
        print("fuera de rango")
#hello
    
    
    








