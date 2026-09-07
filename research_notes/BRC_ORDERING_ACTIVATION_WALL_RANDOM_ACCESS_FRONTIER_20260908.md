# BRC Boundary Ordering ↔ Activation Wall Random-Access Frontier

Status: `RESEARCH FRONTIER / EXACT COMPOSITION + EXISTING-TOOL REUSE + CLASSICAL N^(1/4) BASELINE + NEW COMPLEXITY TARGET / NO SPEEDUP CLAIM`
Date: `2026-09-08`
Parent: `research_notes/BRC_COLLISION_LOCAL_ORBIT_ORDERING_FRONTIER_20260908.md`
Existing reused operator: `t1.nonly_valuation_wall_gcd_extractor`
Source snapshot before write: `main@de93b983b7e67fcf247ef53cba450bdb080d5e2b`

## 0. BRC reuse resolution

The collision frontier ended at the one-bit query

`sign(u*p-v*q)`

or equivalently the ordering of the two pure hidden boundaries

`L_(2u+1,1)` and `L_(1,2v+1)`.

A capability audit found that this is not a new semantic primitive. The admitted domain operator

`t1.nonly_valuation_wall_gcd_extractor`

already implements an exact N-only hidden-prime activation wall. The correct resolution is therefore

`COMPOSE_APPLIED / EXTEND_EXISTING_TOOL`,

not creation of a new BRC family.

The new question is computational: can a factor-scale activation state be evaluated by random access substantially faster than both the current linear stream and the classical block-product baseline?

---

## 1. Boundary order is exactly a minimum-factor threshold

Let `N=pq`, `1<p<q`, and let `u,v>0` be public integers. Then

`u/v < q/p`

iff

`u*p < v*q`

iff, after substituting `q=N/p`,

`u*p^2 < v*N`

iff

`p < sqrt(v*N/u)`.

Thus the cross-boundary order bit from the collision note is exactly a threshold query for the least hidden factor.

For `u/v>1`, the threshold `T=sqrt(vN/u)` lies below `sqrt(N)<q`. Therefore the query is in the one-factor zone: if the threshold crosses any hidden prime, it crosses `p` but not `q`.

Equality is not problematic. If `u*p^2=vN`, then the public rational `vN/u` is the exact square `p^2`; verifying that square and division already returns the factor. Otherwise one may replace the real threshold by the appropriate neighboring integer without changing the strict comparison.

Freeze:

`BOUNDARY_ORDER_BIT = MIN_FACTOR_THRESHOLD_BIT`.

This is stronger than the previous energy-threshold equivalence because it identifies the exact existing algorithmic primitive needed to evaluate the bit.

---

## 2. Classical factorial threshold is already a perfect order-bit evaluator

For any public integer `B` satisfying `1<=B<q`,

`gcd(B!,N)` equals

- `1` when `B<p`;
- `p` when `p<=B<q`.

Hence a threshold evaluator for `p<=B` is already a factor extractor on every positive answer.

The collision-order binary search picture can therefore be sharpened:

> the first threshold crossing need not merely return one more bit of `q/p`; a provenance-preserving threshold observable can expose the factor immediately.

The hard part is only to evaluate the huge prefix/product without `Theta(B)` sequential work.

---

## 3. Existing PCF4R valuation wall is a denominator-cancelled threshold family

The reused operator uses

`A_s=(2s)!(3s)!/(s!)^5`.

For prime `r>3` and `0<=s<r`, its accepted theorem is

`v_r(A_s)=floor(2s/r)+floor(3s/r)`,

so

`r | A_s <=> 3s>=r`.

Thus `A_s` converts the public threshold `B=3s` into an exact modular activation event while keeping all streamed denominators invertible before the first hidden factor is crossed.

For `N=pq`, as long as `s<p`,

- `3s<p` gives `gcd(A_s,N)=1`;
- `p<=3s<q` gives `gcd(A_s,N)=p`;
- `q<=3s` gives `gcd(A_s,N)=N`.

This is precisely the three-state threshold observer required by the boundary-order reduction.

The existing dyadic synchronization theorem and square-root fallback are therefore a coarse adaptive order search already present in the repository. Its current limitation is implementation cost: `A_1,A_2,...` are streamed consecutively, so the first factor-scale wall costs `Theta(p)` recurrence updates in the balanced case.

---

## 4. Tunable multinomial activation walls do not improve naive total work

A useful generalization is

`M_(c,s)=(c*s)!/(s!)^c`, `c>=2`.

This is an integer multinomial coefficient. For a prime `r>s`, the denominator contains no factor `r`, while the numerator contains `r` exactly when `c*s>=r`. Hence

`r | M_(c,s) <=> c*s>=r`.

The exact valuation is

`v_r(M_(c,s)) = sum_(j>=1) floor(c*s/r^j)`

under `s<r`; only positivity is needed for the wall.

The consecutive ratio is

`M_(c,s)/M_(c,s-1)
 = prod_(j=1)^c (c(s-1)+j) / s^c`.

So increasing `c` moves the activation index from `Theta(p)` to `Theta(p/c)`, but one recurrence update now contains `c` numerator factors. A direct stream to the first wall touches

`Theta(c*(p/c))=Theta(p)`

factor terms. Therefore the tunable wall changes geometry but gives no naive asymptotic gain by itself.

This is a work-conservation observation for the direct recurrence, not a lower bound against block products or special algorithms.

---

## 5. Random access lands directly on the classical block-product / fast-recurrence frontier

The scalar PCF4R recurrence

`A_s = A_(s-1) * 6(2s-1)(3s-2)(3s-1)/s^3`

is a first-order recurrence with polynomial/rational coefficients after denominator clearing.

Bostan–Gaudry–Schost (SIAM J. Comput. 36 (2007), 1777–1806) give baby-step/giant-step methods for computing isolated or several nonconsecutive terms of polynomial-coefficient recurrences. In their integer-factorization application, the same block-product machinery detects a prime divisor bounded by `b` in essentially `sqrt(b)` ring/product scale (up to multiplication/logarithmic factors), improving the classical Strassen/Pollard deterministic framework.

Consequently, applying a generic fast-recurrence evaluator to the factor-scale PCF4R state `s=Theta(p)` yields the natural balanced-semiprime scale

`sqrt(p) = N^(1/4)`

up to subpolynomial/logarithmic factors.

Equivalently, one can bypass the PCF4R notation and apply the classical block factorial product directly to the minimum-factor threshold `B=Theta(p)`; it is the same computational frontier.

This is a major implementation improvement over the current `Theta(p)` streamed domain operator, but it is **not** a new factorization-complexity result.

Modern rigorous deterministic general factoring is already asymptotically better: Harvey obtained `N^(1/5+o(1))`, and Harvey–Hittmeir later supplied a log-log improvement at exponent one fifth. Therefore an `N^(1/4)` random-access wall implementation is primarily a semantic/reuse baseline, not a competitive breakthrough target.

---

## 6. Adaptive order queries do not worsen the exponent, but also do not fix it

Suppose we use the boundary-order view and issue `O(log N)` adaptive rational threshold queries to narrow `q/p`.

If each query at factor-scale threshold is evaluated independently by a generic `sqrt(p)` block method, total work is still

`N^(1/4+o(1))`

because the logarithmic query count is absorbed in the subpolynomial/logarithmic factor.

Moreover, a positive threshold query already returns `p` through the gcd, so full ratio reconstruction is unnecessary.

Thus the real complexity question is not how to reduce the number of order bits. It is how to make **one factor-scale threshold decision** cheaper than the classical block-product cost.

Freeze:

`QUERY_COMPLEXITY_IS_NOT_THE_BOTTLENECK`.

`FACTOR_SCALE_THRESHOLD_EVALUATION_IS_THE_BOTTLENECK`.

---

## 7. Observer audit: what information may safely be compressed

For a threshold-only future operation, the entire exact residue `A_s mod N` is more information than necessary. The declared output is only the trichotomy

`UNIT / PROPER_NONUNIT / TOTAL_NONUNIT`

or, in the one-factor zone, the Boolean/proper-factor pair

`B<p` versus `p<=B<q`.

Therefore a new BRC algorithm is allowed to quotient away the exact hypergeometric value **if and only if** it preserves the first hidden-prime activation event and its gcd witness.

This opens a narrower possibility not addressed by generic term computation:

> compute the activation/nonunit status of a huge recurrence/product block without materializing its full residue value.

However, ordinary product trees already exploit exactly this distinction through batched invertibility/gcd tests. Calling the output a BRC collapse is not new progress unless the branch/recoalescence structure yields an asymptotically or measurably stronger compression than those classical product-tree methods.

---

## 8. New BRC complexity target

The collision program and valuation-wall program now share one smallest unresolved unit:

`N, B=Theta(sqrt(N))`

`-> decide whether the least prime factor p <= B, and if yes return a proper gcd`,

under the semiprime/equal-length promises relevant to RSA-270,

**without**:

- streaming `Theta(B)` local recurrence terms;
- materializing a `Theta(sqrt(B))` generic baby-step/giant-step block frontier;
- reducing to the known Strassen/Bostan–Gaudry–Schost small-factor product search;
- importing a stronger general deterministic factoring engine and relabeling it BRC.

A successful BRC contribution must exploit some additional exact structure of the activation carrier, such as a smaller sufficient recoalescence certificate, a new quotient stable under giant jumps, or cross-scale reuse that lowers the factor-scale decision below the classical `N^(1/4)` baseline.

Because the best known rigorous deterministic general algorithms already achieve exponent one fifth, external novelty/competitiveness would in fact require comparison against that stronger baseline as well. The immediate project benchmark remains two-tiered:

1. beat the current project operator's `Theta(p)` stream;
2. then determine whether the resulting method is genuinely distinct from and stronger than existing deterministic-factorization machinery.

---

## 9. Kill conditions and next experiments

Kill a candidate if:

- it merely replaces sequential products with an ordinary product tree / BSGS and lands at `N^(1/4+o(1))`;
- it computes a full factor-equivalent `S`, `E3`, boundary, or divisor before the threshold event;
- it uses squared-gap proximity while discarding the sign/order information;
- its apparent gain comes only from taking a larger activation coefficient `c` while per-step degree/work grows proportionally;
- it silently invokes a modern `N^(1/5)` factoring routine as a subroutine.

Retain a candidate only if it produces a smaller exact activation certificate or a reusable jump law whose cost is demonstrably below the generic block frontier on the same arithmetic model.

Recommended next finite/theoretical experiment:

1. express one long PCF4R block as a BRC branch family indexed by its linear numerator factors and denominator valuations;
2. search for an observer-safe quotient that preserves only `gcd(block,N)` / activation, not the block residue;
3. compare its state count and arithmetic work exactly against a balanced product tree and Bostan–Gaudry–Schost block evaluation;
4. if no quotient below square-root block width survives, record the valuation-wall collision route as semantically unified but algorithmically classical.

No Foundation promotion, Working Truth promotion, or factorization-speedup claim is made.