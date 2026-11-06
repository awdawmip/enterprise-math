# R5: a sharp rational square on the interior time fiber (two-key LR section)

Date: 2026-11-06 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Source and exact scope
Frozen scientific inputs remain GLOBAL `a01383f825ef9d43b4b754254303298c64041568` and EM `86149263e38c22292c9def1e0f69092efa1be77e`. Reuse the exact positive `delta=1/4` P/Q tree, stop-mass formula and single quadratic LR gate of EM commit `57f7d654e5dd002567e0b0d333937e6e38f3b4cb`; the previously proved full four-dimensional LR cube of radius `1/52` is in EM `993818cfa2c4139a6cf22b02bb6887c504da4f01`. This is a finite likelihood-ratio/BRC observer, not a native X6 dynamical claim.

**Theorem (all real square).** At the fixed interior stop-time pair `(T_P,T_Q)=(15/8,15/8)`, every real
$
(e_P,e_Q)=(1/2+c,1/2+d),\q\quad |c|,|d| \le h_*=\frac{287903}{10672000}
$
has an explicit genuine seedless LR stopping/declaration policy in the frozen model. Thus the entire closed two-dimensional square in this four-dimensional time fiber is in both `O4(LR)` and `O4(FULL_HIST)`. Its half-side is `3742739/2668000` times the half-side of the previous full four-cube when restricted to the same time fiber (approximately 40.28% larger).

**Restricted-family sharpness.** In the family of *fixed continuation flows* with `u_1=(13/10)u_0`, fixed `T_P=T_Q=15/8`, shared LR time-3 continuation, and all stopped-ratio declarations fixed to `1/2` except the two extreme ratios `1/10,19/10`, the largest symmetric error square centered at `(1/2,1/2)` has half-side exactly `h_*`. This is an optimum within the stated family, not the optimum over all LR policies or all fixed-time fibers.

## Exact universal policy
Use the inherited time-2/3/4 kernels, and set
$
g=91/276,\quad u_0=35/138,\quad u_1=91/276,\quad
(X_0,X_1,X_2)=(637/7360,1099/11040,497/7360).
$
Here `u_i=g a_i`, and `X_j` is the pooled Q time-3 continued mass. The capacities are
$
(V_0,V_1,V_2)=(637/7360,1099/11040,777/7360).
$
All flows are legal (`0 \le u_i \le g \le 1;0 \le X_j \le V_j`). Define the time-1 continuation probability `g`, the time-2 continuation probability `u_i/g`, and the time-3 *shared-ratio* continuation `X_j/V_j`. At the central ratio `j=1`, `A=u_0/10, B=9u_1/40`, so `k=(alpha A+beta B)/(A+B)=353/942` and `J=k X_1`. Consequently `F=(A+B)J-X_1(alpha A+beta B)=0` exactly.

The seven Q stopped-ratio masses (in ratio order `1/10,1/2,3/4,1,5/4,3/2,19/10`) are
$
(287903/3312000, 0, 7/184, 1259597/1656000, 0, 7/184, 84301/1104000).
$
They are nonnegative, have total mass and first LR moment both exactly 1, and produce `T_P=T_Q=15/8`.

Put `m_-=M_{1/10}=287903/3312000;m_+=M_{19/10}=84301/1104000`. For any *real* `|c|,|d| \le h_*`, declare P with the two extreme-key probabilities
$
t_-=1/2+\frac{10c+19d}{18m_-},
\qquad
t_+=1/2-\frac{10c+d}{18m_+},
$
and `t_r=1/2` at every other stopped-ratio key. All occurrences of a ratio share the same declaration probability, including across distinct histories/time stages. The exact mass margins are
$
m_-=\frac{29h_*}{9},\qquad
m_+-\frac{11h_*}{9}=\frac{2083627}{48024000}>0.
$
Hence `0 \le t_-,t_+ \le 1` for the *entire real closed square*, because `|10c+19d| \le 29h_*` and `|10c+d| \le 11h_*`. All other declarations are `1/2`.

Writing `s_-=t_--1/2;s_+=t_+-1/2`, the changes in errors are `d=m_-s_-+m_+s_+` and `-c=(1/10)m_-s_-+(19/10)m_+s_+`. The displayed inverse formulas solve this exact 2x2 system. Therefore `e_P=1/2+c` and `e_Q=1/2+d` without approximation.

## Exact optimality certificate within the fixed family
Any flow in the stated family has variables `x=(g,u,X_0,X_1,X_2,h)`, `u_0=u`, `u_1=13u/10`, `k=353/942`, time equalities
$
E_Q:=g+\frac{23}{20}u+X_0+X_1+X_2=\frac78,
$
$
E_P:=g+\frac{19}{16}u+\frac12 X_0+X_1+\frac32 X_2=\frac78.
$
Because only the two extreme declaration keys vary and all other declarations are `1/2`, coverage of *all four corners* `(c,d)=(\pm h,\pm h)` requires `M_- \ge 29h/9`. The flow also obeys
$
C_1=\frac{13}{10}u-g \le 0,\quad
C_2=X_0-\frac{273}{800}u \le 0,\quad
C_3=X_1-\frac{157}{400}u \le 0,\quad
C_4=\frac{29}{9}h-\frac{509X_0+9X_2}{900}-\frac{353}{942}X_1 \le 0.
$
The following exact **linear identity in all six variables** is a dual certificate:
$
h=\frac{41129}{1334000}C_1+
\frac{78011}{667000}C_2+
\frac{17899747}{209438000}C_3+
\frac9{29}C_4+
\frac{115107}{1334000}E_Q-
\frac{36989}{667000}E_P.
$
All four multipliers of `C_i` are nonnegative; hence
$
h \le\frac78\left(\frac{115107}{1334000}-\frac{36989}{667000}ight)=\frac{287903}{10672000}=h_*.
$
The displayed policy attains this bound and satisfies both extreme mass bounds, proving sharpness in the stated restricted family. The certificate covers arbitrary *real* flow variables and square targets.

## Verification, observer scope and next question
`VERIFY.py` was actually run using Python standard-library `fractions.Fraction`: checks the exact kernels/flow, seven stopped-ratio masses and first moment, time equalities, inverse at the four error-square vertices, exact optimum and the six-coefficient dual identity. Actual stdout is preserved in `EXACT_OUTPUT.txt`. Universal real-square coverage and optimality are proved by the displayed identities/linear constraints; checking only four vertices is legitimate because the inverse declaration probabilities are affine in `(c,d)`.

This is a BRC-relevant lossless *observer section*: the compressed continued masses and shared declaration keys reconstruct the intended four observables on the stated fiber, while the inherited full-history coefficient `J` remains the explicit residual variable for the unsolved global R5 problem.

**Next discriminating unit:** On the same time fiber, choose a rational `W` just outside this sharp *restricted-family* square with `e_P+e_Q \ne 1`; solve the full six-variable FULL linear feasibility system, then the entire seven-variable `K(W)` quadratic sign interval, *allowing all flows and all declaration keys*. A fixed-flow dual certificate alone is not a global image-separation witness. Keep frozen science pins and independent mathematical admission unchanged.

## Provenance
GitHub research notes: EM `57f7d654e5dd002567e0b0d333937e6e38f3b4cb`, EM `993818cfa2c4139a6cf22b02bb6887c504da4f01`. Global rules read from `awdawmip/chatgpt-global-knowledge` canonical main 2026-11-06; P000 startup projection verified against canonical P000 blob. Current GitHub actor `awdawmip`. Enterprise Math native `session_start` request `r5-20261106-1341-research5-session` returned `FAILED: Error` when read back; `dispatch` request `r5-20261106-1341-dispatch` was still RUNNING at that observation. Native registration/active owner/CLAIM therefore remain to be reconciled, and this artifact is author-side research, not an admitted Result.
