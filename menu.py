def mostrar_menu_principal():
    print("MENU PRINCIPAL")
    print("================================")
    print("Seleccioni una opcio i premi Intro")
    print("================================")
    print("1. Afegir client\n2. Eliminar client\n3. Consultar client\n4. Modificar un camp d'un client (*)\n5. Sortir")
    number = False
    option = None
    while not number:
        option = input("Enter an option:")
        if option.isdigit() :
            option = int(option)
            number =True
        else:
            print("No es una opcio valida")
    return option
def mostrar_menu_consulta():
    print("MENU CONSULTA")
    print("================================")
    print("Seleccioni una opcio i premi Intro")
    print("================================")
    print("1. Cercar client per Identificador\n2. Cercar client per Nom\n3. Cercar client per Cognom\n4. Llistar tots els clients\n5. Llistar tots els clients per Nom (*)\n6. Enrere")
    option = None
    number = False

    while not number:
        option = input("Enter an option:")
        if option.isdigit() :
            option = int(option)
            number =True
        else:
            print("No es una opcio valida")
    return option

