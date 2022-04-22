
from animal import *

class Oiseaux:

    def __init__(self, p_poid = 0, p_couleur_plumage = ""):
        Animal.__init__(self, p_poid)

        self.couleur_plumage = p_couleur_plumage

    def __str__(self):
        return f"""Le poid du oiseaux est de {self.poid}
La couleur plumage du oieseau est {self.couleur_plumage}"""