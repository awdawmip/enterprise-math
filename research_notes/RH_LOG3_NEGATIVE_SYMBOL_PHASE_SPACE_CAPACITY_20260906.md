# RH `H_log3` negative-symbol outer measure and phase-space capacity certificate

Status: `TASK_RESEARCH / VERIFIED NEGATIVE-SYMBOL OUTER-MEASURE + TRACE-CAPACITY CERTIFICATE / NOT A NEGATIVE-INDEX BOUND / NOT FULL H_LOG3 POSITIVITY / NOT AN RH PROOF`
Date: `2026-09-06`
Researcher-ID: `EM-DIRECT-7C1A42`
Scope: `RH / Weil form / H_log3 / full-line non-pole multiplier / negative frequency set / time-frequency concentration / Galerkin complement`

## 0. Main certified result

For the non-pole Riemann-Weil multiplier relevant to the compact support window

`H_log3 = {f : supp f subset [-log3,log3]}`,

the active prime-power shifts are exactly

`m in {2,3,4,5,7,8}`.

The boundary shift `m=9` is operator-null on this window and must not be retained in the pointwise active comb.

Define the exact active scalar multiplier

`a(t)`
`= Re psi(1/4+i t/2)-log pi`
`  - 2 sum_(m in {2,3,4,5,7,8}) Lambda(m)/sqrt(m) cos(t log m)`.

Let

`E_-={t in R : a(t)<0}`.

A 192-bit Arb interval scan on `[0,4000]`, combined with a separate analytic proof that `a(t)>0` for every `|t|>=4000`, certifies

`boxed: |E_-| <= 88.8666}`.

The corresponding time-frequency concentration operator on `[-log3,log3]` has exact trace

`Tr K_E = (2log3)|E_-|/(2pi)=log3 |E_-|/pi`,

hence

`boxed: Tr K_(E_-) < 31.07657471142701 < 31.2}`.

This is a phase-space capacity certificate. It is not a bound on the negative index of the Weil form and does not prove full-window positivity or RH.

## 1. Exact boundary-null certificate for `m=9`

For any `f` supported in `[-L,L]`, its autocorrelation at displacement `2L` is zero in `L2` sense: the support of `f(x)` and the support of `f(x+2L)` intersect only at a single endpoint, a measure-zero set.

At `L=log3`,

`log 9 = 2 log3`.

Therefore the `m=9` prime-power translation contributes exactly zero to the quadratic form on `H_log3`.

Thus the active prime-power set is

`{m : log m < 2log3, Lambda(m) != 0}`
`= {2,3,4,5,7,8}`.

This is an exact support/observer certificate, not a numerical threshold convention.

## 2. Active absolute comb constant

Define

`A_log3 = 2 sum_(m in {2,3,4,5,7,8}) Lambda(m)/sqrt(m)`.

The production Arb run gives

`A_log3 = 6.34259743608709162639498634971...`.

Therefore the signed trigonometric prime comb obeys the pointwise absolute bound

`|-2 sum Lambda(m)/sqrt(m) cos(t log m)| <= A_log3`.

The actual certified negative-set scan below uses the signed symbol itself, not this absolute envelope. The constant is used only for the high-frequency positivity proof.

## 3. High-frequency positivity beyond `|t|=4000`

A Binet-type representation for the digamma function gives the elementary lower bound, for `t>0`,

`h_inf(t):=Re psi(1/4+i t/2)-log pi`
`>= 1/2 log(1+4t^2)-log(4pi)`
`   -2/(1+4t^2)-1/(3t)`.

Hence

`a(t) >= LB(t)`

where

`LB(t)`
`=1/2 log(1+4t^2)-log(4pi)`
` -2/(1+4t^2)-1/(3t)-A_log3`.

The derivative of the displayed lower bound is strictly positive:

`LB'(t)`
`=4t/(1+4t^2)`
` +16t/(1+4t^2)^2`
` +1/(3t^2) >0`.

The production Arb run certifies

`LB(4000)`
`=0.1134917808347576548455462075057719624... >0`.

Therefore

`boxed: a(t)>0 for every |t|>=4000}`.

All negative-symbol geometry is rigorously confined to the finite band `[-4000,4000]`.

## 4. Arb outer-measure scan on the finite band

Production implementation:

- script: `scripts/rh_log3_negative_symbol_capacity_arb.py`;
- workflow: `.github/workflows/rh-log3-negative-symbol-capacity.yml`;
- source head: `7bf1586a05e621274779cf09afce5c243844e236`;
- workflow run: `34023342294`;
- job: `101459845426`;
- Python `3.13.15`;
- `python-flint==0.9.0`;
- Arb precision: 192 bits.

The half-band `[0,4000]` is recursively split. Each interval cell is evaluated by the complete Arb/acb symbol expression.

- if the resulting ball is strictly negative, the whole cell is certified negative;
- if strictly positive, the whole cell is certified positive;
- if the sign remains unresolved, the cell is split;
- at final width `1e-4`, any unresolved cell is conservatively included in the negative outer set.

The run used `30166` interval evaluations and returned:

- definitely-negative cells: `3334`;
- ambiguous final `1e-4` cells: `614`;
- certified negative half-measure lower: `44.3719`;
- certified negative half-measure outer: `44.4333`.

By evenness,

`88.7438 <= |E_-| <= 88.8666`.

The upper bound is the theorem input used below.

## 5. Exact time-frequency trace identity

Let `P_L` denote multiplication by the spatial-window indicator of `[-L,L]`, and let `P_E=F^(-1) 1_E F` be the orthogonal frequency projection under the convention

`f_hat(t)=integral f(x)e^(-itx) dx`,
`||f||^2=(1/(2pi)) integral |f_hat(t)|^2 dt`.

The time-frequency concentration operator is

`K_E=P_L P_E P_L`.

Its integral kernel has diagonal value `|E|/(2pi)`. Therefore

`Tr K_E = integral_(-L)^L |E|/(2pi) dx`
`= (2L)|E|/(2pi)`
`= L|E|/pi`.

For `L=log3` and the certified outer measure,

`boxed: Tr K_(E_-) <= log3*88.8666/pi}`
`= 31.0765747114270078673900814395...`.

Thus

`boxed: Tr K_(E_-) <31.2}`.

## 6. Rigorous concentration-capacity consequence

Let

`1>=lambda_1>=lambda_2>=...>=0`

be the eigenvalues of `K_(E_-)`.

For any `eta>0`, positivity and the trace identity give the elementary counting inequality

`#{j:lambda_j>=eta} * eta <= sum_j lambda_j = Tr K_(E_-)`.

Therefore

`boxed: #{j:lambda_j>=eta} <= floor(Tr K_(E_-)/eta)}`.

In particular, with `eta=0.99`,

`Tr K_(E_-)/0.99 <31.4`,

so

`boxed: #{j:lambda_j>=0.99} <=31}`.

Interpretation: at most 31 orthogonal compact-window directions can put at least 99% of their Fourier energy inside the negative-symbol region.

This is a **concentration-capacity** statement. It is not a negative-index theorem for the signed Weil multiplier.

## 7. Relation to the verified 32-dimensional `V_8` certificate

The preceding research certified strict Weil positivity on the 32-dimensional branch-sine subspace `V_8`.

The current trace capacity being close to 31 is structurally striking, but dimension matching alone does not imply that `V_8` spans the dangerous concentration space.

A separate floating diagnostic of the concentration operator indicated that the low branch-sine subspace captures only about 11 units of the total negative-band concentration trace, leaving roughly 20 in its orthogonal complement. This diagnostic is `TESTING` only, but it is enough to reject the shortcut

`DIM(V_8)=32 > TRACE CAPACITY ~31 -> V_8 IS RESPONSE-COMPLETE`.

No such conclusion is valid.

The proper continuation is to construct a response-adapted/union-band Slepian carrier for `E_-`, or prove an equivalent low/high Schur certificate.

## 8. Why the signed-symbol set is much smaller than the crude envelope band

The absolute comb bound uses only

`a(t) >= h_inf(t)-A_log3`.

It guarantees eventual positivity but destroys all prime-phase cancellation and all local sign information.

The Arb finite-band scan retains the actual signed prime comb. This shrinks the dangerous frequency observer from a crude contiguous high-frequency envelope to a union of narrow negative bands with certified total measure below `88.8666`.

BRC reading:

`ABSOLUTE PRIME MASS != SIGNED PRIME RESPONSE GEOMETRY`.

The latter is the correct carrier for a time-frequency complement analysis.

## 9. Smallest unresolved unit

The next high-value theorem is a signed-symbol complement reduction.

Write the non-pole multiplier as `a(t)` and choose a positive reference floor outside the negative set. One needs an inequality that bounds any negative quadratic contribution by a concentration operator supported on `E_-`, while retaining the positive-symbol magnitude and the finite-rank pole term.

A useful target is a Birman-Schwinger/Schur form in which the only compact obstruction is built from

`P_L F^(-1) 1_(E_-) F P_L`

or, more sharply, from the weighted negative symbol

`P_L F^(-1) a_-(t) F P_L`.

Then the correct finite carrier should be built from the top eigenfunctions of this union-band concentration/weighted response operator rather than from the first sine modes.

The remaining proof must still control the complement and the pole channels before full `H_log3` positivity can be claimed.

## 10. Hard boundaries

- `TRACE CAPACITY <31.2 != NEGATIVE INDEX <=31`.
- `AT MOST 31 DIRECTIONS WITH 99% NEGATIVE-BAND CONCENTRATION != AT MOST 31 NEGATIVE WEIL DIRECTIONS`.
- `V_8 DIMENSION 32 != RESPONSE COMPLETENESS`.
- The floating trace-capture diagnostic for `V_8` is not theorem data.
- This record concerns the non-pole scalar multiplier; the pole term remains a separate finite-rank channel.
- No full-window positivity and no RH proof is claimed.

## Provenance

- Production source: `scripts/rh_log3_negative_symbol_capacity_arb.py`.
- Production workflow run: `34023342294`, job `101459845426`.
- Source head: `7bf1586a05e621274779cf09afce5c243844e236`.
- Predecessor finite certificate: `research_notes/RH_LOG3_N8_ARB_POSITIVITY_CERTIFICATE_20260906.md`.
- Researcher-ID: `EM-DIRECT-7C1A42`.
