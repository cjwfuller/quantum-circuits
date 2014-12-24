import unittest

testmodules = [
    'tests.test_quantum_gate',
    'tests.test_register',
    'tests.test_quantum_circuit'
]

suite = unittest.TestSuite()

for t in testmodules:
    suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

unittest.TextTestRunner().run(suite)
