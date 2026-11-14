# R5: variable-v seedless-LR four-observer cube enlargement (2026-11-07)

Scientific status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Frozen scientific pins: global a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Immediate scientific predecessor: f4b6612c6bbc767fbbe37148309dd24d47f0c1a1 (research_notes/brc_r5_fixed_v_exact_max_cube_20261107/RESEARCH.md). Current normative main snapshots read separately: global bb45d87c3c994b7c4340281bb5e3db005f60f3df; EM 3056f752ac13601b0fc3feb52e3203a56aacbfdd.

## Theorem

In the frozen strictly positive four-stage P/Q-BRC probability model with delta=1/4, let the original four-observer readout be W=(eP,eQ,TP,TQ), with eQ=Q(declare P) and eP=P(declare Q). Put

\[
W_*=\left(\frac{161801}{180000},\frac{6499}{18000},\frac{267}{80},\frac{137}{40}\right).
\]

Every real W satisfying

\[
\boxed{\|W-W_*\|_\infty\le\frac{47}{40000}}
\]

is attained by a legal seedless likelihood-ratio (LR) randomized strategy. The construction uses g=u0=1, u1=v=1651/2000, time-3 continuation shared across the pooled likelihood-ratio key, and stopped declarations shared across the pooled key.

The preceding result proved an *exact* maximum centered cube radius 3747/3214400 for the **entire** fixed-v=33/40 seedless-LR family (including all six stopped LR declaration keys). Our new radius is greater by the exact ratio

\[
\frac{47/40000}{3747/3214400}=\frac{94423}{93675}>1.
\]

Consequently changing v strictly expands the already certified fixed-flow region; the relative radius improvement is approximately 0.7985%. This is a valid comparison between **fixed-flow subfamilies**. It neither states nor settles a difference between unrestricted FULL_HIST and seedless LR images. Global optimality for variable v is still open.

## Frozen probability kernel and observables

Time-2 likelihood ratios: (3/4,5/4). Time-3 likelihood ratios: (1/2,1,3/2). Time-4 likelihood ratios: (1/10,1,19/10).

The two time-3 Q rows are q3[0]=(13/20,1/5,3/20) and q3[1]=(1/40,9/20,21/40). The time-4 Q rows q4[i,j] are:

- j=0: (509/900,382/900,9/900), independent of i.
- j=1,i=0: (47/180,43/90,47/180).
- j=1,i=1: (67/162,14/81,67/162).
- j=2: (9/900,382/900,509/900), independent of i.

All Q rows are strictly positive, sum to one and have the prescribed conditional first LR moment, as checked exactly by VERIFY.py. For v=1651/2000, the Q mass available before the time-3 decisions at each LR key is

\[
V_j=(q3[0,j]+v\,q3[1,j])/2,\qquad
V=(53651/160000,\;22859/80000,\;46671/160000).
\]

Choose pooled time-3 continued Q masses X_j in [0,V_j]. Their legal LR-shared continuation probability is X_j/V_j. At history (i,j), the time-4 continued Q mass is

\[
x_{ij}=(u_i/2)q3[i,j]\,X_j/V_j,\qquad (u_0,u_1)=(1,v).
\]

The Q stopped mass M_r at LR key r is obtained by pooling the following contributions:

    M[5/4] += (1-v)/2
    M[r3[j]] += Vj-Xj
    M[r4[z]] += sum_ij xij*q4[i,j,z].

Repeated likelihood-ratio key 1 is pooled. Let E_r in [0,M_r] be the Q stopped mass declaring P. The four-observer readout is exactly

\[
e_Q=\sum_r E_r,\quad e_P=1-\sum_r rE_r,
\]
\[
T_Q=2+(1+v)/2+\sum_j X_j,\quad
T_P=2+(3+5v)/8+X_0/2+X_1+3X_2/2.
\]

## Explicit affine inverse

For arbitrary real t=(t0,t1,t2,t3) in [-1,1]^4 set W=W*+(47/40000)t. Define

\[
X_2=\frac{7611}{160000}+\frac{47}{40000}t_2-\frac{47}{80000}t_3,
\]
\[
E_a=\frac{201971}{1000000}+
\frac{47}{36000}(t_0+t_1)
-\frac{47}{72000}t_2+\frac{96681}{100000000}t_3,
\]
where a=1/10.

The other values are recovered by exact linear identities:

    p=TP-(2+(3+5*v)/8)
    q=TQ-(2+(1+v)/2)
    X0=X2+2*(q-p)
    X1=2*p-q-2*X2
    D=eP+eQ-1
    Eb=2*D-(9/5)*Ea
    E1=eQ-Ea-Eb

Take E at the stopped keys 1/10,1/2,1 to be Ea,Eb,E1 respectively, and zero at the other stopped keys. Substitution recovers the requested real W in all four coordinates. Declare P with LR-shared probability E_r/M_r at each stopped key with M_r>0, or use zero when M_r=0.

The only remaining feasibility conditions are the following 12 affine slack inequalities:

    X0, X1, X2, V0-X0, V1-X1, V2-X2,
    Ea, Eb, E1, M[1/10]-Ea, M[1/2]-Eb, M[1]-E1 >= 0.

The executed Fraction-only checker evaluates the **exact minima** of all 12 slacks over the 16 vertices t in {-1,1}^4. The minima in the displayed order are:

    28161/160000
    22859/80000
    7329/160000
    491/3200
    0
    19389/80000
    177966271/900000000
    76718471/500000000
    323/562500000
    1033/1800000000
    279/500000000
    769757009/4500000000

Every minimum is nonnegative. Since each slack is affine in t and [-1,1]^4 is the convex hull of its 16 vertices, the inequalities hold for **all real t**, including irrational and boundary targets. All time-3 continuation and all stopped declaration probabilities are therefore legal. The exact readout formulas prove the theorem.

## Verification and continuation

VERIFY.py was executed with standard-library fractions.Fraction; EXACT_OUTPUT.txt records its actual stdout. The source checker validates all frozen conditional Q/LR moments, mass normalization, four-observer recovery, all 16 exact vertices, and a supplementary grid of 625 rational targets. The finite grid is an extra consistency check; the all-real result follows from the affine-vertex proof.

This provides a new verified inner region for unrestricted seedless LR and identifies a limitation of holding v=33/40 fixed. It is useful to optimize v jointly with all time-3 continuation and stopped declaration masses; separately, the original R5 mother question remains open: whether the unrestricted four-observer FULL_HIST and seedless LR images coincide. In the separating direction, test the complete seven-variable K(W) and residual F=(A+B)J-X1(alpha A+beta B), rather than infer a four-observer difference from the established five-observer mass separation.

Control read 2026-11-07: native service status/tasks both returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false. Active R5 owner and formal CLAIM are unconfirmed; this scientific source is author-side evidence, not a formally admitted Result or independent Review.
