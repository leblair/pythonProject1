from client import Client
from menu import menu_modificar_client

class Llibreta:
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

    def get_llista_clients(self):
        for i in self.llista_clients:
            print(i.__str__())

    def afegir_client(self,nom,cognom,telefon,correu,adreca,ciutat):
        client = Client(self.id_client,nom,cognom,telefon,correu,adreca,ciutat)
        self.id_client+=1
        self.llista_clients.append(client)
        print(client.__str__())

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
