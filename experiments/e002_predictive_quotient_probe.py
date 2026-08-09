#!/usr/bin/env python3
"""Deterministic probe for the E002 finite predictive quotient compiler."""

from itertools import product

from enterprise_math.predictive_quotient import (
    predictive_block_profile,
    restricted_block_count,
    stable_predictive_partition,
)


def countdown_system(width: int, dimension: int):
    states = tuple(product(range(width + 1), repeat=dimension))
    initial = tuple(product(range(1, width + 1), repeat=dimension))

    def tick(state):
        return tuple(max(0, value - 1) for value in state)

    return states, initial, {"tick": tick}


def main() -> None:
    width = 5
    dimension = 3
    states, initial, actions = countdown_system(width, dimension)
    observations = {
        "full": lambda state: tuple(int(value == 0) for value in state),
        "sum": lambda state: sum(int(value == 0) for value in state),
        "any": lambda state: int(any(value == 0 for value in state)),
        "all": lambda state: int(all(value == 0 for value in state)),
    }

    print(f"fine_states={len(states)}")
    print(f"initial_precision_fiber={len(initial)}")
    for name, observe in observations.items():
        profile = predictive_block_profile(
            states,
            actions,
            observe,
            width,
            subset=initial,
        )
        stable = stable_predictive_partition(states, actions, observe)
        print(f"observation={name}")
        print(f"fiber_profile={profile}")
        print(f"stable_global_blocks={stable.block_count}")
        print(f"stable_depth={stable.stabilization_depth}")
        print(
            "stable_initial_blocks="
            + str(restricted_block_count(states, stable.partition, initial))
        )


if __name__ == "__main__":
    main()
