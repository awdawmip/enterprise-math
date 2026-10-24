# N=14 auxiliary iid sequential discrimination: exact 79th optimal affine segment

2026-10-24. **Author-level exact finite-model proof**, not Driver review, native CLAIM, BRC/X6 transfer theorem, Lean verification, or P000 promotion. Source predecessor: [stage 78](../n14_aux_iid_affine_78_20261024/PROOF.en.md), commit `74f1440e602ec2dd43a3ac3293cd25be9c1321f9`.

## Model and theorem

Observe iid symbols in {0,1,2} with P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), stopping by N=14. For any randomized **ordered-history** test let eP=P(decide Q), eQ=Q(decide P), and tP,tQ denote expectations of sample count. Define V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha.

Inherit the precise stage-78 stopping table and freeze A78=(7,6,1) to P. Let
```
alpha78 = 5171945833514479493/14900301753911083008
V78     = 3070638708629737543/232817214904860672
s78     = 23988183023675761/41779200000000000
eta79   = 5303571875/3233572429234176
Gamma79 = 1483387884/242449
```
**Theorem.** For EVERY real 0<=delta<=eta79,
```
V14(alpha78+delta)=V78-Gamma79*delta.
alpha79=5171970272373679493/14900301753911083008
V79=3068302372712437543/232817214904860672
```
The Bellman supporting line is sharp: it cannot be attained at any alpha>alpha79.

## Complete exact Bellman dual certificate

At z=(n,a,b), Q(word)/P(word)=2^(a+b)/3^a. Under L=tP+lambdaP eP+lambdaQ eQ set
```
K79=lambdaQ=776081412/242449
lambdaP=72+(8/9)*K79=707306472/242449
Gamma79=lambdaP+lambdaQ
```
The state action costs relative to P are: immediately P, lambdaQ*2^(a+b)/3^a; immediately Q, lambdaP; continue when n<14, 1+sum_i P_i D(child_i). Exhaustive backwards recursion over 680 count states compares 1240 nonchosen actions: 1238 strict positive gaps, **0 negative gaps**, exactly two action ties:
```
B=(12,0,1): continue/Q
A79=(8,4,0): continue/P
smallest positive gap=3364539239/143002238976
Droot=113524236416659537907157095/53125930293146884767744
     =V78+Gamma79*alpha78.
```
At any ordered history the conditional suffix law depends only on these counts, so this Bellman minimum bounds *all* history-specific randomized tests, not only count-Markov policies. Since both multipliers are positive,
```
Droot <= tP+lambdaP*eP+lambdaQ*eQ
      <= max(tP,tQ)+Gamma79*alpha.
```
Therefore V14(alpha)>=Droot-Gamma79*alpha globally.

## Actual first-hit BRC-positive branch masses

All binomial(8,4)=**70** nominal ordered histories at A=(8,4,0) are genuinely first-reachable. Exact masses pA=21875/2654208, qA=21875/13436928. The balancing tie B has 12 first-reachable histories, pB=48828125/725594112 and qB=48828125/362797056. Path identities, multiplicity and positive rational weights are retained; path counts are not probabilities.

Conditional on following the inherited continuation after a first hit, write (P-error,Q-error,extra P-time,extra Q-time). Exact suffix quadruples:
```
RA=(117797/191102976, 990673/995328, 9227861/7962624, 110887/82944)
RB=(63/64, 1/144, 9/8, 13/12).
```
An independently organized ordered-word DFS enumerates 123 completed suffix words from A, across 22 terminal states. Thus stop-at-A truncates **70*123=8610** old complete histories. A and B path cones are disjoint because the number of letter-0 observations is 4 at A and 0 at B and can only grow; hence no coin interaction term occurs.

## Two-coin exact primal attainment

At A, stop and decide P with probability u∈[0,1]; otherwise continue. At B, stop and decide Q with probability s; otherwise continue. Define
```
X=pA*RA.Perror=2576809375/507227047723008
Y=qA*(1-RA.Qerror)=101828125/13374150672384
E=pB*(1-RB.Perror)=48828125/46438023168
H=qB*RB.Qerror=48828125/52242776064.
```
Then relative to (u,s)=(0,s78),
```
Delta eP=-X*u+E*(s-s78)
Delta eQ=+Y*u-H*(s-s78).
```
The unique equality-of-errors compensation is
```
s=s78+h79*u
h79=(X+Y)/(E+H)=55630673/8704000000
eta79=-X+E*h79=Y-H*h79=5303571875/3233572429234176
s79=s78+h79=24255210254075761/41779200000000000.
```
Both extreme s values are strictly between 0 and 1. Exact forward recursion yields the prescribed alpha78,V78 at u=0 and alpha79,V79 at u=1. The tP-tQ differences at these endpoints are
```
2211858463500674861/3725075438477770752
2186055790582274861/3725075438477770752
```
which are positive. By disjointness, all four risks/times are affine in u, so tP>tQ throughout the REAL parameter interval. Both tie actions Bellman-minimize, so L=Droot and tP=V78-Gamma79*eta79*u. This meets the global dual lower bound for *every* real u, not merely seven sampled fractions.

## Sharpness, proof status and continuation

Any rule attaining the same supporting line above alpha79 must make every dual inequality equality, hence have eP=eQ=alpha and choose only Bellman-minimizing actions at positive-probability histories. Only A,B allow randomization. Every surviving ordered history at a given count state has the same P/Q likelihood ratio and conditional suffix, so even arbitrary history-wise tie randomization reduces to effective u,s∈[0,1]. Error equality requires s=s78+h79*u, giving alpha=alpha78+eta79*u<=alpha79, contradiction. This is *nonattainment of the line*, not nonexistence of V14 beyond alpha79.

Exact author verifier and ordered-branch crosscheck implement the complete finite rational recurrences; both share the inherited stop table and are not independent Driver review. Source-hosted verifier is the provenance-preserving stage78 adaptation; stage79 values were also computed and exact-checked locally using the uploaded stage78 research package. No native BRC/X6/Heartbeat equivalence or independent validation is asserted. Formal Owner/CLAIM remains unknown after CONTROL_QUOTA and STATIC_READONLY_SCOPE_DENIED.

**Candidate 80th frontier, not proved:** K80=8690664/2767, tie A80=(7,0,2), continue/Q. Next solve 80th full-Bellman certificate, positive weighted first hits and suffixes, balancing-coin compensation, time-gap and sharpness; see NEXT_TASK_PACKET_80.md.
