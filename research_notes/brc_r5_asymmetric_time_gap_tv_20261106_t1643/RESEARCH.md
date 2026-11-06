# R5 — Sharp asymmetric time-gap total-variation support theorem

Date: 2026-11-06, Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Scientific input and observer scope

Preserve frozen science pins GLOBAL a01383f825ef9d43b4b754254303298c64041568, EM 86149263e38c22292c9def1e0f69092efa1be77e. Continue the verified four-stage strictly positive P/Q tree (delta=1/4) and the global support theorem at 0a9e9066ee947a6410ed4b4601cdc9d419d0c90b; the probability tree provenance is recorded there. Current behavioral rules were read separately at canonical main. This finite P/Q branch observer is an externally typed mathematical test, not native X6 spatial evolution.

In the exact four-stage model, FULL_HIST policies may use arbitrary real history-conditioned stopping and declarations; seedless LR policies share every repeated likelihood-ratio decision key. Observations are e_Q=Q(declare P), e_P=P(declare Q), T_i=E_i[tau], i=P,Q. Set D=e_P+e_Q-1.

## Theorem — globally sharp asymmetric penalties

For every FULL_HIST (and therefore every seedless LR) real randomized policy of the frozen four-stage experiment,

$$
\boxed{\left|e_P+e_Q-1\right|\le
\frac{T_Q-1}{8}-\frac1{200}(T_P-T_Q)_+
-\frac{14}{125}(T_Q-T_P)_+,\qquad y_+=\max\{y,0\}.}
$$

Both positive coefficients are sharp in their respective time-gap signs, already among seedless LR policies. This sharp support refines the predecessor's |D| <= (T_Q-1)/8 and gives a new globally valid necessary condition on all four observer coordinates.

## Explicit proof by nonnegative capacity slacks

Write Q time-1 continued mass g (0<=g<=1), time-2 continued Q mass u_i/2 for branches i=0,1 (0<=u_i<=g). Frozen Q time-3 rows:

$$
q_{3,0}=(13/20,1/5,3/20),\quad q_{3,1}=(1/40,9/20,21/40).
$$

Let x_ij be the actual continued Q mass from time-3 history (i,j), with 0<=x_ij<=u_i q_{3,i,j}/2. Define X_j=x_0j+x_1j and the retained history parameter J=(47/180)x_01+(67/162)x_11. The stopped Q likelihood-ratio masses M_r in the predecessor give the total variation support

$$
S=\sum_{r<1}(1-r)M_r
 =g/8+3u_0/80+u_1/160+(9/1000)(X_0+X_2)+(9/10)J.
$$

The time observers, without discarding any source history, are

$$
T_Q-1=g+(u_0+u_1)/2+X_0+X_1+X_2,
$$
$$
T_P-1=g+(3u_0+5u_1)/8+X_0/2+X_1+3X_2/2.
$$

Thus d=T_P-T_Q=(u_1-u_0)/8+(X_2-X_0)/2. Introduce genuine nonnegative residual capacities

$$
a=u_0/10-x_{01}\ge0,\qquad b=9u_1/40-x_{11}\ge0.
$$

Set G=(T_Q-1)/8-S. Exact rational substitution gives

$$
G=\frac7{500}u_0+\frac1{1600}u_1+
\frac{29}{250}(X_0+X_2)+\frac{11}{100}a+\frac{89}{360}b.
$$

The two exact signed nonnegative certificates are

$$
\boxed{
G-\frac d{200}=\frac{117}{8000}u_0+
\frac{237}{2000}X_0+\frac{227}{2000}X_2+
\frac{11}{100}a+\frac{89}{360}b\ge0,
}
$$

$$
\boxed{
G+\frac{14}{125}d=\frac{117}{8000}u_1+
\frac3{50}X_0+\frac{43}{250}X_2+
\frac{11}{100}a+\frac{89}{360}b\ge0.
}
$$

For every history-dependent declaration, D=sum_h(1-r_h)Q(h)t_h with 0<=t_h<=1. Since sum_h(1-r_h)Q(h)=0, the sharp fixed-flow range is -S<=D<=S. Combining both signed certificates yields the displayed theorem on the entire real admissible FULL_HIST policy class. The proof does not rely on a finite grid or on convexity of the LR observable image.

## Optimality witnesses and equality structure

For d>0, the first certificate is saturated when u_0=X_0=X_2=a=b=0, allowing 0<u_1<=g<=1, x_11=9u_1/40 and every other x_ij=0. Choose g=u_1=1. The exact values are

$$
(T_Q,T_P,S,G,d)=(109/40,\ 57/20,\ 43/200,\ 1/1600,\ 1/8).
$$

For d<0, the second certificate is saturated when u_1=X_0=X_2=a=b=0, allowing 0<u_0<=g<=1, x_01=u_0/10 and every other x_ij=0. Choose g=u_0=1. Then

$$
(T_Q,T_P,S,G,d)=(13/5,\ 99/40,\ 93/500,\ 7/500,\ -1/8).
$$

In each of these two concrete policies, declare P at every stopped likelihood ratio r<1, and declare Q at r>=1. This single likelihood-ratio threshold declaration attains D=S. The stopping decisions also depend only on the current likelihood-ratio key within the frozen tree, so these are genuine seedless LR witnesses. Their nonzero d and exact equality prove the optimality of both coefficients in the stated sense.

## Verification and the next research unit

The accompanying VERIFY.py was actually run with standard-library fractions.Fraction. It checks the seven stopped-ratio masses, Q normalization and P/Q likelihood-ratio first moment, the two time formulas, both nonnegative certificates, 512 encoded deterministic stopping policies, 2,000 additional interior rational policies, and both sharpness witnesses with exact declaration errors. EXACT_OUTPUT.txt records actual stdout. The theorem for all real policies is proved by the displayed identities.

Use this support to reject time-asymmetric candidate W before constructing the full LR seven-variable K(W); then choose a rational FULL_HIST point **inside** the new support region and attempt full real LR residual-sign infeasibility or an exact reconstruction. The theorem does not claim to characterize the complete four-dimensional observable image. Native owner/CLAIM/independent review are separate control operations; this is a portable author-side result.
