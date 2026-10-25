# R4-EC20 — Fifteen positive Newton diagonals at unbounded grades

**2026-10-25 | Exact author-side algebraic result; not independently reviewed or mathematically admitted.**

## Source and mathematical scope

Fixed GLOBAL_KNOWLEDGE_V1 source: main@4292cf9480b01650cccdda42b811dd2de3057aec. Initial Enterprise Math source: main@b8f3037621f986e5ee78832080c50d0e8ced26c3. Antecedent R4-EC19: dd6ecde56a6746cb2ee48fc8d88e7aa34a467eb4; kernel from R4-EC17. This is the **positive ordered binary affine auxiliary BRC clean-source observer**, not P000-native X6 dynamics or an all-word provenance-preserving quotient.

Write

\[
E(x,u)=\frac{1-ux^2}{1-(1+u)x+2u^2x^4-u^3x^6},\qquad
f_j(n)=[x^nu^j]E-[x^nu^{j-1}]E\quad(j\ge1).
\]

By the existing EC19 fixed-grade theorem,

\[
E_j(x)=\frac{A_j(x)}{(1-x)^{j+1}},\quad
A_0=1,\quad A_1=x-x^2+x^3,\quad A_{-1}=0,
\]
\[
A_j=x A_{j-1}-2x^4(1-x)A_{j-2}+x^6(1-x)^2A_{j-3},
\quad\deg A_j\le3j.
\]

## New theorem — EC20-TOP15

For **every** integer \(j\ge1\) and \(0\le d\le\min(14,j)\), put \(b_j=2j+6\). Then

\[
\boxed{\Delta^{j-d}f_j(b_j)>0.}
\]

In particular, for unrestricted \(j\),

\[
\Delta^j f_j(2j+6)=1,\quad
\Delta^{j-1}f_j(2j+6)=6,\quad
\Delta^{j-2}f_j(2j+6)=14
\]
(the second and third identities require \(j\ge1\), \(j\ge2\) respectively).

This **does not** prove positivity of all Newton differences, nor all-grade unimodality.

## Complete mathematical reduction

Define \(B_j(x)=A_j(x)-(1-x)A_{j-1}(x)\), so

\[
F_j(x):=\sum_{n\ge0}f_j(n)x^n
=\frac{B_j(x)}{(1-x)^{j+1}},
\qquad\deg B_j\le3j.
\]

For \(r=j-d\), the exact forward-difference identity gives

\[
\Delta^r f_j(2j+6)
=[x^{3j+6-d}]\frac{B_j(x)}{(1-x)^{d+1}}
=\sum_{k=0}^{3j}[x^k]B_j(x)\binom{3j+6-k}{d}.
\]

The binomial upper arguments are all nonnegative (in fact at least 6). Therefore, with \(t\) formal,

\[
\Delta^{j-d} f_j(2j+6)=[t^d]H_j(t),\qquad
H_j(t)=(1+t)^{3j+6}B_j((1+t)^{-1}). \tag{1}
\]

Now let \(X_j(t)=(1+t)^{3j}A_j((1+t)^{-1})\). Direct substitution yields

\[
X_0=1,\ X_1=1+t+t^2,\quad
X_j=(1+t)^2X_{j-1}-2t(1+t)X_{j-2}
+t^2(1+t)X_{j-3}.
\]

Consequently

\[
\sum_{j\ge0}X_j(t)z^j=
\frac{1-tz}{Q(z,t)},\quad
Q=1-(1+t)^2z+2t(1+t)z^2-t^2(1+t)z^3.
\]

Since \(H_j=(1+t)^6(X_j-t(1+t)^2 X_{j-1})\), we obtain the **exact formal identity**

\[
\boxed{
\mathcal H(z,t)=\sum_{j\ge0}H_j(t)z^j
=\frac{(1+t)^6(1-tz)(1-t(1+t)^2z)}
{1-(1+t)^2z+2t(1+t)z^2-t^2(1+t)z^3}.
} \tag{2}
\]

Write \(h_d(z)=[t^d]\mathcal H(z,t)\). The following finite recurrence determines it exactly:

\[
h_d=\frac{N_d-Q_1h_{d-1}-Q_2h_{d-2}-Q_3h_{d-3}}{1-z},
\]
where \(N_d=[t^d](1+t)^6(1-tz)(1-t(1+t)^2z)\),
\(Q_1=-2z+2z^2\), \(Q_2=-z+2z^2-z^3\), \(Q_3=-z^3\)
and \(h_{-1}=h_{-2}=h_{-3}=0\).

For each \(d\le14\), exact polynomial division obtains \(h_d=P_d(z)/(1-z)^{m_d}\). Coefficient extraction gives
\[
q_d(j)=[z^j]h_d(z),\qquad j\ge d.
\]
This is a polynomial in \(j\). The executed exact symbolic certificate computes **all 15** polynomials and verifies that **every monomial coefficient of** \(q_d(d+w)\) **is strictly positive** for \(w\ge0\). Hence by (1)-(2)
\(\Delta^{j-d}f_j(2j+6)=q_d(j)>0\) for every \(j\ge d\). QED.

Explicit examples, each valid for every \(j\ge d\):

| d | q_d(j) |
|---:|---|
| 0 | 1 |
| 1 | 6 |
| 2 | 14 |
| 3 | j+11 |
| 4 | 8j-25 |
| 5 | 30j-115 |
| 6 | (j-4)(j+141)/2 |
| 7 | 5j²+90j-517 |
| 8 | 25j²-29j-606 |

For \(9\le d\le14\), all exact polynomials and shifted coefficient certificates are preserved in the accompanying structured report and reproducible program. In particular, at \(d=14\), \(w=j-14\),

\[
q_{14}(14+w)=146475+\frac{178291}{2}w+\frac{55683}{4}w^2+\frac{1267}{2}w^3+\frac{17}{4}w^4.
\]

## Executed verification and limitations

The author executed exact SymPy rational coefficient derivations and checked every shifted coefficient for d=0..14, plus 629 direct integer depth-recurrence/Newton comparisons for j<=48 and 15,269 independent truncated grade-direction integer checks for j<=1024. Those are **checks**, not the source of universal quantification: the latter follows from equations (1)-(2) and the 15 finite exact rational certificates. The existing EC19 all-r theorem still covers only j<=512. Neither Lean nor native X6 was run; no service-issued CLAIM, accepted Result, or independent Driver review is implied.

Reuse resolution: REUSE_APPLIED for the precise EC17 kernel and EC19 fixed-grade/Newton method; EXTEND_EXISTING_TOOL for the top-diagonal rational transform, not a new top-level BRC tool family. The observer/multiplicity/path and native-scope limitations remain unchanged.

## Next question — R4-EC21

Can \(q_d(d+w)>0\) be proved for **every** \(d\ge0,w\ge0\), or is there an exact counterexample? Equation (2) is the exact rational target. Separately prove/falsify the six near-center inequalities \(f_j(2j+s)\ge0\) for all grades \(j\) and \(s=0,\ldots,5\). These two universal conditions together with EC19's polynomial reduction would settle unrestricted left-half unimodality; a longer finite search alone would not.
