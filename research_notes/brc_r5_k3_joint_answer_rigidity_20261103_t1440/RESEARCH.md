# R5 K3 — Joint P/Q terminal-answer source rigidity at constant delay

Date: 2026-11-03 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Precise provenance and frozen scope

Direct continuation of `research_notes/brc_r5_k3_answer_two_rigidity_slices_20261103_t1340/RESEARCH.md` at immutable EM commit `38ba53848c340fe253d29b01ec9d6d594c9e0654`, itself inheriting the all-signed K3 support oracle at `2c47ed2096e2cbdc1b5bbd88291dc8583d9f72de`. Frozen scientific pins remain Global Knowledge `a01383f825ef9d43b4b754254303298c64041568` and Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Current behavioral rules are read separately. P000 and ACTIVE worldview were read and not modified.

We study the same explicitly declared finite **auxiliary** two-law four-observer process, not an asserted native X6 embedding. Four hidden positive-mass sources are `C,I,BJ,IJ`; the observer retains the joint source information until an exact aggregation is proved. The path-level interpretation of the newly tagged terminal Bernoulli label as the original stopping experiment's actual error event is an outstanding semantic obligation.

## Exact observer

Let x,y,i in [0,1] with x+i<=1. The LR upstream relation is i=(1-x)y. The positive source masses and coefficients are

`w=(1/4,(1-x)/4,y/8,i/8)`, `alpha=(1/2,2/3,1/2,3/4)`, `d=y/16+3i/32`, `c_s=w_s alpha_s`.

For FULL, the stage controls z_s,t_s,u_s belong to [0,1] separately for each s; LR shares one z,t,u. Let `M_s=c_s z_s`, `S_s=(2/3)M_s t_s`, `U_s=S_s u_s`. All four terminal delay probabilities are fixed to `r_s=v_s=3/4` under both laws; the tagged answer fraction is `theta=1/8`. Allow **joint arbitrary** p_s,q_s in (0,1), independently across all four sources, and define

```
eP=107/128-21x/128+d/4 - (sum S)/2 + (sum p_s U_s)/8
eQ=13/64+3x/64-d/2 + (sum S)/8 + (sum q_s U_s)/32
TP=3+sum M +(3/2)sum S +(3/4)sum U
TQ=3+(1/2)sum M +(3/8)sum S +(3/16)sum U.
```

These are the four declared auxiliary observable coordinates. Their positive gate/source mass provenance and bounded error-probability regime are exactly those of the predecessor.

## New joint eight-parameter classification theorem

**Theorem.** For every p,q in (0,1)^4, the convex hulls of the REAL behavioral observer sets FULL and seedless LR are equal **if and only if** both p and q are separately constant across all four sources. When both are constant, the actual real observer sets also agree: `O(FULL)=O(LR)`.

Indeed, for every real tau in (0,1), consider the two signed normals

```
nP(tau)=(8,0,-(4+8tau)/9,(80+16tau)/9)
nQ(tau)=(0,-32,(8tau-4)/9,(80-16tau)/9).
```

Let `P_a(tau)=sum_s c*_s max(a_s-tau,0)` and `N_a(tau)=sum_s c*_s max(tau-a_s,0)`, with `c*=(1/8,1/6,1/16,3/32)` (the x=0,y=i=1 source weights). Then **for every simultaneously varying p and q**, and every legal real upstream/gate policy,

```
hFULL(nP)-hLR(nP)=(2/3)min(P_p,N_p)
hFULL(nQ)-hLR(nQ)=(2/3)min(P_q,N_q).
```

Unlike the preceding slice normals, nP has B=0 and nQ has A=0; this makes the two certificates independent of the other four answer parameters. For a nonconstant a, any tau in (min_s a_s,max_s a_s) produces a strictly positive support difference.

## Proof of all-real dual formulas

For a general n=(A,B,C,D), the prior Bellman envelope gives baseline `B0=constant+Ux+Vd`, with `U=(-21A+6B)/128`, `V=(A-2B)/4`, and local source maximum

```
max(0,K,K+(2/3)H,K+(2/3)(H+J_s)),
K=C+D/2,
H=-A/2+B/8+3C/2+3D/8,
J_s=3C/4+3D/16+(A/8)p_s+(B/32)q_s.
```

This follows by maximizing a nested z/t/u gate of the form `c_s z_s[K+(2/3)t_s(H+u_s J_s)]` successively at the endpoints; it holds for real gate probabilities because the dependence is multi-affine. Substitution of nP yields `K=4`, `H=-(4+2tau)/3<0`, `H+J_s=p_s-tau`, `U=-21/16<0`, `V=2>0`. Substitution of nQ yields `K=4`, `H=(2tau-4)/3<0`, `H+J_s=tau-q_s`, `U=-3/2<0`, `V=16>0`.

Since `-1<a_s-tau<1`, the local FULL source maxima are respectively `4+(2/3)(p_s-tau)_+` and `4+(2/3)(tau-q_s)_+` (always positive). Every such positive source factor increases with its own carrier. Under FULL, the baseline increases with y and i and decreases with x, while the source carriers are nonincreasing in x and nondecreasing in y/i. The common FULL maximizing upstream corner is therefore x=0,y=i=1, for **all** p,q and tau.

Under seedless LR, the shared gates have only four stage outcomes. The 0 and stage-2 possibilities are dominated by stage 1 (`K=4`, `H<0`), so the LR support envelope is the maximum of `B0+4T(x,y)` and `B0+4T(x,y)+(2/3)F(x,y)` with `T=sum c_s`, `F=sum c_s(a_s-tau)` for nP and `F=sum c_s(tau-a_s)` for nQ. Both pieces have positive coefficients on each c_s (at least 10/3), decrease with x, and increase with y since U<0,V>0 and LR carriers `c=(1/8,(1-x)/6,y/16,3(1-x)y/32)`. Thus both achieve their upstream maximum at x=0,y=1. Writing P,N for the corresponding signed positive and negative sums at that corner, FULL gives `B*+4T*+(2/3)P`, while LR gives `B*+4T*+(2/3)max(0,P-N)`. The difference is exactly `(2/3)min(P,N)`.

If either p or q varies between sources, select tau strictly between its min and max; the corresponding positive and negative sums are both strictly positive because every c*_s>0. This proves necessity. Conversely, suppose p_s=p0 and q_s=q0 for all s. For any FULL policy, preserve x and d by setting

```
y'=32d/(5-3x),  i'=(1-x)y';
T=1/8+(1-x)/6+d;
z'=(sum M_s)/T;
t'=3(sum S_s)/(2sum M_s) if sum M_s>0 else 0;
u'=(sum U_s)/(sum S_s) if sum S_s>0 else 0.
```

The FULL constraints imply `0<=y'<=1`; all three common gates lie in [0,1]. The LR source-carrier sum is T, and these gates exactly reproduce `sum M`, `sum S`, `sum U`; since p0,q0 and r=v=3/4 are source-constant, all four declared observer values coincide. LR is a subset of FULL, so this proves equality of **actual** real observer images.

## Exact computational verification and witness

`VERIFY.py` uses standard-library `fractions.Fraction` for all arithmetic. It performs 96 paired signed support comparisons, for 3 tau values, 4 p vectors, 4 independent q vectors, and the two isolating normal families. Every comparison enumerates 1536 FULL upstream/gate deterministic configurations and 16 seedless LR configurations; 40 additional nonbinary-policy aggregation checks are included. 223 exact Python assertions passed. Deterministic corner coverage is justified by the triangular FULL upstream polytope, the LR multi-affine upstream map, and the nested gate Bellman vertices; enumeration is a cross-check on the continuous proof above.

Take tau=1/2, p=(1/4,1/2,3/4,1/2), q=(3/4,1/2,1/4,1/2). Both separators are simultaneously supported by **one** FULL gate witness `x=0,y=i=1`, local stages `(1,1,3,1)`. Its observer is

`W=(659/768,401/3072,85/24,1247/384)`.

For `nP=(8,0,-8/9,88/9)`, exact `hF=1135/32`, `hLR=851/24`, gap `1/96`, hence `dist_inf(W,conv O(LR))>=1/1792`. For `nQ=(0,-32,0,8)`, exact `hF=2093/96`, `hLR=523/24`, gap `1/96`, and distance lower bound `1/3840`. The first is the stronger bound for this W. These estimates follow from duality with each normal's l1 norm.

Execution transcript is `EXACT_OUTPUT.txt`; source is `VERIFY.py`. This is a complete real-parameter classification **within the explicitly stated auxiliary**, with an elementary exact proof and independently executed rational regression tests. No native independent Driver review or canonical task Result has been obtained.

## Next

First construct an exact positive P/Q terminal-path event decomposition for the auxiliary tagged Bernoulli term and verify that it reproduces the *original* error event, timing and LR=4 collisions without modifying the frozen scientific question. If this bridge fails, retain the valid auxiliary classification and repair the observer definition. For mother-goal progress, vary the stopping topology/observable construction while checking all-signed convex-hull equality by exact LR convex-combination or separating certificates before studying set-image nonmembership. Preserve joint-source information until any compression has an observer-specific proof.
