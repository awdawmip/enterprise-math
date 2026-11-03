# BRC N=4 S23: global uniqueness of the cost-efficiency crossover for sufficiently small contrast

Date: 2026-11-04. Status: AUTHOR_ANALYTIC_PROOF / EXACT_SYMBOLIC_AUDIT_EXECUTED / INDEPENDENT_REVIEW_PENDING / NOT_ADMITTED.

## Precise scope and input

This is the **source-tagged two-state sampling experiment**, not the unrestricted nine-coordinate recovery or ten-label decoder. Scientific input remains frozen at `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. It continues `research_notes/brc_n4_s23_chernoff_all_contrasts_endpoint_existence_20261104_research1/PROOF.md` in PR #1765. P000 and the native observer/provenance requirements remain unchanged.

Fix `0<s<1`, `0<h<=1/42` for lawful S23 witnesses, and write `a=1/2+h`, `b=1/2-h`, `s=(1-beta_E)^2`. Under two equally likely hypotheses, the full tagged trial `T` has laws `(sa,1-s,sb)` / `(sb,1-s,sa)` and cost `2-s`; the single-event trial `B` has Bernoulli success parameters `sa` / `sb` and cost `1`. All trials are independent. Write `C_T`, `C_B` for exactly optimized Chernoff information and `F(s,h)=C_T/(2-s)-C_B`. Positive F favors T.

## Theorem (uniform small-contrast, full-s crossover classification)

**There exists a real epsilon>0** such that for every `0<h<min(epsilon,1/42)` there exists **exactly one** `s_c(h)` in `(0,1)` satisfying `F(s_c(h),h)=0`, with `F(s,h)<0` for all `0<s<s_c(h)`, and `F(s,h)>0` for all `s_c(h)<s<1`.

The crossing extends to a real-analytic even curve in h near zero with

`lim_(h->0) s_c(h) = s_* = (20-2*sqrt(91))/9`.

Here epsilon is obtained by an analytic compactness argument, **without a numerical lower bound**. In particular, the theorem does not classify `h=1/42`; that finite contrast has a predecessor's locally unique root interval only.

## Proof

**1. Uniform analytic formula for the optimized B exponent.** Put `v=2h` and `k=s/(2-s)`. For a Chernoff exponent `t`, set `delta=2t-1`. The B coefficient can be expressed exactly as

`Z_B(s,v,delta)=X exp(alpha*delta)+Y exp(-gamma*delta)` with

`X=(s/2)*sqrt(1-v^2)`, `Y=((2-s)/2)*sqrt(1-k^2*v^2)`, `alpha=atanh(v)`, `gamma=atanh(k*v)`.

For `s>0` and `v!=0`, strict convexity in delta gives the unique unconstrained optimizer

`delta_* = log(Y*gamma/(X*alpha))/(alpha+gamma)`.

Define the even real-analytic function `g(y)=sqrt(1-y^2)*atanh(y)/y`, assigning `g(0)=1`, and `phi(y)=log g(y)`. Since `Y*gamma/(X*alpha)=g(k*v)/g(v)`, we have

`delta_*=[phi(k*v)-phi(v)]/[atanh(v)+atanh(k*v)]`.

The expansion `phi(y)=-y^2/6+O(y^4)` and even analyticity show that its numerator is divisible by `(1-k^2)*v^2`, while its denominator is `v` times an analytic factor whose value at `v=0` is `1+k>=1`. Therefore `delta_*(s,v)` has a joint real-analytic extension on a neighborhood of `[0,1] x {0}`, and

`delta_*(s,v)=(1-k)*v/6+O(v^3)` **uniformly** for `s in [0,1]`.

Consequently `|delta_*|<1` uniformly for sufficiently small |v|, so the displayed optimizer is genuinely within the Chernoff exponent domain. At `s=0` both experiments have coefficient one and the analytic expression is used only as a continuation; at `s=1` the optimizer equals zero. Let `M(s,v)=Z_B(s,v,delta_*(s,v))`; then `C_B=-log M`, `C_T=-log T`, where `T(s,v)=1-s+s*sqrt(1-v^2)`. Both M and T are positive and jointly analytic near `[0,1] x {0}`.

**2. Four-order expansion with the exact optimized exponent.** Direct expansion using the analytic optimizer (its linear term suffices through v^4 by stationarity) gives uniformly in s,

`M(s,v) = 1 - s*v^2/[2*(2-s)] - s*(31*s^2-62*s+40)*v^4/[72*(2-s)^3] + O(v^6)`,

`T(s,v) = 1 - s*v^2/2 - s*v^4/8 + O(v^6)`.

Since `F(s,h)=log M(s,2h)-log T(s,2h)/(2-s)`, its constant and quadratic coefficients vanish identically. Symmetry under `h -> -h` makes F even. The fourth-order coefficient is

`F(s,h) = A(s)*h^4 + O(h^6)`, where

`A(s) = -2*s*(1-s)*(9*s^2-40*s+4)/[9*(2-s)^3]`.

**3. Remove both endpoint zeros before taking limits.** For every sufficiently small h, exactly `F(0,h)=0` (both trials are uninformative) and `F(1,h)=0` (the two trial laws coincide with equal cost). Joint analyticity, evenness, the order-four zero in h and the two exact endpoint identities imply the factorization

`F(s,h)=h^4*s*(1-s)*H(s,h)`

with H jointly real-analytic near `[0,1] x {0}`. One can obtain this without power-series division by applying the integral form of the fundamental theorem of calculus to successively divide the analytic remainder by h, s and `(1-s)`; the same factorization follows from the local convergent power series at the endpoint charts. Thus

`H(s,0) = -2*(9*s^2-40*s+4)/[9*(2-s)^3]`.

The exact derivative is

`H_s(s,0) = 2*(68+44*s-9*s^2)/[9*(2-s)^4] >= 17/18 > 0` for `0<=s<=1`.

Also `H(0,0)=-1/9` and `H(1,0)=6`. By compactness and joint continuity of H and H_s, a single `epsilon>0` exists such that for all `|h|<epsilon`, H is strictly increasing in `s in [0,1]`, with H(0,h)<0<H(1,h). The intermediate value theorem and strict monotonicity yield a unique root in `(0,1)` and the asserted sign order for each h>0. Since `H_s(s_*,0)>0`, the analytic implicit-function theorem yields an analytic root curve; its h-evenness follows from H being even. QED.

## Audit, meaning, and research frontier

`VERIFY.py` uses SymPy exact rationals/symbolics to independently audit both coefficients, the cancellation of lower-order terms, the derivative formula and endpoints. It does not substitute finite calculation for the compactness/analyticity argument, and does not produce a numerical epsilon. This theorem bridges the previous all-contrast *existence* result and the finite-h local certificate: **global uniqueness holds on an entire (unspecified) small-contrast interval**, so any second crossing at a larger h would have to emerge outside that guaranteed regime.

The source observer T and event-only projection B are kept distinct. No full-state, cross-observer sufficiency or physical dynamics transfer is asserted. The unrestricted ten-label S23 minimax mother question remains at the previously recorded interval `[1/2,2/3]`.

## Next test

Quantify an explicit lower bound `epsilon>=1/42` by certified bounds on `H_s(s,h)` over `[0,1] x [0,1/42]`, or find a certified sign violation that narrows the viable range. A second route is a direct interval proof of F's sign outside the predecessor's finite-h root bracket, using exact optimization and endpoint normalization. Distinguish either certified result from mesh sampling.
