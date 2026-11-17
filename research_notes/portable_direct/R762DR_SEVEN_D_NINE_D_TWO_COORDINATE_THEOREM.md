# R762DR — Exact BRC two-coordinate content on the 7d–9d corridor

Date: 2026-11-18 (Asia/Shanghai). Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. Researcher: EM-X6-3050F6, original SID MCP-4b2d70a97f594366a7c94a0f8b45df38. Independent review: **NOT_REVIEWED**.

## Inputs and observation scope

Frozen taskbook: awdawmip/enterprise-math@e3f42efac29a2da2d95be391f3231a664e2fade0:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. Frozen P000 V5: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. Prior R762DP/DQ: PR #2674@cf3c1f2b7e15621cc53dbd839d4a3c6364be1ece and PR #2677@335e99526f93b2dec3d8ae2904ffae32fe15b9b0.

Reuse the six *named positive-multiplicity microbranches* of the **candidate** paired-triad residual model, with complete three-coordinate polynomial

\[
P(X,Y,Z)=1+X+Z+XY+YZ+XYZ.
\]

The explicitly declared partial endpoint observer \(\pi_{XZ}(u,v,w)=(u,w)\) gives

\[
F(X,Z)=P(X,1,Z)=1+2X+2Z+XZ
\]
in \(R_Q=\mathbb Z[X,Z]/(X^Q-1,Z^Q-1)\). For \(n\ge0\), let \(c_Q(n)\) be the gcd of all \(Q^2\) coefficients of \(F^n\). Their sum is \(6^n\), so precisely reproducing *only this endpoint marginal distribution* with equiprobable deterministic initial seeds costs \(M_Q(n)=6^n/c_Q(n)\) seeds. A paired candidate block corresponds to two microbranch factors, \(n=2k\). This is not an assertion about the native licensed TRIADIC_CLOSURE_E event, full three-coordinate area, signed Ports, named histories or complete three-dimensional slice; X6 and P000 are preserved.

## Theorem

For **every** \(a\ge2\), let \(d=3^{a-1}\), \(Q=3d\). Then for every integer \(0\le n<9d\),

\[
\boxed{
c_Q(n)=
\begin{cases}
1,&0\le n<3d,\\
9,&3d\le n<5d,\\
81,&5d\le n<7d,\\
729,&7d\le n<9d.
\end{cases}}
\]

The first three corridors are the established R762DP/DQ results. This note proves the **new sharp fourth corridor**, not merely the value at \(n=7d\). Hence for all \(7d\le n<9d\), \(M_Q(n)=6^n/729\). Neither \(a=1\) nor \(n\ge9d\) is included.

## Proof

Put \(A_Q=\mathbb Z[T]/(T^Q-1)\), \(x=T-1\). The powers \(1,x,\ldots,x^{Q-1}\) form an integral basis. In the two-axis tensor ring write \(x=X-1,z=Z-1\), so \(F=xz+3(2+x+z)\); modulo 3 this is \(xz\) in \(\mathbb F_3[x,z]/(x^Q,z^Q)\).

**Lemma 1 (sharp one-axis 7d).** In \(A_Q\), \(x^{7d}\) is divisible by 27, and \(x^{7d}/27\bmod3=x^d U_x(x)\), where \(U_x(0)\ne0\) in \(\mathbb F_3\).

Indeed \(x^Q=3H\), where the integral polynomial representative of \(H\) is
\[
H=-\sum_{i=1}^{Q-1}\frac{\binom Qi}{3}x^i.
\]
The valuations \(v_3\binom Qi=a-v_3(i)\) for \(0<i<Q\) show that the terms below degree \(d\) have coefficients divisible by 3, while the coefficient in degree \(d\) becomes a unit after dividing by 3. Thus \(H=x^d u+3v\) with integral polynomials \(u,v\) and \(u(0)\not\equiv0\bmod3\). As \(Q=3d\),
\[
\frac{x^{7d}}{27}=\frac{x^d H^2}{3}
=H u^2+2x^{2d}uv+3x^d v^2.
\]
This proves integral divisibility. Modulo 3 the quotient is
\[
x^d[u^3+2x^d uv],
\]
whose bracket is a unit. The same holds for \(z\).

**Lemma 2 (5d lower bound).** \(x^{5d}\in9A_Q\). For \(H=x^Q/3\), Lemma 1 gives \(H\bmod3\in(x^d)\), so \(x^{5d}=3x^{2d}H\) is divisible by 9 since \(x^{3d}=0\) in the characteristic-three quotient.

**Case \(a\ge3\).** Write \(b=a-1\ge2\), hence \(d\ge9\). Expand
\[
F^{7d}=\sum_{j=0}^{7d}\binom{7d}{j}3^j(xz)^{7d-j}(2+x+z)^j.
\]
For \(1\le j\le6\), \(7d-j\ge5d\); Lemma 2 implies the \((xz)\)-power is divisible by \(3^4\). For \(j=1,2,3\), the binomial coefficient 3-adic valuations are respectively \(b,b,b-1\), giving total valuations at least \(b+5,b+6,b+6\), all at least 7. Terms \(j=4,5,6\) have valuation at least \(j+4\ge8\), and \(j\ge7\) have an explicit factor \(3^7\). Therefore
\[
F^{7d}\equiv x^{7d}z^{7d}\pmod{3^7R_Q}.
\]
Lemma 1 now yields
\[
F^{7d}/729\bmod3=x^d z^d W(x,z),
\]
where \(W\) has nonzero constant term and is a unit in \(\mathbb F_3[x,z]/(x^{3d},z^{3d})\). For \(0\le r<2d\), multiply by \(F^r\bmod3=x^rz^r\):
\[
F^{7d+r}/729\bmod3=x^{d+r}z^{d+r}W\ne0.
\]
Thus \(v_3(c_Q(7d+r))=6\).

**Case \(a=2\), \(Q=9,d=3\).** This finite exceptional case can be proved by the complete cyclic integer recurrence, indices modulo 9:
\[
A_{m+1}(i,j)=A_m(i,j)+2A_m(i-1,j)+2A_m(i,j-1)+A_m(i-1,j-1)
\pmod{2187},
\]
with \(A_0(0,0)=1\) and all other entries zero. Twenty-one steps establish that **all 81 residues** of \(F^{21}\) are divisible by 729 and that the exact quotient, expressed in \(x=X-1,z=Z-1\), has the following eight-term residue:
\[
\frac{F^{21}}{729}\equiv
x^3z^3\bigl(1+x^4+x^5+z^4+z^5+x^4z^4+x^4z^5+x^5z^4\bigr)
\pmod{3;\ x^9=z^9=0}.
\]
The bracket has constant coefficient 1, hence is a unit. Multiplication by \(F^r\bmod3=x^rz^r\) proves \(v_3(c_9(n))=6\) for all \(21\le n<27\). The attached executable reproduces the entire 81-coefficient certificate with exact integer operations, without sampling.

Finally the coefficient sum is \(6^n\); any prime divisor of \(c_Q(n)\) divides 6. No factor 2 occurs for \(n\ge1\): with odd \(Q\), \(\mathbb F_2[C_Q^2]\) is reduced and \(F\bmod2=1+XZ\ne0\), hence \(F^n\bmod2\ne0\). Thus the exact integer gcd is \(3^6=729\). Combining with R762DP/DQ proves the stated four-corridor theorem. QED.

## Recalculation and limits

The companion **R762DR_VERIFY.js** and its generated **R762DR_EVIDENCE.json** check all \(n=1,\ldots,9d-1\), for \(Q\in\{9,27,81\}\), using integers modulo \(3^7=2187\). The tests include all four corridors, exact modular mass, the nonzero residue witness at \(7d\), and the full \(Q=9\) eight-term polynomial certificate. This is an author-side exact finite check, separate from the universal symbolic proof for \(a\ge3\). Independent review: NOT_REVIEWED; no Lean verification; no formal project Result/admission.

**Further scientific frontier:** establish or refute the apparent next content jump \(c_Q(9d)=6561\) for all \(a\ge2\) (only finite examples for \(Q=9,27,81\) currently), classify the full three-area-coordinate \(3\)-adic content, and obtain authenticated native TRIADIC_CLOSURE_E signed Cell/Link/Port legality and V17/V29/V39 transport before claiming a future-safe native observer quotient.
