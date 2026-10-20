# Auxiliary BRC: a global 1/22 no-gain radius for two-step first-failure identification

Status: AUTHOR_DRAFT / EXACT_FINITE_CERTIFICATE / OWNER_UNVERIFIED / NOT_ADMITTED.
Date: 2026-10-20 (Asia/Shanghai).
GLOBAL_KNOWLEDGE_V1 source: awdawmip/chatgpt-global-knowledge@4e971c219b239fcec77f70b46c2907798d981d44.
Enterprise Math source: awdawmip/enterprise-math@86a903f3769a1a6925faadf815a8615f6fe9384e.
This is an auxiliary six-label deletion-feedback model, not native P000 X6 Cell dynamics.

## Theorem

Let N={0,...,5}, threshold q=5, and weights w*=(1,1,1,1,1,1) and w†=(0,1,1,1,2,2). An initial publicly protected label 5 is followed by one secret deletion v≠5 and safe feedback, which occurs surely under either model. A future public probe p triggers an independently drawn secret deletion v≠p from a shared, time-stationary row kernel K(p,v). Deletions are cumulative and idempotent; safety means surviving total weight ≥5. For each row put U(p,v)=1/5 (v≠p), and rho=max_p TV(K(p,·),U(p,·)).

Let V1(K) be the maximum total variation between the two models' first-failure distributions for one future probe, and let V2(K) be that for up to two future probes. If rho ≤ 1/22, then V2(K)=V1(K). In fact for every ordered two-probe word (p,q),

    Delta1_K(5)-Delta2_K(p,q) ≥ 152/166375 > 0,

where Delta_j is P†(all j future probes safe)−P*(all j future probes safe). Thus no two-step first-failure observation strictly improves on the best one-step experiment within the stated entire 30-coordinate row-kernel class. This strictly strengthens the previous generic no-gain radius 2/125; combined with the previously proved rational-kernel family, the remaining global critical radius satisfies

    1/22 ≤ rho* ≤ (sqrt(745)-15)/130 ≈ 0.094574524.

The number 1/22 is a proven sufficient no-gain radius, NOT the true critical distance or its optimality claim.

## Proof

For any deletion path, target safety implies that at most one distinct label has been deleted. Since the competitor's initial total is 7 and each single label weighs ≤2, target safety implies competitor safety. Therefore Delta_j equals the probability of one common event E_j: competitor safe and target unsafe, retaining full path provenance.

For two future probes (p,q), let Delta2_K(p,q)=P_K(E_3 on the three protected rows 5,p,q), and use Delta1_K(5)=P_K(E_2 on rows 5,5). The three first-failure outcome probabilities differ by (Delta1, Delta2−Delta1, −Delta2); because Delta1,Delta2≥0, the exact total variation is max(Delta1,Delta2).

Write K_p=U_p+d_p. Each d_p has zero sum and l1 norm ≤2 rho. The difference D_{p,q}(K)=Delta2_K(p,q)−Delta1_K(5) is a polynomial of degree ≤3 in the row probabilities. Expand products around U exactly:

    D(K)=D(U)+Σ_{r,v} Gamma_{p,q;r}(v)d_r(v)+R.

Gamma is the conditional-event coefficient obtained by fixing each occurrence of secret action v on public row r, averaging all other positions uniformly, and subtracting the analogous contribution from the two-position reference event. Repeated public rows contribute for every occurrence.

Put G_{p,q}=Delta1_U(5)−Delta2_U(p,q), and let

    L_{p,q}=Σ_r (max_{v≠r} Gamma_{p,q;r}(v)−min_{v≠r} Gamma_{p,q;r}(v)).

Since each d_r has zero sum, the linear term is at most L_{p,q} rho.

For any product of k≥2 row-deviation factors, even when the same row is repeated in different time positions, the signed product measure has total mass zero and l1 norm ≤(2rho)^k. The integral of an indicator against it has absolute value at most 2^(k−1)rho^k. There are three quadratic and one cubic products in Delta2, and one quadratic product in Delta1, so

    R ≤ 8rho²+4rho³.

Consequently

    Delta2_K(p,q)−Delta1_K(5)
    ≤ −G_{p,q}+L_{p,q}rho+8rho²+4rho³.

All 36 ordered pairs are exhaustively checked by exact integer path enumeration (125 legal three-action sequences per word, plus 25 for the reference), and exact rational Gamma calculation. The 36 (G,L) pairs fall into these ten classes:

- (4,4): count 1; G=12/125; L=43/25.
- (5,5): count 1; G=2/25; L=3/5.
- (4,5),(5,4): count 2; G=12/125; L=19/25.
- (0,4),(4,0): count 2; G=27/125; L=41/25.
- (0,5),(5,0): count 2; G=27/125; L=16/25.
- (0,0): count 1; G=41/125; L=7/5.
- Both in {1,2,3}: count 9; G=6/25; L=9/5.
- One in {1,2,3}, other 4: count 6; G=23/125; L=9/5.
- One in {1,2,3}, other 5: count 6; G=22/125; L=23/25.
- One 0, other in {1,2,3}: count 6; G=7/25; L=8/5.

For rho=1/22, the smallest of

    G−L/22−8/22²−4/22³

among all 36 words occurs for (4,4) and is exactly 152/166375>0. The bound worsens monotonically in rho≥0, proving the inequality for every rho≤1/22. Hence all two-step tail differences are strictly below Delta1_K(5), while V1(K)≥Delta1_K(5); using TV=max(Delta1,Delta2) proves V2=V1.

The conclusion also applies to adaptive continuation after the first safe observation in this absorbing first-failure model, since after failure there is no next action, and after safety there is only one observable continuation branch for a fixed protocol. Randomized policies are mixtures of deterministic policies and cannot improve the maximum TV of this binary-hypothesis experiment.

## Exact computation and scope

The finite certificate computes the Boolean event on every legal path, the zero-sum row gradient Gamma with Fraction, the per-row oscillations, and the 36 rational margins; minimum exact margin is 152/166375. Independent rational deletion-mask DP crosschecks 108 two-word cases under three concrete positive row kernels at distances 0, 1/25, and 1/22. Those finite checks support the explicit finite coefficient table; the full real-kernel conclusion comes from the analytic signed-measure remainder inequality. No numerical approximation, external physics premise, secret credential, formal claimant authority, or theorem promotion is used.

Required native source for BRC carrier: definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json. Method reuse: exact positive-rational path mass and provenance (REUSE_APPLIED); the perturbation certificate specializes existing path-event checker structure.

Owner/permission: authenticated GitHub user awdawmip. Native dispatch returned CONTROL_QUOTA and session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false). No formal owner confirmation, CLAIM, reviewer independence or native Source Result has occurred. This document is only unreviewed scientific provenance.

Next question: sharpen the generic signed-measure quadratic bound by computing exact second-order per-row interaction oscillations; alternatively find an exact rational counterexample at rho<0.094574524, checking all 6 one-step and 36 two-step strategies.
