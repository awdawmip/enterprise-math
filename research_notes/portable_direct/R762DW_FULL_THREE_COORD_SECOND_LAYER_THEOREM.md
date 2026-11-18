# R762DW — Universal second 3-adic layer and exact valuation strata of the full-three-coordinate BRC

Date: 2026-11-18 (Asia/Shanghai). Task `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, publication `TP2-8B7E13C5904A2D6F1142`, researcher `EM-X6-3050F6`, original claim `MCP-d6d2c143cc4d2df4dea1c00c`. Status: author-proved finite-kernel theorem; independently rerunnable exact-integer evidence; independent review `NOT_REVIEWED`.

## Exact model and frozen pins

Science: `p000_reality_foundation.json` V5 at `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; frozen taskbook `research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md` at `e3f42efac29a2da2d95be391f3231a664e2fade0`. Reuse R762DN, R762DT and R762DU/DV. Work in the integer group ring

\[
R_Q=\mathbb{Z}[C_Q^3],\quad P=1+X+Z+XY+YZ+XYZ.
\]

Write \(C_Q(n;u,v,w)\) for the positive six-branch integer count in \(P^n\) at a full three-coordinate endpoint in \(C_Q^3\). Signed Port/native Cell/Link legality and V17/V29/V39 transport remain separate questions.

## Theorem 1: universal modulo-9 quotient kernel

For every \(a\ge 2\), put \(Q=3^a\), \(b=Q/9\), \(U=X^b,V=Y^b,W=Z^b\), and in the integral group ring \(\mathbb Z[C_9^3]\) set

\[
C=P(U,V,W),\qquad A=P(U^3,V^3,W^3),\qquad
K=\frac{A^3}{3}+A^2(C^3-A)\pmod9.
\]

The division by three is coefficientwise exact in the integral group ring, and for all \(a\ge2\),

\[
\boxed{\frac{P^Q}{3}\equiv K(X^b,Y^b,Z^b)\pmod9.}
\]

The complete 729-point kernel has this **exact** residue histogram:

| Residue of \(K\) modulo 9 | 0 | 2 | 3 | 5 | 6 |
|---|---:|---:|---:|---:|---:|
| Number of endpoints | 198 | 21 | 276 | 6 | 228 |

The 21 entries equal to 2 and 6 entries equal to 5 are exactly the 27 points of the subgroup \(H_3=\{0,3,6\}^3\). All 504 entries equal to 3 or 6 lie outside \(H_3\).

**Proof.** Put \(E_j=P(X^{3^j},Y^{3^j},Z^{3^j})\). Frobenius gives \(P^{3^j}=E_j+3D_j\) with integral \(D_j\), and the exact recurrence

\[
D_{j+1}=\frac{E_j^3-E_{j+1}}3+3E_j^2D_j+9E_jD_j^2+9D_j^3.
\]

Thus \(D_{a-1}\equiv (E_{a-2}^3-E_{a-1})/3\pmod3\). Here \(E_{a-2}=C\), \(E_{a-1}=A\). Cubing \(P^{Q/3}=A+3D_{a-1}\) and dividing by three yields

\[
\frac{P^Q}{3}=\frac{A^3}{3}+3A^2D_{a-1}+9AD_{a-1}^2+9D_{a-1}^3
\equiv\frac{A^3}{3}+A^2(C^3-A)\pmod9.
\]

The coefficientwise integrality of \(A^3/3\) follows from \(A^3\equiv P(U^9,V^9,W^9)=6\equiv0\pmod3\). All monomials in \(K\) lie in the injected order-\(9^3\) subgroup. The histogram is an **exhaustive finite lemma**: the accompanying `R762DW_VERIFY.py` enumerates all 729 entries from the displayed group-ring expression and independently checks them against \((P^9\bmod27)/3\bmod9\) via six-shift integer recurrence. The enumerator's arithmetic and loops are explicit and independently repeatable. This completes the proof for every \(a\). \(\square\)

## Theorem 2: exact first two valuation strata for \(Q\le n<Q+Q/9\)

Let \(0\le r<b\), and express the unique endpoint coordinates as \(u=u_0+bi\), \(v=v_0+bj\), \(w=w_0+bk\), where \(0\le u_0,v_0,w_0<b\), \(0\le i,j,k<9\). Then

\[
\boxed{\frac{C_Q(Q+r;u,v,w)}3\equiv
K(i,j,k)\ C_b(r;u_0,v_0,w_0)\pmod9.}
\]

For \(b=1\), use the trivial group \(C_1^3\). Define

\[
S_b(r)=\#\{\rho:C_b(r;\rho)\not\equiv0\pmod3\},\quad
T_b(r)=\#\{\rho:C_b(r;\rho)\equiv3\text{ or }6\pmod9\}.
\]

The **exact endpoint counts** whose integer path count has three-adic valuation exactly one or two are

\[
\boxed{N_{v_3=1}=27S_b(r),\qquad
N_{v_3=2}=504S_b(r)+27T_b(r).}
\]

All other endpoints have valuation at least three, including zero counts (convention \(v_3(0)=\infty\)). By R762DU's ternary Lucas support theorem,

\[
S_b(r)=6^{N_1(r)}18^{N_2(r)},\qquad
\sum_{0\le r<b}N_{v_3=1}=27\,25^{a-2},
\]

where \(N_1,N_2\) count digits 1 and 2 in the padded base-3 expansion of \(r\).

**Proof.** Multiply Theorem 1 by \(P^r\). For \(r<b\), all three ordinary monomial exponents of \(P^r\) belong to \([0,b-1]\), so translations by the embedded \(C_9^3\) subgroup have disjoint endpoint residues modulo \(b\); each full coefficient is exactly the displayed product modulo 9. The 27 values of \(K\) on \(H_3\) are units modulo3, producing \(27S_b(r)\) original coefficients of valuation one and \(27T_b(r)\) of valuation two. The other 504 \(K\) values of valuation one modulo9 yield \(504S_b(r)\) additional original coefficients of valuation two. The 198 remaining kernel entries are zero modulo9. R762DU gives the formula for \(S_b\); summing each ternary digit's contributions \(1+6+18=25\) gives the aggregate. \(\square\)

## Evidence, reproducibility and boundaries

Run `python R762DW_VERIFY.py` using the Python standard library. It computes the full 729-state kernel through the group-ring formula and direct \(P^9\bmod27\) recurrence, then independently evaluates \(P^{Q+r}\bmod27\) and the factorized prediction for all 59,778 endpoint checks at \((Q,r)=(9,0),(27,0),(27,1),(27,2)\). The kernel enumeration is finite and exhaustive; generality in \(a,r\) follows from the symbolic proof, not finite extrapolation. At \(Q=9,r=0\), valuation counts are \(27,504,198\) for \(v_3=1,2,\ge3\). At \(Q=27,r=2\), they are \(486,9099,10098\).

The all-horizon full-three-coordinate content conjecture remains open. An immediate next unit is an \(H_{27}\)-supported universal formula for \(P^Q/3\bmod27\); separately determine the licensed native `TRIADIC_CLOSURE_E` signed Cell/Link/Port event language before claiming future-safe native BRC compression.

Prior works: R762DN@4e9001fe28f8bc19ce93e5a1f87d842a241d7756; R762DT@2b00cadde50fa5528f4a6e87c0a027ec64767dba; R762DU/DV@53ce5dcb3e55deb783f0a6436ae5248aa49a7a05.
