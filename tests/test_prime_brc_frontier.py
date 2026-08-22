from enterprise_math.prime_brc_frontier import frontier, mirror_frontier_escape


def test_frontier_three_block_normal_form():
    # Fully smooth: 105=7*(3*5) at k=10.
    a=frontier(10,105)
    assert (a["A"],a["p"],a["m"],a["kind"])==(7,3,5,"FULLY_K_SMOOTH_COMPOSITE")
    # Large-prime-tail composite: 111=3*37.
    b=frontier(10,111)
    assert (b["A"],b["p"],b["m"],b["kind"])==(3,37,1,"LARGE_PRIME_TAIL_COMPOSITE")
    # Prime: 109.
    c=frontier(10,109)
    assert (c["A"],c["p"],c["m"],c["kind"])==(1,109,1,"PRIME")


def test_semiprime_mirror_cross_escape():
    # k=20,M=420,r=17: 403=13*31, 437=19*23.
    data=mirror_frontier_escape(20,17)
    assert data["small_core"]==13
    assert data["large_core"]==19
    assert data["lower_cross"]==13*23<20**2
    assert data["upper_cross"]==19*31>21**2


def test_non_semiprime_composite_escape():
    # Search-free fixed witness with deeper factorization on one side.
    # k=31,M=992,r=23: 969=3*17*19, 1015=5*7*29.
    data=mirror_frontier_escape(31,23)
    assert data["escape"] is True
    assert data["lower_cross"]<31**2
    assert data["upper_cross"]>32**2
