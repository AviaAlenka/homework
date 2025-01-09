import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        rw = Runner("r_walk")
        for i in range(10):
            rw.walk()
            # print(rw.distance) # Для проверки
        self.assertEqual(rw.distance, 50)
        # При изменении 50 на другое значение тест проваливается

    def test_run(self):
        rr = Runner("r_run")
        for i in range(10):
            rr.run()
            # print(rr.distance) # Для проверки
        self.assertEqual(rr.distance, 100)
        # При изменении 100 на другое значение тест проваливается

    def test_challenge(self):
        rw2 = Runner("r_walk_2")
        rr2 = Runner("r_run_2")
        for i in range(10):
            rw2.walk()
            rr2.run()
        self.assertNotEqual(rw2.distance, rr2.distance)
        # При изменении assertNotEqual на assertEqual тест проваливается

if __name__ == "__mane__":
    unittest.main()