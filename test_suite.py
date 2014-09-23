import unittest

testmodules = [
    'test_gate',
    'test_register',
    'test_quantum_circuit'
]

suite = unittest.TestSuite()

for t in testmodules:
    suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

unittest.TextTestRunner().run(suite)
