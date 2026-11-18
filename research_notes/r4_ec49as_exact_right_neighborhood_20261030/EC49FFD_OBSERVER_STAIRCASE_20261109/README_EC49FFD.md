# EC49FFD — Exact full-BRC-key observer staircase and five-key interval census

Date: 2026-11-09 (Asia/Shanghai). **Scientific pin (unchanged):** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Scope: frozen six-operation native signed-X6 BRC model, original nine-state DFA, complete keys K=(x,y,z), horizons H2–H9. This is an author-side result, not a Source-native Result, CLAIM, Driver review or Foundation promotion.

**Prior evidence:** `EC49FFC_LENGTH_DOMINANCE_20261109/VERIFY_EC49FFC_COMPACT.py` at immutable author commit `2dd856c416f111d90d523dcb10cde952248ec814` defines the exact operation alphabet `a,c,d,e,f,g`, DFA and observation labels. EC49FFC Theorems A/C establish fixed signed-native length/endpoint and count-admissible horizon intervals. All observer and cost semantics are preserved.

For an operation word of horizon h, the complete-key identities are:
```
#a=z-1, #e=z, t=#c+#d=x+y-h-1,
#f=h+1-y-2z, #g=h+1-x.
```
All counts are nonnegative integers. Let S(h,K) denote the union of **nonzero** terminal DFA signatures over every admissible ordering and every split of t between c and d. Put L={1,2,4,8}, B={16,32}.

## Theorem A: exact observer-support dichotomy (all count-admissible h)

```
t>=1  => S(h,K) = {1,2,4,8}.
t=0   => S(h,K) = ({16} if #f>0 else empty)
                   union ({32} if #g>0 else empty).
```

**Proof.** For the original DFA, consuming any c or d moves the state into the forward-invariant class {2,3,6,7,8} (state 8 is an output-zero sink). Thus no word containing c or d can end at high states 4 or 5. All four low signatures are attained, without changing K: choose every c/d occurrence to be c and begin with c^t, reaching state 2 (label 4); replace c by d, reaching state 3 (label 1). Since #e=z>=1, instead begin with e c^t or e d^t, reaching states 6 (label 8) or 7 (label 2). Append all remaining a,e,f,g steps: they fix each of those four respective states. If t=0, only a,e,f,g occur. Initial f enters absorbing-with-respect-to-these-letters state 4 (label 16), initial g state 5 (label 32), and initial a/e state 1 (output zero). Both claimed high labels are realized exactly when their corresponding letter count is positive. This also proves no other nonzero outputs exist. Every constructed word satisfies the original count and complete BRC key; the signed-native endpoint follows EC49FFC Theorem A. QED.

## Theorem B: every complete key has an observer staircase

For any key admitting a count-feasible horizon, let
```
H(K)=x+y-1,     r(K)=min(x-2*z,y).
```
EC49FFC Theorem C gives exactly `H(K)-r(K) <= h <= H(K)`. Every earlier integer horizon in this interval supports **all four** low labels, and the unique terminal horizon H(K) supports only the high subset
```
{16 if x>2*z} union {32 if y>0}.
```
In particular, **full high B at h iff H(K)=h and full low L at h-1** (when the immediately preceding horizon is included in the declared range). Indeed, at terminal h the counts are `#f=x-2z`, `#g=y`, and passing to h-1 changes `t:0->1, f->f-1, g->g-1`. The preceding horizon is feasible iff f,g>=1, exactly the full-high condition. QED.

**Reuse consequence:** a single full key cannot emit high at two horizons, or high and low at the same horizon. A full-high key at h simultaneously supplies full low at every earlier horizon h-r,...,h-1. This is label support, not equality of ordered six-axis native prefixes: retain the full word order for cost calculations.

## Corollary: closed-form finite census

At horizon h let n=h+1-2z. Every feasible key has a unique t,f,g>=0 with t+f+g=n and K=(t+2z+f,t+g,z). Therefore
```
N_full_low(h) = sum_{z=1..floor(h/2)} binom(h+2-2z,2)
N_full_high(h)= floor((h-1)^2/4)
N_16_only(h) = N_32_only(h) = floor(h/2)
N_zero(h) = 1 when h odd, otherwise 0.
```
For H2–H9 respectively, counts (full-low, 16-only, 32-only, full-high, zero) are:
```
H2 ( 1,1,1, 0,0)    H3 ( 3,1,1, 1,1)
H4 ( 7,2,2, 2,0)    H5 (13,2,2, 4,1)
H6 (22,3,3, 6,0)    H7 (34,3,3, 9,1)
H8 (50,4,4,12,0)    H9 (70,4,4,16,1).
```
There are 294 horizon/key count-feasible pairs, 164 distinct full keys, 270 pairs with strictly positive x,y,z. Four zero-observation pairs have y=0.

## Corollary: all 15 EC49FEO signature-feasibility families reduce to interval cover

The exact 22-word templates require full L at H2, full B at H3, and four full-B / two full-L horizons among H4–H9. With five high horizons and at most five complete keys, Theorem B forces precisely one distinct full-high key K_h for each high h. Because a complete key can be high only once, all other required low horizons must lie in the **preceding low intervals** of those same five keys. Conversely, the explicit words in Theorem A provide every required signature whenever these intervals cover all low horizons. Thus interval coverage is a necessary-and-sufficient test for **signature quota feasibility**, without enumerating words or considering native-prefix costs.

At high horizon h the number of eligible full-high keys is floor((h-1)^2/4), with a unique key (3,1,1) at H3, automatically supplying low at H2. Iterate all choices of four late high horizons, then all Cartesian products of their full-high key options; check `forall low l: exists key K with H(K)-r(K)<=l<H(K)`. This gives exactly **42,048** key inventories, **27,732** signature-feasible and **14,316** signature-infeasible across **15** templates, independently reproducing the EC49FEO quota census. H9 must be one of the high horizons: otherwise all five keys have high endpoints at H3–H8 and cannot supply low at H9. Hence five of the fifteen families are immediately impossible at the signature layer.

The previously recorded 94-edge exact minimum for these templates is **not proved by interval coverage**: it also requires the distinct ordered signed-native prefix-cost certificates from EC49FEO. The new contribution is a symbolic, horizon-general, independent observer-support theorem and a much smaller exact quota oracle.

## Executed evidence and bounds

`VERIFY_EC49FFD.py` independently computes every terminal DFA state reachable from each operation-count multiset, with memoized exact integer bitmasks. Over **all 294** count-feasible (h,K) pairs, and all c/d splits, the observed output support matches Theorem A with **0 discrepancies**, using **2,380** cached multiset states. It independently reproduces the full 15-family interval census: 42048 / 27732 / 14316. The computational check is finite H2–H9 evidence; the DFA transition-invariance argument above proves the support staircase for arbitrary admissible h. Code includes all source DFA constants and uses only Python standard library. No floating-point computation or external solver is required.

**BRC interface used:** full key -> integer horizon interval -> exact reachable DFA labels -> retain original ordered signed-X6 words for native-prefix optimization. Replacing the last stage by only (h,K) would erase path-order residuals relevant to the cost observer.

## Next question

Construct a minimum-key signature interval-cover oracle for arbitrary H2–H9 observation-support targets, including cases with fewer full-high horizons where 16 and 32 may come from *different* keys. Search the inclusion-minimal rank-nine supports outside the already classified 22-path and 23-path families, then perform native prefix optimization only on surviving feasible key inventories. Keep frozen science, exact task publication/owner/CLAIM, and Driver admission scopes distinct.
