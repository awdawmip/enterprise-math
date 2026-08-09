#!/usr/bin/env python3
"""Deterministic Stage-5 probe: one trajectory, different future languages."""

from enterprise_math.precision_task_observable import (
    any_or_all_class_count,
    full_vector_class_count,
    linear_two_coordinate_class_count,
    symmetric_sum_class_count,
    two_coordinate_equality_class_count,
)


def main() -> None:
    horizon = 4
    buckets = horizon + 1
    print(f"horizon={horizon}")
    print(f"crossing_buckets={buckets}")

    print(f"full_2d={full_vector_class_count(2, horizon)}")
    print(f"linear_generic_1_2={linear_two_coordinate_class_count(1, 2, horizon)}")
    print(f"linear_sum_1_1={linear_two_coordinate_class_count(1, 1, horizon)}")
    print(f"linear_difference_1_minus1={linear_two_coordinate_class_count(1, -1, horizon)}")
    print(f"single_coordinate={linear_two_coordinate_class_count(1, 0, horizon)}")
    print(f"equality_boolean={two_coordinate_equality_class_count(horizon)}")

    dimension = 5
    print(f"dimension={dimension}")
    print(f"full_nd={full_vector_class_count(dimension, horizon)}")
    print(f"symmetric_sum_nd={symmetric_sum_class_count(dimension, horizon)}")
    print(f"any_crossed_nd={any_or_all_class_count(horizon)}")
    print(f"all_crossed_nd={any_or_all_class_count(horizon)}")
    print(
        "integer_state_savings_any="
        + str(full_vector_class_count(dimension, horizon) - any_or_all_class_count(horizon))
    )


if __name__ == "__main__":
    main()
