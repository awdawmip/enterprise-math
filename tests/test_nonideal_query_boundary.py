from enterprise_math.nonideal_query_boundary import analyze_nonideal_boundary


def test_chain_width_one_does_not_save_nonideal_state():
    elements = ("a", "b")
    leq = frozenset({("a", "a"), ("b", "b"), ("a", "b")})
    state = frozenset({"b"})
    report = analyze_nonideal_boundary(elements, leq, state)
    assert not report.is_ideal
    assert not report.normalization_valid
    assert report.violating_pair == ("a", "b")
    assert report.violating_query == frozenset({"a", "b"})


def test_chain_ideal_state_preserves_maximal_query_normalization():
    elements = ("a", "b", "c")
    leq = frozenset(
        {
            ("a", "a"),
            ("b", "b"),
            ("c", "c"),
            ("a", "b"),
            ("b", "c"),
            ("a", "c"),
        }
    )
    report = analyze_nonideal_boundary(elements, leq, frozenset({"a", "b"}))
    assert report.is_ideal
    assert report.normalization_valid
    assert report.violating_pair is None


def test_branching_poset_nonideal_defect_is_still_pairwise():
    elements = ("a", "b", "c")
    leq = frozenset(
        {
            ("a", "a"),
            ("b", "b"),
            ("c", "c"),
            ("a", "c"),
            ("b", "c"),
        }
    )
    report = analyze_nonideal_boundary(elements, leq, frozenset({"c"}))
    assert not report.is_ideal
    assert not report.normalization_valid
    assert report.violating_pair in {("a", "c"), ("b", "c")}


def test_empty_and_full_states_are_ideals():
    elements = (0, 1)
    leq = frozenset({(0, 0), (1, 1), (0, 1)})
    assert analyze_nonideal_boundary(elements, leq, frozenset()).normalization_valid
    assert analyze_nonideal_boundary(elements, leq, frozenset(elements)).normalization_valid
