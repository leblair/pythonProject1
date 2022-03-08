class Client:
    nom = ""
    cognom = ""
    telefon = ""
    correu = ""
    adreca = ""
    ciutat = ""

    def __init__(self, nom, cognom, telefon, correu, adreca, ciutat):
        self.ciutat = ciutat
        self.adreca = adreca
        self.correu = correu
        self.telefon = telefon
        self.cognom = cognom
        self.nom = nom

    def nom(self):
        return self.nom

    def __str__(self):
        return "Nom: ", self.nom,"Telefon: ",self.telefon,"Correu: ", self.correu,"Adreca: ",self.adreca,"Ciutat: ",self.ciutat


