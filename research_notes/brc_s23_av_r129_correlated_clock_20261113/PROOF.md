# R129 — Coefficient-sensitive exact enumeration of correlated S23 rotation signatures

Date: 2026-11-13 (Asia/Shanghai). Author-side auxiliary S23 research continuing R128. Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Prior research: R128 at `bcc4588af664b3c7b7d1c18cfcbfd15b089ac8c8`.

## Problem and exact reparameterization

For rational `x,l,h` with `l<h`, signed integer coefficients `A,d,E`, integer `m>=2`, define the S23 auxiliary Boolean observer

`M_i(theta)=1[{x+(A+i*d)*theta}<{E*theta}]`, for `0<=i<m`; `{z}=z-floor(z)`.

In the rank-one coefficient family `d!=0, A=s*d, E=r*d`, for arbitrary integers `s,r`, set `beta={d*theta}`. The exact observer becomes

`W_i(beta)=1[{x+(s+i)*beta}<{r*beta}]`, `0<=beta<1`.

The quotient is only for the specified auxiliary observation; original coefficients, theta witnesses and source provenance are retained.

## R129.1 — Exact critical-fiber enumeration, quadratic coefficient bound

Write `t_i=s+i`. Define the finite set of interior critical residues

`C = {beta in (0,1): r*beta in Z} union ⋃_i {beta in (0,1): x+t_i*beta in Z, t_i!=0} union ⋃_i {beta in (0,1): x+(t_i-r)*beta in Z, t_i!=r}`.

Define `K=|C|` and `B=max(|r|-1,0)+sum_{i=0}^{m-1}(|s+i|+|s+i-r|)`.

**Theorem.** Each bit and the full joint word are constant on every open component of `(0,1)\C`. The set of all words over one complete half-open beta period is obtained **exactly** by evaluating `beta=0`, every member of `C`, and one rational interior midpoint of each of the `K+1` complementary open components. Consequently,

`K<=B,quad |{W(beta):0<=beta<1}|<=2K+2<=2B+2=O(m^2+m(|s|+|r|))`.

For fixed integers `s,r` this is `O(m^2)`, compared to the known `Theta(m^4)` family of all free binary rotation words. The candidate count is independent of the numerical size of `d`; representation and witness costs depend on its binary length.

**Proof.** In any interval where the affine functions `x+t_i beta` and `r beta` avoid integer crossings, both fractional parts are continuous. Their strict comparison can change only at equality of their fractional parts, equivalent to `x+(t_i-r)beta in Z`. The listed critical set captures all three types of crossing. Coefficient zero yields an identically constant affine function, not an isolated crossing. A nonzero integer coefficient `a` makes `x+a beta` traverse an open interval of length `|a|` and meet at most `|a|` integers. The function `r beta` meets `max(|r|-1,0)` interior integers. The union bound gives `K<=B`. The listed rational representatives cover every singleton and open cell, and there are `K+(K+1)+1=2K+2` of them. QED.

## R129.2 — Every rational open interval, exact strict witnesses

**Theorem.** Given any rational open `J=(l,h)`, the words attained by `theta in J` can be generated exactly with no more than `2K+6` rational beta probes, recovering an exact rational `theta` witness for every word. Their number remains at most `2K+2`.

**Algorithm.** Insert `{d*l}` and `{d*h}` into the rational critical residues, together with 0 and 1, sort, and evaluate beta at each interior singleton, at beta=0 and at one midpoint in each open cell (beta=1 is excluded). A beta probe is attainable precisely when an integer `k` satisfies

`min(d*l-beta,d*h-beta)<k<max(d*l-beta,d*h-beta)`.

Choose `k=floor(min(...))+1`, test that `k<max(...)`, and if so set `theta=(k+beta)/d`. This exactly recovers an interior theta witness for either sign of d.

**Proof.** The image of an open real interval under `theta -> {d theta}` on the circle is an open arc (possibly wrapped) for angular width below one revolution; it is the whole circle minus its one endpoint residue for width equal to one revolution; and it is the whole circle for width greater than one revolution. Membership changes only at the two endpoint residues. Combining these two cuts with `C` makes both image membership and all Boolean bits constant on every open beta cell. The strict integer inequality handles singleton points, endpoint exclusions and wraparound. At most `K+2` distinct interior cuts are added, giving at most `2K+6` probes. Every attainable word on J is among the one-period words. QED.

At exactly one period of open interval length, the missing residue may carry a unique word: the algorithm preserves this R127.4 endpoint distinction rather than silently treating the interval as closed.

## R129.3 — Exact quadratic lower-bound family

Set `x=0,s=0,r=1`, and let beta range over `[0,1)`. For beta>0, `W_0=1` and for `1<=i<m`

`W_i(beta)=floor(i*beta)-floor((i-1)*beta)`.

Indeed, the difference is the binary carry when adding beta, equivalent to `{i beta}<beta`. At beta=0 all bits are zero.

**Exact theorem.** For every `m>=2`, the number of distinct words is

`T(m)=2+sum_{q=2}^{m-1}phi(q)=Theta(m^2)`,

with the standard summatory-totient asymptotic `T(m)=3(m-1)^2/pi^2+O(m log m)`. Thus the quadratic order for fixed `s,r` is sharp.

**Proof.** For beta>0, the word's bits from positions `1,...,m-1` recover the entire vector `(floor(j beta))_{j=1}^{m-1}` by cumulative summation. That vector changes exactly at the reduced rationals `p/q in (0,1)` of denominator `2<=q<=m-1`; crossing `p/q` changes at least `floor(q beta)`. At an exact rational, all floor values agree with their immediately right-hand values, creating no additional singleton word. There are `sum_{q=2}^{m-1}phi(q)` such thresholds and one more open sector than thresholds. The beta=0 all-zero word is distinct because `W_0=1` for beta>0. QED.

The carry-word/Farey count are classical mechanical/Sturmian structures. The project-specific contribution is the exact S23 coefficient specialization, sharp bound, and arbitrary-open-interval witness-preserving enumerator.

## Algorithm and reproducibility

For rational x, generate all critical fractions `(k-x)/a` and `k/r` for relevant nonzero integer coefficients and interior integer crossings. Sort/deduplicate `O(B)` fractions using `O(B log B)` rational comparisons, evaluate at most `O(B)` bit vectors using `O(mB)` rational operations, and recover theta with a constant number of exact floor/comparison operations per probe. For fixed s,r the arithmetic-operation bound is `O(m^3)`; exact bit costs include coefficients, x, interval endpoints and `log|d|`. Original input-to-(s,r) uses `d!=0`, `A%d=0`, `E%d=0` and exact divisions. No 2D/3D integer-program calls are needed for this coefficient family.

Verification used Python standard-library Fraction with `check_r129.py`: sharp count for every m=2..30; 220 signed/rational random instances with 32,960 within-cell checks and 6,372 singleton critical checks; 180 signed-d, rational-open-interval cases against independently enumerated theta-domain affine crossings; 204 additional signed-d pointwise equality checks. Output: `R129_COUPLED_CLOCK_PASS`. Tests check the implementation; the universal argument is above. Reproducibility details and actual counts are in `verification_r129.json`.

Prior-art distinction: Frid & Jamet, *The number of binary rotation words*, RAIRO-ITA 48 (2014) 453–465, DOI 10.1051/ita/2014019, establishes the free rotation-word `Theta(m^4)` result. This note concerns the S23 correlated subfamily, not that universal enumeration theorem.

**Frontier:** examine whether a wider bounded-short-relation family `E=uA+vd` admits comparable exact, witness-preserving signature enumeration without general integer programming; benchmark cost on the same rational test sets. Formal Task/CLAIM, mathematical review and native X6 event authority are separate from this author-side auxiliary result.
