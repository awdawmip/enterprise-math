# R129.4 — Exact gcd period quotient of the correlated S23 word family

2026-11-13. Supplement to R129's one-parameter event-sweep theorem. Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. The gcd period itself was already observed in R127 (`72f6de415d45fbd9a0a3bfde7aae36ccc99d0b93`); the additional result here is a *full-signature circular event-count bound and exact open-endpoint qualification* for R129's oracle.

Let `S_i(theta)=1[{x+(A+i*d)theta}<{E theta}]` for arbitrary integer A,d,E, real x, and i=0,...,m-1. Put `g=gcd(|A|,|d|,|E|)`. Assume g>0 and set `P=1/g`.

**R129.4a (period quotient):** For all real theta, `S(theta+P)=S(theta)`. Thus every signature attained over an arbitrary real interval lies in the complete period-word set `V={S(theta):0<=theta<P}`. Every open interval whose length exceeds P attains exactly V. An open interval with length exactly P contains every phase class except the endpoint residue, and can omit a signature supported only on that excluded class.

**R129.4b (circular cut count):** Define the event residues in the phase circle `R/PZ` from the three affine integer-crossing families used in R129: `E theta in Z`, `x+(A+i*d)theta in Z`, and `x+(A+i*d-E)theta in Z`, omitting identically integral affine functions as non-events. Let Q be the number of distinct event classes. Then

`Q <= B = (|E| + sum_{i=0}^{m-1}(|A+i*d|+|A+i*d-E|))/g`.

Every one of the B terms is an integer because g divides A,d,E. If Q>0, the circle has Q open event arcs and Q event points. Each arc carries a constant m-bit word. Therefore the complete-period word count satisfies `|V|<=2Q<=2B`; if Q=0, it is 1. In particular,

`|V| <= max(1,2B)`.

This bound is independent of the length of the original interval. For rational x, an exact oracle computes all cuts on any reference period `[u,u+P)`, including one endpoint class and every open-arc midpoint; this detects both ordinary and boundary-only words. The Q=0 case is constant. For any interval I, the word-set is a subset of V, even if I contains many thousands of periods. The bound is coefficient-sensitive and complementarily uses R128's free rotation-word O(m^4) bound.

**Proof.** Each phase increment under `theta -> theta+P` equals `(A+i*d)/g` or `E/g`, both integers. Fractional parts and all bits are unchanged, establishing period P. The quotient map of an open interval onto the phase circle is surjective if length>P and omits exactly its endpoint residue if length=P. For any nonconstant affine phase `b+s theta` with integer slope s divisible by g, the condition `b+s theta in Z` has exactly `|s|/g` distinct solution classes mod P: translation by P advances the phase by integer `s/g`. Summing over all event families bounds their union by B. R129.1 establishes constancy between consecutive events. A circle with Q>0 marked points has Q connected open arcs and Q singleton marked points, hence at most 2Q distinct attained words. With Q=0 it has a single constant word. This proves all claims.

**Sharp endpoint exception within the same R129 family.** For `x=A=0,d=E=1`, the period is P=1. On `(0,1)`, the first bit is identically one and the exact word count is `H_m=1+sum_{q=2}^{m-1}phi(q)` from R129.3. At `theta=1`, all bits are zero, a word absent from the whole open interval `(0,1)`. For any epsilon>0, `(0,1+epsilon)` contains the complete phase circle, hence its word set is `H_m+1` words. At m=32 the two counts are 308 and 309. Thus a period-length open interval may lose a boundary singleton; endpoint semantics materially affect exact word counts.

**Exact finite validation.** The companion script `check_r129_period.py` uses the R129 Fraction oracle, deterministic seed 129220261113, 160 signed integer-coefficient instances, 800 exact shift checks, and 160 comparisons of long-interval sets to complete-period sets. Every instance passed. It also tested the sharp endpoint exception for m=2..32, 31 exact cases; the final pair is 308 versus 309. Output: `R129_PERIOD_QUOTIENT_PASS`. The universal proof is the argument above, not the finite tests.

**Next:** Reduce the quotient parameter further for special relation classes, test potential nonminimal periods rather than asserting minimality, and benchmark gcd-folding versus one-pass event enumeration and coefficient-independent rotation-word ILP methods. This note preserves the S23 auxiliary observer type and does not grant formal task or native X6 event authority.
