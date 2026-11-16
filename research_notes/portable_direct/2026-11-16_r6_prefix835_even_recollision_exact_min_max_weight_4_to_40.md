# PREFIX-835 — Exact minimum maximal source weights for 19 even-time Q recollisions, with a uniform resource lower bound

**Date:** 2026-11-16. **Status:** AUTHOR_PROVED / EXACT_FINITE_EXHAUSTION / EXACT_NAMED_STATE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
**Frozen scientific pin:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
**Antecedents:** PREFIX-832 (all-time weighted Q observation formula), PREFIX-833 (full-histogram collision criterion), PREFIX-834 (fixed-operator parity/source-count minimality). Research is a typed positive named-source BRC *auxiliary* model, not a native X6 temporal or physical-event claim.

## Fixed problem

For p=q=3 initially present distinguishable positive-integer unmarked sources, marked source initially absent, and fixed **a=1,b=2** in the combined weighted legal operation Q=R+A, find two **different** three-element positive-integer source-weight multisets whose complete unnormalized occupancy histograms agree again at a specified even integer T≥4 after earlier separation.

Define M(T) as the **minimum possible largest weight** among all six source weights in such a pair. Source number p, operator, capacity, initial occupancy and observer are all fixed, so M(T) measures the magnitude of the integer input and not the number of sources.

## Theorem 835.1 — Exact finite optima for T=4,6,...,40

For each listed even T, M(T) has the following **proved exact value**, established by exhaustive enumeration of all admissible ordered-by-weight pairs up to the first successful maximum bound:

| T | M(T) | T | M(T) | T | M(T) |
|---:|---:|---:|---:|---:|---:|
| 4 | 11 | 6 | 9 | 8 | 23 |
| 10 | 28 | 12 | 34 | 14 | 21 |
| 16 | 24 | 18 | 40 | 20 | 30 |
| 22 | 26 | 24 | 43 | 26 | 43 |
| 28 | 42 | 30 | 34 | 32 | 48 |
| 34 | 26 | 36 | 41 | 38 | 29 |
| 40 | 50 | | | | |

The full exact witness table (all 19 pairs, Δe2, Δe3, first-hit search counts and full T histograms) is in `PREFIX835_R6_WEIGHT_OPTIMUM_RESULTS.json`.

Three illustrative *sharp* certificates:

* **T=4:** A=(1,4,10), B=(2,2,11), M=11, Δe2=6, Δe3=-4.
* **T=6:** A=(2,5,8), B=(3,3,9), M=9, Δe2=3, Δe3=-1.
* **T=34:** A=(1,16,16), B=(2,5,26), M=26, Δe2=96, Δe3=-4.

They satisfy Δe1=0 and 4Δe2+3(T-2)Δe3=0; their full observer histories agree at times **exactly 0,1,T** and differ at all other integer times. Theorem 833.1 establishes the all-time uniqueness of the recollision; independent exact named-state iteration checks all frames through T+2.

**Proof of the *finite* minimum and completeness.** By the full p=3 classification of PREFIX-834.2, every admissible even-time pair necessarily has n=2, hence e1(A)=e1(B), e2(A)≠e2(B), and 4Δe2+3(T-2)Δe3=0. Conversely those exact conditions guarantee the full-histogram recollision at T; distinct positive triples obey them if and only if they are different elements of the same bucket keyed by

\[
\left(s,\;f_T\right)=\left(x+y+z,\;4(xy+xz+yz)+3(T-2)xyz\right).
\]

Every positive-integer unordered three-element multiset has **exactly one** nondecreasing representative 1≤x≤y≤z. Enumerate representatives in increasing z=M, then all 1≤x≤y≤M. Keep earlier representative for each (s,f_T). The **first** time two distinct representatives occupy the same bucket, that M equals the optimum: no smaller candidate pair exists because every triple with a smaller maximum was exhaustively visited. Distinct sorted triples with the same s,e2,e3 would be the roots of the same monic cubic and therefore are identical; hence a collision for *different* triples automatically gives Δe2≠0 and Δe3≠0. The explicit witnesses and the exhaustive enumeration certify all 19 displayed exact M(T). This proves a scoped finite theorem rather than an untested extrapolation to arbitrary T.

## Theorem 835.2 — Uniform magnitude lower bound for all even T

For **every even integer T≥4**, any such p=3 fixed-operator positive-integer re-alias pair with maximum weight M obeys

\[
\boxed{M^2\ge1+\frac{T-2}{4}\quad\text{and hence}\quad
M\ge\left\lceil\sqrt{\frac{T+2}{4}}\right\rceil .}
\]

**Proof.** From the p=3 criterion,
\(4|\Delta e_2|=3(T-2)|\Delta e_3|\).
Both products e3 are integers, and Δe3≠0 since Δe2≠0, so |Δe3|≥1. For a positive triple bounded by M, its second elementary symmetric coefficient lies in [3,3M²]. Therefore
\(
3(T-2)\le4|\Delta e_2|\le12(M^2-1)
\),
giving the displayed bound. QED.

Together with the explicit PREFIX-834 family having M≤3T-1, these prove a **nonconstant lower resource law**:
\[
\frac12\sqrt{T+2}\le M(T)\le3T-1
\quad(T\ge4\text{ even}),
\]
subject to integer ceiling on the left. The finite exact sequence is nonmonotone (e.g. M(4)=11>M(6)=9; M(32)=48>M(34)=26), so simple monotone extrapolation does not describe the actual optimal finite resources.

## Exact computation and provenance

The accompanying `PREFIX835_R6_WEIGHT_OPTIMUM_CHECK.py` is a complete standard-library arbitrary-precision Python enumerator. It visits every sorted positive triple of each maximum bound M, stores its exact (sum,f_T) bucket, returns on the first distinct collision, and independently evolves the named-subset+marked-flag Q system for each returned witness through T+2. Results contain 19 optimal certificates and all complete histograms at the recollision times.

Execution (rerun with exact JSON byte-for-byte deterministic comparison) returned `ALL_EXACT_ASSERTIONS_PASSED`:
- 19 even target times, 4≤T≤40, step 2.
- 139,475 examined source triples (summed across independent target searches).
- 13,794 named-state weighted edge updates.
- 1,900 complete histogram scalar comparisons.
- Exact full histogram equality times {0,1,T} through T+2 for every witness.

An independent JavaScript BigInt enumerator reproduced all 19 M values, the aggregate statistics and corresponding finite histograms. No floating-point approximation is involved in candidate enumeration or checking. Each T has a finite exhaustive exclusion certificate implicit in enumerating all triples with M below the first matching bucket; source code plus deterministic results allow direct recalculation.

**Proof boundary:** general T lower bound and fixed finite list of exact optima have proofs above. The asymptotically sharp growth rate of M(T) remains **OPEN**; the observed oscillatory finite pattern does not settle its order. This result does not establish physical heartbeat timing, signed/phase cancellation, native X6 admission, a shared task CLAIM, or project mathematical promotion.

## Next work

Look for constructive infinite subfamilies beating O(T) and sharpen the general lower bound, possibly using fixed-sum integer geometry and Diophantine divisibility of Δe2 and Δe3. Study minimal *forward-safe* observer coordinates in the presence of isolated complete histogram aliases, and separately return to q≥5,b>0 positive minimal Q-carrier construction. Preserve all prior source pins and named-source provenance.
