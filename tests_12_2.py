import unittest
from pprint import pprint
import runner_and_tournament

class TournamentTest(unittest.TestCase):
    def setUpClass(self):
        global all_results
        all_results = {}
        return all_results

    def setUp(self):
        global r1
        global r2
        global r3
        r1 = runner_and_tournament.Runner("Усэйн", 10)
        r2 = runner_and_tournament.Runner("Андрей", 9)
        r3 = runner_and_tournament.Runner("Ник", 3)
        return r1, r2, r3

    def tearDownClass(self):
        pprint(all_results)
        pass

    def test_1(self):
        t1 = runner_and_tournament.Tournament(90, r1, r3)
        t1.start()
        all_results = runner_and_tournament.Tournament.start
        self.assertTrue(max(all_results, key=all_results.get), "Ник")

    def test_2(self):
        t2 = runner_and_tournament.Tournament(90, r2, r3)
        t2.start()
        self.assertTrue(max(all_results, key=all_results.get), "Ник")

    def test_3(self):
        t3 = runner_and_tournament.Tournament(90, r1, r2, r3)
        t3.start()
        self.assertTrue(max(all_results, key=all_results.get), "Ник")



if __name__ == "__mane__":
    unittest.main()
