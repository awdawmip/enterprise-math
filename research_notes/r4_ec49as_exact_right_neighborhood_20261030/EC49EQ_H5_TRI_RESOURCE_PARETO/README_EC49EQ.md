# EC49EQ — H=5 完整三资源 Pareto 精确分类

Status: `AUTHOR_FINITE_EXHAUSTIVE_PROOF / INTEGER_DP_PASS / MILP_CROSSCHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`  
Date: 2026-11-02 · Parent: EC49EP · Next: EC49ER  
Frozen scientific sources (as explicitly carried by EC49EP's `NEXT_EC49EQ.md`): `GLOBAL_KNOWLEDGE_V1@773d538180bfb49e24cffeb35c3ee75eb0628e2e`, `enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Current normative policies are separately read from canonical `main`; they are **not** scientific input substitutions. The prior author-side frontier is EC49EP at immutable commit `694c70f8136e0268e167dc1c7a5d702e98da3c3a` (Draft PR #1730).

## Theorem (complete H=5 Pareto frontier)

Let `a,b,c,d,e,f,g` denote the frozen EC49EP operations encoded as **ordered signed native X6 primitives**

```
a=(-E1,-E1)          b=(-E2,-E2)
c=(+E1,+E2,-E1,-E2) d=(+E2,+E1,-E2,-E1)
e=(+E3,+E1,+E1,-E3)
f=(+E1,-E1)          g=(+E2,-E2).
```

Each chosen future operation word must return signed displacement `(+2,0,0,0,0,0)`; the ambient native model has six axes, with axes 4–6 unchanged on this restricted input family. The nine historical states and A/B first-event observer are exactly those of EC49EP. On each future horizon `h=2,3,4,5`, a selected set of complete operation words must yield rank 9 in the 9-row terminal observer matrix, and every word within that horizon must have the **same complete six-axis positive-step vector** `p`. Distinct horizons may use distinct vectors. Define resource triple:

* `E`: number of distinct **nonempty ordered signed native prefixes** needed jointly for all selected words;
* `M`: number of distinct complete six-component vectors `p` (equivalently, two-channel symbolic positive-BRC multiplier cache keys);
* `S`: number of distinct exact nine-history terminal transfer signatures (each a nine-component map into `{N,A,B,AB,BA}`).

Compare feasible triples by coordinatewise dominance. Then the **complete** H=5 nondominated set is

\[
\boxed{\mathcal P_5=\{(50,3,6),(52,4,4),(64,2,6),(64,3,4)\}.}
\]

In particular,

\[
\boxed{\min(E\mid H=5,M=2)=64},\qquad
\boxed{\min(E\mid H=5,M=3,S=4)=64},\qquad
\boxed{\min(E\mid H=5,S=4)=52}.
\]

The first equality resolves EC49EQ's primary question. It quantifies a **14-native-prefix-edge premium** for the smallest achievable BRC cache (two complete positive-step keys), relative to the already-proved unconstrained minimum `E=50`. Relative to the `S=4` minimum, saving one cache key costs at least 12 more prefixes (52 to 64).

## Explicit native-word witnesses

All four use `h=2: ce, de, ec, ed` (28 paid prefixes, `p=(3,1,1,0,0,0)`). Additional words are:

| Triple `(E,M,S)` | `h=3` | `h=4` | `h=5` |
|---|---|---|---|
| `(50,3,6)` | `feg, gef` | `fegf, geff` | `fegff, gefff` |
| `(52,4,4)` | `cef, def, ecf, edf` | `ceff, deff, ecff, edff` | `cefff, defff, ecfff, edfff` |
| `(64,2,6)` | `fge, gfe` | `ecgf, fgec, fged, gfed` | `fgefg, gfegf` |
| `(64,3,4)` | `cec, ded, ecc, edd` | `cefg, degf, ecfg, edgf` | `cefgf, degff, ecfgf, edgff` |

For each row, **the executable certificate independently checks** every complete native path, its signed X6 return, within-horizon equal `p`, exact rational rank 9, the nonempty signed-native-prefix union, and the distinct `p` and transfer-signature counts. Positive-BRC multiplication uses `p` as a symbolic monomial exponent vector for both channels. Ordered path and observer signatures remain separately keyed; no signed or phase cancellation is assumed.

## Proof: finite completeness and integer dynamic programming

**1. Complete candidate universe.** Exhaust the 7-letter alphabet for `h=2..5` and retain only true signed-X6 returns. Counts are respectively `8, 51, 304, 1770`. Group by complete six-component `p`; the numbers of rank-9 groups are `1,4,9,17`. For each group, enumerate all subsets of its *distinct* observer transfer signatures, compute the terminal 9-row rank, and retain every inclusion-minimal rank-9 signature subset. All full-rank groups have a **unique** essential subset of exactly two or four signatures. The four-signature subset always equals the mandatory `h=2` set, denoted `T4`; the two-signature subset always equals one shared, disjoint `T2`. This is a complete finite computation, with an explicit checker and exhaustive group classification. As a consequence, a nondominated solution can retain only the essential representative signatures. Its `S` is exactly 4 when every selected horizon uses `T4`, and 6 when any horizon uses `T2`.

**2. Rank is exact.** The terminal matrix is made of the nine-row 0/1 indicator columns corresponding to each selected transfer signature and the five terminal buckets. For every 9×9 integer minor, the column Euclidean norms are ≤3, so the Hadamard determinant bound is `|det| ≤ 3^9 = 19683 < 1,000,003`. Rank 9 modulo `1,000,003` is therefore equivalent to rank 9 over `Q`. All four witnesses additionally pass an independent `fractions.Fraction` rational elimination test.

**3. Minimal cache `M=2`: exactly 8 scenarios.** The compulsory `h=2` vector is `p0=(3,1,1,0,0,0)`. This `p0` is available at `h=3` but not at `h=4` or `h=5`. Any two-key solution must therefore have `p4=p5=p`, where `p` is in the intersection of the complete rank-9 `h=4` and `h=5` fiber lists. That intersection has 7 elements. For `h=3` one must use `p0`; one additional scenario uses `p3=p` because that `p` also supports rank 9 at `h=3`. All eight scenarios necessarily contain `T2`, hence `S=6`. Exhaustive exact integer prefix-tree DP gives minimum `E=64`, attained by the explicit row above.

**4. Four-signature `S=4`: exactly 273 scenarios.** Restrict each future horizon to groups whose essential subset is `T4`: there are 3 at `h=3`, 7 at `h=4`, and 13 at `h=5`, giving `3×7×13=273` cases. Count distinct keys including `p0`. Exactly 22 cases have `M=3`, and 251 have `M=4`. Exact native-prefix-tree DP gives `min E=64` for the 22 three-key cases and `min E=52` for the 251 four-key cases, each attained above. No `M=2,S=4` case exists.

**5. Why the trie DP is exhaustive.** Each native letter is a signed primitive operation with a prefix-free two- or four-step encoding; therefore a word is represented by a unique terminal node of the rooted *signed native* prefix tree. Attach one required bit to each pair `(h, essential signature)`. On each node, the state `D_node[mask]` is the *minimum integer number of newly paid native edges* in its subtree whose selected terminals cover exactly `mask`. The empty choice has `(0,0)`; a used child contributes its exact DP cost; independent child masks combine by bitwise OR with integer min-plus convolution. A used node pays 1 iff its signed prefix is absent from the already-paid 28-edge `h=2` trie. When a node is both a terminal and a prefix for another word, its terminal signature is available at no extra edge cost. At the root, the all-required-bits mask gives the globally minimal additional cost. Enumerating all essential-signature words and their complete prefixes makes the DP a complete finite optimum, not a greedy sample. The program stores each scenario's native-prefix node and DP-state counts and cost.

**6. Pareto closure.** `M>=2` follows from `p0` being absent at `h=4,5`; `S>=4` from the mandatory `h=2` four signatures. The only S-values needed on a nondominated frontier are 4 and 6 (Step 1). For `S=4`, Step 4 supplies the best E at `M=3,4`, and `M=2` is absent. For `S=6`, Step 3 gives the two-key minimum `64`; the earlier EC49EM exact edge-only theorem gives `E>=50` for every H=5 solution, and the EC49EP nested family attains `(50,3,6)`. Every `M>=4,S=6` solution is dominated by that latter witness. These bounds and witnesses yield precisely the four displayed nondominated triples.

## Reproducible execution and evidence

Files in this directory:

* `VERIFY_EC49EQ.py` — **standalone Python standard-library**, completely enumerates eligible signed native words and all `281` critical scenarios, computes exact integer OR-mask trie minima, separately checks rational witness rank, and produces the full record `EC49EQ_EXECUTED.json`.
* `VERIFY_EC49EQ_MILP.py` — separately builds binary native-prefix variables and signature-cover constraints in SciPy/HiGHS and solves all 281 cases; all return solver status 0, reported gap 0 and integral primal/dual objective equality, matching the exact DP case by case.
* `EC49EQ_EXECUTED.json.gz.b64` — lossless gzip/base64 transport of the complete actual primary report, including the per-case 281 optimum and DP coverage statistics. Recover with `base64 -d ... | gzip -d > EC49EQ_EXECUTED.json` (or equivalent).
* `EC49EQ_SUMMARY.json` and `EC49EQ_MILP_EXECUTED.json` — small readable actual execution summaries, exact witness triples and independent optimizer scope.
* `NEXT_EC49ER.md` — next research question and reusable exact interfaces.

Executed on 2026-11-02 in Python 3 standard library, and separately in Python+SciPy/HiGHS (`mip_rel_gap=0`); both outputs `PASS`. **The main finite proof relies on integer exhaustive DP**; MILP is an independent optimization cross-check, not a replacement for enumeration.

## Authority, type and continuation

The present computation is an **author-side finite mathematical proof and implementation certificate** for the declared positive-BRC symbolic multiplication and native ordered X6 observer. It is not a native physics evolution, phase-cancellation certificate, or a new P000 premise. At the current run, authenticated GitHub identity is `awdawmip` with repository write access. The Enterprise Math native session attempt returned `STATIC_READONLY_SCOPE_DENIED` (`operation_sent=false`), and owner listing returned `CONTROL_QUOTA`. Thus native Research Activity, CLAIM, Result and independent Driver review/admission remain pending; GitHub branch preservation has its own separate status.

**Next EC49ER:** H=6 three-resource frontier. In particular, test whether a two-cache-key full-rank cover of `h=2..6` exists in the frozen full-six-axis-positive-count model, then derive the `S=4` optimal cache/edge exchange using the now reusable exact prefix trie DP. Compare the full cost of input expansion, trie storage, BRC factor caching, terminal observation reuse and output-recovery work before making implementation-speed claims.
