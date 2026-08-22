"""Prime-BRC cross-denominator shadow staircase.

For k/2<p<k define

    C_p = floor(((k+1)^2-1)/(p+1)) - floor(k^2/p).

The corresponding real q-window has length strictly below one.  Thus C_p is a
0/1 edge event.  When present it gives the unique q with

    k^2 < p*q < M < (p+1)*q < (k+1)^2,

so the same large divisor q>k produces one strict hit in each half of the
square basin.  These are the non-destructive even/odd shadow pairs used by the
Prime-BRC kappa/chi interpretation.
"""

from __future__ import annotations

from .prime_brc_phase import square_basin_frame, square_midpoint_defect
from .legendre import square_carry


def cross_denominator_edge(k: int, p: int) -> dict[str, object]:
    if k < 3:
        raise ValueError("require k>=3")
    if not (2 * p > k and p < k):
        raise ValueError("require k/2<p<k")
    frame = square_basin_frame(k)
    L = int(frame["lower"])
    M = int(frame["center"])
    U = int(frame["upper"])
    lower_q = L // p
    upper_q = (U - 1) // (p + 1)
    edge = upper_q - lower_q
    if edge not in (0, 1):
        raise AssertionError("subunit cross-denominator window escaped 0/1")

    # Exact width identity:
    # p(p+1)*(1 - (U/(p+1)-L/p)) = (k-p)^2 >0.
    width_num = p * U - (p + 1) * L
    width_den = p * (p + 1)
    if not (0 < width_num < width_den):
        raise AssertionError("cross-denominator window is not positive subunit")

    t = k - p
    h, s = divmod(t * t, p)
    if edge != int(s > h):
        raise AssertionError("residue-greater-than-quotient edge criterion failed")
    alt = 1 + (t * t - 1) // (p + 1) - (t * t) // p
    if alt != edge:
        raise AssertionError("denominator-transfer floor-stability identity failed")

    data: dict[str, object] = {
        "k": k,
        "p": p,
        "t": t,
        "h": h,
        "s": s,
        "edge": edge,
        "width_numerator": width_num,
        "width_denominator": width_den,
        "floor_stability": edge,
    }
    if edge:
        q = lower_q + 1
        lower_state = p * q
        upper_state = (p + 1) * q
        if not (L < lower_state < M < upper_state < U):
            raise AssertionError("shadow edge failed strict midpoint crossing")
        if not (k < q <= 2 * k - 1):
            raise AssertionError("shadow edge label escaped k<q<=2k-1")
        if square_carry(k, q) != 2 or square_midpoint_defect(k, q) != 0:
            raise AssertionError("double-hit q did not realize (kappa,chi)=(2,0)")
        data.update(
            {
                "q": q,
                "lower_state": lower_state,
                "upper_state": upper_state,
                "lower_radius": M - lower_state,
                "upper_radius": upper_state - M,
            }
        )
    return data


def shadow_staircase(k: int) -> dict[str, object]:
    """Enumerate the exact monotone shadow staircase for one k."""
    if k < 3:
        raise ValueError("require k>=3")
    start = k // 2 + 1
    edges = []
    for p in range(start, k):
        data = cross_denominator_edge(k, p)
        if data["edge"]:
            edges.append(data)
    q_labels = [int(item["q"]) for item in edges]
    if any(a <= b for a, b in zip(q_labels, q_labels[1:])):
        raise AssertionError("shadow staircase q labels are not strictly decreasing")
    if len(set(q_labels)) != len(q_labels):
        raise AssertionError("shadow staircase reused a double-hit q label")
    return {
        "k": k,
        "edges": tuple(edges),
        "edge_count": len(edges),
        "q_labels": tuple(q_labels),
    }


def double_hit_large_moduli(k: int) -> tuple[int, ...]:
    """Return transverse q>k whose strict square-basin hit count is exactly two.

    The staircase theorem gives a bijection between these q and C_p=1 edges.
    """
    frame = square_basin_frame(k)
    L = int(frame["lower"])
    M = int(frame["center"])
    U = int(frame["upper"])
    result = []
    for q in range(k + 1, 2 * k):
        lower_hits = M // q - L // q
        upper_hits = (U - 1) // q - M // q
        if M % q == 0:
            # The half formulas need endpoint correction at M; direct strict scan
            # avoids silently treating a midpoint hit as two side hits.
            hits = (U - 1) // q - L // q - 1
        else:
            hits = lower_hits + upper_hits
        if hits == 2 and M % q != 0:
            result.append(q)
    staircase = tuple(int(item["q"]) for item in shadow_staircase(k)["edges"])
    if tuple(sorted(result, reverse=True)) != staircase:
        raise AssertionError("double-hit large-modulus spectrum != shadow staircase")
    return tuple(result)


def guaranteed_near_k_shadow_prefix(k: int) -> dict[str, object]:
    """All t with 1<=t and t^2<k-t force the p=k-t edge.

    This yields an elementary O(sqrt(k)) deterministic suffix of the staircase;
    it is a composite-shadow construction, not a prime-distribution statement.
    """
    if k < 3:
        raise ValueError("require k>=3")
    t_values = []
    t = 1
    while t * t < k - t:
        p = k - t
        data = cross_denominator_edge(k, p)
        if data["edge"] != 1:
            raise AssertionError("t^2<p failed to force a shadow edge")
        t_values.append(t)
        t += 1
    return {
        "k": k,
        "t_values": tuple(t_values),
        "guaranteed_edge_count": len(t_values),
        "p_values": tuple(k - t for t in t_values),
    }
