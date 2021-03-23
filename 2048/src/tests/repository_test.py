
import unittest
from score_repository import ScoreRepository
from initialize_database import initialize_fake_database
from database_connection import get_fake_database_connection

class TestRepository(unittest.TestCase):

    def setUp(self):
        initialize_fake_database()
        self.rep = ScoreRepository(get_fake_database_connection())
        self.test_rep = ScoreRepository()
    
    def test_add_new_highscores_and_get_top5(self):
        self.rep.add_new_highscore("pelaaja1", 100)
        self.rep.add_new_highscore("pelaaja2", 150)
        self.rep.add_new_highscore("pelaaja3", 0)
        self.rep.add_new_highscore("pelaaja4", 15)
        self.rep.add_new_highscore("pelaaja5", 240)
        top5 = self.rep.get_top5()
        self.assertEqual(top5, [("pelaaja5", 240), ("pelaaja2", 150),
                         ("pelaaja1", 100), ("pelaaja4", 15), ("pelaaja3", 0)])
        self.rep.add_new_highscore("pelaaja6", 200)
        top5 = self.rep.get_top5()
        self.assertEqual(top5, [("pelaaja5", 240), ("pelaaja6", 200),
                         ("pelaaja2", 150), ("pelaaja1", 100), ("pelaaja4", 15)])
    
    def test_check_if_highscore(self):
        self.rep.add_new_highscore("pelaaja1", 100)
        self.rep.add_new_highscore("pelaaja2", 150)
        self.rep.add_new_highscore("pelaaja3", 0)
        self.rep.add_new_highscore("pelaaja4", 15)
        bool = self.rep.check_if_highscore(2)
        self.assertEqual(bool, True)
        self.rep.add_new_highscore("pelaaja5", 240)
        bool = self.rep.check_if_highscore(20)
        self.assertEqual(bool, True)
        self.rep.add_new_highscore("pelaaja5", 250)
        bool = self.rep.check_if_highscore(2)
        self.assertEqual(bool, False)
