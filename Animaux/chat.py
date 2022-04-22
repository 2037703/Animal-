
from animal import *

class Chat:

    def __init__(self, p_poid=0, p_couleur_poil = ""):
        Animal.__init__(self, p_poid)

        self.couleur_poil = p_couleur_poil

    def __str__(self):
        return f"""La couleur du poil du chat est {self.couleur_poil} 
Le poid du chat est de {self.poid}"""

