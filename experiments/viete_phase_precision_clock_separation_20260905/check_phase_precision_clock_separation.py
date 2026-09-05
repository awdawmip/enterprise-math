#!/usr/bin/env python3
"""Exact checker for physical phase refinement versus pro-state precision projection.

The physical C6->C12 refinement embeds old Cell phases by k -> 2k and the
fine successor advances by one half-step. Therefore one coarse successor is
exactly two fine successors. This differs from the standard residue-reduction
inverse system used by the rotation precision pro-state, where +1 commutes
levelwise.
"""


def modulus(m: int) -> int:
    return 6 * (2 ** m)


def successor(n: int, x: int, steps: int = 1) -> int:
    return (x + steps) % n


def phase_embedding(m: int, k: int) -> int:
    n = modulus(m)
    return (2 * (k % n)) % modulus(m + 1)


def precision_projection(m: int, q: int) -> int:
    return q % modulus(m)


def physical_collapse(m: int, q: int) -> int:
    """Typed temporal collapse using canonical representatives 0..2N-1."""
    n = modulus(m)
    return (q % (2 * n)) // 2


def check_general_clock_law():
    for m in range(0, 10):
        n = modulus(m)
        fine = modulus(m + 1)

        for k in range(n):
            ik = phase_embedding(m, k)

            # Physical phase-preserving embedding doubles the fine index.
            assert phase_embedding(m, successor(n, k)) == successor(fine, ik, 2)

            # It does NOT intertwine one coarse step with one fine step.
            assert phase_embedding(m, successor(n, k)) != successor(fine, ik, 1)

            # Standard precision projection commutes with synchronous +1.
            assert precision_projection(m, successor(fine, ik, 1)) == successor(
                n, precision_projection(m, ik), 1
            )

        # Physical collapse is the left inverse of the phase embedding.
        for k in range(n):
            assert physical_collapse(m, phase_embedding(m, k)) == k

        # But physical collapse only intertwines TWO fine steps with ONE coarse step.
        for q in range(fine):
            assert physical_collapse(m, successor(fine, q, 2)) == successor(
                n, physical_collapse(m, q), 1
            )


def check_projection_is_not_physical_collapse():
    for m in range(0, 8):
        n = modulus(m)
        mismatches = []
        for k in range(n):
            fine_old_phase = phase_embedding(m, k)
            p = precision_projection(m, fine_old_phase)
            r = physical_collapse(m, fine_old_phase)
            assert r == k
            if p != k:
                mismatches.append(k)
        assert mismatches


def check_no_synchronous_total_map_preserves_old_phases():
    # Any f:C_{2N}->C_N satisfying f(q+1)=f(q)+1 has form f(q)=c+q mod N.
    # Requiring f(2k)=k for all old phases is impossible for N>=2.
    for m in range(0, 10):
        n = modulus(m)
        possible = False
        for c in range(n):
            if all((c + 2 * k) % n == k for k in range(n)):
                possible = True
                break
        assert not possible


def check_first_physical_layer_labels():
    # Encode physical C12 as E_k=2k, G_k=2k+1.
    n = 6
    fine = 12
    for k in range(6):
        e = 2 * k
        g = 2 * k + 1
        assert successor(fine, e) == g
        assert successor(fine, g) == 2 * ((k + 1) % 6)
        assert physical_collapse(0, e) == k
        assert physical_collapse(0, g) == k
        assert physical_collapse(0, successor(fine, e)) == k
        assert physical_collapse(0, successor(fine, g)) == (k + 1) % 6
        assert successor(fine, e, 2) == 2 * ((k + 1) % 6)


def main():
    check_general_clock_law()
    check_projection_is_not_physical_collapse()
    check_no_synchronous_total_map_preserves_old_phases()
    check_first_physical_layer_labels()
    print("PASS: physical phase-refinement / pro-state precision-clock separation")
    print("phase embedding: i_m Q_m = Q_{m+1}^2 i_m")
    print("precision projection: p_m Q_{m+1} = Q_m p_m")
    print("physical collapse: r_m Q_{m+1}^2 = Q_m r_m")
    print("no synchronous total f can also satisfy f(2k)=k for all old phases")


if __name__ == "__main__":
    main()
