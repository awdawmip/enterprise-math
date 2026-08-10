from enterprise_math.poset_query_count_pushforward import query_multiplicity_pushforward


def test_query_counts_recover_projected_not_ambient_multiplicity():
    elements = ("a", "b")
    leq = frozenset({("a", "a"), ("b", "b")})
    query = ("a",)

    left = {frozenset({"a"}): 1}
    right = {frozenset({"a", "b"}): 1}
    left_push = query_multiplicity_pushforward(elements, leq, query, left)
    right_push = query_multiplicity_pushforward(elements, leq, query, right)

    assert left != right
    assert left_push.projected_multiplicities == right_push.projected_multiplicities
    assert left_push.projected_counts == right_push.projected_counts
    assert left_push.query_width == right_push.query_width == 1


def test_query_pushforward_conserves_total_multiplicity():
    elements = ("a", "b", "c")
    leq = frozenset((x, x) for x in elements)
    multiplicities = {
        frozenset(): 2,
        frozenset({"a"}): 3,
        frozenset({"a", "b"}): 5,
        frozenset({"a", "c"}): 7,
    }
    push = query_multiplicity_pushforward(elements, leq, ("a", "b"), multiplicities)
    assert push.ambient_total == push.projected_total == 17


def test_chain_query_inside_diamond_has_width_one_count_horizon():
    elements = ("a", "b", "c", "d")
    leq = frozenset(
        {
            ("a", "a"),
            ("b", "b"),
            ("c", "c"),
            ("d", "d"),
            ("a", "b"),
            ("a", "c"),
            ("a", "d"),
            ("b", "d"),
            ("c", "d"),
        }
    )
    multiplicities = {
        frozenset({"a", "b"}): 2,
        frozenset({"a", "c"}): 3,
        frozenset({"a", "b", "c", "d"}): 5,
    }
    push = query_multiplicity_pushforward(elements, leq, ("a", "d"), multiplicities)
    assert push.query_width == 1
    projected = dict(push.projected_multiplicities)
    assert projected[frozenset({"a"})] == 5
    assert projected[frozenset({"a", "d"})] == 5


def test_full_query_is_identity_pushforward():
    elements = (0, 1)
    leq = frozenset({(0, 0), (1, 1)})
    multiplicities = {
        frozenset(): 1,
        frozenset({0}): 2,
        frozenset({1}): 3,
        frozenset({0, 1}): 4,
    }
    push = query_multiplicity_pushforward(elements, leq, elements, multiplicities)
    assert dict(push.projected_multiplicities) == multiplicities
