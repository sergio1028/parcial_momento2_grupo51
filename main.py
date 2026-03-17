gastos = []

def registrar_gasto():
    placa = input("Placa del vehiculo: ")
    concepto = input("Concepto: ")
    valor = float(input("Valor: "))

    gasto = {
        "placa": placa,
        "concepto": concepto,
        "valor": valor
    }

    gastos.append(gasto)

def mostrar_total():
    total = 0
    for gasto in gastos:
        total = total + gasto["valor"]
    print("Total gastado:", total)

def buscar_por_placa():
    placa = input("Ingrese placa: ")
    for gasto in gastos:
        if gasto["placa"] == placa:
            print(gasto["concepto"], gasto["valor"])

while True:

    print("\nControl de gastos")
    print("1 Registrar gasto")
    print("2 Ver total")
    print("3 Buscar por placa")
    print("4 Salir")

    opcion = input("Opcion: ")

    if opcion == "1":
        registrar_gasto()

    elif opcion == "2":
        mostrar_total()

    elif opcion == "3":
        buscar_por_placa()

    elif opcion == "4":
        break