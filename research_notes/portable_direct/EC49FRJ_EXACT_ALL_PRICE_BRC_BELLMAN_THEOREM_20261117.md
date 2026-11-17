# EC49FRJ — Exact unrestricted native BRC Bellman optimum for every real price x ≥ 1

Date 2026-11-17. Frozen scientific input pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Scientific parent: EC49FRI [PR #2621](https://github.com/awdawmip/enterprise-math/pull/2621) @ 9fb350ce22db16f25c1cc5b9b86f022d5dd4cd83. Status AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Exact finite original BRC model

Class 16943 has 310 original configurations, 141 **full named** distinct root-state profiles i with positive integral multiplicities m_i summing to 310, 144 terminal and 84 root named physical observations, total 228. Response partitions: 209, only used for same-cost internal computational deduplication; all 228 distinct physical first-action names are retained in the certificate and theorem.

Let x≥1 be real root observation cost / positive terminal cost t; let λ∈[0,1] and p_i(λ)=(1−λ)/141 + λ m_i/310. Any complete identifying adaptive physical tree Q has nonnegative integer per-profile numbers r_i and d_i of root and terminal observations. Write V(x,λ)=inf_Q Σ_i p_i(λ)(r_i x+d_i). All arithmetic and full profile observation sequences are original native BRC; no source, port, or named-action collapse is used as an external semantic equivalence.

Five **fixed complete feasible named physical trees** A,B,C,D,E have exact integer aggregate (Σr_i, Σd_i, Σm_i r_i, Σm_i d_i):

| Fixed tree | Full 4-integer aggregate |
|---|---|
| A | (6,290,6,751) |
| B | (5,293,5,704) |
| C | (5,295,5,685) |
| D | (4,296,4,707) |
| E | (4,298,4,688) |

For any such tree Z=(uR,uT,mR,mT), define
Z(x,λ)=(1−λ)(uR x+uT)/141 + λ(mR x+mT)/310.

## Global theorem (all real prices, not a sample bound)

**For all real x≥1 and all real λ∈[0,1], V(x,λ)=min(A,B,C,D,E).**

More explicitly: EC49FRI has already proved V=min(A,B,C) on [1,3]×[0,1]. Here the stronger new theorem establishes **V=min(D,E) for every real x≥3 and every real λ∈[0,1]**. Put β=620/3299. The exact phase identity is E−D=(620−3299λ)/43710, independent of price. D wins for 0≤λ≤β, E wins for β≤λ≤1; both tie on β.

At every real x≥3, **the entire set of optimal first original physical observations** is:

| prior λ | every tied optimal physical first query |
|---|---|
| λ=0 | {32,34,140,142} |
| 0<λ<β | {140,142} |
| λ=β | {16,23,140,142} |
| β<λ<1 | {16,23} |
| λ=1 | {16,23,59,88} |

## Proof I: finite six-anchor interpolation proves [3,20]×[0,1]

Execute exact unrestricted Bellman over all 141 original named states and 228 physical first observations; independently repeat using a second implementation of weighted-subset dynamic programming. Eight anchor evaluations were made in total, the first six being:

| x | λ | exact global V | all tied optimal first queries |
|---:|---|---|---|
| 3 | 0 | 308/141 | 32,34,140,142 |
| 3 | 620/3299 | 7290/3299 | 16,23,140,142 |
| 3 | 1 | 70/31 | 16,23,59,88 |
| 20 | 0 | 8/3 | 32,34,140,142 |
| 20 | 620/3299 | 8718/3299 | 16,23,140,142 |
| 20 | 1 | 384/155 | 16,23,59,88 |

Every Q's fixed-prior cost is affine in x. At λ=0,β,1 its gap from the same fixed feasible D (at 0/β) or E (at β/1) is nonnegative at both prices 3 and 20 by exact unrestricted endpoint optimality, and therefore throughout the real price interval. For each fixed real x in [3,20], every Q's cost is affine in λ; its gap from D on [0,β], or E on [β,1], is nonnegative at both prior endpoints, hence throughout. Because D and E are themselves feasible, this proves **unrestricted V=min(D,E) for every real x∈[3,20] and λ∈[0,1]**. No finite-grid approximation is used to substitute for real-parameter inference.

For first-action classification within the rectangle, any optimal Q at an interior point with nonnegative affine endpoint gaps must attain equality at both endpoints. Intersect the **complete** native physical first-action tie sets at both endpoints to obtain the listed action IDs. Their inclusion is established by replayed, fixed, complete original trees. At λ=0 fixed first-action trees 32/34 and 140/142 share the optimal uniform aggregate (4,296); at λ=1 trees 59/88 and 16/23 share the optimal multiplicity aggregate (4,688). At β trees 16/23 and 140/142 tie.

## Proof II: two exact high-price anchors force a universal root-observation lower bound

Define four nonnegative integer observation totals for any Q:

Ru=Σ_i r_i, Tu=Σ_i d_i, Rm=Σ_i m_i r_i, Tm=Σ_i m_i d_i.

Prune every non-splitting query along any branch; any such reduced identifying tree has at most 140 splitting observations on each root-to-profile path. Consequently Tu≤141·140=19740 and Tm≤310·140=43400. Any unpruned identifying tree has no smaller root-count totals than its pruning.

At **the single finite integer root price X=100000**, repeat unrestricted native exact Bellman and independent weighted-subset integer DP for each extreme prior:

| x | λ | exact global V | all tied optimal first queries |
|---|---|---|---|
| 100000 | 0 | 400296/141 | 32,34,140,142 |
| 100000 | 1 | 400688/310 | 16,23,59,88 |

Each full source-native JSON certificate gives every named first query cost and all complete optimal trees; its exact integer optimal numerator and physical ties were reproduced by an independent exact subset DP. Original frozen data, two implementations, complete certificates, verification logs and tree-replay results are included in the evidence archive.

If a reduced identifying Q had **Ru≤3**, then at X its unweighted integer numerator would obey Ru·X+Tu ≤ 3·100000+19740 =319740 <400296, contradicting the unrestricted optimum. Hence every feasible Q has **Ru≥4**. Likewise if **Rm≤3**, its multiplicity-weighted numerator ≤3·100000+43400=343400 <400688; contradiction. Hence every feasible Q has **Rm≥4**. Both bounds follow from two finite exact global certificates plus a finite depth bound, without extrapolation.

Therefore every feasible Q has price slope

∂_x C_Q(x,λ)=(1−λ)Ru/141 + λ Rm/310 ≥ 4(1−λ)/141 +4λ/310.

Both fixed D and E have exactly Ru=Rm=4, so both attain the universal minimal slope under every λ. For any λ, at x=20 the already proven rectangle theorem supplies a fixed winning D or E, call it L. For any x≥20 and any Q, the affine cost difference is

C_Q(x,λ)−L(x,λ) =
[C_Q(20,λ)−L(20,λ)] +
(x−20)[∂_x C_Q−∂_x L] ≥0.

Thus **the same fixed L remains unrestricted globally optimal for every real x≥20**, giving V=min(D,E) on the entire unbounded half-strip x≥3. Combine with EC49FRI [1,3] to prove the global five-tree theorem for **all real x≥1**.

For first-action classification at x>20, each competitor gap is nondecreasing in x, so no first action absent at x=20 can enter. Every action included at x=20 has a replayed complete original tree with the corresponding minimal root-mass slope four under the applicable prior; therefore it remains tied optimal. This proves the exact five-case first-action classification for all x≥3.

## Evidence and scope

Full self-contained conversation-delivered archive **EC49FRJ_EXACT_ALL_PRICES_COMPLETE_EVIDENCE_20261117.tar.xz**. Archive SHA256 **d7905b2d50441b619300d14d87a2e326272fae7103b4e6528d6653d66778b479**. It was reopened and all **30 manifest-listed files** verified by size and SHA256. It contains eight original unrestricted native full Bellman JSONs, eight independently recomputed exact optimal values and named first-action ties, complete replayed native identifying trees, frozen raw source, both programs, standalone analytic checker and full parent EC49FRI archive. This full tar archive is delivered as a user file, **not asserted to be a GitHub blob**; this PR stores the complete mathematical proof, a runnable rational checker and a certificate/index locator.

Frozen original master SHA256 cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e; named profile CSV SHA256 a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f.

**Status**: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Portable mathematical evidence is distinct from native Task/CLAIM/Result/Review/Activity. This proposition is about the frozen finite BRC observation model and makes no modification to protected P000 or ACTIVE worldview.

**Next science**: find a direct original-physical-observation branch-cover proof of Ru≥4 and Rm≥4 that avoids the high-price Bellman extraction, and rigorously classify extensions of the frozen observation set, root profiles and composite/provenance observers under which these bounds change. There is no finite x_crit in this unchanged model.
