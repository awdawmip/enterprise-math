import unittest
from enterprise_math.precision_count_coupling_basis import (
    birth_depth, coupling_dimension, coupling_residual, reconstruct_joint
)

class CountCouplingBasisTests(unittest.TestCase):
    def test_dimension(self):
        self.assertEqual(coupling_dimension((2,2)),1)
        self.assertEqual(coupling_dimension((2,3)),2)
        self.assertEqual(coupling_dimension((2,2,2)),4)

    def test_fractionless_reconstruction(self):
        self.assertEqual(reconstruct_joint((2,2), ((3,7),(4,6)), (4,)), (1,2,3,4))

    def test_equality_birth(self):
        self.assertEqual(coupling_residual((2,2),(1,0,0,1)),(2,))
        self.assertEqual(birth_depth(2,2,1),0)
        self.assertEqual(birth_depth(2,2,4),3)

if __name__=="__main__":
    unittest.main()
