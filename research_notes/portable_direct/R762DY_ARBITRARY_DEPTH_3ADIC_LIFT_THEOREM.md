# R762DY — Arbitrary-depth Frobenius kernel for positive three-coordinate BRC, and the exact fourth valuation stratum

Date 2026-11-18 (Asia/Shanghai). Original task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`; publication `TP2-8B7E13C5904A2D6F1142`; researcher `EM-X6-3050F6`; claim `MCP-d6d2c143cc4d2df4dea1c00c`. Status: symbolic author proof plus exhaustive exact-integer author checks; independent mathematical review `NOT_REVIEWED`.

Scientific inputs frozen to P000 V5 at `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` and taskbook at `e3f42efac29a2da2d95be391f3231a664e2fade0`. Existing R762DU/DV, R762DW and R762DX are reused, not redone. This is a theorem about the positive six-branch *terminal three-coordinate observer*, not a claim of native signed event permission.

## Setup

In the commutative integral group ring \(\mathbb Z[C_Q^3]\), let

\[
P_Q=1+X+Z+XY+YZ+XYZ,\qquad X^Q=Y^Q=Z^Q=1.
\]

Write \(C_Q(n;u,v,w)\) for the nonnegative integer coefficient of \(X^uY^vZ^w\) in \(P_Q^n\). If \(Q=3^a\), the Frobenius congruence \(P_Q^Q\equiv P_Q(X^Q,Y^Q,Z^Q)=6\equiv0\pmod3\) makes all coefficients of \(P_Q^Q/3\) integral.

For \(s\ge1\), define the **universal finite kernel**

\[
\boxed{K_s:=\frac{P_{3^s}^{3^s}}{3}\ \bmod 3^s\in(\mathbb Z/3^s)[C_{3^s}^3].}
\]

It has exactly \(3^{3s}\) endpoint positions and can be enumerated from positive six-branch integer recurrence modulo \(3^{s+1}\).

## Theorem A — arbitrary-depth ternary Frobenius lift

For every \(a\ge s\ge1\), set \(Q=3^a\), \(b=3^{a-s}\), and let \(\iota_b\) inject \(C_{3^s}^3\) into \(C_Q^3\) by sending each basis generator to its \(b\)-th power. Then

\[
\boxed{\frac{P_Q^Q}{3}\equiv \iota_b(K_s)\pmod{3^s}.}
\]

Thus the first \(s\) three-adic digits of every positive endpoint coefficient of \(P_Q^Q/3\) are determined by a single \(3^{3s}\)-point kernel, independently of the larger \(Q\).

**Proof.** In any commutative \(\mathbb Z\)-algebra, if \(F\equiv G\pmod3\), then \(F^{3^s}\equiv G^{3^s}\pmod{3^{s+1}}\): for \(t\ge1\), expanding \((G+3^tH)^3-G^3\) shows it is divisible by \(3^{t+1}\); induct on \(s\). Put \(F=P_Q^b\) and \(G=P_Q(X^b,Y^b,Z^b)\). Frobenius in characteristic three gives \(F\equiv G\pmod3\), because \(b\) is a power of three. Then

\[
P_Q^Q=F^{3^s}\equiv G^{3^s}=\iota_b(P_{3^s}^{3^s})\pmod{3^{s+1}}.
\]

Both sides are coefficientwise divisible by three. Divide the integral difference by three to get the asserted modulo-\(3^s\) congruence. QED.

## Theorem B — full pointwise corridor and arbitrary finite valuation strata

Fix \(a\ge s\ge1\), \(Q=3^a\), \(b=3^{a-s}\), \(0\le r<b\). Every endpoint has unique coordinates \(u=u_0+bi\), \(v=v_0+bj\), \(w=w_0+bk\), where \(0\le u_0,v_0,w_0<b\) and \(0\le i,j,k<3^s\). Then

\[
\boxed{
\frac{C_Q(Q+r;u,v,w)}3\equiv
K_s(i,j,k)\ C_b(r;u_0,v_0,w_0)\pmod{3^s}.
}
\]

Let \(h_j(s)\) be the number of universal kernel positions with exact residue valuation \(j\) for \(0\le j<s\); let \(A_j(b,r)\) be the number of coefficients of \(P_b^r\) with exact valuation \(j\) modulo \(3^s\). Then, for each \(1\le t\le s\), the number of full \(Q^3\) endpoint coefficients with integer three-adic valuation exactly \(t\) is

\[
\boxed{N_t(Q,r)=\sum_{j=0}^{t-1}h_j(s)\,A_{t-1-j}(b,r).}
\]

Every other endpoint coefficient has valuation at least \(s+1\), including zero coefficients (\(v_3(0)=+\infty\)).

**Proof.** The ordinary unreduced \(P^r\) has every monomial exponent in \([0,r]^3\subset[0,b)^3\). Therefore the translates by the injected subgroup \(C_{3^s}^3\) cannot collide in the three coordinate residues modulo \(b\). Theorem A multiplied by \(P^r\) gives the pointwise product. For nonzero residues, the valuation of a product modulo \(3^s\) is the sum of component valuations so long as the sum is less than \(s\). The overall factor of three adds one, proving the convolution of residue-valuation populations. QED.

## Exact universal fourth-layer certificate

For \(s=4\) the kernel has \(3^{12}=531441\) positions. Direct exact-int cyclic recurrence for \(P_{81}^{81}\bmod243\), followed by coefficientwise division by three, gives the following exhaustive populations for \(K_4\bmod81\):

| \(v_3(K_4)\) residue class | Number of positions |
|---|---:|
| 0 | 27 |
| 1 | 504 |
| 2 | 9,242 |
| 3 | **169,104** |
| >=4 | **352,564** |
| **Total** | **531,441** |

Consequently for every \(Q=3^a\) with \(a\ge4\), \(b=Q/81\), \(0\le r<b\), and \(A_j=A_j(b,r)\),

\[
\begin{aligned}
N_1&=27A_0,\\
N_2&=504A_0+27A_1,\\
N_3&=9242A_0+504A_1+27A_2,\\
\boxed{N_4&=169104A_0+9242A_1+504A_2+27A_3.}
\end{aligned}
\]

In particular, at \(Q=81,n=81\), the exact valuation populations of the original positive endpoint count are \((27,504,9242,169104)\) at valuations \(1,2,3,4\), with 352,564 remaining positions divisible by \(3^5\).

The companion Python program `R762DY_VERIFY.py` (NumPy integer operations, no floating point) exactly checks all 531,441 positions by six-shift cyclic recurrence modulo243; computes the histogram and its 24 explicit nonzero residue keys; and compares nested reductions to the previously verified \(K_3,K_2,K_1\) at all embedded subgroup positions. It computes the SHA256 of the byte-serialized kernel to provide reproducible implementation provenance. This is an exhaustive finite certificate for \(s=4\); Theorems A and B prove uniformity in \(a\) and \(r\).

## Mathematical scope and next objective

This result unifies R762DW and R762DX as the \(s=2,3\) instances of a general lifting mechanism and adds a new fourth exact valuation stratum. It leaves the arbitrary-\(n\), all-horizon exact gcd-content problem open. The unresolved native event target is to source admissible signed `TRIADIC_CLOSURE_E` Cell/Link/Port updates and V17/V29/V39 transport before any future-safe observer compression.

Prior source: R762DU/DV at `53ce5dcb3e55deb783f0a6436ae5248aa49a7a05`; R762DW–DX source under Draft PR #2693. Signed branch provenance and X6's six original axes remain part of the full physical research target.
