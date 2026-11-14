# EC49EH — Equal-positive-count BRC fibers and shared X6 primitive tries

**Date:** 2026-11-02. **Parent:** EC49EG, immutable author frontier `3d66861f3329909c821cf60da8c51dd2f7014551` (Draft PR #1730). **Deliverable:** finite exact h=2,3 proof, optimization evidence H=4,5,6, an analytic all-H constructive bound and a conditional all-H optimum. **Status:** `AUTHOR_EXACT_FINITE_PROOF / MIXED_INTEGER_OPTIMALITY_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`.

**Frozen scientific pins (inherited unchanged from EC49EG):** GLOBAL_KNOWLEDGE_V1 `773d538180bfb49e24cffeb35c3ee75eb0628e2e`; Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Separately read current behavioral source:** global canonical main `759baa011d112b77c75eaa2f2c6ae4288b3d2b5b`; EM canonical main `01686797499ab8cbd9e3d9416990958987f8a9d7`. P000 and ACTIVE Heartbeat World remain unchanged.

## Exact scope, carrier, observer and cost

Native full signed-six-axis ordered primitive operations:

```
a = (-E1,-E1),        b = (-E2,-E2),
c = (+E1,+E2,-E1,-E2),  d = (+E2,+E1,-E2,-E1),
e = (+E3,+E1,+E1,-E3),  f = (+E1,-E1),  g = (+E2,-E2).
```

A historical path ends at chart-relative six-axis displacement `(-2,0,0,0,0,0)`. Each selected future operation word has exactly `h` letters and full native displacement `(2,0,0,0,0,0)`. The two positive-pair events are `A=(+E1,+E2)` and `B=(+E2,+E1)`; the terminal observation has buckets `N,A,B,AB,BA`, with `AB`/`BA` denoting first-seen order. The nine seam-sensitive history atoms are `N0,N1,N2,A0,A2,B0,B1,AB,BA`; all are realized by actual ten-primitive-step histories with equal positive counts `(2,2,0,0,0,0)`.

For a true future primitive path `w`, let `p_i(w)` count positive `+Ei` primitives. Each positive BRC instrument has an exactly multiplicative factor `X(w)=∏x_i^{p_i(w)}` and `Y(w)=∏y_i^{p_i(w)}`, `x_i,y_i>0`, plus unweighted path count. Word/horizon labels remain separate; positive factors are never averaged before terminal observation.

**New constraint:** within each *fixed* horizon `h`, all *selected* returning future words must have identical complete six-axis `p(w)` (horizons may have distinct fibers). Their nine-row Boolean word:bucket transfer columns must span rank 9. Define `U_eq(H)` to be the minimum size of the union of nonempty **genuine signed primitive-step prefixes** of all selected words, across **all** horizons `h=2,...,H`; shared intermediate prefixes are billed once. Extra words are permitted but never obligatory, and per-horizon families need not individually minimize their costs.

## Result 1 — Complete finite exact enumeration at H=2 and H=3

```
U_eq(2) = 28;       U_eq(3) = 36.
```

There are exactly eight returning operation words at h=2; the sole equal-count rank-nine fiber is `p=(3,1,1,0,0,0)` with the **four** words `ce,de,ec,ed`. The 9x9 transfer minor has determinant `-1`. All four are necessary, and their signed primitive prefix trie has exactly 28 edges (the two `e`-first paths share a four-step primitive prefix).

At h=3 the complete alphabet has **51** returning words across **7** positive-count fibers. An exhaustive standard-library checker enumerated **12,369 nonempty candidate subsets** inside those fibers. For every subset it computed the exact prefix union with the mandatory h=2 family and checked rank 9. Modulo `1000003` is *exact for the full-nine-rank decision*: every 9x9 subdeterminant of a nine-row 0/1 matrix has absolute value at most `3^9=19683 < 1000003` by Hadamard, so a rationally nonzero full-nine minor is nonzero mod that prime. (For near-full-rank classification, only the full-rank threshold is used.)

Exactly two subsets attain the minimum 36:

- `cef,def,ecf,edf`, with shared `p=(4,1,1,0,0,0)`;
- `ceg,deg,ecg,edg`, with shared `p=(3,2,1,0,0,0)`.

Each is obtained by extending the four mandatory h=2 terminal paths by one two-step native `f` or `g`, adding exactly eight new primitive trie edges. The checker exhausts every same-fiber subset, not only families of 2–4 words. An independent JavaScript implementation independently recovers the total, two minimizing subsets and exact fiber minima.

## Result 2 — Bounded finite integer optimization H=4,5,6

| H | Computed minimum `U_eq(H)` | Additional edges beyond mandatory h=2 | HiGHS MIP gap |
|---:|---:|---:|---:|
| 2 | 28 | 0 | exact enumeration |
| 3 | 36 | 8 | exact enumeration + 0 |
| 4 | **44** | **16** | **0** |
| 5 | **50** | **22** | **0** |
| 6 | **54** | **26** | **0** |

The submitted executable `SOLVE_EC49EH_MILP.py` generates every returning a–g word up to the requested H (8, 51, 304, 1770 and 10224 at h=2..6). For each exact positive-count fiber it groups words by their **full nine-atom transfer signature**, enumerates all inclusion-minimal signature subsets spanning rank 9, and builds a binary integer program. Each signed primitive trie edge has a 0/1 inclusion variable; child⇒parent edges enforce prefix closure; one selected full-rank fiber certificate is required at each horizon. The objective counts all new prefix edges beyond the mandatory 28-edge h=2 trie. Every feasible integer family yields a feasible integer program assignment, and every selected integer certificate yields an actual valid family: hence the combinatorial encoding is exact within the stated finite language.

SciPy `milp`/HiGHS reported successful **global mixed-integer optimality** with `mip_gap=0`, primal integer objectives 16/22/26 beyond 28, and matching MIP lower bounds. The program explicitly re-checks the chosen genuine paths, positive counts, rank and exact nonzero 9x9 integer determinant, and their primitive union cost. This is a reproducible *solver-supported finite optimum*, **not a formally verified integer-programming proof trace**. Independent pure-integer exhaustive coverage applies to H=2,3; the analytic constructions below are proved for all H. Full solver versions, constraint counts, selected words and reported bounds are in the JSON evidence.

An H=4 certificate is to continue all four mandatory paths with `f` twice (at h=3 and h=4), producing cost 44. At H=5 an optimal alternative uses the two **same-fiber** words `feg,gfe` at h=3, extends them to `fegf,gfef` at h=4, and to `fegfg,gfefg` at h=5. Their p-vectors are respectively `(3,1,1)`, `(4,1,1)` and `(4,2,1)` (three trailing zeros understood). Each pair provides rank 9, with a 9x9 integer determinant `-1`; the total signed primitive trie cost together with h=2 is exactly **50**. The computed H=6 certificate uses a similarly nested two-path family, cost 54.

## Result 3 — Two all-H constructive laws, and a conditional optimum

For every integer H≥2, the four equal-count words

```
ce f^(h−2), de f^(h−2), ec f^(h−2), ed f^(h−2)   (h=2,...,H)
```

retain the unimodular h=2 transfer: appending `f=(+E1,-E1)` creates no internal A/B event and does not change the terminal event-order state. Each horizon has identical `p=(h+1,1,1,0,0,0)`. The four nested genuine primitive paths have exactly `28+8(H−2)=8H+12` distinct prefix edges.

A second, lower-slope construction valid for H≥3 uses

```
F_h = f e g f^(h−3),     G_h = g e f f^(h−3).
```

These words have full return `+2E1`, each has exactly `2h+2` genuine primitives, and **both** have identical `p=(h,1,1,0,0,0)`. They create no internal A/B event; only the first primitive determines their seam response. The selected nine Boolean observation columns have integer determinant `−1` for every h≥3. `F_h` is a full native primitive prefix of `F_(h+1)`, likewise `G_h` of `G_(h+1)`. The h=2 mandatory trie shares **only the very first +E1/+E2 primitive** with these respective paths: its other second primitives are positive, whereas `f` and `g` immediately turn negative. Thus their joint cross-horizon primitive trie costs `28+2[(2H+2)−1]=4H+30`.

Consequently, analytically for **every H≥3**,

```
max(28,4H+4) ≤ U_eq(H) ≤ min(8H+12,4H+30).
```

The lower bound uses the proven EC49EG necessary pair of distinct +E1 and +E2 roots with each horizon-H native path length at least `2H+2`, plus the mandatory 28-edge h=2 fiber. It is not asserted sharp in general.

**Conditional all-H equality.** Restrict the chosen horizon-H fiber to words containing no `c` or `d` operations. Returning rank-nine families then require both an `f`-first and a `g`-first word (the historical A0/A2 and B0/B1 seam distinctions). Both have `2H+2` or more native primitive steps; each shares exactly one root primitive edge with the mandatory h=2 trie, hence any such family costs at least `4H+30`. The `F_h,G_h` construction reaches the lower bound while satisfying all intervening horizons. The **conditional** optimum is therefore exactly `4H+30` for all H≥3.

This conditional equality does not impose absence of `c,d` on candidate solutions of the unrestricted problem. The unrestricted all-H sharp formula remains a next question.

## Verification and scope of claims

`VERIFY_EC49EH.py` (Python standard library) reconstructs the nine real ten-step histories, native displacement, occurrence order, both strictly positive BRC multiplications, full h=2,3 returning-word universes, **all** within-fiber h=3 subsets, integer 9x9 Bareiss determinants and all-H certificate patterns through H=32. `VERIFY_EC49EH_INDEPENDENT.js` separately reimplements transfer, modular rank, exhaustive h=2,3 search and both trie formulae through H=32. Both returned `PASS`. `SOLVE_EC49EH_MILP.py` requires NumPy/SciPy; it returned `PASS` with zero HiGHS MIP gap at H=3,4,5,6 and rechecked exact integer candidate witnesses. Full nonempty outputs are stored in the adjacent JSON files.

This is a **model-internal native-X6 path/observer/positive-BRC theorem**, not a claim about observed physical dynamics, cancellation of signed amplitudes or runtime RAM cost. H=2,3 are completely enumerated under the exact grammar; H=4..6 are solver-supported integer optimization computations; the two all-H *upper bounds* and conditional equality follow from their explicit analytic constructions. Work retains original source restrictions and separate mathematical-admission roles.

**Actual author authority:** GitHub connector user `awdawmip` has repository write access. The native Enterprise Math MCP service returned `STATIC_READONLY_SCOPE_DENIED` (`operation_sent=false`) on researcher-session registration, and active-owner listing returned `CONTROL_QUOTA`; no current native owner was confirmed. This PR artifact is **author-side research storage only**, not a CLAIM, native Result, independent Driver review or Foundation promotion.

## Next testable question

**EC49EI:** derive a uniform lower bound for the **unrestricted** equal-positive-count `U_eq(H)` matching or improving the two current constructions for H≥7. Test whether all-H exact value is `min(8H+12,4H+30)`; seek a counterexample using many-word event-bearing fibers, or prove a type/trie lower bound. A second unit measures positive BRC factor and five-bucket readout overhead separately from primitive trie edges. Preserve source pins, nine seam atoms, word/horizon labels and full six-axis paths.
