# N=14 auxiliary iid: 84th exact optimal affine segment (author-level)

**Date 2026-10-25.** This is an exact finite-model author proof. It is not an independent Driver review, native execution/CLAIM or a theorem about Heartbeat, native X6 or BRC–Shor dynamics.

## Model and theorem

For *all* randomized sequential tests, including ones depending on their entire ordered observation history, let the horizon be 14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Write eP=P(decide Q), eQ=Q(decide P), tP=E_P T, tQ=E_Q T, and V14(alpha)=min{max(tP,tQ): eP,eQ<=alpha}.

Freeze the stage83 author predecessor:
alpha83=5172016234515395543/14900301753911083008;
V83=24511993371361253729/1862537719238885376;
B=(12,0,1) immediately decides Q with probability s83=22597148038114427/41779200000000000. State A83=(8,4,4) is fixed to Q, A82=(9,7,2) to P and older endpoint actions retain their stated values in the inherited action table in \`derive84.py\`.

**Exact theorem, all real parameters:** for every 0<=delta<=eta84,
V14(alpha83+delta)=V83-Gamma84*delta, where

eta84=35099010625/25868579433873408,
Gamma84=37415125476/8022631.

The sharp right endpoint and objective value are

alpha84=5172036451545515543/14900301753911083008,
V84=24500207606836313729/1862537719238885376.

## Exhaustive global Bellman certificate

At count-state (n,a,b), Q/P=2^(a+b)/3^a. Set K84=19502203788/8022631, lambdaQ=K84, lambdaP=72+8K84/9=17912921688/8022631, Gamma84=lambdaP+lambdaQ. In P-normalization the three actions have costs: stop P = lambdaQ*(Q/P); stop Q = lambdaP; continue = 1+sum_i P_i*D(child_i). Continue is available only for n<14.

Exact rational backwards evaluation of the inherited selected action against every alternative on **all 680 count-states** yields **1240** nonselected comparisons, **1238 strictly positive gaps**, **0 negative gaps**, and exactly two zero gaps:
A84=(7,4,0) continues versus stops P; B=(12,0,1) continues versus stops Q. The smallest positive gap is 380274535165/11977723901952. The root value is

Droot=2868894732374199775677018845/1757935628827668026228736
=V83+Gamma84*alpha83.

The iid conditional likelihood ratio and continuation law are constant across ordered histories with the same count-state. The Bellman inequality therefore applies to **every ordered-history-adaptive randomized test**, not merely a count-based subfamily:

Droot <= tP+lambdaP*eP+lambdaQ*eQ
      <= max(tP,tQ)+Gamma84*alpha.

## Primal: positive weighted ordered histories

For new tie A=(7,4,0), all 35 nominal ordered prefixes first reach A under the frozen predecessor; their exact first-hit masses are pA=4375/884736 and qA=4375/4478976. Continuing at A, the conditional tuple (P-error,Q-error,additional P-time,additional Q-time) is

RA=(3994163/4586471424,11865791/11943936,228785459/191102976,470683/331776).

A separate ordered-word DFS gives 327 terminal suffix words and 29 terminal decision-state/action classes. Early termination at A thus truncates 35*327=**11445** original full terminal paths. These integer counts are **not** probability masses; first-hit P/Q masses use exact positive-rational path weights.

For B=(12,0,1), all 12 nominal prefixes first reach B, with pB=48828125/725594112, qB=48828125/362797056, and continuation tuple RB=(63/64,1/144,9/8,13/12).

Let u be the probability of stopping at A and deciding P, and s the probability of stopping at B and deciding Q; elsewhere use the inherited actions. Define

X=pA*RA[P-error]=17474463125/4057816381784064;
Y=qA*(1-RA[Q-error])=341884375/53496602689536;
E=pB*(1-RB[P-error])=48828125/46438023168;
H=qB*RB[Q-error]=48828125/52242776064.

The cones of A and B are disjoint, because A occurs at n=7 with a=4 zeros, while B occurs at n=12 with a=0 zeros, and a cannot decrease. Thus *no mixed u*s terms* occur in risks or times, and relative to (u,s)=(0,s83):

Delta eP=-X*u+E*(s-s83),
Delta eQ= Y*u-H*(s-s83).

Both errors are equal exactly when

s=s83+h84*u, h84=(X+Y)/(E+H)=1875183527/348160000000.

Their common value is alpha83+eta84*u, with eta84=-X+E*h84=Y-H*h84>0. For all real u in [0,1] this is a valid randomized policy, with 0<s83<=s<=s84<1, where s84=22822170061354427/41779200000000000.

At u=0 and u=1 respectively the exact tP-tQ gaps are

2374155610282626305/3725075438477770752 > 0,
2358671366823186305/3725075438477770752 > 0.

By disjointness the gap is affine, so tP>tQ for **all real u** in [0,1]. All occupied actions are Bellman minimizing, hence the policy attains Droot=tP+lambdaP*eP+lambdaQ*eQ, and tP=V83-Gamma84*eta84*u. Substituting delta=eta84*u proves the entire real affine interval.

## Sharp right endpoint

Suppose alpha>alpha84 attained this same dual line. Because lambdaP and lambdaQ are positive, equality forces eP=eQ=alpha, and every positive-mass action must be Bellman-minimizing. Exhaustive strict gap excludes randomization except A and B. Even history-dependent tie probabilities may be averaged to effective u,s in [0,1] on count fibers, since each such fiber has a common conditional future and fixed likelihood ratio. With disjoint cones, balancing requires s=s83+h84*u and hence alpha=alpha83+eta84*u<=alpha84, contradiction. The finite-horizon policy-performance set is compact, so equality cannot hold beyond the right endpoint.

## Evidence boundary and successor

Local author checks actually executed and passed: \`derive84.py\` computes exact Fraction Bellman, weighted first-hit/suffix and forward endpoints; \`crosscheck84.py\` independently enumerates ordered first hits/suffixes, validates actual P/Q path weights and confirms additional exact interpolation equalities. The two programs share the inherited stopping table, so they are **not** independent mathematical review. The auxiliary positive-weight BRC carrier retains prefix order, multiplicity, stopping provenance and exact weights. No native X6/Heartbeat isomorphism, Lean formalization, independent Driver review, verified owner/CLAIM or frozen native Result is asserted.

New **unproved** stage85 candidate after fixing A84 to P:
K85=180792/79, A85=(11,5,1), continue versus P. Determine the new first-hit cone, exact error-balancing coefficient, full Bellman equality interval or explicit obstruction.

Predecessor: awdawmip/enterprise-math@ebd02a08ad207326c124eff17aed2be174228576:research_notes/n14_aux_iid_affine_83_20261025/PROOF.en.md.
