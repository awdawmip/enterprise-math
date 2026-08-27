# P022 Composite Franel Equal-Depth Escape — Research Return

Task: `RS-P022-COMPOSITE-FRANEL-EQUAL-DEPTH-ESCAPE`  
Publication: `TP2-E4537008BB8B0CCFF88F`  
Researcher: `EM-P022CE-84B7D1`  
Frozen owner source: `program/p022-geometry-v2@603ef1c72245612359f8b59cab7a492de21a9166`

## Verdict

`P022_COMPOSITE_FRANEL_EQUAL_DEPTH_ESCAPE_CLOSED_OR_MINIMAL_EXCEPTION_FROZEN`

Disposition: **MINIMAL_EXACT_EXCEPTION_FROZEN**.

The surviving composite equal-depth mechanism is not justified as universally impossible. It admits an exact reduction to a strictly smaller arithmetic exceptional set. In the admissible forced-midpoint sector

\[
q=6k-1,\qquad q\equiv5,23\pmod{24},\qquad m=3k-1=\frac{q-1}{2},
\]

the pre-existing escape reduction requires

\[
v_q(F_{2k-1})=v_q(F_m)>0,\qquad v_q(F_{2k})=0.
\]

The smallest exact extra congruence required for this escape is

\[
\boxed{K_k\equiv0\pmod q},\qquad k=\frac{q+1}{6},
\]

where

\[
K_0=0,\qquad K_1=1,
\]

and

\[
\boxed{
K_{d+1}=(28d^2+1)K_d+8(2d-1)^4K_{d-1}.
}
\]

The frozen half-integer companion theorem gives, for the present forced-midpoint primes and offset \(d=k<m\),

\[
\boxed{q\mid F_{2k-1}\iff q\mid K_k.}
\]

Thus every admissible equal-positive-depth escape lies inside the named companion congruence \(q\mid K_{(q+1)/6}\). No owner theorem proving this congruence impossible was found. A finite diagnostic found no witness, but that is deliberately not promoted to an all-prime result.

## 1. Exact midpoint first jet from the harmonic packet

Let

\[
a_j=(-1)^j\frac{\binom{2j}{j}^3}{64^j},\qquad
O_j=H_{2j}-\frac12H_j,
\]

and define in \(\mathbf Z_q\)

\[
\mathcal A_q=\sum_{j=0}^{m}a_j,\qquad
T_q=\sum_{j=0}^{m}a_jO_j,\qquad
U_q=\sum_{j=0}^{m}a_jH_j.
\]

For \(m=(q-1)/2\), termwise expansion gives

\[
\binom mj
\equiv
(-1)^j\frac{\binom{2j}{j}}{4^j}(1-qO_j)
\pmod{q^2}.
\]

Cubing and summing yields the exact first correction

\[
\boxed{F_m\equiv\mathcal A_q-3qT_q\pmod{q^2}.}
\]

The frozen harmonic pairing supplies

\[
\boxed{U_q\equiv2T_q\pmod q.}
\]

Since the forced midpoint has \(q\mid F_m\), the same expansion implies \(q\mid\mathcal A_q\). Put

\[
C_q=\frac{\mathcal A_q}{q}\pmod q,
\qquad
\alpha_q=\frac{F_m}{q}\pmod q.
\]

Then

\[
\boxed{
\alpha_q
\equiv C_q-3T_q
\equiv C_q-\frac32U_q
\pmod q.
}
\]

This is the exact midpoint first jet. In particular,

\[
v_q(F_m)=1\iff\alpha_q\ne0.
\]

No unproved supercongruence \(\mathcal A_q\equiv0\pmod{q^2}\) is assumed; the base quotient \(C_q\) is retained explicitly.

## 2. Exact transport jet at the third index

The frozen midpoint-offset transport can be written

\[
F_{m-d}=A_d(q)F_m+B_d(q)F_{m-1},
\]

with

\[
A_0=1,\ B_0=0,\qquad A_1=0,\ B_1=1,
\]

and for either \(C=A\) or \(C=B\),

\[
8(t-(2d+1))^2C_{d+1}(t)
=(t-(2d-1))^2C_{d-1}(t)
-\bigl(7(t-(2d+1))(t-(2d-1))+8\bigr)C_d(t).
\]

Set

\[
E_d=A_d(0),\qquad G_d=B_d(0),\qquad H_d=B_d'(0).
\]

At \(t=0\), \(E_d,G_d\) obey

\[
8(2d+1)^2C_{d+1}
=(2d-1)^2C_{d-1}-(28d^2+1)C_d.
\]

Differentiating the rational recurrence gives

\[
\boxed{
\begin{aligned}
8(2d+1)^2H_{d+1}
={}&(2d-1)^2H_{d-1}-(28d^2+1)H_d\\
&-2(2d-1)G_{d-1}+28dG_d+16(2d+1)G_{d+1}.
\end{aligned}}
\]

The frozen integer normalization is

\[
\boxed{
K_d=((2d-1)!!)^2(-8)^{d-1}G_d.
}
\]

Consequently, on the exceptional congruence \(q\mid K_k\), \(G_k\in q\mathbf Z_q\). Put

\[
s_k=((2k-1)!!)^2(-8)^{k-1},\qquad
g_q=\frac{G_k}{q}\pmod q.
\]

Because \(s_k\) is a \(q\)-adic unit,

\[
\boxed{
g_q\equiv\frac{K_k}{q}s_k^{-1}\pmod q.}
\]

Let

\[
u_q=F_{m-1}\pmod q.
\]

The frozen consecutive-zero exclusion makes \(u_q\) a unit in the surviving escape setting. Expanding the transport at \(t=q\) gives

\[
A_k(q)\equiv E_k\pmod q,
\qquad
B_k(q)\equiv G_k+qH_k\pmod{q^2}.
\]

Therefore, if \(q\mid K_k\),

\[
\boxed{
\beta_q:=\frac{F_{2k-1}}q
\equiv
J_q:=E_k\alpha_q+(g_q+H_k)u_q
\pmod q.
}
\]

Substituting the midpoint harmonic jet,

\[
\boxed{
J_q
\equiv
E_k\left(C_q-\frac32U_q\right)
+(g_q+H_k)u_q
\pmod q.
}
\]

This is the requested first p-adic correction governing the two positive Franel depths.

## 3. Casoratian guard: the midpoint coefficient does not disappear

Define

\[
X_d=(-8)^dE_d,\qquad Y_d=(-8)^dG_d.
\]

The two basis solutions satisfy the exact Casoratian identity

\[
\boxed{
X_dY_{d+1}-X_{d+1}Y_d
=\frac{(-8)^{d+1}}{(2d+1)^2}.
}
\]

If \(q\mid G_k\), then \(q\mid Y_k\). Applying the Casoratian at \(d=k-1\) shows that \(X_k\), hence \(E_k\), is a \(q\)-adic unit because the right-hand side and its denominator are \(q\)-units. Thus the coefficient of the midpoint first jet in \(J_q\) cannot itself vanish modulo \(q\) merely because the companion congruence holds.

## 4. Exact valuation stratification

Under the minimal exceptional congruence \(q\mid K_k\), the first jets classify the depth-one layer exactly:

\[
\begin{array}{c|c|c}
\alpha_q & J_q & \text{valuation consequence}\\ \hline
\ne0 & \ne0 & v_q(F_m)=v_q(F_{2k-1})=1\\
0 & \ne0 & v_q(F_m)\ge2,\ v_q(F_{2k-1})=1\\
\ne0 & 0 & v_q(F_m)=1,\ v_q(F_{2k-1})\ge2\\
0 & 0 & v_q(F_m),v_q(F_{2k-1})\ge2;\ \text{second jet required}
\end{array}
\]

Hence the first correction does **not** support an unconditional impossibility theorem. It gives a sharper and exact statement:

1. outside \(q\mid K_k\), the composite equal-depth escape is impossible already at the divisibility layer;
2. inside \(q\mid K_k\), if both first jets are nonzero, equal depth \(1\) actually follows;
3. if exactly one first jet vanishes, equality is ruled out;
4. only the double-zero first-jet stratum requires a second p-adic correction.

This is why the correct stopping point is the companion congruence rather than a larger prime cutoff or a generic-independence assertion.

## 5. Reconnection to composite-defect row visibility

The prior forced-midpoint scale identity reduced a surviving composite defect to

\[
v_q(F_{2k-1})-v_q(F_{2k})-v_q(F_m)=0,
\]

and the escape hypotheses reduce this further to

\[
v_q(F_{2k-1})=v_q(F_m)>0,
\qquad v_q(F_{2k})=0.
\]

The half-integer coordinate now inserts the exact gate

\[
\boxed{
q\mid F_{2k-1}
\iff
q\mid K_{(q+1)/6}.
}
\]

Therefore composite-defect row visibility is proved for every admissible prime outside

\[
\boxed{
\mathcal E_K=
\left\{q:\ q\equiv5,23\pmod{24},\ q\text{ prime},\ q\mid K_{(q+1)/6}\right\}.
}
\]

The current owner lineage does not prove \(\mathcal E_K=\varnothing\), and this research execution does not claim it. The universal P022 row-visibility claim must therefore either exclude \(\mathcal E_K\) or discharge the new exact arithmetic frontier \(q\nmid K_{(q+1)/6}\) for all admissible primes.

If an admissible member of \(\mathcal E_K\) is ever found, the packet above immediately decides the depth-one layer using \(\alpha_q,J_q\); only the simultaneous congruences \(\alpha_q=J_q=0\) require a second jet.

## 6. Finite diagnostic — not proof

The independent checker

`python scripts/check_p022_composite_franel_equal_depth_escape.py`

performs exact algebra/regression checks and, separately, a finite diagnostic.

Default result:

```text
EXACT_ALGEBRA=PASS
MIDPOINT_Q2_PACKETS=PASS (16 target-sector primes < 300)
FINITE_DIAGNOSTIC=PASS (564 target-sector primes < 20000; q|K_k witnesses=0)
FINITE_WITNESSES=NONE
FINITE_DIAGNOSTIC_IS_NOT_AN_ALL_PRIME_PROOF=TRUE
```

The scan verifies the frozen bridge \(q\mid F_{2k-1}\iff q\mid K_k\) on the tested target-sector primes and finds no exceptional prime below 20000. It is retained only as regression/evidence and is not used to infer \(\mathcal E_K=\varnothing\).

## Frozen outputs

- `research_returns/P022_COMPOSITE_FRANEL_EQUAL_DEPTH_ESCAPE_RETURN_20260827.md`
- `research_artifacts/P022_COMPOSITE_FRANEL_EQUAL_DEPTH_ESCAPE/equal_depth_reduction.json`
- `scripts/check_p022_composite_franel_equal_depth_escape.py`

## Unresolved residue

Exactly one all-prime arithmetic gate remains before universal closure of this escape channel:

\[
\boxed{
q\nmid K_{(q+1)/6}
\quad\text{for every admissible }q\equiv5,23\pmod{24}.
}
\]

No proof or counterexample to that statement was obtained here. This is a materially smaller frontier than the original equality-of-valuations problem and is an explicit integer recurrence congruence, not a vague p-adic independence assumption.
