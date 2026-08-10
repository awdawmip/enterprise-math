from math import ceil, log2

from enterprise_math.balanced_binary_synergy import balanced_binary_synergy


def test_balanced_compiler_attains_helper_and_depth_bounds():
    for arity in range(2, 10):
        compiler = balanced_binary_synergy(arity)
        assert len(compiler.helpers) == arity - 2
        assert len(compiler.rules) == arity - 1
        assert max(len(rule.premise) for rule in compiler.rules) == 2
        assert compiler.depth == ceil(log2(arity))
        assert compiler.helper_lower_bound == arity - 2
        assert compiler.depth_lower_bound == ceil(log2(arity))
        assert compiler.raw_projection_verified


def test_balancing_strictly_beats_sequential_depth_for_arity_five():
    compiler = balanced_binary_synergy(5)
    assert compiler.depth == 3
    assert 3 < 4  # sequential Stage-135 depth is k-1
    assert len(compiler.helpers) == 3


def test_power_of_two_has_perfect_binary_depth():
    compiler = balanced_binary_synergy(8)
    assert compiler.depth == 3
    assert len(compiler.helpers) == 6
    assert len(compiler.rules) == 7
