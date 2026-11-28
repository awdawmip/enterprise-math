# EC49FVI — the 11/17-adic periodic union excludes 564/935 exponent residue pairs

Date: 2026-11-21 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FINITE_FIELD_AND_CRT_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED / NOT_ADMITTED.

This addendum extends the EC49FVI mod-11 theorem (same Draft PR #2884) under the unchanged derived Bernoulli observation pin BRC16943. The P000 and Heartbeat-X6 premises are unchanged. No compound minimax-risk admission is asserted.

## A second periodic obstruction at p=17

Use the same \(L_a,L_b,a,b,G_{h,n}\) as the primary proof and write \(k=h+n\). All model denominators are invertible modulo 17. The exact reductions are

\[
u\equiv3,\quad\gamma\equiv16,\quad L_a=1+6X,\quad
L_b=3+14X,\quad L_a-L_b=15+9X\quad(\bmod17).
\]

The sole finite point with \(L_a=L_b\) is \(X=4\), where \(a=b=L_a=L_b=8\). The polynomial divided difference and its leading projective coefficient satisfy

\[
G_{h,n}(4)=8^{h+n-1}(n+3h)\pmod{17},\qquad
G_{h,n}^*(1,0)=
\frac{6^{h+n}-14^{h+n}}{6-14}\pmod{17}.
\]

At the other 16 finite points and infinity (17 nonsingular projective points), powers depend only on exponents modulo 16 because all positive-exponent zero-base cases are stable. Exact finite-field evaluation gives **96** admissible \((h\bmod16,n\bmod16)\) patterns for which all 17 values are nonzero. At \(X=4\) one further requires \(n+3h\not\equiv0\bmod17\); each pattern then lifts to \(17^2-17=272\) residue pairs mod 272, for **26112/73984** positive exponent classes with a zero-free projective polynomial. Their rational likelihood phases are rigorously excluded for every rational width in (0,1).

| h mod 16 | Allowed n mod 16 |
|:--:|:--|
| 0 | 1, 3, 5, 7, 9, 11, 13, 15 |
| 1 | 0, 1, 2, 3, 9, 10, 11, 13 |
| 2 | 1, 2, 3, 4, 9, 11 |
| 3 | 0, 1, 3, 6, 7, 9, 11, 14 |
| 4 | none |
| 5 | 0, 1, 2, 5, 7, 10, 13, 15 |
| 6 | 1, 3, 6, 9, 11, 12 |
| 7 | 0, 5, 6, 7, 11, 13, 14, 15 |
| 8 | none |
| 9 | 0, 1, 2, 3, 5, 9, 10, 11 |
| 10 | 4, 5, 7, 10, 13, 15 |
| 11 | 0, 1, 3, 6, 9, 11, 14, 15 |
| 12 | none |
| 13 | 0, 2, 5, 7, 9, 10, 13, 15 |
| 14 | 5, 7, 12, 13, 14, 15 |
| 15 | 0, 3, 5, 6, 7, 13, 14, 15 |

## Exact two-prime union theorem

Let \(\mathcal C_{11}\) and \(\mathcal C_{17}\) denote the positive exponent-pair residue classes certified by the two prime-local tests. The moduli are 110 and 272; their gcd is 2 and lcm is \(M=14960\). A CRT lift in each exponent coordinate exists uniquely modulo \(M\) exactly when the two constituent residues agree in parity.

Exact counts, grouped by \((h\bmod2,n\bmod2)\):

| parity | mod 110 | mod 272 |
|:--:|--:|--:|
| 00 | 440 | 2176 |
| 01 | 1760 | 6528 |
| 10 | 1760 | 6528 |
| 11 | 880 | 10880 |

Therefore the exact number of classes in the intersection is

\[
I=440\cdot2176+1760\cdot6528+1760\cdot6528+880\cdot10880
=33,510,400.
\]

The separate lifted counts are

\[
A=4840(14960/110)^2=89,520,640,\qquad
B=26112(14960/272)^2=78,988,800.
\]

Inclusion–exclusion gives the exact union theorem:

\[
\boxed{|\mathcal C_{11}\cup\mathcal C_{17}|
=A+B-I=134,999,040\quad\text{in }M^2=223,801,600,}
\]
\[
\boxed{\text{residue-pair coverage }=\frac{134999040}{223801600}
=\frac{564}{935}\approx0.6032085561.}
\]

For **every** positive integer pair \((h,n)\) whose residue modulo \(M\) lies in this union, and every rational \(x\in(0,1)\), \(t(x)\ne h/(h+n)\). The fraction measures exponent-pair residue classes, not the natural density of distinct reduced fractions or widths.

## Verification and next direction

The included standard-library Python script recomputes both prime-local finite-field tables from the original exact rational coefficients, independently verifies the claimed conditions against all \(110^2+272^2=86084\) exponent classes, and recomputes CRT parity counts and their exact union. Local execution returned ALL PASS. All computations and the argument use exact modular integers and rational arithmetic.

The complement is an open scientific region. Next compare mod-19 and mod-31 periodic local tests and calculate their joint CRT union, including parity and higher gcd compatibility; look for a rational-width rational-phase witness in the remaining arithmetic classes. Independent mathematical review and upstream FUQ/FUR transfer remain separate.
