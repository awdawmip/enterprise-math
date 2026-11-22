# R5: exact primitive-43 contribution for every failure threshold

Date: 2026-11-22. Scope: independent portable research on the frozen R5 **true five-event scalar partition** model, not a new native-X6 claim. Status: **AUTHOR_EXACT_PROOF / EXACT_INTEGER_CROSSCHECKED / NOT_REVIEWED**. No formal CLAIM/RUN or Result/Review is asserted.

## Frozen source and model

Scientific input remains pinned to **enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15**. Continue from the verified portable m=1..4 period frontier **enterprise-math@0a9a5cb9d79e4200521ef50cfe90ee9ca82225e1**, especially its RESEARCH.md and m4 witness at order 43.

The available prices are the integers 214 through 314. A configuration is a vector of multiplicities a_p≥0 with total price N=Σ p a_p. Its failure event E_i(m) is Σ_{p∈S_i}a_p < m, for fixed positive integer m. The five supports are

- S0 = {214,215,216,217,218}
- S1 = {214,216,217,218,219,220,221}
- S2 = {215,216,217,218,219,220,221}
- S3 = {223,...,290}
- S4 = {296,...,312}.

Let F_m(q) count configurations satisfying at least one E_i. With D(q)=∏_{p=214}^{314}(1-q^p), write F_m(q)=R_m(q)/D(q). The exact inclusion-exclusion numerator is

R_m(q)=Σ_{∅≠I⊆{0,...,4}} (-1)^{|I|+1} Q_{I,m}(q) ∏_{p∈U_I}(1-q^p),

where U_I=∪_{i∈I}S_i and Q_{I,m} is the **finite polynomial** enumerating all a_p on U_I satisfying *every* joint event constraint in I. No independence assumption is used.

## Theorem: exact 43-divisibility phase classification

Let M_m(O_m(N)) be the minimal common coefficient period of the polynomial-in-N terms of degree at least 2 in the coefficient quasipolynomial of F_m, with the lower-degree remainder O_m(N). Then, for every integer m≥1,

**43 | M_m(O_m(N)) if and only if m mod 43 lies in {1,2,...,36}.**

Equivalently, the 43-component vanishes exactly when m mod 43 belongs to {0,37,38,39,40,41,42}. In those classes M_m(O_m(N)) is not divisible by 43.

This supplies a rigorous, infinite family of threshold-dependent **strict period contractions**. The universal denominator bound from the same 101 prices is L = 229746052653717600; therefore, for the seven zero classes,

M_m(O_m(N)) | L/43 = 5342931457063200.

In the other 36 classes, 43 is an obligatory factor, independently of what happens to other prime-power factors. The theorem determines precisely the 43-adic component; it does not assert the full minimum period for m≥5.

## Proof

Fix a primitive 43rd root ζ. Of 214,...,314, exactly the three prices 215,258,301 are divisible by 43. Accordingly D(q) has zero order 3 at q=ζ. The intersections of the five supports with {215,258,301} are respectively {215}, ∅, {215}, {258}, {301}. Every inclusion-exclusion term involving any event other than E1 contains a factor (1-q^p) with 43|p and therefore vanishes upon q=ζ. For I={1}, no denominator-cancellation factor vanishes, and the complete numerator value is exactly

R_m(ζ) = P(ζ) Q_m(ζ),
P(q)=∏_{p∈S1}(1-q^p),
Q_m(q)=Σ_{r=0}^{m-1} [u^r] ∏_{p∈S1}(1-u q^p)^{-1}.

The seven residues p mod 43 for S1 are A={42,1,2,3,4,5,6}. They are all nonzero and pairwise distinct. Thus P(ζ)≠0. Form the threshold generating series over K=Q(ζ):

G(t)=Σ_{m≥1}Q_m(ζ)t^{m-1}
    =1/[(1-t)∏_{a∈A}(1-ζ^a t)].

The eight linear factors in the denominator are *distinct factors* of 1-t^43. Therefore

G(t)=B(t)/(1-t^43),

where B(t)=(1-t^43)/[(1-t)∏_{a∈A}(1-ζ^a t)] is an **actual polynomial in K[t] of degree 43-8=35**. Coefficient comparison proves Q_{m+43}(ζ)=Q_m(ζ) for all m≥1 and Q_m(ζ)=0 for m in {37,38,39,40,41,42,43}.

For 1≤m≤36, work in the ring of integers Z[ζ] modulo the prime ideal (1-ζ), whose residue field is F_43. Here ζ≡1. Consequently,

Q_m(ζ) ≡ Σ_{r=0}^{m-1} binom(r+6,6)
       = binom(m+6,7)  (mod 1-ζ).

For m from 1 to 36, 7≤m+6≤42, so binom(m+6,7) is nonzero modulo 43: the numerator factorials contain no factor 43 and the denominator 7! is invertible. Thus Q_m(ζ)≠0 in all 36 classes. The periodicity above settles all positive m.

For primitive order 43, D has zero order 3. A nonzero R_m(ζ) therefore leaves an order-3 pole, which generates a nonzero degree-2 quasipolynomial Fourier coefficient with primitive 43rd-root frequency and forces 43 to divide every valid coefficient period modulo O_m(N). Conversely, when R_m(ζ)=0, the remaining pole has order at most 2 and does not affect the terms of degree ≥2. Every primitive 43rd root is a Galois conjugate, so the same cancellation holds at all primitive 43rd roots.

Every order d divisible by 43 other than d=43 is at least 86. In the interval 214,...,314 there are at most two multiples of any d≥86, so the denominator pole order is at most 2 and such orders cannot contribute degree-2 terms. Hence removing the order-43 pole removes **all** possible 43-divisibility from the coefficient period. This establishes both directions.

## Exact integer verification and prior-case crosscheck

VERIFY_ROOT43.py works in the cyclic integer ring Z[x]/(x^43-1), reducing to the primitive cyclotomic quotient via x^42=-(1+x+...+x^41). It computes complete homogeneous polynomial coefficients for the seven S1 prices, multiplies by P, and checks every phase and nonzero/zero decision for m=1,...,86. It also confirms primitive-root vectors for m and m+43 agree for all 43 phase classes.

One regression anchor against the previously saved m=4 result is the coefficient at 0-based cyclotomic coordinate 0 of R_4: **1**, matching the previous m4 certificate. Sample coordinate values of R_m are m=1:3, m=5:1, m=36:2, m=37:0, m=43:0. The proof above, rather than this finite experiment, is what establishes the infinite classification. Local Python 3 arbitrary-precision integer run: **ALL CHECKS PASS**.

Proof method: exact inclusion-exclusion, typed event-support incidence (retain overlap provenance), cyclotomic root filters and finite-field valuation. Signed phase information is necessary; aggregating to a positive-only BRC total would erase the decisive cancellation. No P000 or frozen input changes.

## Provenance, authority and next question

Inherited author-side m1..4 artifacts remain at commit 0a9a5cb9d79e4200521ef50cfe90ee9ca82225e1; this note neither rewrites their proof nor claims independent review of them. The theorem above is self-contained given the frozen sets, with author-side exact check and independent mathematical review pending.

The owner-inventory observation for this turn is r5-20261122-0941-current-inventory-once-v1; inspect its original terminal receipt rather than submit another inventory request. This portable research artifact is not a Task CLAIM, PROGRESS, Result or Review. Activity source association requires this conversation's actually authenticated Researcher/Activity and the current CAS contract.

**Next discriminating research question:** Classify the 37, 29 and 32 order contributions by the same support-incidence and finite-field method. Determine which other factors contract as m grows, and only then assemble the exact all-threshold O_m(N) minimum period. Investigate whether the seven 43-zero classes intersect other factor-zero classes, starting at m=37.

## Reproduce

From this directory under Python 3: run **python VERIFY_ROOT43.py**. It writes CERTIFICATE.json alongside itself and prints ALL CHECKS PASS. No floating-point operations or external packages.
