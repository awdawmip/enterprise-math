# Exact first positive future-risk increment after horizon 200,000

Date 2026-11-09. This addendum uses the Farey–three-gap theorem in PROOF.md and its exact rational implementation. Frozen input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Exact theorem at historical length m=128

For every integer L with 200000 <= L <= 322048,

    R(128,L) = 479873 - 1830144*theta.

At L=322049, the first strict increase occurs:

    R(128,322049) = 520258 - 1984165*theta,
    R(128,322049)-R(128,322048)
                  = 40385 - 154021*theta > 0.

Therefore the newly established constant stretch is L=200001,...,322048 (122048 consecutive steps).

## Proof and certificate

1. The historical arcs are fixed. Adding future phase cuts only subdivides their current gaps; each historical arc's maximum gap length is nonincreasing. Thus R(128,L) is nondecreasing in the integer L.
2. The previously proven L=200000 endpoint (479873,-1830144) is reproduced exactly by VERIFY_FAREY_GAP_RISK.py.
3. Independently call the exact Farey/floor-sum evaluator at L=322048 and L=322049. The resulting pairs are respectively (479873,-1830144) and (520258,-1984165). Both endpoints of the certified rational theta interval give the same gap-winning choices, so these formulas hold for the locked exact theta.
4. By monotonicity and equality at L=200000 and 322048, every intervening value equals this same risk. The last difference is positive because 40385-154021*theta is positive at both endpoints of the rational interval.

VERIFY_NEXT_BREAK.py also locates the first increase by monotone bisection of [200000,400000] using only 19 distinct exact Farey risk evaluations. The bisection is a reproducible search; the theorem follows from the endpoint equality, strict final difference, and monotonicity.

Run:

    python VERIFY_FAREY_GAP_RISK.py
    python VERIFY_NEXT_BREAK.py

The previous 200000-step source and new trillion-step single-horizon formula use the same frozen theta definition. The algorithmic and numeric results apply to the S23/AV *circle observer*, with no change to the native P000 geometry or scientific pin.

Next problem: generate all positive-increment block edges and affine increment values in output-sensitive order using Farey denominator transitions, starting from the 322049 edge. Identify a finite certificate for each claimed block, and compare full input/output and precision bit cost to the prior O(N log N) method.
