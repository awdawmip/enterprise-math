# D25 — Reflected R_p restored and a D-finite kernel / Hasse constant-term bridge

Date: 2026-11-08 (Asia/Hong_Kong). Role: TASK_RESEARCH author-side portable, REGISTER_PENDING; UNREVIEWED / NOT_ADMITTED. Research logical lane: chatgpt-research-hourly-enterprise-math-20260923. Exclude maintenance lane chatgpt-hourly-enterprise-math-20260921.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Accepted D24 UR/JT0 is input; D25 LIFT remains open. No source native checkpoint, CLAIM, OPEN or Result is claimed.

## Frozen reflected R_p recovered from an authoritative predecessor

Source: research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_RETURN_20260827.md §2, verified Git blob cf36004694dc2c8c9134e2e1e989c076b88e4c03; original parent formula:

For p=6m+1 prime, define
\[
B_i=\frac{(1/6)_i(1/3)_i}{(i!)^2\,2^i},\quad
C_r=\frac{2^{r-1}(r-1)!^2}{18(5/6)_r(2/3)_r}.
\]
\[
\boxed{R_p=2\sum_{i=1}^{m}B_i
\sum_{r=1}^{i}(1+6(i-r))C_r\pmod p.}
\]
The current D25 scalar is \(\Delta_p=((g/p)h-1)/p\bmod p\), where
\(g=\sum_{i=0}^{p-1}B_i\), \(h=\sum_{i=0}^{p-1}(12i+1)B_i\).
This is the actual frozen R_p input: it is computed independently, never set equal to a measured Delta.

## Proved universal reflected-kernel lemma

Write \(D=t\,d/dt\), \(F(t)=\sum_{r\ge1}C_rt^r\in\mathbb Q[[t]]\). Directly from the exact factorial quotient,
\[
C_1=1/10,\qquad
\frac{C_{r+1}}{C_r}=\frac{36r^2}{(6r+5)(3r+2)}\quad(r\ge1).
\]
Consequently
\[
\boxed{\big[(6D-1)(3D-1)-36tD^2\big]F(t)=t.}\tag{KERNEL-ODE}
\]
Proof is coefficientwise: the degree-one coefficient is \(10C_1=1\); for every \(n\ge2\), the coefficient is
\((6n-1)(3n-1)C_n-36(n-1)^2C_{n-1}=0\).
The constant term is zero, and the recurrence with \(F(0)=0\) gives a unique formal power series. No p-specific assumption enters this lemma.

Define
\[
K(t)=F(t)\frac{1+5t}{(1-t)^2},\qquad
[t^i]K(t)=\sum_{r=1}^i(1+6(i-r))C_r.
\]
For i≤m, the exact p-adic parameter lift
\((1/6,1/3)=(-m+p/6,-2m+p/3)\) yields
\[
B_i\equiv\binom mi\binom{2m}{i}2^{-i}\pmod p.
\]
Set \(Q_m(z)=\sum_{i=0}^m\binom mi\binom{2m}{i}z^i\).
Taking the Laurent constant term proves the exact frozen-source identity
\[
\boxed{R_p\equiv2\operatorname{CT}_t
\left[Q_m\!\left(\frac1{2t}\right)\frac{1+5t}{(1-t)^2}F(t)\right]\pmod p.}\tag{D25-R-CT}
\]
Indeed, expand \(Q_m(1/(2t))\), and the constant coefficient pairs index i of Q with index i of K. Only indices 1≤i≤m enter and all denominators are p-units. This is a fixed D-finite kernel and a finite Hasse-polynomial pairing. It is a new representation of previously known R_p, not a proof of LIFT or a complexity improvement over the existing linear-time reflected-sum routine.

A finite recurrence for the inner coefficient is \(U_0=S_0=0\), \(U_i=U_{i-1}+C_i\), \(S_i=S_{i-1}+C_i+6U_{i-1}\); it gives \([t^i]K=S_i\).

## Direct native-observer comparison using preserved source ports

The previous author-side exact Gauss expansion at x=1/2 yielded
\[
\Delta_p\equiv D_0+D_S+D_H\pmod p,\quad
D_0=(ZH_0-1)/p,\quad D_S=SH_0,\quad D_H=ZH_1.
\]
Here Z, S, H0, H1 carry the original rational p-adic lifts and first/second source strata; the operator order and division by p are preserved. Independently compute (a) the raw original p-term weighted B recurrence modulo p^3; (b) R_p from the original reflected double sum; (c) R_p from (D25-R-CT). The results are:

| p | D0 | DS | DH | Delta | R direct/CT | Delta-R |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 0 | 9 | 4 | 0 | 0 | 0 |
| 19 | 16 | 11 | 4 | 12 | 12 | 0 |
| 43 | 16 | 0 | 42 | 15 | 15 | 0 |
| 67 | 41 | 27 | 20 | 21 | 21 | 0 |
| 373 | 81 | 12 | 103 | 196 | 196 | 0 |

All values are reduced modulo their respective primes. A standalone standard-library checker confirms Delta=R_direct=R_CT for every 166 primes p<5000 in p=13,19 (mod 24), 83 primes in each class. A separate rational exact check establishes the reflected kernel coefficient recurrence for m=1 through 8. These are finite regressions, not universal LIFT proof. The external p373 check is not the native H0/B0/DP/Hesse-kappa experiment #1559.

## Exact next research interface

The formerly missing R input is now source-resolved. The unsolved original LIFT becomes the fully explicit target
\[
\boxed{\frac{ZH_0-1}{p}+SH_0+ZH_1
\equiv2\operatorname{CT}_t
\left[Q_m\!\left(\frac1{2t}\right)\frac{1+5t}{(1-t)^2}F(t)\right]\pmod p.}\tag{D25-GREEN-PAIRING-TARGET}
\]
Find a valid source-preserving finite Green–Wronskian / creative-telescoping certificate matching the two sides, including the divided ZH0 lift and cutoff-sensitive Phi_xx. This candidate route is not asserted as necessary for every possible proof. Reuse the pinned native September checkpoint and its actual completed_units (do not rewrite its immutable frontier).

Read-only native status at this run: BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE, operation_sent=false; original same-lane request IDs em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 read WAITING_RESOURCE/EVENT_COLLECTION_IO. Keep protected old session/staging UNKNOWN_PRESERVE, no duplicate native mutation. Recovery issue #1558.