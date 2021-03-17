
import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti_rahaa = Maksukortti(1000)
        self.kortti_ei_rahaa = Maksukortti(0)
    
    def test_kassa_olemassa(self):
        self.assertNotEqual(self.kassa, None)
    
    def test_kassassa_oikea_summa_rahaa_ja_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_syo_edullisesti_kateisella_toimii_kun_kateista_tarpeeksi(self):
        palautus = self.kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(palautus, 260)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_syo_edullisesti_kateisella_toimii_kun_kateista_ei_tarpeeksi(self):
        palautus = self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(palautus, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_syo_maukkaasti_kateisella_toimii_kun_kateista_tarpeeksi(self):
        palautus = self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(palautus, 100)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_syo_maukkaasti_kateisella_toimii_kun_kateista_ei_tarpeeksi(self):
        palautus = self.kassa.syo_maukkaasti_kateisella(100)
        self.assertEqual(palautus, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_syo_edullisesti_kortilla_kun_rahaa_tarpeeksi(self):
        palautus = self.kassa.syo_edullisesti_kortilla(self.kortti_rahaa)
        self.assertEqual(palautus, True)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_syo_edullisesti_kortilla_kun_rahaa_ei_tarpeeksi(self):
        palautus = self.kassa.syo_edullisesti_kortilla(self.kortti_ei_rahaa)
        self.assertEqual(palautus, False)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_syo_maukkaasti_kortilla_kun_rahaa_tarpeeksi(self):
        palautus = self.kassa.syo_maukkaasti_kortilla(self.kortti_rahaa)
        self.assertEqual(palautus, True)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_syo_maukkaasti_kortilla_kun_rahaa_ei_tarpeeksi(self):
        palautus = self.kassa.syo_maukkaasti_kortilla(self.kortti_ei_rahaa)
        self.assertEqual(palautus, False)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_lataa_rahaa_kortille_toimii_oikein(self):
        self.kassa.lataa_rahaa_kortille(self.kortti_ei_rahaa, -500)
        self.assertEqual(str(self.kortti_ei_rahaa), "saldo: 0.0")
        self.kassa.lataa_rahaa_kortille(self.kortti_ei_rahaa, 500)
        self.assertEqual(str(self.kortti_ei_rahaa), "saldo: 5.0")