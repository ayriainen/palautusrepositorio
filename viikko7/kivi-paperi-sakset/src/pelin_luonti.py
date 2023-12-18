from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

def luoPeli(tyyppi):
    if tyyppi == 'a':
        return KPSPelaajaVsPelaaja()
    elif tyyppi == 'b':
        return KPSTekoaly()
    elif tyyppi == 'c':
        return KPSParempiTekoaly()
    else:
        return None
