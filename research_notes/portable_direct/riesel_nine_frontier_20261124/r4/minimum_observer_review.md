# Collaborative check of the R4 minimum and thirteen-coordinate observer

Research continuation, 2026-11-24; Researcher `EM-DIRECT-970E1C`, Activity
`RA-D2EC212845B63844081F9A14`. This is shared-context mathematical checking,
not independent project Review or formal acceptance.

Inspected: `tail_proof.md`, `observer_proof.md`, `verify_r4_nine.py`, the
prime-inventory metadata, and the saved native `r4_nine_certificate.json`.
The complete 4392-start calculation and native execution were not rerun
for this review. Small certificate metadata and cross-file comparisons
were performed.

## 1. The global minimum scope is justified

The complete R4 prefix reduction is valid. The v14 basic-pair theorem forces
5 and 13. The complete one-W theorem would require all four inactive Z
coordinates, so exactly one of 19 and 73 is impossible. For zero W,
restrict to v=0 and v=1 modulo three. A 3-divisible f channel hits at most
one of them, with relative capacity at most 3/13. A channel with 3 not
dividing f crosses both; after the common f=7,8,10 channels are killed,
the four gcd-column combined bounds are 2/11,5/26,3/13,2/13. Each is at
most 3/13. Seven channels therefore supply at most 21/13 of the required
mass two. This forces Q0 in every nine-prime R4 dictionary.

The four tail dictionary types are exhausted by `tail_proof.md`. The
enumerator uses exactly their prime permutations, phase slots, fixed tails,
and independent root signs. It computes 120+6+6+60 phase dictionaries and
3840+24+48+480=4392 signed CRT starts. Each `crt` result is the least
nonnegative representative modulo its full modulus; because it lies in
the positive A4 residue class, it is strictly positive. All later positive
roots of a description are larger. Taking the smallest first root among
all descriptions consequently gives the minimum over the complete class.

The RRR dictionary type is explicitly included despite contributing no
new root beyond RR. Inclusion does not corrupt minimization; every such
progression is contained in one of the RR progressions. The certificate's
four family minima have respectively 394,371,395,378 digits. The 371-digit
minimum agrees exactly with the earlier Q7-family calculation on R4, now
upgraded to the whole R4 exact-cost-nine class by the full classification.
Its R4 progression index is 75240521932528635.

This 371-digit R4 root is distinct from the 156-digit Q7-family minimum
on the larger R3 fiber; the two earlier conditional minima have different
ambient families.

This is a global minimum on R4, not on the larger R3 cost-nine class.

## 2. The complete observer and density have the correct scope

The root predicates use the three disjoint prime groups G7, R12, H20.
At each prime their required sign pairs are disjoint, which the script
checks before counting. The inclusion-exclusion count is independently
matched to a weighted mask count. The union numerator is
M9 minus the product of the three false-event counts; it counts roots
once even when several dictionary descriptions apply. The absorbed RRR
type is correctly absent from the root union.

The inventory's verified-root list contains all five G primes, all three
R primes, all five H primes, X864, and the primes of the selected old and
fixed dictionaries. Thus the script's uses of prime orders and the
ten-cover support do not treat an uncertified integer as a prime. The
new H factorization values are recomputed cyclotomically, multiplied
exactly, and checked against exact base-two orders. Their maximum order
is 720.

## 3. All thirteen finite 9/10 witness pairs are valid

For each target observer prime the script makes exactly one group predicate
true and then changes only the target residue to zero. In the R group,
another R prime supplies phase eight while the target supplies zero. In
the H group, the target and two companions supply all three colors. In
the G group, all five primes supply all five colors. All other groups are
false; the common single R phase-eight coordinate cannot itself make the
R predicate true. Losing the target destroys the sole true group.

The common ten-cover has Q7, one permanent R prime at w=8 modulo twelve,
X864 at w=12 modulo twenty-four, and one ordinary prime divisor of C864
at w=0 modulo twenty-four. These last two channels partition the only
remaining w=0 modulo twelve holes. The CRT uses a residue modulo the whole
C864, which implies the desired residue at its least prime divisor; C864
is not counted as prime. The complete product identity, the coprimality
with X864 and with the old/observer moduli, and the exact-order property
for every prime divisor of C864 justify this ordinary two-prime support.

The permanent R coordinate is chosen different from a target in R. No
conflicting residue is imposed at that coordinate. Therefore both roots
in every pair keep the same common ten-cover. The on-root has cost nine
by the complete predicate; the off-root has cost greater than nine and
at most ten, so exactly ten. The script constructs thirteen distinct
target cases and compares their common CRT moduli, rather than merely
postulating Boolean residue vectors.

The reported common 87 named primes consist of the fixed 74, the twelve
non-target observer primes, and X864. The target is excluded. The
additional common modulus C864 is separately labeled as composite or
unfactored. This accounting is correct.

The arbitrary-N necessity proof in `observer_proof.md` correctly extends
the assignments: take the lcm of S4,N,M9/q,X*ell and then change q by CRT.
When q does not divide N, all lcm factors are coprime to q. The constructed
roots preserve the common finite ten-cover and every other observer
coordinate. Equal root residues then give equal full future trajectories.
Sufficiency for trajectories uses the observed first term to recover a^2
modulo the odd M9; every category is a sign pair, so the square suffices.
Thus the exact condition M9|N and sharp maximum order 720 follow.

## 4. Total-cost and native certificate consistency

The compact 371-digit minimum has a displayed 29-prime full cover, checked
over its complete 60480 period. Its 29 retained positive-index full terms
have 406 pairwise gcds equal to one, forcing every possible cover to use
at least 29 primes. Therefore tau=29 and delta_P=9 follow independently
of the minimum-scope classification.

The saved native certificate reports PASS with native execution enabled.
The greatest witness index 1472 gives 1472 one-step updates and 736
two-step evaluations. Its 87 observed primes give 1472*87=128064
independent quotient/remainder readouts. The 74 fixed-coordinate
comparisons give 1472*74=108928 comparisons. Joint readout and integer
recomposition counts are each 1472. These agree with both code and
certificate. The native interval is expressly a witness-production
interval; the separate full-period upper check supplies coverage for the
whole infinite sequence.

No necessary mathematical correction was identified in the inspected
minimum, enumeration, observer, common ten-cover, or certificate scope.

## 5. The additional 26880 upper bound

The proposed upper bound for the complete ninth-budget observer on R1,
R2, and R3 is valid as well. An inclusion-minimal supplement of size at
most nine contains 5 and 13 by the new basic-pair theorem. Its remaining
s<=7 primes cover the thirteen progressions n=8+12r+420t, with r in A.
Each remaining prime has a private point in at least one such progression.

If its effective period e=ord_q(2^420) exceeded 2^(s−1), the next
2^(s−1) positions after a private point would all be covered by the
other at most s−1 congruence classes. The inherited Crittenden–Vanden
Eynden interval theorem would make these other classes cover the full
progression, contradicting the private point. Therefore e<=64 and
ord_q(2)=e*gcd(ord_q(2),420)<=26880.

Only finitely many odd primes have e<=64, because each divides one of
the finite list 2^(420e)−1. Observing all their root residues decides the
existence of a supplement of the required size and gives the upper bound.
All roots of these fibers already have composite terms, so a prime divisor
detected by a congruence is proper; no additional comparison with the root's
size is necessary. The sign-pair argument gives the same sufficient bound
for complete future residue observations. The statement does not assert
optimality of 26880 or extend the nine-budget basic-pair forcing theorem
to larger budgets.
