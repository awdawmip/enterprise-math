import unittest

from enterprise_math.causal_future_module import causal_future_closure
from enterprise_math.causal_product_system import (
    block_diagonal,
    independent_product_causal_rank,
    independent_product_observations,
    independent_product_operations,
)


class CausalProductSystemTests(unittest.TestCase):
    def test_block_diagonal_is_componentwise_operation_table(self):
        left = ((0, 1), (0, 0))
        right = ((2,),)
        self.assertEqual(
            block_diagonal(left, right),
            (
                (0, 1, 0),
                (0, 0, 0),
                (0, 0, 2),
            ),
        )

    def test_independent_causal_rank_is_additive(self):
        left_shift = (
            (0, 1),
            (0, 0),
        )
        right_identity = ((1,),)
        left_obs = ((1, 0),)
        right_obs = ((1,),)

        left_rank, right_rank, product_rank = independent_product_causal_rank(
            (left_shift,),
            left_obs,
            (right_identity,),
            right_obs,
        )
        self.assertEqual((left_rank, right_rank), (2, 1))
        self.assertEqual(product_rank, left_rank + right_rank)

    def test_product_observations_do_not_create_cross_terms(self):
        observations = independent_product_observations(
            ((1, 2),),
            ((3,),),
        )
        self.assertEqual(observations, ((1, 2, 0), (0, 0, 3)))

    def test_product_closure_equals_sum_of_component_visible_ranks_in_examples(self):
        examples = (
            (
                (((1,),), ((1,),)),
                (((1,),), ((1,),)),
            ),
            (
                (
                    (((0, 1), (0, 0)),),
                    ((1, 0),),
                ),
                (
                    (((0, 1, 0), (0, 0, 1), (0, 0, 0)),),
                    ((1, 0, 0),),
                ),
            ),
        )
        for (left_ops, left_obs), (right_ops, right_obs) in examples:
            left = causal_future_closure(left_ops, left_obs)
            right = causal_future_closure(right_ops, right_obs)
            product = causal_future_closure(
                independent_product_operations(left_ops, right_ops),
                independent_product_observations(left_obs, right_obs),
            )
            self.assertEqual(
                product.causal_visible_rank,
                left.causal_visible_rank + right.causal_visible_rank,
            )


if __name__ == "__main__":
    unittest.main()
