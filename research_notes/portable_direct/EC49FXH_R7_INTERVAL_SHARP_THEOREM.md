# EC49FXH — Sharp r=7 paired-bit observation over all consecutive relative-phase sets

Date: 2026-11-23 (Asia/Shanghai). Immutable scientific pin: **BRC16943**. Direct predecessor: EC49FXG (PR #2977; theorem `743ae1d6a00e728a6cd2d38b37d3dbf414fe4aa7:research_notes/portable_direct/EC49FXG_R6_INTERVAL_SHARP_THEOREM.md`). Parent reduction: EC49FWT–FXG. Status: **AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED**.

## Claim (entire k=1..55 regime)

In the inherited *auxiliary* 110-periodic P10/one-hole Farey–CRT double Boolean observer, the known reference and complete separately indexed reflection spectra restrict the relative phase to D_k={0,1,...,k-1} where 1<=k<=55. A fixed physical activation at t mod110 returns two separately counted channel bits. Require sampled bitwise Hamming distance >=7, sufficient for correction of up to three arbitrary unknown channel-bit errors.

**Exact optimal number of physical activation sites:**

    N_fixed(D_k;7)=25-min(5,max(0,floor((26-k)/2))).

| k | 1–16 | 17–18 | 19–20 | 21–22 | 23–24 | 25–55 |
|---|---:|---:|---:|---:|---:|---:|
| optimal fixed activations | 20 | 21 | 22 | 23 | 24 | 25 |

**This is a conditional theorem of the frozen auxiliary CRT observer**. Its equivalence to the original P10/Farey sensor cases is inherited from the cited predecessor chain, not independently re-proved here. The causal Farey branch, anchor, height, signs, affine seed, phase origins and relevant structural residual stay separately typed; no quotient to native X6 or heartbeat dynamics is asserted.

## Exact inherited criterion and universal lower bound

Write S subset Z/110 for activated sites, d in D_k, i in Z/5 and missing column j in Z/11. The inherited necessary-and-sufficient observation criterion is the family of inequalities

    F_S(d,i,j)=sum_{t in S} [1_{t mod5=i,t mod11!=j}+1_{(d-t) mod5=i,(d-t) mod11!=j}] >= 7.

Let m_i be the number of sites in color i (mod5). The unsubtracted count in row (d,i) is n=m_i+m_(d-i). Summing the eleven possible deleted columns removes n total contributions, so when F>=7 we must have n>=8. Summing n over all five i for one fixed d yields 2|S|>=40, hence |S|>=20 for every nonempty phase set.

For k>=5, each color i has a self-reflection phase d in {0,...,4} satisfying d=2i (mod5). The corresponding row has n=2m_i>=8, so m_i>=4. Call a color light when m_i=4 and heavy when m_i>=5. If s colors are light, |S|>=4s+5(5-s)=25-s.

## Ruling out too many light colors

For a light color, its four sites must have pairwise distinct mod11 columns: otherwise the self-reflection row deletes at least two of eight contributions for a suitable j and F<=6. Identify those four distinct columns together with their mod5 color as a 4-subset of the corresponding residue class in Z/55.

For any two light-site residues x,y in Z/55 (including the same residue twice), we must have (x+y) mod55 NOT in D_k. Otherwise choose the phase d=(x+y) mod55 and the deleted column j=x mod11. The two light channels lose at least two of their eight possible contributions; thus F<=6. This is a necessary constraint even when the two residues belong to the same color.

For each color i, enumerate all C(11,4)=330 quadruples of its residues {i+5a:0<=a<=10}, keep exactly those whose 16 ordered pair sums avoid D_k, and enumerate compatible families choosing at most one surviving quadruple per color. Cross-compatibility means all 16 cross sums avoid D_k. This complete finite search, with the enumeration and pruning loop explicit in the attached standalone script, produces:

| k | surviving quadruples by colors 0..4 | maximum compatible light colors |
|---:|---|---:|
| 17 | (1,2,2,1,2) | 4 |
| 19 | (1,1,2,1,1) | 3 |
| 21 | (0,1,1,1,1) | 2 |
| 23 | (0,0,1,0,1) | 1 |
| 25 | (0,0,0,0,0) | 0 |

The search is finite and exhaustive because every light color supplies exactly four *distinct* mod11 columns, every possible four-subset appears in its 330 candidates, and all five color inclusion/exclusion choices are visited. The early pruning condition (chosen_count+remaining_colors<=best_count) cannot discard a larger feasible family. For intermediate k the allowed quadruple and compatibility families only shrink when k increases. Consequently for every 17<=k<=55, s<=max(0,floor((26-k)/2)). This proves |S|>=25-s>=the claimed N. For k<=16 the universal |S|>=20 already proves the lower bound.

## Explicit attaining configurations

Set s=min(5,max(0,floor((26-k)/2))). For each integer x in {13-s,...,12}, choose the four actual physical sites x, x+5, x+10, x+15 (one light color). For every other residue class i mod5 choose the five sites i,i+5,i+10,i+15,i+20 (one heavy color). This gives exactly 4s+5(5-s)=25-s distinct physical sites.

All positions lie between 0 and 27. Each color's selected sites occupy distinct mod11 columns. For any two light-site residues x,y, the ordinary sum lies between 26-2s and 54 inclusive; because k<=26-2s when s>0, no sum lies in D_k modulo55. Therefore a light/light row loses at most one of its 8 contributions, giving F>=7. A light/heavy row has at least 9 potential contributions and loses at most two, giving F>=7; a heavy/heavy row has at least 10 and loses at most two. This establishes the upper bound with equality. The s=0 case has only five-site heavy colors and F>=8.

## Verification and limitations

The independent exact integer JavaScript verifier evaluates every k=1..55, each d in D_k, all five colors i and eleven missing columns j. Count =55*sum_{k=1}^{55} k=84,700 F evaluations; all pass. It also generates all 5*330 candidate light quadruples at each of the five lower-bound thresholds and exhaustively verifies the maximum compatible family size 4,3,2,1,0. The output preserves all 55 attaining sets and the finite-obstruction witnesses. No floating-point approximation is used in the scientific arithmetic.

Independent mathematical review and native same-anchor Farey phase-reachability verification remain open. These results are not a Task CLAIM, Result/Review admission or P000 revision. The numeric bit Hamming criterion concerns separate channel-bit errors; corruption of an entire two-bit physical activation requires a separate metric.

**Next question:** exact r=8 intervals and the minimum *activation-symbol* distance under whole-activation errors/erasures. Then determine which relative phase sets are reached by actual same-anchor Farey evolutions, preserving signed/height/branch/CRT provenance.
