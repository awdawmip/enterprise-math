# R758P6 — Three eight-step flat loops generate the entire 2,520-state auxiliary A7 frame, with exact nine-block diameter

Date: 2026-11-13 (Asia/Shanghai). Status: exact theorem in the declared **candidate** six-axis signed-unit X6 / auxiliary S7 frame model, author-side; not a native P000 TRIADIC_CLOSURE_E acceptance.

## Inputs and correspondence

Frozen scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Direct predecessor R758P5B is Draft PR #2214, head `d4ab9bb9a8212d4220edbdfec70b16560e2ddb38`; its full auxiliary-frame construction and exact A7 theorem are retained. R758P3/P4 are PR #2204/#2208. P000 remains locked: six native spatial axes, a separate time axis, and a three-dimensional research slice; the seventh label `*` here is **only an internal frame label**, not a seventh native spatial axis or primitive force.

Let `F={*,1,2,3,4,5,6}`; for each of six native spatial axes `i`, let `T_i=(* i)\in S(F)`, an involution assigned to both signed directions of that axis. For a signed-unit Cell path `w=(\epsilon_1 i_1,...,\epsilon_n i_n)`, define `H(w)=T_{i_n}\cdots T_{i_1}`. A path is closed when each signed coordinate displacement totals zero. The signed projected-area vector `A(w)\in Z^15` has components `A_{ab}(w)=sum_{step along b} x_a(before step)*delta x_b` for `a<b`. On rooted closed paths `A(uv)=A(u)+A(v)` and `H(uv)=H(v)H(u)`.

For every `1<=i<j<=6`, use the *canonical* eight-step zero-area closed Cell loop from R758P5B:
```
W_ij=(+i,+j,-i,-j, +i,-j,-i,+j).
```
The first four steps have area +1 in the ij projection, the second -1. All 15 total areas are zero. Its frame is `g_ij=H(W_ij)=T_j T_i`, a 3-cycle on the frame labels `{*,i,j}`. Its reversed signed path is a zero-area eight-step inverse with frame `g_ij^{-1}`.

## Theorem A — the sharp sparse-generator number for this W_ij family

Choose only the following **three** canonical spatial loops:
`W_12`, `W_34`, and `W_56`.
Then
```
<g_12,g_34,g_56> = A(F) = A7, of order 7!/2 = 2520.
```
Moreover, no subset of the **15 canonical W_ij loops** of size one or two generates all A7. Therefore **three** is the minimum canonical-W-generator count, rather than all fifteen.

**Proof (elementary 3-cycle extension).**
For a finite label set `S` containing `s`, with `|S|>=3`, suppose a group already contains `A(S)` and additionally contains the 3-cycle `c=(s u v)` on two fresh labels `u,v`. Conjugating `c` by `A(S)` yields `(t u v)` for every `t\in S`, since `A(S)` is transitive on S. For distinct `t,t'\in S`, the product `(t u v)(t' u v)^{-1}` is a 3-cycle `(t u t')` (up to equivalent cyclic notation). Together with `A(S)`, these cycles generate `A(S\cup\{u\})`. Now `|S\cup\{u\}|>=4`; this alternating group is 2-transitive. Conjugating `c=(s u v)` by it yields all 3-cycles `(t t' v)` with two distinct old labels. They and `A(S\cup\{u\})` generate `A(S\cup\{u,v\})`. This proves the extension lemma.

Start with `<g_12>=A(\{*,1,2\})`. Apply the lemma to `g_34` to obtain `A(\{*,1,2,3,4\})=A5`, and then to `g_56` to obtain A7. All generators are even permutations, giving equality.

For minimality, each canonical `g_ij` fixes every label outside `{*,i,j}`. One or two generators together move at most 3 or 5 labels, respectively. Such a group fixes at least two labels when there are only two canonical generators; it cannot equal the transitive group A7. The three exhibited loops attain the lower bound. QED.

## Theorem B — exact symmetric block-word metric

Let `G=\{g_12^{\pm1},g_34^{\pm1},g_56^{\pm1}\}`. Every element of A7 is a product of **at most nine** elements of G. The bound nine is sharp for this precise six-element block alphabet: exactly six group elements have shortest word length nine.

By exhaustive BFS in the Cayley graph, using exact permutations and inverse generators, the distance distribution from the identity is:

| Minimum eight-step flat-loop blocks | Number of A7 frame states |
|---:|---:|
| 0 | 1 |
| 1 | 6 |
| 2 | 24 |
| 3 | 96 |
| 4 | 312 |
| 5 | 714 |
| 6 | 967 |
| 7 | 358 |
| 8 | 36 |
| 9 | 6 |
| **Total** | **2520** |

Each block can be realized by `W_ij` or its reversed signed path, each a rooted closed native spatial word of length 8 with `A=0`. Concatenation returns to the same Cell and has exactly zero 15-component area. Hence **every A7 final frame has a representative flat-area, Cell-returning candidate path of length at most 72 native unit steps**. This is a *constructive upper bound*, not a global shortest spatial path theorem. The nine-block lower bound refers only to the chosen three `W_ij^{\pm1}` blocks.

**Finite proof.** A breadth-first search starts with identity at distance zero and repeatedly appends all six generator/inverse permutations, inserting each new element once at its first (therefore shortest) depth. It produces the histogram above, exhausts all 2520 even permutations, and no new element arises thereafter. No floating-point computation is used. The companion program independently checks the 15 W_ij loops, their inverses, the generated subgroup sizes 3/60/2520 for the chosen prefixes, and all 2520 states.

## Theorem C — sparse bases are covariant as a family, not as one fixed subset

The permutation group S6 acts transitively on the 15 unordered axis pairs `{i,j}`. Therefore, the **only** nonempty collection of canonical `W_ij` blocks invariant as a set under every native axis relabeling is the complete fifteen-block family. The three-block matching `{W_12,W_34,W_56}` is a choice of basis (a coordinate gauge), not an S6-fixed subset. Every perfect matching of six native axes gives another three-generator A7 basis by conjugating the chosen matching. There are exactly `(6-1)!!=15` such matchings, all related by S6, and every one has the same symmetric generator word-metric diameter nine.

This is the precise cost distinction: **three blocks for any selected full-rank generating basis; fifteen canonical blocks if the fixed available-generator library must itself be invariant under all S6 relabelings**. All 15 matching bases were independently checked by exhaustive exact BFS (15 × 2520 reachable elements, each with the histogram in Theorem B).

## Scientific value and the remaining native obligation

R758P5B established that 15 canonical W_ij generators cover A7. This theorem compresses the generating library to **3 canonical flat-area blocks**, determines the exact maximum block depth (**9**), and gives a finite **72-step** uniform construction for the full auxiliary-frame observation fiber. It is a concrete branch/source-preserving BRC realization and compression result, not an identification of the frame with P000 force balance.

Next discriminating question: under a Source-admitted TRIADIC_CLOSURE_E Cell/Link/Port event and the actual V29/V39 native updates, can any of these three flat-loop blocks be represented or simulated as legal event composites, with source and order preserved? If yes, determine whether the native induced monoid has a smaller faithful generating set; if no, isolate the exact admission or transport obstruction. Native event legality, a canonical CLAIM, a formal Result, and independent Driver review remain separate open operations.

## Verification provenance

The included standalone Python verifier uses only the standard library and exact tuple-permutation compositions. It was run locally on 2026-11-13; recorded exact JSON output `research_notes/R758P6_EXACT_EVIDENCE.json`. No background compute, remote execution, credentials or native theorem acceptance is claimed.
