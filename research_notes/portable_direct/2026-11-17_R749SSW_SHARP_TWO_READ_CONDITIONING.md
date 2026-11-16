# R749SSW — Exact two-read conditioning at a known cutoff

**Date:** 2026-11-17. **Status:** AUTHOR_EXACT_NOT_REVIEWED. **Scope:** frozen five-distinct-labeled-source auxiliary scalar observation model, not native X6/BRC dynamics. **Scientific input pin:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Follows R749SST (11-read global exact injectivity), R749SSU (finite inversion) and R749SSV (sharp phase envelopes), preserving their author-only evidence status.

## Model and new theorem

With the first two weight-one sources **distinct and labeled**, set
[
Omega_q={(k_1,ldots,k_5)inmathbf Z_{ge0}^5:
k_1+k_2+2k_3+3k_4+6k_5le q-1},quad
C_q=|Omega_q|,quad T_q=sum_{kinOmega_q}k_1.
]
For every integer (qge6), and every common pair (e,din[-2,2]), put
[
X_q(e,d)=rac{T_q+e}{C_q+d},qquad
Y_q(e,d)=q^3X_q(e,d)-rac{S(q)}{108},
]
where (S(q)=18q^4+54q^3-345q^2+2070q-16315), exactly as in R749SSV.

**Theorem 1 (sharp normalized inter-read gap).** For *all* integers (qge6) and *all* common continuous errors (e,din[-2,2]),
[
oxed{X_{q+6}(e,d)-X_q(e,d)>1.}
]
The constant 1 is sharp: for every fixed admissible pair, the left-hand side converges to 1 as (q	oinfty) along any residue class modulo 6.

**Corollary 1 (known-cutoff two-read injectivity).** For any fixed integer (qge6), the pair ((Y_q,Y_{q+6})) uniquely determines both (e) and (d) on the entire admissible square. Given the readings (y_0,y_1), let
[
x_0=rac{y_0+S(q)/108}{q^3},qquad
x_1=rac{y_1+S(q+6)/108}{(q+6)^3}.
]
The exact inverse is
[
oxed{d=rac{x_0 C_q-T_q-x_1 C_{q+6}+T_{q+6}}{x_1-x_0}},
qquad
oxed{e=x_0(C_q+d)-T_q}.
]
The denominator (x_1-x_0) is strictly larger than 1 on the model image. In particular, the Jacobian of the two-read map never vanishes. Its normalized determinant is ((x_0-x_1)/[(C_q+d)(C_{q+6}+d)]).

**Corollary 2 (explicit local error stability).** For two admissible error pairs ((e,d)) and ((e',d')) at the *same known* cutoff, let
(delta=max(|X_q(e,d)-X_q(e',d')|,|X_{q+6}(e,d)-X_{q+6}(e',d')|)).
Then
[
|d'-d|le (C_q+C_{q+6}+4)delta
]
and
[
|e'-e|leleft[(C_q+2)+rac{T_q+2}{C_q-2}
(C_q+C_{q+6}+4)ight]delta.
]
If the two raw (Y) vectors differ by at most (arepsilon) in sup norm, it suffices to set (deltalearepsilon/q^3). If a noisy measurement and an admissible fitted vector each deviate by at most (arepsilon) from one another's common observed data, replace (arepsilon) by (2arepsilon) for the two-model comparison. These are conservative, exact cutoff-dependent bounds.

## Proof by six residue-class polynomial positivity

The exact generating functions are
[
sum_{qge0} C_q z^q =
rac{z}{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},quad
sum_{qge0} T_q z^q =
rac{z^2}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
]
All poles are sixth roots of unity. At (z=1) their respective maximal orders are 6 and 7, so (C_{6+r+6k}) and (T_{6+r+6k}) are **exact** polynomials in (kge0) of degrees 5 and 6, for each (r=0,ldots,5). Interpolation using 6 and 7 values therefore determines the polynomials globally; the certificate reconstructs the coefficients from the original labeled-source generating function.

Write (C=C_q, C'=C_{q+6}, T=T_q, T'=T_{q+6}) and
(A=T'C-TC', B=T'-T, D=C'-C).
Here (D>0) because the larger cutoff admits strictly more labeled configurations; also (Cge C_6=41), hence (C+d,C'+d>0).

Direct expansion gives
[
(C+d)(C'+d)ig(X_{q+6}(e,d)-X_q(e,d)-1ig)
=N(e,d)
]
where
[
N(e,d)=A+dB-eD-(C+d)(C'+d).
]
For fixed (d), this expression is decreasing in (e), since (D>0). For (e=2), it is a concave quadratic in (d), since the (d^2)-coefficient is (-1). Consequently its minimum over the full square occurs among ((e,d)=(2,-2),(2,2)).

For each residue (r), substitute (q=6+r+6k) into these two exact endpoint expressions and expand in nonnegative integer (k). Every coefficient in each of the resulting **12 degree-eight polynomials** is a *strictly positive rational number*. The global minimum coefficient is (69/40). The degree-zero coefficients, an additional convenient auditable checksum, are:

| (r) | (N(2,-2)) at (k=0) | (N(2,2)) at (k=0) |
|---:|---:|---:|
| 0 | 39 | 1679 |
| 1 | 945 | 3341 |
| 2 | 2184 | 5588 |
| 3 | 4527 | 9239 |
| 4 | 8685 | 15065 |
| 5 | 14859 | 23339 |

Coefficient positivity establishes (N(e,d)>0) for the entire continuous square, **at every integer (qge6)**. Division by the two positive denominators proves Theorem 1. The code independently checks (D)'s positive coefficients.

For sharpness, the coefficient of (k^5) in each phase polynomial (C_{6+r+6k}) equals the coefficient of (k^6) in (T_{6+r+6k}), namely (9/5). Their rational quotient therefore behaves as (k+	ext{constant}+O(1/k)) for fixed (e,d). Taking one step (kmapsto k+1) proves the limit 1.

To obtain Corollary 1, solve the two linear equations (e-x_i d=x_i C_i-T_i); their determinant is (x_1-x_0>1). For Corollary 2, subtract the two states' equations to get
[
(e'-e)-x_i(d'-d)=delta_i(C_i+d'),quad |delta_i|ledelta.
]
Eliminating (e'-e), using (x_1-x_0>1) and (|C_i+d'|le C_i+2), yields the (d) bound. The (e) bound follows from the (i=0) equation and
(0<x_0le (T_q+2)/(C_q-2)).

## Exact example and computational scope

At (q=6,e=2,d=-2): (C_6=41,T_6=50,C_{12}=380,T_{12}=881), so
[
X_6=4/3,quad X_{12}=883/378,quad X_{12}-X_6=379/378=1+1/378.
]
The strict inequality is close to equality already at this small cutoff.

**Reproduction:** Python 3, SymPy; execute `python research_notes/portable_direct/R749SSW_TWO_READ_CONDITIONING_CERT.py`. It uses only exact integers/rationals, verifies all 12 positivity polynomials, the (D) polynomials, highest coefficients and the example; it outputs a JSON PASS record. The generating-function pole argument is the mathematical proof that finite interpolation determines the full infinite residue-class sequences. No floating-point grid or finite-(q) extrapolation is used.

**Relation to the existing frontier.** R749SST supplies the separately needed unknown-(q) 11-read injectivity theorem. Here (q) is fixed and known, and the result gives a uniform conditioning certificate for elimination of its two error parameters; it strengthens the previously used two-read inversion step. The six-step interval is the **auxiliary scalar observation offset**, not a native heartbeat duration. Source labels, multiplicities, joint composite directions, common errors and future observer fibers remain typed and uncollapsed; any BRC/X6 transfer needs a genuine preservation map.

**Next questions:** derive certified finite-range cross-(q) noise separation using this stable parameter elimination; check whether unknown-(q) global injectivity requires 5–10 rather than 11 reads; construct a signed/source-preserving BRC carrier for the labeled joint combinatorial population.
