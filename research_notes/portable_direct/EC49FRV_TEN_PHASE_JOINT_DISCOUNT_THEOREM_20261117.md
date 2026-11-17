# EC49FRV — Exact ten-chamber BRC named-observer joint-discount theorem

**Date:** 2026-11-17. **Scientific input (frozen):** fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. **Immediate predecessor:** EC49FRU, PR #2655 (https://github.com/awdawmip/enterprise-math/pull/2655), immutable source commit 2788eba05069adc1b66395b08035eca77ca22a5f. **Evidence level:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / TWO_INDEPENDENT_RAW_RESPONSE_RECONSTRUCTIONS / NOT_REVIEWED.

## Exact native model

In frozen native BRC original class 16943, retain all 310 original configurations, 141 distinct complete named response states, and 228 original named physical observations (144 terminal and 84 root). The prior is uniform across the 141 complete named states (predecessor lambda=0), and the root/terminal base-price ratio x=1. Original response functions, query identity, provenance and scientific freeze pin do not change.

All observations have common base price t>0; only original terminal observations q32 and q34 receive the same discount delta*t. They cost (1-delta)t, and all 226 others cost t, with real 0<=delta<=1. At delta=1 the two named prices are zero.

For a complete legal adaptive original-observation-labelled identifying tree Q, let U(Q) be total query uses over all 141 named-state paths, and N(Q) total uses of exactly q32 and q34 along those paths. Then

    C_Q(delta) = t/141 * (U(Q) - delta N(Q)).

## Theorem 1 — exact unrestricted optimum for all real discounts

For every real delta in [0,1], among ALL legal complete native BRC identifying trees,

    141 V(delta) / t = min_j (U_j - delta N_j)

with these ten **complete and necessary** affine incidence types:

| Closed optimal discount interval | U_j | N_j | Affine value |
|---|---:|---:|---|
| [0,1/4] | 296 | 152 | 296-152 delta |
| [1/4,1/3] | 297 | 156 | 297-156 delta |
| [1/3,2/5] | 304 | 177 | 304-177 delta |
| [2/5,1/2] | 306 | 182 | 306-182 delta |
| [1/2,5/9] | 310 | 190 | 310-190 delta |
| [5/9,3/5] | 315 | 199 | 315-199 delta |
| [3/5,2/3] | 321 | 209 | 321-209 delta |
| [2/3,3/4] | 337 | 233 | 337-233 delta |
| [3/4,4/5] | 343 | 241 | 343-241 delta |
| [4/5,1] | 355 | 256 | 355-256 delta |

Exact transition points:

    {1/4, 1/3, 2/5, 1/2, 5/9, 3/5, 2/3, 3/4, 4/5}.

The neighboring affine branches tie at their shared endpoints. Each affine cost is realized by a complete original physical-query-labelled adaptive tree. The exact finite certificate checks that each tree identifies all 141 named states, with the stated total query uses and q32/q34 incidences. In each chamber's interior its branch is strictly below the other nine branches.

## Theorem 2 — minimum universal fixed-tree menu size = 10

At least ten different affine incidence types are required for a menu of fixed complete trees that obtains V(delta) for every delta in [0,1], and ten suffice.

Proof: Each fixed tree has one affine cost U(Q)-delta N(Q). On each open chamber, an optimal finite menu must contain one affine function coinciding identically with that chamber's exact optimal branch: a finite collection of other affine functions can equal that branch at at most finitely many points. All ten chambers are nonempty and have distinct slopes -N_j; no one affine tree type can coincide with two branches on distinct chambers. The ten replayed complete witnesses establish attainability.

The preceding four-*surcharge* theorem EC49FRU applies to a,b,c,d>=0. Its five fixed witness trees have combined q32+q34 incidence no greater than 141. With any strictly positive *common discount* 0<delta<=1/4 the true optimum is 296-152delta, using a full native tree with n32=141 and n34=11. Thus the unchanged earlier five-tree menu has a strict cost gap at least 11 delta*t/141. This is path-local reuse of *two distinct original named observations*, not an observer-identity collapse.

## Exact integer Bellman recurrence and complete finite anchors

For a nonempty subset S of 141 named states, let Pi_q(S) be the partition by the full original named response of physical observation q. For delta=n/d (0<=n<=d, d positive integers), solve:

    B_{n,d}({s}) = 0
    B_{n,d}(S) = min over q with |Pi_q(S)|>=2 of
      [ |S|*(d - n*1_{q in {32,34}}) + sum_{T in Pi_q(S)} B_{n,d}(T) ].

All 228 original named physical observations are considered at every nonsingleton state. Every informative observation creates strict smaller state subsets. At delta=1 a zero-price uninformative observation can be deleted without affecting identification or total cost. Thus pruning noninformative queries is still exact at the zero-price endpoint.

At all 11 rational anchors, the following exact unrestricted Bellman optima were independently reconstructed from the TWO raw-response input parsers and calculated with the SHARED integer Bellman recurrence:

| delta=n/d | d * 141 * V(delta)/t | reachable Bellman subsets per route |
|---|---:|---:|
| 0 | 296 | 13063 |
| 1/4 | 1032 | 13063 |
| 1/3 | 735 | 13063 |
| 2/5 | 1166 | 13063 |
| 1/2 | 430 | 13063 |
| 5/9 | 1840 | 13063 |
| 3/5 | 978 | 13063 |
| 2/3 | 545 | 13063 |
| 3/4 | 649 | 13063 |
| 4/5 | 751 | 13063 |
| 1 | 99 | 13063 |

Raw parser paths: EC49FRQ_INDEPENDENT_ALL228.py and EC49FQI_NATIVE_DATA.py, both reconstructing original frozen 94-family BRC data. All 228 indexed named response vectors agree after exact original index mapping. The same exact DP recurrence is used on both route outputs; they are independent INPUT reconstructions, not two independently implemented optimization algorithms. Full certificate includes exact Bellman route results and ten original complete native decision-tree witnesses replayed on all 141 states.

## Lemma — exact interpolation from endpoint Bellman certificates

For finite identifying systems with nonnegative, affine query prices, let F(delta) be the minimum cost over legal complete informative decision trees. One can prune uninformative queries, including zero-price uninformative nodes; there are finitely many informative trees over the finite state domain, so F is concave (the infimum of affine costs). Suppose a particular legal complete tree Q has affine cost L(delta), and exhaustive exact Bellman anchors certify F(a)=L(a) and F(b)=L(b), for a<b. For any a<=delta<=b, concavity gives

    F(delta) >= ((b-delta)/(b-a))*F(a) + ((delta-a)/(b-a))*F(b)
             = L(delta).

Since Q is admissible, F(delta)<=L(delta). Hence equality for every *real* delta in [a,b]. Applying this to the ten physical-query-labelled witness trees and their neighboring exact rational anchors gives Theorem 1 on the entire real interval [0,1]. This is a universal continuum conclusion from a proved finite completeness claim, not a floating-point parameter sweep.

## Evidence / original input / reproducibility

- Frozen scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
- Exact raw original BRC master SHA256: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e.
- Exact original profile CSV SHA256: a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f.
- Full original-domain verification: 141 complete named states, all 228 named physical observers, 11 integer Bellman anchors through two independent raw-response rebuilds, 10 full original decision trees with all 141 paths replayed. No random or floating-point solver is used for the Bellman theorem.
- Full local machine certificate EC49FRV_COMPLETE_10_CHAMBER_NATIVE_CERTIFICATE.json: 148697 bytes, SHA256 d7d79859cc0f36661571c9d0035edd80d1276ae70521c29fb9594c2a34723c3b. Self-contained evidence archive includes frozen source, dependency parsers, Python recurrence, ten complete trees, 11 anchor logs, scripts and hash manifest. Local archive SHA256 bffb4641372b59b4813911ed1665c5a642a6499244c9db7bf1da50c9d33e87e2 (227128 bytes, 39 manifest files). The complete local machine certificate and archive are **not automatically GitHub-hosted by this Markdown file**.
- These are results within the frozen BRC observation/price model. Mathematical admission status: NOT_REVIEWED.

## Control provenance and next scientific question

At 2026-11-17T15:34:22.452435Z, the native Source exact lookup on research topic RS-EC49AS, request emr4-20261117-2332-exact-task-read-v1, returned SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY on 5de0077a1142871da7e5d013c28bab40a75c108b. It is directory absence only, not an active owner projection. Historical researcher EM-DIRECT-8454C6 and Activity RA-ED136F89271FD89288F3E58D are contribution provenance, not present authorized CLAIM/Result/Review/Activity checkpoint. This document is independent portable research on its own new non-overwriting file path.

**Next:** Determine the exact two-parameter phase structure when q32 and q34 discounts are independently chosen (0<=delta32,delta34<=1). Preserve q32/q34 original names and path-local incidence; find genuinely new joint-use affine incidence types and phase boundaries. Then extend to q140/q142 and weighted original configurations.