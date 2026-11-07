# D25 — Exact Fricke tangent parity exchange at the conjugate CM fibers

Date: 2026-11-08 (Asia/Hong_Kong). **TASK_RESEARCH author-side exact algebraic theorem PROVED; symbolic checker executed; UNREVIEWED / NOT_ADMITTED.** Mother Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical lane `chatgpt-research-onhour-enterprise-math-20260923`. This is an external Fricke/CM field calculation, not the native original-class H0/B0 experiment.

## Input and proven tangent calculation

Reuse the previously proved Fricke 6:8 rational maps, without re-proving the global analytic correspondence:

[
z(t)=\frac{108t^2(t+9)(t+8)^2}{(t+12)^6},\qquad
w(t)=\frac{256t^3(t+8)(t+9)^3}{(t^2+36t+216)^4}.
]

Let `s²=2` and `t_e=e 6s` for `e=±1`. Direct substitution and differentiation over `Q(s)` give the exact identities

[
z(t_e)=\tfrac12,\qquad w(t_e)=\tfrac19,
\qquad z'(t_e)=-1+e\frac{3s}{4},
\qquad w'(t_e)=\frac49-e\frac{8s}{27}.
]

As `Norm(z'(t_e))=-1/8` and `Norm(w'(t_e))=16/729`, neither derivative vanishes at any odd residue characteristic `p>3`. Dividing **exactly before reduction** yields

[
\boxed{\frac{dw}{dz}(t_e)=e\frac{8s}{27}.}
]

Proof: quotient of the displayed rational derivatives, with `s²=2`. Both conjugate fibers were checked independently by exact SymPy symbolic differentiation. This is a local differential identity, not the global p-adic Frobenius-lift transport.

## Finite-field Frobenius parity and two-coordinate matrix

For any prime `p≡13,19 mod24`, `2` is a nonsquare and `s^p=-s` in `F_{p²}`. Write a tangent increment of the original **external** z-coordinate as `δz=x+ys`, `x,y∈F_p`. The corresponding tangent increment in w is

[
\delta w=e\frac{8s}{27}\delta z
=e\left(\frac{16y}{27}+\frac{8x}{27}s\right).
]

Thus, in the declared basis `(1,s)`, the **exact invertible** tangent matrix is

[
\boxed{
M_e=e
\begin{pmatrix}
0&16/27\\
8/27&0
\end{pmatrix},\quad
M_e^2=\frac{128}{729}I,\quad
\det M_e=-\frac{128}{729}\ne0\ \text{in }F_p.
}
]

It exchanges the Frobenius-even and Frobenius-odd one-dimensional summands. If both `δz` and `δw` must be Fp-rational, the only tangent pair is zero. This is a precise obstruction to a **same-rational-scalar tangent** identification at this CM fiber, and a constructive prescription to retain the odd coefficient: two Fp components are needed in the local transfer. It is NOT an impossibility theorem for Cartier or Dwork transport, which can involve Frobenius semilinearity and additional p-adic correction terms.

At the positive fiber e=+1, exact matrix reductions are:
* p=13: `[[0,3],[8,0]]`, square `11 I`.
* p=19: `[[0,2],[1,0]]`, square `2 I`.
* p=373: `[[0,194],[97,0]]`, square `168 I`.

The negative fiber multiplies M by minus one. The preceding source-typed p-adic three-port decomposition `C_p/s^epsilon=R_Q+R_L+R_T` remains intact. Its 13-class odd signed component is now geometrically compatible with the Fricke tangent parity exchange, but **no identification of the tangent matrix with the desired p-adic first-lift operator has been proved**. The target `C_p=0` for all primes remains OPEN.

## Next exact action

Build a first-order Frobenius–Cartier *covariant* transport in the two-component basis (1,s), with Hasse quotient q, low parameter derivative L, and single-zero crossing tail T as three independent source ports; test algebraically whether its semilinear normalization removes the p=373 observed (4,322,47) residual triple and then prove the family identity. Do not infer the native original-class H0/B0 coefficient, divided-power rank, eta or Hesse kappa from this external tangent matrix. Original native p=373 evidence remains pending in https://github.com/awdawmip/enterprise-math/issues/1559.

Native original request `onhour11-20261106-1400-exact-research-lane-continuation` was read as RUNNING / REVALIDATING, not replayed. No new native Source claim/session/run or scheduler changes. Source-proof level: AUTHOR_SIDE_PROVED; not reviewed/admitted.
