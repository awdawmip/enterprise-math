# Enterprise Math R5: exact ancestor-statistic boundary for a source-sensitive two-route merger

2026-10-29. Author-side result: AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED. This is not a native CLAIM, Driver review, accepted theorem, or native Heartbeat World X6 dynamics.

## Sources and frozen constraints

This result immediately extends this run's rank/coin-pushing result at research_notes/brc_r5_merged_tail_rank_quotient_20261029_t0740/RESEARCH.md. The physical source-sensitive diamond's exact time formula is from research_notes/brc_r5_sensitive_tail_bellman_20261029_t0337/RESEARCH.md, Enterprise Math immutable commit 7d15ad6ab750b1caf041d1e760b8b354fc804083.

Knowledge snapshot: GLOBAL_KNOWLEDGE_V1 main@7b33f8066e9993e7c941959a9d738ed405248eb8; Enterprise Math main@d41c13c55100140ac6ca6bab920abd6ea93174c3; immutable native Source manifest ID 147f7b53374e32a4606a5c6d9a9611e6594a385f0edd3be902c2e01806b05f04. Global bootstrap/manual, P000, ACTIVE worldview, BRC and current portable research protocol read. Native session_start refused with STATIC_READONLY_SCOPE_DENIED, operation_sent=false; owner list returned CONTROL_QUOTA. No Source owner/CLAIM/Result is asserted. BRC carrier preserves positive source-by-route Q masses before observer-safe quotient.

## Exact model and observer

There are two separately identifiable predecessor LR decision keys, so independent route coins yield 0<=L,R<=U<=1. At the later common merged LR key there is ONE shared seedless real continuation coin gamma in [0,1]. The complete tail terminal Q signature histogram is H=gamma(a L+b R), with a,b fixed strictly positive vectors (columns of A), and a single observable upstream linear statistic is C=c_L L+c_R R. Define the real policy image:

S(A,c) = {(U,C,H): 0<=U<=1, 0<=L,R<=U, 0<=gamma<=1,
                            C=c_L L+c_R R, H=gamma(aL+bR)}.

No persistence or hidden source access is permitted; each policy coin may be any real in [0,1].

## Theorem (sharp necessary AND sufficient condition, all real)

S(A,c) is a compact convex polytope IF AND ONLY IF rank(A)=1 OR c=(0,0). In the complementary case rank(A)=2, c != 0, its ACTUAL seedless-LR image is nonconvex, not just an origin/path lifting.

Proof of sufficiency. If a,b are proportional, write a=lambda h,b=mu h with h>0 and lambda,mu>0. Set t=gamma(lambda L+mu R). Any real 0<=t<=lambda L+mu R is attainable by gamma=t/(lambda L+mu R) or gamma=0 at a zero denominator. Thus the exact image is the affine projection of the linear constraints 0<=L,R<=U<=1, 0<=t<=lambda L+mu R, C=c_L L+c_R R, H=t h. If c=0, independently of rank use beta_L=gamma L, beta_R=gamma R. Conversely any beta in [0,U]^2 is realized by gamma'=1,L'=beta_L,R'=beta_R and root/route coins beta/U (zero if U=0). Hence C=0, H=a beta_L+b beta_R is a compact polytope.

Proof of necessity. Assume a,b linearly independent and c != 0. Pick i with c_i != 0 and let j be the other route. The following are legal seedless policies with U=1:
P0 has L-vector=e_i and gamma=0, so C=c_i,H=0.
P1 has L-vector=e_i+e_j and gamma=0, so C=c_i+c_j,H=0.
Q has L-vector=e_j and gamma=1, so C=c_j,H=a_j (jth column of A).
The two candidate midpoints P0/Q and P1/Q have identical H=a_j/2, but respective C coordinates (c_i+c_j)/2 and (c_i+2c_j)/2.
Independence of the two columns forces any policy with H=a_j/2 to satisfy gamma L_i=0 and gamma L_j=1/2, hence gamma>0, L_i=0, and 1/2<=L_j<=1. Therefore its C must lie in I_j=[min(c_j/2,c_j),max(c_j/2,c_j)]. Both proposed C midpoints could be in I_j only if c_i=0: for c_j>0 their interval constraints imply simultaneously 0<=c_i<=c_j and -c_j<=c_i<=0; for c_j<0 the inequalities reverse with the same intersection; for c_j=0 both midpoints equal c_i/2 outside I_j={0}. Contradiction. Thus one midpoint is unattainable over ALL real policies. QED.

This characterizes the *minimal scalar ancestor measurement* boundary within this two-route, full-histogram model. It does not characterize the much coarser full four-observer image.

## Strict positive rational Q-time witness

Let v=(11/1200,23/3600), w=(1/40,1/100); signature likelihood ratios s=(1/2,1,3/2,5/2), and source-conditional Q kernels
eta_A=(1/8,1/4,3/8,1/4), eta_B=(5/32,3/16,13/32,1/4).
Each kernel is positive, sums to one, and has LR mean 3/2, so its P row is a normalized change of law. With K_(s,i)=eta_i(s), use a=K v, b=K w. The terminal s=1/2 and s=5/2 rows have exact rank-two minor

a_(1/2)b_(5/2)-a_(5/2)b_(1/2)=49/92160000.

This equals det(v,w) * det([[eta_A(1/2),eta_B(1/2)],[eta_A(5/2),eta_B(5/2)]])=(-49/720000)*(-1/128), a BRC source by observer residual certificate. Hence H uniquely determines beta=(gamma L,gamma R) from those two signature cells.

The actual earlier source-sensitive two-law Q stopping time satisfies
tQ=1+U/2+(3/40)L+(11/40)R+M, M=sum_s H_s.
Set c=(3/40,11/40).

Choose legal seedless LR policies
P=(U,L,R,gamma)=(1,1,1,0) with H_P=0, C_P=7/20,
Q=(1,1,0,1) with H_Q=a, C_Q=3/40.
Their midpoint has U=1, H=a/2, C=17/80. Terminal rank two forces beta=(1/2,0), hence R=0, 1/2<=L<=1, and necessarily C=(3/40)L<=3/40. Thus the midpoint lies OUTSIDE the entire real-policy S(A,c), with a sharp conditional excess

C_mid - max{C: U=1, H=a/2} = 17/80 - 3/40 = 11/80 > 0.

The affine change of variables C=tQ-1-U/2-sum H transfers the same exact nonconvexity to (U,tQ,H). Here tQ_mid=6193/3600 and, at the SAME U,H, no real policy can attain that tQ (gap 11/80). This is a conditional fiber separation, NOT a claimed global four-observer distance lower bound.

## Verified evidence and precise limits

Standalone VERIFY.py uses Fraction for the 49/92160000 determinant, invertible terminal histogram readout, two exact policies and midpoint, conditional 11/80 separation, previous physical tQ identity, 1296 exact rational route/merger regressions, and finite signed-c parameter checks of the midpoint interval proof. It ran and emitted PASS_EXACT_R5_ANCESTOR_OBSERVER_RANK_TWO_BOUNDARY in EXACT_OUTPUT.txt.

The theorem covers ALL real coins by explicit algebraic proof, NOT by finite testing. These results demonstrate true NONCONVEXITY of the augmented (U,C,H) and (U,tQ,H) policy images. They do NOT show nonconvexity of the four-observer target (eP,eQ,TP,TQ), nor any equal full-vs-LR all-signed convex hulls. In fact this same physical diamond has an earlier strict signed support gap and is already ruled out as the target mother counterexample. No independent mathematical acceptance or priority determination is claimed.

Next: calculate how much of the tail rank-two signature contrast survives the pair of freely randomized terminal declaration errors together with TP,TQ, with U/H unobserved. An exact all-signed deterministic hull/Farkas test is mandatory before pursuing actual real-policy nonmembership of any novel candidate.