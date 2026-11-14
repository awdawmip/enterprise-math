# EC49EO — Exact three-resource BRC/observer/prefix Pareto classification at H=3, and the H=4 two-key/four-block optimum

**Date:** 2026-11-02. **Status:** AUTHOR_FINITE_EXHAUSTIVE_PROOF / TWO_IMPLEMENTATIONS_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## 1. Source, native model and selected question

Continue [EC49EN](../EC49EN_LOG_BRC_CACHE_PARETO/README_EC49EN.md), specifically the three-resource objective it left open. Keep its frozen scientific inputs **GLOBAL_KNOWLEDGE_V1@773d538180bfb49e24cffeb35c3ee75eb0628e2e** and **Enterprise Math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab**. The updated normative rules are read separately; P000, the ACTIVE Heartbeat World, the typed positive-weight BRC substrate and native six-axis observer semantics remain in force. Source lineage also includes EC49EM's all-H optimum for prefix edges.

The seven available operations are ordered *signed-native-X6 primitive steps*:

```
a=(-E1,-E1), b=(-E2,-E2), c=(+E1,+E2,-E1,-E2),
d=(+E2,+E1,-E2,-E1), e=(+E3,+E1,+E1,-E3),
f=(+E1,-E1), g=(+E2,-E2).
```

A future word is an ordered sequence of operations with net displacement `+2E1`. Its length in **operations** is `h`. The nine seam-history atoms are `(N,0),(N,1),(N,2),(A,0),(A,2),(B,0),(B,1),(AB,0),(BA,0)`; final observer categories are `N,A,B,AB,BA`, where A and B record the first encountered adjacent `(+E1,+E2)` and `(+E2,+E1)` positive-step events, with the seam last-positive-step state retained. In each horizon h=2,...,H select a same-complete-positive-count `p=(p1,...,p6)` fiber with rational terminal observation rank nine.

For a selection of words across horizons, define the exact resource triple:

- `E`: number of **distinct nonempty ordered signed-native primitive-step prefixes** across all words (shared trie-edge cost).
- `M`: number of distinct complete positive-count exponent vectors `p`. In the two independent positive BRC channels these are the keys for the pair of formal monomials `X_p=∏x_i^{p_i}` and `Y_p=∏y_i^{p_i}`. Symbolic equality is by vector, not by accidental numerical equality.
- `S`: number of distinct 9-row × 5-bucket terminal observer-transfer matrices (one per signature). History, ordered-word identity and provenance remain represented separately.

A triple is Pareto dominated if another valid selection is no larger in all three coordinates and strictly smaller in at least one.

## 2. Main theorem: complete H=3 three-resource Pareto frontier

**Theorem 1.** Under the above native model, for the horizons `h=2,3` the exact nondominated triples `(E,M,S)` are **precisely**

```
(36,2,4) and (42,1,6).
```

The `M=2` optimal witness is:

```
h=2: ce, de, ec, ed         p2=(3,1,1,0,0,0)
h=3: cef, def, ecf, edf     p3=(4,1,1,0,0,0)
```

Every h=3 path extends a distinct h=2 leaf by the two native steps of `f`. The h=2 trie has 28 edges, the extensions add eight, and both horizons retain the same four transfer matrices: **(E,M,S)=(36,2,4)**. An equally optimal cost uses `ceg,deg,ecg,edg`, positive vector `(3,2,1,0,0,0)`.

The `M=1` witness is:

```
h=2: ce, de, ec, ed       p2=(3,1,1,0,0,0)
h=3: feg, gef             p3=(3,1,1,0,0,0)
```

Both added words have eight native steps and different first positive primitive directions. They overlap the h=2 tree on exactly one initial step each, giving **E=28+7+7=42**, M=1 and S=6.

**Complete finite proof.** The return equation forces `#b=0`, `#e=#a+1`. At h=2, all 49 operation words are tested; exactly eight return `+2E1`. Complete inspection of all `2^8−1=255` nonempty subsets with fixed positive count and rational rank nine yields exactly the four-word base `ce,de,ec,ed`. At h=3 exactly 51 of 343 operation words return. Their fixed-count fibers contain exactly **four** rank-nine-positive-count classes:

| Positive vector `(p1,p2,p3,0,0,0)` | Complete fixed-count fiber size | Minimum total E including forced h=2 tree |
|---|---:|---:|
| `(3,1,1)` | 6 | 42 |
| `(3,2,1)` | 12 | 36 |
| `(4,1,1)` | 12 | 36 |
| `(4,2,1)` | 12 | 44 |

For every such fiber, inspect all its nonempty subsets and retain exactly those with rank nine; count `E` by actual signed-primitive prefix sets and `M,S` by actual positive counts and transfer matrices. All nondominated triples are the two stated above. The scripts perform the complete search, preserving each word and matrix rather than inferring from operation counts alone.

All rank-nine decisions are made by Gaussian elimination modulo **1,000,003** on integer 0/1 observer columns. This test is *equivalent* to rational rank nine in the present 9-row setting: a rational rank-nine matrix has a nonzero integer 9×9 minor; each binary column has Euclidean norm ≤3, so Hadamard gives `|det|≤3^9=19683<1,000,003`. Thus a nonzero determinant cannot become zero modulo the chosen prime. Conversely, a nonzero modular determinant is a nonzero integer determinant. Rank-nine absence and presence are certified for this finite matrix universe.

## 3. Second theorem: H=4 with exactly two BRC keys and four observer matrices

**Theorem 2.** For horizons `h=2,3,4`, **conditioned on M=2 and S=4**, the exact minimum is

```
E_min(H=4 | M=2, S=4) = 56.
```

One attaining selection is:

```
h=2: ce, de, ec, ed               p=(3,1,1,0,0,0)
h=3: cec, ded, ecc, edd           p=(4,2,1,0,0,0)
h=4: cefg, degf, ecfg, edgf       p=(4,2,1,0,0,0)
```

The four h=2 signatures are mandatory and already exhaust the `S=4` cache. At h=3, selecting `p=(3,1,1)` would use `f`-first/`g`-first rank-nine transfers and increase S to six. The same p cannot supply h=4. Therefore M=2 and S=4 require h=3 and h=4 to share their *one other* positive-count fiber, and that fiber must produce all four existing signatures at both horizons. Complete return-word enumeration gives a **unique** such positive-count fiber: `p=(4,2,1,0,0,0)`. (At h=4, the other h=3 eligible fibers `(3,2,1)` and `(4,1,1)` become the `q=0` case and require two new transfer matrices.)

For this unique fiber, the cardinalities of available h=3 native words carrying each of the four required signatures are `(2,2,1,1)`; at h=4 they are `(12,12,12,12)`. Any full-rank solution using only these four matrices contains at least one representative of **each** signature at **each** horizon. Additional words with signatures already present only add prefix edges. Hence it suffices to enumerate

```
(2×2×1×1) × (12×12×12×12) = 82,944
```

possible representative choices. Actual signed-native-X6 prefix bitsets give the minimum **56** and the witness above. `verify_ec49eo_h4.py` and an independently implemented JavaScript/BigInt checker each complete all 82,944 cases and agree.

## 4. A simple all-H four-observer construction

**Proposition 3.** For every integer H≥2, the following selected words at each horizon `h=2,...,H` yield a valid same-positive-count rank-nine solution:

```
W_h = {ce f^(h-2), de f^(h-2), ec f^(h-2), ed f^(h-2)}.
```

They attain the explicit **three-resource upper-bound witness**

```
(E,M,S) = (8H+12, H−1, 4).
```

All four at horizon h have positive counts `(h+1,1,1,0,0,0)`, so their two positive-weight BRC multipliers agree. The added `f` operation is `(+E1,-E1)`: after the initial return word it does not introduce a new positive adjacent `(+E1,+E2)` or `(+E2,+E1)` event, hence the four h=2 transfer matrices remain exact in all horizons. Since each of the four original h=2 leaves adds two new native steps per additional h, the union increases by eight distinct prefix edges for each additional horizon, giving `28+8(H-2)=8H+12`. Different h have different positive-count vectors; `M=H-1`. The source code checks this construction for h=2..16; the structural argument is for all h.

**Resource interpretation.** At H=3 the construction **improves** EC49EN's displayed four-observer witness `(44,2,4)` to `(36,2,4)`; EC49EN's correct two-resource `(M,S)` Pareto statement remains intact. At H=4 it gives `(44,3,4)`, to be compared with the strict two-key/four-block optimum `(56,2,4)`. At H=5 it gives the feasible `(52,4,4)`, compared with the EC49EM global prefix lower bound `E≥50` and the EC49EN logarithmic key optimum. These are specific feasible triples, not a claim that every such H≥4 triple is nondominated.

## 5. Exact execution, reproducibility and evidentiary scope

- `verify_ec49eo.py` (Python standard library) exhaustively enumerates h=2,3 return words and all full-rank fixed-positive-count subsets; computes the exact H=3 triple Pareto set; verifies the two examples. Captured execution: `EC49EO_EXECUTED.json`.
- `verify_ec49eo_h4.py` (Python standard library) exhaustively enumerates the 82,944 necessary H=4 two-key/four-block representatives, using integer prefix-edge masks. Captured execution: `EC49EO_H4_EXECUTED.json`.
- `verify_ec49eo_independent.js` (Node.js / V8, standard language features only) independently reimplements native paths, observer evolution, modular Gaussian elimination, return-word generation, exact H=3 Pareto enumeration, H=4 prefix-bitset enumeration, and tests the all-H construction for H=2..16. Captured execution: `EC49EO_INDEPENDENT_EXECUTED.json`.

All three reported **PASS** when actually executed on 2026-11-02. The coverage/complete-search reductions above are the finite proof; the all-H proposition uses the explicit native-step construction. The BRC cost is a *symbolic positive-weight monomial cache* and does not substitute for phase/amplitude cancellation, machine runtime or storage of distinct word provenance. No physical-time or unverified native-to-physical bridge is asserted.

The task's native service identity attempt returned `STATIC_READONLY_SCOPE_DENIED` (`operation_sent=false`), while owner inventory returned `CONTROL_QUOTA`. Thus the research is preserved as a portable author-side draft; no authenticated native Research Activity, CLAIM, Result or independent Driver verdict is represented. This source proof keeps prior contributions and frozen pins.

## 6. Next exact question

**EC49EP:** Solve the H=4 and H=5 *complete* `(E,M,S)` Pareto frontiers, starting with `E_min(H=4 | M=2)` without fixing S, then full dominance pruning. Use exact native path/transfer signatures and complete-search certificates, retaining all positive-count and observer/provenance distinctions. Compare the new non-dominated points with `(8H+12,H−1,4)` and with EC49EM's unconstrained `E_min=4H+30` for H≥5. A constructive smaller frontier witness is as valuable as a proof that one candidate is optimal.
