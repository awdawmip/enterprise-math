# R5: exact target-dependent-v optimum via a single BRC mass-capacity corner (2026-11-07)

**Scientific pins unchanged:** GLOBAL \`a01383f825ef9d43b4b754254303298c64041568\`; Enterprise Math \`86149263e38c22292c9def1e0f69092efa1be77e\`. Immediate certified lower-bound source: \`6f648b3c96a38cdaacda4633bee1cd5aba5904ff:research_notes/brc_r5_common_v_global_cube_optimum_20261107/{RESEARCH.md,VERIFY.py,EXACT_OUTPUT.txt}\`. Current normative policy was loaded independently; P000 and ACTIVE worldview remain intact.

**Status:** AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Exact all-real theorem

Use the frozen strictly positive four-stage P/Q–BRC kernel at δ=1/4 and the four-observer map W=(eP,eQ,TP,TQ), where eQ=Q(declare P) and eP=P(declare Q). In the full **seedless LR subfamily g=u0=1**, allow u1=v to vary arbitrarily with the target W; allow all three pooled time-3 LR continuation probabilities and all six stopped-LR declaration probabilities to vary with W.

Let
\[
W_*=(161801/180000,\;6499/18000,\;267/80,\;137/40),\qquad H=3543/3009580.
\]

Then the largest centered four-dimensional closed cube contained in the union of this subfamily's four-observer images has exact half-radius
\[
\boxed{\max\{h\ge0:\ W_*+[-h,h]^4\subseteq\mathcal O_{g=u_0=1}\}=H.}
\]
Moreover, **one ray already witnesses sharpness**:
\[
\boxed{W_*+h(1,1,1,-1)\in\mathcal O_{g=u_0=1}\iff 0\le h\le H.}
\]
Both statements quantify over all real randomized LR strategies and real targets, including irrational parameters. Allowing v to depend on W therefore does not enlarge this centered cube in the stated subfamily.

## Upper bound: same observed corner forces two competing capacities

The time-3 Q masses are
\[
V_0=13/40+v/80,\quad V_1=1/10+9v/40,\quad V_2=3/40+21v/80,\qquad 0\le X_j\le V_j.
\]
The stopped LR keys are r∈{1/10,1/2,1,5/4,3/2,19/10}. With stopped Q mass M_r, declared-P mass E_r∈[0,M_r], and D=eP+eQ−1,
\[
e_Q=\sum_r E_r,\qquad D=\sum_r(1-r)E_r.
\]
Setting M_a=M_{1/10}, M_b=M_{1/2}, every legal declaration obeys the simultaneous capacities
\[
D\le e_Q/2+2M_a/5,\qquad D\le 9M_a/10+M_b/2. \tag{1}
\]
For the proposed cube, choose **one and the same corner**
\[
W_+(h)=W_*+h(1,1,1,-1).
\]
Since eP≤1, any feasible such corner has h≤18199/180000. Since g=u0=1 implies TQ≤3+v, this corner also forces
\[
v\ge17/40-h\ge58301/180000>96/1019. \tag{2}
\]
Put p=TP−[2+(3+5v)/8], q=TQ−[2+(1+v)/2]. Time equations eliminate two flows:
\[
X_0=3q/2-p-X_1/2,\qquad X_2=p-q/2-X_1/2.
\]
From the frozen Q kernel,
\[
M_a=(509/900)X_0+c_1(v)X_1+(1/100)X_2,\qquad
c_1(v)V_1=47/1800+67v/720,
\]
\[
M_b=V_0-X_0,\qquad
c_1(v)-(509/900+1/100)/2=(1019v-96)/[900(9v+4)]>0
\]
using (2). At fixed (v,TP,TQ), both Ma and Mb increase with X1; consequently both are bounded by the algebraic X1=V1 substitutions. Evaluated at **the same** W_+(h):
\[
M_a\le M_a^*=(8737-1661v)/36000-(1259/900)h,
\]
\[
M_b\le M_b^*=(5v-1)/20+(5/2)h. \tag{3}
\]
Insert (3), eQ=eQ*+h, D=D*+2h into (1). Direct exact algebra yields
\[
(2317/1125)\,[U_1(v)-h]\ge0,\qquad
(2009/1000)\,[U_2(v)-h]\ge0,
\]
where
\[
U_1(v)=(1589-1661v)/185360,\qquad
U_2(v)=3(1113v-887)/80360. \tag{4}
\]
Thus the **single target** W_+(h) forces h≤min(U1(v),U2(v)) regardless of how v was selected. U1 is strictly decreasing, U2 strictly increasing, and they meet at
\[
v_*=17741/21497,\qquad U_1(v_*)=U_2(v_*)=3543/3009580=H.
\]
For h>18199/180000 feasibility already fails by eP≤1; the preceding proof handles the remaining h. Therefore **h≤H for every real seedless LR strategy in g=u0=1**, including target-dependent v.

## Matching lower bound and ray attainment

The predecessor immutable source gives an explicit affine inverse at common v* for *every* W in W*+[-H,H]^4, and the twelve affine legality slacks are nonnegative at all sixteen vertices. That already proves the lower bound for the larger target-dependent-v union.

For a self-contained check of the ray endpoint, the adjacent exact checker reconstructs (X0,X1,X2,Ea,Eb,E1) at W* and at W_+(H), verifies every stopped likelihood-ratio mass, positivity, mass first moment, both errors and both stop times. All intermediate 0≤h≤H ray points follow by affine interpolation of continued Q mass and declared-P stopped Q mass at fixed v* and X1=V1. This interpolation preserves the legal seedless LR representation (terminal kernels at j=0,2 are history-independent; the j=1 key fully continues). Hence the ray iff statement holds.

## BRC meaning, evidence and next work

The retained carrier is the stopped-likelihood-ratio mass vector (M_r)_r together with declaration flows (E_r)_r; W is a coarser four-coordinate readout. A **single** observed corner simultaneously saturates two competing BRC capacity laws. The previously open “choose v separately for each W” optimization is resolved exactly within g=u0=1.

\`VERIFY.py\` uses standard Python \`fractions.Fraction\` and checks the coefficient identities, exact crossing, probability normalization, LR moments, and two exact policy witnesses. \`EXACT_OUTPUT.txt\` records its actual run; the all-real argument uses analytic inequalities and the predecessor's full 16-vertex affine certificate. Formal project admission and independent review are outstanding.

**Next discriminating research:** allow g and/or u0 to vary and test the critical ray with h>H. An exact legal seedless-LR realization would break this subfamily ceiling; alternatively derive a global supporting inequality. The independent mother-question route remains the unrestricted four-observer FULL_HIST versus seedless LR comparison via K(W) and F=(A+B)J−X1(αA+βB). No claim of separation for unrestricted LR follows from the present subfamily result.

**Control observation:** GitHub identity awdawmip, repo admin/push true; native status, task-list and session-start returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false. Active R5 owner/CLAIM unconfirmed; no native Result or Review written.
