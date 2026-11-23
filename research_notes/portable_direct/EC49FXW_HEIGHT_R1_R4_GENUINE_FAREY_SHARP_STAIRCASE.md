# EC49FXW — Sharp height staircase for genuine Farey fixed sites at Hamming distances 1–4

Date: 2026-11-23 (Asia/Shanghai). Scientific input remains **BRC16943**. Continuation of EC49FXV at `d1bf9b7b827b919d4c14da968e5a9f792c550ef8`; parent EC49FXU at `5e33d4576bb0c1ef09e9169f8e17df469b8b7692`. Status: **AUTHOR_PROVED / EXACT_FINITE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED**.

## Precise observation model

Retain the frozen Boolean predicate
[
C_{11}(h,n)=P_{10}(hmod10,nmod10),1_{9h+10n
otequiv0pmod{11}}.
]
For every reduced positive Farey anchor `a/b` with `0<a<b`, `b<=H`, use the original determinant-one left-branch rephasing to generate its normalized ten-by-eleven product trace `W=U ⊗ V`. Distinct normalized traces form `W_H`. The observer is given the **full indexed reflection-defect spectrum** of the hidden trace and the external denominator bound `H`, but not its anchor or affine origin. It chooses a single fixed set `S⊆(Z/10)×(Z/11)` of **physical Boolean sites before seeing the spectrum**. For `1<=r<=4`, define `N_H(r)` to be the minimum `|S|` such that all distinct equal-spectrum traces in `W_H` have Hamming distance at least `r` on `S`.

## Theorem: four universal height plateaus

For every integer `H>=22` and every integer `1<=r<=4`,
[
oxed{N_H(r)=3r+mathbf1_{Hge52}+mathbf1_{Hge58}+mathbf1_{Hge64}.}
]

| Denominator height | r=1 | r=2 | r=3 | r=4 |
|---|---:|---:|---:|---:|
| 22–51 | 3 | 6 | 9 | 12 |
| 52–57 | 4 | 7 | 10 | 13 |
| 58–63 | 5 | 8 | 11 | 14 |
| 64 and higher | 6 | 9 | 12 | 15 |

The `r=1` column agrees with EC49FXV; **the new sharp classification is for r=2,3,4 below height 64**. For `r=3`, one arbitrary unknown corrupted bit is correctable by the conventional Hamming criterion. For `r=2`, one **known-location erasure** is correctable.

## Proof: analytic lower bound plus explicit upper witnesses

1. The exact genuine-anchor census reconstructs the 600 normalized product traces, 478 indexed spectra and 122 equal-spectrum doubletons (see reproducible companion program). Every doubleton shares the same 11-factor `V`, either full or with one excluded column `z`. Its difference support has the form `G×(Z/11\{z})`; take `z=null` for full `V`.

2. Among the genuine doubleton row supports are three *pairwise disjoint* sets
[
A={1,4,6,9},quad B_*={2,7},quad C={3,8}.
]
All three appear by denominator height 22. Consequently any admissible layout needs at least `r` sites in each of `A,B_*,C`, hence `|S|>=3r`. Each minimal group has genuine doubletons whose deleted columns together cover all eleven possibilities, first by heights `52,58,64`, respectively. For any such full-hole group, exactly `r` selected sites cannot work: choose the hole equal to the column of one of those sites, which decreases the pairwise distance to at most `r-1`. Thus each full-hole group requires `r+1` sites. The three groups are disjoint, giving the stated lower bound at every height `H>=22`.

3. For the four plateau right endpoints `H=51,57,63,64`, the companion certificate gives explicit site sets for each `r=1,2,3,4` of exactly the lower-bound cardinality. The verifier recomputes the first actual anchor witnessing every trace, every indexed spectrum and every equal-spectrum doubleton, then checks every selected site against *all* doubletons present by its endpoint: 78, 94, 108, 111 constraints respectively, or 1,564 exact layout/distance tests across the 16 layouts. All pass. Monotonicity of `W_H` proves every intervening height by retaining the later-height upper layout and the lower bounds. At `H>=64`, a simpler uniform upper layout is `S={(j,v):j∈{1,2,3},0<=v<=r}`. Every one of the seven possible genuine difference supports contains at least one entire minimal group `A,B_*,C`, and hence at least one of rows `1,2,3`. The `r+1` different columns survive any one deletion with at least `r` observations. This covers all 600 ambient traces, which are exhausted by height 139, and all larger heights.

This proves equality without integer-programming optimality claims. The finite census is a justified exhaustive sublemma: for `b=2..139`, enumerate every `1<=a<b` with `gcd(a,b)=1`, compute its unique frozen lexicographic determinant-one normalization, and obtain all 50×12 products. Their spectrum is computed exactly as `D(s,t)=2(|U||V|-|U∩(s-U)| |V∩(t-V)|)`. The emitted witness layout and all constraints are directly checked against those bytes/integers. Additionally, the program evaluates the original `C11` predicate at all 110 trace indices for the 600 first-occurrence anchors, i.e. 66,000 exact direct equalities.

For quick inspection, an optimum `r=2` layout at height 57 is `(2,6),(3,0),(7,6),(8,0),(9,8),(9,9),(9,10)`; at height 63 it is `(3,0),(6,7),(7,4),(7,5),(7,6),(8,0),(9,1),(9,2)`. The full 16 concrete site sets and the machine-checkable direct constraints are in the companion code and JSON.

## Scope and next research

The bound `H` is supplied exogenously; its acquisition cost remains an independent observer problem. These are exact **genuine Farey scalar auxiliary** results under the existing normalized-observer model, not a proof about native six-dimensional X6 evolution or full three-dimensional slices. The parent `C11` model/predicate is reused at its frozen pin without altering P000, ACTIVE worldview, BRC inputs or formal task/Review states.

The `r<=4` restriction on the low-height classification is substantive: preliminary exact optimization at `H=52,r=5` gives 17 sites, whereas naive continuation of this formula would give 16. An independent lower-bound proof and higher-distance height staircase remain open; treat that diagnostic as **EXPLORATION / NOT_PROVED**, not as this theorem's result.

Reproduction: run `node research_notes/portable_direct/EC49FXW_HEIGHT_ERROR_DISTANCE_STAIRCASE_VERIFY.js`, compare its full JSON to the accompanying output, then inspect `endpoint_certificate`, `thresholds`, `original_C11_checks` and `all support contain a minimal group` assertions. No floating-point computation, MIP solver, remote API, Lean or CI required. Independent mathematical Review remains open.
