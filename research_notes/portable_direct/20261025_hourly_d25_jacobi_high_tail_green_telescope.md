# D25/LIFT — exact signed Jacobi high-rank telescope and one-dimensional endpoint obstruction

Date: 2026-10-25. Role: TASK_RESEARCH. **New portable mathematical lemma, author-derived and author-exact-checked; UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CHECKPOINT.** Parent Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; mother Objective `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` is unchanged.

## Connection with the open unit

The already established second-parameter-jet equation is inhomogeneous, with an unavoidable terminal `-4 z^p (mod p)`. The previous result established a no-polynomial-primitive shortcut. We now identify exactly **which source ranks can compensate that term inside the Jacobi differential operator**, and construct an actual signed polynomial telescope of the isolated terminal and critical-rank ports. This does **not** yet pair with the reflected Clausen corner, so the D25/LIFT hard congruence remains open.

## Theorem A: exact rational high-tail telescope

Let `p=6m+1≥7` be prime and retain the **original** finite Jacobi source

\[
b_n(x)=\frac{(-x)_n(-2x)_n}{(n!)^2},\qquad
\mathcal L_m=\theta^2-z(\theta-m)(\theta-2m),\quad
\theta=z\frac{d}{dz}.
\]

Define its **second parameter-jet high-rank carrier**, without taking a field-observer quotient first,

\[
G_{\rm high}(z)=\sum_{n=2m+1}^{p-1}b_n''(m)z^n.
\]

For every integer `2m+1≤n≤p-1`, both numerator Pochhammer factors have simple zeros and hence

\[
\boxed{\displaystyle
b_n''(m)=
\frac{4(-1)^m m!(2m)!(n-m-1)!(n-2m-1)!}{(n!)^2}.}
\]

Writing `w_{p-1}=b_{p-1}''(m)/2`, one obtains an **exact rational identity**:

\[
\boxed{\displaystyle
\mathcal L_m G_{\rm high}
=\frac{4(-1)^m}{\binom{2m}{m}}z^{2m+1}
-40m^2w_{p-1}z^p.}
\]

All ranks `2m+2,\ldots,p-1` cancel *exactly*, not just modulo p. Using the prior authenticated-by-algebra (not native-admitted) terminal residue `-40m²w_{p-1}≡-4 (mod p)`, the finite-field reduction is

\[
\boxed{\displaystyle
\mathcal L_m G_{\rm high}
\equiv a_p z^{2m+1}-4z^p\pmod p,
\qquad
a_p=\frac{4(-1)^m}{\binom{2m}{m}}\in\mathbb F_p^\times.}
\]

Thus the terminal anomaly **does have a signed Jacobi polynomial telescope when and only when a compensating critical-rank source is retained**. This does not contradict the earlier no-go result for the isolated `-4z^p` (and does not imply a full LIFT telescoper).

**Exact proof.** For `n≥2m+1` the products `(-x)_n` and `(-2x)_n` each vanish simply at `x=m`; differentiating their product twice gives the displayed factorial coefficient. Differentiating the exact hypergeometric coefficient recurrence twice, where the value and first jet both vanish, gives

\[
(n+1)^2b_{n+1}''(m)=(n-m)(n-2m)b_n''(m).
\]

In the coefficient of `z^n` in `\mathcal L_mG_{high}`, this cancels each interior rank. At the first rank `2m+1`, the coefficient is `(2m+1)^2 b_{2m+1}''(m)=4(-1)^m/\binom{2m}{m}`. At the last exterior rank `p`, it is `-(5m)(4m)b_{p-1}''(m)=-40m²w_{p-1}`. The sum telescopes exactly.

## Theorem B: explicit Jacobi range criterion modulo p

For `S(z)=\sum_{n=0}^p s_nz^n\in\mathbb F_p[z]` with `\deg S≤p`, consider the equation

\[
\mathcal L_mG=S,\qquad \deg G≤p-1.
\]

Let `j_*=2m+1`. For `j_*≤j≤p-1`, define the nonzero **source-rank Green weights**

\[
\boxed{\displaystyle
\lambda_j=
\frac{(m+1)(2m+1)}{j^2}
\prod_{k=j+1}^{p-1}\frac{(k-1-m)(k-1-2m)}{k^2}\in\mathbb F_p^\times.}
\]

Then `S` has such a polynomial preimage **if and only if**

\[
\boxed{\quad s_0=0
\quad\text{and}\quad
\Omega_p(S):=s_p+\sum_{j=2m+1}^{p-1}\lambda_js_j=0.\quad}
\]

The first critical weight has the closed form

\[
\boxed{\displaystyle
\lambda_{2m+1}=(-1)^m\binom{2m}{m}\pmod p.}
\]

This gives a precise **one-dimensional endpoint obstruction** after excluding the obvious constant coefficient. In particular, a source supported entirely below rank `2m+1` cannot compensate a nonzero terminal `s_p`.

**Proof.** Write `G=Σ_{n=0}^{p-1}g_nz^n`. For `1≤n≤p-1` the equation is

\[
n^2g_n=(n-1-m)(n-1-2m)g_{n-1}+s_n.
\]

Since these `n` are nonzero in `\mathbb F_p`, this recursion always works (choose `g_0=0`). At `n=m+1` and `n=2m+1`, the multiplier of `g_{n-1}` vanishes, so later `g_{p-1}` depends only on `s_j` for `j≥2m+1`. Expanding the recursion gives

\[
(p-1-m)(p-1-2m)g_{p-1}
=\sum_{j=2m+1}^{p-1}\lambda_js_j.
\]

At `n=p`, `p^2g_p=0` in the field, so the remaining coefficient condition is exactly `\Omega_p(S)=0`. It is necessary and sufficient, proving the criterion.

The first weight's factorial form follows by expanding the product:

\[
\lambda_{2m+1}=
\frac{(m+1)(2m+1)(5m-1)!(4m-1)!((2m)!)^2}
{m!((6m)!)^2}.
\]

Wilson's theorem and complementary-factorial relations yield
`(5m-1)!(m+1)! ≡ (-1)^{m+2}`, `(4m-1)!(2m+1)! ≡ 1`, and `((6m)!)² ≡ 1 (mod p)`. Substitution simplifies the weight to `(-1)^m(2m)!/(m!)²`, as claimed.

Apply the criterion to `S=-4z^p`: `\Omega_p(S)=-4\neq0`, so **no polynomial of degree ≤p-1** can produce the pure anomaly. Apply it to `S=a_pz^{2m+1}-4z^p`: `\Omega_p(S)=\lambda_{2m+1}a_p-4=0`, and Theorem A constructs the required preimage explicitly. This is the precise signed compensation mechanism.

## Exact verification

The companion [integer/rational checker](20261025_hourly_d25_jacobi_high_tail_green_telescope_check.py) performs four exact rational `Fraction` tests (`m=1,2,3,4`) of **every middle rank and both terminal coefficients**, plus mod-p tests for all 35 primes `7≤p≤373, p≡1 mod 6` and `p=1327,19963`. All **37** prime tests pass. Each prime test independently compares the high-tail recurrence with the direct endpoint factorial, computes the full adjoint weights, checks the critical weight, and verifies `\Omega_p(\mathcal L_m z^n)=0` for all `0≤n≤p-1`.

| p | critical rank `2m+1` | `a_p` | `\lambda_{2m+1}` | product mod p |
| ---: | ---: | ---: | ---: | ---: |
| 7 | 3 | 5 | 5 | 4 |
| 13 | 5 | 5 | 6 | 4 |
| 19 | 7 | 15 | 18 | 4 |
| 373 | 125 | 343 | 348 | 4 |

No floating-point calculation, Native BRC execution, original-class CM/Frobenius experiment, formal checker, independent mathematical review or native Source checkpoint is represented by these author tests.

## BRC/source composition and next frontier

The exact operator, original Pochhammer rank `n`, first and second parameter jets, signed source coefficients, p-adic valuation and the field point observer remain separately typed. The **source rank `2m+1` cannot be replaced by an unlabelled constant**: its identity and signed amplitude are what cancel the external terminal residue. This is a source-preserving partial composition of the existing BRC information-fidelity methodology, not a native transfer theorem into the six-axis spatial ontology.

**New do-not-repeat:** do not seek a polynomial preimage of *bare* `-4z^p` or attempt a correction supported solely below rank `2m+1`; both are excluded by the exact range criterion. Do not reinterpret this partial signed telescope as proof of `\Delta_p=R_{ref,p} mod p`.

**Next smallest action:** insert the concrete `G_{high}` split into the already-proved D25 source-bridge at `z=1/2` and examine whether the *remaining low-jet term* matches the reflected Clausen corner `T_{jet,p}`, retaining signed critical rank and the endpoint. The open uniform LIFT identity is still

\[
B_{01,p}+A_2H_0/72-T_{jet,p}\equiv0\pmod p
\quad\text{for every }p\equiv13,19\pmod{24}.
\]

Preserve current Source claim/Result frontier, original class `H_0/B_0`, `[X]U mod p²`, Frobenius normalization and kappa evidence requirements; no canonical authorization or native CM run has been obtained in this portable subunit.
