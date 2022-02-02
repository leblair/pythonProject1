from llibreta import Llibreta
import menu

option = menu.mostrar_menu_principal()
llista_clients = []
id_client =0
libreta = Llibreta(llista_clients,0)

option2 = None
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
    option2 = menu.mostrar_menu_consulta()
