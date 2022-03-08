
from client import Client
from llibreta import Llibreta
import psycopg2
import menu

try:
    conn = psycopg2.connect("dbname='AABE-XYZ' user='odoo' host='172.17.0.1'password='odoo'")
    cur = conn.cursor()
    print("Exercici 1:")
    cur.execute("DROP TABLE IF EXISTS cliente")
    command = (
        "CREATE TABLE cliente (cliente_id SERIAL, cliente_name VARCHAR(255), cliente_cognom VARCHAR(255), cliente_telefon VARCHAR(255), cliente_correu VARCHAR(255), cliente_adreca VARCHAR(255), cliente_ciutat VARCHAR(255))")
    cur.execute(command)
    conn.commit()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()

llista_clientsA = []
libreta = Llibreta(llista_clientsA)

option2 = None
exit = False
exitConsult = None
while not exit:
    exit = False
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
        idBuscar  = (input("Entra el identificador de client:"))
        libreta.eliminar_client(idBuscar)
    if option==3:
        exitConsult = False
        while not exitConsult:
            option2 = menu.mostrar_menu_consulta()
            if option2==1:
                idBuscar = str(input("Entra el identificador de client:"))
                libreta.cercar_per_id(idBuscar)

            if option2 ==2:
                nomBuscar = input("Entra el nom del client:")
                libreta.cercar_per_nom(nomBuscar)

            if option2 == 3:
                cognomBuscar = input("Entra el cognom del client:")
                libreta.cercar_per_cognom(cognomBuscar)

            if option2 ==4:
                libreta.get_llista_clients()
            if option2 ==5:
                libreta.ordenar_por_nombre()
            if option2 ==6:
                exitConsult =True
    if option ==4:
        libreta.modificar_camp_client()
    if option ==5:
        exit = True

