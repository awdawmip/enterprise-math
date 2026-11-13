# BRC N=4 / S23: exact six-witness minimax profile along O(1,t)

**Date:** 2026-11-02. **Status:** AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED. Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Parent six-witness 8/15 source: `6fe4cae0c1bd3e99d71758987827a681f0f655cc`.

## Model and theorem

Retain six *labeled* positive sources (AU0,AU1,AV,BU0,BU1,BV), four stopping atoms, common k=4 encoder with group order AU,AV,BU,BV, and original six prepared mixing rows M20/20:
(10,10,0,0,0,0), (9,11,0,0,0,0), (0,0,20,0,0,0), (0,0,0,10,10,0), (0,0,0,2,18,0), (0,0,0,0,0,20).
The legal 11-control vector is z=(a_A,a_B,b_U,b_AV,b_BV;c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV) in [0,1]^11, with shared causal b_U. Source s has distribution F(a,b,c)=(a,(1−a)b,(1−a)(1−b)c,(1−a)(1−b)(1−c)). The prepared source row i equals sum_s M20[i,s]F_s(z)/20; the decoded row applies the *same* positive mixing matrix to a common stochastic four-group decoder D. Let L_D(z)=max_{1≤i≤6}TV(P_i(z),Q_i(D)); G(z)=min_{1≤j≤10} L_{D_j}(z).

The first eight decoders remain frozen, each group row putting weight 1/2 on the stops specified by its pair:
1: 34 24 34 24; 2: 34 23 34 34; 3: 34 34 34 23; 4: 24 24 12 12; 5: 12 12 24 34; 6: 12 13 23 24; 7: 23 34 12 13; 8: 24 34 12 14.
D9,D10 may be *arbitrary real stochastic* 4-by-4 kernels. Put O(s,t)=(s,t,0,0,0;0,1,1,1,0,1), N(s,t)=(s,t,0,0,0;1,0,0,0,0,0), W=(1,0,0,0,1;0,0,0,0,0,0), J=(1,1/3,0,0,0;0,0,0,0,1,0), A=O(1/7,1), B=O(1,1/7), C=N(1/7,1), X_t=O(1,t).

**Theorem (all real t and arbitrary real free decoders).** For every t in [0,1/7],
R(t):=inf_{D9,D10} max_{z in {W,J,A,B,C,X_t}} G(z)
= max{32/63, min(1/2+t/2, 5/9−t/3)}.
It is 32/63 on [0,1/63], 1/2+t/2 on [1/63,1/15], and 5/9−t/3 on [1/15,1/7], with *unique maximum 8/15 at t=1/15*.

## Lower certificate: disjoint events plus exact two-coloring

For three witnesses U,V,T covered by the same stochastic decoder at radius r on one *original prepared row* i, choose disjoint stop events E_U,E_V,E_T. The total-variation event inequality and sum q(E)≤1 yield 3r≥P_i(U)(E_U)+P_i(V)(E_V)+P_i(T)(E_T)−1. This argument already quantifies over all real decoder probabilities, requiring no decoder discretization.

The fixed-eight decoder minima on W,J,A,B,C are 1,2/3,4/7,4/7,4/7 respectively. Each of their 10 triples admits a certified event sum at least 1+3×32/63. Below 32/63 every witness must take one of the two free labels; among five at least three share one label, contradicting the corresponding event certificate. Here are all 10 certificates, in format triple : prepared-row / event sets in order / total target mass:
WJA:6/2·4·13/8/3; WJB:6/2·14·3/20/7; WJC:6/2·4·13/8/3; WAB:6/2·1·34/20/7; WAC:3/1·3·24/19/7; JAB:6/4·1·23/53/21; JAC:3/1·3·24/19/7; JBC:6/4·3·12/53/21; WBC:6/2·3·14/20/7; ABC:3/3·1·24/19/7. Dot separates disjoint atom groups; each mass is computed with the six original positive mixtures.

For X_t, the frozen decoder 5 has exact loss u(t)=1/2+t/2, while each of the other 7 frozen decoders has loss 1 (a source-event difference). Thus below v(t)=min{u(t),w(t)} where w(t)=5/9−t/3, every one of the six witnesses must take free label 9 or 10.

The following ten triple certificates cover all 32 unordered two-label assignments (fix W color; 2^5 remain). Format triple : source row : three disjoint stop events : exact mass sum:
- WJX : 6 : 2/14/3 : 3−t
- JAC : 3 : 1/3/24 : 19/7
- WAX : 6 : 2/1/34 : 3−t
- JCX : 6 : 4/1/23 : 8/3−t
- WJC : 6 : 2/4/13 : 8/3
- WJA : 6 : 2/4/13 : 8/3
- WCX : 6 : 2/1/34 : 3−t
- WAC : 3 : 1/3/24 : 19/7
- JAX : 6 : 4/1/23 : 8/3−t
- ACX : 3 : 3/4/12 : 19/7

Their event lower bounds (mass sum minus 1, divided by 3) are all ≥u(t) for 0≤t≤1/15 and ≥w(t) for 1/15≤t≤1/7. The inequalities are affine and may be checked at interval endpoints. Every possible two-color assignment has a monochromatic triple from the table: exhaustive 32-coloring validation is finite and exact in VERIFY.py. Hence R(t)≥v(t); combined with the five-point certificate R(t)≥max{32/63,v(t)}.

## Upper certificate: explicit common decoders and convex interpolation

For 0≤t≤1/15, use D9 and D10 (rows AU,AV,BU,BV, each row stops 1–4):
D9=(9/14,0,5/14,0);(9/14,0,0,5/14);(1/2,0,0,1/2);(1/2,1/2,0,0).
D10=(41/63,0,22/63,0);(41/63,0,22/63,0);(29/45,0,29/315,83/315);(31/63,0,22/63,10/63).
D9 covers W,C with risk 1/2 and D10 covers J,A,B with risk ≤32/63. Frozen decoder 5 covers X_t at u(t). Thus the first full six-witness bank attains at most max{32/63,u(t)}.

For 1/15≤t≤1/7, set E=(9/14,0,5/14,0);(9/14,0,5/14,0);(1/2,0,0,1/2);(1/2,1/2,0,0), covering W,A at risk 1/2. The other free decoder is T(t)=(1−λ)T_left+λ T_right, λ=(t−1/15)/(1/7−1/15), with:
T_left=(71/105,0,34/105,0);(71/105,0,0,34/105);(3/5,0,1/15,1/3);(7/15,0,2/5,2/15).
T_right=(41/63,0,22/63,0);(41/63,0,0,22/63);(29/45,0,29/315,83/315);(31/63,0,22/63,10/63).
Each T(t) is a stochastic common four-group kernel. At t=1/15, T_left risks on J,B,C,X_t are 8/15,16/35,8/15,8/15; at t=1/7, T_right risks on J,B,C,X_t are all 32/63. Targets P(z) and decoded distributions Q(T(t)) are affine along this line, including X_t; TV is convex under joint affine interpolation, so risks at every real t are ≤(1−λ)(8/15)+λ(32/63)=w(t). E covers W,A at 1/2≤w(t). The second bank attains ≤w(t). Combine both upper and lower certificates to conclude equality.

## Exact validation, scope and next question

The actually executed Python stdlib Fraction VERIFY.py checks original six prepared rows; all eight frozen decoders and constructed decoders; 10 fixed-five and 10 varying-six event certificates; all 32 two-colorings; exact endpoints t=0,1/63,1/15,1/7; plus 105 rational regression points. The finite checks establish these concrete rational certificates; the lower event inequality and affine-TV convexity give the continuous real theorem. Reuse the companion RUN_EVIDENCE.json as execution evidence.

This theorem is **finite-witness and fixed-eight** for the original six-source observer. It fully answers the one-dimensional X_t subproblem. It does not change the broader two-real-face interval [8/15,4/7] or 11-real-parameter, ten-label [1/2,2/3] (k=4,6). The statistical source labels are an auxiliary BRC observer, not a demonstrated native P000 six-axis Cell/three-dimensional slice/independent-time physical map. Native owner/CLAIM/Result, independent review and admission are pending.

**Next:** select a seventh lawful strategy off the single X_t line, and construct an exact multi-point covering obstruction (including how first-eight decoders can absorb witnesses); alternatively build two decoders covering whole O/N real faces below 4/7 with rigorous TV sign-cell certificates.
