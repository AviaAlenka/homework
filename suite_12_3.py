import unittest
import tests_12_3

modST = unittest.TestSuite()
modST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
modST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(modST)