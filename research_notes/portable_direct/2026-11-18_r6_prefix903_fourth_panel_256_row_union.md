# PREFIX-904-A — Fourth 64-row complete collision panel and exact 256-row symmetric union

Date: 2026-11-18 (Asia/Shanghai). Lane: 进取数论研究6; independent portable-direct auxiliary research.
Science pin: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`, unchanged.
Predecessors: PREFIX-897, PREFIX-900, PREFIX-901, PREFIX-902; parallel independent PREFIX-903 dyadic-gap result incorporated in PREFIX-904-B.
Status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / EXISTING_BYTE_PINNED_CLASSIFIER_REUSED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
The shared RS-X6-NATIVE-TIME-DYNAMICS task has separate ownership and its native admission boundary remains unchanged.

**Designation reconciliation:** This fourth-panel calculation was initially prepared under the local PREFIX-903 label before discovering the independently published PREFIX-903 dyadic-gap theorem. The fourth-panel result is now PREFIX-904-A. Its 7,630,612,196 count is relative to PREFIX-902 and *excludes* dyadic-gap certificates; the canonical combined PREFIX-904-B result (including dyadic-gap overlap removal) is **7,632,945,416**. The source filename is preserved as provenance rather than rewritten.

## Precisely stated auxiliary model

Let \(p=32\), \(N=2^{32}\), \(Q=\{262145,262147,\ldots,524287\}\) (131072 positive odd moduli), and \(T=(p+1)N\). The legal, distinct *directed and named* transitions are \(Z_x=(x,x)\) and \(F^i_x=(x,x\oplus2^i)\), for \(0\leq x<N\), \(0\leq i<32\). For \((a,b)\in Q^2\), the observer returns \(\Phi_{a,b}(u,v)=(u\bmod a,v\bmod b)\). A collision means two different legal named transitions with the same observation, not lossless equality of their original source and trajectory data.

Let \(U\subset Q\) be the exact 552-element PREFIX-895 previously certified special set, and define the prior sufficient-collision set
\[
E=\{(a,b):ab<T\;\lor\;a\in U\;\lor\;b\in U\;\lor\;\operatorname{lcm}(a,b)<N
\;\lor\;33\lceil N/a\rceil>b\;\lor\;33\lceil N/b\rceil>a\}.
\]
The established exact count is \(|E|=7,567,620,214\).

Let \(P_0=\{510001+194j\}\), \(P_1=\{510003+194j\}\), \(P_2=\{510005+194j\}\), all with \(0\le j<64\), and \(P=P_0\cup P_1\cup P_2\), \(|P|=192\).
The already published PREFIX-902 symmetric union has size \(7,614,875,038\).

Define the fourth panel \(B=\{510009+194j:0\le j<64\}\). Direct membership checks give \(B\cap U=\varnothing\) and \(B\cap P=\varnothing\).

## Proposition 904-A — Complete fourth panel

All \(64\cdot131072=8,388,608\) ordered pairs in \(B\times Q\) have a collision in the declared auxiliary model. Exhaustive, disjoint priority classification with the byte-pinned PREFIX-900 finite two-flip checker yields

| Priority class | Count |
|---|---:|
| Existing four-family \(E\) | 505,808 |
| Zero-step versus flip witness | 3,479,779 |
| Anchored flip-versus-flip witness | 4,402,632 |
| General flip-versus-flip witness | 389 |
| Unresolved | **0** |
| **Total** | **8,388,608** |

Each of the 64 rows has exactly 131072 classified \(b\)'s. Every 389 general-flip witness was reconstructed and checked for range, distinct labeled transitions, the exact XOR operation and both modular congruences; three anchored examples per row (192 in total) passed the same checks. A separate Python implementation independently recomputed \(E\)-membership for all \(B\times Q\) pairs and agreed row by row. The complete per-row counts are in \`PREFIX903_R6_FOURTH_PANEL_64ROW_COUNTS.csv\`. The C++ checker is the *already published*, exact Git blob \`175aabe087718cc48ecc8e2f7492cef6731fc5ca\` at \`research_notes/portable_direct/PREFIX900_R6_64ROW_FF_COMPLETE.cpp\` (source commit \`f3237399a1daed4c88120e4f6b5f9be64a6d3e00\`). Reproduction and independent union arithmetic are in \`PREFIX903_R6_FOURTH_PANEL_CHECK.py\`.

The proof of finite completeness reuses the explicit exhaustive signed two-flip index, congruence and integer-bit-fiber counting argument established in PREFIX-900; the result is a computational theorem under that checker and the declared finite model. It is not a claim of independent review or native X6 event admission.

## Proposition 904-B — Exact de-duplicated 256-row symmetric union

The reversal map \((x,y)\mapsto(y,x)\) preserves legal named XOR flips and bijects collisions for \((a,b)\) with collisions for \((b,a)\). Hence panel \(B\times Q\) also certifies \(Q\times B\).

The exact existing-family intersections are:
\[
|E\cap (B\times Q)|=505808,\quad
|E\cap (B\times P)|=83,\quad
|E\cap(B\times B)|=64.
\]
The previously verified \(E\cap(P\times Q)\) count is \(507393+506797+505972=1520162\). The combined square intersection is \( |E\cap((P\cup B)^2)|=594\), agreeing with \(364+2\cdot83+64\).

Every overlap is accounted for by inclusion-exclusion. The **new**, nonoverlapping pair count is
\[
\Delta=2\bigl(64\cdot131072-505808-(64\cdot192-83)\bigr)-(64^2-64)
=\boxed{15,737,158}.
\]
The exact 256-row union and its complement in \(Q^2\) are therefore
\[
\boxed{7,614,875,038+15,737,158=7,630,612,196},\qquad
\boxed{17,179,869,184-7,630,612,196=9,549,256,988}.
\]
An independent calculation using
\[
|E\cup (D\times Q)\cup(Q\times D)|
=|E|+2(|D||Q|-|E\cap(D\times Q)|)-(|D|^2-|E\cap D^2|),\quad |D|=256
\]
returns the same 7,630,612,196. Both calculations use exact integers.

## Reproduction, source, status and continuation

The original C++ file was fetched through the authorized GitHub connector; the local file had 5130 bytes and Git blob SHA-1 equal to \`175aabe087718cc48ecc8e2f7492cef6731fc5ca\`. The original checker was compiled with \`g++ -O3 -std=c++17\`; 64 full first-port runs were performed on all 131072 choices each. The separate Python checker compiled the same byte-verified C++ file again, verified all 64 CSV rows, validated all 389 general witnesses, recalculated the old-family classification on all panel pairs, and checked both union formulas. Its local outcome: \`all_resolved=true; general_witnesses_checked=389; delta=15737158; union=7630612196\`.

Scientific input is frozen; this publication supplies auxiliary, observer-relative collision certificates, not an assertion that this reduced observer is P000's complete native six-axis spatial state, accepted Link/Port triadic operation or physical time evolution. Preserve provenance and source identity on any later transfer.

The global boundary remains \(B_{\mathrm{fix,odd}}(32)\in\{19,20\}\). The next useful direction is a uniform modulus-pair witness criterion or another disjoint panel, while retaining the possibility of a true injective modulus pair rather than precommitting to its nonexistence.

No formal CLAIM, mathematical Result, independent review, Working Truth or P000 promotion is inferred from this GitHub publication.
