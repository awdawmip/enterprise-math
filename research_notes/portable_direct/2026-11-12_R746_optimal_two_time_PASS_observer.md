# R746 — Optimal two-time V29 PASS observer for the branch-blind BRC triad loops

Date: 2026-11-12 (Asia/Shanghai). Independent author-side conditional theorem, not native X6 admission.
Parent scientific question: RS-X6-TRIADIC-CLOSURE-DYNAMICS.
Frozen P000 science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` (P000 V5 and joint-observer companion).
Exact dependency: R744 at `9f266f4d182abf7c6c0bdb3c3fed621987b9be80`, especially its three rooted length-3 loops and four branch-blind binary PASS codebooks for each of two carriers.
Existing native V29 PASS counter semantics: `M[a,b] += 1`. All stock and sampling claims below are *typed observers of this cumulative counter*, not assertions of physical token movement.

## Question and observer definitions

A fixed R744 generator emits four offdiagonal PASS pulses `F=PASS(0→1)`, `R=PASS(1→0)`: the first arc pulse `x`, one helper pulse `\bar x` inverse to it, and two remaining arc pulses `y,\bar y`. Thus every generator word is `x \bar x y \bar y`. At the end of each 4-pulse period the counter increment is always (F,R)=(2,2). The hidden symbol is one of I,P,Q.

Write `D_t=M_{01}(t)-M_{10}(t)`; observe cumulative PASS counts at chosen clocked within-period times `t∈{1,2,3,4}`, with the period anchored at `D_0=0`. An observation is a read of this integer contrast only. It does not read the active BRC triad, arc identity, force source, future branch or full event log. The problem is to recover the complete ordered generator word from such sparse reads.

## Theorem A — exact time-contrast factorization

For every R744-valid source-injective branch-blind codebook, with `x,y∈{F,R}`, the contrast trace is

```text
D_0=0,
D_1=s(x),  D_2=0,  D_3=s(y),  D_4=0,
s(F)=+1, s(R)=-1.
```

Hence the two timestamps (1,3) capture exactly the ordered pair (x,y). For either network and all four valid codebooks, the map

```text
{I,P,Q} → {(D_1,D_3)}
```

is injective. Proof: among the three rooted loops, one first arc uses one outgoing root branch and the other two use the opposite root branch, so the first contrast separates the singleton. The remaining pair traverses distinct second arcs out of the same intermediate triad; source injectivity forces their y labels to differ. Thus the third contrast separates that pair. Four-pulse balance guarantees D resets to zero before the next period. Induction yields lossless reconstruction of any finite word `w∈{I,P,Q}^k` from its 2k clocked (1,3) contrast samples.

For one R744 codebook on each network:

| network | I signature | P signature | Q signature |
|---|---|---|---|
| A | (-1,+1) | (+1,+1) | (+1,-1) |
| B | (+1,+1) | (-1,-1) | (+1,-1) |

Ordered generator reconstruction then yields its exact final V17 S3 holonomy by multiplying the already specified I/P/Q permutations. It also recovers the entire generator sequence, not merely its terminal relation. The injection holds for all lengths k, without probabilistic assumptions.

## Theorem B — sharp sampling cost for this observer class

For one period, `D_2=D_4=0`, while each of `D_1,D_3` is binary. No single fixed within-period contrast sample can distinguish three generator choices. The pair (1,3) does, so **two time-indexed integer-contrast reads per generator are necessary and sufficient**.

More strongly, if a *fixed nonadaptive* sampling schedule is to recover every one of the `3^k` independent generator words of length k from contrast alone, it must sample both t=1 and t=3 in *every period*, hence exactly 2k reads are optimal. Proof by changing only a period with fewer than two informative reads; its observed signature has at most two values for three symbols, and all other periods start and end with D=0, giving two indistinguishable global histories.

For an adaptive read policy, inspect either t=1 or t=3, and inspect the other only in the ambiguous 2-symbol branch. It uses one read for one generator and two for the other two, so worst-case 2 reads and, under independent uniformly selected I/P/Q, exact expected cost 5/3 reads per period. Since any first read offers at most two outcomes, this is optimal within this single-period two-time contrast-read model. No probability law is assumed by the lossless deterministic theorem.

## Theorem C — the two-stock quantities are derived counter potentials

Define `\widehat b_0(t)=1-D_t`, `\widehat b_1(t)=1+D_t`. Then `\widehat b_0+\widehat b_1=2` identically, and a pulse F changes the derived pair by (-1,+1), while R changes it by (+1,-1). The R744 prefix-capacity condition `0≤\widehat b_i≤2` is **exactly equivalent** to `|D_t|≤1`. Every valid R744 word attains this property and returns to (1,1) after four pulses.

This is an explicit readout factorization through the genuine cumulative PASS counts; for the declared counter-based capacity observer, no separately stored token inventory or postulated physical transport dynamics is needed. A native interpretation involving physical token carriers, Cell/Link/Port authorization, force/closure consumption or creation still requires its own event rule. The two local PASS ports are not two spatial dimensions or a native two-dimensional plane.

## Exact verification, provenance, and boundary

The accompanying standalone JavaScript checker enumerates all 2^7 binary arc assignments on each rooted seven-arc carrier. It recovers exactly 32 locally source-injective codebooks and exactly four valid inverse-first-helper balanced codebooks per carrier. Every valid codebook has three distinct paired signatures and every individual timestamp has at most two signatures. For each of eight valid codebooks it exhaustively checks all 9,841 words of lengths 0..8, independently reconstructing the generator sequence from (D1,D3), verifying every |D|≤1 prefix, final equal counts, and recovered named S3 relation: **78,728 exact histories**. Infinite-word-length injectivity follows from the period-reset induction, not from finite search.

Input provenance: R744's published exact frozen loop graph and named generator permutations; SOURCE current behavioral rules read separately. Mathematical status: author proof with exact finite validation; independent Source scientific review pending. Formal native CLAIM/Result is not asserted by this research-branch publication.

## Consequence and next discriminating native test

The terminal counter pair `(M01,M10)` at every period boundary loses the whole I/P/Q word (and can lose all six final holonomies). Two within-period time-tagged contrast observations per period instead retain every generator identity exactly. This isolates a concrete interface distinction: **the missing native question is whether an X6-permitted, causally ordered PASS event may be emitted as the inverse-first helper while preserving the three nonzero attached force sources, the active TRIADIC_CLOSURE_E certificate and signed-axis provenance, and whether its timestamped counter readout is exposed.** The counter observer itself is implementable by integer subtraction on the existing PASS ledger; physical realization is a separate task.

No P000 axiom, frozen science pin, native role, CLAIM or review status is changed.
