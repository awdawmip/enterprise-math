# CBRC F7 Driver r460 — exact rational certificate for the whole B=8 input box

Date: 2026-11-22 (Asia/Shanghai). Original F7 scientific author: `EM-CBRCF7-83A1D4`; extension/checker: `EM-DVR-DEBB5E` in a shared, nonblind Driver context. The original frozen `RR-AA38973D56330E59D315` and its formal review status are unchanged. This is a **finite-box mathematical result**, not an accepted Native Result or a global minimax resolution.

## Exact proposition

Keep the original scalar F7 model:
[
A=I+uv^T,qquad u=(1,1,-1,-1)^T,quad v=(1,-2,-1,2)^T,
]
[
q:mathbb Z^2	o[0,infty), q(0,0)=0, q(-x,y)=q(x,y), q(s,0)=1 (s
e0),quad q(x,y)ge1/2 ((x,y)
e(0,0)),
]
with the exact fixed-scale marks (q(2,1)=q(-1,-1)=1/2).
Let
[
D_q(z)=q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)-q(z_1,z_2)-q(z_3,z_4).
]
Define the restricted-input minimax quantity
[
E_B^*=inf_{	ext{all original scalar-admissible }q} max_{zin{-B,ldots,B}^4}|D_q(z)|.
]
Then **the complete input cube with B=8 admits exact minimax error**
[
oxed{E_8^*=1/2.}
]
Consequently (E_B^*=1/2) for every integer (1le Ble8). This does not assert (E_infty=1/2), since the verified inequalities have only a bounded input domain.

## Analytic lower bound

For (z=(-2,1,0,0)), (v^Tz=-4) and (Az=(-6,-3,4,4)). Using evenness, the fixed mark and the nonzero lower bound,
[
D_q(z)=q(6,-3)+q(4,4)-	frac12ge	frac12.
]
Because this z lies in each cube (Bge2), this directly proves (E_B^*ge1/2) for all (Bge2). For (B=1), use (z=(1,-1,0,0)): (v^Tz=3), (Az=(4,2,-3,-3)), and (D_q(z)=q(4,2)+q(3,-3)-1/2ge1/2). Thus the lower bound is valid for every integer (Bge1).

## Explicit rational upper certificate

A globally defined scalar-admissible (q_*) is supplied by the accompanying exact certificate. It assigns:

- (q_*(0,0)=0), and (q_*(s,0)=1) for every nonzero s;
- (q_*(2,1)=q_*(1,-1)=1/2), and (q_*(-x,y)=q_*(x,y));
- (q_*(x,y)=n_{|x|,y}/40) on **524** explicit nondefault non-axis canonical pairs in the published table; on all other non-axis, nonzero pairs, (q_*(x,y)=1/2).

The table uses integer numerators from 21 through 40, hence the global scalar conditions hold exactly, without a bounded-domain definition or floating-point assumptions.

The executable checker reconstructs (Az=(a+k,b+k,c-k,d-k)) for (k=a-2b-c+2d), and exhaustively evaluates **every** of the (17^4=83,521) ordered integer inputs in ([-8,8]^4) using only integer values of (40q_*). It checks (-20le40D_{q_*}(z)le20) at every input and obtains 3,176 saturating inputs, so the maximum is exactly (1/2). This supplies a finite exhaustive proof rather than a floating-point LP indication. The certificate was found using finite sparse LP exploration, but reproducing the proof requires only Python's standard library and integer arithmetic.

The same table and the 83,521 signed inequalities were separately re-evaluated with integer arithmetic in the research session, confirming exactly 524 unique overrides, zero violations, maximum magnitude 20 and 3,176 saturators.

Source checker:
`research_checks/CBRC_F7_R460_BOX8_EXACT_RATIONAL_CERT_20261122.py`
at `e9b3cabec1ce5b46d4a9c23dfe0bd8ce52e8a951`.

## Interpretation and follow-up

This certificate **separates two phenomena**: the r454–r459 exact mixed-witness energy gains are genuine finite-region quadratic coercivity improvements, but they do not by themselves imply an improved global error lower bound. The present complete input-box experiment reaches the inherited (1/2) lower bound through (B=8). A useful next discriminator is to seek exact rational (E_B^*=1/2) certificates at larger B or an explicit finite obstruction (E_B^*>1/2), keeping denominator growth and input coverage visible. Do not infer the stronger global statement from finite checks.

Scientific classification: finite-domain exact exhaustive certificate and exact lower witness; no claim of independent decisive review, formal verification, new Task owner, Native Review/Result acceptance, Task completion or P000 promotion. Original F7 Researcher and prior Driver scientific contributions are preserved.
