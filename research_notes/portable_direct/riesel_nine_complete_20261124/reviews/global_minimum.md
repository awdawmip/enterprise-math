# Shared-context check of the complete R3 cost-nine minimum

Research continuation v15. This is collaborative mathematical checking,
not independent project Review or formal acceptance.

Read `proof.md` and all of `verify_global_minimum.py`, inspected the
retained global certificate's family minima and native metadata, and
checked the related zero-W bounded-search code and the one-W minimum
argument. The full CRT enumeration and native execution were not rerun
for this review.

## 1. The canonical both-W enumeration is complete at the stated root level

The five families match the proved Q0-retaining root predicate. The first
family chooses an unordered five-prime subset of the nine period-seven
primes and permutes the five phases; this gives the same 15120 phase
descriptions as the ordered slot count. The other counts are 30,240,20,
504. With their respective independent signs, the signed totals are
483840,120,1920,80,4032, summing to 489992.

The t-phase to root-residue conversion uses exponent 16+72t, and the
w-phase conversion uses 16+18w, both correct for F_n=a^2*2^n-1.
The progression-index CRT uses (r-A3)*S3^(-1) modulo each distinct free
prime, giving a least nonnegative index in [0,M). All later positive R3
roots have index j0+kM with k>=0.

These canonical forms classify root existence, not every raw nine-prime
dictionary. The same-root replacement arguments in the both-W proof are
therefore essential and are properly cited in the minimum proof.

## 2. Later CRT lifts and incidental cost-eight roots are handled correctly

The code does not discard a progression because its first root happens
to satisfy the eight predicate. It minimizes all first indices in each
eligible family before applying the complete eight predicate to that
single family minimum. That minimum is exact cost nine in every relevant
family. Consequently every root in every progression of the family is
at least this already-admissible minimum, regardless of incidental
cost-eight first roots elsewhere in the family.

Only two structurally persistent cost-eight descriptions are excluded
beforehand: the old binary family, and the ternary descriptions whose two
free primes are both in D6. Their smaller covers persist along their
entire CRT progression. The code retains their counts. The three-C10
mod-five descriptions are not individually filtered: retaining them in
the unfiltered minimum search is valid because that entire family's
least first root is itself exact cost nine.

The complete eight predicate includes all three retained-prefix
alternatives and both zero-W alternatives. A single prime cannot supply
two requested phases in these Boolean tests because its root-sign
categories for distinct effective phases are disjoint. Thus the apparent
existential tests across phase slots enforce distinct prime use.

The recorded relevant first indices are 183162559016,11380571075,
282899156086651,9783969331088138390. The winner is the binary refinement
at index 11380571075. Its prime/residue data agree with the proof:
1153 -> 529, 3457 -> 2775, 816769 -> 737278.

## 3. The other W branches close the whole-R3 minimum

The one-W classification exhausts 307200 signed CRT descriptions. Its
least unfiltered first root has index 811311504227722 and itself fails
the complete eight predicate. In particular every one-W root is larger
than the new candidate, independently of any later lifts.

The zero-W code handles all 47 geometric patterns and all allowable
prime/sign choices. Its early option filter is valid: an index below the
initial bound cannot have a residue modulo a chosen prime at or above
that bound. Its partial update gives the least nonnegative extension y
of x modulo m, so pruning y at or above the current bound is exact.
At a complete leaf the while loop would inspect every later lift below
the current bound, including after a cost-eight first lift. The retained
certificate has no complete candidate below the supplied bound.

Because budget nine forces 5 and 13, and an exact-nine root has an
irredundant minimum supplement, the zero/one/two W split is exhaustive.
The combined result is the whole R3 exact-cost-nine minimum. It does not
determine the corresponding minimum on R1 or R2.

## 4. Full-integer lower bounds and native counts

For the 151-digit winner the script constructs and retains the full
integers at all 29 displayed witness indices. It checks proper selected
divisors, private status in the 29-prime dictionary, all 406 pairwise
gcds, and P-freeness of the nine external witnesses. The coprime-term
lemma therefore gives tau>=29 against every possible prime dictionary;
the P-free witnesses separately give delta_P>=9. The complete selected
cover, checked over its actual period 20160, supplies both upper bounds.

For the one-W comparison root the selected dictionary has 28 primes,
with old prime 113 omitted. Two distinct 28-term witness sets are checked:
the short set proves the unrestricted total lower bound, and the second
set additionally makes all nine external witnesses P-free. Hence its
exact pair (delta_P,tau)=(9,28) has the stated separate justification.

The native intervals are 2912 and 6512. Their observed-prime counts are
46 and 49. Therefore the recorded counts are consistent:

- 2912+6512=9424 one-step updates;
- 1456+3256=4712 two-step evaluations;
- 2912*46+6512*49=453040 independent prime readouts;
- 9424 joint readouts and 9424 exact recompositions;
- 9424*43=405232 fixed-coordinate comparisons.

The three witness sets contribute 29+28+28=85 entries and
406+378+378=1162 gcd checks. They are two roots and three sets, not three
roots or 85 distinct integer terms. The certificate actually retains
29 distinct terms for the winner and 34 distinct terms across the two
comparison-root sets. The proof's wording preserves that distinction.

Every native state is checked against the exact integer formula; the
two-step action has effect 4x+3 with unit weight and multiplicity. The
frozen module blob checks precede import. The witness intervals are
correctly distinguished from the complete covering periods.

No necessary mathematical or reporting correction was identified in the
inspected global-minimum proof, enumeration, dependencies, lower-bound
logic or native count interpretation.
