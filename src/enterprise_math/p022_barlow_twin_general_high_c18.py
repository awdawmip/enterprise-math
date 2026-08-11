"""Blackout exclusion for the c=18 / q=5 mod24 simple-high sector.

In the general simple high-digit branch put a=r+h with 3|r and 3|h.  On the
forced residue sector c=18 one has

    q = 8(r-h)-19,
    b = -5r + 8h^2 + 19h + 18,

where b is the secondary low digit and complete simple-high escape forces
b to be a Franel q-zero in the symmetric primitive band.

This file proves that b cannot remain inside the original twin blackout.

1. If r<b<2r-2, complete escape forces b itself to be a nontrivial twin center.
   Modulo five this is impossible.  For h=0,2 mod5 one has 5|(2b-1); for
   h=3,4 mod5 one has 5|(2b+1).  The remaining class h=1 mod5 is already
   impossible because the six prime forms

       2r-1, 2r+1, 2(r+h)-1, 2(r+h)+1, 4r-5, q

   cover all r mod5.

2. b=r+1 is excluded by single-digit Franel nonadjacency.

3. b=2r-2 is impossible arithmetically: the equality gives

       7r = 8h^2+19h+20,

   whose right side is 2 mod3 when 3|h, while 3|r for a nontrivial twin center.

4. b=2r-1 is the terminal target and has zero q-depth after terminal
   cancellation, so it cannot be the secondary low zero.

5. The remaining lower boundary b=r is also impossible.  The equality gives

       6r = 8h^2+19h+18.

   Integrality and 3|r,h force h=18t and

       r = 432t^2+57t+3,
       q = 3456t^2+312t+5.

   Modulo five, for every t one of the required prime forms is divisible by 5:

       t=0: 2r-1 (also 2a-1 and q),
       t=1: 2r+1,
       t=2: 4r-5,
       t=3: 2r+1 (also q),
       t=4: 2r-1.

   In the late branch these forms exceed 5, hence cannot be prime.

Consequently every complete simple-high escape in the c=18 sector satisfies

    b >= 2r.

This is a pure arithmetic/defect-visibility reduction; no new Franel
congruence is used.
"""

from __future__ import annotations


def c18_secondary_low(rank: int, gap: int) -> int:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank <= 0:
        raise ValueError("rank must be positive")
    if isinstance(gap, bool) or not isinstance(gap, int) or gap <= 0:
        raise ValueError("gap must be positive")
    return -5 * rank + 8 * gap * gap + 19 * gap + 18


def c18_interior_twin_mod5_obstruction(gap: int) -> tuple[str, int]:
    """Return the mod-5 obstruction attached to an interior low twin zero.

    For h mod5 !=1 one of 2b+-1 is identically divisible by five.  The class
    h=1 is labeled ``source-lines`` because the original six prime forms cover
    all r mod5 there.
    """
    if isinstance(gap, bool) or not isinstance(gap, int) or gap <= 0:
        raise ValueError("gap must be positive")
    residue = gap % 5
    if residue in (0, 2):
        return "2b-1", 0
    if residue in (3, 4):
        return "2b+1", 0
    return "source-lines", residue


def c18_source_lines_cover_mod5_at_gap_one(rank_residue: int) -> str:
    """For h=1 mod5 identify a required prime form divisible by five."""
    residue = rank_residue % 5
    table = {
        0: "4r-5",
        1: "2(r+h)+1",
        2: "2r+1",
        3: "2r-1",
        4: "q",
    }
    return table[residue]


def c18_terminal_low_boundary_is_mod3_impossible(rank: int, gap: int) -> bool:
    """Certify b=2r-2 contradicts 3|r,h."""
    if rank % 3 or gap % 3:
        raise ValueError("rank and gap must be multiples of three")
    low = c18_secondary_low(rank, gap)
    if low != 2 * rank - 2:
        raise ValueError("secondary low digit is not the terminal boundary")
    if (8 * gap * gap + 19 * gap + 20) % 3 != 2:
        raise AssertionError("terminal boundary right side must be 2 modulo three")
    if (7 * rank) % 3 != 0:
        raise AssertionError("twin rank must make the left side zero modulo three")
    return True


def c18_source_low_boundary_parameter(gap: int) -> tuple[int, int, int]:
    """For b=r return (t,r,q) after the forced h=18t reduction."""
    if isinstance(gap, bool) or not isinstance(gap, int) or gap <= 0:
        raise ValueError("gap must be positive")
    numerator = 8 * gap * gap + 19 * gap + 18
    if numerator % 6:
        raise ValueError("b=r does not give an integral rank")
    rank = numerator // 6
    if rank % 3:
        raise ValueError("b=r rank is not a nontrivial twin-center multiple of three")
    if gap % 18:
        raise AssertionError("b=r with 3|rank forces h to be divisible by eighteen")
    t = gap // 18
    expected_rank = 432 * t * t + 57 * t + 3
    prime = 8 * rank - 8 * gap - 19
    expected_prime = 3456 * t * t + 312 * t + 5
    if rank != expected_rank or prime != expected_prime:
        raise AssertionError("c18 source-boundary parameterization changed")
    return t, rank, prime


def c18_source_low_boundary_mod5_obstruction(gap: int) -> str:
    """For b=r identify a required prime form divisible by five."""
    t, _, _ = c18_source_low_boundary_parameter(gap)
    table = {
        0: "2r-1",
        1: "2r+1",
        2: "4r-5",
        3: "2r+1",
        4: "2r-1",
    }
    return table[t % 5]
