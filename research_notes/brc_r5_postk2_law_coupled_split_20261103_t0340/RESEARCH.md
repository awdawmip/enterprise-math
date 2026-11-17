# R5 — Source-conditional post-K2 P/Q time fork: exact exposed-face rigidity

2026-11-03 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Scientific predecessor (immutable): awdawmip/enterprise-math@330562930d1822369f9e6063292cd5521823916b:research_notes/brc_r5_independent_two_law_k2_20261103_t0236/{RESEARCH.md,VERIFY.py,EXACT_OUTPUT.txt,NEXT_TASK.md}. Frozen scientific source pins: global a01383f825ef9d43b4b754254303298c64041568; enterprise-math 86149263e38c22292c9def1e0f69092efa1be77e. Current normative main rules, P000 and ACTIVE worldview were separately read, not substituted for the scientific input. This is a finite positive-source BRC probability-flow experiment, not a native-X6 physics claim.

Mother question: find a valid two-law finite stopped experiment with four physical observers O=(eP,eQ,TP,TQ), satisfying conv O(FULL)=conv O(LR) but O(FULL) different from O(LR). This paper gives an all-real classification for a new 12-parameter *post-K2 terminal time fork* and a concrete separator after two preceding signed normal tests vanish.

## Model and genuine probability laws

Retain the previous X -> J -> K1 -> K2 tree. Hidden source masses are (C,I,BJ,IJ)=(1/4,1/4,1/8,1/8), plus D=1/4. First-stage success probabilities are alpha=(1/2,2/3,1/2,3/4) under P and alpha/2 under Q. Second-stage success c=2/3 under P and c/2 under Q. The seedless LR information keys at J,K1,K2 remain respectively (time,likelihood ratio)=(2,1),(3,1),(4,2). There is no new decision at the time fork.

On K2 success the terminal Q-answer has source-dependent conditional probabilities p_s under P, q_s under Q. Independent of the answer, K2 success now terminates at time 6 with conditional probabilities r_s under P and 2*r_s under Q, otherwise at time 5. Domain: each p_s,q_s lies strictly between 0 and 1, and 0<r_s<1/8. Thus every natural branch, including both post-time alternatives, has strictly positive probability in both laws.

Let root flag probability be x. The two effective source survival masses at J are b and i, with 0<=b<=1, 0<=i<=1-x. Set

  w=(1/4,(1-x)/4,b/8,i/8)
  d=b/16+3*i/32
  Q_s=w_s*alpha_s*z_s
  S_s=c*Q_s*t_s
  R1=sum_s Q_s, R2=sum_s S_s, H=sum_s r_s*S_s.

FULL chooses its source conditional z_s,t_s independently. LR forces b=y, i=(1-x)*y, z_s=z and t_s=t at the colliding information sets. Root-history conditional policies are represented by the exact effective source masses; the checker additionally enumerates original terminal paths.

Direct P/Q terminal-path summation gives the physical observer formulas (1):

  eP=107/128-21*x/128+d/4-sum_s p_s*S_s
  eQ=13/64+3*x/64-d/2+sum_s q_s*S_s/4
  TP=3+R1+R2+H
  TQ=3+R1/2+R2/4+H/2.

Put vp=eP-107/128 and vq=eQ-13/64. Define the invertible readout

  X=(-vp/2-vq/4)/(9/128)
  D=(-3*vp/64-21*vq/128)/(9/128)
  U=4*(TQ-3)-(TP-3)
  V=2*(TP-3)-4*(TQ-3).

For xi_s=(64*p_s-8*q_s)/9 and theta_s=(8*p_s-7*q_s)/12, equation (2) is

  X=x+sum_s xi_s*S_s
  D=d+sum_s theta_s*S_s
  U=R1+H
  V=R2.

The law-coupled post-time split moves U and preserves V. These identities are exact, including real nonbinary control policies.

## Theorem A: two exact all-real signed gaps

Let w*=(1/8,1/6,1/16,3/32), A*=43/96, d*=5/32. For kappa=0 or kappa=-1/8, define

  f_s=theta_s+kappa*xi_s+r_s;
  m=(sum_s w*_s*f_s)/A*;
  n=(-2/3-64*kappa/9,-7/3-32*kappa/9,-1-2*m,4+4*m).

For every continuous kernel in the stated domain and all FULL/LR real behavioral policies,

  h_FULL(n)-h_LR(n) = (c/2)*sum_s w*_s*abs(f_s-m).       (3)

Proof: n dot O, up to a strategy-independent additive constant, is

  Psi=D+kappa*X+U-m*V
     =d+kappa*x+sum_s Q_s*[1+c*t_s*(f_s-m)].

For kappa=0, f lies in (-7/12,19/24), so c*range(f)<11/12<1. For kappa=-1/8, f=-(8*p+17*q)/36+r lies in (-25/36,1/8), so c*range(f)<59/108<1. Therefore each first-stage coefficient [1+c*t_s*(f_s-m)] is positive. FULL maximizes at x=0,b=i=1,z_s=1, then chooses t_s=1 precisely on f_s>m, yielding max_FULL Psi=d*+A*+c*sum_s w*_s*(f_s-m)_+.

For LR set A=sum_s w_s*alpha_s. Componentwise 0<=w_s*alpha_s<=w*_s, A<=A*, d<=d*. Since sum_s w*_s*(f_s-m)=0,

  abs(sum_s w_s*alpha_s*(f_s-m)) <= range(f)*(A*-A).

Hence Psi_LR<=d+z*A+c*range(f)*(A*-A)<=d*+A*. Equality occurs at x=0,y=z=1,t=0. Centering makes the positive weighted sum half the weighted absolute sum. This proves (3) for ALL real policies, not only finite controls.

## Theorem B: complete 12-parameter classification

For the stated post-K2 law-coupled time family,

  conv O(FULL)=conv O(LR)
  iff p_C=p_I=p_BJ=p_IJ, q_C=q_I=q_BJ=q_IJ,
      and r_C=r_I=r_BJ=r_IJ.                              (4)

When (4) holds, actual real-policy images are equal, O(FULL)=O(LR), and the common four-observer image has nonempty four-dimensional interior.

Necessity: Convex-hull equality forces zero gap at kappa=0, so f_s=theta_s+r_s=m for all sources. The corresponding exposing functional reduces to Psi=D+U-m*V=d+R1, independently of ALL second-stage decisions t_s. Its maximum d*+A* forces x=0,b=i=1,z_s=1 for FULL and x=0,y=z=1 for LR. This follows from the positive weights in d and R1; unreachable controls are irrelevant.

On this exposed hyperplane, FULL produces the zonotope

  O_base + sum_s c*w*_s*[0,1]*u_s,

while LR produces the single segment

  O_base + [0,1]*sum_s c*w*_s*u_s,

where u_s=(-p_s,q_s/4,1+r_s,(1+2*r_s)/4) is one unit of source-K2-success physical observation change. Hull equality forces equality of these exposed faces. Since every c*w*_s>0 and each u_s has positive time components, a Minkowski sum of their four segments is a line segment only if all u_s lie on a common positive ray.

The ratio of their time components is (1+2*r_s)/[4*(1+r_s)], strictly increasing in r_s (derivative 1/[4*(1+r_s)^2]). Thus parallelism implies source-constant r. Their time coordinates are then identical, so all positive ray scaling factors equal 1, and their first two components force source-constant p and q. This proves necessity.

Sufficiency: With source-constant p,q,r, (1) depends on FULL only via (x,d,R1,R2). For every FULL real strategy,

  0<=d<=(5-3*x)/32,
  0<=R1<=1/8+(1-x)/6+d,
  0<=R2<=c*R1.

The LR controls y=32*d/(5-3*x), z=R1/[1/8+(1-x)/6+d], and t=R2/(c*R1) if R1>0 (else t=0) all lie in [0,1] and reproduce every physical observer exactly. LR is already included in FULL. The affine determinant from (x,d,R1,R2) to O is -9/512, independent of constant p,q,r: the answer (x,d) block has determinant 9/128 and the time (R1,R2) block determinant -1/4. The LR interior auxiliary Jacobian is ((5-3*x)/32)*c*z*A^2 with A=1/8+(1-x)/6+(5-3*x)*y/32, and is nonzero for interior controls. Thus the common image is four-dimensionally full rank.

## Explicit candidate that fools both previous normals

Set base p0=q0=1/2, r0=1/16, deviations delta=(0,1/256,-1/256,1/128), and p_s=p0+delta_s, q_s=q0+8*delta_s, r_s=r0+4*delta_s:

  p=(1/2,129/256,127/256,65/128)
  q=(1/2,17/32,15/32,9/16)
  rP=(1/16,5/64,3/64,3/32)
  rQ=(1/8,5/32,3/32,3/16).

All parameters are in the open valid domain. Here xi_s is constant, theta_s=1/24-4*delta_s and r_s=1/16+4*delta_s. Consequently f_s is constant for BOTH kappa=0 and -1/8: the earlier two weighted-deviation gap tests give EXACT zero, despite nonparallel u_s.

A third simple physical normal is n=(82/9,95/9,3,0). Its dot product with O differs by a fixed constant from -X-3*D+3*U+3*V. The K2 source coefficient becomes

  k_s=3-xi_s-3*theta_s+3*r_s
     =-7/144+24*delta_s
     =(-7/144,13/288,-41/288,5/36).

Every first-stage coefficient 3+c*k_s is strictly positive; thus FULL chooses z_s=1 and optimizes t_s according to the positive part of k_s. After optimizing x,b,i the exact centered maximum is

  h_FULL(centered)=7/8+c*[(13/288)/6+(3/32)*(5/36)].

Under LR common y,z,t, the optimum has z=1,x=0 (the x coefficient is strictly negative) and

  h_LR(centered)=7/8+c*max(0,K0,K0+K1),
  K0=k_C/8+k_I/6=5/3456, K1=k_BJ/16+3*k_IJ/32=19/4608.

Restoring the common physical additive constant gives the all-real support certificate

  h_FULL(n)=101861/5184,
  h_LR(n)=407237/20736,
  gap=23/2304>0.                                         (5)

A FULL witness with x=0,b=0,i=1,z_s=1,t=(0,1,0,1) has

  W=(4741/6144,1657/9216,5489/1536,29891/9216)

and n dot W=h_FULL(n). Since ||n||_1=68/3, the exact distance bound is

  dist_infinity(W,conv O(LR)) >= 23/52224.

This is an explicit signed hyperplane obstruction for all REAL LR policies, not a finite direction sweep.

## Exact independent computation and next question

The executed Python Fraction VERIFY.py checks four strictly positive rational kernels, all 2,048 reduced FULL and 16 LR deterministic strategies per kernel, both weighted-deviation normals, the new support witness, 2,048 exact uniform aggregation checks, and 160 independent nonbinary original terminal-tree path sums under both P/Q measures with explicit time-5/time-6 branching. Actual execution returned 13,128 exact assertions, marker PASS_EXACT_R5_POSTK2_LAW_COUPLED_SPLIT_RIGIDITY, with raw output preserved as EXACT_OUTPUT.txt. The continuous theorems rely on the analytic proofs, and the finite checker supplies exact corroboration.

This family cancels both predecessor normals without eliminating source residuals; the exposed K2 source zonotope gives the decisive obstruction. Classification applies only to the specified rQ_s=2*rP_s coupling and rP_s<1/8 domain. The original mother problem remains open for independent two-law terminal time kernels or new decisions. The next test is a general split with independent P-delay a_s and Q-delay b_s, exact all-signed hull certificates, then real-image nonmembership if a valid hull-equality candidate appears. GitHub author-side preservation is not a native Source CLAIM, Result, independent Driver review, P000 change or accepted theorem.
