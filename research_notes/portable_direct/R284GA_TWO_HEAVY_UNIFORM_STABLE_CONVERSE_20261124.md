# R284GA — Uniform two-heavy converse for seven-pattern stable residual cuts

Date: 2026-11-24 (Asia/Shanghai). Research mode: informed portable TASK_RESEARCH. Status: AUTHOR_ANALYTIC_REDUCTION / EXACT_FINITE_CENSUS / NOT_INDEPENDENTLY_REVIEWED. This is a scoped result within the frozen R284CO–R284FM–R284FZ four-phase binary observer model, not a P000/ACTIVE worldview change or a native X6 theorem.

## Proposition

Let q be any integer ≥5, u=1, k∈{8,9}, and n=4q+k. Normalize the four cyclic binary phase words by c0=0, and write x=(x1,...,x7) for counts of the seven nonconstant phase-(1,2,3) column patterns p=1,...,7. A histogram is *stable-admissible* when it satisfies the six nominal pairwise distance necessities from R284FO and the six exact all-history stable-state residual-flow separation cuts from R284FM. These are necessary conditions at completed phases and make no assertion about intermediate non-atomic write prefixes.

Define the **two-heavy sector** to consist of histograms for which at least two different types among {3,5,6} have multiplicity ≥2q+2. Such a histogram has a unique heavy pair G (the third cannot also be heavy because n<3(2q+2)). Put

    x_p = 2q · 1[p∈G] + z_p,       z_p≥0,
    z_g≥2 for g∈G,                Σ_{p=1}^7 z_p = k.

**Theorem R284GA.** Within the two-heavy sector, stable-admissibility is exactly a *q-independent* finite system on (G,z). For every q≥5 there are exactly 7 such histograms for n=4q+8 and exactly 66 for n=4q+9, with counts by G:

| n | {3,5} | {3,6} | {5,6} | total | face {3,5,6} | mixed other types |
|---|---:|---:|---:|---:|---:|---:|
| 4q+8 | 3 | 1 | 3 | 7 | 7 | 0 |
| 4q+9 | 28 | 10 | 28 | 66 | 18 | 48 |

These histograms are **exactly** the affine-lifted families of R284FZ, rather than merely a subset of them. This is an all-q converse **conditioned on being in the two-heavy sector**. The separate claim that *every* stable-admissible seven-pattern histogram lies in that sector is the remaining global classification question.

## Proof of q-independent reduction

For pair (i,j), let D_ij be the nonconstant types where phase i and j differ. In pair order (01),(02),(03),(12),(13),(23), they are:

    D_01={1,3,5,7}, D_02={2,3,6,7}, D_03={4,5,6,7},
    D_12={1,2,5,6}, D_13={2,3,4,5}, D_23={1,3,4,6}.

(The last two sets are interchangeable if pairs are reordered; the verifier constructs them from the actual phase bits rather than trusting this display.) Every D_ij meets every two-element subset G⊂{3,5,6}. Let h=|D_ij∩G|≥1. The existing nominal distance threshold is Σ_{p∈D}x_p≥2q+c, with c=5 for cyclic neighbors and c=3 for opposites. If h=1, this is exactly Σ_{p∈D}z_p≥c. If h=2, it holds automatically since Σ_{p∈D}x_p≥4q+4>2q+5. Therefore all nominal necessities become independent of q.

Now form the exact eight-vertex bipartite residual-incidence graph of R284FM: four source last-write groups and four target last-write groups, each with omission capacity q. For any nonempty vertex subset U, let M_U be the types whose two incidence endpoints belong to U, let m=|U|, and let h=|M_U∩G|. Radius-one stable read balls are disjoint for a pair precisely when some U satisfies

    Σ_{p∈M_U} x_p ≥ q m + 3.

It suffices to use the minimum vertex set size for each induced type mask; among nonempty masks these minima are 2, 3 or 4, as reconstructed by the verifier from the actual last-update groups. A mask with h=0 has total weight at most k−4≤5, so cannot meet q m+3 for q≥5 and m≥2. With h=1 and m≥3, its weight is at most 2q+(k−2)≤2q+7<3q+3≤qm+3 for q≥5. If h=1 and m=2, the inequality reduces to Σ_{p∈M_U}z_p≥3. If h=2, the weight is at least 4q+4 and m≤4, hence it always satisfies Σx_p≥qm+3. Consequently the exact stable cut test becomes the following finite, q-independent predicate:

    For every pair (i,j), there is an induced mask M with either
    (a) |M∩G|=2; or
    (b) |M∩G|=1, minimum vertex count m=2, and Σ_{p∈M}z_p≥3.

Together with the nominal inequalities above, this is necessary and sufficient for stable-admissibility *in the declared sector*, for all q≥5. Each omission source and target remains separately represented in this proof; it is not replaced by an aggregate Hamming budget.

## Exact exhaustive offset census

For each G∈{{3,5},{3,6},{5,6}}, set z_g=2+w_g at both heavy types and z_p=w_p otherwise. Then w is a weak seven-part composition of k−4, so the complete finite candidate universe has 3·C(k+2,6) members: 630 for k=8 and 1386 for k=9, total 2016. The companion standard-library integer checker enumerates each exactly once, reconstructs all six phase pair sets, all eight-vertex cut masks, and implements the finite predicate without q. It finds exactly the counts in the theorem. For each of the 2016 offset cases, direct original-q tests at q∈{5,6,7,11,64,1000} agree with the symbolic predicate: 12,096 exact cross-checks; no discrepancies. The theorem's universal q statement uses the analytic cancellation above, not extrapolation of those six parameter samples.

The two heavy pairs are uniquely determined, and the map x↦(G,z) is injective. R284FZ previously constructed all 7/66 lifted families with heavy pair G and proved their stable-admissibility. The present upper count within the whole two-heavy sector is also 7/66, yielding exact equality to those prior lifts.

## Scientific boundary and next question

**What is solved:** q-uniform necessary-and-sufficient classification for every seven-pattern histogram in which two of types 3,5,6 have multiplicity at least 2q+2.

**What is open:** show, or disprove by an explicit histogram at some q≥5, that the six nominal and six stable-cut constraints force this heavy-pair premise even for unrestricted seven-pattern histograms. If established, the complete q-uniform 7/66 stable census would follow; next classify the first-edge survivors (F0–F10), then combine with R284FW's all-q second-edge obstruction. Thus the full conjecture n_min(q,1)=4q+10 for all q≥2 is not yet proved.

Verification: the complete companion source is `research_notes/portable_direct/R284GA_two_heavy_uniform_converse.py`. It checks q-independent predicates and exact flow-cut equivalent eight-vertex masks. No independent mathematical review, formal Result, or shared CLAIM is asserted.

Frozen-source provenance: R284FM all-history exact cuts `awdawmip/enterprise-math@1d1c5dd412719c7aaf016187b6493b77253cd9f9:research_notes/portable_direct/R284FM_NOISY_OBSERVER_FLOW_CUT_AND_ADDITIVE_LOWER_BOUND_20261123.md`; R284FZ lifted families `awdawmip/enterprise-math@1df6e10ca6246eb6d6c9e776fe7ec46f7a96acfc:research_notes/portable_direct/R284FZ_UNIFORM_SIXTY_SIX_STABLE_LIFT_20261123.md`; R284FW obstruction `awdawmip/enterprise-math@bfbeefc839da0fb1b9d6d87db10c531b1f0f5cbc:research_notes/portable_direct/R284FW_ALL_Q_PARAMETRIC_FIRST_EDGE_SURVIVOR_SECOND_EDGE_OBSTRUCTION_20261123.md`. No scientific pin was rebased.
