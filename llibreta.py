from client import Client
import psycopg2
from menu import menu_modificar_client

class Llibreta:

    try:
        conn = psycopg2.connect("dbname='Bddemo' user='odoo' host='172.17.0.1'password='odoo'")
        cur = conn.cursor()
        print("Exercici 1:")
        cur.execute("DROP TABLE IF EXISTS cliente")
        command = (
            "CREATE TABLE cliente (cliente_id VARCHAR(199), cliente_name VARCHAR(255), cliente_cognom VARCHAR(255), cliente_telefon VARCHAR(255), cliente_correu VARCHAR(255), cliente_adreca VARCHAR(255), cliente_ciutat VARCHAR(255))")
        cur.execute(command)
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    llista_clients = []
    id_client = 0

    def __init__(self, llista_clients, id_client):
        self.id_client = id_client+1
        self.llista_clients = llista_clients

    def modificar_camp_client(self):
        found = False
        option = menu_modificar_client()
        chosenId = int(input("Escriu l'id del Client que vols modificar:"))
        for i in self.llista_clients:
            if i.identificador==chosenId:
                found = True
                if option==1:
                    i.nom = input("Escriu el nou nom del Client:")
                elif option ==2:
                    i.cognom = input("Escriu el nou cognom del Client:")
                elif option==3:
                    i.telefon = input("Escriu el nou telefon del Client:")
                elif option==4:
                    i.correu = input("Escriu el nou correu del Client:")
                elif option==5:
                    i.adreca = input("Escriu la nova adreca del Client:")
                elif option ==6:
                    i.ciutat = input("Escriu la nova ciutat del Client:")

        if not found: print("Client amb id ",chosenId, " no trobat")
    def ordenar_por_nombre(self):
        # sort list by `name` in the natural order
        self.llista_clients.sort(key=lambda x: x.nom.lower())

    # def get_llista_clients(self):
    #     for i in self.llista_clients:
    #         print(i.__str__())
    #
    # """def afegir_client(cur, conn, nombre, cognom, telefon, correo, adreca,
    #                   ciutat):  # falta añadir que el id sea el ultimo encontrado
    #
    # cur.execute(
    #     "insert into libretaPython (nombre, cognom, telefon, correo,adreca,ciutat) values(" + "'" + nombre + "','" + cognom + "','" + telefon + "','" + correo + "','" + adreca + "','" + ciutat + "')")
    # conn.commit()
    # print("Cliente añadido")"""

    def afegir_client(self, nom, cognom, telefon, correu, adreca, ciutat):

        client = Client(self.id_client, nom, cognom, telefon, correu, adreca, ciutat)
        self.id_client += 1
        # self.llista_clients.append(client)
        print(client.__str__())
        # insertar cliente en la tabla de Bddemo:

        idstr = str(self.id_client)

        try:
            conn = psycopg2.connect("dbname='Bddemo' user='odoo' host='172.17.0.1'password='odoo'")
            cur = conn.cursor()

            cur.execute(
                "INSERT INTO cliente(cliente_id,cliente_name,cliente_cognom,cliente_telefon,cliente_correu,cliente_adreca,cliente_ciutat) VALUES(" + "'" + idstr + "','" + nom + "','" + cognom + "','" + telefon + "','" + correu + "','" + adreca + "','" + ciutat + "')")

            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def eliminar_client(self, id):
        found = False
        for i in self.llista_clients:
            if id == i.identificador:
                print("Eliminado:\n", i.__str__())
                self.llista_clients.remove(i)
                found = True

        if not found: print("Cliente no encontrado en la lista")

    def cercar_per_id(self, id):
        primero = []
        #primero = self.llista_clients.get()
        for i in self.llista_clients:
            if id== i.identificador:
                primero.append(i)
                return primero
        print("Cliente no encontrado con ese identificador")
        return None
    def cercar_per_nom(self, nom):
        list =[]
        for i in self.llista_clients:
            if nom == i.nom:
                list.append(i)

        return list

    def cercar_per_cognom(self, cognom):
        list = []
        for i in self.llista_clients:
            if cognom == i.cognom:
                list.append(i)

        return list
