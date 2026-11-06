# Stage473-B — exact two-POP/two-APPEND repair and positive BRC support

**Date:** 2026-11-06. **Status:** AUTHOR_SIDE_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED.

## Provenance and scientific domain

Continuation of Stage472-B at immutable author-side commit `a1cd75d5c5eb56b5f964115df83c11d370a3faa1` (Draft PR #1736). Preserve frozen scientific inputs: GLOBAL main `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, Enterprise Math main `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 Git blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current applicable behavioral policy is read independently from the verified canonical main; it does not re-pin science.

Original histories `P=(P_1,...,P_m)` and `Q=(Q_1,...,Q_n)` satisfy `4<=m<n`, have first letter A and take letters in `Sigma={A=+E1,B=+E2,C=+E3}` inside the native signed six-axis space. The fixed initial observer `Phi(P,Q)` contains both lengths, full signed six-dimensional endpoints, complete 12-by-12 ordered adjacency matrices for P and Q and `K=sum_(i=1)^m [P_i=Q_i]`. The positive BRC raw population assigns integer branch mass 1 to each original ordered pair. No history order, source identity or multiplicity is quotiented away before the specified future observer is checked.

A future is a finite labeled legal action sequence with cumulative budgets `POP_P<=2`, `APPEND_P<=2`, `POP_Q<=h`, `APPEND_Q<=1`. POP removes a last step but cannot reduce a word below length 1. APPEND chooses any one of all twelve signed X6 directions, and a newly appended step may itself be popped. Full observers are read after every action (equivalently, at every labeled future node). Put `t=max(1,n-h)`.

Define the old repair word explicitly, using inclusive 1-based positions and empty intervals:

```
L_t = ( Q_t, ((P_i,Q_i))_(t<i<=m), (Q_i)_(max(t+1,m+1)<=i<=n) )
R469 = (L_t, P_(m-1), [Q_m if t>m], [Q_(m+1) if t>m+1]).
```

`R469` is the prior Stage469-B author-side repair. This manuscript gives an independent proof for the enlarged action language, without assuming Stage469-B's semantic theorem.

## Theorem 473.1 — exact future-equivalence repair

On **each fixed complete initial observer fiber**, two original histories have identical complete labeled future observations under the enlarged language if and only if the following repair keys agree:

```
R473 = (R469, P_(m-2), Q_(m-1), [Q_(m+2) if m+2<=n]).
```

Duplicated coordinates and coordinates already fixed by `Phi` may be omitted when encoding an implementation key. Therefore the enlarged language introduces at most three additional ternary labels beyond `R469`: `P_(m-2)`, `Q_(m-1)` and `Q_(m+2)`. This is an exact equivalence characterization; it is not a claim that all three labels are independent on every fiber.

### Necessity: recover every label by legal observations

* The original directed adjacency and fixed first letter A determine the final original step in each history: for every letter x, `out(x)-in(x)=[x=A]-[x=last]`. After k successive POPs, the same identity determines the resulting final direction. Hence `P_(m-1)` and `P_(m-2)` are recovered after one and two P POPs; `Q_t` is recovered after the maximum legal Q POPs.
* Every `Q_i` with `i>t` is recovered by successive Q POP endpoint differences. For every `t<i<=m`, first POP Q down to length `i-1`, then APPEND Q with a chosen signed direction a. The increment in position-match K is `[P_i=a]`. Running the labeled alternatives for all a recovers `P_i` individually. Thus all pairs in `L_t` are observable, including the Q suffix above m.
* To recover `Q_m`, POP P once and APPEND a at position m; to recover `Q_(m+1)`, APPEND P once. When these letters already belong to `L_t`, these probes are redundant. Otherwise each is exactly the isolated tag of `R469`.
* To recover `Q_(m-1)`, POP P twice (current P length m-2), then APPEND a; the K increment is `[Q_(m-1)=a]`. To recover `Q_(m+2)` when present, APPEND P twice without POP and inspect the second K increment. Again the twelve signed alternatives determine the full original letter.

All probes respect the individual budgets. Therefore any two future-equivalent histories have equal `R473`.

### Sufficiency: reconstruct every future observer

Fix `Phi` and `R473`. Both original last directions `P_m,Q_n` are determined by the initial directed adjacency and fixed A. The full list of original P steps that can be removed is `P_(m-1),P_m`, plus `P_(m-2)` as the resulting boundary. The full list of original Q steps that can be removed is `Q_(t+1),...,Q_n`, plus `Q_t` as the resulting boundary. These labels are contained in `R473` or are fixed by `Phi`. Consequently, after any action word, both endpoint vectors and full ordered adjacency counts are reconstructed exactly by subtracting removed original edges and adding the explicitly labeled new edges, including popped appended steps.

For K, a P action can modify original positions `m-1,m` and insert new P positions at most `m+1,m+2`; a Q action can change positions strictly after t. The original equality indicators at all potentially removed common positions are known: for `i>t` they occur as paired `(P_i,Q_i)` in `L_t` (when `i<=m`); at `i=m-1,m` they follow from `P_(m-1),P_m` and `Q_(m-1),Q_m`; and original positions beyond m carried no initial K term. Every new comparison generated by an append at `i<=m-2` uses `P_i` from `L_t` whenever a Q append can reach it (`i>t`); new comparisons at `m-1,m,m+1,m+2` use the explicit repair letters or chosen appended directions. Thus the initial K minus removed original indicators plus all remaining/created indicators determines future K. The calculation respects interleavings and whether a currently popped step was original or appended.

Induction over the labeled action word now reconstructs every observer in the full future tree. Equal `R473` suffices. Combined with necessity this proves Theorem 473.1 for every finite nonnegative h and the declared P/Q budgets.

## Theorem 473.2 — exact nonnegative BRC support, masses and ranking

For fixed original alphabet size three and explicit input lengths m,n, the supported `R473` keys, population `M(k)=#{(P,Q): Phi(P,Q)=phi,R473(P,Q)=k}`, support size, lexicographic rank and inverse rank have a polynomial positive-integer dynamic-programming construction. A conservative **O(n^20)** arithmetic-operation bound follows from at most eighteen bounded directed-edge counters (nine for P and nine for Q), one bounded K counter, a position counter and constantly many ternary boundary labels. Positive-integer masses have O(n) bits because total raw history population is at most `3^(m+n-2)`.

Construct the joint hidden-prefix BRC table through t, storing the current letters, P/Q edge counts, match count, newly isolated boundary tags that have appeared, and positive raw path population. For `t<=m-2`, the observable suffix consists of labeled `(P_i,Q_i)` positions `t<i<=m` followed by visible `Q_i` positions above m. For `t>=m-1`, the visible suffix consists of Q letters after t; `P_m` is forced by its adjacency, and at `t=m-1` its still-unread K comparison with `Q_m` is deferred. In either case, each emitted visible letter deterministically updates the suffix counters. At terminal, the residual required hidden-prefix edge counts and K count (with at most three choices for a hidden P boundary letter) select entries of the positive prefix table. Their sum is the exact `M(k)`.

Memoize deterministic suffix states returning a pair `(Boolean support, positive raw mass)`. Different labeled suffix words contribute separately to support; hidden realizations of one word are summed only in its mass. Rank subtracts the Boolean support of lexicographically earlier child labels and unrank descends to the uniquely selected child. Each additional repair coordinate is either already visible in the suffix or one of only three finite ternary tags, multiplying the predecessor BRC state space by at most `3^3` and preserving polynomial arithmetic complexity. Sparse terminal lookup over `(edge-count vector,K)` avoids a hidden-profile-by-suffix Cartesian product.

**Executed implementation scope:** `STAGE473B.py` implements the `t>=m-1` positive BRC prefix/deterministic suffix program, with class populations, support and rank/unrank. The `t<=m-2` case is covered by the mathematical construction above and the Stage471-B prefix/visible-pair continuation; it was not independently reimplemented in this stage's code. Future-equivalence Theorem 473.1 is proved directly above, independent of that implementation choice.

## Three strict witnesses against the smaller R469 repair

All use `t=n` (Q POP budget zero), have identical full initial signed-X6 observers and identical `R469`, but have different `R473`.

1. **New Q_(m+2) probe.** `m=6,n=14`, `P1=P2=AAAAAA`, `Q1=AAAAAAABAACAAA`, `Q2=AAAAAAACAABAAA`. Execute `APPEND_P(A),APPEND_P(B)`. Initial K=6. Final K is **8 versus 7**. Original directed Q edges and all R469 labels coincide.
2. **New P_(m-2) boundary.** `m=11,n=13`, `P1=AAACAAAABAA`, `P2=AAABAAAACAA`, `Q1=Q2=A^13`. Execute `POP_P,POP_P`. The original P adjacency is the same; after two POPs, the remaining P final direction is **B versus C**, distinguishing its six-dimensional endpoint/adjacency even though final K is 7 in both histories.
3. **New Q_(m-1) probe.** `m=6,n=13`, `P1=P2=AAAAAA`, `Q1=AAAABAAACAAAA`, `Q2=AAAACAAABAAAA`. Execute `POP_P,POP_P,APPEND_P(B)`. Initial K=5; final K is **5 versus 4**.

These witnesses establish distinct necessity phenomena for each new tag in some full-observer fibers. They do not assert the tags are mutually independent for every fiber.

## Executed exact evidence (Python 3 standard library)

`STAGE473B.py` / `STAGE473B_EXECUTED.json`, executed on 2026-11-06:

* Exhaustive original-history grouping on **490 selected complete observer fibers**, from **14** short configurations, checked **2,955** exact class populations, rank/unrank inverses and equality of both repairs' induced partitions. All assertions passed.
* Full labeled future comparison across **all twelve signed APPEND directions** on **19** sampled same/different-repair history pairs in **6** configurations (1 same-repair pair, 18 different-repair pairs), visiting **6,287** synchronized future states; all assertions passed. The program explicitly permits popping steps previously appended.
* Large complete observer fiber `P=A^35`, `n=56`, `Q` having `AA=3`, `AB=BA=14`, `AC=CA=12`, `K=18`: exact total mass `11,154,643,500` at every t. Supported keys for `t=34,35,36,37,56` are respectively **281,600; 281,600; 281,600; 281,600; 16**. No full raw-history or supported-key enumeration was used for these large counts. Largest listed suffix-cache count is **8,544**; representative rank/unrank probes passed.
* The three explicit witnesses were independently checked against actual complete initial observer arrays and R469 equality; each stated operation path distinguishes the resulting observers.

BRC method resolution: **EXTEND_EXISTING_TOOL / REUSE_EXECUTED**. Preserve separate Boolean support and positive integer raw branch populations in the deterministic suffix transfer. The exact future equivalence theorem and the DP algorithm are author-side research results awaiting independent Driver mathematical review; neither alters P000 or the frozen scientific pins.

## Next smallest unit

Stage474-B: increase P's POP and APPEND budgets to three while keeping Q's arbitrary POP and one APPEND. Determine whether the exact repair adds only `P_(m-3),Q_(m-2),Q_(m+3)` and prove or falsify that hypothesis with exact future words. Implement the growing-window BRC transfer for the `t<=m-2` branch and compare rank/mass against complete original-history enumeration at small sizes. Audit Stage469's semantic proof independently before any formal admission.
