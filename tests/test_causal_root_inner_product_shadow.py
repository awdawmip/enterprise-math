import unittest

from enterprise_math.causal_primitive_link_profile import (
    a_roots,
    d_roots,
    e6_scaled_roots,
    e7_scaled_roots,
    e8_scaled_roots,
)
from enterprise_math.causal_root_inner_product_shadow import (
    causal_reconstruction_matches_coordinates,
)


class CausalRootInnerProductShadowTests(unittest.TestCase):
    def test_a_d_e_simply_laced_inner_products_are_relation_shadows(self):
        families = (
            a_roots(2), a_roots(3), a_roots(5),
            d_roots(4), d_roots(7),
            e6_scaled_roots(), e7_scaled_roots(), e8_scaled_roots(),
        )
        for roots in families:
            self.assertTrue(causal_reconstruction_matches_coordinates(roots))


if __name__ == "__main__":
    unittest.main()
