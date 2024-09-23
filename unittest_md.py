import sys, unittest
from md import calcenergy
from asap3 import Trajectory
from ase import units
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from asap3 import EMT

atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                        symbol="Cu",
                        size=(10, 10, 10),
                        pbc=True)
atoms.calc = EMT()

class MdTests(unittest.TestCase):

    def test_calcenergy(self):
        epot, ekin, temp, etot = calcenergy(atoms) 
        self.assertEqual(etot, ekin+epot)

if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())
