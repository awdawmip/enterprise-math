# BRC N=4 / S23: smallest globally optimal mixed Chernoff budget is K=4

Date 2026-11-04. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Exact inputs and declared observer

Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. The inherited source-tagged T/B laws and sampling costs are unchanged. Continue PR #1765 after its K=75001 example, `d2738f32daae8e440b3ba19cd84b402b90a41970`; this new result uses a **self-contained proof**, not the earlier unreviewed holomorphic Cauchy remainder.

Fix `s=1/2`, `v=2h=1/21`, `p=s(1+v)/2=11/42`, `q=s(1-v)/2=10/42`. Tagged T laws:
`P_T=(p,1-s,s(1-v)/2)`, `Q_T=(q,1-s,s(1+v)/2)`.
B laws: `P_B=(p,1-p)`, `Q_B=(q,1-q)`.
Costs `c_T=3/2`, `c_B=1`. An integer pair `(m,n)>=0` is feasible at integer budget K iff `3m+2n<=2K`.

Let `f_A(t)=-ln(sum_y P_A(y)^t Q_A(y)^(1-t))`, A=T,B. For independent mixed observations define the exact **shared exponent** objective
`C(m,n)=max_{0<=t<=1}[m f_T(t)+n f_B(t)]`.
The B observer deterministically merges T outcomes `+ -> success`, `{erase,-} -> failure`. The source identities and joint counts stay available.

## Theorem

For integer budgets `K=1,2,3` no genuine mixture (`m>0,n>0`) maximizes C. At **K=4**, the **unique global optimum** among *all* feasible integer pairs is `(m,n)=(2,1)`, consuming cost exactly 4, and

`C(2,1)-C(0,4)>1/5,000,000`.

Thus K=4 is the smallest integer budget permitting a globally optimal genuine T/B mixture.

### Data processing and complete budget reduction

For every `0<=t<=1`, applying Hölder to the `{erase,-}` fiber gives `sum_b P_B(b)^t Q_B(b)^(1-t) >= sum_y P_T(y)^t Q_T(y)^(1-t)`, so `f_T(t)>=f_B(t)`. This is strict for `0<t<1` because the erase and minus outcomes have distinct likelihood ratios and positive mass. Mixture objectives are positive at t=1/2 and vanish at t=0,1; the optimizing t is internal. Therefore replacing B with T at equal *number* of observations strictly improves C whenever both allocations are budget-feasible.

At K=1,2, mixed pairs are impossible. At K=3, only `(1,1)` is mixed, strictly dominated by feasible `(2,0)`. At K=4, `(2,1)` dominates `(1,2)`, `(2,0)`, and all smaller T-bearing counts by strict pointwise data processing plus adding positive B information. Pure B allocations are maximized by `(0,4)`. Hence it suffices to show `C(2,1)>4C_B`, where `C_B=max_t f_B(t)`.

### Independent rational-interval certificate

The T laws are symmetric, so `C_T=f_T(1/2)=-ln Z_T`, with
`Z_T=1/2+sqrt(440)/42`.
Set `b=f_B(1/2)=-ln Z_B`, where
`Z_B=(sqrt(110)+sqrt(992))/42`.
At the one shared t=1/2, `C(2,1)>=2C_T+b`.

Let `g=f_B'(1/2)`, `d=ln(176/155)>0`. Under the exponentially tilted Bernoulli distribution, the success probability `pi_t` satisfies `q<=pi_t<=p<1/2` (its log odds linearly interpolate those of q and p). Thus

`f_B''(t)=-pi_t(1-pi_t)d^2<=-mu`, `mu=q(1-q)d^2`, and

`g=-(sqrt(110)ln(11/10)+sqrt(992)ln(31/32))/(sqrt(110)+sqrt(992))`.

`VERIFY.py` establishes using exact rational outward intervals that
`mu>1/350`, `|g|<1/120000`, `2C_T-3b>1/4000000`.

Uniform strong concavity centered at t=1/2 yields
`f_B(t)<=b+g(t-1/2)-(mu/2)(t-1/2)^2`, hence
`0<=C_B-b<=g^2/(2mu)<175/14400000000`.
Therefore
`C(2,1)-4C_B >= (2C_T-3b)-4(C_B-b)
 > 1/4000000-700/14400000000 > 1/5000000>0`.

For exact error semantics, `VERIFY.py` uses only `fractions.Fraction` and `math.isqrt`. Each rational square root is enclosed between adjacent rational numbers of denominator `10^29`. For rational `r>=1`, `ln(r)` is bounded by the finite arctanh series `2 sum_{j=0}^{23} z^(2j+1)/(2j+1)`, `z=(r-1)/(r+1)`, with positive remainder at most `2 z^49/[49(1-z^2)]`; `r<1` uses inversion. Exact interval operations certify all inequalities, and feasible integer pairs for K<=4 are completely enumerated. No floating-point optimizer or prior author Cauchy bound is used.

## BRC usage, limits and continuation

The original fine source-tagged carrier T, its B fiber readout, and the shared-exponent discrimination observer constitute the typed BRC application; the exact fiber inequality quantifies the loss from dropping source information. This theorem concerns this finite S23 sampling design, not X6 native time evolution. The original ten-label decoder minimax mother objective remains open within its recorded `[1/2,2/3]`.

Next: classify globally optimal counts K=5..100 at s=1/2 with strict common-exponent certificates and then rational s across the crossover. Determine whether larger budgets genuinely require multiple B trials. Native Researcher-ID, Owner, CLAIM, independent Driver review and formal Result admission are separate operations pending native authority.
