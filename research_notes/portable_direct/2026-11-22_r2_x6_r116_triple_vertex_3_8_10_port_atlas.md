# X6 R116 — Triple-outward vertex bifurcation: exact 3/8/10 near-direction fan and Port atlas

Date: 2026-11-22 (Asia/Shanghai). Status: **AUTHOR_PROOF / EXACT_RATIONAL_REPLAY_PASS / NOT_INDEPENDENTLY_REVIEWED**. Scope: conditional four-positive-weight, all-six-pair BRC observer of R90–R115. Not a native Heartbeat Cell/Link temporal dynamics theorem. Frozen P000 and joint-observer commitments are unchanged.

## Model and inherited sources

For nonzero integer a=(x,y,z), set q(a)=max(sum max(a_i,0),sum max(-a_i,0)), u=x+3y+6z, v=3x+12y+30z, h=7x+39y+126z and t=(0,u,v,h). For positive weights w=(A,B,C,D),

F_w(a)=max_{0<=i<j<=3} |t_i-t_j|/(w_i+w_j),
eta_p(w)=min_{a != 0, q(a)<=p} F_w(a),
N_p(w)={±a:q(a)<=p,F_w(a)<3 eta_p(w)/2}.

The exact integral moment coordinates are (tau,m,n) with m=n (mod 2):

t=(0,tau,3m,tau+6n),
a=(10tau-12m+3n, -5tau+7m-2n, tau+(n-3m)/2).

Use the Type-I normalized R90 chart A+B=1, s=A, X=C+s, Y=D+s. The positive sharp-cone vertex
(s,X,Y)=(1/2,4,18)
has **exactly three incident non-ideal facets**
g_1=1-2s, g_2=18-Y, g_3=9+9X-2Y-18s.
The remaining Type-I facet slacks are strictly positive there. R90's two sharp-cone classification, R114's face-stratum theorem and R115's complete 40-edge extension are upstream sources, not new results of R116.

## Theorem — full local 2-parameter fan, all integer Ports p>=7

Fix arbitrary real r>0 and kappa in R. Let epsilon>0 and put

s=1/2+epsilon/2, X=4+kappa epsilon, Y=18+r epsilon,
w(epsilon)=(s,1-s,X-s,Y-s).

There exists epsilon_0(r,kappa)>0 such that for every 0<epsilon<epsilon_0 and **every integer p>=7** the exact optimum is

**eta_p(w)=12/[18+(r-1)epsilon].**

Write each direction below as an unoriented representative (tau,m,n), with the integral inverse above. Define disjoint sets, annotated by exact minimum Port:

S0={(0,0,2)[7], (0,1,1)[10], (0,1,-1)[17]}.
S1={(1,1,1)[1], (1,0,-2)[4], (1,1,-1)[6], (1,0,0)[11], (1,0,2)[18]}.
S2={(1,-1,-1)[21], (1,-1,1)[28]}.

Let [S]_{\le p} retain precisely the rows whose bracketed Port is <=p. Then

* r>=1: **N_p=[S0]_{\le p}**;
* 0<r<1 and 9kappa<=2r+7: **N_p=[S0 union S1]_{\le p}**;
* 0<r<1 and 9kappa>2r+7: **N_p=[S0 union S1 union S2]_{\le p}**.

These descriptions identify the *complete sets*, not only their sizes. The two equality rays are literal: r=1 excludes all seven tau=1 rows, and 9kappa=2r+7 excludes both S2 rows by the strict cutoff.

The three original sharp-cone facets are **simultaneously crossed outward** exactly when
g_1=-epsilon<0, g_2=-r epsilon<0, g_3=(9kappa-2r-9)epsilon<0,
i.e. r>0 and 9kappa<2r+9. Restricting to that triple-outward sector, for every p>=28 the near-direction counts are **3, 8, or 10** according to the three cases above. The *additional secondary ray* 9kappa=2r+7 lies strictly inside the triple-outward sector; crossing it changes the count by exactly two while the optimum formula stays unchanged. This extends the earlier positive-edge 3/10 and 8/10 bifurcations to their common triple vertex, without an outsider beyond the inherited R90 twelve-row templates.

## Proof

Set X_*=B+C=X-epsilon, Y_*=B+D=Y-epsilon=18+(r-1)epsilon. At epsilon=0 the inequalities Y_*>4X, Y_*>12 and X>3 are strict. Shrink epsilon_0 so they continue to hold and all weights remain positive.

**Minimum.** If tau!=0 then the AB observation costs at least 1, greater than 12/Y_*. For tau=0, m,n have equal parity. When both are even, n!=0 costs at least 12/Y_* by the BD observation, and n=0,m!=0 costs at least 6/X by AC, exceeding 12/Y_* under Y_*>4X and X>X_*; when both are odd, |m|>=1 costs at least 3/X>12/Y_* by Y_*>4X. The direction (tau,m,n)=(0,0,2), inverse a=(6,-4,1), has q=7 and achieves F=12/Y_* (its BD gap; the AD and CD denominators are larger). Hence for all p>=7, eta_p=12/Y_*.

**Complete finite bank.** Write H=3eta_p/2=18/Y_*. For sufficiently small positive epsilon, 0<H<2, XH<6 and Y_*H=18. Any strictly near integer direction therefore satisfies

|tau|<H<2, |3m|<XH<6, |6n|<18, m=n (mod 2).

Modulo global sign, tau=0 or tau=1, with |m|<=1, |n|<=2. Tau=0 gives precisely S0. Tau=1 gives precisely the seven S1/S2 directions. This is an exact reduction of the **unbounded integer lattice**, not a finite search assumption.

All S0 scores are strictly below H at epsilon=0 and remain so nearby. Every tau=1 candidate has AB score exactly 1 at the vertex; the five S1 rows have every other pair score strictly below 1 there. Therefore S1 enters exactly when H>1, equivalent to r<1.

The two S2 rows have, in addition, BC gap exactly 4 at the vertex; their other four non-AB/BC pair scores are strictly below 1. Nearby their membership is equivalent to the conjunction H>1 and

4/(B+C)=4/(X-epsilon) < 18/Y_*,
equivalent to 4[18+(r-1)epsilon]<18[4+(kappa-1)epsilon],
equivalent to **9kappa>2r+7**.

The Port values come by applying the displayed inverse and q to the ten rows; the largest is 28. Filtering these exactly enumerated directions by q<=p proves the theorem simultaneously for every integer p>=7. □

## Exact reproduction, evidence and next question

The accompanying pure-Python Fraction verifier evaluates all six actual observations for every oriented nonzero integer triple with q<=28: **77,196 oriented triples per parameter case**. It compares the **full exact unoriented direction sets** and optimum at p=7,10,17,21,28 for five rational parameter cases: (r,kappa)=(1/2,3/5), (1/2,8/9), (1/2,1), (1,4/5), (2,1), epsilon=1/100. All **25 comparisons passed**, including both strict-equality transitions. Exact rational arithmetic is used throughout. The finite replay is a crosscheck; the unbounded all-Port proof is above.

Source pins: R90 cone facets and optimum, global-knowledge@6395fb2cb9b4596054aba5f2a2a1f7056a71468a, journal/enterprise-math/2026-11-22/x6-r90-exact-sharp-weight-regions.md; R115 authored notes, enterprise-math@c19f2fd673b25192cba8107a099e318de269eb5f; 40-edge continuation, global-knowledge@67dfd2a1766d045ec59ecf25c9a8b51f84d1d04e. Current Source P000 V5, global locked P000 V4 and ACTIVE worldview were read separately; the parent Source science is not repinned by this note.

**Next:** classify the other positive vertices with three or more incident facets using exact local tangent fans and determine the first outsider farther from every sharp-cone closure, including its Port threshold. For p<7 the displayed pure-even optimizer is not feasible and a separate early-Port atlas is needed. Preserve current author proof status pending genuinely independent mathematical review.