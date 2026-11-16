# R5 — Exact one-coordinate BRC observer repair separates FULL_HIST from seedless LR

Date: 2026-11-06, Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Frozen science: GLOBAL a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Predecessors: scalar quadratic gate at 57f7d654e5dd002567e0b0d333937e6e38f3b4cb; exact J-width at 02e1b1263649e6bef8c2acf16212a54ffb9dd851; timing-boundary equality at b18d170624f7e3176edf91d5809628b24bcfe6ff. Current normative context was separately read from main. Scope: the fixed strictly positive delta=1/4 four-stage P/Q/BRC likelihood-ratio tree, an auxiliary finite observer and not an assertion about native X6 dynamics.

## Theorem

Use the seven stopped likelihood-ratio Q masses M_r at r in {1/10,1/2,3/4,1,5/4,3/2,19/10}. Write eQ=Q(declare P), eP=P(declare Q), D=eP+eQ-1, and TP,TQ for expected stopping times.

The actual behavior images of all-real FULL_HIST and seedless LR policies are strictly different under the alternative four-coordinate readout (D,TP,TQ,M_{3/2}). One rational FULL_HIST witness is

(D,TP,TQ,M_{3/2})=(5199/20000,267/80,137/40,27/80).

Every seedless LR policy with (TP,TQ,M_{3/2})=(267/80,137/40,27/80) satisfies D<=10113/40000. The exact separation gap is 57/8000.

Consequently the original four-observer readout (eP,eQ,TP,TQ), when supplemented with only the exact BRC carrier coordinate M_{3/2}, also separates the two actual behavior images. Its explicit five-observer witness is

(eP,eQ,TP,TQ,M_{3/2})=(161801/180000,6499/18000,267/80,137/40,27/80).

The mother R5 problem concerns the four observations without the fifth mass coordinate, so that projection question remains open for this tree.

## Exact construction

The frozen time-3 Q transition rows are q3[0]=(13/20,1/5,3/20), q3[1]=(1/40,9/20,21/40), with stopped likelihood ratios (1/2,1,3/2). Time-4 stopped ratios are (1/10,1,19/10). At central j=1 the terminal rows are q4[0,1]=(47/180,43/90,47/180) and q4[1,1]=(67/162,14/81,67/162). The outer j=0,2 rows are history independent as in the cited pinned scalar gate. All entries are strictly positive, rows normalize, and each conditional likelihood-ratio mean equals its parent ratio.

Choose root and second-stage Q continuation flows g=u0=u1=1. For the two distinct histories i and time-3 keys j, set

(x00,x01,x02)=(13/80,1/40,0);
(x10,x11,x12)=(1/80,9/40,0).

They satisfy 0<=x_ij<=b_ij=(u_i/2)*q3[i,j]. The actual conditional time-3 continue probabilities are (1/2,1/4,0) for history i=0 and (1,1,0) for i=1. Aggregates are X0=7/40, X1=1/4, X2=0. The exact time identities yield

TQ=1+g+(u0+u1)/2+X0+X1+X2=137/40;
TP=1+g+(3u0+5u1)/8+X0/2+X1+3X2/2=267/80.

Set alpha=47/180, beta=67/162, J=alpha*x01+beta*x11=239/2400. Exact stopped ratio masses are

M_{3/2}=3u0/40+21u1/80-X2=27/80,
M_{1/2}=13u0/40+u1/80-X0=13/80,
M_{1/10}=(509X0+9X2)/900+J=1787/9000,
M_{3/4}=M_{5/4}=0.

Declare P exactly at the keys r<1 and Q at the other keys. Its legal stopped P declaration mass is ell_r=M_r for r<1 and 0 for r>=1, yielding

eQ=M_{1/10}+M_{1/2}=6499/18000,
eP=1-(1/10)M_{1/10}-(1/2)M_{1/2}=161801/180000,
D=(9/10)M_{1/10}+(1/2)M_{1/2}=5199/20000.

## All-real LR impossibility certificate

For any legal stopping policy, 0<=u_i<=g<=1 and X2>=0, so

M_{3/2}=3u0/40+21u1/80-X2 <=27/80.

Equality forces u0=u1=g=1 and X2=0, because both displayed coefficients are strictly positive. Thus for EVERY candidate LR strategy matching the three observed coordinates, the time equations reduce to

TQ=3+X0+X1=137/40,
TP=3+X0/2+X1=267/80.

They force X0=2(TQ-TP)=7/40, X1=1/4. A seedless LR shares one conditional time-3 continue probability at j=1, forcing

A=u0/10=1/10, B=9u1/40=9/40,
J_LR=X1*(alpha*A+beta*B)/(A+B)=11/120.

Consequently the LR stopped mass at the extreme small ratio is uniquely

M_{1/10}^{LR}=509*(7/40)/900+11/120=6863/36000,

and its other stopped masses below one are M_{1/2}^{LR}=13/80 and M_{3/4}^{LR}=0. For ANY REAL randomized LR declarations 0<=ell_r<=M_r,

D=sum_r(1-r)*ell_r <=sum_{r<1}(1-r)*M_r
 <=(9/10)*(6863/36000)+(1/2)*(13/80)=10113/40000.

But the FULL witness attains D=5199/20000, strictly exceeding that bound by 57/8000. The exclusion applies to all real LR policies, not just to a sampled or fixed-flow family. QED.

## BRC transport, proof coverage, next test

The carrier is the seven-bin stopped Q histogram with history provenance; the original observer keeps only (eP,eQ,TP,TQ). Adding M_{3/2} repairs one information loss. This reuses the existing BRC scalar-J and timing-flow interface (REUSE_APPLIED); no new general tool family is proposed. The permitted operation is stopped-mass readout and unrestricted ratio-dependent labeling in this finite model.

The companion standard-library Fraction VERIFY.py explicitly checks every frozen stochastic kernel/moment, both time observers, the complete stopped-mass histogram, legal history continuation, exact FULL label errors, and forced pooled-LR comparison; it prints PASS_EXACT_R5_FIVE_OBSERVER_STRICT_SEPARATION. The quantified impossibility is proved by the algebra above, independent of finite checking.

Next unit: remove M_{3/2} while keeping W=(161801/180000,6499/18000,267/80,137/40). Construct the unrestricted seven-variable rational polytope K(W) from the pinned quadratic-gate theorem, then decide globally whether F=(A+B)J-X1*(alpha*A+beta*B) reaches zero on K(W). A root is an LR reconstruction and measures the precise repair lost on projection; a strict global one-sided certificate would settle the original four-observer separation for this W. Preserve frozen scientific inputs and obtain independent review separately from author-side Source publication.
