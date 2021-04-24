from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class Pelitehdas:
    def pelaaja_vs_pelaaja(self):
        return KPSPelaajaVsPelaaja()

    def pelaaja_vs_tekoaly(self):
        return KPSTekoaly()
    
    def pelaaja_vs_parempi_tekoaly(self):
        return KPSParempiTekoaly()