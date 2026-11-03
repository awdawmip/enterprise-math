# BRC N=4 S23: global-in-contrast Chernoff crossover existence and endpoint orientation

Date: 2026-11-04. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_CHECK_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Frozen model, scientific question

Continue the source-tagged paired-state experiment of `research_notes/brc_n4_s23_chernoff_finite_h_local_unique_crossing_20261104_research1/PROOF.md` in PR #1765, retaining its scientific pin `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. For the original lawful S23 witnesses, `0<h<=1/42`; the analytic experiment below is well-defined for the larger open interval `0<h<1/2`. Fix `0<s<=1`, `s=(1-beta_E)^2`, `beta_N=0`. Let `a=1/2+h`, `b=1/2-h`, and `w=sqrt(1-4h^2)`.

Under the two equally likely hypotheses, full tagged-source trial `T` has laws `(sa,1-s,sb)` and `(sb,1-s,sa)`; scalar event trial `B` has Bernoulli success parameters `sa` and `sb`. Trials are independent. Prescribed prices are `c_T=2-s` and `c_B=1`. The Chernoff information of a trial is minus the logarithm of the minimum Chernoff coefficient over exponents `t in [0,1]`. Define the per-cost efficiency difference `F(s,h)=C_T(s,h)/(2-s)-C_B(s,h)`. Positive F favors T; negative F favors B.

The preceding finite-h certificate proved one *locally unique* crossing for `h=1/42` at `s in (0.10243902443,0.10243902445)`. The unresolved question is global uniqueness. This note resolves the global endpoint orientation for **every positive contrast**, and proves global existence of at least one nontrivial crossing throughout the analytic family.

## Theorem: exact endpoint derivatives and at least one interior crossover

For every fixed real `0<h<1/2`, F is continuous on `(0,1]`, and:

1. Define `D_h(t)=t*a+(1-t)*b-a^t*b^(1-t)` for `t in [0,1]`. Then

   `lim_{s->0+} F(s,h)/s = (1-w)/2 - max_{0<=t<=1} D_h(t) < 0`.

   In particular, scalar B has strictly higher Chernoff information per prescribed cost for all sufficiently small positive s. The maximizer is unique and explicit:

   `L=(a-b)/log(a/b)`, `t0=log(L/b)/log(a/b)`,

   `max D_h = b+(a-b)*t0-L`, and `t0>1/2`.

2. At `s=1`, `F(1,h)=0`, and its left derivative is

   `F_s(1,h) = -(1-w)/w^2 - log(w) < -(1-w)^2/w^2 < 0`.

   Equivalently,

   `lim_{s->1-} F(s,h)/(1-s) = (1-w)/w^2 + log(w) > (1-w)^2/w^2 > 0`.

   Thus tagged T has strictly higher Chernoff information per prescribed cost for all s sufficiently close to 1 from below.

3. Therefore, for every `0<h<1/2`, **there exists at least one** `s_c in (0,1)` at which `F(s_c,h)=0`. For all S23-lawful `0<h<=1/42`, this gives an unconditional finite-contrast crossover existence theorem. Global uniqueness remains open.

### Proof of the small-s endpoint

The T coefficient minimizes at exponent one half by exchange symmetry and is exactly `T(s)=1-s+s*w=1-(1-w)s`. Therefore `C_T(s)/(2-s)=s*(1-w)/2+O_h(s^2)`.

For B the Chernoff coefficient at exponent t is

`Z_B(s,t)=s*a^t*b^(1-t)+(1-s*a)^t*(1-s*b)^(1-t)`.

As s tends to zero, uniform Taylor expansion on the compact exponent set `[0,1]` gives

`Z_B(s,t)=1-s*D_h(t)+O_h(s^2)` uniformly in t.

Consequently `min_t Z_B(s,t)=1-s*max_t D_h(t)+O_h(s^2)` and `C_B(s)=s*max_t D_h(t)+O_h(s^2)`. This proves the stated limit.

Since `D_h''(t)=-a^t*b^(1-t)*[log(a/b)]^2<0`, its maximum is unique. The first derivative vanishes when the geometric interpolation is `L=(a-b)/log(a/b)`. The elementary logarithmic mean inequalities `b<L<a` yield the claimed interior t0.

Now set `x=2h` so `w=sqrt(1-x^2)`. At t=1/2,

`D_h(1/2)=1/2-sqrt(a*b)=(1-w)/2`, while

`D_h'(1/2)=x-w*atanh(x)>0`.

Indeed `f(x)=x/sqrt(1-x^2)-atanh(x)` has `f(0)=0` and derivative `(1-x^2)^(-3/2)-(1-x^2)^(-1)>0` for every `0<x<1`. Thus `D_h'(1/2)>0`; the strict maximum lies to the right of 1/2 and is strictly greater than `D_h(1/2)`. The limit of F/s is therefore strictly negative.

For a constructive strict gap, let `ell=log(a/b)`, `d=D_h'(1/2)>0`, and `tau=min(1/2, d/(a*ell^2))`. Since `-D_h''(t)<=a*ell^2` on `[0,1]`,

`max D_h-D_h(1/2) >= d*tau - (a*ell^2)*tau^2/2 > 0`.

The strict inequality follows from `tau<=d/(a*ell^2)` and `tau>0`.

### Proof of the near-one endpoint

At s=1, T is the swapped two-outcome Bernoulli experiment B, so both optimized Chernoff coefficients equal `w=2*sqrt(a*b)` and `c_T=c_B=1`. Hence F(1,h)=0.

For B set `u=s/2`, `v=1-u`, `d=s*h`. Its exponent-half coefficient is `Z_B(s,1/2)=sqrt(u^2-d^2)+sqrt(v^2-d^2)`. At s=1, exchange symmetry and strict Chernoff convexity imply exponent 1/2 is the unique optimizer. The envelope theorem therefore gives the derivative of `log(min_t Z_B)` by differentiating this coefficient at s=1. Writing `k=sqrt(1/4-h^2)=w/2`, direct differentiation yields

`[partial_s log Z_B(s,1/2)]_{s=1}=-h^2/k^2=-(1-w^2)/w^2`.

Since `T(s)=1-(1-w)s`,

`F_s(1,h)=-(1-w^2)/w^2 +(1-w)/w-log(w) = -(1-w)/w^2-log(w)`.

For `0<w<1`, the integral bound `-log(w)=int_w^1 dt/t <(1-w)/w` shows

`F_s(1,h)<-(1-w)/w^2+(1-w)/w=-(1-w)^2/w^2<0`.

The left-hand asymptotic and strict sign follow from differentiability. Finally, F has a negative value for some s close to 0, and a positive value for some s close to 1. Continuity and the intermediate value theorem yield at least one zero in between. QED.

## Scientific increment and bridge to BRC

This all-contrast theorem complements the predecessor's *fixed-h local* rational root certificate: the threshold cannot disappear at other strictly positive contrasts even where the small-h series is not an adequate decision procedure. The endpoint slopes quantify which source observer benefits near low and high erasure rates. The two-state tests preserve the source-tagged T carrier and identify B as a declared event-only projection used solely for this statistical comparison; they make no general sufficiency claim for future operations on the original BRC state.

`VERIFY.py` executes exact rational upper/lower bounds for the two strict endpoint inequalities at `x=1/21` (lawful h=1/42) and two broader-family inputs. These checks support the algebra; the general-for-all-real-h theorem is supplied by the displayed analytic proof, not by the three finite tests.

## Next discriminating unit

Global uniqueness: classify the sign of F on `(0,s_L]` and `[s_R,1)` at `h=1/42`, where `s_L=0.10243902443` and `s_R=0.10243902445`. Construct certified compact-band sign enclosures plus quantitative endpoint neighborhoods, or derive a single-crossing inequality. Keep optimized B exponent. If uniqueness fails, produce an exact certified second root. Then study how the full endpoint orientation depends on specified sampling prices and finite budgets. The ten-label S23 decoder minimax mother target remains `[1/2,2/3]`.
