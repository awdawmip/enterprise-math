# R5: exact optimal four-observer cube at fixed seedless-LR timing flow

Research date: 2026-11-07 (Asia/Shanghai). Scientific status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Frozen science: global a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Scientific predecessor: c1c4b08cbe7eb7e39a980bc04c41b98ab4592657. The current rules were read separately from their canonical main snapshots.

## Theorem (full fixed-flow optimum, not a three-label subfamily)

For the frozen strictly positive four-stage P/Q-BRC model at delta=1/4, restrict the seedless likelihood-ratio timing flow to g=u0=1, u1=v=33/40, while allowing arbitrary legal continuation probabilities at all three time-3 LR keys and arbitrary declarations at **all six reachable stopped LR keys**. Let W=(eP,eQ,TP,TQ), eQ=Q(declare P), eP=P(declare Q), and

\[
 W_*=(161801/180000,\ 6499/18000,\ 267/80,\ 137/40).
\]

Then the **largest closed axis-aligned four-dimensional cube** centered at W* contained in this complete fixed-flow seedless LR image has half-radius

\[
 \boxed{h_*=\frac{3747}{3214400}\simeq0.001165691887}.
\]

Every real W satisfying ||W-W*||_infinity <= h* is implemented by an explicit seedless LR policy, including all irrational and boundary targets. No larger centered cube fits this fixed-flow LR family. The previously proved constructive radius 23/20000 increases by the exact factor 93675/92414, approximately 1.3645%.

## Frozen affine strategy model

Time-2 LR keys r2=(3/4,5/4), time-3 r3=(1/2,1,3/2), and terminal r4=(1/10,1,19/10). Conditional Q kernels:

    q3[0]=(13/20,1/5,3/20)
    q3[1]=(1/40,9/20,21/40)
    q4[i,0]=(509/900,382/900,9/900), for both i
    q4[0,1]=(47/180,43/90,47/180)
    q4[1,1]=(67/162,14/81,67/162)
    q4[i,2]=(9/900,382/900,509/900), for both i.

All rows are strictly positive, normalized and satisfy the conditional first LR moment. Define V_j=(q3[0,j]+v*q3[1,j])/2. Thus V=(1073/3200,457/1600,933/3200). Let X_j be the Q mass continuing at time-3 pooled key j, 0<=X_j<=V_j; the history-level continuation is x_ij=(u_i/2)q3[i,j] X_j/V_j with u=(1,v). The stopped mass at each reachable key r is assembled via

    M_(5/4) += (1-v)/2
    M_(r3[j]) += V_j-X_j
    M_(r4[z]) += sum_{i,j} x_ij*q4[i,j,z].

Repeated LR key 1 is pooled. For each r, let E_r be Q stopped mass declaring P, 0<=E_r<=M_r. Then M_r is affine in X and

\[
e_Q=\sum_r E_r,\quad e_P=1-\sum_r rE_r,\quad
T_Q=2+(1+v)/2+\sum_jX_j,\quad
T_P=2+(3+5v)/8+X_0/2+X_1+3X_2/2.
\]

These are all the legal fixed-flow seedless LR policies, not merely a predetermined choice of declaration keys.

## Global upper bound within the full fixed-flow family

Set D=eP+eQ-1= sum_r (1-r)E_r. Only stopped keys 1/10 and 1/2 have positive coefficients, so

\[
D\le(9/10)M_{1/10}+(1/2)M_{1/2}.
\]

Direct evaluation of the frozen kernels gives

\[
M_{1/2}=V_0-X_0,\qquad
M_{1/10}=(509/900)X_0+(2963/8226)X_1+(9/900)X_2.
\]

Hence using X1<=V1,

\[
\begin{aligned}
D &\le V_0/2+(9/1000)(X_0+X_1+X_2)
 +(2963/9140-9/1000)X_1\\
&\le\boxed{412287/1600000}+(9/1000)(T_Q-2-(1+v)/2).
\end{aligned}
\tag{1}
\]

At W*, D*=5199/20000 and S*=TQ* -2-(1+v)/2=41/80. Every cube of half-radius h contains a corner with eP=eP*+h, eQ=eQ*+h, TQ=TQ*-h, and either sign for TP. At that corner (1) implies

\[
5199/20000+2h\le412287/1600000+(9/1000)(41/80-h)
\quad\Longrightarrow\quad h\le3747/3214400.
\]

Thus the proposed h* is an **upper bound even allowing declarations at all six keys**.

## Explicit affine inverse and exact all-real certificate

For arbitrary real t=(t0,t1,t2,t3) in [-1,1]^4, set W=W*+h*t and define

\[
\begin{aligned}
X_2={}&593751/11522960
 -(8561895/4629925328)(t_0+t_1)
 +(3747/3214400)t_2
 -(131073807/231496266400)t_3,\\
E_a={}&4233133879/20741328000
 +(12401321/46299253280)(t_0+t_1)
 -(1249/1928640)t_2
 +(1418864/1446851665)t_3.
\end{aligned}
\tag{2}
\]

Let a=1/10, b=1/2, E_a=Ea. Recover the remaining coordinates:

    tp = TP - (2+(3+5v)/8)
    tq = TQ - (2+(1+v)/2)
    X0 = X2+2*(tq-tp)
    X1 = 2*tp-tq-2*X2
    D = eP+eQ-1
    Eb = 2*D-(9/5)*Ea
    E1 = eQ-Ea-Eb.

The only nonzero declaration masses are at keys 1/10, 1/2 and 1. For all time-3 keys use the pooled continuation probability Xj/Vj. For each stopped key r, use shared declaration probability E_r/M_r, with zero when M_r=0. This is a seedless LR policy. Substitution into the four affine readout identities returns W exactly.

The twelve necessary feasibility slacks are

    X0, X1, X2, V0-X0, V1-X1, V2-X2,
    Ea, Eb, E1, M_(1/10)-Ea, M_(1/2)-Eb, M_1-E1.

All are affine in t, so their exact minima over the whole real cube occur at its 16 vertices. The executed Fraction-only checker obtains, in that order:

    566211/3214400
    62400151/230459200
    3048954561/66141790400
    135106294483/925985065600
    0
    31034317689/132283580800
    8414194969961/41669327952000
    135106294483/925985065600
    239/4132800
    0
    0
    402953700901/2314962664000

Every slack is nonnegative on the continuous real cube. The two upper-bound corners t0=t1=1,t3=-1,t2=+/-1 attain V1-X1=M_(1/10)-Ea=M_(1/2)-Eb=0. This proves both all-real attainability and **exact optimality**, establishing the theorem.

## Reproducibility and continuation

The published standard-library-only VERIFY.py uses Python fractions.Fraction; EXACT_OUTPUT.txt is its actual executed stdout. It verifies conditional Q normalization and LR first moments, six-key M probability/moment identities, support inequality coefficients, the exact upper radius, all 16 vertex minima, 625 extra rational grid targets, and exact four-observer reconstruction. Finite corner evaluation is a rigorous certificate because every feasibility slack is affine.

The fixed-flow optimization is complete. The **mother question** remains equality of the unrestricted four-observer FULL_HIST and seedless LR images. A useful next unit is to vary v jointly with the full LR continuation/declaration polytope; separately, seek interior FULL_HIST rational W and a complete seven-variable K(W) quadratic-residual zero/sign certificate.

Control: this is author-side scientific evidence. Native control-result retrieval returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false. A service session_start returned QUEUED, while a live Owner/CLAIM and mathematical admission were not verified. Source GitHub publication is distinct from protected native Source admission.
