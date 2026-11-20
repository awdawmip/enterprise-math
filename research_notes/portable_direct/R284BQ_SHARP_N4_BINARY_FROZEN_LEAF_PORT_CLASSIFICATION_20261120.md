# R284BQ — Sharp all-integer frozen-leaf identifiability in the 4×4 binary star-Port observer

Date: 2026-11-20 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_EXHAUSTIVE_CERTIFICATE_PASSED / NOT_REVIEWED.
Parent frontier: R284BP, `5a54002ac3d36d2c5aca143198ac72d2b5219047:research_notes/portable_direct/R284BP_ALL_DIMENSION_ROOT_FROZEN_STAR_PORT_GAUGE_20261120.md` (blob 0e95becfc0bdb5b82f4780357a9a5b4a58a494b3). This is an independent finite-model continuation, not a replacement for the frozen root theorem.

## Observer, precise claim

Let `C∈{1,2}^{4×4}` (65,536 distinct matrices), fix the first leaf diagonal control `d_1=t∈Z`, and allow six independent integer/finite-field controls `d_0,d_2,d_3,z_1,z_2,z_3`. Define

```
F_C(d_0,d_2,d_3,z) = det(diag(d_0,t,d_2,d_3)-C-z_1 E_{01}-z_2 E_{02}-z_3 E_{03}).
```

**BQ1 (sharp finite-family frozen-leaf classification, all integer t).**
Every pair of distinct `C,D∈{1,2}^{4×4}` has a **nonconstant** polynomial response difference `F_C-F_D` in the six free controls if and only if

```
                 t <= -4  OR  t >= 5.
```

For each integer `-3 <= t <= 4` there exist distinct binary matrices with *exactly identical* response polynomials (not merely constant-gap responses).

**BQ2 (one-reading arbitrary finite real circular-error recovery).**
For every prescribed `rho>=0` finite, there exist a prime `p` and one fixed nonadaptive setting of the six free controls in `F_p` such that one residue on a real circle of circumference `p`, corrupted by any circular error of radius at most `rho`, uniquely recovers all 65,536 matrices **if and only if** `t<=-4` or `t>=5`. Decoder existence is by finite lookup, without a claimed polynomial-time construction or a small explicit modulus.

The contrast with the 3×3 leaf case of R284BN is substantive: within the present 4×4 binary family the sharp forbidden integer interval is independent of the finite error radius.

## Exact coefficient representation

Put `a=C_00`, `b=(C_01,C_02,C_03)`, `v=(C_10,C_20,C_30)^T`, `A=C[1:4,1:4]`, and

```
B=diag(t,x_2,x_3)-A;
L=det(B);  g=adj(B) v;
F_C=(d_0-a)L - (b+z)^T g.
```

Each of `L,g_1,g_2,g_3` and `h=-a L-b^T g` is multiaffine in `(x_2,x_3)`. The coefficients in the ordered basis `(1,x_2,x_3,x_2*x_3)`, for these five polynomials, form a 20-component integer vector `V_C(t)`. The 19-vector `S_C(t)` is `V_C(t)` with the coefficient of the constant monomial of `h` removed. Signs of the `g_i` portions do not change equality of signatures. Then

```
F_C-F_D is constant in all six controls   <=>   S_C(t)=S_D(t),
F_C=F_D as polynomials                   <=>   V_C(t)=V_D(t).
```

Four exact corner evaluations `(x_2,x_3)=(0,0),(1,0),(0,1),(1,1)` reconstruct each multiaffine polynomial. The published checker computes `L,g` via the explicit 3×3 adjugate identity; 96 independent sampled 4×4 Leibniz determinant comparisons cross-check evaluation and signs.

## Proof of BQ1 (bounded exhaustive certificate implies all-integer theorem)

1. Every entry of `S_C(t)` is an affine integer function of `t`: `S_C(t)=tP_C+Q_C`, where `Q_C=S_C(0)` and `P_C=S_C(1)-S_C(0)`.
2. Exact complete enumeration of `2^16=65,536` row-major binary matrices finds that all pairs `(P_C,Q_C)` are distinct, and every component of the *full* `V_C(0)` has absolute value at most 8. Thus for `C≠D` some coefficient of `P_C-P_D` or `Q_C-Q_D` is nonzero. If `S_C(t)=S_D(t)` and `P_C≠P_D`, then a nonzero integer slope coordinate satisfies `t(P_C-P_D)_i=-(Q_C-Q_D)_i`, hence `|t|<=16`. If `P_C=P_D`, the joint-uniqueness certificate rules out `S_C(t)=S_D(t)` for any `t`.
3. For every integer `t∈[-16,16]`, a complete independent-key census of all 65,536 values `S_C(t)` finds no repeated keys for `-16<=t<=-4` and `5<=t<=16`. This, with step 2, proves the positive assertion for all integers outside `[-3,4]`.
4. At each of the eight forbidden integers the enumeration records two distinct row-major 16-digit matrix strings with exactly equal `V_C(t)`; equality of the reconstructed coefficient vectors is equality of the entire response polynomials. The witness pairs are:

| t | C (row-major) | D (row-major) | distinct full responses |
|---:|---|---|---:|
| -3 | 1111211112111221 | 1111211112121211 | 63,536 |
| -2 | 1111221112111221 | 1111221112121211 | 63,536 |
| -1 | 1111111111111211 | 1111111111121211 | 55,521 |
| 0 | 1111111111111111 | 1111111111111121 | 45,506 |
| 1 | 1111111111111111 | 1111111111112122 | 52,817 |
| 2 | 1111111111111211 | 1111111111112122 | 62,111 |
| 3 | 1111121111111211 | 1111121111112122 | 64,094 |
| 4 | 1111222211111211 | 1111222211112122 | 64,815 |

The verification JSON additionally gives each `t`'s nonconstant-signature count, 8 full-response witnesses, and 5 distinct nonzero constant-gap witnesses for `t=-3,...,1`. The proof is exact finite exhaustive reasoning plus the integer parameter bound, not a floating-point extrapolation. Independent mathematical review is pending.

## Proof of BQ2

When `t∈[-3,4]`, BQ1 gives a pair whose responses coincide at *every* control setting and every prime, so arbitrary numbers of exact or adaptive observations cannot separate that pair.

Otherwise every polynomial `F_C-F_D` is nonconstant. Put `M=floor(2rho)`. For all unordered pairs and integers `k∈[-M,M]`, `F_C-F_D-k` is a nonzero integer polynomial of total degree at most 4. Choose a prime larger than `2M+1` and all nonzero coefficient magnitudes in this finite family. Modulo `p`, all remain nonzero. Random independent free controls are uniform on `F_p`; Schwartz–Zippel and a union bound show that the probability of any circular separation `<=2rho` is at most

```
       4*(2*M+1)*binom(65536,2)/p.
```

A sufficiently large prime makes this less than 1. At the resulting fixed controls, circular error balls of radius `rho` around the residues are disjoint, so nearest-codeword lookup recovers the matrix. This establishes existence with every finite `rho`; it does not give an efficient search, minimized hardware dynamic range, or a native P000 realization.

## Reproduction, provenance, next problem

Run `python R284BQ_leaf4_binary_checker.py` with standard Python 3, alongside its verification JSON. All coefficient operations and comparisons use exact integers; the `n=4,H=2` enumeration is complete. The checker writes a reproducible JSON result beside itself, with witness strings and t-census. Source claim status: `AUTHOR_PROVED / EXACT_EXHAUSTIVE_CERTIFICATE_PASSED / NOT_REVIEWED`. This research note is an auxiliary signed determinant observer: positive BRC branch mass, native X6 geometry, and physical Port readout are separately typed. The 20-component coefficient vector is sufficient for the declared fixed-leaf observer and free-control horizon; it is not automatically sufficient under future operations changing the frozen control.

Open: derive an algebraic (non-enumerative) classification of the exceptional 4×4 fibre orbits; test whether the radius-independent threshold persists at higher `n,H`; optimize finite modulus/control sizes and replace the exponential lookup decoder. Preserve the R284BP root-gauge result and prior contributors. Historical R1 portable-research lineage `EM-DIRECT-E6B1DD` is provenance, not current authenticated CLAIM/RUN authority.