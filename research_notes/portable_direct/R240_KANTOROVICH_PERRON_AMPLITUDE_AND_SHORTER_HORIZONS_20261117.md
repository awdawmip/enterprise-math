# R240 — Kantorovich lower bound for Perron amplitude; shorter uniform one-mode horizons

2026-11-17 (Asia/Shanghai). **AUTHOR_PROVED / EXACT_RATIONAL_CERTIFICATE / NOT_REVIEWED**.

## Provenance and precise model

This is an independent portable continuation of the exact scalar seven-source stationary sticky-reset observer of R234–R239. Scientific inputs remain frozen at `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`; the R234 rational model family is pinned at `37786e0e0acb51ce36fa9ae68ec84ce28ad46dc6`, R236 bounds at `2bb1983d60bbd3312662e8a52b7df065e03e2ef6`, and R239 one-mode tail at `f052feb457712a8f621e9111404e7da69a542196`. The conclusion concerns the scalar expected principal-ideal-cardinality observer only, not the native six-axis/one-time P000 world or the BRC signed-port/provenance/cross-moment carrier.

For all real `39/100 < s < 41/100`, let `alpha_i(s)`, `pi_i(s)` and `b_i=(1-alpha_i)pi_i` be R234's seven-state strictly positive, reversible chain; source 0 is neutral and k=6, tail length L=2. Define

\[
 Z=\sum_{i=0}^6\frac{b_i}{(1-\alpha_i)^2},\quad z_3=\frac{50}{1089},\quad a=\frac{\pi_0}{1-\alpha_0}=\frac{65}{192},
\]
\[
 S=\sum_{i\ne3}\frac{b_i}{(1-\alpha_i)(r-\alpha_i)},\qquad Q=\sum_{i\ne3}\frac{b_i}{(r-\alpha_i)^2}.
\]
R235–R239 give `594323/600000 < r(s) < 1`, the Perron coefficient `A=W_5 S²/(Z Q)`, total nonconstant spectral mass `T`, and

\[
0\le \frac{R_n}{A r^{n-1}}<\frac{T-A}{A}\,q^{n-1},\quad q=\frac{14771007}{14858075},\quad n\ge2.
\]

## Theorem: improved uniform mass fraction and certified thresholds

For every real `39/100 < s < 41/100`,

\[
\boxed{\frac{A(s)}{T(s)}>\eta_{240}:=\frac{304910592000}{2463633795601}>0.1237.}
\]

Consequently, for all integers n>=2,

\[
\boxed{0\le\frac{R_n(s)}{A(s)r(s)^{n-1}}<\frac{1-\eta_{240}}{\eta_{240}}\left(\frac{14771007}{14858075}\right)^{n-1}.}
\]

In particular the bound certifies relative errors < 1% for **n >= 1118** and < 0.1% for **n >= 1510**, simultaneously for every real parameter in the family. These are the first certified values of this explicit majorant; the actual error may fall below tolerance sooner. R239 had bounds 1477 and 1869 under its earlier amplitude estimate.

## Proof

1. **Exact normalization lower bound.** Substitute R234's alpha and pi into Z and simplify:

\[
 Z(s)=\frac{5(4538s-7153)}{16632(s-1)},\qquad
 Z'(s)=\frac{13075}{16632(s-1)^2}>0.
\]

Hence, for all real s in the open interval,

\[
 Z(s)>Z(39/100)=\frac{122345}{46116}>\frac{53}{20}=:Z_*.
\]

2. **Uniform spread of the retained spectral ratios.** Set

\[
 z_i=\frac{b_i}{(1-\alpha_i)^2}>0,\qquad
 y_i=\frac{1-\alpha_i}{r-\alpha_i}\quad(i\ne3).
\]
Since `r<1`, `y_i>1`. Every retained alpha is < `39/50` (R234), and

\[
21\cdot\frac{594323}{600000}>20+\frac{39}{50}.
\]

Thus `21r>20+alpha_i`, equivalently `y_i<21/20=:M`. Write `U=sum_{i ne 3} z_i=Z-z_3`, use the probability weights `w_i=z_i/U`, and put `m=Σw_i y_i`. The elementary inequality `(y_i-1)(M-y_i)>=0` gives

\[
 \sum_i w_i y_i^2\le (1+M)m-M
 \le \frac{(1+M)^2}{4M}m^2.
\]

The last inequality is the square `((1+M)m-2M)^2>=0` divided by `4M`. Therefore

\[
 \frac{S^2}{Q}
 =U\frac{(\sum w_i y_i)^2}{\sum w_i y_i^2}
 \ge \frac{4M}{(1+M)^2}U
 =\frac{1680}{1681}(Z-z_3).
\]

3. **Use the stationary source-0 mass rather than bounding T by Gamma0.** R220's exact weights give `W5=86400`, `Gamma0=889200`, `Gamma1=655776`, and

\[
 T=\Gamma_1+(\Gamma_0-\Gamma_1)\rho_0,\qquad
 \rho_0=\frac{a}{Z},\quad a=65/192.
\]

Thus

\[
 \frac{A}{T}\ge
 \frac{W_5(1680/1681)(Z-z_3)}{\Gamma_1 Z+(\Gamma_0-\Gamma_1)a}.
\]

The right side is strictly increasing in Z>z3, since the numerator's derivative cross-product is `Gamma1*z3+(Gamma0-Gamma1)*a>0`. Insert `Z>Z_*=53/20` and the exact constants to obtain

\[
\frac{A}{T}>\frac{86400(1680/1681)(53/20-50/1089)}{655776(53/20)+233424(65/192)}
=\frac{304910592000}{2463633795601}.
\]

4. **Exact integer threshold check.** R239 established `0<=R_n<=(T-A)theta^(n-1)` and `theta/r<q<1`. Since `(T-A)/A<(1-eta240)/eta240`, the stated majorant follows. Writing `eta240=N/D`, `q=u/v`, its strict crossing below `1/d` is equivalent to the exact integer comparison

\[
 d(D-N)u^{n-1}<Nv^{n-1}.
\]

For `d=100`, the comparison first holds at `n=1118`, and fails at `n=1117`; for `d=1000`, it first holds at `n=1510`, and fails at `n=1509`. Because `0<q<1`, each bound persists for all larger n. QED.

## Reproduction and limits

Run `python3 R240_kantorovich_uniform_amplitude_check.py`; it uses Python standard-library `fractions.Fraction` and exact integer powers, recomputes the rational coefficients, and binary-searches the first strict integer thresholds. The accompanying `R240_verification.json` is the output of the actual local run, status `PASS`. The symbolic proof covers the entire open real interval; the executable certificate verifies exact arithmetic, not an independent formal proof. `NOT_REVIEWED`; native typed BRC `EffectHistogram` integration `NOT_EXECUTED`.

## Next exact questions

Improve the `1680/1681` factor using state-specific spectral ratios and certify the first *actual* error horizons (rather than the upper-majorant horizons), with rigorous finite interval subdivision over s and guaranteed positive spectral coefficients. Compare exact bit complexity, including root enclosure and output accuracy, with 230-order recurrence and 256-state mask propagation. Any native BRC observer must preserve signed directions, ports, source, provenance, branch multiplicity, rational weights and cross moments.
