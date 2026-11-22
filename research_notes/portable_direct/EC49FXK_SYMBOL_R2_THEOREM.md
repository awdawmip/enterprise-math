# EC49FXK — Exact one-whole-activation-erasure optimum across all 55 consecutive relative-phase sets

Date: 2026-11-23 Asia/Shanghai. Frozen scientific pin: **BRC16943**, unchanged. Inherited EC49FXI whole-activation observer reduction and EC49FXJ union-symbol metric (Draft PR #2982, immutable proof `a789c99012d4f46935a0f4c1af0df98959d17828:research_notes/portable_direct/EC49FXJ_SYMBOL_TRANSVERSAL_THEOREM.md`). Earlier EC49FXB (PR #2968, frozen input) gives sharp *bit-distance* lower bounds at r=2 for k<=4.

## Exact statement

In the same P10/one-hole auxiliary Farey–CRT double Boolean observer, keep the complete separately indexed reflection spectra, known reference, and a fixed physical-activation set S subset Z/110. Let D_k={0,1,...,k-1} subset Z/110, with 1<=k<=55. A whole activation returns the two-bit symbol (left,right), and two candidate symbol words differ at t if **at least one** channel differs. For d in D_k, i mod5 and missing column j mod11, the exact symbol distance is

  G_S(d,i,j)=sum_{t in S} ([t%5=i, t%11 != j] OR [(d-t)%5=i, (d-t)%11 != j]).

Require G_S(d,i,j)>=2 for all d,i,j; this tolerates one erased *entire two-bit physical activation* with its location known.

**Theorem (sharp for every k=1..55):**

  N_symbol(D_k;2) = 8,    k=1,2;
                   = 9,    k=3,4;
                   = 10,   5<=k<=46;
                   = 11,   k=47,48;
                   = 12,   k=49,50;
                   = 13,   k=51,52;
                   = 14,   k=53,54;
                   = 15,   k=55.

Equivalently for 5<=k<=55, write s(k)=min(5,max(0,floor((56-k)/2))); then N_symbol(D_k;2)=15-s(k).

**New threshold:** under one whole-activation erasure, the fixed-site optimum stays at 10 across all k=5,...,46, first increasing at k=47. The optimum matches the EC49FXJ unrestricted-transversal case, 15, at k=55. The error metric is the activation **symbol**, not two independently erased channel bits.

## Analytic lower bounds and finite obstruction

For k<=4, pointwise G<=F where F is the inherited channel-bit Hamming difference. Therefore a symbol-distance-2 layout also has bit-distance >=2. EC49FXB gives N_bit(D_k;2)=8 for k=1,2 and 9 for k=3,4, hence those lower bounds carry over without any new exhaustive search.

For k>=5, each mod5 color i occurs as a self-reflection row because d in {0,1,2,3,4} includes d=2i mod5. Let m_i be the number of sites in that color. In a self row, both channel differences are supported only on that color and their union count is at most m_i; G>=2 forces m_i>=2. Call a color **light** if m_i=2 and **heavy** if m_i>=3. If L colors are light, |S|>=2L+3(5-L)=15-L; in particular |S|>=10.

For any light color i, both selected physical sites t must satisfy

  (2t mod 55) not in D_k.                                  (1)

Indeed if d=2t mod55 belongs to D_k, choose missing column j=t mod11; the symbol at t vanishes from the self-reflection row, leaving at most one of its two selected physical sites, contrary to G>=2. Thus each light color's complete candidate list consists of unordered pairs of two **different physical positions** among the at most 2(55-k) positions satisfying color i and (1). The list is enumerated exactly in `lightCandidates(k)`, including the two distinct lifts t and t+55 of a single mod55 residue.

For any two light colors i!=h, the row d mod5=i+h contains support **only in those two colors**. Their pair of site-pairs must obey G>=2 for all d in D_k with d mod5=i+h and all j mod11. The `pairCompatible(k,p,q)` predicate checks precisely this necessary constraint; contributions from any heavy colors are absent from that row. A complete depth-first enumeration chooses zero or one candidate pair per color. It prunes only when the number already chosen plus the unvisited colors cannot beat the attained maximum. Therefore its maximum is a rigorous finite upper bound on the number L of light colors in any feasible layout.

The decisive finite obstruction (individual light-pair candidate counts by colors 0,1,2,3,4 and exact maximum pairwise compatible light colors) is:

| k | Candidate counts | Maximum L |
|---:|---|---:|
| 47 | (1,6,6,1,6) | 4 |
| 49 | (1,1,6,1,1) | 3 |
| 51 | (0,1,1,1,1) | 2 |
| 53 | (0,0,1,0,1) | 1 |
| 55 | (0,0,0,0,0) | 0 |

The small search has at most six choices per color at the largest threshold and checks the actual integer modular constraints; the source exposes all loops and pruning. Increasing k only adds constraints, hence the upper bound on L at thresholds extends monotonically through the adjacent even k. Thus |S|>=15-s(k) at every k>=47. Together with the universal 10-site bound for 5<=k<=46, this proves all claimed lower bounds.

## Attaining configurations (fully explicit)

For k=1,2 use S_8={74,98,99,100,101,102,105,108}. For k=3,4 use S_9={61,62,70,73,76,78,79,85,89}. Both are certified directly by the exact integer verifier over every required d,i,j.

For every k>=5, put s=s(k), choose the **light** base residues x=28-s,...,27, and activate **both** lifts x and x+55. These s residues have distinct mod5 colors. In each other (heavy) color i, activate the three positions i,i+5,i+10. The activation count is exactly 2s+3(5-s)=15-s; positions are distinct in Z/110.

All sums of two light base residues lie between 56-2s and 54. Whenever s>0, the definition of s ensures k<=56-2s; therefore no such sum belongs to D_k. As a result, all self-reflection light rows retain both symbols (d=2x mod55 is excluded). For rows involving two different light colors, deletion of both channels at the same physical location would force d=x+y mod55 in D_k, which is excluded; the remaining number of differing physical symbols is >=2. A light/heavy row has five potential symbol contributions, and the missing column removes at most two from the duplicated light pair and at most one from the three distinct heavy columns, hence G>=2. A heavy/heavy row retains at least four symbols. A self-reflection heavy row retains at least two of the three selected symbols because the heavy columns are distinct modulo11. Thus every required row has G>=2. This proves attainment for k>=5 analytically.

## Integer crosscheck and reproducible evidence

The standalone Node program `EC49FXK_SYMBOL_R2_VERIFY.js` evaluates every 1<=k<=55, d=0,...,k-1, all five colors and eleven absent columns against the explicit optimum sets: **84,700 exact row evaluations**, all PASS. It independently enumerates every possible two-position light candidate at each threshold 47,49,51,53,55, performs exact pairwise compatibility checks and exhaustively computes maximum feasible light-color counts 4,3,2,1,0. Its `EC49FXK_SYMBOL_R2_OUTPUT.json` includes all 55 attaining physical-site lists and each certified minimum row distance. No floating-point proof or optimization solver is used by the saved verifier; the two small k<=4 witnesses were first located numerically but all their required inequalities are checked directly.

The finite obstruction, valid derivation and upper witnesses constitute an **author proof** of the declared auxiliary-model theorem. Scientific status: **AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED**. Native same-anchor Farey reachability, signed/height/branch provenance and P000-native transfer are unaffected and remain unproved here. This record is not a formal Task CLAIM, Result or independent Review.

## Next question

For a whole-activation *unknown error*, solve symbol distance r=3 over proper consecutive D_k. Determine whether a similar light/heavy classification remains sharp, then compare the reachable phase restrictions in genuine same-anchor Farey evolution. Keep physical activation errors, partial-channel errors and channel-bit Hamming errors as distinct metrics.
