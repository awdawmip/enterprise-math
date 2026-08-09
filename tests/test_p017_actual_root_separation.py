from enterprise_math.p017_actual_root_separation import (
    actual_lower_band_overlaps,
    actual_lower_band_root_images,
    actual_lower_band_root_images_disjoint,
)


def test_sharp_k8_actual_root_collision() -> None:
    overlaps = actual_lower_band_overlaps(8)
    assert overlaps == ((2, 3, frozenset({5})),)


def test_k9_starts_uniform_actual_root_separation() -> None:
    assert actual_lower_band_root_images_disjoint(9)
    images = actual_lower_band_root_images(9)
    assert images[2] == frozenset({6, 7})
    assert images[3] == frozenset({5})


def test_actual_root_images_disjoint_through_large_finite_probe() -> None:
    for k in range(9, 2000):
        assert actual_lower_band_root_images_disjoint(k), (k, actual_lower_band_overlaps(k))


def test_only_small_actual_collisions_before_stable_threshold() -> None:
    events = {
        k: actual_lower_band_overlaps(k)
        for k in range(2, 9)
        if actual_lower_band_overlaps(k)
    }
    assert events == {
        5: ((2, 3, frozenset({3})),),
        6: ((2, 3, frozenset({4})),),
        8: ((2, 3, frozenset({5})),),
    }
