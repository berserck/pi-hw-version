import unittest
import pi_hw_version 

class TestGetHwVersion(unittest.TestCase):
    def setUp(self):
        self.cpuinfo=['Hardware\t: BCM2709\n', 'Revision\t: a02082\n', 'Serial\t\t: 0000000000000000\n']
        self.revision='900092'

    def test_get_hw_version(self):
        """The get HW version should get the Revision from cpuinfo"""
        self.assertEqual(pi_hw_version.get_hw_version(self.cpuinfo), 'a02082')

    def test_get_pi_version(self):
        """Get the raspberry version from a hardware version"""
        self.assertEqual(pi_hw_version.print_pi_hw_version(self.revision), 'PiZero')

if __name__ == "__main__":
    unittest.main()
