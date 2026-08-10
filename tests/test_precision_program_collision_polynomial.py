import unittest
from enterprise_math.precision_program_collision_polynomial import (
    collision_birth_components, collision_hierarchy, collision_increment,
    endpoint_increment, multiplicity_histogram_from_collisions,
)

class ProgramCollisionPolynomialTests(unittest.TestCase):
    def test_binomial_inversion(self):
        multiplicities=(0,1,1,3)
        W=collision_hierarchy(multiplicities)
        self.assertEqual(W,(4,5,3,1))
        self.assertEqual(multiplicity_histogram_from_collisions(W),(1,2,0,1))

    def test_vandermonde_birth(self):
        prev=(0,1,3)
        shell=(2,2,1)
        self.assertEqual(collision_birth_components(prev,shell,2),(5,2))
        self.assertEqual(collision_increment(prev,shell,2),7)
        self.assertEqual(endpoint_increment(prev,shell,2),7)

    def test_same_endpoints_different_birth_mechanism(self):
        prev=(0,1,3)
        shell_a=(2,2,1)
        shell_b=(3,1,1)
        self.assertEqual(sorted(a+b for a,b in zip(prev,shell_a)), [2,3,4])
        self.assertEqual(sorted(a+b for a,b in zip(prev,shell_b)), [2,3,4])
        self.assertEqual(collision_birth_components(prev,shell_a,2),(5,2))
        self.assertEqual(collision_birth_components(prev,shell_b,2),(4,3))

if __name__=="__main__":
    unittest.main()
