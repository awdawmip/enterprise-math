import unittest
from enterprise_math.precision_null_program_collisions import (
    code_from_basis, code_weight_enumerator, pair_collision_from_weights,
    program_collision, triple_collision_from_triangle_profile,
    unique_short_programs,
)

class NullProgramCollisionTests(unittest.TestCase):
    def test_perfect_depth2_unique(self):
        code=code_from_basis((31,))
        self.assertTrue(unique_short_programs(code,2))
        self.assertEqual(program_collision(code,5,2,2),0)

    def test_radius2_cover_pair_formula(self):
        # Null code of H columns [1,2,4,8,16,3,5,6,31].
        basis=(35,69,134,287)
        code=code_from_basis(basis)
        self.assertEqual(len(code),16)
        self.assertEqual(program_collision(code,9,2,2),21)
        self.assertEqual(pair_collision_from_weights(code,9,2),21)

    def test_same_weight_enum_different_w3(self):
        c0=code_from_basis((15,20,36))
        c1=code_from_basis((9,20,34))
        self.assertEqual(code_weight_enumerator(c0,6), code_weight_enumerator(c1,6))
        self.assertEqual(code_weight_enumerator(c0,6),(1,0,3,0,3,0,1))
        self.assertEqual(program_collision(c0,6,1,2),3)
        self.assertEqual(program_collision(c1,6,1,2),3)
        self.assertEqual(program_collision(c0,6,1,3),1)
        self.assertEqual(program_collision(c1,6,1,3),0)
        self.assertEqual(triple_collision_from_triangle_profile(c0,6,1),1)
        self.assertEqual(triple_collision_from_triangle_profile(c1,6,1),0)

if __name__=="__main__":
    unittest.main()
