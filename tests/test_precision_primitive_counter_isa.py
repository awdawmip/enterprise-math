import unittest
from enterprise_math.precision_primitive_counter_isa import (
    aggregate_mass, cell_mass, coordinate_depths, isa_gap_mass
)

class PrimitiveCounterISATests(unittest.TestCase):
    def test_diagonal_line_gap(self):
        rows=((1,1,1),)
        self.assertEqual(coordinate_depths(rows,2,3),(3,3,3))
        self.assertEqual(aggregate_mass(rows,2,3),3)
        self.assertEqual(cell_mass(rows,2,3),9)
        self.assertEqual(isa_gap_mass(rows,2,3),6)

    def test_no_gap_for_coordinate_basis(self):
        self.assertEqual(isa_gap_mass(((1,0),(0,1)),2,2),0)

if __name__=="__main__":
    unittest.main()
