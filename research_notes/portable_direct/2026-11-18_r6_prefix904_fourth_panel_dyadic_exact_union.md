# PREFIX-904 — Fourth 64-row named-XOR panel combined with uniform dyadic-gap certificates

Date: 2026-11-18 (Asia/Shanghai). Research mode: independent portable-direct BRC auxiliary observer, no shared X6 CLAIM.
Frozen science input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`, unchanged.
Exact predecessor frontiers: PREFIX-902 (192-row union), PREFIX-903 (uniform dyadic-gap lemma, already published under \`2026-11-18_r6_prefix903_dyadic_gap_uniform_collision.md\`), plus the fourth-panel computational side result \`2026-11-18_r6_prefix903_fourth_panel_256_row_union.md\`, independently generated before discovering the parallel PREFIX-903 designation. The latter's two numerical totals are relative to PREFIX-902; **do not mislabel them as net relative to the dyadic PREFIX-903**.
Evidence status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Scope and observation

Take \(N=2^{32}\), \(Q=\{262145,262147,\ldots,524287\}\), \(|Q|=131072\).
The *full source objects* are named directed trajectories \(Z_x=(x,x)\) and \(F_x^i=(x,x\oplus2^i)\), \(0\le x<N\), \(0\le i<32\), with their source labels retained. The auxiliary observer is
\(\Phi_{a,b}(u,v)=(u\bmod a,v\bmod b)\).
A collision is equality of two observations for different full source trajectories. This is an observer-relative certificate, not an identity or faithful compression of the complete P000/X6 state.

Let \(E\subset Q^2\) be the exact PREFIX-897 four-family sufficient-collision set of size \(7,567,620,214\), comprising total capacity, the 552-element certified special-modulus set \(U\), zero/zero LCM collision, and the two oriented maximal-fiber conditions. Let \(P\subset Q\) be the 192-element combined PREFIX-900/901/902 row set; \(|E\cup(P\times Q)\cup(Q\times P)|=7,614,875,038\).
Let \(B=\{510009+194j:0\le j<64\}\), disjoint from \(U\cup P\); put \(A=P\cup B\), \(|A|=256\).
Let \(D=\{(a,b)\in Q^2:|a-b|=2^h,\ 1\le h\le17\}\), a uniform constructive same-source collision family from the already proved PREFIX-903 theorem, \(|D|=4,194,306\).

## Lemma 904-A — Complete new 64-row panel

Using the exact 5,130-byte original PREFIX-900 C++17 collision classifier with Git blob \`175aabe087718cc48ecc8e2f7492cef6731fc5ca\`, every one of the \(64\cdot131072=8,388,608\) ordered pairs in \(B\times Q\) was checked exhaustively. The disjoint classification is:

| Old E | Zero/flip | Anchored flip/flip | General flip/flip | Unresolved |
|---:|---:|---:|---:|---:|
| 505,808 | 3,479,779 | 4,402,632 | 389 | **0** |

The 389 general-flip witnesses were individually checked for range, label distinction, XOR end state, and both congruences. In addition, three anchored witnesses per row were checked, and a separate Python recomputation agreed on the entire \(E\cap(B\times Q)\) indicator. The per-row certificate is \`PREFIX903_R6_FOURTH_PANEL_64ROW_COUNTS.csv\`; the complete reproducibility program is \`PREFIX903_R6_FOURTH_PANEL_CHECK.py\`. Both names retain initial local designation, while the final combined mathematical continuation is PREFIX-904.

Time reversal swaps the observer ports and establishes the mirror certificates \(Q\times B\). Exact intersections:
\[
|E\cap (B\times Q)|=505808,\quad |E\cap (B\times P)|=83,\quad |E\cap(B^2)|=64,
\]
\[
|E\cap(A^2)|=594,\quad |E\cap(P\times Q)|=1520162.
\]
Inclusion-exclusion therefore gives the *panel-only* (not yet dyadic-augmented) union
\[
|E\cup(A\times Q)\cup(Q\times A)|
=7567620214+2(256\cdot131072-1520162-505808)-(256^2-594)
=\boxed{7,630,612,196}.
\]
Its net increase against PREFIX-902 is \(15,737,158\).

## Theorem 904-B — Fully de-duplicated combination with PREFIX-903

The already proved dyadic family \(D\) is collision-certified regardless of panel membership. For each \(h=1,\ldots,17\), enumerate the increasing positive-gap pairs \(b=a+2^h\) in \(Q\); every ordered pair is counted twice, for the two port orientations. The exact membership tests for \(E\), \(P\) and \(A\) determine *how many dyadic pairs remain outside the panel-only union*.

The dyadic full-family count is \(4,194,306\). The exact intersections, using ordered-pair counts, are:

| Quantity | Count |
|---|---:|
| \(D\cap E\) | 1,846,732 |
| \(D\cap[(P\times Q)\cup(Q\times P)]\) | 10,878 |
| Their intersection | 16 |
| New dyadic pairs beyond PREFIX-902 | 2,336,712 |
| \(D\cap[(A\times Q)\cup(Q\times A)]\) | 14,376 |
| Its intersection with \(E\) | 22 |
| **New dyadic pairs beyond the 256-row panel-only union** | **2,333,220** |

Of the \(2,336,712\) formerly new dyadic certificates, **3,492** have now been subsumed by the fourth row panel. Therefore the exact fully combined certified set has

\[
\boxed{
|E\cup(A\times Q)\cup(Q\times A)\cup D|
=7,630,612,196+2,333,220
=7,632,945,416.
}
\]

Equivalently, the true **increment over the previously published PREFIX-903 dyadic result** is
\[
\boxed{7,632,945,416-7,617,211,750=15,733,666}.
\]

The complement within all \(|Q|^2=17,179,869,184\) ordered pairs is exactly
\[
\boxed{9,546,923,768}.
\]
This complement means *outside the explicit certified families*, not proven injectivity.

The 17 exact dyadic classes, listing gap exponent \(h\), newly certified dyadic pairs beyond the 256-panel-only union, and their overlap removed by the new fourth panel, are:

| h | Additional after 256 rows | Fourth-panel overlap removed |
|---:|---:|---:|
| 1 | 145924 | 254 |
| 2 | 145918 | 128 |
| 3 | 145776 | 128 |
| 4 | 145632 | 256 |
| 5 | 145600 | 256 |
| 6 | 145512 | 256 |
| 7 | 145350 | 256 |
| 8 | 145028 | 256 |
| 9 | 144392 | 256 |
| 10 | 144142 | 256 |
| 11 | 143616 | 256 |
| 12 | 142676 | 234 |
| 13 | 140792 | 192 |
| 14 | 136882 | 128 |
| 15 | 128438 | 124 |
| 16 | 112000 | 128 |
| 17 | 75542 | 128 |
| **sum** | **2,333,220** | **3,492** |

Two independent inclusion-exclusion routes agree: (i) start from PREFIX-902, add the fourth panel, then add dyadic residuals; (ii) start from PREFIX-903 dyadic, add fourth panel, then subtract its 3,492 dyadic overlaps. All arithmetic is exact integers. The dyadic-gap membership code iterated all 2,097,153 increasing power-of-two-gap pairs, representing 4,194,306 ordered pairs. The existing panel checker separately performed 64 entire modulus rows and checked all identified general witnesses. Both are fully reproducible from published source, without random sampling in the stated finite domains.

## Evidence, scope boundaries and continuation

Published source chain:
- Existing original C++17 proof checker: \`research_notes/portable_direct/PREFIX900_R6_64ROW_FF_COMPLETE.cpp\` at \`f3237399a1daed4c88120e4f6b5f9be64a6d3e00\`, Git blob \`175aabe087718cc48ecc8e2f7492cef6731fc5ca\`.
- \`research_notes/portable_direct/PREFIX903_R6_FOURTH_PANEL_CHECK.py\` and \`PREFIX903_R6_FOURTH_PANEL_64ROW_COUNTS.csv\`: exhaustive fourth-panel counts and exact symmetric 256-panel union.
- Existing \`research_notes/portable_direct/PREFIX903_R6_DYADIC_GAP_CENSUS.py\`: independent dyadic construction and exhaustive checks.
- Companion \`PREFIX904_R6_DYADIC_PANEL_UNION_CHECK.py\` and \`PREFIX904_R6_DYADIC_PANEL_UNION_RESULTS.csv\`: full de-duplication.
No native X6 Cell/Link/Port triadic admission is inferred; P000 is unchanged. Nor is this a formally frozen Result, independent review or Working Truth.

The unresolved central goal is \(B_{\mathrm{fix,odd}}(32)\in\{19,20\}\). A next useful direction is to extend uniform collision theorems to non-power-of-two modulus gaps, or to test disjoint residue-conditioned candidate classes with exact witnesses while reporting genuine injectivity if found.
