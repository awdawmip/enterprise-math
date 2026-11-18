# PREFIX-915 — Exact source-preserving collision multiplicity in named XOR two-port observations

Date: 2026-11-19 (Asia/Shanghai). Lane: 进取数论研究6.
Status: AUTHOR_PROVED / FINITE_SMALL_STATE_EXHAUSTIVELY_TESTED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Scientific input remains frozen at `f42f2906d77f24085c123f3ccfe9667d41caa96d`; current behavioral norms are separately read at main.
Direct predecessors: PREFIX-913 (all-sign signed-dyadic construction), PREFIX-914 (exact +146,518 ordered modulus pairs over PREFIX-912).
This note studies the same auxiliary labeled-XOR observation, not an X6-native event admission or a new candidate of immutable task publication.

## 1. Result and its research value

Earlier sufficient certificates counted whether a modulus pair had **at least one** collision. This note counts the **distinct labeled trajectory pairs** that can be constructed from one fixed signed-dyadic identity. The result is an exact integer fiber multiplicity formula, preserving the start state and both named flip-source indices. It is a refinement of a Boolean collision-support observation, not a new modulus-pair coverage count.

Let `p>=2`, `N=2^p`, `0<=j<i<p`. A named trajectory is
`F_x^t=(x, x XOR 2^t)`, with `0<=x<N`, `0<=t<p`. For positive integers `a,b,k,ell`, put `A=ka`, and choose `eps,eta in {-1,+1}`. Assume `0<A<N` and

```text
k*a - ell*b = eps*2^i - eta*2^j .              (1)
```

Observe `Phi_(a,b)(u,v)=(u mod a,v mod b)`; the observer may merge states, but the pre-observation trajectory labels remain distinct.

**Theorem 915-A (exact multiplicity).** The number of distinct unordered pairs of labeled trajectories of the fixed form

```text
{F_x^i, F_(x+A)^j}
```

with the specified signs `x XOR 2^i=x+eps*2^i` and `(x+A) XOR 2^j=(x+A)+eta*2^j`, and with both p-bit endpoints, equals

```text
L = N-A,  H=2^i,  T=2^(i+1),  q=floor(L/T),  t=L mod T,
bi = 1 if eps=-1 else 0,  bj = 1 if eta=-1 else 0,
u = max(0,min(H,t-bi*H)),
G_j(z) = floor(z/2^(j+1))*2^j + max(0,(z mod 2^(j+1))-2^j),
d = G_j(A+u)-G_j(A),

M = q*2^(i-1) + (d if bj=1 else u-d).         (2)
```

Each pair counted by `M` is a collision under `Phi_(a,b)`. In particular,

```text
M >= floor((N-A)/2^(i+1)) * 2^(i-1).           (3)
```

The formula is exact for all parameters in the stated domain; there is no headroom approximation.

**Theorem 915-B (quarter-state invariant).** If `eps=+1` and `0<A<=2^i`, then

```text
M = 2^(p-2) = N/4,                             (4)
```

independently of `j`, `eta`, and the value of `A` within that range, subject to (1). This is a count of source-distinct collision pairs for a single fixed parameter identity, not a count of different modulus pairs.

## 2. Proof

The bit identity `z XOR 2^t=z+2^t` holds exactly when bit `t` of `z` is zero; `z XOR 2^t=z-2^t` holds exactly when it is one. Thus the required signs are equivalent to two Boolean conditions:

```text
bit_i(x) = bi,   bit_j(x+A) = bj.              (5)
```

Since `A>0`, the two starts differ. Both starts fit within `0..N-1` precisely for `0<=x<N-A=L`; each XOR remains p-bit. Whenever (5) holds, the observed first endpoints differ by `A=ka`. The observed second endpoints differ by

```text
(x+A+eta*2^j) - (x+eps*2^i)
 = ka - eps*2^i + eta*2^j = ell*b
```

by (1). Both observer moduli therefore see equal residues. Because the two source indices `i` and `j` differ, their labeled trajectories cannot be exchanged while preserving the fixed index roles: distinct `x` give distinct unordered labeled pairs.

Count (5) on one complete interval of `T=2^(i+1)` consecutive start states. Exactly the prescribed half-block of length `H=2^i` has bit `i=bi`. Since `j<i`, `H` is divisible by `2^(j+1)`. Within that half-block, as `x` runs, the bit `j` of `x+A` equals each Boolean value exactly `H/2=2^(i-1)` times, regardless of `A`. This proves the full-period summand in (2) and lower bound (3).

For the partial period `0<=x<t`, the intersection with the wanted high-bit half-block is the interval

```text
bi*H <= x < bi*H+u, with u=clamp(t-bi*H,0,H).
```

Here `2^i` is divisible by `2^(j+1)`, so translating by `bi*H` does not change bit `j`. The prefix function `G_j(z)` is exactly the count of integers in `[0,z)` whose bit `j` equals 1. Hence the number of requested low-bit-one positions is `d=G_j(A+u)-G_j(A)`; low-bit-zero positions number `u-d`. Formula (2) follows.

For (4), since `eps=+1`, every eligible `x` has bit `i=0`. In the last period of `[0,N)`, all such `x` satisfy `x<=N-H-1`. If `A<=H`, then `x+A<N` automatically. Thus no otherwise eligible start is lost at the end of the p-bit state interval. Over all `N/T` complete periods, condition (5) has exactly `(N/T)*(H/2)=N/4` solutions. QED.

## 3. Large-domain exact instances

The previously established PREFIX-914 new modulus pair `(a,b)=(321651,440665)` has

```text
k=3, ell=1, i=20, j=19, eps=eta=+1,
A=3a=964953 <= 2^20=1048576,
3a-b=524288=2^20-2^19.
```

Therefore (4) gives **exactly 1,073,741,824** distinct labeled trajectory-pair collisions for this single observer `Phi_(321651,440665)` and one fixed signed-dyadic representation. Its individual witness from PREFIX-914 is `F_83623^20=(83623,1132199)` and `F_1048576^19=(1048576,1572864)`. The observed port differences are `964953=3a` and `440665=b`.

Here `a*b=141740337915 > 33*2^32=141733920768`. Hence the earlier **total capacity** pigeonhole lower bound alone is zero, while (4) proves more than a billion concrete source-distinct collision pairs. This gives a strictly stronger quantitative observation at an already certified modulus pair; it does not increase the PREFIX-914 cumulative set size `7,795,676,346`.

For the earlier PREFIX-913 pair `(271999,521085)` and `(k,ell,i,j,eps,eta)=(3,1,18,15,+1,-1)`, the exact truncated formula (2) gives **1,073,610,752** source-distinct witness pairs, compared with the untruncated quarter-state value `1,073,741,824`. This example exercises the nontrivial tail correction.

## 4. Validation

Companion: `research_notes/portable_direct/PREFIX915_R6_EXACT_MULTIPLICITY_CHECK.py`.

- Python 3 arbitrary-precision integer `G_j` implementation, with exhaustive direct state/bit tests for every `2<=p<=9`, every `1<=A<2^p`, every `0<=j<i<p`, and all four sign combinations: **118,288 parameter cases, zero mismatches**.
- Both 32-bit instances evaluated from (2) and their explicit modular XOR representatives checked using exact integer arithmetic. The large counts are formula-derived, **not 2^32-state brute force**.
- The proof counts a **fixed oriented index-role family of unordered labeled trajectory pairs**. Different parameter identities may count some of the same pairs; summation across identities requires separate de-duplication.

## 5. Next frontier and control

A useful next unit is to aggregate the same-modulus collision-multiplicity fibers over multiple signed-dyadic identities while avoiding duplicate labeled trajectory pairs. Another is to use the exact terminal-tail formula to extend admissible large `k,ell` beyond previously uniform-headroom regimes. Preserve Boolean modulus-pair coverage, labeled collision pair mass, and native X6 event admission as different typed claims.

This note is independent auxiliary mathematics. Historical researcher identities are provenance only; no shared X6 CLAIM, native time event, working-truth promotion or formal Result is asserted by this GitHub research publication.
