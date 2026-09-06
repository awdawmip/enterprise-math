# X6 triadic interaction V19: exact rational pair-factorization criterion and finite valuation torsion

Status: `FREE_RESEARCH / EXACT PRIME-VALUATION DERIVATION + INTEGER-LATTICE CLASSIFICATION / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_TRIADIC_INTERACTION_DEFECT_V18_20260906.md`;
- Weighted-BRC Foundation rule `RATIONAL_GAUGE_HAS_INTEGER_COORDINATES`;
- `src/enterprise_math/brc_rational_holonomy.py` prime-valuation representation.
Checker: `experiments/x6_triadic_rational_pair_factorization_v19_20260906/check_triadic_rational_pair_factorization.py`.

## 1. Question left by V18

V18 defines the pair-shadow map

`P:Z^20 -> Z^15`

from 20 triad-type multiplicities to 15 pair co-occurrence counts and proves:

- `rank(P)=15`;
- `ker(P)` is five-dimensional;
- the fifteen perfect-matching 4<->4 trades generate the full integer pair-shadow defect lattice;
- for positive **real** triad weights, all trade ratios equal one iff the triad log-weight is pair-factorizable over real pair potentials.

The remaining exact arithmetic question is:

> if all triad weights are positive rationals and every V18 trade ratio is exactly one, do positive rational pair factors necessarily exist?

No. There is a finite prime-valuation obstruction after the five-dimensional continuous trade defect has vanished.

## 2. Exact rational problem in prime coordinates

Let `w_S in Q_{>0}` for every three-axis type `S`.

A rational pair factorization means finding unique candidates

`q_e in Q_{>0}`, `e` a two-axis pair,

such that

`w_S = product_{e subset S, |e|=2} q_e`

for all 20 triads.

Use the existing BRC rational prime-valuation carrier. For every prime `p` appearing in the finite family of weights define

`nu_S(p)=v_p(w_S) in Z`,

`lambda_e(p)=v_p(q_e) in Z`.

Then rational pair factorization is equivalent, prime by prime, to the integer incidence system

`nu = P^T lambda`.

Because `P^T` has full column rank 15, any pair-valuation solution is unique over Q and hence any rational pair factorization, if it exists, is unique.

## 3. Trade-flatness is the rational-row-space condition

For each perfect matching M let `v_M in ker(P)` be the V18 4<->4 trade.

Define the positive rational trade ratio

`H_M(w)=product_{S in T_M^+}w_S / product_{S in T_M^-}w_S`.

Then

`H_M(w)=1 for every M`

iff for every prime p

`v_M dot nu(p)=0 for every M`.

Since the V18 trades span `ker(P)` over Q, this is equivalent to

`nu(p) in im_Q(P^T)`.

Thus the trade equations are exactly the **continuous/rational-row-space** compatibility equations. They do not yet impose the integrality of the unique pair valuations.

## 4. Closed formula for the unique rational pair valuations

Fix one prime and suppress `(p)`.

For the integral triad valuation vector `nu`, define:

`T = sum_S nu_S`,

`R_i = sum_{S contains i} nu_S`,

`t_ij = sum_{S contains {i,j}} nu_S`.

Suppose first that `nu=P^T lambda` over Q. Let

`s_i=sum_{j!=i}lambda_ij`,

`L=sum_{i<j}lambda_ij`.

Each pair occurs in four triads, hence

`T=4L`.

In `R_i`, an incident pair occurs four times and a nonincident pair occurs once, so

`R_i=3s_i+L`.

In `t_ij`, the pair `ij` occurs four times and the remaining incident pairs contribute once each, so

`t_ij=2lambda_ij+s_i+s_j`.

Solving gives the exact inverse formula

`lambda_ij = (6 t_ij - 2 R_i - 2 R_j + T)/12`.

Therefore, whenever the trade-flatness equations put `nu` in `im_Q(P^T)`, the displayed values are the **unique** rational pair valuations.

## 5. Exact positive-rational factorization criterion

A family `w_S in Q_{>0}` has a positive-rational pair factorization iff BOTH conditions hold:

### Gate A — pure-triadic defect vanishes

For every V18 perfect-matching trade M,

`H_M(w)=1`.

Equivalently, primewise `nu(p)` lies in the rational row space of `P^T`.

### Gate B — arithmetic root defect vanishes

For every relevant prime p and every pair `{i,j}`,

`6 t_ij(p) - 2 R_i(p) - 2 R_j(p) + T(p)`

is divisible by `12`.

Equivalently every unique rational pair valuation `lambda_ij(p)` is an integer.

When the gates pass, reconstruct uniquely

`q_ij = product_p p^(lambda_ij(p))`.

This is finite and exact. No logarithm or floating-point root is required.

## 6. Canonical arithmetic defect state

After Gate A passes, define

`delta_p(nu) = (lambda_ij(p) mod Z)_{15}`

as an element of `(Q/Z)^15`.

This fractional pair-valuation residue is canonical: it is obtained from the unique rational inverse and does not depend on a chosen Smith basis.

`delta_p=0`

iff the p-part admits integer pair valuations.

Only finitely many primes occur, so the complete rational root defect is the finite-support family

`DELTA_RAT(w)={delta_p}_p`.

It is an arithmetic observer, not a physical energy or extra native state.

## 7. Exact torsion group after the five-dimensional trade defect is removed

Let

`A=P^T: Z^15 -> Z^20`.

Its rational image has rank 15. Let

`sat(im A)=im_Q(A) intersect Z^20`.

Trade-flat integral valuation vectors are exactly the elements of this saturated lattice.

The residual arithmetic obstruction group is therefore

`T_pair = sat(im A) / im A`.

Its Smith invariant factors are

`1,1,1,1,1,1,1,1,1,1,2,2,2,2,6`.

Hence

`T_pair ~= (Z/2)^4 direct_sum Z/6`,

with total order

`|T_pair|=96`.

Equivalently the complete cokernel is

`Z^20 / P^T Z^15 ~= Z^5 direct_sum (Z/2)^4 direct_sum Z/6`.

The free `Z^5` part is the integer shadow of V18's five-dimensional pure-triadic interaction sector. The finite torsion is precisely what remains after all V18 trade equations vanish.

### Exact certificate for the invariant factors

The checker uses no floating point and no external CAS dependency.

It verifies:

- `rank_Q(A)=15`;
- `rank_F2(A)=10`, so exactly five Smith factors are divisible by 2;
- `rank_F3(A)=14`, so exactly one Smith factor is divisible by 3;
- one explicit 15x15 maximal minor, using triad rows

`0,1,2,3,4,5,6,7,8,9,10,11,12,13,16`,

has determinant `96`.

The product of the nonzero Smith factors is the gcd of maximal minors. The mod-2/mod-3 rank drops force it to be divisible by `2^5*3=96`, while the explicit minor forces it to divide 96. Hence the product is exactly 96.

Combined with the divisibility ordering of Smith factors, the only possibility is

`1^10, 2^4, 6`.

## 8. Cubic-root obstruction: trade-flat but not rational-pair-factorizable

Fix a prime p and set

`w_S=p`

for every one of the 20 triad types.

Every perfect-matching trade has four triads on each side, so

`H_M=1`

for all M.

The valuation vector is `nu_S=1`. The inverse formula gives

`lambda_ij=1/3`

for every pair.

Thus pair factors exist over positive reals/algebraic numbers as `p^(1/3)`, but no positive rational pair factorization exists.

The torsion class has exact order 3.

## 9. Square-root obstruction

Fix axis 1 and prime p. Set

`w_S=p` iff `1 in S`,

and `w_S=1` otherwise.

Again all V18 trade ratios equal one.

The unique pair valuations are

`lambda_1j=1/2` for `j!=1`,

and zero on every pair not incident to axis 1.

So the family requires square roots and has no positive rational pair factorization.

The torsion class has exact order 2.

## 10. Order-six obstruction

Multiply the preceding cubic and square examples. Primewise the unique pair valuation is

- `5/6` on the five pairs incident to the selected axis;
- `1/3` on the other ten pairs.

The least positive integer clearing every denominator is 6.

Thus the residual arithmetic obstruction can realize order 6, as required by the `Z/6` Smith factor.

## 11. Relation to BRC rational gauge tools

This stage directly reuses the current Foundation principle:

`RATIONAL_GAUGE_HAS_INTEGER_COORDINATES`.

The appropriate primitive arithmetic carrier is finite prime valuation data, exactly as in `brc_rational_holonomy.py`.

The V18 real/log projector and trade ratios remain useful first gates, but they do not replace integer valuation semantics. In particular:

`ZERO_REAL_TRIADIC_DEFECT != EXACT_RATIONAL_PAIR_FACTORIZATION`.

The residual 96-state torsion class is the exact information erased by moving from rational valuations to unrestricted real logarithmic pair potentials after trade-flatness.

This is a specialization of existing BRC valuation methodology, not a new top-level tool family.

## 12. Observer hierarchy for interaction weights

The interaction-weight hierarchy is now:

1. exact triad weights `w_S in Q_{>0}`;
2. finite prime valuations `nu_S(p)`;
3. V18 pure-triadic trade defect / projector;
4. if trade-flat: finite rational-root torsion `delta_p`;
5. if torsion also vanishes: unique rational pair weights `q_ij`;
6. optional real/log pair potentials as a downstream readout.

Each downward step loses information and is operation-safe only for an observer that does not ask for the erased arithmetic/provenance data.

## 13. Current frontier

Closed:

- exact primewise inverse formula;
- necessary-and-sufficient positive-rational pair-factorization criterion;
- uniqueness of rational pair factors;
- canonical fractional valuation defect;
- residual torsion group `(Z/2)^4 direct_sum Z/6`, order 96;
- explicit order-2, order-3 and order-6 witnesses.

Remaining higher-level issue:

pair-factorizable laws, even exact rational ones, still cannot distinguish V18 trade-related decomposition branches because they depend only on pair shadows. Route selection requires a genuine component in the five-dimensional triadic interaction sector or richer history/context.

The next constructive target is therefore to classify the minimal S6-covariant **non-pairwise triad interaction law** and its coupling to multi-Cell/event dynamics, rather than adding more pair potentials.

No Foundation promotion, physical interaction-energy interpretation or external novelty claim is made.
