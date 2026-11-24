# Collaborative check of the complete zero-W budget-nine classification

Date: 2026-11-24, Asia/Hong_Kong. Existing researcher and Activity identities
are unchanged. This is shared-context mathematical checking, not independent
project Review or formal acceptance.

Inspected `nine_zero_v15/proof.md`, `verify_zero_nine.py`,
`verify_minimum_below_bound.py`, the saved bounded-minimum certificate
metadata, and the exact inherited five-class lemma in the v13 prefix proof.
No additional large computation or native execution was performed for this
check.

## 1. Divisibility-by-three split

The inherited five-class lemma is applied at its actual strength: on the
v=0 and v=1 modulo-three fibers, all eligible channels other than the
omitted W prime have restricted period at least six. The affine change
modulo 35 preserves the row/column incidence structure.

If a 3-divisible class is used, irredundancy forces at least one class in
each of the three v-phase groups. A common cover on an empty group could
otherwise be transported to every phase by CRT, making all phase-specific
classes redundant. The resulting inequalities force four common classes
and one private class in each phase. The five-class lemma then makes the
four common classes the four distinct Z rows.

For the last row, a single private class covering every lift of its two
or three columns must have restricted period dividing seven. Restricted
period one is unavailable: the original f=3 inventory is
{19,73,37,109}; 19 and 73 are omitted and 37 and 109 have root residue
zero on R3. Hence each private channel has original f=21. This gives
exactly type I.

## 2. Forcing at least three Z channels

The all-order gcd-column bounds correctly retain period-35 point classes
with lift period one.

- At m=0, the exceptional two f10 and two f8 channels and the generic
  3/2 mass bound give total 51/4<13.
- At m=1, the correct upper bound is the largest six possible
  contributions: two f10, three f14, and one f8, totaling
  17/2+r/8<r for r=10 or 11. This does not incorrectly force an f8
  choice into every cover.
- At m=2, residual sizes eight and nine are excluded by 5*(3/2).
  For size seven, at least four contributions must exceed one. Only
  the two f10 channels and two nonduplicate f14 phases on the unique
  large row can do so. Once those f14 phases cover that row, the other
  three classes have mass at most three on four remaining points.

Thus m is three or four without any prime-magnitude cutoff.

## 3. Remaining finite geometries

For m=3, two large rows cannot be covered with only three available J
primes. A large and small row force two opposite J phases on the large
row; two U point classes are then necessary on the small row, because a
fourth J is unavailable. With two small rows, equality requires each of
four classes to have mass one. The only periods attaining that mass are
10,14,35. Their edges are exactly the row, column and parity directions
of the eight-vertex cube. Its nine perfect matchings lose the pure T and
pure J cases to the two-prime and three-prime inventories, leaving the
stated seven matchings.

For m=4, the common/point distinction is exhaustive because gcd(f,35)
has only four possibilities. With periods coprime to three, three common
classes have the irredundant pattern 2,4,4. With one point class, the two
common classes would already cover the entire row. With two point
classes, a three-point row is impossible and a two-point row gives
precisely VI or VII. Three point classes give V on a large row or VIII
on a small row. The inventories J,L,U,S implement exactly these induced
periods. No further period can attain the needed two- or three-class
coverage.

The eight displayed phase-count formulas evaluate to
7200,114048,336384,14400,95040,12096,48384,48384, whose sum is 675936.
Distinct phase slots and injective prime assignments justify the
falling-factorial counts. All seven free primes are coprime to the fixed
modulus, giving 128 sign descriptions per phase dictionary.

## 4. Exact-cost realization and bounded minimization

Setting unselected budget-eight coordinates to zero defeats every
retained-W eight-cover: no B8 or D6 member is selected, and no more than
two C10 members are selected. The zero-W eight predicate is likewise
excluded in every type for the stated reasons: three Z rows, too few
J/U channels, or a three-point missing row. The exact-cost-nine
realizations therefore use the complete eight predicate, including both
W alternatives, rather than dictionary irredundancy alone.

The bounded-minimum script imposes congruences on the nonnegative R3
index j. A single-coordinate least residue at least the bound cannot
occur below it. Each partial CRT lift is y=x+k*M with k>=0, so pruning
y at or above the current bound preserves every smaller completion.
At a complete description the loop checks every lift below the bound,
including later lifts after a cost-eight first root. Reusing the complete
eight predicate by the root index is valid across descriptions.

The saved certificate inspected here has strict bound 11380571075,
reports all 47 geometries processed, and has zero complete ordinary-root
candidates below that bound. Its scope is the full classified zero-W
branch below the stated index; it does not by itself assert a global
zero-W minimum above that bound.

No necessary mathematical correction was found. The only requested
clarification was to spell out the f=3 inventory and its fixed exclusions,
including both 37 and 109, at the period-one step.
