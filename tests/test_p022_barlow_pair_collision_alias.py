from itertools import combinations

from enterprise_math.p022_barlow_fiber_convolution import (
    profile_collision_count,
    profile_from_segments,
    profile_image_size,
)
from enterprise_math.p022_barlow_pair_collision_alias import (
    cleaner_three_segment_alias,
    first_pair_collision_alias,
    pair_collision_from_segments,
    pair_moment_from_segments,
    verify_first_alias_identity,
)


def _partitions_fixed(total: int, parts: int, minimum: int = 1):
    if parts == 1:
        if total >= minimum:
            yield (total,)
        return
    for first in range(minimum, total // parts + 1):
        for rest in _partitions_fixed(total - first, parts - 1, first):
            yield (first,) + rest


def test_exact_n21_pair_alias_has_same_j2_but_different_higher_data() -> None:
    left, right = first_pair_collision_alias()
    assert sum(left) == sum(right) == 21
    assert len(left) == len(right) == 4
    assert pair_moment_from_segments(left) == pair_moment_from_segments(right) == 23465490048
    assert pair_collision_from_segments(left) == pair_collision_from_segments(right) == 11731696448

    left_profile = profile_from_segments(left)
    right_profile = profile_from_segments(right)
    assert left_profile != right_profile
    assert profile_image_size(left_profile) == 792
    assert profile_image_size(right_profile) == 756
    assert profile_collision_count(left_profile, 3) == 64506690871040
    assert profile_collision_count(right_profile, 3) == 70446056775360

    data = verify_first_alias_identity()
    assert data["length"] == 21
    assert data["checkpoint_count"] == 4
    assert data["M2"] == 23465490048


def test_no_pair_alias_exists_at_smaller_total_length_with_fixed_checkpoint_count() -> None:
    # Complete finite search over segment multisets.  N=21 is therefore the
    # first total length at which fixed-(N,m) J2 aliasing appears in this class.
    for total in range(1, 21):
        for parts in range(1, total + 1):
            seen = {}
            for segments in _partitions_fixed(total, parts):
                moment = pair_moment_from_segments(segments)
                assert moment not in seen
                seen[moment] = segments


def test_three_segment_alias_has_clean_ratio_identity_and_j3_separation() -> None:
    left, right = cleaner_three_segment_alias()
    assert sum(left) == sum(right) == 22
    assert len(left) == len(right) == 3
    assert pair_moment_from_segments(left) == pair_moment_from_segments(right) == 326704870800
    assert pair_collision_from_segments(left) == pair_collision_from_segments(right) == 163350338248

    left_profile = profile_from_segments(left)
    right_profile = profile_from_segments(right)
    assert profile_image_size(left_profile) == 180
    assert profile_image_size(right_profile) == 171
    assert profile_collision_count(left_profile, 3) == 5505541532248208
    assert profile_collision_count(right_profile, 3) == 6017794610369968
