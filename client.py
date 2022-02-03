class Client:
    identificador = ""
    nom = ""
    cognom = ""
    telefon = ""
    correu = ""
    adreca = ""
    ciutat = ""

    def __init__(self, identificador, nom, cognom, telefon, correu, adreca, ciutat):
        self.ciutat = ciutat
        self.adreca = adreca
        self.correu = correu
        self.telefon = telefon
        self.cognom = cognom
        self.nom = nom
        self.identificador = identificador

    def nom(self):
        return self.nom

    def __str__(self):
        return "Cliente_id: ", self.identificador, "Nom: ", self.nom,"Telefon: ",self.telefon,"Correu: ", self.correu,"Adreca: ",self.adreca,"Ciutat: ",self.ciutat


