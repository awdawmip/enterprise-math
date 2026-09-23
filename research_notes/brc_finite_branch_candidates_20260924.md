# BRC finite target-branch candidate theorem

Status: `PROVED_DERIVATION / PORTABLE_RESEARCH_NOTE / NOT_A_RESULT / NOT_A_REVIEW / NOT_A_SOURCE_CHECKPOINT / UNREVIEWED`

Stable logical lane: `chatgpt-research-hourly-enterprise-math-20260923`.

Task context: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`.

This note does not allocate a new Researcher identity and does not change formal D24/UR ownership. Control issue #1511 remains the gate for lawful successor-session `continuation_prepare -> CLAIM -> OPEN`. The present unit is portable auxiliary BRC research only.

## 1. Consumed branch-gain cocycle

For a finite exponent vector `m`, the exact generic and target-branch weights are

`W_infty(m)=sum_j m_j(2j+1)`,

`W_p(m)=W_infty(m)-Gamma_p(m)`.

The preceding cocycle theorem gives

`Gamma_p(m)=E_p(m)+D_p(m)-C_p(m)+F_p(m)`,

where

- `E_p(m)=sum_j m_j 1_((p-1)|2j)` is harmonic-endpoint credit;
- `D_p(m)=sum_j m_j v_p(j)` is denominator credit;
- `C_p(m)=sum_j m_j v_p(1+4^j)` is coefficient-cancellation debit;
- `F_p(m)=sum_j v_p(m_j!)` is factorial credit.

For the uniform sufficient carrier, only branches with `Gamma_p(m)>0` can make a monomial appear earlier than the generic branch. This note identifies a finite exact set containing every such target prime.

## 2. Credit-prime candidate set

Let

`Supp(m)={j: m_j>0}`

and

`M(m)=max_j m_j`.

Define the finite target-prime candidate set `P_credit(m)` as the union of three provenance-labelled sets:

### Endpoint candidates

`P_E(m)={ target primes p : (p-1)|2j for some j in Supp(m) }`.

Equivalently, for each occupied port `j`, an endpoint candidate has

`p=d+1`

for some divisor `d|2j`, with `p` prime and `p == 13 or 19 (mod24)`.

### Denominator candidates

`P_D(m)={ target primes p : p|j for some j in Supp(m) }`.

These are target-congruence prime divisors of occupied port indices.

### Factorial candidates

`P_F(m)={ target primes p : p<=M(m) }`.

These are exactly the target primes for which at least one multiplicity factorial can have positive p-adic valuation.

Then

`P_credit(m)=P_E(m) union P_D(m) union P_F(m)`.

This set is finite and can be generated directly from divisor data of the occupied ports plus target primes up to the largest multiplicity.

## 3. Finite branch-candidate theorem

### Theorem

For every finite exponent vector `m` and every target prime

`p notin P_credit(m)`,

one has

`Gamma_p(m)=-C_p(m)<=0`.

Consequently

`max(0, sup_(target p) Gamma_p(m))`

is exactly

`max(0, max_(p in P_credit(m)) Gamma_p(m))`.

Therefore no target prime outside `P_credit(m)` can enlarge the uniform sufficient carrier at this monomial.

### Proof

Take a target prime `p` outside `P_credit(m)`.

Because `p notin P_E(m)`, no occupied port is a harmonic endpoint, so

`E_p(m)=0`.

Because `p notin P_D(m)`, `p` divides no occupied port index, so

`D_p(m)=0`.

Because `p notin P_F(m)`, every multiplicity satisfies `m_j<p`, hence

`v_p(m_j!)=0`

for all `j`, and therefore

`F_p(m)=0`.

The cocycle reduces to

`Gamma_p(m)=-C_p(m)`.

Since coefficient-cancellation valuation is nonnegative,

`Gamma_p(m)<=0`.

Such a branch can coincide with the generic carrier (`C=0`) or prune it (`C>0`), but it cannot make the monomial visible earlier. Therefore it cannot beat the generic branch in the uniform union. Taking the maximum over target primes may be restricted to `P_credit(m)`, with `0` representing the generic branch. QED.

## 4. Exact uniform first-visibility formula

Define the best positive branch gain

`Gamma_*(m)=max(0, max_(p in P_credit(m)) Gamma_p(m))`.

Then the uniform sufficient carrier first sees the monomial at the exact horizon

`B_unif(m)=W_infty(m)+1-Gamma_*(m)`.

Equivalently,

`m is retained at horizon N`

iff

`B_unif(m)<=N`.

Thus uniform branch-set generation can be reorganized monomial-first:

1. construct an exponent vector `m` with its generic weight;
2. generate only the finite credit-prime set `P_credit(m)`;
3. evaluate the exact typed cocycle on those candidates;
4. keep the largest positive gain.

No other target prime can improve the uniform threshold.

## 5. Explicit finite bound

Every endpoint candidate satisfies

`p-1<=2j`

for some occupied `j`, hence

`p<=2j+1`.

Every denominator candidate satisfies

`p<=j`.

Every factorial candidate satisfies

`p<=M(m)`.

Therefore every positive-gain target prime lies below the monomial-specific bound

`B(m)=max( M(m), max_(j in Supp(m))(2j+1) )`.

So a simpler, less selective safe scan is

`target primes p<=B(m)`.

The divisor-generated `P_credit(m)` is usually much smaller and is exact for the positive-gain observer.

This bound is independent of the requested precision horizon `N`; it is determined by the monomial itself.

## 6. Why coefficient-cancellation primes are not candidate generators

A prime may divide some source coefficient `1+4^j` even when it is much larger than every port index and multiplicity. Such a prime can give

`C_p(m)>0`.

But coefficient cancellation enters the cocycle with a negative sign. If the same prime carries no endpoint, denominator, or factorial credit, then

`Gamma_p(m)=-C_p(m)<0`.

Therefore coefficient-cancellation provenance must still be evaluated for any *credit candidate* branch, because it can reduce or destroy that branch's advantage; however cancellation by itself never creates a new uniform-union candidate.

This distinction is an observer-dependent BRC quotient:

- for `UNIFORM_EARLIEST_VISIBILITY`, cancellation-only primes can be safely omitted from candidate generation;
- for `EXACT_PER_PRIME_SUPPORT` or provenance reconstruction, they cannot be omitted because they may prune the generic carrier.

## 7. Interaction with earlier large-prime cutoff

The earlier horizon theorem said that at precision `N`, target primes `p>N` cannot enlarge the uniform union.

The present theorem is orthogonal and often sharper. For a particular monomial, positive gain is possible only for

`p in P_credit(m)`

and hence only for

`p<=B(m)`.

Thus at fixed horizon one may safely intersect the two filters:

`p <= min(N, B(m))`

and then retain only the divisor/factorial-generated credit candidates inside that bound.

This replaces a scan over all target primes below the horizon by a finite arithmetic candidate extraction attached to the monomial's own provenance.

## 8. Examples

### `m=e_6`

The endpoint condition for `p=13` holds because `12|12`, so

`P_credit(e_6)={13}`.

No other target branch can make `e_6` appear earlier than generic.

### `m=e_13`

The denominator port contributes candidate `p=13`, again giving

`P_credit(e_13)={13}`.

### `m=19 e_1`

There are no endpoint or denominator candidates, but factorial credit is possible for target primes at most `19`, giving

`P_credit(19e_1)={13,19}`.

The exact cocycle then decides which branch gives the earliest uniform appearance.

### `m=e_3`

There is no target endpoint, denominator, or factorial credit candidate, so

`P_credit(e_3)=empty`.

The class-13 branch `p=13` does see a source-coefficient cancellation at this port, but that is a debit: it delays the branch and cannot beat generic. Hence the generic branch is automatically optimal for uniform first visibility.

## 9. Exact falsification

Checker:

`research_checks/check_brc_finite_branch_candidates_20260924.py`

Checker commit:

`8b16863c7c753ed7012a92625e25660bab7cb3d4`.

The checker was executed locally before publication. It generates random finite exponent vectors and compares the maximum exact gain over all target primes below the provable monomial-specific bound against the maximum over `P_credit(m)`. It additionally probes larger target primes and verifies they never have positive gain.

Regression summary:

- exponent vectors checked: `3000`;
- outside-candidate target-prime checks: `299810`;
- vectors where `P_credit(m)` was a strict reduction of the simple bounded target-prime set: `2673`;
- failures: `0`.

Finite computation is falsification/regression only. The theorem is the exact vanishing of all three positive credit mechanisms outside `P_credit(m)`.

## 10. BRC interpretation

The theorem gives a safe branch-selection quotient only for the observer

`UNIFORM_EARLIEST_VISIBILITY`.

The raw carrier still keeps four mechanism types `(E,D,C,F)`. Candidate generation uses only the three positive-credit provenance channels `(E,D,F)`; the negative cancellation channel `C` remains attached to each candidate and must be evaluated before a branch can be declared dominant.

This is stronger than treating all target primes as an undifferentiated list and stronger than a mere numerical cutoff. The candidate set is generated from the monomial's own endpoint divisors, port prime factors, and multiplicity range.

## 11. Do not repeat / next

Do not scan every target prime for each monomial merely to discover which branches could improve the uniform union. Positive-gain candidates now have an exact finite generator.

If formal D24 control remains blocked, the next nonredundant auxiliary question is **candidate dominance** inside `P_credit(m)`: derive arithmetic conditions under which one candidate branch can be discarded because another has `Gamma_q(m)>=Gamma_p(m)` on a whole family of exponent vectors, without erasing cancellation provenance needed for exact-per-prime observers.

If #1511 gains a deployed lossless rollover/disposition operation, stop auxiliary compiler work and resume the Source-native D24 frontier through the lawful successor identity, preserving the existing Source checkpoint and native frontier exactly.
