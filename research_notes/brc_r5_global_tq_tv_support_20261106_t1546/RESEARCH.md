# R5 — sharp global Q-stopping-time / total-variation envelope and rigidity

Date: 2026-11-06 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Exact scientific source and typed observer

Preserve frozen pins: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. The strictly positive four-stage P/Q finite BRC observer is the one at EM `57f7d654e5dd002567e0b0d333937e6e38f3b4cb` and its predecessor's two-stage hexagon at `712dea22569529fa1785c6a2f94d263fa0d579b1`. No new scientific input replaces the frozen tree. This is an externally typed exact P/Q probability experiment, not a claim about native X6 evolution. It retains stopped-history masses and the joint branch relation until the prescribed observer.

A policy may stop at times 1,2,3,4 using *arbitrary FULL_HIST* history-dependent randomized continuation and declaration. Write (e_Q=Q(\mathrm{declare}\ P)), (e_P=P(\mathrm{declare}\ Q)), (T_Q=E_Q[\tau]), (T_P=E_P[\tau]). Set (D=e_P+e_Q-1). Seedless LR is the subfamily whose continuation and declaration use shared likelihood-ratio keys.

## Theorem: all-policy sharp support and exact equality faces

For **every real randomized FULL_HIST policy** in the frozen four-stage experiment, hence every seedless LR policy,
[
 \boxed{ |e_P+e_Q-1|\le (T_Q-1)/8.}
]
Here (1\le T_Q\le4). For each real (s\in[0,1]) with (T_Q=1+s\in[1,2]), both signs of the bound are attained by genuine seedless LR policies with (T_P=T_Q=1+s). In fact the whole scalar support interval ([-s/8,s/8]) is attained by seedless LR policies at those two stopping times.

The equality cases are rigid: for (s>0), if a FULL_HIST policy has (T_Q=1+s\le2) and (|D|=s/8), then (g=s), (u_0=u_1=X_0=X_1=X_2=0), and (T_P=T_Q). For (D=+s/8), the time-2 ratio (3/4) declares P surely and ratio (5/4) declares P never; for (D=-s/8) these decisions reverse. The ratio-1 time-1 declaration remains free. Thus the exact upper/lower exposed faces of the four-observer image at (T_Q=1+s) are
[
\boxed{(e_P,e_Q,T_P,T_Q)=
(1\pm s/8-q,\ q,\ 1+s,\ 1+s),\quad
s/2\le q\le1-s/2,}
]
where the sign is the sign of (D). At (s=0), both faces coincide: ((1-q,q,1,1)), (q\in[0,1]). This describes the complete equality faces even among unrestricted history-aware policies.

In particular, on the earlier fiber (T_P=T_Q=15/8), the entire FULL_HIST image satisfies (57/64\le e_P+e_Q\le71/64); the extreme lines are already attained by the previous seedless LR two-stage hexagon. This strengthens the prior *fixed-family* support bound to a **global four-stage all-policy support bound**.

## Proof: explicit BRC positive residual certificate

Let (g\in[0,1]) be Q mass continued from time 1, and (u_i\in[0,g]) the continued Q mass along each of the two time-2 branches, scaled such that their actual masses are (u_i/2). For each time-3 key (j\in\{0,1,2\}), let (x_{ij}\ge0) be the *actual Q mass* continued from the time-2 branch (i), with capacity (0\le x_{ij}\le u_i q_{3,i,j}/2). Set (X_j=x_{0j}+x_{1j}), (V_j=\sum_i u_iq_{3,i,j}/2). The frozen Q transition rows are
[
 q_{3,0}=(13/20,1/5,3/20),\qquad
 q_{3,1}=(1/40,9/20,21/40).
]
Consequently (V_1=u_0/10+9u_1/40). The Q time-4 leftmost-ratio coefficient from central key (j=1) is
[
 J=\alpha x_{01}+\beta x_{11},\quad \alpha=47/180,\quad\beta=67/162>\alpha,
]
so (\beta X_1-J=(\beta-\alpha)x_{01}\ge0). In FULL_HIST (J) need not be a function of (X_1) alone; the formula retains precisely the hidden-history contribution.

The seven terminal Q stopped-ratio masses (M_r), in order (r=1/10,1/2,3/4,1,5/4,3/2,19/10), are
[
\begin{aligned}
 M_{1/10}&=(509X_0+9X_2)/900+J,\\
 M_{1/2}&=V_0-X_0,\\
 M_{3/4}&=(g-u_0)/2,\\
 M_{1}&=1-g+V_1+(382/900)(X_0+X_2)-2J,\\
 M_{5/4}&=(g-u_1)/2,\\
 M_{3/2}&=V_2-X_2,\\
 M_{19/10}&=(9X_0+509X_2)/900+J.
\end{aligned}
]
These sum to 1 and have first LR moment 1. By the definition of the sequential Q time observer,
[
 T_Q-1=g+(u_0+u_1)/2+X_0+X_1+X_2.
]
Define the stopped-history total-variation support
[
 S:=\sum_{r<1}(1-r)M_r
 =\frac g8+\frac{3u_0}{80}+\frac{u_1}{160}
   +\frac9{1000}(X_0+X_2)+\frac9{10}J.
]
For any history-dependent declaration probabilities (t_h\in[0,1]), with each stopped history carrying likelihood ratio (r_h), the exact observer satisfies
(D=\sum_h(1-r_h)Q(h)t_h). Because (\sum_h(1-r_h)Q(h)=0), it follows that (-S\le D\le S), even if distinct histories have identical ratios but different declarations.

The following **sum-of-nonnegative-residuals identity** is exact:
[
\boxed{
 \frac{T_Q-1}{8}-S=
 \frac{u_0}{3600}+\frac{u_1}{1600}
 +\frac{29}{250}(X_0+X_2)
 +\frac{89}{360}(V_1-X_1)
 +\frac9{10}(\beta X_1-J).}
]
Each term is nonnegative by an actual probability-capacity or branch-identity constraint. Therefore (|D|\le S\le(T_Q-1)/8). The strictly positive coefficients on (u_0,u_1) imply that equality requires (u_0=u_1=0), whence (X_j=0) and (g=T_Q-1), (T_P=T_Q). At (g=s>0), the two positive non-unit stopped-ratio masses are (M_{3/4}=M_{5/4}=s/2); saturation forces exactly the two indicator declarations described above. Letting the time-1 ratio-1 declaration probability range over ([0,1]) yields (q=s/2+(1-s)t_1\in[s/2,1-s/2]), proving completeness of the equality faces. For the interior scalar support interval choose (t_{3/4}=(1+z)/2), (t_{5/4}=(1-z)/2), (t_1=1/2) for (z\in[-1,1]), giving (D=sz/8) exactly. QED.

## Exact computation and evidentiary scope

The included `VERIFY.py` was executed using Python standard-library `fractions.Fraction`. It checks positivity and likelihood-ratio conditional means of every frozen kernel, normalized stopped masses and first moment, both forms of S, the exact residual identity, all-policy support at extreme declarations, and sharp seedless-LR constructions. The declared finite grid has 19,683 history-dependent stopping-flow combinations (3 choices for g, 3 for each time-2 continued fraction, 3 for each of six time-3 continued fractions), plus 30 exact sharp-family checks. The **universal real theorem** follows from the symbolic identity and inequalities, not from finite enumeration. Console stdout is in `EXACT_OUTPUT.txt`.

No full global R5 observable-image equality or strict separation is asserted. No formal task claim, independent Driver review or mathematical admission was obtained in this author-side step. Source of predecessor: [two-stage hexagon commit](https://github.com/awdawmip/enterprise-math/commit/712dea22569529fa1785c6a2f94d263fa0d579b1).

## Next discriminating unit

At (T_Q=15/8), consider rational FULL_HIST points with (57/64<e_P+e_Q<71/64) (strict slack of this globally exact envelope) and (T_P\ne T_Q) or interior (T_P=T_Q). Search for points outside the prior seedless-LR two-stage hexagon, then test **all** LR stopping flows via the full seven-variable K(W) quadratic residual. A point outside the two-stage hexagon alone is not global LR separation. Preserve the immutable R5 source pins and existing review/owner boundaries.
