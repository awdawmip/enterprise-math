# BRC N=4 / S23: exact analytic endpoint continuation for the cubic Chernoff proxy

Date: 2026-11-04. Status: AUTHOR_ANALYTIC_DERIVATION / EXACT_RATIONAL_ENDPOINT_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Scientific scope and provenance

Continue the source-tagged, two-state T/B sampling experiment of Enterprise Math PR #1765, frozen scientific input `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Immediate predecessor `research_notes/brc_n4_s23_endpoint_normalized_20261104_research1/PROOF.md` at immutable commit `9851e0d146a50a5f9b788467635c24c38d6e79d7`. The present lemma concerns the cubic proxy's analytic endpoint values, and gives fully explicit sign margins for all legal contrasts. The full ten-label decoder minimax mother problem retains its interval [1/2,2/3].

Set real `0<v=2h<=1/21` and `0<s<1`. Under two hypotheses the full tagged trial T has laws `(s(1+v)/2,1-s,s(1-v)/2)` and its swap, whereas the event-only Bernoulli trial B has success probabilities `s(1+v)/2`, `s(1-v)/2`; the stipulated costs are `2-s`, `1`. Distinct source tags are retained in T. This comparison uses B as one declared observer, without claiming universal safe erasure of source provenance.

Write

- `r=sqrt(1-v^2)`, `a=atanh(v)`, `k=s/(2-s)`, `gamma=atanh(k*v)`;
- `d3(s,v)=(1-k)*v/6 + (1-k)*(9*k^2+10*k+9)*v^3/180`;
- `M3(s,v) = s*r/2*exp(a*d3) + (2-s)/2*sqrt(1-k^2*v^2)*exp(-gamma*d3)`;
- `T(s,v)=1-s+s*r`;
- `F3(s,v)=log(M3(s,v)) - log(T(s,v))/(2-s)`;
- `G3(s,v)=F3(s,v)/[s(1-s)]` for `0<s<1`.

The predecessor proved `F3(s,v)-E(s,v) <= F(s,v) <= F3(s,v)` with `F=C_T/(2-s)-C_B` (truly optimized Chernoff information), and
`0 <= (F3-F)/[s(1-s)] <= 128*(1-s)*v^12/((2-s)^2*(1-v^2)^2) <= 32*v^12/(1-v^2)^2`.

## New theorem (closed endpoint formulas and uniform explicit margins)

For every fixed real `0<v<=1/21`, the function `G3(.,v)` has a real-analytic extension to an open neighborhood of `[0,1]`, with

`G3(0,v) = [r*(exp(a*d0)-1)-v*d0]/2`, where `d0=v/6+v^3/20`,

`G3(1,v) = (1-r)/r^2 + log(r)`.

Both endpoint signs have contrast-uniform rational margins:

`G3(0,v) <= -(7/1800)*v^4 < 0`;

`G3(1,v) > (1-r)^2/r^2 > v^4/4 > 0`.

In addition, the exact optimized normalized information gap `G=F/[s(1-s)]` has endpoint limits and the same strict orientations:

`G(0+,v) <= G3(0,v) <= -(7/1800)*v^4`,

`G(1-,v) = G3(1,v) > v^4/4`.

The already established proxy enclosure provides the explicit lower bound `G(0+,v) >= G3(0,v) - 32*v^12/(1-v^2)^2`. The theorem provides analytic endpoint evaluations usable as boundary data in a subsequent rigorous full-interval sign/derivative certificate. It does not yet certify monotonicity or a unique interior crossing at `v=1/21`.

## Proof

**1. Analytic division by the two exact endpoint factors.** Fix `0<v<=1/21`. The denominator `2-s` is positive near `[0,1]`. The radicands `(2-s)^2-s^2*v^2` and `1-v^2` are strictly positive on `[0,1]`. Hence `k`, `d3`, `M3`, `T` and their real logarithms are analytic on a neighborhood of the closed interval. Moreover `M3(0,v)=T(0,v)=1`, and `M3(1,v)=T(1,v)=r` since `d3(1,v)=0`. Thus `F3(0,v)=F3(1,v)=0`. Analytic division first by `s`, then by `1-s`, gives a real-analytic extension of `G3` including both endpoints. In particular `G3(0,v)=F3_s(0,v)` and `G3(1,v)=-F3_s(1,v)`.

**2. Formula at zero.** When `s=0`, `k=gamma=0`, `d3=d0`, and `M3=1`. Differentiate `M3`: the `s*r*exp(a*d3)/2` term contributes `r*exp(a*d0)/2`; the other term contributes `-1/2-v*d0/2`. The derivative of `d3` contributes nothing at this endpoint because it is multiplied by `s` or `gamma=0`. Therefore `M3_s(0,v)=[r*exp(a*d0)-1-v*d0]/2`. Since `T_s=r-1`, direct differentiation of `F3` gives

`F3_s(0,v) = M3_s(0,v)-(r-1)/2 = [r*(exp(a*d0)-1)-v*d0]/2`.

**3. Uniform strictly negative sign.** For `0<v<1`, put `f(v)=v-sqrt(1-v^2)*atanh(v)`. Then

`f'(v)=[sqrt(1-v^2)-1+v*atanh(v)]/sqrt(1-v^2) >= 1-sqrt(1-v^2) >= v^2/2`, since `atanh(v)>=v`. As `f(0)=0`, integration yields `r*a-v <= -v^3/6`.

For `v<=1/21`, exact rational comparisons show

`a <= v/(1-v^2) <= (441/440)*v < (101/100)*v`,

`v/6 <= d0 <= v/5`,

`a*d0 <= (101/100)*v^2/5 <= 101/220500 < 1/2000`, and

`exp(a*d0) <= 1/(1-a*d0) <= 2000/1999 < 11/10`.

The elementary Taylor bound `exp(z)-1 <= z+z^2*exp(z)/2` for `z>=0` therefore gives

`r*(exp(a*d0)-1)-v*d0 <= (r*a-v)*d0 + r*a^2*exp(a*d0)*d0^2/2`

`<= -v^3*d0/6 + (3/5)*v^2*d0^2`

`<= -v^3*d0*(1/6-3/25) = -(7/150)*v^3*d0 <= -(7/900)*v^4`.

Here `r*a^2*exp(a*d0) <= (101/100)^2*(11/10)*v^2 < (6/5)*v^2`, and the last inequality uses `d0>=v/6`. Dividing by 2 proves `G3(0,v)<=-7*v^4/1800`.

**4. Formula and margin at one.** At `s=1`, `d3=0`, `k=1` and `M3=r`. The derivative with respect to the proxy exponent vanishes there by the T/B swap symmetry, so the derivative of `d3` has no effect on `M3_s(1,v)`. Evaluating the exponent-zero coefficient

`M(s,v,0)=[s*r+sqrt((2-s)^2-s^2*v^2)]/2`

gives `M3_s(1,v)=-v^2/r` and `partial_s log M3(1,v)=-v^2/r^2`. Differentiating `F3=log M3-log T/(2-s)` gives

`F3_s(1,v)=-v^2/r^2-(r-1)/r-log r=-(1-r)/r^2-log r`.

Therefore `G3(1,v)=(1-r)/r^2+log r`. Since `-log r=integral_r^1 dt/t < (1-r)/r` for `0<r<1`, we get `G3(1,v)>(1-r)^2/r^2`. Finally `1-r=v^2/(1+r)>v^2/2` and `r<1`, establishing the lower bound `>v^4/4`.

**5. Transfer to the true optimizer.** By the predecessor's full-open-interval bound, `G3(s,v)-32*v^12/r^4 <= G(s,v) <= G3(s,v)`. The analytic true-optimizer endpoint limit exists by the earlier optimizer formula and endpoint theorem. Taking `s->0+` gives the asserted negative sign and lower enclosure. Near `s=1`, the predecessor's sharper factor `128*(1-s)*v^12/((2-s)^2*r^4)` tends to zero, yielding `G(1-,v)=G3(1,v)` and its positive sign. QED.

## Executed exact certificate and coverage

`VERIFY.py` uses Python standard-library integer `isqrt`, `Fraction`, and rational Taylor remainder bounds for `sqrt`, `atanh`, `exp`, `log` at the worst lawful contrast `v=1/21`. It checks exact rational comparisons used in step 3, evaluates rigorous intervals for both transcendental endpoint formulas, and verifies the inherited normalized error bound against the negative margin. No float is used for asserted inequalities; printed decimals are only outward-rounding displays of verified rational enclosure endpoints. The proof of uniform coverage `0<v<=1/21` is the analytic argument above, not finite sampling.

The endpoint inputs are source-tagged in T; event-only B is a declared statistical observer. All P000/X6 and joint-relation research constraints remain part of the scientific provenance; this reduced two-state experiment is a specified restricted comparison.
