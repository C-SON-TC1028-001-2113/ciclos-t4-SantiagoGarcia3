def main():
    #escribe tu codigo abajo de esta linea
    nu1 = int(input("Valor 1: "))
    nu2 = int(input("Valor 2: "))
    if nu1>0 and nu2>0 :
        if nu1!=nu2:
            if nu1>nu2:
                for i in range(nu2, nu1+1):
                    if i%2==0 :
                        print(i)
            elif nu2>nu1 :
                for i in range(nu1, nu2+1):
                    if i%2==0 :
                        print(i)
        else:
            print('No hay pares')