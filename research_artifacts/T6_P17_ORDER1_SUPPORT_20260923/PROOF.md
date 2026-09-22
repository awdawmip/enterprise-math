# Exact p17/order1/r1 affine exclusion

Researcher-ID: EM-DIRECT-3AD825 / TASK_RESEARCH
Scope: direct-user finite support problem. The existing T6 Task remains awaiting
Driver review; no old CLAIM or Acceptance is asserted. This proof does not use
the truth of the earlier p19 conclusion as a premise.

## Frozen mathematical question

Let w_j=17j-1, j=1,...,16. Is there an integer vector u such that

    sum_j u_j j^(-k) = -18^(-k) (mod 17^k),  k=1,...,6,
    sum_j w_j max(u_j,0) <= 2026,
    sum_j w_j max(-u_j,0) <= 2331?

The positive vertical atom has denominator306 and exponent305. Its addition
to u gives side totals at most2331. This is a necessary local relaxation of
equal BRC shape observers H0,...,H6, not a sufficient full collision criterion.
The whole signed multiplicity vector, a=e+1 denominators and both side budgets
are retained. The16-dimensional coefficient lattice is not native space;
P000 and the Heartbeat World's6+1 dimensions are unchanged.

## Input is independently checkable

The exact q0 lattice basis comes from the pinned p17_q0_certificate.json,
SHA256 fdf0b060d47bccd5b2a5095dc4b72d13b68476f49494eb4435b0b50dd30c65f6.
Both implementations recheck its16-dimensional determinant17^21, all six
homogeneous congruences and the unit6x6 Vandermonde minor modulo17. The latter
implies surjectivity onto the mixed moduli; hence determinant plus inclusion
certifies the entire lattice, not an insufficient sublattice.

An exact modular solve gives one affine representative u0. Its six equations
are checked. Any other solution is u0 plus an integral combination of the
recorded basis. A lattice translation only makes the representative smaller;
it does not select or discard a solution. The input contains the full weighted
basis, representative, rational Gram-Schmidt D_i, triangular coefficients mu
and affine orthogonal coordinates. The JavaScript consumer checks the exact
Gram identity B B^T=mu diag(D) mu^T and the affine coordinate identities.
It does not trust a decimal norm or a floating LLL decision.

## Two-candidate completeness lemma

For a row basis b_0,...,b_(d-1), let D_i>0 be its exact Gram-Schmidt squared
lengths. Suppose every sought affine lattice point has squared norm at mostR²
and every D_i>R². At a descending enumeration node, after the larger-index
integer coefficients are fixed, write its next rational center as c=N/D,
with D>0. Orthogonality implies

    D_i (z+c)^2 <= R², hence |z+c|<1.

Writing q=floor(c), the only possible integers are -q-1 and -q. When c is
integral the former is superfluous; the other missing neighboring integer has
distance exactly1 and is excluded by the strict bound. Nonintegral endpoints
and half-integer ties cause no loss because both adjacent candidates remain.
Thus each node has at most two children, and a depth-d tree has at most
2^(d+1)-1 nodes including its root. Reject a branch only when its exact partial
squared norm already exceedsR², or at a full vector when an original side
budget fails. Exhausting this complete tree proves absence. Resource exhaustion
does not prove absence.

Here R²=2026²+2331²=9538237. The bound follows by applying sum(x_i²)<=sum(x_i)²
separately to the nonnegative positive and negative weighted entries. The
recorded exact D_i all strictly exceedR², so the lemma applies with d=16 and
at most131071 nodes. No root calculation is needed: all tests are rational
cross multiplications, with materialized quotients/remainders routed through
the existing BRC facade or its explicit BigInt language port.

## Actual complete proof tree

The search visits8 nodes and16 candidate branches. Every branch closes by an
exact squared-norm inequality; no full16-coordinate leaf survives. Below are
integer floors of the exact accumulated squared norms, for convenient reading.
The full rational values and quotient/remainder witnesses are in certificate.json.

| Node / coordinate | First candidate: floor norm / action | Second candidate: floor norm / action |
| --- | --- | --- |
| 0 / 15 | -1: 9743247 / reject | 0: 1492871 / node1 |
| 1 / 14 | 0: 4459930 / node2 | 1: 7548965 / node5 |
| 2 / 13 | -1: 14565198 / reject | 0: 5508309 / node3 |
| 3 / 12 | -1: 12085617 / reject | 0: 8305336 / node4 |
| 4 / 11 | -1: 14160377 / reject | 0: 11361903 / reject |
| 5 / 13 | 0: 7838022 / node6 | 1: 20982224 / reject |
| 6 / 12 | -1: 8356658 / node7 | 0: 20206565 / reject |
| 7 / 11 | 0: 10569526 / reject | 1: 15541482 / reject |

Every rejection floor is greater than9538237. The second node genuinely has
two admissible partial branches; blindly keeping only one nearest integer is
not a complete proof for this actual input. Both branches are explicitly
retained and subsequently rejected. Therefore the displayed r1 affine class
is empty. This is neither the whole p17 order1 nor the global T6 threshold.

## Actual verification and portability

The producer completed in8.953 seconds, using1855837 BRC evaluations, with
R1_AFFINE_CLASS_EMPTY. The independently coded JavaScript BigInt consumer
recomputed saturation, Gram and affine identities and checked all8 proof nodes,
returning PORTABLE_BIGINT_CERTIFICATE_PASS with333986 BRC evaluations. Five
deliberate certificate mutations were rejected. These are author cross-checks;
they are not a non-author or Driver review.

Open verify.html and select portable_input.json plus certificate.json, or run
node verify_portable.js portable_input.json certificate.json. Browser execution
uses only BigInt and standard Web Crypto; it needs no Python, FLINT, local
shell, service account or SDK. Python generation is optional. Every mathematical
integer in the portable input is a decimal string. The BRC port exposes and
checks Euclidean quotient/remainder/collapse traces; ordinary IEEE-754 Number
is confined to bounded indices and counters.

## Completed extension and actual next question

After the r1 certificate was complete, all fifteen remaining relaxed order1
classes r=2,...,16 were also checked; they were inexpensive and were not left
open merely to create a task. All are empty, using146 further nodes, so the
whole16-class family closes with154 nodes. Full input/certificates are in
remaining_inputs.json and remaining_certificates.json. Root subsequently independently consumed all sixteen class certificates:
154 nodes and170 norm-pruning edges passed. ROOT_REVIEW.json and
ROOT_ORDER1_REVIEW.json retain their distinct scopes and actual independent
processes. These checks are not formal Driver Acceptance.

The actual next unresolved unit is order2, not r2. order2_problem.json contains
all272 relaxed primitive patterns:16 q2 single atoms,136 same-side q1 pairs,
and120 opposite-side q1 pairs up to sign. The data generator checks every
mixed target and two-candidate bound but does not solve these cases. The
candidate Task preserves the real T6 parent and makes exact proof/data the
requirement; local Python, FLINT, SDK or a particular shell are not premises.

No global novelty, new global tool family, Working Truth, Foundation promotion,
or earlier-result Acceptance is asserted. Root handles Source publication.

Global-Knowledge-Sync: main@6f6fa5c / GLOBAL_KNOWLEDGE_V1
