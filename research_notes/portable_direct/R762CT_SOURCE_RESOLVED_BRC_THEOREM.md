# R762CT — Source-resolved K4 BRC: a sharp one-step sufficient observer

**Date:** 2026-11-17. **Task:** `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, publication `TP2-8B7E13C5904A2D6F1142`. **Research identity:** `EM-X6-3050F6`, existing run `RUN-2f66fcc8f96765967a2e8cae`. **Status:** exact finite exhaustive proof and independently implemented arithmetic check; author-verified, independent review `NOT_REVIEWED`. **Frozen science:** taskbook `e3f42efac29a2da2d95be391f3231a664e2fade0`, P000 V5 input `a72226e2430ffa4786321ac86e7f0c599d5f0389`. **Immediate predecessor:** R762CS, PR #2612, `562db81b5649ddce718ce8469e57c93bcbcf79ce`.

## 1. Exact mathematical domain and question

Use the ten states $S$ of unordered complementary three-subsets of the six *named* auxiliary K4 edge labels (E=(01,02,03,12,13,23)), with the representative of $T\sim E\setminus T$ the smaller six-bit integer mask. Write $F:S\to\{0,1\}$ for the four star/face states and $P=1-F$ for the other six states. A source equality partition $pi:E\to\{0,\ldots,k-1\}$ assigns each edge to exactly one class, with class labels in restricted-growth order. There are $B_6=203$ such partitions.

For a source class $j$, let (B_j(s,t)) count the admissible *candidate* swaps: choose one label $x$ in one triple and one $y$ in its complement with (pi$x$=pi$y$=j), exchange their membership, and reach the unordered state $t$. These matrices have nonnegative integer entries. For a word (omega=$j_1,\ldots,j_h$), set $B_omega=B_{j_1}\cdots B_{j_h}$, with $B_\varnothing=I$. The source-selective future observer is the full two-channel vector
$
\mathcal O_h^{\rm src}$s$=
\big($B_\omega F$$s$,$B_\omega P$$s$\big)_{|\omega|\le h}.
$
The word fixes the *sequence of source classes allowed at successive candidate steps*. This is a richer query language than R762CS's single uncolored weighted sum $T=\sum_j w_jB_j$. For positive real class weights $w_j>0$, the weighted word operator is ($\prod_{r=1}^h w_{j_r}$B_\omega); this factor is strictly positive and independent of the starting state.

All statements below concern this conditional **positive-count N-BRC** source-selective model; no signed native `TRIADIC_CLOSURE_E` event law is assumed.

## 2. Main theorem: one step is globally sufficient and sharp

**Theorem.** For every source partition $pi$ of the six named edges, every strictly positive real source weight vector, and all $s,t\in S$,
$
\boxed{\mathcal O_1^{\rm src}$s$=\mathcal O_1^{\rm src}$t$
\quad\Longleftrightarrow\quad
\mathcal O_\infty^{\rm src}$s$=\mathcal O_\infty^{\rm src}$t$.}
$
The uniform bound 1 is optimal: for example $pi=000011$, two path/path states with masks 19 and 22 have equal present F/P type but different first-step source-selective F counts.

The resulting minimal sufficient quotients have the following exact distribution across all 203 source partitions:

| Minimal equivalence class count | Number of partitions |
|---:|---:|
| 2 | 2 |
| 3 | 27 |
| 4 | 28 |
| 5 | 66 |
| 6 | 24 |
| 7 | 24 |
| 10 | 32 |
| **Total** | **203** |

Thus 32 admissible source-label patterns have **no nontrivial lossless state identification** in the specified future source-selective language: all ten named decomposition states remain distinguishable.

### Finite proof with an explicit equitability certificate

For a fixed $pi$, define a signature on each state:
$
\sigma$s$=\left(F$s$,P$s$,\big($B_jF$$s$,$B_jP$$s$\big)_{j=0}^{k-1}\right).
$
Let $C_1,\ldots,C_m$ be its distinct fibers. The exhaustive verifier derives $pi$ recursively, derives the ten states from the 20 triples and complement equivalence, and builds all source-labelled transitions from the raw exchange law.

For **each** $pi$, it checks the following exact integer identity for every $s,t\in C_a$, every source class $j$, and every signature class $C_b$:
$
\boxed{\sum_{u\in C_b}B_j(s,u)=\sum_{u\in C_b}B_j(t,u).}\tag{*}
$
It checks 203 partitions, 2,030 state signatures, 1,245 same-fiber unordered state pairs and **4,038** pair/source equitability comparisons (each comparison checks the full vector over all destination fibers). No sample restriction on the source partitions or arithmetic approximation is involved.

Consequently each $B_j$ descends to a well-defined integer transition matrix $overline B_j$ on the signature classes, and (F,P) are constant on the fibers by definition. Induction on the word length shows that all $B_\omega F,B_\omega P$ are constant on each signature class for every finite word. The reverse direction holds because the empty and one-letter words are already included in the infinite language. Therefore the theorem follows. Positive weights preserve all state equalities and separations because every fixed word scales both compared readouts by the same nonzero scalar.

Minimality is immediate: two states with different signatures are distinguished by either the empty word or a one-letter source-selection query; no coarser state quotient can preserve this language.

This is an exact *finite-domain proof*: its generality is over all set partitions of **this** six-element source set and all positive weights, supported by fully specified exhaustive enumeration and an elementary quotient-induction argument. It does not assert a similar one-step law for arbitrary numbers of edges or different event graphs.

## 3. New provenance-loss witness against the uncolored observer

Take source partition $pi=000011$, with source class 0 on edges (01,02,03,12) and class 1 on (13,23). Choose $s$ with mask 19 and $t$ with mask 22 (state indices 4 and 6 in ascending canonical mask order). With *unit source weights* $w_0=w_1=1$, the previous uncolored observer of R762CS gives the identical observations
$
\mathcal O_2^{\rm total}$s$=\mathcal O_2^{\rm total}$t$
=((0,1),(2,3),(8,17)).
$
By R762CS, these two states also agree for *every* subsequent uncolored total F/P path count.

Nevertheless the separately selectable source-class first-step F counts are:
$
($B_0 F$$s$,$B_1 F$$s$)=(2,0),\qquad
($B_0 F$$t$,$B_1 F$$t$)=(1,1).
$
For the source word $\omega=(0)$, the observed F count is 2 versus 1. This is an explicit **observer-language-dependent residual**: the source channel can recover a distinction lost even after all uncolored future observations.

Across all 203 partitions with unit weights, the source-selective one-step quotient is strictly finer than the uncolored two-step quotient in **66** cases. The largest number of source-selective classes within a single uncolored fiber is 1 in 137 partitions, 2 in 57, and 3 in 9. Thus, *for this unit-weight comparison*, an optimal fixed-length fiber repair needs up to **2 additional bits**, and the 9 three-way fibers establish sharpness. Source-selective weight positivity does not impose a numerical upper bound on arbitrary uncolored weight coincidences; that separate comparison is not asserted here.

## 4. Scope, use and next question

Theorem R762CS concerns the uncolored aggregate family (T^r(F,P)) and has a sharp two-step horizon; R762CT concerns individually selectable source-class operators $B_j$ and has a sharp one-step horizon, with potentially more distinguishable states. The result supplies a concrete BRC *future-query interface* for provenance-preserving comparisons, not a claim of native triadic event admission.

To test the actual `TRIADIC_CLOSURE_E` problem, first obtain or construct its signed Cell/Link/Port incidence predicate under the frozen P000 and required V17/V29/V39 transport, then check which source-selective words are genuinely licensed. The corresponding allowed-language subfamily determines the observer quotient. Orientation and the closed-path area/provenance residuals of R762CH/CK remain explicit candidate coordinates until their future operation safety is established.

**Reproduction:** run `node R762CT_SOURCE_RESOLVED_BRC_VERIFY.js` (Node.js, no packages). It prints `R762CT_SOURCE_RESOLVED_BRC_EVIDENCE.json`. The same result was independently cross-checked in a Python integer implementation of the 203-partition signature and quotient census. Exact integer checks support this conditional six-edge theorem; independent mathematical review remains `NOT_REVIEWED`.
