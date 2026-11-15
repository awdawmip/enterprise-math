# EC49FQJ — Certified two-parameter BRC optimality rectangle

Date: 2026-11-16. Scientific status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Frozen pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Extends EC49FQI, PR #2539, without changing the native observation model.

## Exact statement

Native BRC class 16943 contains 310 original configurations with 141 distinct complete named-root cost profiles. The permitted observations are 144 full-terminal scalars (indices 0..143) and 84 named-root scalars (indices 144..227); the goal is to identify the complete named-root profile with arbitrary finite adaptive decision trees. Denote by m_i the number of original configurations realizing profile i, so that the m_i sum to 310. Define the prior

    p_lambda(i)=(1-lambda)/141 + lambda*m_i/310.

A named-root scalar query costs r>0; a terminal scalar query costs t>0. Set x=r/t.

**Theorem. For every REAL parameter pair 1/10 <= lambda <= 1/6 and 1 <= x <= 3, the globally minimal expected identification cost over ALL adaptive trees is**

    V(lambda;r,t)=(1-lambda)*(5r+293t)/141 + lambda*(5r+704t)/310.

**The complete set of optimal first physical queries is {140,142} at EVERY parameter pair in this closed rectangle.** All 228 legal queries remain available at descendants.

This establishes a stable two-parameter phase of the intermediate-first-query behavior discovered in EC49FQI, across a threefold named-root observation price and a nondegenerate prior interval.

## Exact corner certificates

For lambda=a/b, integer state weights are W_i=310(b-a)+141*a*m_i, summing to 141*310*b. With t=1 and r=x, the four complete unrestricted integer Bellman computations yield:

| lambda | x | integer total mass | optimal total integer cost | ALL optimal initial physical indices |
|---|---:|---:|---:|---|
| 1/10 | 1 | 437100 | 931389 | 140,142 |
| 1/6 | 1 | 262260 | 561869 | 140,142 |
| 1/10 | 3 | 437100 | 960699 | 140,142 |
| 1/6 | 3 | 262260 | 578779 | 140,142 |

On any nonsingleton feasible state set S, the exhaustive exact recurrence is

    C(S)=min_{q with nontrivial partition} [c(q)*W(S)+sum_z C(S_{q,z})],
    C({i})=0, c(q)=r for q>=144 and t otherwise.

Every child of an eligible q is a strict subset. A non-splitting query provides no information and costs strictly more than zero; it can always be removed. Thus the recurrence optimizes unrestricted finite exact-identification policies. The 228 physical forced-first costs are checked, preserving distinct indices even when response partitions coincide. The native input was reconstructed directly from the two frozen source files. Four full Bellman certificates and an independent recomputation/replay script are included in the companion complete evidence archive.

Two fully realized adaptive trees, starting respectively with physical queries 140 and 142, are supplied in the companion archive certificate witness_both_queries_x_5_2_lam_1_10.json. Replaying BOTH trees on all 141 complete profiles and weighting by the 310 original configurations yields exactly the same quadruple

    (U_R,U_T; M_R,M_T)=(5,293;5,704).

Here U is the sum over the 141 profiles, and M is the sum with multiplicity m_i. Consequently each tree attains the same explicit cost formula above for every (lambda,x), including every corner.

## Rigorous multi-affine extension to the continuum

For any fixed correct finite adaptive policy pi, let R_i(pi),T_i(pi) be its root and terminal query counts on profile i. Its expected cost divided by t is

    f_pi(lambda,x)/t =
      (1-lambda)/141 * sum_i (x*R_i+T_i)
      + lambda/310 * sum_i m_i*(x*R_i+T_i).

This is bilinear in lambda and x (separately affine in each). The two explicit trees above have the common bilinear cost F(lambda,x). Every policy pi satisfies f_pi>=F at all four corners, by the unrestricted Bellman certificates. Consequently its bilinear excess D_pi=f_pi-F has four nonnegative corner values.

Define u=(lambda-1/10)/(1/6-1/10), v=(x-1)/2, with u,v in [0,1]. The exact identity

    D_pi(lambda,x)=(1-u)*(1-v)*D_00 + u*(1-v)*D_10
                   +(1-u)*v*D_01 + u*v*D_11

writes the excess everywhere in the rectangle as a convex combination of its four nonnegative corner values. Hence f_pi>=F everywhere, while each explicit witness tree achieves equality. This proves the value formula for all real parameters in the closed rectangle.

For the first-query classification, suppose an optimal pi at a strict interior point began with q outside {140,142}. Its excess vanishes at that point. All four interpolation weights are then strictly positive, so its excess must vanish at all four corners. Since the complete Bellman initial-action set at each corner equals {140,142}, this is impossible. For edge interiors, the same argument uses the two adjacent positive corner coefficients; the four corners are directly certified. Both 140 and 142 are attained everywhere by the displayed two fixed trees, proving the exact first-query classification throughout the closed rectangle.

**General lemma.** In a finite adaptive identification problem with parameter-independent action responses, if a fixed policy is optimal at all corners of a parameter box and every fixed-policy expected cost is multi-affine in those parameters, that policy is optimal throughout the box. The intersection of corner optimal-first sets similarly bounds the interior first-action set. The two equal-cost witnesses supply the matching lower bound on that set here.

## Verification and source provenance

Frozen pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. The original master file's SHA256 is cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e. The native root-cost CSV's SHA256 is a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f. The state population, query response vectors and provenance remain those of EC49FQI.

The four independent exact Bellman replays found precisely [140,142] at every corner and verified the integer minima above. Two native tree replays recovered the exact four observational count totals above. The checks are exhaustive on the declared 141-root-profile finite domain and use integer arithmetic. The theorem has not received an independent project mathematics review; no P000, Foundation, CLAIM, Result or Review status is changed.

**Next:** locate the first exact two-dimensional phase boundary outside lambda in [1/10,1/6] or x in [1,3]. Compare all 228 forced-first costs with the appropriate descendant optimizations and inspect where fixed witness-tree optimality first breaks, preserving complete named-root residual information.

Context: RS-EC49AS publication directory not found on current project main as observed in the corresponding run. This is independent portable research under the existing user authorization, not a formal Task claim.
