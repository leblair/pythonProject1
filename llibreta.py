from client import Client


class Llibreta:
    llista_clients = []
    id_client = 0

    def __init__(self, llista_clients, id_client):
        self.id_client = id_client
        self.llista_clients = llista_clients


    def get_llista_clients(self):
        for i in self.llista_clients:
            print(i.__str__())

    def afegir_client(self,nom,cognom,telefon,correu,adreca,ciutat):
        client = Client(self.id_client,nom,cognom,telefon,correu,adreca,ciutat)
        self.id_client +=1
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
