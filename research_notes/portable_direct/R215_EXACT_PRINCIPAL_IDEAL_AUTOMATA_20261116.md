# R215 — Exact principal-ideal cardinalities from Stirling fibres and pattern-avoidance automata

Date: 2026-11-16 (Asia/Shanghai)
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED
Research branch: `research/em-r1-r215-exact-ideal-count-20261116`

## Frozen inputs, object, and research scope

Frozen scientific starting point: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34` (unchanged).
Exact antecedents: R209's compatible-tail Stirling fibre formula, R213's Green ideal membership classification at `26bccd30c4afb00bf143acd7627eff9cdf954693`, and R214's quotient/grouped encoding at `1b7508f9f7f5b70f79052b7966f21221ba1f1ecf`.
P000 remains locked: the six native spatial axes, twelve signed directions and independent time are not redefined. All statements here concern a **finite typed observer monoid**, not the native physical dynamics, a three-dimensional slice, physical BRC propagation or a claim that direction/provenance data can be discarded for arbitrary future observers.

Fix integers `m>=1`, `k>=0`, `L>=1`. The alphabet is `A=[m] × ({0}∪[k])`, of size `a=m(k+1)`; tag 0 is neutral. For a word `w`, its observer state `F(w)=(s(w),t_L(w))` retains the last-occurrence order of nonneutral tags and the last `min(L,|w|)` complete paired events. Multiplication is induced by concatenation. `J=F(A*)`. For any state `x`, `U(x)` is its observed nonneutral support and `r=|U(x)|`. A state with tail length `<L` is exactly a short literal word `u`; a state of tail length `L` is full.

## Theorem A — exact *individual* Green-ideal cardinalities

Define the Stirling fibre counts (with `{n\brace j}` a Stirling number of the second kind)

```text
C(r,L) = sum_{j=0}^{min(r,L)} {L+1 \brace j+1}
W_r    = r! m^L C(r,L)
T_r    = sum_{j=r}^{k} binom(k-r,j-r) W_j.
```

For **every full state** `x` of support size `r`,

```text
|xJ| = |JxJ| = T_r.
```

For **every short state** `x=u` of word length `h<L` and support size `r`,

```text
|xJ|  = T_r + sum_{n=h}^{L-1} a^(n-h),
|JxJ| = T_r + sum_{n=0}^{L-1} (a^n - Avoid_u(n)).
```

Here `Avoid_u(n)` is the exact number of length-`n` words over `A` avoiding the contiguous factor `u`; for the empty word set `Avoid_empty(n)=0`. These are cardinalities of principal ideals in the **original full observer monoid J**, not just in the 8-bit Green-J quotient.

**Proof.** R209 gives `W_j` distinct full states for *each fixed support set of cardinality j*, by choosing `j!` last-occurrence orders and `m^L C(j,L)` compatible complete tails. By R213, a full state of support `U` lies in either principal ideal of `x` exactly when its support contains `U(x)`. Among supports of size `j`, there are `binom(k-r,j-r)` such supersets. Summing their distinct state fibres proves `T_r`; the full part depends only on `r`.

For full `x`, its right/two-sided ideals contain no short state, proving the first assertion. For short `x=u`, R213 characterizes short states in `xJ` as exactly those short literal words beginning with `u`; at each length `n>=h` there are `a^(n-h)`. Short states in `JxJ` are precisely short words containing `u` contiguously; their number at length `n` is `a^n-Avoid_u(n)`. The short and full sectors are disjoint. Adding the already-counted full-sector fibres proves both formulas. For the empty word, every word contains the empty factor, and both ideals are all of `J`. QED.

**Consequence.** The size of the principal right ideal of a short state depends only on its length and support size. The size of its principal two-sided ideal may depend on its internal paired-event pattern and self-overlaps even at fixed length and support. Full states of the same support cardinality have the same two sizes, although distinct support sets still define distinct ideals.

## Theorem B — exact KMP prefix-automaton count without enumerating J

For nonempty short pattern `u=(u_1,...,u_h)`, construct its classical proper-prefix/suffix transition automaton with states `0,...,h-1`: state `p` means the longest suffix of the word read so far agreeing with a proper prefix of `u` has length `p`. A transition that reaches `h` enters a forbidden match sink and is excluded. Let `d_n[p]` count match-avoiding words after `n` letters in state `p`, with `d_0[0]=1` and all other entries zero. Then

```text
d_(n+1)[q] = sum_{p=0}^{h-1} d_n[p] *
              #{c in A: delta_u(p,c)=q<h},
Avoid_u(n) = sum_{p=0}^{h-1} d_n[p].
```

Inductively the transitions count *each* avoiding word once; a word first matching `u` is removed forever. Thus the recurrence gives exact `Avoid_u(n)` for all `n<L`, proving an algorithm for the two-sided ideal cardinality using only the short pattern, the finite alphabet and Stirling fibres. Its arithmetic consists solely of nonnegative integer additions, multiplication and exact binomial/Stirling evaluations. With a straightforward KMP transition construction, the pattern-count portion takes `O(a h^2 + a h L)` elementary integer operations and `O(h + ah)` integer storage if transitions are stored (or `O(h)` DP storage plus on-demand transitions); bit complexity additionally depends on the integers' growing lengths. No exponential enumeration of `|J|` is required.

For the quotient `Q=J/Green-J` of R214, the same proof gives ideal cardinalities by replacing each full support-fibre weight `W_j` with 1. Equivalently the full-sector term becomes `2^(k-r)`, leaving the short-word pattern counts unchanged. This is an exact query-specific reduction; the full-J result above retains the richer R210 action carrier.

## Exact overlap witness, including right-vs-two-sided contrast

Take `m=1`, `k=1`, `L=4` and write source tags as letters `0,1` (one direction). The short patterns `u=11` and `v=10` both have length `h=2` and support cardinality `r=1`.

```text
W_1 = {5 \brace 1} + {5 \brace 2} = 1+15 = 16,
T_1 = 16,
|uJ|=|vJ|=T_1+1+2=19.
```

In lengths `0,1,2,3`, `11` occurs in `11, 011,110,111` (4 short words), while `10` occurs in `10,010,100,101,110` (5 short words). Consequently

```text
|J(11)J|=16+4=20,       |J(10)J|=16+5=21.
```

The two right ideals have the same cardinality, but the two-sided ideals have different cardinalities. This resolves R213's overlap observation with an exact automaton counting mechanism.

## Native X6-sized observer counts (not a BRC timing benchmark)

Set `m=12,k=6,L=2,a=84`. From `W_r` the full-state principal ideal counts for `r=0,...,6` are

```text
T_0=1,407,600
T_1=1,174,176
T_2=986,400
T_3=833,760
T_4=708,480
T_5=604,800
T_6=518,400.
```

The original monoid has `1,407,685` states. A one-event short state carrying one selected source has a right/two-sided ideal of `1,174,177` full-observer states. No raw direction/source tail is discarded for subsequent native BRC operations merely by computing this integer ideal size.

## Exact finite validation, evidence and next questions

The accompanying `R215_principal_ideal_automata_check.py` constructs the monoid by generator BFS for ten declared small parameter models, computes its full multiplication table using independently retained representative words, then explicitly calculates every state's principal right and two-sided ideal set. It checks all predicted sizes against these sets, and separately checks the Stirling state count and overlap witness. These finite checks are independent corroboration of the symbolic proof, not an all-parameter exhaustive proof. Only Python standard-library integer operations were used; no floating point, generic propagator, trigonometric functions or physical residual attribution.

Verification output: `R215_verification.json`, result `PASS`, ten complete models, 348 distinct states checked, 21,458 pairwise table products. The program was executed locally before publication. The installed `enterprise_math` package/EffectHistogram adapter was not available in this local environment, so the native BRC integration benchmark remains `NOT_EXECUTED`. Independent review: `NOT_REVIEWED`.

Further work: (1) compute exact per-state ideal sizes from R214's grouped 21-bit action ranks with partial decoding and prove/update a bit-complexity bound; (2) construct a noninvasive native BRC `EffectHistogram` test using the 8-bit quotient solely as an ideal-query readout, preserving tagged effects, rational weights, multiplicities and R203 cross moments; (3) continue R205's 31–35 dimensional binary-affine minimality question for depth 2.
