# R5 K3 — One common terminal label, genuine two-law experiment and all-signed Bellman theorem

2026-11-03 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Problem and immutable provenance

Mother objective: construct a genuine finite two-measure stopped hypothesis test with equal four-observer FULL-history and seedless likelihood-ratio (LR) convex hulls but unequal actual real-behaviour observation images. This unit examines a stricter K3 terminal topology in which *both stop and continue report the very same terminal answer label*. The predecessor at `e498befa4d647ade7eb87620127ebe20213167eb` had two action-selectable labels L0,L1; `7f7cd02139b41d0fa59cd46213eff2c6f2dab9f4` established a 16-parameter support envelope for that different topology. Frozen scientific input pins remain Global Knowledge `a01383f825ef9d43b4b754254303298c64041568` and Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`; current normative rules have separate current-main provenance. P000 and ACTIVE worldview unchanged. BRC positive source flow is reused, without a claim of native-X6 realization.

## A single policy-independent finite physical terminal law

Four hidden sources are C,I,BJ,IJ, and the P/Q ratio at K3 *before action* is 4. For FULL choose real x,y in [0,1], i in [0,1-x], and sourcewise z_s,t_s,u_s in [0,1]. LR requires i=(1-x)y and common z_s=z, t_s=t, u_s=u. Define

```
w=(1/4,(1-x)/4,y/8,i/8), alpha=(1/2,2/3,1/2,3/4),
M_s=w_s*alpha_s*z_s, S_s=(2/3)*M_s*t_s, U_s=S_s*u_s,
d=y/16+3*i/32.
```

P-arrival mass at K3 for source s is S_s, and Q-arrival mass is S_s/4. For each source augment the *same fixed*, policy-independent sample space with three independent exogenous bits B,D,L. Their P- and Q-measure distributions are

```
P(B=1)=Q(B=1)=1/2;
P(D=1|s)=r_s, Q(D=1|s)=v_s;
P(L=Q|s)=1/2+p_s/8, Q(L=Q|s)=1/2-q_s/8,
```

where all sixteen p_s,q_s,r_s,v_s lie strictly in (0,1). Every one of the eight terminal atoms is positive under both laws. Gate action a in {0,1} yields time 5+B+a*D and terminal decision delta=L *for either action*. The controller does not observe L,B,D before the K3 action. Hence the pre-action LR=4 collision is retained, and the testing decision is a single physically shared output function under P and Q.

**Theorem 1 (physical observer identity).** For every admissible real FULL or LR policy, the actual type-I and type-II testing errors eP=P(delta=Q), eQ=Q(delta=P) and mean stopping times are

```
eP=107/128-21*x/128+d/4-sum(S)/2+sum_s(p_s*S_s)/8;
eQ=13/64+3*x/64-d/2+sum(S)/8+sum_s(q_s*S_s)/32;
TP=3+sum(M)+(3/2)*sum(S)+sum_s(r_s*U_s);
TQ=3+sum(M)/2+(3/8)*sum(S)+sum_s(v_s*U_s)/4.
```

*Proof.* Under P, the source arrival S_s has conditional error 1/2+p_s/8 for either gate action; under Q, arrival S_s/4 has conditional error 1/2+q_s/8. Relative to the inherited symmetric-label baseline the extra error masses are p_s*S_s/8 and q_s*S_s/32, independent of u_s. The conditional P extra time mean is r_s*u_s, Q extra time mean is v_s*u_s with Q mass S_s/4. Summing sourcewise disjoint events together with the unchanged upstream observer proves all four formulas. Every terminal product probability sums to 1. In particular, at fixed upstream masses and kernel, the *two error coordinates remain invariant when any K3 continuation control u_s changes*. QED.

## Exact all-signed real-policy support formula

For any signed n=(A,B,C,D) in R^4 put

```
K=C+D/2,  L=-A/2+B/8+3*C/2+3*D/8;
H_s=A*p_s/8+B*q_s/32, T_s=C*r_s+D*v_s/4;
c_s(x,y,i)=w_s*alpha_s;
b_n(x,y,i)=A*(107/128-21*x/128+d/4)
            +B*(13/64+3*x/64-d/2)+3*(C+D);
stage_0(s)=0;
stage_1(s)=K;
stage_2(s)=K+(2/3)*(L+H_s);
stage_3(s)=K+(2/3)*(L+H_s+T_s);
F_s=max(stage_0,stage_1,stage_2,stage_3).
```

Let VF be the six upstream corners {(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0)} and VL be the four LR corners {(0,0,0),(0,1,1),(1,0,0),(1,1,0)}.

**Theorem 2.** For *all real signed n and all 16-parameter kernels*,

```
h_FULL(n)=max_{v in VF}[ b_n(v)+sum_s c_s(v)*F_s(n) ];
h_LR(n)=max_{v in VL}[ b_n(v)+
             max_{j=0,1,2,3} sum_s c_s(v)*stage_j(s,n) ].
```

*Proof.* Sourcewise signed continuation contribution equals exactly c_s*z_s*[K+(2/3)*t_s*(L+H_s+u_s*T_s)], which is multiaffine in z_s,t_s,u_s, so its maximum on the real cube occurs at a corner. The four distinct nested corner stages above exhaust its maxima. FULL selects a potentially different stage for every source. LR must use a common stage for all four. With stages fixed, the FULL objective is affine in the upstream prism with six extreme points. The LR constraint i=(1-x)y makes the remaining objective bilinear on a square, hence maximal at its four corners. All reductions are exact for the entire real behavioral domain. QED.

Unlike the prior action-selectable-label topology, H_s appears at stage 2 and persists at stage 3; it is a function of S_s rather than U_s. Thus this is a new support formula for the genuinely stricter experiment.

## One rational strict physical separator, two normals and same witness

Choose
```
p=(1/4,1/2,3/4,1/2), q=(3/4,1/2,1/4,1/2);
r=v=(3/4,3/4,3/4,3/4);
nP=(8,0,-8/9,88/9), nQ=(0,-32,0,8).
```

The exact closed oracle, independently corroborated by complete Fraction enumeration, gives

```
              h_FULL     h_LR      difference
nP            1135/32    851/24    1/96
nQ            2093/96    523/24    1/96
```

A single FULL policy has upstream (x,y,i)=(0,1,1), source stages (C,I,BJ,IJ)=(1,1,3,1), with stage 1=(z=1,t=0,u=0), stage 3=(z=t=u=1). Its *actual physical observation* is

```
W=(659/768,401/3072,85/24,1247/384).
nP·W=1135/32,  nQ·W=2093/96.
```

Every LR policy and its entire convex hull satisfy nP·v<=851/24 and nQ·v<=523/24. The dual L1 norm of nP is 56/3, proving

```
dist_infty(W,conv O(LR)) >= (1/96)/(56/3)=1/1792.
```

The nQ certificate independently gives >=1/3840. The exact strict support obstruction therefore *survives the common-label restriction*. The mother problem requires hull equality, so this example excludes one source-sensitive candidate; it does not solve the mother question.

## Executed verification scope, evidence and continuation

`VERIFY.py` is a dependency-free standard-library Fraction checker, actually run, with stdout in `EXACT_OUTPUT.txt`. It checks all P/Q terminal atom probabilities for four sources, two measures, two actions, and two 16-parameter rational kernels, verifying positivity, normalization, label errors and terminal times; for each of five signed directions it compares closed support against exhaustive 1536 FULL and 16 LR deterministic configurations on each kernel. It checks real nonbinary-policy invariance, the actual witness, both supports and dual distance. **167 exact assertions pass.** The analytic proofs establish the stated continuous real quantifiers; the finite tests are arithmetic regression, not a substitute for the proofs. Mathematical independence, native CLAIM/Result/Driver review and native-X6 bridge remain unresolved.

**Next question:** use this stricter common-label all-signed oracle to seek rational nontrivial hull-equality candidates and give exact rational LR convex decompositions of every FULL vertex (<=5 LR vertices each) or one rational Farkas separator. Only for a full-hull-equal candidate investigate actual real-image nonmembership. Preserve the frozen science pins, current identity/owner authority and BRC source provenance.
