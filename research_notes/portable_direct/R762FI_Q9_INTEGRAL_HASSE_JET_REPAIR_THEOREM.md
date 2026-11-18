# R762FI — Integral Hasse-jet repair of the R762FH Fourier blindspot

Date: 2026-11-19 (Asia/Shanghai).
Status: AUTHOR PROVED GENERAL INTEGRAL INVERTIBILITY; EXACT FINITE CERTIFICATE h=3..8 / NOT_REVIEWED.
Same frozen Task RS-X6-TRIADIC-CLOSURE-DYNAMICS. This note uses the positive six-branch q=9 BRC shadow defined in R762FH; no native signed force-event claim.

## Research question

Ordinary evaluations at the 729 ninth-root characters miss the genuine q9 full-terminal difference modulo 3^h at h=3,...,8 (R762FH). Can one replace these lossy mod-3 Fourier observations with an integer observer and obtain a fixed low-complexity scalar witness for those counterexamples?

## FI1 — General integral Hasse-jet coordinate equivalence

Each F in R=Z[X,Y,Z]/(X^9-1,Y^9-1,Z^9-1) has its canonical integer representative
F(X,Y,Z)=sum_{0<=x,y,z<=8} f_{xyz} X^x Y^y Z^z.

Set u=X-1,v=Y-1,w=Z-1 and define the 729 integral Hasse jets by the canonical representative:
J_{ijk}(F) = [u^i v^j w^k] F(1+u,1+v,1+w)
           = sum_{x>=i,y>=j,z>=k} binom(x,i) binom(y,j) binom(z,k) f_{xyz},
for 0<=i,j,k<=8.

The one-axis transform M_{i,x}=binom(x,i) (0<=i,x<=8) is upper triangular with diagonal entries one. Its determinant is one, and the three-axis transform M tensor M tensor M is unimodular over Z. Therefore, for every modulus m>=1, and all F,G in R,

F = G coefficientwise (mod m)  <==>  J_{ijk}(F)=J_{ijk}(G) (mod m) for all 729 indices.

This is a general exact statement (no finite-h dependency). Hasse jets are linear functionals of the canonical 0..8 representatives, not undefined derivatives in the polynomial quotient; the representative choice is part of the interface.

## FI2 — One degree-10 integral observer detects every tested blind difference

For h=3,4,5,6,7,8 set L_h=18*3^(h-3), n=36 and D_h=T(36+L_h)-T(36) as in R762FH. The full exact 729-endpoint integer computation followed by the unimodular Pascal transform yields

J_{0,4,6}(D_h) = 3^(h-1) (mod 3^h).

Thus **one fixed total-degree 10 Hasse jet**, at unchanged 3-adic precision, distinguishes all six genuine full-vector differences that are invisible to every ordinary cyclotomic character at that precision. The finite result does not claim all-h applicability.

Further exact finite results common to all six h:
- precisely 227 of 729 Hasse jets are nonzero mod 3^h;
- every jet of total degree <10 vanishes mod 3^h; minimum detecting degree is 10;
- all 729 coefficients of D_h have **exact** valuation h-2, not merely the coefficientwise minimum h-2 established in R762FH;
- the 729-coordinate scaled profiles (D_h / 3^(h-2)) mod 3 are identical for h=3,...,8;
- the scaled profiles modulo 9 are identical for h=4,...,8. The h=3 profile need not match modulo 9.

Table:
| h | L_h | J_{0,4,6}(D_h) mod 3^h | Nonzero jets | Minimum degree |
|---|---:|---:|---:|---:|
| 3 | 18 | 9 | 227 | 10 |
| 4 | 54 | 27 | 227 | 10 |
| 5 | 162 | 81 | 227 | 10 |
| 6 | 486 | 243 | 227 | 10 |
| 7 | 1458 | 729 | 227 | 10 |
| 8 | 4374 | 2187 | 227 | 10 |

## Proof, execution, and boundaries

FI1 is the exact unimodular Pascal-matrix argument. FI2 is a finite exhaustive certificate: R762FI_VERIFY.py imports the R762FH six-branch exact integer transition table; computes the normalized 729-coordinate vectors for n=36 and every n+L_h; checks coefficientwise divisibility; divides exactly; performs the three successive length-9 binomial transforms modulo 3^h; and checks the asserted support, minimum degree, fixed jet and cross-h scaled profiles. The JSON execution output R762FI_EVIDENCE.json records the six checked cases. All inputs are integer, there are no floats, random tests or external datasets. Local execution: PASS. Independent mathematical review: NOT_REVIEWED.

The 729-jet observer is lossless, but is not claimed to be smaller than the original 729 coordinates; the one-jet detection is proved only for the six specified differences. It is a concrete route toward a smaller *task-specific* integral observer. The next unresolved result is a uniform all-h theorem or exact counterexample for the fixed Hasse jet and the proposed q9 period, followed by a provably minimal joint-jet/lattice compression. Signed Cell/Link/Port dynamics remain separate.
