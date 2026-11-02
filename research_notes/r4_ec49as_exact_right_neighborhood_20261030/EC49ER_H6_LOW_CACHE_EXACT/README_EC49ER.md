# EC49ER — Exact H=6 low-cache native-X6/BRC resource classification

Date: 2026-11-02. Parent: EC49EQ, commit `fb82b62af022829b0a52b729af1c7461407a0665`, Draft PR #1730. Next: EC49ES. **Status: `AUTHOR_FINITE_EXHAUSTIVE_PROOF / EXACT_INTEGER_DP_PASS / INDEPENDENT_MILP_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`.**

**Frozen scientific pins, inherited from EC49EQ's successor entry:** `GLOBAL_KNOWLEDGE_V1@773d538180bfb49e24cffeb35c3ee75eb0628e2e`, `enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Current *behavioral* rules were separately read at global canonical main `37fc58c1e0eee8d1211f034946bff2d3cae2458c` and Enterprise Math main `e6f675caf4a340766d117d16c859c1f9c06b2512`. They do not replace scientific pins.

## Model and research target

Work in the existing signed native six-axis X6 coordinate torsor, with separate time/ordered path and nine historical first-A/B-event observer states. **No dimensional collapse:** axes 4–6 are explicitly zero for the *restricted input family*, not absent in the ambient P000 six-dimensional native space. Native ordered signed step encodings:

```
a=(-E1,-E1), b=(-E2,-E2),
c=(+E1,+E2,-E1,-E2), d=(+E2,+E1,-E2,-E1),
e=(+E3,+E1,+E1,-E3), f=(+E1,-E1), g=(+E2,-E2).
```

A future word of horizon h is legal iff its signed displacement is `(2,0,0,0,0,0)`. On each h=2,...,6, choose any set of legal words with one common complete *positive-step vector* p, whose collective nine-row, five-terminal-bucket A/B-first-event observation matrix has rational rank 9. Different horizons may have different vectors. Every original native path identity, signed order and observer signature remains separately retained; the BRC cache uses the two-channel *symbolic positive-weight* monomial indexed by p, and asserts neither phase nor signed cancellation.

Count `(E,M,S)` where E is the number of distinct nonempty signed native prefixes of every chosen word, M is the number of different full six-component p keys over all horizons, and S is the number of different nine-state exact terminal transfer signatures. Essential h=2 words `ce,de,ec,ed` require 28 edges, the unique p0=(3,1,1,0,0,0), and four signatures T4. A q=0 full-rank fiber uses two distinct additional T2 signatures. For all full-rank fibers through h=6, the program *exhaustively* establishes that their unique inclusion-minimal rank-nine signature set is T4 (q>0) or T2 (q=0). This follows the prior EC49EL/EC49EQ transfer classification, and is explicitly rechecked by the new source.

## New Theorem 1 — two BRC cache keys at H=6

There are **exactly three** complete p-fiber assignments possible when M=2. Their second vector, with final three coordinates zero, is respectively `(4,3,1)`, `(5,2,1)` or `(5,3,1)`; the exact minimum prefix-edge counts are **90, 90, 110**. All such solutions have S=6. Hence

\[
 \boxed{\min\{E\mid H=6,M=2\}=90,\qquad S=6\text{ necessarily}.}
\]

In particular, 90 is attained by the h=2 baseline and:

| h | words |
|---|---|
| 3 | `feg`, `gef` |
| 4 | `cegc`, `degd`, `ecgc`, `edgd` |
| 5 | `cegfg`, `deggf`, `ecgfg`, `edggf` |
| 6 | `fegggf`, `gefggf` |

Each of these four horizon groups has common p and rank 9. The prefix union has exactly 90 signed native edges and only two complete p keys. An equally optimal p=(5,2,1) witness is included in the executed JSON.

**Analytic reduction of the candidate p population.** Write a,b,c,d,e,f,g for the operation counts, `q=c+d`, `u=f`, `v=g`. Native return implies b=0, e=a+1, and therefore

\[
p=(q+2e+u,\ q+v,\ e,\ 0,0,0),\quad
 h=p_1+p_2-1-q,
 \quad 0\le q\le\min(p_1-2e,p_2),\ e\ge1.
\]

The h2 key p0 appears at h3 but not at any h≥4. Thus M=2 forces p3=p0 and one identical second p for h4,h5,h6. At h4, `q4=p1+p2-5≤min(p1-2e,p2)` implies p1≤5, p2≤5−2e; at h6, `q6=p1+p2−7≥0` implies p1+p2≥7. The latter bounds force e=1, p1≤5, p2≤3 and p1+p2≥7; consequently the three vectors listed above are **the only possibilities**, all realized by rank-nine fibers. h3 at p0 has the two T2 observer signatures disjoint from T4, forcing S=6.

For each of the **three** remaining finite assignments, enumerate *all* legal words in its fibers, retain all words with its necessary transfer signatures, and compute the exact rooted native-prefix-tree integer OR-mask DP (explained below). It returns E=90,90,110. The displayed native words attain E=90. This is an exact finite proof, not an inference from a numerical trend or solver tolerance.

## New Theorem 2 — all three-key H=6 cases

Complete exact integer-DP enumeration of **all 434 distinct complete p assignments with M=3** gives:

\[
\boxed{\min\{E\mid H=6,M=3,S=4\}=84}\quad(10\text{ assignments}),
\]

\[
\boxed{\min\{E\mid H=6,M=3,S=6\}=68}\quad(424\text{ assignments}).
\]

The S=4 minimum has p selections `(4,2,1)` at h3,h4 and `(5,3,1)` at h5,h6; an exact E=84 witness (plus h2 baseline) is:

| h | words (S=4, E=84, M=3) |
|---|---|
| 3 | `cec`, `ded`, `ecc`, `edd` |
| 4 | `cefg`, `degf`, `ecfg`, `edgf` |
| 5 | `cefgc`, `degfd`, `ecfgc`, `edgfd` |
| 6 | `cefgfg`, `degfgf`, `ecfgfg`, `edgfgf` |

The S=6 minimum has p h3=(3,1,1), h4=h5=(4,2,1), h6=(5,2,1), with E=68, M=3 and S=6:

| h | words (S=6, E=68, M=3) |
|---|---|
| 3 | `feg`, `gef` |
| 4 | `ecgf`, `edgf`, `fegc`, `gefd` |
| 5 | `fegfg`, `gefgf` |
| 6 | `fegfgf`, `gefgff` |

All 434 exact per-case minima and DP-state counts are saved in `EC49ER_ALL_M3_EXECUTED.json`, and the winning configurations are separately independently checked by SciPy/HiGHS with reported gap=0, dual objective equal to E (84 or 68). Integer DP, not floating-point MIP, supports finite optimality.

**Comparison:** The previously proved unconstrained edge-only minimum `E=4H+30` at H=6 is 54, attainable with `(54,4,6)` through the nested `feg f^(h-3)` / `gef f^(h-3)` word families. The two-key requirement costs an extra 36 native prefixes (90−54), while allowing three keys and six signatures reduces that premium to 14 (68−54). These are exact resource tradeoffs **within the declared model**, not a full H=6 Pareto frontier and not an implementation-runtime speedup claim.

## A proven feasible four-key/four-signature upper bound, not optimum

An additional actual word construction yields `(E,M,S)=(80,4,4)`. At h3/h4/h5/h6 use respectively:

```
cec ded ecc edd
cecc dedd eccc eddd
cecfg dedgf eccfg eddgf
cecfgf dedgff eccfgf eddgff
```

See `EC49ER_M4_S4_UPPER.json`; the exact native trie witness has 80 prefixes and rational rank 9 per horizon. **The H=6 M≥4/S=4 case search was not completed; 80 is only a feasible upper bound and must not be presented as a minimum.** In particular this work does not claim the complete H=6 three-resource Pareto set.

## Finite proof kernel and validation scope

Complete word enumeration gives the following exact counts:

| horizon h | all legal native-return words | rank-nine p fibers |
|---|---:|---:|
| 2 | 8 | 1 |
| 3 | 51 | 4 |
| 4 | 304 | 9 |
| 5 | 1,770 | 17 |
| 6 | 10,224 | 28 |

Every 9×9 integer minor of an observation matrix has `|det|≤3^9=19683<1000003`, because each 0/1 terminal observation column has norm ≤3. Thus rank 9 modulo prime `1000003` is equivalent to rank 9 over Q. Witness ranks are also checked directly using `fractions.Fraction` elimination; all selected words are checked for signed six-axis return, identical p within each horizon, exact terminal signature coverage, distinct global p and transfer-signature counts.

**Exact OR-mask trie DP:** Each native-operation code is a prefix-free sequence of two or four signed native axis steps. Construct a trie containing the full signed primitive paths of *all* qualifying words from each selected h/p fiber that have a necessary signature. Tag each terminal with bit `(h,signature)`. Bottom-up states map an OR-mask to the minimum integer additional prefix-edge cost in that subtree; merge child states via min-plus convolution and OR masks. A native edge already covered by the 28-edge h2 base trie costs zero extra; all other used edges cost one. At the root, the full required mask gives the exact global minimum for the fixed fiber assignment. Enumeration over all possible M=2 and M=3 fiber assignments gives the theorems. Word terminal identity and ordered native intermediate steps are retained throughout the proof.

Executed actual certificates: `VERIFY_EC49ER.py` + `EC49ER_EXECUTED.json` (three M2 cases), `VERIFY_EC49ER_ALL_M3.py` + `EC49ER_ALL_M3_EXECUTED.json` (434 M3 cases), separate `VERIFY_EC49ER_MILP.py` / `EC49ER_MILP_EXECUTED.json` (three M2 crosschecks), separate `VERIFY_EC49ER_M3_MILP.py` / `EC49ER_M3_MILP_EXECUTED.json` (two winning M3 crosschecks). An additional witness record `EC49ER_M4_S4_UPPER.json` records the nonoptimal upper bound. All scripts and source JSON are included in the companion lossless evidence archive; do not interpret BRC symbol counts as signed phase-cancellation verification. No physical-time evolution, generic off-family X6 dynamics or speedup benchmark was established.

## Real role/owner status and next question

Authenticated GitHub user `awdawmip`, repository admin/push permitted. Native research-session request denied with `STATIC_READONLY_SCOPE_DENIED` (`operation_sent=false`); control owner query returned `CONTROL_QUOTA`, thus **no current active owner could be confirmed**. These author-side mathematical results are saved as a portable draft, not as a formal Research Activity, CLAIM, Result, Driver review or admitted theorem. No P000, protected ACTIVE worldview or frozen scientific pins changed. Keep separate the GitHub author-side publication from native state machine authority.

**Next EC49ES:** Finish H=6 `(M,S)` high-cache cases. Specifically compute exact `min E` for `(M=4,S=4)` and `(M=5,S=4)`, then full Pareto dominance including existing `(90,2,6)`, `(68,3,6)`, `(84,3,4)`, `(54,4,6)` and feasible `(80,4,4)`. Use exact quotient/trie compression, analytic bounds or signed-native dominance certificates to avoid unbounded case-by-case explosion. Distinguish all cost sources: constructing input paths, sign-sensitive X6 expansion, source/preprocessing, trie size, exact BRC multiplications/cache, matrix storage, rank recovery and verification.