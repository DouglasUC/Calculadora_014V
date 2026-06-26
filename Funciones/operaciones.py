memoria = []
total = 0


def suma(n):

    for i in range(n):
        nro = int(input("Ingrese número", i + 1))
        total += nro
    return total


def resta(n):
    return


while True:
    print("--- MENÚ CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("5. Salir")

    op = input("Digite la opción del menú")

    match op:
        case "1":
            res = suma(int(input("Ingrese cantidad de números a sumar: ")))
            memoria.append(res)
        case "2":
            print()
        case "5":
            print("Usted ha salido del sistema")
            break
        case _:
            print("Opción no valida")
