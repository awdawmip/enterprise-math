# EC49FAK — exact 94-edge optimum for four rooted H9 key-reuse families

Date: 2026-11-04. Classification: AUTHOR_ANALYTIC_FINITE_THEOREM / EXACT_BIGINT_Q_RANK_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Source and precise local problem

Continue EC49FAJ at immutable Git commit `ab1ff23273f70b6c6fb83d7ae74b112705458f1d` (original verifier blob `b47310070d1815fafe59b3d3aff477f7dd30ee7b`), preserving frozen scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The native signed X6 seven-letter operations are `a=(-1,-1), b=(-2,-2), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2)`. The nine-history T4/T2 observation and complete positive BRC key use the EC49FAJ program exactly.

Fix **all** word families of horizons 2 through 7 to one of the four EC49FAB selections with source ranks 1512, 1513, 2200 or 2203. Each H7 family has exactly two ordered operation words `p,q`. In the **rooted suffix-only subproblem**, every selected H8 word must append one operation to `p` or `q`; every H9 word must append two operations to `p` or `q`. Each word has net signed X6 displacement `(2,0,0,0,0,0)`. Each horizon has one complete positive BRC key; H8 and H9 share the **same fifth key**, so the total global key count remains five. All observation signatures belong to the six signatures already used at H2..H7; each horizon has rational observation rank nine. Minimize the union of **nonempty ordered signed native primitive-step prefixes** over H2..H9.

## Theorem (exact local optimum)

For each of the four source ranks, the rooted suffix-only subproblem has optimal total prefix cost

```
E_rooted(H9; source_rank) = 94.
```

**Exhaustive reduction.** At H7 the target net displacement already holds. An appended zero-net single operation must be one of `c,d,f,g`. A zero-net two-operation suffix must consist of any ordered pair in `{c,d,f,g}²` or `ae,ea`. This lists **4** possible one-operation suffixes and **18** possible two-operation suffixes per root. Direct counting of the complete positive six-coordinate key shows that H8 and H9 can share their new fifth key only when the H8 suffix is `c` or `d` and the H9 suffix is `fg` or `gf`; it is `(5,5,1,0,0,0)` for ranks 1512/2200 and `(7,3,1,0,0,0)` for ranks 1513/2203. Therefore the **entire** feasible candidate pools are the four H8 words `pc,pd,qc,qd` and the four H9 words `pfg,pgf,qfg,qgf`.

Using the exact nine-history transfer readouts and Gaussian elimination over rational integers (BigInt fraction-free, no floating point), every subset of k H8 words has rank **2k+1** for k=1,2,3,4, respectively **3,5,7,9**. Therefore rank nine forces **all four** H8 candidates. Among the 15 nonempty H9 subsets, exactly **nine** have rank nine (four cross-root pairs, four triples, the four-word set), so at least one H9 word must descend from each H7 root.

The H2..H7 rooted prefix union has exactly **72** edges. The four forced H8 suffixes have disjoint four-step new tails, contributing **16** edges. Each chosen H9 suffix has four signed steps and, after its corresponding H7 root, shares at most the first step with H8 c/d; its remaining three are new. Distinct H7 roots do not share new tails. Since H9 rank nine requires one word from each root, H9 needs **at least six** additional edges. Thus `E >= 72+16+6 = 94`. The EC49FAJ constructions `pfg,qfg` attain equality.

The exhaustive verifier checks all `2^4-1=15` nonempty H8 subsets and all 15 H9 subsets using exact rational rank; the nine rank-nine joint selections per case are individually costed with their complete native signed prefix unions. All four cases have nine feasible joint selections, minimum 94, exactly four minimum-attaining selections. One existing witness for each source rank is included in `EXACT_REPORT_EC49FAK.json`.

## Significance and next question

This certifies a concrete **local obstruction**: changing only H8/H9 by suffix extension of the two unchanged H7 paths cannot produce `E<=93` for any of these four fixed early schedules. The larger H9 optimization problem remains under the previously reported **80 <= E9* <= 94** author-side bounds. The next useful discriminating search (EC49FAL) allows new H8 or H9 legal words **not descended from the fixed H7 pair** (or changes H6/H7), while preserving full positive cache keys, signed primitive path provenance, observation signature budget and exact rank. Prioritize words with significant existing-prefix overlap and test whether a 93-edge complete construction exists.

## Reproduction and trust scope

Run `node VERIFY_EC49FAK.js > EXACT_REPORT_EC49FAK.json` using Node v22 or another JavaScript engine supporting BigInt. All native signed primitive steps are expanded before prefix counting; arithmetic ranks are exact over Q by integer row operations. The C++ OR-mask global optimizer and original Source-native state machine are not invoked. The result is author-side analytical + independently cross-checked finite mathematics, not a Source-native CLAIM/Result or independent Driver acceptance. P000, ACTIVE worldview and original frozen scientific input are unchanged.
