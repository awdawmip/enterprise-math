# R005-A — p=2 Discrete One-Unit Gap Repair Beyond the Continuous Frontier

Status: `PROVED R005 STRUCTURAL + EXACT FINITE PATCH / NOT CANONICAL / LEAN PENDING`  
Date: `2026-08-30`  
Researcher-ID: `R005A-7C2`  
Task: `RS-R005-PRIME-ALGORITHM-LAB`  
Owner generation: existing `research/r005a-prime-algorithm-lab-20260810`

## 1. Purpose

The confirmed maximal-gap-start checkpoint gives a continuous real-interval certificate through

\[
K_{85}=2,821,231,035,570.
\]

That endpoint comes from requiring the Tier-B q^2 cofactor interval to have real width at least 916 before the global e=1 cofactor resource ends.

The condition is sufficient but not necessary for integer prime capture. Immediately beyond `K85`, q is restricted to primes and the cofactor interval is discretized by floors.

This checkpoint extracts the first discrete repair layer exactly.

---

## 2. P2-DR1 — floor-width gap lemma

Let an external finite computation certify that every consecutive prime gap in a cofactor range is at most an even integer `G`.

For any exclusive-collision cofactor interval

\[
I=\left(\frac AQ,\frac UQ\right],
\]

define

\[
n=\left\lfloor\frac AQ\right\rfloor,
\qquad
D=\left\lfloor\frac UQ\right\rfloor-n.
\]

Then the eligible integer cofactors are exactly

\[
n+1,\ldots,n+D.
\]

### Full discrete width

If

\[
D\ge G,
\]

then `I` contains a prime.

### One-unit deficit

If

\[
D=G-1,
\]

then `I` can be prime-free **only if**

1. `n` itself is prime; and
2. the next consecutive prime after `n` is exactly `n+G`.

Equivalently:

\[
\boxed{
D=G-1
\ \land\ 
I\text{ prime-free}
\Longrightarrow
n\text{ starts an exact gap }G.
}
\]

### Proof

If `n` is composite, let `p` be the greatest prime below `n`. Then

\[
p\le n-1.
\]

The next prime `p'` satisfies

\[
p'\le p+G\le n+G-1=n+D,
\]

so `p'` lies in the cofactor interval.

If `n` is prime and its next gap is strictly smaller than `G`, prime gaps above 2 are even, hence the next gap is at most `G-2`; the next prime again lies at most at `n+G-2<n+D+1`.

Therefore failure is possible only when `n` itself begins a gap of exact length `G`.

This converts a continuum-style width deficit into a sparse exact gap-start event.

---

## 3. The first post-K85 seam

Use the already established resource pair

\[
(G_1,X_1)=(1724,P_{85}),
\]

where

\[
P_{85}=101,412,319,996,363,309,069,
\]

and the Tier-B q^2 resource

\[
(G_2,X_2)
=
(916,1,686,994,940,955,803).
\]

For a prime q, the global e=1 channel can first fail at

\[
k_g(q)=\left\lceil\sqrt{P_{85}q}\right\rceil.
\]

The q^2 channel has real width at least 916 from

\[
k_b(q)=\frac{916q^2}{2}=458q^2
\]

onward.

The continuous certificate fails when

\[
k_g(q)<k_b(q).
\]

The first prime q for which this occurs is

\[
\boxed{q=78,487.}
\]

For the first several such q, however, the initial q^2 real width still lies in

\[
[915,916).
\]

Hence the floor width is only 915 or 916, and P2-DR1 says that only the 915 events whose floor starts an exact 916-gap need inspection.

The last prime in this one-unit phase is

\[
\boxed{q=78,541.}
\]

The next prime is `78,553`, whose initial q^2 width is approximately `914.810606`, so it belongs to the deeper deficit phase.

---

## 4. Exact event parametrization

Put

\[
Q=q^2,
\qquad
H=916/2=458.
\]

Inside the seam

\[
k_g(q)\le k<k_b(q)=HQ,
\]

write

\[
k=HQ-s,
\qquad
1\le s\le HQ-k_g(q).
\]

Then

\[
\left\lfloor\frac{k^2+2k}{Q}\right\rfloor
-
\left\lfloor\frac{k^2}{Q}\right\rfloor
=
916+
\left\lfloor\frac{s^2-2s}{Q}\right\rfloor
-
\left\lfloor\frac{s^2}{Q}\right\rfloor.
\]

The one-unit deficit `D=915` occurs exactly when, for

\[
j=\left\lfloor\frac{s^2}{Q}\right\rfloor,
\]

one has

\[
\boxed{
0\le s^2-jQ<2s.
}
\]

For fixed j, only the integers around `sqrt(jQ)` can satisfy this. This is the exact event compression used by the verifier.

The verifier does **not** scan every k in the seam.

---

## 5. Exact 64-bit primality audit

Artifact:

`experiments/r005a_p2_discrete_gap916_patch.cpp`

Result:

`experiments/r005a_p2_discrete_gap916_patch_results_20260830.json`

Every floor cofactor inspected in this phase is below `2^64`. The executable uses the standard deterministic Miller–Rabin base set

`2, 325, 9375, 28178, 450775, 9780504, 1795265022`

for exact uint64 primality decisions.

For every `D=915` event:

1. test whether the floor `n` is prime;
2. if not, P2-DR1 closes the event immediately;
3. if yes, test `n+916`;
4. only if both endpoints are prime, test every odd interior integer until an interior prime is found;
5. a failure would be recorded only if no interior prime exists.

Large j-ranges were split into disjoint inclusive chunks; counts add exactly and no semantic condition changes across chunks.

---

## 6. Finite results

The complete one-unit phase contains seven prime q values:

\[
78,487,
78,497,
78,509,
78,511,
78,517,
78,539,
78,541.
\]

Across those seven seams the exact audit checked

\[
\boxed{4,001,995,327}
\]

floor-width-915 events.

Among them:

\[
\boxed{115,035,018}
\]

had a prime floor start, and

\[
\boxed{4,380,645}
\]

had both `n` and `n+916` prime.

After checking the interior of every such endpoint pair, the number of exact 916 consecutive-prime gaps hitting the dangerous event set was

\[
\boxed{0}.
\]

Per-q counts are frozen in the JSON result file.

Thus every one of these seven q witnesses remains forced throughout its complete post-global/pre-width seam.

---

## 7. New exact p=2 endpoint

The next unprocessed prime witness is

\[
q_{next}=78,553.
\]

Its global e=1 resource first ceases to be automatic at

\[
k_g(78,553)
=
2,822,453,183,434.
\]

Every smaller prime witness is already covered by the prior multiscale theorem or by the exact discrete seams above. Every larger q still satisfies the global e=1 resource before this k.

Therefore the least-basis classification extends exactly through

\[
\boxed{
K_{\mathrm{DR1}}
=
2,822,453,183,433.
}
\]

Under the declared external finite prime-gap resources:

\[
\boxed{
35,902\le k\le2,822,453,183,433
\Longrightarrow
\text{unique least safe divisor-witness basis}.
}
\]

The same 49 historical no-least basin indices remain the only failures in

\[
2\le k\le K_{\mathrm{DR1}}.
\]

Relative to `K85`, this adds

\[
\boxed{1,222,147,863}
\]

additional k-indices.

The certified endpoint is now approximately `242.0234` times the original Campbell-based endpoint `11,661,903,789`.

---

## 8. Repair complexity

Because the failure set remains unchanged and every one of those 49 residual hypergraphs has transversal number one,

\[
\boxed{
\tau(\mathcal R_k)\le1
\quad
\text{for every }2\le k\le2,822,453,183,433.
}
\]

The first possible p=2 repair-complexity jump is pushed beyond this new discrete endpoint.

---

## 9. Structural meaning

The important result is not the additional `1.22e9` k-values by itself.

A new proof layer has appeared:

\[
\boxed{
\text{real gap envelope}
\to
\text{floor-width deficit}
\to
\text{exact large-gap-start event}
\to
\text{reciprocal/power pullback}.
}
\]

The continuous multiscale certificate loses information when a real interval is shorter than the maximum gap by less than one integer. P2-DR1 recovers that information exactly.

This is the powered analogue of the earlier reciprocal-gap obstruction language, now with integer-floor phase included.

---

## 10. Next frontier: deficit two

At the next prime

\[
q=78,553,
\]

the initial q^2 real width is approximately

\[
914.810606.
\]

Therefore floor widths 914 and 915 both matter.

The next structural lemma should classify a general deficit

\[
D=G-d.
\]

If `a` is the previous prime at or below the cofactor floor `n`, and

\[
t=n-a,
\]

then a prime-free interval requires

\[
g(a)>D+t,
\]

where `g(a)` is the consecutive prime gap after `a`.

For `G=916` and `D=914`, failure can occur only when the floor lies at offset `t=0` or `1` from the start of an exact 916-gap.

That deficit-two event geometry is the next exact target. Direct enumeration of all floor events is no longer the right representation; the search should be driven by large-gap starts and their finite offset shadows.

Status remains:

`PROVED R005 STRUCTURAL + EXACT FINITE PATCH / EXTERNAL GAP INPUT DECLARED / NOT CANONICAL / LEAN PENDING / NOVELTY UNVERIFIED`.
