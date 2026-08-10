import unittest
from enterprise_math.precision_binary_isa_pareto import (
    max_readout_depth, readout_depth, storage_count,
    streaming_update_incidences, total_semantic_readout_length
)

class BinaryISAParetoTests(unittest.TestCase):
    def test_endpoints(self):
        self.assertEqual(storage_count(3,1),3)
        self.assertEqual(storage_count(3,3),7)
        self.assertEqual(max_readout_depth(7,3),3)

    def test_exact_chunk_depth(self):
        self.assertEqual(readout_depth(7,3),3)
        self.assertEqual(readout_depth(6,3),2)
        self.assertEqual(readout_depth(0,3),0)

    def test_update_formula(self):
        self.assertEqual(streaming_update_incidences(3,2),9)
        self.assertGreater(total_semantic_readout_length(4,1), total_semantic_readout_length(4,2))

if __name__=="__main__":
    unittest.main()
