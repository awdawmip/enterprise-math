# R762CT — Source-resolved K4 BRC: one-step sufficient future observer

**Date:** 2026-11-17. **Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142. **Research identity:** EM-X6-3050F6, existing Run RUN-2f66fcc8f96765967a2e8cae. **Frozen science:** taskbook e3f42efac29a2da2d95be391f3231a664e2fade0; P000 V5 a72226e2430ffa4786321ac86e7f0c599d5f0389. **Predecessor:** R762CS, GitHub PR #2612 @ 562db81b5649ddce718ce8469e57c93bcbcf79ce. **Status:** exact finite exhaustive argument plus independently implemented numerical reproduction; independent review NOT_REVIEWED.

## Definition and scope

Let $E=(01,02,03,12,13,23)$ denote the six named edges of an auxiliary K4. The ten states are the unordered complementary three-subsets

$$
S=\{T\subseteq E:\ |T|=3\}/(T\sim E\setminus T),\quad |S|=10.
$$

Use the smaller six-bit mask as the canonical representative. Let $F:S\to\{0,1\}$ indicate the four star/face configurations, and let $P=1-F$. A source-equality assignment $\pi:E\to\{0,\ldots,k-1\}$ is a set partition in canonical restricted-growth order. There are $B_6=203$ choices.

For each source class $j$, define the nonnegative integer matrix $B_j(s,t)$ by counting swaps of one edge label in one triple with a label in its complement, where both labels have source class $j$, leading to state $t$. For a class word $\omega=(j_1,\ldots,j_h)$, let $B_\omega=B_{j_1}\cdots B_{j_h}$ with $B_\varnothing=I$. Define the full source-selective F/P counting observer through depth $h$ as

$$
\mathcal O_h^{\mathrm{src}}(s)=
\left((B_\omega F)(s),(B_\omega P)(s)\right)_{|\omega|\le h}.
$$

A word specifies which source class is allowed at each candidate update, in that order. This query language refines the uncolored weighted operator $T=\sum_jw_jB_j$ used in R762CS. For fixed strictly positive weights $w_j$, the count for a specific word is multiplied by $\prod_rw_{j_r}>0$, identically for any starting state.

## Theorem — sharp universal one-step sufficiency

For every one of the 203 source partitions, every strictly positive real source weight vector, and all $s,t\in S$,

$$
\boxed{\ \mathcal O_1^{\mathrm{src}}(s)=\mathcal O_1^{\mathrm{src}}(t)
\ \Longleftrightarrow\
\mathcal O_\infty^{\mathrm{src}}(s)=\mathcal O_\infty^{\mathrm{src}}(t).\ }
$$

The bound one is optimal: some same-F/P states differ in a one-letter source-selective observation. The minimal sufficient class-count distribution across all 203 partitions is:

| Number of distinguishable states | Source partitions |
|---:|---:|
| 2 | 2 |
| 3 | 27 |
| 4 | 28 |
| 5 | 66 |
| 6 | 24 |
| 7 | 24 |
| 10 | 32 |
| **Total** | **203** |

In particular, in 32 source configurations no two of the ten named states can be collapsed under this future-query language.

### Exhaustive certificate and proof

For fixed $\pi$, the one-step signature is

$$
\sigma(s)=
\left(
F(s),P(s),
\big((B_jF)(s),(B_jP)(s)\big)_{j=0}^{k-1}
\right).
$$

Partition $S$ into its signature fibers $C_1,\ldots,C_m$. For every partition $\pi$, the executable proof derives all ten states and transitions directly from the edge labels and tests this **equitable-quotient identity** for every pair $s,t$ of the same fiber, every source class $j$, and every destination fiber $C_b$:

$$
\boxed{\quad
\sum_{u\in C_b}B_j(s,u)=
\sum_{u\in C_b}B_j(t,u).
\quad}\tag{1}
$$

The exact integer census checks 203 source partitions, 2,030 state signatures, 1,245 within-fiber unordered state pairs and **4,038 pair/source comparisons**, each comparing the complete integer vector over the destination fibers. The verifier enumerates all restricted-growth partitions recursively and checks every applicable pair; its domain is finite and exhaustive.

By (1), every $B_j$ descends to a well-defined integer matrix on the signature fibers. Since $F$ and $P$ are constant on the fibers, induction on the word length shows that every source-word future F/P count is fiber-constant. Conversely, the empty word and all length-one words already occur in $\mathcal O_1^{\mathrm{src}}$; states with different signatures are immediately distinguishable. This proves both future sufficiency and minimality. Strictly positive source weights preserve these equivalences because a fixed word is multiplied by the same nonzero positive factor at both states.

The theorem quantifies over **all** source partitions of these six labels and all positive weights. The 203-pattern census is a finite exhaustive proof, followed by an algebraic induction covering infinitely many word lengths. The claim is specific to the declared ten-state candidate graph and its F/P source-word observer.

## Provenance-loss counterexample for aggregated observation

Let $\pi=000011$ in edge order $(01,02,03,12,13,23)$, so source 0 contains the first four edges and source 1 the final two. Choose canonical masks 19 and 22, state indices 4 and 6.

With *unit* weights $w_0=w_1=1$, both states have identical uncolored F/P observations at time 0, 1 and 2:

$$
\mathcal O_2^{\mathrm{total}}(19)=
\mathcal O_2^{\mathrm{total}}(22)
=((0,1),(2,3),(8,17)).
$$

By the verified R762CS theorem, their future uncolored total counts agree at every later step. Source-selective one-step F counts differ:

$$
((B_0F)(19),(B_1F)(19))=(2,0),\qquad
((B_0F)(22),(B_1F)(22))=(1,1).
$$

Selecting only source class 0 distinguishes 2 from 1 immediately. This shows exactly how a provenance-sensitive future operation can separate states whose complete uncolored future count language is identical.

For the unit-weight comparison on all 203 source partitions, 66 source-resolved quotients strictly refine the uncolored two-step quotient. The largest number of source-resolved classes inside an uncolored fiber is 1 for 137 partitions, 2 for 57, and 3 for 9. Therefore, for this precisely declared unit-weight observer comparison, the optimal maximum fixed-length repair coordinate is **2 bits**, and the nine three-way cases make that bound sharp.

## Reproducibility and next native question

The accompanying Node.js verification script uses only standard language facilities and exact integers, and outputs the matching evidence JSON; the finite classification was also cross-checked with an independently written Python enumeration. Review status: NOT_REVIEWED.

R762CS establishes two-step sufficiency for the *aggregate* weighted F/P count observer. R762CT establishes one-step sufficiency for the *source-selective word* observer, with greater state distinctions. The native TRIADIC_CLOSURE_E task still requires an actual signed Cell/Link/Port admissibility/update law and source-backed V17/V29/V39 transport. The next discriminating test is to derive its legally selectable source words and check whether those words descend through the present quotient; any surviving path-area or signed Port query must preserve its necessary additional provenance coordinates from R762CH/CK. This work is a conditional positive N-BRC model, not a native signed force cancellation certificate.
