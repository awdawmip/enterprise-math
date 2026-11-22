# EC49FXL — Sharp single unknown whole-activation-error optimum for all consecutive relative-phase sets

**Date:** 2026-11-23 (Asia/Shanghai). **Frozen scientific input:** BRC16943, unchanged. **Status:** AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.

**Predecessor:** EC49FXK, immutable commit 168eca0a89415c3b2add265ba8a37727012b3b70, research_notes/portable_direct/EC49FXK_SYMBOL_R2_THEOREM.md. This note uses its 110-period P10/one-missing-column Farey–CRT *auxiliary* two-channel observer and strengthens the requested activation-symbol distance from 2 (one known erased activation) to 3 (one unknown corrupted activation). The reference index and full indexed spectra are retained.

## Problem and exact theorem

For each k=1,...,55 let D_k={0,1,...,k-1} subset of Z/110 be the allowed left-minus-right relative phase. A physical observation set S consists of distinct t in Z/110. At each t the two Boolean readings form **one symbol**. For every allowed phase d, CRT color i in Z/5 and missing column j in Z/11, the symbol distance between the two same-spectrum candidates is

\[
G_S(d,i,j)=\sum_{t\in S}\mathbf1\big[
(t\bmod5=i\ \&\ t\bmod11\ne j)
\ \lor\
((d-t)\bmod5=i\ \&\ (d-t)\bmod11\ne j)
\big].
\]

The strict requirement is G_S(d,i,j)>=3 **for every** d in D_k, i=0,...,4 and j=0,...,10. This suffices to correct one arbitrary erroneous whole activation, including simultaneous corruption of its two channel bits.

**Theorem (sharp for every k=1,...,55):**

\[
\boxed{
N_{\mathrm{symbol}}(D_k;3)=
\begin{cases}
11,&1\le k\le2,\\
13,&3\le k\le4,\\
15,&5\le k\le45,\\
k-30,&46\le k\le49,\\
20,&50\le k\le55.
\end{cases}}
\]

The cost is monotone with k. Most notably, the optimum remains 15 for 41 consecutive phase-set sizes k=5,...,45, then rises **once per newly admitted phase** at k=46,47,48,49,50. All calculations use exact integers.

## Proof: lower bound

Let m_i denote the number of activated physical sites t with t mod5=i, so |S|=sum_i m_i.

**A. Self-color rows.** A phase d with d mod5=2i gives a row whose two Boolean differences are supported entirely in color i. Thus G_S<=m_i. For k>=5 all five self-color phase residues occur in D_k, forcing every m_i>=3 and |S|>=15.

**B. Distinct-color rows.** When d mod5=i+h with i!=h, the two channel contributions live in two disjoint color classes i and h. For any chosen physical site in these colors, at least one missing-column value j deletes its contribution from the relevant channel. Hence min_j G_S(d,i,j) <= m_i+m_h-1, so G>=3 forces m_i+m_h>=4.

At k=1 (d=0), the self-color is 0 and the disjoint pairs are {1,4}, {2,3}. Therefore m_0>=3, m_1+m_4>=4 and m_2+m_3>=4; summing gives |S|>=11. The same bound holds at k=2 by inclusion.

For k>=3, the self-color rows d=0,1,2 impose m_0,m_3,m_1>=3. The d=1 distinct-color pair {2,4} imposes m_2+m_4>=4. These five disjoint pieces imply |S|>=13 for k=3,4.

**C. Large-k sharpening.** For k>=5, if m_i=3 then every chosen t in color i must obey

\[
(2t\bmod55)\notin D_k.
\]

Otherwise take d congruent to 2t modulo55 within D_k and choose j=t mod11. In the associated self-color row the physical activation t vanishes in both channels; the remaining at most two activations give G<=2. Note that t and t+55 yield the same residue modulo55, while there are only **two distinct physical lifts** of each such residue. Therefore a color with m_i=3 needs at least two distinct safe residues x modulo55 with x mod5=i and (2x mod55)>=k.

For k=45,...,50 the safe-residue counts by color i=0,1,2,3,4 are respectively:

| k | counts by color | number of colors allowing m_i=3 |
|---|---|---:|
| 45 | 2,2,2,2,2 | 5 |
| 46 | 1,2,2,2,2 | 4 |
| 47 | 1,2,2,1,2 | 3 |
| 48 | 1,1,2,1,2 | 2 |
| 49 | 1,1,2,1,1 | 1 |
| 50 | 1,1,1,1,1 | 0 |

For k>50 counts can only decrease. Thus at least 5-L colors must have m_i>=4, with L=max(0,50-k) for 45<=k<=55. This yields |S|>=3L+4(5-L)=20-L. In the range k=46,...,49 this is k-30; from k=50 onward it is 20. All lower bounds are now proved without a numerical optimizer.

## Proof: attaining constructions

**Small k.** For k=1,2 activate the following 11 physical sites:

\[
S_2=\{4,5,13,19,35,40,43,44,46,47,53\}.
\]

For k=3,4 activate these 13 physical sites:

\[
S_4=\{3,5,7,10,14,15,21,23,24,31,33,36,54\}.
\]

The standalone exact integer program exhaustively checks the required 2*5*11=110 and 4*5*11=220 row constraints respectively. It records the minimum over missing columns for each d,i, permitting direct independent reproduction of these finite witnesses. Both have minimum 3. Thus the first two ranges attain the proved lower bounds.

**All k>=5: a uniform closed-form site construction.** Index colors i=0,...,4 and set

| i | x_i | y_i | cutoff c_i |
|---|---:|---:|---:|
| 0 | 25 | 50 | 45 |
| 1 | 26 | 51 | 47 |
| 2 | 27 | 52 | 49 |
| 3 | 23 | 53 | 46 |
| 4 | 24 | 54 | 48 |

For each color i select **light sites** L_i={x_i,x_i+55,y_i} when k<=c_i; otherwise select **heavy sites** H_i={i,i+5,i+10,i+15}. These sites are distinct in Z/110, and site sets for different colors are disjoint. Exactly five light colors occur for k=5,...,45; four, three, two and one for k=46,47,48,49; and zero for k>=50. Therefore the total activation count equals the claimed upper bound.

To verify the constraint for all d,i,j analytically:

1. In a self-color row, each light site's potential full-symbol erasure requires d≡2t (mod55). For k<=c_i both 2x_i mod55 and 2y_i mod55 are at least k, so none of the three sites vanishes and G=3. For a heavy color all four sites have distinct mod11 columns; for any missing column at most one physical site vanishes, giving G>=3.
2. In a distinct-color row with two heavy colors, each has four distinct mod11 columns, and at most one site is removed per color, so G>=6. For a light/heavy pair, missing a column can delete at most two of the three light sites and at most one heavy site, giving G>=3+4-2-1=4.
3. For two light colors i!=h, both color groups contain three sites and exactly one duplicated mod11 column (x_i or x_h). Each would lose at most two sites. Both duplicated pairs can be deleted in the same missing-column row only if d≡x_i+x_h (mod55), since the left channel is color i and the right channel is color h. For all pairs of colors simultaneously light at k, direct inspection of the five explicit c_i and x_i values gives k<=min(c_i,c_h)<x_i+x_h<55. Therefore the simultaneous two-plus-two deletion never occurs in D_k. At most three sites are removed from six; hence G>=3.

This proves every upper bound analytically and completes the theorem.

## Exact reproducible evidence and scope

The dependency-free JavaScript program EC49FXL_SYMBOL_R3_INTERVAL_VERIFY.js runs an integer evaluation for every k=1,...,55, every allowed d in D_k, all five CRT colors and all eleven missing columns. Number of independently evaluated constraints:

\[
55\sum_{k=1}^{55}k=55(1540)=84{,}700.
\]

All 84,700 inequalities pass with minimum observed symbol distance exactly 3; the output includes every attaining physical-site set and the two small-k finite-witness row matrices. The program also checks the safe-color counts and light-pair exclusion needed in the analytic upper/lower arguments. A separate local SciPy/HiGHS integer-programming crosscheck for all 55 k values found the identical optimal profile; the proof above does not rely on that floating-point solver.

**Claim boundary.** This is an internal sharp theorem for the declared frozen **auxiliary** Farey–CRT observer, not a proof of actual same-anchor Farey reachable phases, not a P000-native six-dimensional dynamics result, and not an independently accepted project Result. Signed/height/branch provenance and the original anchored trajectory remain separate scientific obligations. No existing theorem or frozen scientific pin is altered.

## Next meaningful question

Determine the exact physically reachable set D (and correlated relative-phase/source restrictions) under genuine same-anchor Farey evolution rather than a free consecutive interval. For whole-activation symbol distance r>=4, test whether a three/four/five-site color occupancy hierarchy yields an analogous sharp threshold law, retaining whole-activation errors separately from individual channel-bit errors.
