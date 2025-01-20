import unittest
from runner import Runner
import runner_and_tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(bool(is_frozen), "Тесты в этом кейсе заморожены")
    def test_walk(self):
        rw = Runner("r_walk")
        for i in range(10):
            rw.walk()
        self.assertEqual(rw.distance, 50)

    @unittest.skipIf(bool(is_frozen), "Тесты в этом кейсе заморожены")
    def test_run(self):
        rr = Runner("r_run")
        for i in range(10):
            rr.run()
        self.assertEqual(rr.distance, 100)

    @unittest.skipIf(bool(is_frozen), "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        rw2 = Runner("r_walk_2")
        rr2 = Runner("r_run_2")
        for i in range(10):
            rw2.walk()
            rr2.run()
        self.assertNotEqual(rw2.distance, rr2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

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

    @unittest.skipIf(bool(is_frozen), "Тесты в этом кейсе заморожены")
    def test_1(self):
        t1 = runner_and_tournament.Tournament(90, r1, r3)
        global all_results
        all_results = t1.start()
        self.tearDownClass()
        self.assertTrue(all_results.get(2) == "Ник" )

    @unittest.skipIf(bool(is_frozen), "Тесты в этом кейсе заморожены")
    def test_2(self):
        t2 = runner_and_tournament.Tournament(90, r2, r3)
        global all_results
        all_results = t2.start()
        self.tearDownClass()
        self.assertTrue(all_results.get(2) == "Ник")

    @unittest.skipIf(bool(is_frozen), "Тесты в этом кейсе заморожены")
    def test_3(self):
        t3 = runner_and_tournament.Tournament(90, r1, r2, r3)
        global all_results
        all_results = t3.start()
        self.assertTrue(all_results.get(3) == "Ник")

    @classmethod
    def tearDownClass(self):
        print(all_results)

if __name__ == "__mane__":
    unittest.main()