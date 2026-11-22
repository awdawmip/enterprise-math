# EC49FWZ — Exact optimal observer for a complete antipodal-free relative-phase transversal

**Date:** 2026-11-22. **Frozen scientific input:** BRC16943 (unchanged). **Direct predecessor:** EC49FWY, immutable proof at \`awdawmip/enterprise-math@c2e77728240c9c4281a999a9a0e92ef4b7d63c28:research_notes/portable_direct/EC49FWY_RELATIVE_PHASE_ALIAS_BIFURCATION_THEOREM.md\`. **Evidence status:** AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.

## Observer and scope

Retain the exact auxiliary finite CRT/Farey model from EC49FWY. A known Boolean reference is

\[
w(t)=\mathbf1_U(t\bmod10)\,\mathbf1_V(t\bmod11),\qquad t\in\mathbb Z/110,
\]

where U is one of 50 frozen P10 support masks and V is the full mod-11 residue set or the complement of one residue. The sensor channels are \(L(t)=w(t-s_L)\), \(R(t)=w(-t-s_R)\); one activation at physical site \(t\) reads **two separate Boolean bits**. The complete indexed reflection-defect spectrum of each side, the reference, and the admissible relative phase set \(D\) are known. The target is the two observed membership words, not an absolute phase coordinate or an X6 temporal state.

EC49FWV/FWY imply that each single-side spectrum admits exactly two distinct observed words separated by half-turn 55. In a nonempty fiber, a set \(D\) with \(D\cap(D+55)=\varnothing\) leaves only the two **simultaneous** half-turn alternatives. Required sampled Hamming distance is \(r\). Distance \(r=1\) permits noiseless identification, \(r=2\) one known *channel-bit* erasure, and \(r=3\) one unknown *channel-bit* error. Errors in whole physical activations (possibly affecting both channels) are a different model.

An **antipodal transversal** \(D\subseteq\mathbb Z/110\) contains exactly one representative of every pair \(\{a,a+55\}\), \(a\in\mathbb Z/55\); equivalently \(|D|=55\) and the reduction \(\pi_{55}:D\to\mathbb Z/55\) is bijective. There are \(2^{55}\) such D. In particular, **all even relative phases** \(D=2\mathbb Z/110\) and all odd relative phases are transversals.

Define \(N_{\rm fixed}(D;r)\) as the smallest number of physical sites chosen *before* U, V and the two phases are revealed, such that the restricted two-channel observations have distance at least r for every compatible nonempty fiber.

## Theorem — full-transversal exact minimum, extended to the maximum possible distance

For **every** antipodal transversal \(D\) and every integer \(1\le r\le40\),

\[
\boxed{N_{\rm fixed}(D;r)=5m(r)},\qquad
m(r)=\begin{cases}
\lceil r/2\rceil+1,&1\le r\le20,\\
\lceil r/2\rceil+2,&21\le r\le40.
\end{cases}
\]

For \(r\ge41\) **no** fixed layout, even all 110 positions, attains the required distance. For every antipodal-free D, regardless of size, its fixed-layout constraint system depends only on \(\pi_{55}(D)\), not on the choice of the antipodal representative in each occupied class. Thus all \(2^{55}\) complete transversals have **identical feasible layouts**, not merely the same optimum.

Selected values:

| r | 1 | 2 | 3 | 4 | 19 | 20 | 21 | 22 | 39 | 40 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| N_fixed | 10 | 10 | 15 | 15 | 55 | 55 | 65 | 65 | 110 | 110 |

For the ordinary targets, parity-only relative-phase uncertainty needs **10** activations for exact recovery, **10** to tolerate one erased channel bit, and **15** to correct one unknown channel-bit error. EC49FWY's known-single-offset optimum is 5/8/10, so the multi-offset worst case here is strictly different despite each spectrum still having only two candidates.

## Proof

**1. Exact finite reduction.** Let \(P_i=\{i,i+5\}\subseteq\mathbb Z/10\), \(i=0,\ldots,4\). The original frozen P10 set has 50 masks; their half-turn disagreement supports are unions of \(P_i\), and at least one admissible mask has exactly one \(P_i\) (the frozen mask U=299 is a concrete witness). A half-turn changes U but leaves V fixed since \(55\equiv0\pmod{11}\). The two-bit sampled distance is additive across differing blocks, so it suffices and is necessary to secure distance r for every singleton block, every missing mod-11 column, every phase.

Fix the singleton block in *observed-left* coordinates as i, and denote the deleted observed column by j. Because \(R(t)=L(\delta-t)\) for \(\delta=s_L-s_R\), the distance for a physical layout \(S\subseteq\mathbb Z/110\) is precisely

\[
F_S(\delta,i,j)=\sum_{t\in S}
\left(
\mathbf1_{t\bmod5=i,\ t\bmod11\ne j}
+
\mathbf1_{(\delta-t)\bmod5=i,\ (\delta-t)\bmod11\ne j}
\right). \tag{1}
\]

Every i, j, and relative phase in D is realizable using a frozen one-pair U, a one-hole V and sensor phases. This validates **necessity**, not merely an upper-envelope argument. Formula (1) depends only on \(\delta\bmod55\), so changing any representative \(\delta\leftrightarrow\delta+55\) does not change a single inequality. For a transversal D all 55 residues modulo 55 occur.

**2. Lower bound by an exact adverse phase.** Partition S into five disjoint physical blocks \(S_i=\{t\in S:t\bmod5=i\}\); write \(m_i=|S_i|\). In each block the 11 mod-11 columns contain \(n_{i,j}\in\{0,1,2\}\) sites with sum \(m_i\), so some j has \(n_{i,j}\ge\lceil m_i/11\rceil\). By CRT and the full projection \(\pi_{55}(D)=\mathbb Z/55\), an allowed phase exists with \(\delta\equiv2i\pmod5\), \(\delta\equiv2j\pmod{11}\). The reflected channel then feeds block i only from S_i and excludes exactly the same column j on each side. Thus

\[
F_S(\delta,i,j)=2(m_i-n_{i,j})\le2m_i-2\lceil m_i/11\rceil.
\]

Consequently **each** block must have at least
\[
m(r)=\min\{0\le m\le22:2m-2\lceil m/11\rceil\ge r\}.
\]
For \(m=0,1\) this bound is zero; for \(2\le m\le11\) it equals \(2m-2\), for \(12\le m\le22\) it equals \(2m-4\). The value at m=12 remains 20, explaining the jump from 55 sites at r=20 to 65 sites at r=21. The displayed two-piece m(r) follows. Summing five independent block lower bounds gives \(N_{\rm fixed}\ge5m(r)\).

**3. Attaining construction.** In *every* block i install m(r) sites with column occupancy at most \(q=\lceil m(r)/11\rceil\): for \(m\le11\) use distinct columns, one of the two physical sites in each column; for \(m\ge12\) use one physical site in each of 11 columns then an additional site in \(m-11\) distinct columns. For arbitrary \(\delta,i,j\), the left contribution from block i is at least \(m-q\). The right contribution comes from block \(k=(\delta-i)\bmod5\), whose reflected deleted column is \((\delta-j)\bmod11\), and is also at least \(m-q\). Hence
\[
F_S(\delta,i,j)\ge2m-2q\ge r.
\]
The same layout works for all transversals and, in fact, for any antipodal-free subset D. Because every actual frozen disagreement mask is a union of singleton blocks, the bound carries to all admissible states. Combining with part 2 gives equality.

**4. Sharp impossibility threshold.** In a singleton-block, one-hole witness each channel's half-turn alternatives differ at exactly 20 of 110 sites; across both channels there are 40 differing bits even if all 110 sites are read. Therefore r>40 is impossible for the declared uniform worst-case target. This is a statement about the finite observer, not X6 time dynamics.

## Complete classification and number of optimal layouts

For r≤20, optimality forces exactly m sites in each block. Their modulo-11 columns must be **pairwise distinct** within that block: a repeated column j permits \(\delta\bmod5=2i\), \(\delta\bmod11=2j\), giving \(F_S\le2m-4<r\). Conversely distinct columns attain the bound. Each chosen column has two physical positions, t and t+55. Consequently the number of optimal fixed site layouts is exactly

\[
\boxed{\bigl(2^m\binom{11}{m}\bigr)^5},\quad 1\le r\le20.
\]

For 21≤r≤40, m≥13 and every block has 22 physical sites, at most two per column. **Any** choice of exactly m physical positions in each block has worst missing-column loss at most four, hence is optimal, giving

\[
\boxed{\binom{22}{m}^5},\quad 21\le r\le40.
\]

The count treats physical positions as distinct but does not count equivalent readout labels or ordered activation sequences.

## Recalculation and limits

The companion self-contained JavaScript verifier independently regenerates 72 primitive P10 directions and their 50 distinct masks, reproduces the disagreement histogram \(\{2:10,4:26,6:10,8:4\}\), checks all **121,000** single-block/offset/column constraints for r=1..40, verifies the lower-bound size inequalities, runs **66,550** direct Boolean-word comparisons against U=299 for all 110 left phases, 55 offset classes and 11 missing columns, and checks the 40-bit maximum. It uses exact integer/Boolean operations and reports ALL_PASS. Those computations cross-check the written proof; no independent reviewer or project theorem acceptance has been asserted.

This is a static *auxiliary finite observer theorem* under the inherited indexed spectra and known reference. It neither collapses original Farey provenance nor proves preservation of future signed X6/heartbeat observations. The original phase, signed branch, Farey anchor, affine seed, height, and residual relations remain separately typed.

## Next discriminating question

For **proper** antipodal-free multi-offset sets (especially short consecutive intervals such as D={0,1}, and larger intervals D={0,...,k−1} with k≤55), determine the exact fixed-layout optimum and characterize transition thresholds in the induced 55-column/5-block incidence hypergraph. Quantify when coupled two-channel savings survive without a fully known relative offset. Then compare the mathematically allowed phase sets against actual same-anchor Farey trajectories, preserving the signed/provenance data necessary for subsequent neighbors.

**Authority and custody:** informed independent portable research continuation under the original frozen scientific pin. Current native lookup for the topic RS-EC49AS is publication-directory-only and has no formal Task directory at checked Source; no formal CLAIM, Result, Review, P000 change or theorem promotion is asserted. Existing Researcher and Activity ownership is preserved.
