# R749STT — Exact three-read optimality for the initial 73/85 scalar pair

Date: 2026-11-17. Mathematical status: `AUTHOR_EXACT_NOT_REVIEWED`.
Immutable frozen scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.
Scientific predecessors: R749STP; R749STQ–STS (Draft PR [#2653](https://github.com/awdawmip/enterprise-math/pull/2653)), specifically R749STR's two-read collision for the pair (73,85).
This note describes the **five-source labeled auxiliary scalar observer**, not a native X6/Port/Cell correspondence. No shared Task CLAIM, Result or Review is asserted.

## Model and new theorem

The five distinct labeled coordinates have nonnegative integer values and weights `(1,1,2,3,6)`. For `n>=1`, `C_n` counts tuples with weighted sum at most `n-1`; `T_n` sums their *first* weight-one coordinate. Put

```
S(n) = 18*n^4 + 54*n^3 - 345*n^2 + 2070*n - 16315,
Y_n(e,d) = n^3*(T_n+e)/(C_n+d) - S(n)/108.
```

Each candidate `q=73` and `p=85` has an independent, **fixed across observations** nuisance pair `(e,d)` and `(E,D)` in the full continuous real square `[-2,2]^2`. The `j`th consecutive reading is `Y_(q+6*j)` or `Y_(p+6*j)`.

**Theorem.** Define the three-read contrast

```
L_n(e,d) = Y_n(e,d) - (21/10)*Y_(n+6)(e,d) + (11/10)*Y_(n+12)(e,d).
```

For every real `(e,d,E,D) in [-2,2]^4`,

```
L_73(e,d) - L_85(E,D)
 >= delta
 = 67536937868192626099237277/18291917078444373205412530425
 > 0.
```

The bound is **sharp**, attained at `(e,d,E,D)=(-2,2,2,2)`. The two initial observations have an exact legal rational collision, given below. Consequently

```
m_initial({73,85}) = 3.
```

With absolute additive error at most `eta` in each of the six raw readings, the contrast remains positive for

```
0 <= eta < (5/42)*delta
 = 67536937868192626099237277/153652103458932734925465255570.
```

No independence or probability assumption is used.

## Exact two-read collision (minimality)

Reuse and independently check the following R749STR witness:

```
E = 7/5,  D = 2,
e = -3017722237060578733161/1527694442423074582592,
d =  1445925897017416432877/763847221211537291296.
```

All four parameters are in `[-2,2]`. Direct Fraction arithmetic gives both equalities

```
Y_73(e,d) = Y_85(E,D),
Y_79(e,d) = Y_91(E,D).
```

Thus **one or two** successive initial observations cannot universally identify the candidate.

## Proof of the three-read separator

The exact integer counts are:

| n | C_n | T_n |
|---:|---:|---:|
| 73 | 707343 | 8931013 |
| 79 | 1020943 | 13914446 |
| 85 | 1436968 | 21025004 |
| 91 | 1978664 | 30933812 |
| 97 | 2672553 | 44459556 |

These follow by coefficient extraction from the five-weight product or direct integer dynamic programming, independently regenerated in the checker.

For `n=73,85`, take the partial derivatives of `L_n` in its two nuisance variables. The `S` contributions disappear upon differentiation. The four **strict** signs on the entire closed real square are

```
partial_e L_73 > 0,    partial_d L_73 < 0,
partial_E L_85 > 0,    partial_D L_85 > 0.
```

To certify them without sampling, write each signed rational derivative with a positive denominator and map the square to `(x,z) in [0,1]^2`, using nuisance variable `-2+4*x` for the left candidate and `2-4*x` for the right, with denominator parameter `-2+4*z` in both. Expand the numerator in tensor-product Bernstein basis of its exact degrees. The reproducible certificate computes the numerator and denominator directly from the integer counts. It checks **26/26 strictly positive Bernstein numerator coefficients**, distributed across the four signs as `3,10,3,10`. The coefficient-expanded denominators also have positive coefficients and positive constants, hence are strictly positive on the entire box.

Therefore `L_73` is minimized at `(-2,2)`, while `L_85` is maximized at `(2,2)`. Their exact difference, evaluated using rational arithmetic, is the stated `delta>0`. This proves the inequality for every point of the continuous nuisance cube, and the corner attains equality. Since the contrast contains three terms with absolute coefficients summing to `1+21/10+11/10=21/5`, two candidates' measurement noise changes its difference by at most `(42/5)*eta`, proving the strict noise margin.

## Reproducibility, evidence strength and next frontier

Companion `R749STT_THREE_READ_73_85_CERT.py` (Python 3, SymPy, fractions) rebuilds the five-source counts, independently checks the R749STR collision, generates the four rational derivative positivity certificates in Bernstein form, evaluates the sharp margin and writes `R749STT_THREE_READ_73_85_RESULTS.json`. Author execution on 2026-11-17: **PASS**, all 26 coefficients strictly positive. No floating-point step enters the proof.

This settles the previously open gap `h=2` in the fixed-`q=73` congruent family. R749STR already proved two-read separation for every `h>=3`, and R749STS settled the one-read threshold at `h=130`. The remaining adjacent-gap question is **the minimal initial observation horizon for `(q,p)=(73,79)`**; it may require a nonlinear observer or a longer exact collision/separation certificate. A separate future problem is to construct an actual provenance-preserving typed BRC/Port/Cell observer map, verifying its allowed future operations.
