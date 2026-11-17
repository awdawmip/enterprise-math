# R749STA — Infinite exact three-read collisions; fourth-read fiber residual

**Date:** 2026-11-17. **Evidence:** AUTHOR_EXACT_NOT_REVIEWED (local exact SymPy author certificate PASS; independent review pending). **Mode:** independent portable scalar research. **Frozen scientific input:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. **Predecessor:** R749SSZ, PR #2608, commit `20595afd5c42ceb593e2e83286ffbcf831a5c80f`. Prior upper bound: R749SST (11 exact observations suffice globally).

## The frozen labeled-source observer

Use five **distinct** labeled sources with weights `(1,1,2,3,6)`. For every integer `q>=6`, let

\[
\Omega_q=\{k\in\mathbb{Z}_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le q-1\},\quad
C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q}k_1.
\]
\[
S(q)=18q^4+54q^3-345q^2+2070q-16315,\qquad
Y_q(e,d)=\frac{q^3(T_q+e)}{C_q+d}-\frac{S(q)}{108},
\]
\[
\mathcal O_q^{(m)}(e,d)=
(Y_q(e,d),Y_{q+6}(e,d),\ldots,Y_{q+6(m-1)}(e,d)).
\]

The error pair `(e,d)\in[-2,2]^2` is **shared across all reads within each candidate**, with independent errors allowed between different candidates. The six-step index is an auxiliary ordered readout, not a native physical-time identification.

## Main theorem

**For every integer `q>=73` with `q\equiv1\pmod6`, put `p=q+4\equiv5\pmod6`. There exist admissible real parameters `d_q\in(-1,0)` and `E_q,D_q\in(-2,2)` such that**

\[
\boxed{\mathcal O_q^{(3)}(-3/2,d_q)
=\mathcal O_{q+4}^{(3)}(E_q,D_q).}
\]

All four error parameters lie strictly inside `(-2,2)`. Consequently three **exact** readings cannot globally identify an unknown unbounded cutoff, or its residue modulo six. Combining this infinite counterfamily with the established 11-read sufficient upper bound gives

\[\boxed{4\le m_*\le 11,}\]

where `m_*` denotes the smallest observation count sufficient to distinguish **every pair** of different cutoffs under the frozen model. The new lower bound improves R749SSZ's `m_*\ge3`.

## Exact construction

The distinct-source generating functions are

\[
\sum_{q\ge0}C_qz^q=\frac{z}{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\quad
\sum_{q\ge0}T_qz^q=\frac{z^2}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]

Multiplying these by `(1-z^6)^6` and `(1-z^6)^7`, respectively, yields finite numerator polynomials of degrees 23 and 29. On each progression `q=6+r+6j` these generate **exact** degree-five and degree-six rational quasipolynomials for `C_q,T_q`. The companion program constructs the components from the finite numerator coefficients and exact binomial polynomials, including the first `j=0` boundary (excluded shifts yield zero binomial coefficients), so the proof covers the complete infinite progression rather than extrapolating a finite sample.

Fix the first candidate's `e=-3/2` and let `d\in[-1,0]`. Write `a_j=q+6j`, `b_j=q+4+6j`, `j=0,1,2`. Define

\[
y_j=Y_{a_j}(-3/2,d),\quad
x_j=\frac{y_j+S(b_j)/108}{b_j^3},\quad
v_j=x_jC_{b_j}-T_{b_j}.
\]

The `j`th desired equality is exactly `E-x_jD=v_j`. Solving `j=0,1` yields the explicit **rational functions**

\[
D(q,d)=\frac{v_0-v_1}{x_1-x_0},\qquad E(q,d)=v_0+x_0D(q,d).
\]

The third equality holds if and only if the collinearity defect

\[
F(q,d)=(v_0-v_1)(x_2-x_0)-(v_0-v_2)(x_1-x_0)
\]

vanishes. Exact rational reduction writes `F=N/H`, with bidegrees `deg(N)=(21,3)`, `deg(H)=(24,3)` in `(q,d)`. The reduced `E,D` each have numerator and denominator of bidegrees `(16,2)`.

## Global positivity certificate (450 positive coefficients)

For `q=73+k`, `k\ge0`, substitute `d=-u/(1+u)`, `u\ge0`. For every polynomial `P(q,d)` tested, expand

\[
(1+u)^{\deg_d P}P(73+k,-u/(1+u)).
\]

If every monomial coefficient is strictly positive, then `P(q,d)>0` throughout `q\ge73, -1<d\le0`; the endpoint `d=-1` is checked by continuity or directly.

| Exact checked polynomial | Positive coefficients | Smallest coefficient |
|---|---:|---:|
| `-N(q,-1)` | 22 | 960048 |
| `N(q,0)` | 22 | 1139472 |
| `H(q,d)` | 100 | 2187 |
| `den(E)` | 51 | 52488 |
| `2den(E)+num(E)` | 51 | 103896 |
| `2den(E)-num(E)` | 51 | 71064 |
| `den(D)` | 51 | 4374 |
| `2den(D)+num(D)` | 51 | 3834 |
| `2den(D)-num(D)` | 51 | 9288 |

The exact certificate verifies **all 450 coefficients** using integer/rational arithmetic. Thus `F(q,-1)<0<F(q,0)`, the entire connecting path is denominator-safe, and `-2<E(q,d),D(q,d)<2` everywhere on it. By the intermediate value theorem a root `d_q\in(-1,0)` exists for every `q=73+6j`, proving the theorem.

## Exact algebraic witness at q=73

For `q=73,p=77`, the third-read equality specializes to the integer cubic

\[
\begin{aligned}
0={}&-15618855526087614323456d^3\\
&+251745728589325682154438351145d^2\\
&+1051525031591217484057132026985205d\\
&+961772529408317889570818785924418.
\end{aligned}
\]

The two rational endpoints `-1` and `-9/10` have opposite signs. Exact Sturm root counting gives precisely **one** root `d_*\in(-1,-9/10)`. For orientation, `d_*\approx-0.914845769039641`, `E(73,d_*)\approx0.526270191134656`, and `D(73,d_*)\approx-1.03983206335047` (approximations are not the proof).

For the **fourth** reading define

\[
R_4(d)=Y_{95}(E(73,d),D(73,d))-Y_{91}(-3/2,d).
\]

The fourth-read rational numerator has exact polynomial `gcd=1` with the cubic over `\mathbb Q[d]`; hence `R_4(d_*)\ne0` rigorously. Numerically `R_4(d_*)\approx1.35558431\times10^{-5}`. This provides a concrete BRC-type future-observer fiber witness: two distinct states with the same first three readouts can differ on the next permitted readout.

## Reproduction, semantics and continuation

Run `python R749STA_INFINITE_THREE_READ_COLLISION_CERT.py` with Python 3 and SymPy. The script reconstructs the exact generating-function components, rational collision maps, endpoint signs, six parameter guards, the Sturm witness and the fourth-read gcd. It outputs `R749STA_INFINITE_THREE_READ_COLLISION_RESULTS.json` and reports `PASS 450 positive coefficients; q73 fourth-read gcd 0`. Mathematical verification is by **symbolic polynomial certificates on an infinite domain**, not a numerical grid.

The result concerns a five-labeled-source auxiliary scalar observer. A native X6/BRC dynamical application requires an explicit state/carrier/port embedding, its third spatial slice component where relevant, and preservation of provenance, order and future operations. P000's six spatial dimensions and independent time dimension remain unchanged.

**Next open question:** Can four exact reads collide at arbitrarily large cutoffs, or are four eventually sufficient for residue identification? Another useful direction is a compact future-residual repair coordinate and a positive cutoff-dependent noise margin.

**Review status:** AUTHOR_EXACT_NOT_REVIEWED. No shared X6 Task CLAIM, Result, Review or Foundation promotion is asserted.
