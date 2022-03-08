from client import Client
import psycopg2
from menu import menu_modificar_client


class Llibreta:
    llista_clients = []

    def __init__(self, llista_clients):
        self.llista_clients = llista_clients

    def modificar_camp_client(self):
        valid = False
        option = menu_modificar_client()
        chosenId = (input("Escriu l'id del Client que vols modificar:"))
        campo =""
        if(option == 1): campo="cliente_name"
        if(option == 2): campo="cliente_cognom"
        if(option == 3): campo="cliente_telefon"
        if(option == 4): campo="cliente_correu"
        if(option == 5): campo="cliente_adreca"
        if(option == 6): campo="cliente_ciutat"

        cdata = input("Escriu la nova dada per " +campo +" del Client:")

        try:
            conn = psycopg2.connect("dbname='AABE-XYZ' user='odoo' host='172.17.0.1'password='odoo'")
            cur = conn.cursor()
            cur.execute("UPDATE cliente SET " + campo + "=%s where cliente_id=%s", (cdata, chosenId))
            conn.commit()
            print("Files modificades: {0}".format(cur.rowcount))
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def ordenar_por_nombre(self):
        try:
            conn = psycopg2.connect("dbname='AABE-XYZ' user='odoo' host='172.17.0.1'password='odoo'")
            cur = conn.cursor()
            cur.execute("select * from cliente order by cliente_name;")
            rows = cur.fetchall()
            for i in rows:
                print(i)

            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def get_llista_clients(self):
        try:
            conn = psycopg2.connect("dbname='AABE-XYZ' user='odoo' host='172.17.0.1'password='odoo'")
            cur = conn.cursor()
            cur.execute("select * from cliente;")
            rows = cur.fetchall()
            for i in rows:
                print(i)

            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def afegir_client(self, nom, cognom, telefon, correu, adreca, ciutat):
        client = Client(nom, cognom, telefon, correu, adreca, ciutat)

        print(client.__str__())
        try:
            conn = psycopg2.connect("dbname='AABE-XYZ' user='odoo' host='172.17.0.1'password='odoo'")
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO cliente(cliente_name,cliente_cognom,cliente_telefon,cliente_correu,cliente_adreca,cliente_ciutat) VALUES(" + "'" + nom + "','" + cognom + "','" + telefon + "','" + correu + "','" + adreca + "','" + ciutat + "')")

            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def eliminar_client(self, id):
        try:
            conn = psycopg2.connect("dbname='AABE-XYZ' user='odoo' host='172.17.0.1'password='odoo'")
            cur = conn.cursor()
            cur.execute(
                "delete from cliente where cliente_id=(%s)", id)
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def cercar_per_id(self, id):
        try:
            conn = psycopg2.connect("dbname='AABE-XYZ' user='odoo' host='172.17.0.1'password='odoo'")
            cur = conn.cursor()
            cur.execute("select * from cliente where cliente_id=%s", (id,))
            rows = cur.fetchone()
            print(rows)
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def cercar_per_nom(self, nom):
        try:
            conn = psycopg2.connect("dbname='AABE-XYZ' user='odoo' host='172.17.0.1'password='odoo'")
            cur = conn.cursor()
            cur.execute("select * from cliente where cliente_name=%s", (nom,))
            rows = cur.fetchall()
            for i in rows:
                print(i)

            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def cercar_per_cognom(self, cognom):
        try:
            conn = psycopg2.connect("dbname='AABE-XYZ' user='odoo' host='172.17.0.1'password='odoo'")
            cur = conn.cursor()
            cur.execute("select * from cliente where cliente_name=%s", (cognom,))
            rows = cur.fetchall()
            for i in rows:
                print(i)

            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
