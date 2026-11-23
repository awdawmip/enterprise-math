# R284GB — Global seven-pattern stable classification from three star cuts

Date: 2026-11-24 (Asia/Shanghai). Mode: informed portable TASK_RESEARCH. Status: AUTHOR_COMPUTER_ASSISTED_PROOF / EXACT_RATIONAL_DUAL_VERIFIED / NOT_INDEPENDENTLY_REVIEWED. Frozen scientific lineage: R284FM, R284FO, R284FZ, R284GA; no rebasing of scientific inputs.

## Theorem

Use the original four-phase cyclic binary observer with unbounded cross-generation omission residue, at most q omitted writes per physical update, and u=1 bit of read noise. Write x_1,...,x_7 for multiplicities of the seven nonconstant phase columns, x_p nonnegative integers. Suppose q >= 5 and n = sum(x_p) is either 4q+8 or 4q+9. Define *stable-admissible* as satisfying both (i) all six nominal pairwise distance necessities from R284FO and (ii) the six exact all-history stable residual-flow separation cuts from R284FM.

**Global two-heavy theorem (R284GB).** Every stable-admissible histogram contains two different types g,h in {3,5,6} with x_g >= 2q+2 and x_h >= 2q+2. In fact, the six nominal distance constraints and only the three stable-cut constraints for phase pairs (0,1), (0,2), (0,3) already force this property.

**Corollary (unrestricted stable census).** Combining the theorem with the q-independent, necessary-and-sufficient two-heavy classification in R284GA, the *complete unrestricted seven-pattern* stable-admissible census, for every integer q>=5, is exactly **7** histograms at width 4q+8 and **66** at width 4q+9. Of the latter, 18 use only types {3,5,6} and 48 also use at least one of {1,2,4,7}. The complete census is not a count of valid non-atomic write protocols.

## Proof of the forcing lemma

Normalize c_0=0 and let the phase-bit pattern of type p be (0, p&1, (p>>1)&1, (p>>2)&1). For phase pair (i,j), let D_ij be the types with unequal bits. The six nominal necessities are

    sum_{p in D_ij} x_p >= 2q+c_ij,

with c_ij=5 for cyclic adjacent phase pairs and c_ij=3 for opposite phase pairs.

For each pair (i,j), the R284FM residual-incidence graph has four source and four target vertices, each with omission capacity q. For every nonempty vertex subset U, let M(U) be the types whose source and target incidence endpoints both lie in U. A necessary and sufficient *stable-pair separation* is that some U satisfies

    sum_{p in M(U)} x_p >= q |U| + 3.

Enumerate all 255 nonempty eight-vertex subsets, group by the induced nonempty type mask, and keep its minimum vertex count m. This is logically equivalent: at fixed type mask, the smallest m produces the weakest threshold. The star pairs (01),(02),(03) have respectively 7, 9, and 7 distinct nonempty masks. Their explicit masks and m are reconstructed, not hardcoded, by the companion checker from the actual last-update incidences.

It suffices to exclude width 4q+9 with fewer than two heavy types. Indeed any width 4q+8 counterexample could be padded with one additional type-1 column. All nominal and stable-cut left-hand sides are nondecreasing, the omission budget q is unchanged, and none of x_3,x_5,x_6 changes. The padded histogram would be a width 4q+9 counterexample.

If there are fewer than two heavy types, choose g in {3,5,6} such that the other two types satisfy x_h<=2q+1 (integer multiplicities). There are three choices of g. For each star pair choose one valid mask witness (M,m). There are 7*9*7*3 = **1323** exhaustive disjunctive branches. In every branch put y=(x_1,...,x_7,q) and impose exactly 21 linear inequalities A y <= b:

- all six nominal necessities;
- the three selected star-mask stable necessities;
- the two non-heavy caps x_h-2q<=1;
- seven nonnegativity inequalities -x_p<=0;
- -q<=-5;
- the two inequalities representing sum(x_p)-4q=9.

For **each of the 1323 branches**, the accompanying computation constructs nonnegative rational multipliers lambda for all 21 rows and checks, using only exact Python Fraction arithmetic, that

    sum_{r=1}^{21} lambda_r A_{r,j}=0  for every j=1,...,8,
    sum_{r=1}^{21} lambda_r b_r=-1.

Hence a hypothetical feasible y would imply 0 <= -1. This is a finite exact Farkas-certificate proof and does not rely on the truth of any floating-point solver declaration. Each floating-point LP call is used solely to *propose* candidate multipliers; the checker independently reconstructs rational multipliers and verifies every exact identity and nonnegativity. If a proposed certificate fails rational reconstruction, the program raises an error instead of reporting success.

The executed verifier found 1323/1323 valid rational contradictions. The largest denominator occurring in its reconstructed multipliers was 34. All q>=5 are covered simultaneously as one real variable q in the inequalities, rather than being sampled one by one. The source code also regenerates the star masks, checks their completeness, enumerates all branch combinations and checks the bound normalization. Therefore no two-heavy counterexample exists in the declared model. Applying the prior R284GA within-sector converse yields the corollary.

## Reproduction and independent verification

Source: `research_notes/portable_direct/R284GB_star_cut_dual_checker.py`. Execution: `python R284GB_star_cut_dual_checker.py` with Python 3, numpy and scipy. The program regenerates the 1323 dual certificates and checks each over exact rationals; SciPy is not in the trusted verification step. Local execution on 2026-11-24 returned:

    PASS: star cuts alone + six nominal distances force two-heavy
    q>=5, n=4q+9: 1323/1323 exact rational Farkas contradictions
    maximum exact dual coefficient denominator: 34
    n=4q+8 follows by padding type-1 count to n=4q+9
    Combining R284GA: full stable census 7 and 66 for all q>=5

The local checker used the same source algorithm and rational identities as the published source. Any independent audit should first verify the correspondence of the R284FM eight-vertex physical incidence model to the cut inequalities; this proof assumes that established frozen lemma. No formal native Result or independent mathematical Review is inferred from a successful research computation.

## Meaning and remaining problem

**Solved:** full global stability-only census in the unrestricted seven-pattern space for every q>=5, removing R284GA's two-heavy premise. The new argument needs only one star of three stable cuts, not all six, to force the premise.

**Not solved:** universal first-publish-edge elimination of every family except R284FW's F0-F10, nor universal prefix safety for those remaining families. The existing finite q=2,...,14 global sharp results remain at their documented scopes; this stability theorem alone does not establish n_min(q,1)=4q+10 for all q.

**Next discriminating unit:** derive a q-independent exact first-edge prefix predicate for the 7/66 affine families using the R284FT flow representation. Enumerate the fixed offsets rather than all 4q+k columns. Prove or refute the claimed universal 1/10 first-edge survivors; if proved, combine R284FW's second-edge obstruction to obtain the full q>=5 sharp capacity lower bound, with q=2,...,4 handled by prior exact certificates. Preserve frozen source pins and original authorship.

## Provenance

- R284FM exact all-history cut: enterprise-math@1d1c5dd412719c7aaf016187b6493b77253cd9f9, `research_notes/portable_direct/R284FM_NOISY_OBSERVER_FLOW_CUT_AND_ADDITIVE_LOWER_BOUND_20261123.md`.
- R284GA conditional converse: enterprise-math@0c3284aec3e378b384beb43f232018d7978455da, `research_notes/portable_direct/R284GA_TWO_HEAVY_UNIFORM_STABLE_CONVERSE_20261124.md`.
- R284FW parameterized second-edge obstruction: enterprise-math@bfbeefc839da0fb1b9d6d87db10c531b1f0f5cbc, `research_notes/portable_direct/R284FW_ALL_Q_PARAMETRIC_FIRST_EDGE_SURVIVOR_SECOND_EDGE_OBSTRUCTION_20261123.md`.
- Separate BRC/P000/ACTIVE worldview provenance is retained and untouched. The four-phase binary observer is an auxiliary typed mathematical model, not an assertion of a native six-dimensional physical theorem.
