from tekoaly_parannettu import TekoalyParannettu
from kps import KPS

class KPSParempiTekoaly(KPS):
    def _toisen_siirto(self, ensimmaisen_siirto):
        tekoaly = TekoalyParannettu(10)
        tokan_siirto = tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto