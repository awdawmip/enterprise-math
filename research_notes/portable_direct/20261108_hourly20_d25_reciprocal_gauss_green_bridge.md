# D25 — Reciprocal Hasse and reflected kernel share a Gauss operator; exact Green–Wronskian defect

Date: 2026-11-08 (Asia/Hong_Kong). TASK_RESEARCH author-side portable; lane chatgpt-research-hourly-enterprise-math-20260923 (not maintenance). UNREVIEWED / NOT_ADMITTED; REGISTER_PENDING. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3.

Consumes the same-run source-verified reflected R_p kernel and Hasse pairing, Enterprise Math commit a9a7f32a386cc97030bb0e6361d9cc4f3d41d5e5. This unit advances the next differential interface instead of recomputing finite R_p.

## 1. Exact reciprocal Gauss defect (proved over Q for all positive integers m)

Let P=6m+1 (no primality hypothesis), and use the frozen terminating Hasse polynomial
\[
Q_m(z)=\sum_{i=0}^m\binom mi\binom{2m}i z^i,\qquad
W_m(t)=Q_m\!\left(\frac1{2t}\right).
\]
Let D=t d/dt and
\[
\mathcal L=(6D-1)(3D-1)-36tD^2
=18(1-2t)D^2-9D+1.
\]
Then the following identity is exact in Q[t,t^{-1}]:
\[
\boxed{\mathcal L W_m=-P(9D-2)W_m-P^2W_m.}\tag{RECIPROCAL-GAUSS}
\]

Proof. Coefficient recurrence for Q gives its exact differential equation
\[
D_z^2 Q_m-z(D_z-m)(D_z-2m)Q_m=0.
\]
With z=1/(2t), D_z=-D, hence
\[
36tD^2W_m=18(D+m)(D+2m)W_m.
\]
Use 6m=P-1 to rewrite
\[
18(D+m)(D+2m)=(6D+P-1)(3D+P-1)
=(6D-1)(3D-1)+P(9D-2)+P^2.
\]
Substituting yields the boxed identity. No numerical regression or conjectural premise is used.

For any prime p=P, Q has 2-power denominators, so reduction is defined. It follows that
\[
\boxed{\mathcal L W_m\equiv0\pmod p.}\tag{RECIPROCAL-MOD-P}
\]
This is an exact common-operator statement: the earlier universal reflected kernel F(t)=sum C_r t^r satisfies \(\mathcal L F=t\) over Q[[t]], while the reciprocal finite Hasse polynomial is a homogeneous solution modulo p. The two were previously only linked by a constant-term pairing for R_p.

## 2. Source-preserving Green–Wronskian equation (proved)

Define the formal Laurent-series Wronskian
\[
J_m(t)=W_m(t)\,DF(t)-F(t)\,DW_m(t).
\]
The product rule gives \(DJ_m=W_mD^2F-FD^2W_m\). Consequently
\[
W_m\mathcal LF-F\mathcal LW_m
=18(1-2t)DJ_m-9J_m.
\]
Using \(\mathcal LF=t\) and the exact reciprocal defect above,
\[
\boxed{18(1-2t)DJ_m-9J_m
=tW_m+P\,F(9D-2)W_m+P^2FW_m.}\tag{D25-GREEN-DEFECT}
\]
This equality is exact in Q((t)) and retains the full first- and second-order P-defect. For p=P prime it yields a homogeneous-vs-forced solution pairing modulo p **only on coefficient ranges with p-unit denominators**. The original reflected R_p still equals
\[
2\operatorname{CT}\left(W_m(t)\frac{1+5t}{(1-t)^2}F(t)\right)\pmod p,
\]
requiring only the first m kernel coefficients, all of which have p-unit denominators.

## 3. Exact validation and remaining target

An independent Python Fraction/Laurent-polynomial checker verifies RECIPROCAL-GAUSS for m=1,2,3,7,11,62 (P=7,13,19,43,67,373), and verifies that D25-GREEN-DEFECT holds through Laurent degree 9 when F is truncated after degree m+9. It separately checks that \(\mathcal LF=t\) at every computed coefficient through that cutoff. The verification is arithmetic regression; both boxed identities already have full algebraic proofs. The truncation produces its first omitted forcing term at t^(m+10); multiplication by W_m shifts this down no farther than t^10.

The new scientific opportunity is concrete: find a valid finite adjoint or Green boundary identity converting the **specific weight** (1+5t)/(1-t)^2 in the reflected constant-term pairing into the left p-adic Gauss ports (ZH0-1)/p+SH0+ZH1, retaining their rational lifts and cutoff Phi_xx. The displayed Green defect supplies an exact operator match and a p-order defect to test. It does not establish the final all-prime D25 LIFT. Alternative avenues remain open; do not treat this adjoint route as a required universal method.

Original native research requests em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 remain protected and pending in earlier receipt. Native status this run returned BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE, operation_sent=false. No native Researcher session/CLAIM/OPEN/checkpoint, Result or review is asserted. Restore through #1558; separate native p373 benchmark #1559 remains open.