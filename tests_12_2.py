# Для вывода имён спортсменов в словарях с результатами пришлось внести поправку
# в файл runner_and_tournament.py (в 35-й строке вместо "finishers[place] = participant"
# записать "finishers[place] = str(participant)")
# Дополнительное задание не делала :-(
import unittest
import runner_and_tournament

class TournamentTest(unittest.TestCase):

    def setUp(self):
        global r1
        global r2
        global r3
        r1 = runner_and_tournament.Runner("Усэйн", 10)
        r2 = runner_and_tournament.Runner("Андрей", 9)
        r3 = runner_and_tournament.Runner("Ник", 3)
        return r1, r2, r3

    @classmethod
    def setUpClass(self):
        global all_results
        all_results = {}
        return all_results

    def test_1(self):
        t1 = runner_and_tournament.Tournament(90, r1, r3)
        global all_results
        all_results = t1.start()
        # print(f"Тест 1: {all_results}")
        self.tearDownClass()
        self.assertTrue(all_results.get(2) == "Ник" )

    def test_2(self):
        t2 = runner_and_tournament.Tournament(90, r2, r3)
        global all_results
        all_results = t2.start()
        # print(f"Тест 2: {all_results}")
        self.tearDownClass()
        self.assertTrue(all_results.get(2) == "Ник")

    def test_3(self):
        t3 = runner_and_tournament.Tournament(90, r1, r2, r3)
        global all_results
        all_results = t3.start()
        # print(f"Тест 3: {all_results}")
        self.assertTrue(all_results.get(3) == "Ник")

    @classmethod
    def tearDownClass(self):
        print(all_results)

if __name__ == "__mane__":
    unittest.main()
