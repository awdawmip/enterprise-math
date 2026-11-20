# X6 R69 — Exact five-vector theorem for heteroscedastic positive-BRC D=3 star-moment recovery

Date: 2026-11-21 (Asia/Shanghai).
Scientific status: CONDITIONAL_AUTHOR_PROOF / EXACT_FRACTION_AUTHOR_ENUMERATION / NOT_INDEPENDENTLY_REVIEWED.
Line: R61–R68, following R68 heteroscedastic common-bias theorem.
Frozen scientific source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json; preserve the six native spatial axes, independent time, the Cell/Link/source distinctions and whole-triad TRIADIC_CLOSURE_E.

## Precise observation model

Fix integer p >= 3, maximum successful degree D=3, and named two-source positive-weight BRC branch relation. A row of degree d has d allowed B Ports, and t independent B resets conditional on the same named A Port give Z_t=(uv)^t * sum_i r_i^t. Here u,v>0 are known positive rational weights, r_i in {0,1,2,3}, and m_t=Z_t/(uv)^t=sum_d c_d d^t. This algebraic observation model is conditional; a native chronological reset/triadic Cell transition remains unproved. The retained full relation may contain extra structure invisible in the histogram.

For t=1,2,3, let y_t=m_t+b+e_t, where b is an arbitrary unknown *shared* additive bias, |e_t| <= eta*w_t and w_t>0. The target is (c_2,c_3), not the full relation or separate (c_0,c_1).

R68 establishes, for nonzero a=(c_2-c'_2,c_3-c'_3), the sharp pairwise ambiguity threshold

eta_pair(a;w) = 1/2 * max_{i<j} |z_i-z_j|/(w_i+w_j),

where z_1=0, z_t=sum_{d=2}^3 a_d(d^t-d), and feasibility is q(a)=max(sum positive a_d, sum negative -a_d)<=p. Define integer coordinates

x=a_2+3*a_3, y=3*a_2+12*a_3;
z=(0,2x,2y), y in 3Z, a_2=4x-y, a_3=y/3-x.

Thus eta_pair=Phi_w(x,y), where

Phi_w(x,y)=max(|x|/(w_1+w_2), |y|/(w_1+w_3), |x-y|/(w_2+w_3)).

## Theorem — an exact five-vector reduction for arbitrary channel weights

For **every** integer p>=3 and **every** (w_1,w_2,w_3) in (0,infinity)^3, the globally sharp threshold for distinct high-degree histograms is

eta*_{p,3}(w) = min {Phi_w(x,y) : (a,q,x,y) belongs to T and q<=p},

where the fixed set T consists of exactly these five sufficient competitors:

| a=(a_2,a_3) | q(a) | (x,y) | eligible populations |
|---|---:|---|---|
| (1,0) | 1 | (1,3) | all p>=3 |
| (-3,1) | 3 | (0,3) | all p>=3 |
| (4,-1) | 4 | (1,0) | p>=4 |
| (5,-1) | 5 | (2,3) | p>=5 |
| (9,-2) | 9 | (3,3) | p>=9 |

Consequently the *value* of the best indistinguishability threshold for all positive real precision weights has a five-candidate closed formula independent of p, except for eligibility at p=4,5,9. Other actual difference vectors can tie an optimal value; the theorem makes no uniqueness assertion for their full set.

**Proof.** For any feasible nonzero integer a, form (x,y) above. The sign reversal a -> -a preserves q and Phi; assume y>=0. If y=0 then x is a nonzero integer, a=(4x,-x), q=4|x|>=4. The T vector (x',y')=(1,0), q'=4, is eligible and satisfies simultaneously |x'|<=|x|, |y'|<=|y|, |x'-y'|<=|x-y|.

Otherwise y=3k for integer k>=1. Four exhaustive cases remain:

1. x<=0: choose (0,3), q'=3. From a_2=4x-3k<=-3 we have q(a)>=3. The candidate's coordinate triple (|x'|,|y'|,|x'-y'|)=(0,3,3) is coordinatewise <= (|x|,3k,3k-x).
2. 1<=x<=3k-2: choose (1,3), q'=1<=q(a) for nonzero integer a. Its triple (1,3,2) is coordinatewise <= (x,3k,3k-x).
3. x=3k-1: choose (2,3), q'=5. Here a_2=9k-4>=5, hence q(a)>=5. Its triple (2,3,1) is coordinatewise <= (3k-1,3k,1).
4. x>=3k: choose (3,3), q'=9. Here a_2=4x-3k>=9k>=9, hence q(a)>=9. Its triple (3,3,0) is coordinatewise <= (x,3k,x-3k).

In all cases the chosen candidate is eligible whenever a is and has three absolute coordinate gaps no larger. Since all w_i+w_j are strictly positive, Phi(candidate)<=Phi(a). Conversely the five candidates are genuine integer differences, with exactly the displayed q. By R68's named-positive-BRC realizability theorem, each eligible candidate is realizable by two p-row degree distributions: use positive and negative parts of a for degrees 2 and 3, fill the rest with degree-zero rows, and realize each degree-d row with the first d distinct named B Ports. Thus the five-vector minimum equals the globally sharp ambiguity threshold. QED.

## Exact consequences and new diagnostic examples

The formula has only four possible population regimes: 3, 4, 5..8, and >=9. At w=(1,1,1), it yields R64's D=3 steps eta*=3/2 for p=3 and eta*=1/2 for p>=4.

For highly uneven weights w=(100,1,1), the entire Port-number staircase is:

eta*_{p,3} = 1 (p=3), 1/2 (4<=p<=8), 3/101 (p>=9).

The final discontinuity is realized by a=(9,-2), q=9, x=y=3. By contrast, for w=(1,1,100), a=(-3,1) yields eta*=3/101 already at p=3. These are distinct source-histogram residual structures with entirely positive branch masses.

This solves the **unrestricted positive-weight D=3 exact minimax value**, extending R68 beyond its earlier sufficient small-heterogeneity stability region; it does not claim D>=4 is solved.

## Reproducibility and limits

Exact Python standard-library Fraction test (x6_r69_d3_finite_formula_verify.py): exhaustive feasible a in [-p,p]^2 for each p=3..15; all 5^3 positive integer weight triples with entries {1,2,3,5,11}; a total of 1,625 exact-weight/population combinations and 507,000 checked feasible vectors (with repetitions across profiles), all agreeing with the five-vector formula. It separately verifies the coordinatewise domination property for every enumerated feasible a. This is author checking; the theorem's all-p/all-real-weight statement rests on the combinatorial proof above.

The code and exact output are the sibling files x6_r69_d3_finite_formula_verify.py and x6_r69_d3_finite_formula_results.json. No classical physical propagation, trigonometry, matrix exponential or new native BRC experiment is performed.

Source: R68 paper at https://github.com/awdawmip/enterprise-math/blob/e158d0cd7bb5e9c6bcc7bd0db36b71a66bd1bcaa/research_notes/portable_direct/2026-11-21_x6_r68_heteroscedastic_common_bias_star_moments.md . Prior R64 uniform D=3 classification and R65–R67 are inherited by exact referenced scope.

## Frontier

For D>=4 determine a comparably small *weight-independent* Pareto candidate set, or prove its size grows with p/D; then evaluate actual nonuniform precision transition chambers. Independently, test whether frozen-P000 TRIADIC_CLOSURE_E admits an original-typed Port-preserving reset and Cell/Link mapping; conditional positive star moments must not be promoted to a native time law.

Provenance: prior researcher EM-X6-214D9C, activity RA-545183ADD4EF71C3E4698AEE, Source scientific contribution only. Current native CLAIM/PROGRESS and the pending R63–R69 Activity links require separate actual permission verification; no owner claim or scientific admission is asserted here.
