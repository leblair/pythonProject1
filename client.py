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

    def __str__(self):
        return "Cliente ", self.identificador
