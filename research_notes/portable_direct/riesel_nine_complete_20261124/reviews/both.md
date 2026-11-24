# Collaborative check of the complete Q0-retaining ninth-budget predicate

2026-11-24, existing Researcher `EM-DIRECT-970E1C`, Activity
`RA-D2EC212845B63844081F9A14`. This is shared-context mathematical checking,
not independent project Review or formal acceptance.

Inspected `nine_both_v15/proof.md`, `verify_both_tail.py`, and the saved
certificate structure. No large calculation was rerun for this review.

## All-period scope

The no-A argument treats all effective periods through gcd-column masses.
For a fixed gcd(h,L), the compatible-lift mass decreases with h/gcd(h,L),
so considering the smallest allowed period in that column is a valid
universal upper bound. The positive deleted-row cases and the m=0 fixed
R/U cases retain the period-35 point channels; there is no lost full-lift
case or implicit prime-size cutoff. The special U-only period-ten argument
correctly uses all six (parity, occupied mod-five column) categories.

The private-point covering-interval lemma applies on an actual occupied
progression modulo 35. If a selected class has effective period greater
than 2^(t-1), the next 2^(t-1) progression positions are covered entirely
by the other at most t-1 classes. Crittenden--Vanden Eynden therefore
contradicts the original private point. This gives the stated finite
effective-period candidate set even when the original periods are
arbitrarily large. A private point can be moved to a positive position by
the common periodicity.

## Finite geometric exhaustion

The recursive enumeration is complete. At a remainder with k slots, any
successful completion contains a class with at least ceil(|D|/k) remaining
hits. Branching over every such class permits at least one ordering of
every successful set. It rejects repeated rows, checks all candidates
through their full common period, and tests private points against the
full original residual set. Stopping at a covered remainder loses only
redundant extensions, which are irrelevant to the inclusion-minimal
geometries. Thus its nine four-slot B2 geometries and five three-slot B4
geometries are exact finite consequences of the universal period lemma.

The accompanying three-slot reasoning is also consistent: with no
period-two channel, each class needs mass at least 3/13 and hence only
periods 3,4,5,7 remain. A period-four class requires two period-five
classes, which leave an entire progression that one quarter cannot fill.
A period-seven class requires the two largest columns, whose three
remaining points occupy three distinct modulo-seven rows. Mixed period
three/five triples leave whole lifts uncovered. The surviving triples
are the stated pure ternary or occupied-column triples.

## Same-root replacements and claim scope

After the fixed A channel is selected, inserting U means restricting to
even z. The split ternary geometry 3,3,6,6 becomes three t-period-three
classes after dropping its odd split member. The split mod-five geometry
5,5,10,10 becomes three t-period-five classes. The four period-four
classes reduce to two t-period-two classes. The original three-class
geometries restrict without adding a fourth free class. In every case
the total remains at most five tails including A,U.

In the t-period-three triple, replacing the phase-one member by the fixed
R channel preserves the same root and leaves two E5 primes at phases zero
and two. The inventory correctly includes D6 as well as the new R12
primes; likewise the mod-five inventory includes C10 as well as H20.
These steps prove the five canonical root-existence families, not a list
of every original dictionary. The proof consistently states that scope.

The phase counts 15120+30+240+20+504=15914 and the signed counts
483840+120+1920+80+4032=489992 are consistent with the slot assignments.
The old binary family and incidental eight-covers are expressly retained;
exact cost nine is obtained only after applying the complete v13
eight-budget exclusion. The maximum order 720 belongs to this branch,
while the complete all-R3 observer must also include the zero-W branch.

No necessary correction was identified in the inspected universal
reduction, finite exhaustive algorithm, same-root replacements, inventory
translation, or stated scope.
