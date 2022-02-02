from client import Client
from llibreta import Llibreta
import menu

llista_clientsA = []
cliente0 = Client()
llista_clientsA.append(cliente0)
id_client =0
libreta = Llibreta(llista_clientsA,0)

option2 = None
exit = False
exitConsult = None
while not exit:
    option = menu.mostrar_menu_principal()
    if option ==1:
        nom = input("Entra el nom:")
        cognom = input("Entra el cognom:")
        telefon = input("Entra el telefon:")
        correu = input("Entra el correu:")
        adreca = input("Entra la adreca:")
        ciutat  = input("Entra la ciutat:")
        libreta.afegir_client(nom,cognom,telefon,correu,adreca,ciutat)

    if option ==2: #implementar un bucle para pedir otras opciones
        idBuscar  = int(input("Entra el identificador de client:"))
        libreta.eliminar_client(idBuscar)
    if option==3:
        while not exitConsult:
            exitConsult =False
            option2 = menu.mostrar_menu_consulta()
            if option2==1:
                idBuscar = int(input("Entra el identificador de client:"))
                listaReturnCliente = (libreta.cercar_per_id(idBuscar))
                for i in listaReturnCliente:
                    print(i.__str__())
            if option2 ==2:
                nomBuscar = input("Entra el nom del client:")
                listaReturnCliente = libreta.cercar_per_nom(nomBuscar)
                for i in listaReturnCliente:
                    print(i.__str__())
            if option2 == 3:
                cognomBuscar = input("Entra el cognom del client:")
                listaReturnCliente = libreta.cercar_per_cognom(cognomBuscar)
                for i in listaReturnCliente:
                    print(i.__str__())
            if option2 ==4:
                libreta.get_llista_clients()
            if option2 ==5:
                libreta.llista_clients.sort(key=lambda x: x.nom)
                libreta.get_llista_clients()
            if option2 ==6:
                exitConsult =True
    if option ==5:
        exit = True

