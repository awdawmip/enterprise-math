# PREFIX-874 — Global odd-half-gap sieve at the 32-source 19-bit boundary

Date: 2026-11-17. Direct continuation of PREFIX-873 and its signed-half-order witness theorem.
Scientific source freeze f42f2906d77f24085c123f3ccfe9667d41caa96d unchanged.
Status: AUTHOR_PROVED / EXACT_INTEGER_ENUMERATION / TWO_INDEPENDENT_AUTHOR_SIDE_ALGORITHMS / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Result

In the auxiliary p=32 named-binary BRC complete-transition observer, both ports are fixed odd moduli between 3 and Q=2^19-1=524287. Let (qH,qL) have qH>qL and define g=(qH-qL)/2. For every positive **odd** half-gap g, use PREFIX-873's explicit collision theorem:

Choose the least m>=1 for which 2^m is congruent to +1 or -1 modulo g, and choose sigma in {-1,+1} with g | (2^m+sigma). Put k=(2^m+sigma)/g, N=2^32. If m<=30 and k*qH+3<N, then the pair (qH,qL), and also its reversal, is NOT lossless. This gives two explicit legal named one-bit transitions sharing both observations, with full old/new state and source identity retained.

Let Gmax=floor((Q-3)/2)=262142. For each odd g from 1 through Gmax satisfying signed-order conditions, let

  M(g)=largest odd integer <=min(Q,floor((N-4)/k));

and let L(g)=2g+3. When M(g)>=L(g), the exact number of analytically excluded **unordered** modulus pairs with that half-gap is

  C(g)=(M(g)-L(g))/2+1.

Different g correspond to different positive modulus gaps and therefore to disjoint sets of pairs.

### Theorem 874.A — Complete bounded evaluation of this certificate family

Across ALL odd g in [1,262142], precisely 360 half-gaps have C(g)>0. Of these, 239 have M(g)=Q, giving a collision for every allowed odd qH with that half-gap; the remaining 121 have an explicitly bounded qH interval. The sum of the exact intervals is

  SUM C(g) = 61,017,906 unordered pairs
           = 122,035,812 ordered port pairs.

This count is a **complete finite classification of pairs excluded by the specific PREFIX-873 shortest-signed-order criterion** over its defined odd-half-gap domain. It is not an exhaustive classification of all invalid 19-bit modulus pairs. The original global boundary B_fix,odd(32) in {19,20} remains open.

### Proof of the count

Enumerate each odd g in the specified finite interval. The multiplicative order of 2 modulo odd g is finite. A least signed half-order m<=30 can be found by exact modular recurrence x_{m+1}=(2*x_m) mod g, stopping at x_m=1 or x_m=g-1. If neither appears by m=30, the PREFIX-873 theorem has no admissible source-bit index i=m+1 under p=32. For each remaining g, compute k and the exact largest odd cap M(g). Count odd integers from 2g+3 to M(g). All formulas are integer floor arithmetic, and all pair families are disjoint by their half-gap. The executable certificate computes 360 nonempty rows and the asserted sum.

For independent algorithmic coverage of the finite enumeration, the checker also enumerates all odd divisors g of 2^m-1 or 2^m+1, m=1..30, using integer square-root trial division, and preserves the first (least m) representation. The two methods produce exactly the same 360 rows, including signed parameters, ceiling values, counts and explicit legal collision witnesses. This equality establishes complete coverage of the stated finite search under the exact arithmetic implementation; the infinite conditional collision theorem is proved in PREFIX-873.

### Witness and scope

Each of 360 certified half-gap rows contains a four-endpoint witness at its maximal allowed qH. The checker verifies all bit-flip legality, endpoint ranges and identical observations. The formula from PREFIX-873 establishes validity for the rest of each counted interval.

In this result g is the **half-gap**, not necessarily gcd(qH,qL). A theorem ruling out pairs with a gap of 2g does not rule out every pair sharing a given gcd. The native X6 Heartbeat World, P000 6+1 worldview, three-dimensional slice and residual-provenance constraints remain intact. This is an exact auxiliary named-source observer calculation.

## Reproduction

Run the zero-dependency Python file PREFIX874_R6_ALL_GAPS_CHECK.py with Python 3.8+ to produce PREFIX874_R6_ALL_GAPS_RESULTS.json. It checks 360 endpoint witnesses, validates all computed counts and repeats the entire finite family enumeration via two structurally different methods. No floating-point arithmetic or external network used. The result JSON stores the exact parameters and witnesses for every certified gap.

The prior proof and first 23-gap certificate:
https://github.com/awdawmip/enterprise-math/blob/b99af78b7ffb090228f4b6e27341f691b7376b6a/research_notes/portable_direct/2026-11-17_r6_prefix873_signed_halforder_gap_collision.md

## Next scientific frontier

Combine this criterion with k*q1-l*q2 two-power differences where k and l are unequal; count the union under strict deduplication and compare exclusion against the exact necessary gcd/fiber-capacity filters of PREFIX-871/872. A complete 19-bit no-go requires covering ALL remaining pairs or a separate analytic impossibility theorem. Alternatively seek a valid 19-bit construction. Continue independent p=62 coprime investigation. Do not promote an auxiliary observation collision to a native X6 evolution claim without an explicit typed mapping.
