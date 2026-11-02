# R5 — Nonuniform time-face fiber forces four-observer separation

**Date:** 2026-11-03 (Asia/Shanghai). **Status:** AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Objective and prior scientific frontier

The mother objective is a finite physical two-law stopped tree with equal convex hulls for the true four-observer O=(e_P,e_Q,T_P,T_Q) under FULL history versus seedless LR, while their actual real-behavior image sets differ.

The directly preceding result, Enterprise Math commit d5c15d07bf71d7a66d1cc8fd9bb5e12d58e8ffcc, research_notes/brc_r5_ratio_balanced_time_projection_20261103_t0643/RESEARCH.md, classifies equality of the *two-time-coordinate projected* hulls. In particular, a=b=(3/4,1/2,1/4,1/4) is a nonuniform time-equality candidate. The all-signed FULL Bellman oracle comes from enterprise-math@fbeb40d310d5dbdb2766d4e1994293d74bf830c2, research_notes/brc_r5_delay_ratio_rigidity_20261103_t0542/RESEARCH.md. The physical P/Q stopping-tree embedding comes from enterprise-math@0592311ad484d47c449563167d2ae6521ccf4234.

Frozen SCIENTIFIC source pins: Global Knowledge a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Behavioral rules read separately at current canonical main. P000 and ACTIVE worldview are unchanged. This is a positive-rational BRC source-flow finite probability construction, with no native X6 physical calibration asserted.

## Physical source-flow observer

Hidden source order is (C,I,BJ,IJ). First serial P-success factors alpha=(1/2,2/3,1/2,3/4), Q factors alpha/2; second serial P-success c=2/3, Q factor c/2. The three LR time/likelihood-ratio collision keys stay J=(2,1), K1=(3,1), K2=(4,2).

For FULL, x,y in [0,1], i in [0,1-x], z_s,t_s independently in [0,1]. Set

~~~
w=(1/4,(1-x)/4,y/8,i/8);
d=y/16+3i/32;
Q_s=w_s alpha_s z_s;
S_s=c Q_s t_s.
~~~

Seedless LR requires i=(1-x)y and shared z_s=z,t_s=t with x,y,z,t in [0,1]. The exact physical P/Q observer is

~~~
e_P=107/128-21x/128+d/4-sum_s p_s S_s,
e_Q=13/64+3x/64-d/2+(sum_s q_s S_s)/4,
T_P=3+sum_s Q_s+sum_s(1+a_s)S_s,
T_Q=3+(sum_s Q_s)/2+(sum_s(1+b_s)S_s)/4.                (1)
~~~

All p_s,q_s,a_s,b_s are independently strictly between 0 and 1, subject only to the further assumptions of the theorem. Before four-observer readout, positive BRC source identity and both P/Q path measures remain explicitly represented.

## Theorem — an entire nonuniform time-equality branch fails four-observer hull equality

Let 0<a_0<a_I<=a_C<1 and

~~~
a=(a_C,a_I,a_0,a_0),   b_s=rho(1+a_s)-1
~~~

where rho is any real number for which every b_s lies in (0,1). Let all eight real p_s,q_s independently range over (0,1). The preceding time-projection theorem implies

~~~
conv (T_P,T_Q)(FULL) = conv (T_P,T_Q)(LR).
~~~

Nevertheless, the full true four-observer convex hulls are strictly separated for **all** such real parameters:

~~~
conv O(FULL) != conv O(LR).
~~~

More precisely, define tau=(a_I+a_0)/2, c=2/3 and

~~~
g=min{(c/6)(a_I-tau),(5c/32)(tau-a_0)} > 0.            (2)
~~~

For any 0<delta<g, define h=-c(1+tau), f=1, and

~~~
n_3=(h-f)/(1/2-rho/4);
n_2=1-rho*n_3/4;
n=(delta,0,n_2,n_3).                                    (3)
~~~

The denominator is positive since strict 0<a_s,b_s<1 forces 1/2<rho<2. Over **all real behavioral policies**,

~~~
h_FULL(n)-h_LR(n)=5 delta/128 > 0.                       (4)
~~~

A physically realized FULL witness W satisfies

~~~
dist_infinity(W,conv O(LR)) >=
   (5 delta/128)/(delta+|n_2|+|n_3|).                    (5)
~~~

The gap is independent of all eight answer parameters. This exact theorem removes the declared open nonuniform branch from the mother-target candidate pool.

## Proof — exposed-time-vertex answer fiber

**Step 1 (strict pure-time LR vertex and its margin).** At delta=0, the normal (3) satisfies h=n_2+n_3/2=-c(1+tau) and f=n_2+rho*n_3/4=1. After optimizing the serial second control, each source K1 contribution is

~~~
A_s=h+c(1+a_s)f=c(a_s-tau).
~~~

Thus A_C,A_I>0, whereas A_BJ=A_IJ=-c(tau-a_0)<0. The LR objective is multilinear in (x,y,z,t). Its unique maximizing binary corner is (x,y,z,t)=(0,0,1,1); its score is the constant baseline 3(n_2+n_3) plus A_C/8+A_I/6. Every z=0 or t=0 corner has incremental time score at most zero. At z=t=1, x=1 removes positive I and y=1 at x=0 inserts negative BJ and IJ. The exact minimum positive loss among the other 15 LR binary corners is

~~~
g=min{A_I/6,(1/16+3/32)(-A_BJ)}
 =min{(c/6)(a_I-tau),(5c/32)(tau-a_0)}.
~~~

So g is strictly positive for every real admissible kernel. No unenumerated real LR policy can exceed its binary-corner maximum.

**Step 2 (positive answer tilt retains the LR vertex).** Add delta*e_P to this time-only normal. Because e_P is a physical probability, 0<=e_P<=1. An alternative LR corner can improve the answer component by at most delta, while losing at least g in time score. For 0<delta<g, the same LR vertex remains the unique optimal binary corner, hence the optimal LR real-behavior score is n dot V, where

~~~
V=(107/128-p_C/12-p_I/9,
   13/64+q_C/48+q_I/36, T_P*, T_Q*).                     (6)
~~~

**Step 3 (FULL can move inside the hidden answer fiber).** Set x=0, y=i=1, z_C=z_I=t_C=t_I=1 and z_BJ=z_IJ=0 (the other t values are irrelevant). This FULL strategy retains its two positive C/I continuations, so has EXACTLY the same (T_P,T_Q) coordinates as V. But its upstream source-dependent answer variable is d=1/16+3/32=5/32 instead of the LR vertex's d=0. Therefore the true FULL witness is

~~~
W=V+(5/128,-5/64,0,0).                                 (7)
~~~

Its normal score exceeds the unique LR vertex by 5delta/128 for every p_s,q_s.

**Step 4 (FULL optimality for all real behaviors).** The exact predecessor FULL Bellman formula for an arbitrary normal (n_0,n_1,n_2,n_3) is

~~~
B=107n_0/128+13n_1/64+3(n_2+n_3);
h_x=-21n_0/128+3n_1/64; h_d=n_0/4-n_1/2;
h=n_2+n_3/2;
k_s=-n_0 p_s+n_1 q_s/4+n_2(1+a_s)+n_3(1+b_s)/4;
L_s=max(0,h+c max(0,k_s));
h_FULL=B+L_C/8+max(0,(h_d+L_BJ)/16)
       +max(h_x,L_I/6+max(0,3(h_d+L_IJ)/32)).             (8)
~~~

For (3), h_x=-21delta/128<0, h_d=delta/4>0, k_s=1+a_s-delta*p_s. Since g< a_I-tau, for all p_s in (0,1) one has

~~~
L_C=c(a_C-tau-delta*p_C)>0;
L_I=c(a_I-tau-delta*p_I)>0;
L_BJ=L_IJ=0.
~~~

The maximizing upstream FULL branch in (8) is precisely the source-resolved strategy (7); h_FULL(n)=n.W. Combining Step 2 and Step 3 yields (4); Holder's inequality yields (5). This proves the quantified theorem over the entire declared continuous real parameter family.

## Exact rational example and verification

Take rho=1, a=b=(3/4,1/2,1/4,1/4), p=q=(1/2,1/2,1/2,1/2). Then tau=3/8, (n_2,n_3)=(35/12,-23/3), g=5/384, delta=1/1000. The true observer points are

~~~
W=(7/9,43/288,173/48,619/192);
V=(851/1152,131/576,173/48,619/192).
~~~

Their four-dimensional support gap is 1/25600, and the exact L-infinity distance lower bound is 15/4064384.

The standalone Python standard-library Fraction verifier in adjacent VERIFY.py checks seven strict-positive rational parameter cases (rho=1, 4/5, 6/5, upper-level tie, near-boundary p/q). It exactly enumerates all 2048 raw FULL binary controls and 16 LR corners per case and crosschecks the all-signed analytic Bellman oracle, time margin, support gap and actual source-fiber witnesses. EXACT_OUTPUT.txt is the saved actual run output. Continuous-real claims follow analytically from Steps 1–4; finite enumeration is a regression.

**BRC reuse applied/executed:** positive source mass, serial Q_s->S_s composition, and source-specific answer readout. The new residual is (5/128,-5/64,0,0): it is invisible after the *time-only* projection but survives in the true four-observer readout. The original mother problem remains open. The next unit is the other nonuniform order branch a_C>=a_BJ>a_I=a_IJ, including its time-equal boundary fibers.

**Authority:** GitHub author-side preservation is distinct from a native Source CLAIM/Result/Driver review. This run's native Site reported research_authority_granted=false; bounded active-owner lookup returned CONTROL_QUOTA. The proof has not received independent mathematical review or canonical admission.
