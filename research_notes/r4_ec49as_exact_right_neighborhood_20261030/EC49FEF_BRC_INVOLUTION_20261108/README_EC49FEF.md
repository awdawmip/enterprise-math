# EC49FEF — Signed-X6 BRC cache-key / native-prefix involution

Date: 2026-11-08. Author-side exact mathematical result and finite computation. Scientific inputs remain frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Reuse EC49FEB (108 late triples), EC49FED (28 early configurations) and EC49FEE (native-prefix 0–1 MIP). P000 and ACTIVE worldview are unchanged.

## Exact theorem

Let the operation alphabet be `a c d e f g`, with ordered native signed X6 step words:

```
a=(-1,-1); c=(+1,+2,-1,-2); d=(+2,+1,-2,-1);
e=(+3,+1,+1,-3); f=(+1,-1); g=(+2,-2).
```

Define the letterwise involution `I=(c d)(f g)`, leaving `a,e` fixed. It acts on words and finite word sets. The following statements hold for **every** finite set of operation words in the frozen model:

1. `I` preserves operation-word length and every path's final signed six-axis displacement. The full positive BRC key transforms according to
   `K(x,y,z)=(y+2z,x-2z,z)`; `K(K(k))=k`. In particular, valid endpoint `+2E1` remains valid.
2. Let the nine-state DFA transitions be `T` from the frozen original kernel. Then `sigma=(2 3)(4 5)(6 7)` (states 0,1,8 fixed) satisfies `sigma(T(q,s))=T(sigma(q),I(s))` for every state and letter: **54 exact identities**. The output signature permutation is `pi=(1 4)(2 8)(16 32)`, with zero fixed. The rank-nine clauses `(16|2),(16|4),(32|1),(32|8)` permute among themselves. This preserves all observer rank-nine conditions and exact per-window quotas.
3. Writing `Ch(v)` for outgoing letters in the operation-word Trie, the native prefix cost is exactly
   `C_native(W)=sum_v sum_(s in Ch(v)) |OPS(s)| - N_cf(W) - N_dg(W)`.
   Six native codewords are prefix-free. The only partial one-step overlap at a shared operation-Trie node occurs between `c/f` (first step +E1) or `d/g` (first step +E2). The involution interchanges these two overlap types, preserves codeword length and the Trie, so
   **`C_native(I(W))=C_native(W)`**.

Proof: `a` contributes net `-2E1`, `e` contributes `+2E1`, and the other four letters have zero displacement. Each of the positive-key components changes as the explicit K formula under c/d and f/g swapping. The DFA conjugacy follows by checking its 9x6 transition table; initial state 0 is fixed, so all finite word sequences inherit it. Prefix-freeness permits a symbol-Trie edge accounting with precisely the two local overlap corrections above. All formulae are exact integer identities, not a numerical approximation.

The involution is an **operator/observer symmetry**; since `e` is left intact, it is not a physical global swap of the E1/E2 axes and does not alter P000.

## Quantitative orbit reduction

The 108 quota-feasible late triples of EC49FEB form `A x B x C`, with
```
A: (3,2,1) (4,1,1)
B: (3,4,1) (4,3,1) (5,2,1) (5,2,2) (6,1,1) (6,1,2)
C: (4,6,1) (5,5,1) (6,4,1) (6,4,2) (7,3,1)
   (7,3,2) (8,2,1) (8,2,2) (8,2,3)
```
Each factor is K-stable and K exchanges both A entries. Therefore **108 late configurations form exactly 54 two-element orbits**. The EC49FED 28 early configurations are closed under I and form **15 orbits** (13 pairs and two fixed configurations); the 108x28=3024 full fixed-input models form **1512 pairs**, since the A factor has no fixed point. Paired models have exactly equal minimum native-prefix costs, and a feasible-word set/valid lower-bound proof can be transferred by I. This analytically accounts for equal EC49FEE histograms at late configurations `((4,1,1),(5,2,1),(7,3,1))` and `((3,2,1),(4,3,1),(5,5,1))`.

Local independent exact check: 54/54 DFA conjugacy equalities, all 108 late triples / 54 orbits, the old 28 configurations and 56 old complete systems rechecked under I. The separately replayed 56 previous feasible systems retain their native cost.

## New two exact MIP instances and their mirrors

Fix EC49FED early configuration index 20 (35 native edges), `A=(3,2,1)` and `B=(3,4,1)`. Using the **unchanged** published EC49FEE 0–1 native-prefix Trie MIP, solve late groups:

| C | HiGHS status | late optimal value / bound | total native edges |
|---|---|---|---|
| (4,6,1) | OPTIMAL, gap 0 | 83 / 83 | **118** |
| (5,5,1) | OPTIMAL, gap 0 | 83 / 83 | **118** |

Both complete 24-word witnesses are in `EC49FEF_WITNESS.json` and are independently checked by `EC49FEF_CHECK.py`; transporting them through I yields two additional 118-edge complete systems with `A=(4,1,1),B=(6,1,1)` and respectively `C=(8,2,1)`, `C=(7,3,1)`. The exact equivalence transfers their optimality within the paired fixed-input models. These two MIP dual bounds are solver reports; no independent branch-and-bound certificate is claimed.

A bounded exploratory orbit scan also attempted other triples; cases without a completed optimality report are explicitly retained as exploratory and not used for global exclusion. The mother goal remains **at most five full BRC keys and at most 93 native-prefix edges**. The previously recorded 94-edge construction remains the better mother-problem upper bound.

## Reproducibility and next EC49FEG

Run `python EC49FEF_CHECK.py` in this directory to check the exact finite identities and four full constructions. For the two MIP optimality reports, use EC49FEE's previously published `EC49FEE_OPT_TRIE.py` and `EC49FED_NATIVE_CORE.py` without changing the frozen operators; run `solve((3,2,1),(3,4,1),C,early_index20,time_limit)` for the two C values.

Next: use the 54-orbit quotient to prioritize exact target-93 tests without duplicate mirror searches; separately group the 12 optional H5 mixed-key schedules into their 6 involution pairs. This is author-side portable mathematical evidence, pending actual native owner/claim and independent Driver review.
