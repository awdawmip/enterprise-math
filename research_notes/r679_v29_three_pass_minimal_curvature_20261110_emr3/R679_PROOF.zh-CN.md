# R679｜三元 PASS 最小非平坦输运与中间事件分支证书

Date: 2026-11-10 Asia/Shanghai
Task: RS-X6-GLOBAL-TRIADIC-FIELD-NETWORK-LAW / TP2-47D65B35A7D48082EFBB
Frozen science: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f
Predecessor: R678@298a433b91aa21bec8832051a7a440b3b565b97e
Status: AUTHOR-SIDE EXACT FINITE PROOF; independent Driver review pending.

## 1. Definition and exact question

Use V29 nonnegative integer count ledger at a shared X6 Cell o:
M[a,b], Rin[a], Rout[a]≥0. Signed observables are Ω=M−Mᵀ and u=Ω1+Rin−Rout. The four internal port labels are distinct from native six-axis X6 Cell displacement labels.

V23 maps each 3-subset S of {0,1,2,3,4,5} to c(S)∈{−1,0,1}⁴. The four ordered perfect matchings (each coordinate independently) are:

- ((0,1),(2,3),(4,5))
- ((0,2),(1,4),(3,5))
- ((0,3),(1,5),(2,4))
- ((0,4),(1,3),(2,5)).

For each matching c_j(S)=0 unless S meets each pair in exactly one endpoint. If it does, c_j(S)=+1 if the number of second endpoints selected is even, and −1 otherwise. All 20 codes are distinct. N(S) consists of the 9 triads T with |S∩T|=2. V27 scores T using

```
Φ(S,T) = u·c(T) + c(S)ᵀ Ω c(T),   T∈N(S).
```

A strict selector means the maximum is unique at *every* one of the 20 source triads. Given the 20-state deterministic map f, recurrent cycles carry V17 slot transport: shared axes keep their slot, the departing axis transfers its slot to the entering axis. A cycle is nonflat when its final permutation of the base three slots is not identity.

Start at arbitrary integer baseline bias u∈Z⁴ created by matched inter-Cell boundary TRANSFER events on a declared extension of the X6 interaction graph, with no internal PASS initially (Ω=0). Complete the three distinct V29 primitive PASS events, in any order:

```
A = PASS(o;0→1),  B = PASS(o;1→2),  C = PASS(o;2→0).
```

Each PASS increments precisely the corresponding nonnegative M entry. Its Δu is e_source−e_target. Therefore all three collectively have Δu=0 and yield

```
M[0,1]=M[1,2]=M[2,0]=1, all other M[a,b]=0
Ω = [[ 0,+1,−1,0],
     [−1, 0,+1,0],
     [+1,−1, 0,0],
     [ 0, 0, 0,0]].
```

The nonzero 3×3 block has kernel span(1,1,1); a 2×2 nonzero minor proves rank Ω=2. PASS preserves local scalar sum 1ᵀu and matched TRANSFER preserves global V29 charge Q.

**Question:** among all integer u, what is the least ||u||₁ such that the *completed* three-PASS state has a strict V27 selector on all 20 triads **and** at least one nonidentity recurrent V17 slot holonomy? How many minimal examples are there, and what are the selector ambiguities after each primitive PASS prefix?

## 2. Theorem: exact minimum is 19

The exact minimum is

```
min{||u||₁ : globally strict completed V27 map with nonflat recurrent V17 cycle} = 19.
```

Precisely six integer u of norm 19 attain it:

```
(-4,-3,-2,+10)   (-3,-2,-4,+10)   (-2,-4,-3,+10)
(+2,+4,+3,-10)   (+3,+2,+4,-10)   (+4,+3,+2,-10).
```

For each, the completed deterministic 20-state map has a nonflat six-cycle with slot holonomy (2,1,0) and a flat two-cycle. The V27 known witness u=(-2,-4,-3,+10) exhibits 012→123→234→034→035→025→012.

**Complete finite proof.** For each k=0,...,19 enumerate the exact shell B_k={u∈Z⁴:Σ|u_i|=k}. Recursively select all four nonnegative magnitudes summing to k and independently both signs for each positive coordinate. Every vector appears exactly once and every vector of that norm is reached. Independent cardinality formula for k>0 is

```
|B_k| = Σ_{j=1}^{min(k,4)} 2^j * binom(4,j) * binom(k−1,j−1);
|B_0|=1.
```

For every u compute 180 exact integer V27 scores, reject any u with a tied maximum for any S; otherwise enumerate the 20-state functional graph's recurrent cycles, transport the three V17 slots around each cycle, and test nonidentity. The accompanying executable exact-integer checker uses Python standard library only; its finite search is exhaustive, not sampling. Its complete output by k (tested / globally strict / nonflat recurrent) is:

```
k= 0      1       0       0
k= 1      8       0       0
k= 2     32       0       0
k= 3     88       0       0
k= 4    192       0       0
k= 5    360       0       0
k= 6    608       0       0
k= 7    952       0       0
k= 8   1408       6       0
k= 9   1992      18       0
k=10   2720      36       0
k=11   3608      78       0
k=12   4672     150       0
k=13   5928     312       0
k=14   7392     438       0
k=15   9080     756       0
k=16  11008     984       0
k=17  13192    1560       0
k=18  15648    1878       0
k=19  18392    2862       6
```

Total exactly 97,281 integer four-vectors. The first 19 shells contain no nonflat strict selector. At norm 19 the six fully listed exact vectors pass, yielding both lower and upper bounds 19. This proves the minimum over the *entire* declared integer four-vector domain.

In the *separated boundary-first event class*, one matched TRANSFER incidence at shared o changes exactly one component of u by ±1. Thus a baseline vector u requires at least ||u||₁ such incidents. An explicitly extended graph with an allowed native single-axis boundary edge for each needed direction realizes each signed unit by a matched TRANSFER. Hence exactly 19 boundary transfers plus the stipulated three internal PASSs give **22 primitive events** at the stated minimum. This minimum is scoped to that separated construction, not all possible interleaved/autonomous networks.

## 3. Theorem: all 36 minimum-cost PASS orders are nonstrict mid-batch

For *each* of the six minimal u and *each* of the six permutations of ABC, recompute u and Ω from the actual ordered primitive PASS increments after prefix lengths 0,1,2,3, and compute all 20 sets of maximizers. The exact strictness signature is universally

```
[True, False, False, True].
```

Thus all 36 positive label-distinguished histories have at least one co-maximizer at both intermediate times, yet strictness at the start and after the completed batch. The accompanying JSON contains, for each branch and each stage, the number of source triads with winner-set cardinality 1/2/3/... and the product of all 20 choice counts.

A faithful discrete **positive BRC** carrier is the six-element labeled set of PASS orderings for each fixed u, with positive unit weight per history and ordered concatenation as serial composition. It retains prefix provenance and winner-set multiplicities; projection to completed M, u, Ω merges all six histories. No signed/complex amplitude cancellation or physical heartbeat propagation is asserted. This is an exact observer/future-operations test.

## 4. Reproduction and next problem

Run `python R679_VERIFY.py`. The final line must be `R679_THREE_PASS_MINIMAL_CURVATURE_BRC_EXACT_PASS`. The local source also contains `R679_CORE.py` and full `R679_EVIDENCE.json` in the downloadable package; that compact checker independently reproduces all 97,281 cases and all 36 intermediate histories. Arithmetic is exact finite integer/set arithmetic, not physical π/trigonometric propagation.

The completed-batch strict map is a *static* future selector. To obtain a genuinely autonomous time-resolved X6 update, build a source-backed rule for the active triad, V17 frame and future legal branches **at each primitive PASS/TRANSFER**, track V39 loop current j, and test the typed R675 rotation/port equivariance. Preserve nonnegative V29 counts, genuine event time, the R462 frozen science pin, original authorship and Driver-independent review.

Sources: `research_notes/X6_ATOMIC_TRIADIC_PASSAGE_DRIVES_ODD_HOLONOMY_V27_20260906.md`, `research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md`, R678 @ `298a433b91aa21bec8832051a7a440b3b565b97e`.