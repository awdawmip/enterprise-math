# Collaborative check of the v14 basic-pair and one-W proofs

The reviewed text is `nine_prefix_v14/proof.md`. This records shared-context
mathematical assistance, not independent project Review. No large execution
or old classification search was repeated.

The basic-pair omission bound separates every exceptional effective order
from the all-order remainder bound. The nine-largest-capacity sum is
2375/2376. The full-exponent old-hole density 6/35 converts its positive
gap to 1/13860. The restricted-parity calculation for exactly one basic
prime uses the correct affine image of H: the fixed W channels are
precisely one-third of the surviving original H points congruent to one
modulo three. Under the parity coordinate change these points are
relabeled, but their counts are unchanged. Deleting every possible
mod-seven row or row pair covers all phase choices; empty and duplicate
rows can only waste slots.

For the six-class lemma, the m=0, j=3 restriction is valid. All three
period-ten rows must lie in the two five-point columns, so the complete
three-point column is left to three other rows. Effective periods one
and two are absent there. Each remaining row covers at most one-third;
equality forces periods 15 or 35 in the original coordinate, and their
actual total A-mass is then one each. This defeats the preceding loose
global bound.

For j=4, at most one period-ten row may occupy the three-point column.
An entire parity subprogression of that column is therefore left to two
rows. Their maximum relative mass is one-half, whose equality period is
two after restriction. Solving h/gcd(h,10)=2 gives h=4 or h=20; only
h=20 is allowed. Each has actual A-mass 3/4. The resulting total is
strictly smaller than thirteen. The m=1,2,3 deleted-row estimates use
the proper remaining slot counts and strict rational gaps.

In the cross-phase step m=4, the final two rows occupy only the missing
mod-seven class. A first-phase period-21 representative in another row
would leave that entire row uncovered on v=2 modulo three. Thus all four
representatives must have unrestricted v-period seven and exhaust Z.
The two completion rows must both remain active on the second phase,
forcing original periods 14 or 35. They then cover all modulo-three
phases without the selected W prime, contradicting inclusion-minimality.

For m=5, any selected period-21 representative misses v=2 modulo three.
One further congruence class cannot cover two full occupied mod-seven
rows: the two distinct modulo-five points within a row force its period
to divide seven, and a second row forces that period to divide a
nonmultiple of seven. This would give period one, which is unavailable.
Therefore exactly one row uses period 21, the other four exhaust Z, and
the last prime must be another period-21 prime on the missing
modulo-three phase. This proves the asserted complete one-W form.

The phase count 2*5*4!*5*4=4800 and the six free-prime sign multiplier
2^6 are consistent. Inclusion-minimality is explicitly distinguished
from exact root cost; the latter is obtained separately by killing the
complete eight-budget predicate. No necessary mathematical correction was
identified in the inspected proof.
