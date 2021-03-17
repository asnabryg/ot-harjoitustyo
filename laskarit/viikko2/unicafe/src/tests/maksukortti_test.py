import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.kortti, None)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.kortti), "saldo: 10.0")
    
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.kortti.lataa_rahaa(1052)
        self.assertEqual(str(self.kortti), "saldo: 20.52")
    
    def test_saldo_vahenee_oikein_jos_rahaa_tarpeeksi(self):
        bool = self.kortti.ota_rahaa(250)
        self.assertEqual(str(self.kortti), "saldo: 7.5")
        self.assertEqual(bool, True)
    
    def test_saldo_ei_muutu_jos_rahaa_otetaan_liikaa(self):
        bool = self.kortti.ota_rahaa(2000)
        self.assertEqual(str(self.kortti), "saldo: 10.0")
        self.assertEqual(bool, False)
        
