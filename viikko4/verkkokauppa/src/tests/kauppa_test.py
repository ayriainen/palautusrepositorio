import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):

    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            
            if tuote_id == 2:
                return 10
            
            if tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            
            if tuote_id == 2:
                return Tuote(2, "leipä", 4)
            
            if tuote_id == 3:
                return Tuote(2, "peruna", 3)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_tietylla(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_kahden_eri_tuotteen_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_tietylla(self):
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 9)

    def test_saman_tuotteen_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_tietylla(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)

    def test_olevan_ja_loppuneen_tuotteen_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_tietylla(self):
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_ostoskorin_nollautumin_metodilla_aloita_asiointi(self):
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_tapahtumalle(self):

        pankki_mock_b = Mock()
        viitegeneraattori_mock_b = Mock()

        viitegeneraattori_mock_b = Mock(wraps=Viitegeneraattori())

        varasto_mock_b = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            
            if tuote_id == 2:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            
            if tuote_id == 2:
                return Tuote(2, "leipä", 4)

        varasto_mock_b.saldo.side_effect = varasto_saldo
        varasto_mock_b.hae_tuote.side_effect = varasto_hae_tuote

        kauppa_b = Kauppa(varasto_mock_b, pankki_mock_b, viitegeneraattori_mock_b)

        kauppa_b.aloita_asiointi()
        kauppa_b.lisaa_koriin(1)
        kauppa_b.lisaa_koriin(2)
        kauppa_b.tilimaksu("pekka", "12345")
        self.assertEqual(viitegeneraattori_mock_b.uusi.call_count, 1)
        kauppa_b.aloita_asiointi()
        kauppa_b.lisaa_koriin(1)
        kauppa_b.tilimaksu("pekka", "12345")
        self.assertEqual(viitegeneraattori_mock_b.uusi.call_count, 2)

    def test_perakkaisten_viitenumerojen_arvot(self):

        pankki_mock_b = Mock()
        viitegeneraattori_mock_b = Mock()

        viitegeneraattori_mock_b.uusi.side_effect = [1, 2, 3]

        varasto_mock_b = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            
            if tuote_id == 2:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            
            if tuote_id == 2:
                return Tuote(2, "leipä", 4)

        varasto_mock_b.saldo.side_effect = varasto_saldo
        varasto_mock_b.hae_tuote.side_effect = varasto_hae_tuote

        kauppa_b = Kauppa(varasto_mock_b, pankki_mock_b, viitegeneraattori_mock_b)

        kauppa_b.aloita_asiointi()
        kauppa_b.lisaa_koriin(1)
        kauppa_b.lisaa_koriin(2)
        kauppa_b.tilimaksu("pekka", "12345")
        pankki_mock_b.tilisiirto.assert_called_with("pekka", 1, "12345", "33333-44455", 9)
        kauppa_b.aloita_asiointi()
        kauppa_b.lisaa_koriin(1)
        kauppa_b.tilimaksu("pekka", "12345")
        pankki_mock_b.tilisiirto.assert_called_with("pekka", 2, "12345", "33333-44455", 5)
        kauppa_b.aloita_asiointi()
        kauppa_b.lisaa_koriin(2)
        kauppa_b.tilimaksu("pekka", "12345")
        pankki_mock_b.tilisiirto.assert_called_with("pekka", 3, "12345", "33333-44455", 4)

    def test_ostoskorista_poisto(self):
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)
