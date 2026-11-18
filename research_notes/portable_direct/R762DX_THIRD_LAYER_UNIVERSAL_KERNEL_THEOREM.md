# R762DX — Universal third 3-adic layer of complete three-coordinate positive BRC

2026-11-18. Task `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, publication `TP2-8B7E13C5904A2D6F1142`; original Researcher `EM-X6-3050F6` and CLAIM `MCP-d6d2c143cc4d2df4dea1c00c`. Mathematical status: author-proved symbolic reduction with exhaustive finite group-ring kernel certificate and independent recurrence checks; mathematical review `NOT_REVIEWED`.

Frozen P000 V5 @ `a72226e2430ffa4786321ac86e7f0c599d5f0389`; immutable taskbook @ `e3f42efac29a2da2d95be391f3231a664e2fade0`. Reuse R762DU/DV and R762DW. Work with the six-positive-branch full three-coordinate integer BRC polynomial \(P=1+X+Z+XY+YZ+XYZ\) in \(\mathbb Z[C_Q^3]\), preserving all three area-residue coordinates.

## Theorem 1 — universal order-27^3 quotient kernel for every Q=3^a, a>=3

Put \(Q=3^a\), \(b=Q/27\), and \(U=X^b,V=Y^b,W=Z^b\) of order 27. In \(\mathbb Z[C_{27}^3]\), define

\[
B=P(U,V,W),\qquad C=P(U^3,V^3,W^3),\qquad A=P(U^9,V^9,W^9),
\]
\[
T_0=\frac{B^3-C}{3},\qquad T_1=\frac{C^3-A}{3}.
\]

Every division by three is coefficientwise integral. The universal 27-torsion kernel is

\[
\boxed{
K_{27}=\frac{A^3}{3}+3A^2T_1+9A^2C^2T_0+9AT_1^2+9T_1^3\pmod{27}.
}
\]

For every \(a\ge3\), in the full integer group ring of modulus Q,

\[
\boxed{P^Q/3\equiv K_{27}(X^b,Y^b,Z^b)\pmod{27}.}
\]

The complete 19,683-position kernel has this exact residue histogram modulo 27:

| Residue | 0 | 2 | 3 | 5 | 6 | 9 | 12 | 15 | 18 | 20 | 21 | 24 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Count | 9910 | 13 | 132 | 6 | 84 | 4424 | 120 | 72 | 4818 | 8 | 24 | 72 |

Consequently, precisely 27 quotient coefficients are units modulo 3, 504 have \(v_3=1\), 9242 have \(v_3=2\), and 9910 vanish modulo 27. These strata are compatible with the nested order-\(3^3\), order-\(9^3\) and order-\(27^3\) subgroups. The complete histogram is an exhaustive finite group-ring lemma, certified by the accompanying independently repeatable verifier.

**Proof.** Let \(E_j=P(X^{3^j},Y^{3^j},Z^{3^j})\), \(D_j=(P^{3^j}-E_j)/3\). Frobenius gives integrality and the exact recurrence

\[
D_{j+1}=\frac{E_j^3-E_{j+1}}3+3E_j^2D_j+9E_jD_j^2+9D_j^3.
\]

Reduce the \(j=a-2\) recurrence modulo 9, and the preceding \(j=a-3\) one modulo 3. Since \(E_{a-3}=B,E_{a-2}=C,E_{a-1}=A\), obtain

\[
D_{a-1}\equiv T_1+3C^2T_0\pmod9,
\qquad D_{a-1}\equiv T_1\pmod3.
\]

Cube \(P^{Q/3}=A+3D_{a-1}\), divide coefficientwise by three and reduce modulo 27:

\[
P^Q/3=A^3/3+3A^2D_{a-1}+9AD_{a-1}^2+9D_{a-1}^3
\equiv K_{27}\pmod{27}.
\]

Every term lies in the embedded subgroup \(C_{27}^3\). Enumeration of all 27^3 integral coefficients of the closed expression gives the exact histogram; `R762DX_VERIFY.py` independently checks every entry against a direct \(P^{27}\bmod81\) six-shift cyclic recurrence. The symbolic congruence then establishes the same kernel for all \(a\ge3\). QED.

## Theorem 2 — exact first three coefficient valuation strata for Q<=n<Q+Q/27

For \(0\le r<b=Q/27\), write any endpoint uniquely as \(t=(u_0+bi,v_0+bj,w_0+bk)\) with \(0\le u_0,v_0,w_0<b\) and \(0\le i,j,k<27\). Then

\[
\boxed{C_Q(Q+r;t)/3\equiv K_{27}(i,j,k)\ C_b(r;u_0,v_0,w_0)\pmod{27}.}
\]

Let \(S_b(r),T_b(r),U_b(r)\) count coefficients of \(P^r\) modulo b of 3-adic valuations \(0,1,2\), respectively, excluding zero coefficients. Then the **exact numbers of full coefficients of \(P^{Q+r}\)** with valuations one, two and three are

\[
\boxed{
\begin{aligned}
N_{v_3=1}&=27S_b(r),\\
N_{v_3=2}&=504S_b(r)+27T_b(r),\\
N_{v_3=3}&=9242S_b(r)+504T_b(r)+27U_b(r).
\end{aligned}}
\]

Every other coefficient position has valuation at least four (including zero). R762DU gives \(S_b(r)=6^{N_1(r)}18^{N_2(r)}\) in base three and \(\sum_{0\le r<b}N_{v_3=1}=27\cdot25^{a-3}\).

**Proof.** The ordinary polynomial \(P^r\) has coordinate exponents within \([0,r]^3\subset[0,b)^3\). The translates by the order-\(27^3\) subgroup therefore do not collide modulo b. Multiplication by the kernel gives the pointwise formula. The quotient kernel has valuations 0,1,2 in exact counts 27,504,9242; multiply this finite valuation histogram by the small coefficient valuation classes (S,T,U), adding 1 for the overall factor three, to obtain all three formulas. The digit-sum corollary is R762DU. QED.

## Reproduction, precise boundaries and next work

`python R762DX_VERIFY.py` uses NumPy integer arrays (author run with NumPy 2.3.5) and integer dictionary group-ring convolution. It checks the full 19,683-entry kernel by two algebraically independent routes; it also evaluates \(P^{81},P^{82},P^{83}\bmod81\) across \(3\cdot81^3=1,594,323\) endpoints and confirms the three valuation counts. Q=81 examples: r=0 yields (27,504,9242), r=1 yields (162,3024,55452), and r=2 yields (486,9099,166860). Author checks PASS; independent mathematical review NOT_REVIEWED. All-a and all-r claims rest on the symbolic proof and exhaustive finite kernel, not on Q81 samples.

The result concerns positive terminal area-counts, rather than native signed event legality. Next: derive the universal H81 quotient kernel modulo81, work toward the full-horizon three-coordinate gcd-content conjecture, and independently obtain licensed `TRIADIC_CLOSURE_E` Cell/Link/Port rules and V17/V29/V39 transport before native observer claims.
