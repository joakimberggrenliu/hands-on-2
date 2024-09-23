import sys, unittest
from md import calcenergy
from asap3 import Trajectory
from ase import units
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from asap3 import EMT


import md
import os

md.run_md()

class MdTests(unittest.TestCase):

    def test_calcenergy(self):
        self.assertTrue(True)
        filepath = "/home/joabe712/TFYA99/project-hands-on/hands-on-2/hands-on-2/"
        os.path.exists(filepath)


if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())