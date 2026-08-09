from math import isqrt

import pytest

from enterprise_math.label_erasure import (
    full_state_recoverable,
    label_decoder,
    label_recoverable,
    overlap_pairs,
)


def test_label_recoverable_iff_shell_images_are_disjoint() -> None:
    shells = {
        "left": range(0, 4),
        "right": range(10, 14),
    }
    assert label_recoverable(shells, lambda x: x)
    assert overlap_pairs(shells, lambda x: x) == ()

    assert not label_recoverable(shells, lambda x: x % 10)
    collisions = overlap_pairs(shells, lambda x: x % 10)
    assert len(collisions) == 1
    assert collisions[0][2] == frozenset({0, 1, 2, 3})


def test_decoder_exists_exactly_on_disjoint_images() -> None:
    shells = {2: [20, 21], 3: [30, 31]}
    decoder = label_decoder(shells, lambda x: x // 10)
    assert decoder == {2: 2, 3: 3}

    with pytest.raises(ValueError):
        label_decoder(shells, lambda _x: 0)


def test_label_recovery_is_weaker_than_full_state_recovery() -> None:
    shells = {
        "a": [25, 26, 27],
        "b": [49, 50],
    }
    assert label_recoverable(shells, isqrt)
    assert not full_state_recoverable(shells, isqrt)


def test_full_state_recovery_requires_within_shell_injectivity_too() -> None:
    shells = {"a": [1, 2], "b": [3, 4]}
    assert full_state_recoverable(shells, lambda x: x)
    assert not full_state_recoverable(shells, lambda x: x // 2)
