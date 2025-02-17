import unittest

import version1 as uut

class TestUnusedSubnets(unittest.TestCase):

    def test_with_contiguous_used_subnets(self):
        supernet = '192.168.1.0/24'
        used_subnets = [
            '192.168.1.0/30',
            '192.168.1.4/30'
        ]
        expect = [
            '192.168.1.8/29',
            '192.168.1.16/28',
            '192.168.1.32/27',
            '192.168.1.64/26',
            '192.168.1.128/25'
        ]
        result = uut.find_unused(supernet, used_subnets)
        self.assertEqual(result, expect)


    def test_with_non_contiguous_used_subnets(self):
        supernet = '192.168.1.0/24'
        used_subnets = [
            '192.168.1.0/30',
            '192.168.1.8/30'
        ]
        expect = [
            '192.168.1.4/30',
            '192.168.1.12/30',
            '192.168.1.16/28',
            '192.168.1.32/27',
            '192.168.1.64/26',
            '192.168.1.128/25'
        ]
        result = uut.find_unused(supernet, used_subnets)
        self.assertEqual(result, expect)


    def test_with_no_used_subnets(self):
        supernet = '192.168.1.0/24'
        used_subnets = []
        expect = ['192.168.1.0/24']
        result = uut.find_unused(supernet, used_subnets)
        self.assertEqual(result, expect)


    def test_with_used_subnets_outside_of_supernet(self):
        supernet = '192.168.1.0/24'
        used_subnets = [
            '192.168.0.0/30',
            '192.168.0.8/30'
        ]
        expect = ['192.168.1.0/24']
        result = uut.find_unused(supernet, used_subnets)
        self.assertEqual(result, expect)




if __name__ == "__main__":
    unittest.main()