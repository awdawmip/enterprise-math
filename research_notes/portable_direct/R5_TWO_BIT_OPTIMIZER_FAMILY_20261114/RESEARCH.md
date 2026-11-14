# R5 exact two-bit optimizer family and interaction at high center budgets

Date: 2026-11-14. Frozen scientific input: 435e77af0d180eac32bd1f9c4c464bc4010b7551. Status: AUTHOR_SIDE_EXACT_PROOF_AND_RECALCULATION; independent review NOT_REVIEWED. This is a derived one-dimensional indexed observer within the Enterprise Math research program, not an asserted native X6 spatial dynamics theorem.

## Model and sources

Reconstruct the 954 strictly ordered integer events and their 28 original length-three gaps from the immutable frozen input, using the generator in Enterprise Math Draft PR #2379, research_notes/brc_r5_exact_cost_spectrum_20261114/VERIFY_R5_COST_SPECTRA.py, whose original scientific source is pinned above. Gap and event labels are zero-based. Given any closure set B within C={0,...,27}, replace each selected length-three gap by length two and keep all event labels. Candidate centers must be selected at event indices. Opt_B(K) is the family of all exactly K indexed-center subsets covering every event to distance at most 2 and attaining the least sum of nearest-center distances J_B(K). N_B(K)=|Opt_B(K)|.

Earlier source inputs:
- Full-budget cost-invariance theorem J_B(K)=J_empty(K) for every B when 214<=K<=954: commit 136928dfd4d66b8fefce72a7067fdfed834f3e9f, Draft PR #2373.
- Full optimizer-family invariance at K=292 and 315<=K<=954: commit 68ac5b5507fbef23378658df5beb6ca1c7ab48ba, Draft PR #2379.
- 11 globally optimizer-inert cuts and local interval factorization: commit 8f833128e18fa79ad70b6c8e7b7059a16756e085, same Draft PR.

The present work is an independent scientific materialization. No formal Task claim, Result acceptance or reviewer authority is asserted.

## New exact theorem: all high-budget optimizer sets factor through TWO bits

Let H=C\{15,17}. For every B subset C, set T=B∩{15,17}. Then for EVERY integer budget 292<=K<=954,

  Opt_B(K) = Opt_T(K).

For K=292 and 315<=K<=954 this family is independent even of the two remaining bits. Thus for each K in 293..314, the full optimizer-family readout of all 268,435,456 patterns has at most four exact values, indexed by (b15,b17) in {0,1}^2. Every two-bit fiber contains 2^26=67,108,864 closure patterns. This sharpens the preceding 17-bit quotient at these budgets.

### Exact proof

(1) Single-gap closure preserves every previously feasible selected-center INDEX SET and its sum-of-distances cost: with an unclosed gap of length three, a cross-gap candidate is at least three away. A previously covered event already has a same-side center within distance at most two. Closing the gap makes any cross-gap candidate no nearer than two, so it cannot lower the previous nearest-center cost; feasibility remains. Iterating shows previously feasible labeled center sets survive with unchanged cost.

(2) The earlier full-budget cost theorem gives J_A(K)=J_A'(K) for all A⊆A' and K>=214. Combined with (1), Opt_A(K) ⊆ Opt_A'(K) for all such budgets.

(3) For each of four sets T ∈ {empty,{15},{17},{15,17}}, exact integer chosen-center path DP computes the full minimizing-center counts for T and H∪T at each K=292,293,...,315. All 4×24 endpoint pairs have identical optimum costs and identical counts; the accompanying verification program constructs coordinates independently from the frozen integer/rational generator, checks the equality at each budget, and compares three intermediate closure backgrounds. The complete four-state counts are reproducible from EXACT_TWO_BIT_SPECTRA.json; full arbitrary-precision integers are stored as decimal strings. The DP has one path for each increasing center-index subset. A start edge accounts for events left of the first center, each internal edge for intervening events (nearest of its two neighboring centers), and the terminal suffix for the remaining events. The recurrence carries (minimum cost, count of tied minimizers), and exactly rejects edge/suffix distances greater than two. The 108 seeded small-coordinate inputs are independently checked by enumeration of every center subset.

(4) For any arbitrary B, T⊆B⊆H∪T. By (2), Opt_T(K)⊆Opt_B(K)⊆Opt_{H∪T}(K). Since the two finite endpoint sets have the same proven cardinality, both inclusions are equalities for 292<=K<=315. The previous universal family-invariance theorem supplies K>=315. This proves the statement for every original closure mask, rather than statistically extrapolating from sampled masks.

## Exact two-bit count polynomial and nonadditive interaction

Write a=1 if gap 15 is closed and b=1 if gap 17 is closed. For every B and K in [292,315], the counts obey the exact multilinear interpolation

  N_B(K)=N00(K)+a*A15(K)+b*A17(K)+a*b*Gamma(K),

with the 24 exact rows in EXACT_TWO_BIT_SPECTRA.json. Specifically A15=N10-N00; A17=N01-N00; Gamma=N11-N10-N01+N00. The values depend on K alone and not on any of the other 26 gap bits. The certificate establishes:

- A15(K)>0 and A17(K)>0 precisely at K=293,...,314 within 292..315;
- Gamma(K)>0 precisely at K=294,...,313, and Gamma=0 at K=292,293,314,315;
- at K=293 the minimum cost is 741, N00=12606779601463240519046922240, A15=A17=495879658013739785241231360, Gamma=0;
- at K=294 the minimum cost is 738, and Gamma=991759316027479570482462720;
- at K=314 Gamma returns to zero, while both single-cut coefficients remain positive;
- at K=315 all three coefficients are zero.

The strictly positive mixed coefficient is an EXACT joint-optimizer multiplicity interaction: combinations newly optimal due to both cuts are not captured by adding the two single-cut count changes. This is computed for the complete 28-bit mask population by the theorem. It does not reclassify full native provenance.

## Reconfiguration corollary

Define rho_B(K)=min{|S\T|: S in Opt_B(K), T in Opt_B(K+1)} for feasible consecutive budgets. Since both families at K and K+1 depend only on B∩{15,17} whenever 292<=K<=953,

  rho_B(K)=rho_{B∩{15,17}}(K), for EVERY 292<=K<=953.

Hence any exact optimizer-family-based edit, nesting, overlap or symmetric-difference statistic at these transitions may be classified using just four two-bit cases, while lower transitions K<=291 still require their own scope-specific analysis. The present calculation proves this reduction and leaves exact rho numerical values for later work.

## Execution and reproducibility

The standalone Python 3 verifier supplied here was executed locally on the pinned generator. It used integer arithmetic and Fraction for exact input reconstruction, and arbitrary-precision Python integers for all optimizer counts. It computed 20 endpoint/intermediate exact center spectra through K=315, checked all four two-bit endpoint contexts across every K=292..315, inspected two single-gap activations and their 20 strict mixed-interaction budgets, and performed 108 seeded exhaustive small-input checks. Status: PASS_EXACT_R5_TWO_GAP_CONTEXT_EXPERIMENT.

The recorded full-size checks use exact DP plus the inclusion proof; 268,435,456 patterns are covered logically, not enumerated individually. Independent mathematical review is still NOT_REVIEWED. The local execution validates the author's script; a separately provisioned checkout should rerun the exact posted bytes for further reproduction.

Source record: prior PR #2379 at branch head 8f833128e18fa79ad70b6c8e7b7059a16756e085, plus the earlier immutable frozen pin. Prior published witnesses and all existing results are preserved unchanged.

## Specific next research unit

Compute exact minimum deletion/reconfiguration distance rho_T(K) for the four T subsets of {15,17}, K=292..314, using pair-coupled optimal path DP with source-labeled centers; locate the first strict edit difference and preserve exact witness pairs. For K<=291 retain the effective 17-bit quotient proven previously. The separate 2,520-byte certificate / 28-coordinate / 8,192-prefix-query native benchmark remains open and requires its own correctly typed evidence.
