# PREFIX-1040 — Narrow-band rational envelopes and two enlarged positive spectral neighborhoods

Date: 2026-11-23 (Asia/Shanghai). Parent: PREFIX-1039. Classification: AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_CERTIFICATE / NOT_INDEPENDENTLY_REVIEWED.

## Immutable scope and attribution

Frozen scientific foundation: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json` (P000 V5). Preserve Stage46 signed BRC candidate `W=J12-6I12`, incoming `-e1`, blocked bidirectional Link `{0,e1}`, one outgoing negative step, and the six-dimensional X6 Cell–terminal-port–grade joint observer, including branch identity, sign, multiplicity and provenance. This note concerns **only** the inherited auxiliary six-phase scalar spectral representation. It does not perform an original typed BRC operation, a new classical comparison experiment, or native residual attribution. Its native relationship remains `NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION`.

Source premises:
- PREFIX-1037, commit `928461a6f8c675b9a7bd38586cf47db9d25835e9`, gives conditional endpoint certificates `g(4)>6371/60` and `g(16)>919/90`.
- PREFIX-1039, commit `37685de6636af8f51f50e73fd2c1f157323733a4`, gives the full inherited kernel `K(t;y)` and the finite-part/tail split under its stated Bessel bounds.
- PREFIX-1035, commit `ebccbb436685bafe6d697ace256ad93b39c0c50f`, gives the separate conditional Picard–Fuchs route. No ODE integration is performed here.

## Result — explicit rational positive neighborhoods

Assuming the inherited kernel identity and Bessel bounds in PREFIX-1037/1039, the continuous scalar density `g` obeys:

\[
\boxed{ |x-y|\le 1/5000,\quad x,y\in[4-10^{-4},4+10^{-4}]
 \ \Longrightarrow\ |g(x)-g(y)|<104400\sqrt{|x-y|}.}
\]

\[
\boxed{ |x-y|\le 1/5000,\quad x,y\in[16-10^{-4},16+10^{-4}]
 \ \Longrightarrow\ |g(x)-g(y)|<291700\sqrt{|x-y|}.}
\]

In particular, using exactly the inherited certified endpoint lower bounds,

\[
\boxed{|y-4|\le10^{-6}\quad\Longrightarrow\quad g(y)>7/4,}
\qquad
\boxed{|y-16|\le10^{-9}\quad\Longrightarrow\quad g(y)>49/50.}
\]

These are 10x and 2x enlargements of the previously *radius-certified* neighborhoods in PREFIX-1039. There are also higher-margin interior sub-bands:

\[
|y-4|\le 1/4{,}000{,}000 \Longrightarrow g(y)>53;
\quad
|y-16|\le1/1{,}600{,}000{,}000\Longrightarrow g(y)>29/10.
\]

The theorem is restricted to the derived scalar density, and is conditional on its inherited representation. No claim about full-interval positivity or original native X6/BRC positivity follows.

## Proof — local interval optimization

PREFIX-1039 proves, for any band with valid rational brackets `r_-≤√y≤r_+`, that its exact coefficient envelopes `S,M,L` satisfy `|\partial_y K(t;y)|≤S` on `0≤t≤1`, and on `t≥1` satisfy `|K(t;y)|≤M t^{-3/2}`, `|\partial_yK(t;y)|≤L t^{-1/2}`. For `δ=|x-y|>0`, finite integration through `T=q/δ≥1` plus two absolute tails yields

\[
|g(x)-g(y)|\le\big(S+2L\sqrt q+4M/\sqrt q\big)\sqrt\delta,\qquad q\ge1.
\tag{1}
\]

This bound uses differentiation only under a finite integral. Its formal unconstrained best splitting parameter is `q_*=2M/L`, with coefficient `S+4√(2LM)` when `q_*≥1`. To retain a fully rational certificate, we use `√q=3/2` near 4 and `√q=7/3` near 16.

For each center `c`, set `a=c-1/10000`, `b=c+1/10000`. At `c=4`, use `r_-=19999/10000`, `r_+=20001/10000`; at `c=16`, use `r_-=39999/10000`, `r_+=40001/10000`. Direct integer square comparison gives `r_-²≤a` and `r_+²≥b` in both cases.

Recalculate the *same* coefficient formulas used in PREFIX-1039, with
\[
v=\max(|36-2a|,|36-2b|),\quad w=\max(|17a-91|,|17b-91|),\quad z=\max(|a-6|,|b-6|),\quad R=(2r_-)^{-1}.
\]
The polynomial coefficient envelopes are
\[
\begin{aligned}
\mathcal H&=b^2(36-a)^2,&\mathcal H_1&=2b(36-a)v,&\mathcal H_2&=2v^2+4b(36-a),\\
\mathcal P&=b(36-a)w,&\mathcal P_1&=vw+17b(36-a),\\
\mathcal A&=2\mathcal H_1+\mathcal P,&\mathcal A_1&=2\mathcal H_2+\mathcal P_1,\\
\mathcal B&=\mathcal H/r_-,&\mathcal B_1&=\mathcal H_1/r_-+\mathcal H/(2r_-^3),\\
\mathcal C&=12(11+b),&\mathcal C_1&=12,\\
\mathcal D&=r_+z,&\mathcal D_1&=r_++Rz,\\
\mathcal E&=2b,&\mathcal E_1&=2.
\end{aligned}
\]
Then
\[
\begin{aligned}
S&=\tfrac15[\mathcal A_1+\mathcal A R+\mathcal B_1+\mathcal B R+
\mathcal C_1(\mathcal D+\mathcal E r_+)+\mathcal C(\mathcal D_1+\mathcal D R+\mathcal E_1r_++\mathcal ER)],\\
M&=\tfrac25[\tfrac{11}{10}\mathcal A+2\mathcal B+\mathcal C(2\mathcal D+6\mathcal E)],\\
L&=\tfrac25[\tfrac{11}{10}\mathcal A_1+2\mathcal AR+2\mathcal B_1+4\mathcal BR+
\mathcal C_1(2\mathcal D+6\mathcal E)+\mathcal C(2\mathcal D_1+4\mathcal DR+6\mathcal E_1+14\mathcal ER)].
\end{aligned}
\tag{2}
\]

Apply equation (2) with exact rational arithmetic to the two bands. The resulting coefficients in (1) are:

| Center | `√q` | Exact coefficient `S+2L√q+4M/√q` | Strict rational upper bound |
|---|---|---|---|
| 4 | 3/2 | `521694816381896240240236487467/4999250037499375000000000` | 104400 |
| 16 | 7/3 | `54428786298869178867337710608401/186652667016663750000000000` | 291700 |

These values are obtained by exact rational substitution in (2); the accompanying program checks the inequalities.

For `|y-4|≤10^{-6}`, equation (1) gives
\[
g(y)>\tfrac{6371}{60}-\tfrac{104400}{1000}
=\tfrac{107}{60}>\tfrac74.
\]
For `|y-16|≤10^{-9}`, since `31622²<10^9` implies `√(10^{-9})<1/31622`,
\[
g(y)>\tfrac{919}{90}-\tfrac{291700}{31622}
=\tfrac{1403809}{1422990}>\tfrac{49}{50}.
\]
Using `√(1/4{,}000{,}000)=1/2000` and `√(1/1{,}600{,}000{,}000)=1/40000` yields the two higher-margin sub-bands. QED, under the cited scalar premises.

## Verification and epistemic state

The local checker `research_notes/portable_direct/PREFIX1040_R6_SHARP_LOCAL_MODULUS_CHECK.py` evaluates (2) using Python standard-library `fractions.Fraction`; it checks both bracket squares, the two exact coefficient inequalities and the four strict positive lower bounds. Local execution output: `EXACT_FRACTION_CERTIFICATE_PASSED`; this is an exact rational verification of the *implications* from PREFIX-1039's established envelope premises, not an independent numerical Bessel study or native BRC propagation.

The result is an AUTHOR conditional proof, not independently reviewed or promoted. PREFIX-1039's wide-band `g>50` and `g>5/2` neighborhoods remain valid on their original ranges. This new result trades a lower guaranteed value for a larger certified positive radius.

## Next scientific question

The intrinsic saddle cusp coefficients in PREFIX-1034 are much smaller than these coarse absolute-integral modulus bounds. A useful new unit is to derive **explicit, nonasymptotic remainder control** for the resonant mode and the smooth background of `g` near `y=4,16` (rather than just optimizing the coarse `S,M,L` envelopes), or to construct a verified interval ODE/Spectral band certificate for the gaps. Both routes should preserve the native signed-BRC attribution boundary; an actual native calculation requires the typed BRC interface and its signed joint-observer mapping.

Mother objective `B_fix,odd(32)∈{19,20}` remains open. Prior attribution: historical `EM-DIRECT-FBEA5D / RA-3FB2D033BE6048D8712FF056` denotes source provenance only; no current-session authentication, CLAIM/PROGRESS or Result/Review is asserted.
