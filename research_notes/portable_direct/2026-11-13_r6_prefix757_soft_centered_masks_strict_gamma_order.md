# PREFIX-757-R6 — Soft centered killed Pascal masks and strict Gamma-clock ordering

Date: 2026-11-13 (Asia/Shanghai). Parent line: PREFIX-675. Direct predecessor: PREFIX-756.
Scientific input pin (unchanged): `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Current-rule read: `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`, project ACTIVE P000, and applicable account mathematical-evidence rules.
Status: AUTHOR_ANALYTIC_PROOF_WITH_INDEPENDENT_350_INTEGER_MASK_CHECK / UNREVIEWED / NOT_ADMITTED.
Object: an external finite stopped Bernoulli/Gamma auxiliary model. No assertion of an X6-native temporal bridge.

## Theorem 757.1 — centered *soft* killing preserves the Bernstein order

For every integer n >= 1, let `w_n(k)` be any **real** retention weights in [0,1] for 0 <= k <= n, with
`w_n(k)=w_n(n-k)`, and `w_n(k+1)>=w_n(k)` for 0 <= k < floor(n/2).
No interval, positivity away from edges, constant row width, or binary-mask assumption is imposed.

Define `a[0,0]=1`, out-of-range coefficients zero, and
`a[n,k]=w_n(k)*(a[n-1,k]+a[n-1,k-1])`.
Set `b[n,k]=a[n,k]/C(n,k)` and
`S_n(p)=sum_{k=0}^n a[n,k]*p^k*(1-p)^(n-k)`.
For every finite n, the normalized sequence `b[n,k]` is nonnegative, symmetric and nondecreasing toward its center. Consequently, for **all real** `0<=p1<=p2<=1/2`,
`S_n(p1)<=S_n(p2)`.

**Proof.** The normalized Pascal bridge prior to retention is
`t[n,k]=((n-k)/n)*b[n-1,k]+(k/n)*b[n-1,k-1]`.
By the previous-row symmetry, `t[n,k]=t[n,n-k]`. Its adjacent differences obey
`n*(t[n,k+1]-t[n,k])=(n-k-1)*(b[n-1,k+1]-b[n-1,k])+k*(b[n-1,k]-b[n-1,k-1])`.
For `0<=k<floor(n/2)`, both differences on the right are nonnegative by the induction hypothesis, including the even-n central equality case. Thus `t[n,k]` is centrally nondecreasing. Multiplication by the likewise nonnegative, symmetric, centrally nondecreasing `w_n(k)` retains these properties: for `0<=k<floor(n/2)`,
`w_n(k+1)t[n,k+1]-w_n(k)t[n,k] = w_n(k+1)*(t[n,k+1]-t[n,k])+(w_n(k+1)-w_n(k))*t[n,k]>=0`.
Induction from `b[0,0]=1` proves the coefficient statement.

Write `b[n,k]=b[n,0]+sum_{j=1}^{floor(n/2)} d_j 1{j<=k<=n-j}`, where `d_j=b[n,j]-b[n,j-1]>=0`. For `K~Bin(n,p)`,
`S_n(p)=b[n,0]+sum_j d_j Pr_p(j<=K<=n-j)`.
The exact derivative of the central binomial interval probability is
`n*C(n-1,j-1)*[p^(j-1)*(1-p)^(n-j)-p^(n-j)*(1-p)^(j-1)]>=0`
on `[0,1/2]`, since `n-j>=j`. This proves the continuum assertion. QED.

**Probabilistic corollary.** Since `0<=w_n(k)<=1`, these weights define genuine history-dependent retention probabilities on Bernoulli paths. The survival probabilities `S_n(p)=Pr(T_p>n)` are consistent and nonincreasing in n. The theorem gives stochastic ordering `T_{p1}<=_st T_{p2}` for `0<=p1<=p2<=1/2`. If all paths stop by a common finite N, and conditionally on `T_p=m` a time clock has Gamma(m,1) law, its tail is
`H_p(t)=exp(-t)*sum_{n=0}^{N-1} S_n(p)*t^n/n!`
and is coordinatewise nondecreasing in p for every t>=0. The independent maximum of two such clocks inherits this stochastic order in each coordinate. This extends the binary centered interval theorem of PREFIX-756 to soft, non-interval, partially retained masks.

## Theorem 757.2 — *strict*, explicit lower bounds in the frozen 189-level family

Assume the exact frozen width masks and recursion at scientific pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`; retain the 189-level termination certified in PREFIX-755/756. Exact independent testing of all `sum_{n=1}^{25}(n+1)=350` first mask memberships finds all `k=0..n` accepted for n=1..24, and exactly `k=1..24` accepted for n=25. Thus
`S_25(p)=1-p^25-(1-p)^25`.
For any real `0<=p1<p2<=1/2`, put
`D=S_25(p2)-S_25(p1)=[p1^25+(1-p1)^25]-[p2^25+(1-p2)^25]>0`.
Indeed, `S'_25(p)=25[(1-p)^24-p^24]>0` for `p<1/2`.

For every `t>0`, the other frozen rows are ordered by PREFIX-756, hence
`H_{p2}(t)-H_{p1}(t)>=D*exp(-t)*t^25/25!>0`.
For any `z in [0,1/2]`, termination at row 189 gives
`1-H_z(t)>=exp(-t)*t^189/189!`.
Therefore for `Y(p,z)=max(Gamma(T_p,1),Gamma(T_z,1))` with independent conditional clocks,
`Pr(Y(p2,z)>t)-Pr(Y(p1,z)>t)`
`=(H_{p2}(t)-H_{p1}(t))*(1-H_z(t))`
`>=D*exp(-2t)*t^214/(25!*189!)>0`.

For every real `r>0`, the tail integral identity yields the explicit uniform bound
`E[Y(p2,z)^r]-E[Y(p1,z)^r] >= r*D*Gamma(214+r)/(25!*189!*2^(214+r))>0`.
This is strict stochastic dominance, and hence strict increase of all positive raw moments, including the mean and the second raw moment, in each coordinate. The numeric constant is deliberately conservative, not optimized.

**Scope:** Stochastic order of Y does not itself assert monotonicity of its variance or of `V_q=q^2 Var(Y)-q E[Y]`; that extremal functional retains its separate certificates. No new geometric exclusion cells are counted.

## Actual finite validation and source provenance

Executed local Python-stdlib script `PREFIX757_R6_SOFT_MASK_STRICT_ORDER_CHECK.py` reconstructed only the published PREFIX-755 frozen integer width predicate through n=25, checked all 350 mask memberships, verified the precise binomial survivor counts at row 25 and evaluated the rational case `p1=0, p2=1/4`. The exact result is
`D=(4^25-1-3^25)/4^25=281263154558295/281474976710656>0`.
The accompanying result JSON records the observed domain and calculation. Prior exact 189-level termination and centeredness are explicitly **consumed** from PREFIX-755/756, not independently re-executed in this script. The abstract soft-weight theorem is a written analytic proof, not a floating point experiment.

Reference frontier:
- `research_notes/portable_direct/2026-11-13_r6_prefix756_centered_killed_pascal_monotonicity.md` at `0f8b4c3b13b5976ec442631e820fee7fa1a1c10c`.
- `research_notes/portable_direct/PREFIX755_R6_BERNSTEIN_MONOTONE_GAMMA_CHECK.py` at `c6747cee5259fe74b5416d862b9d431857abd9f8`.
- The direct scientific freeze remains `f42f2906d77f24085c123f3ccfe9667d41caa96d`.

## Next research

1. Independently review the all-orders weighted-mask proof and the gamma-tail truncation, including endpoints and shape-count indexing.
2. Apply the strict stochastic order to comparison-point selection or certified bounds on the genuinely uncovered fine-grid cells from PREFIX-752, **without** assuming that variance is monotone.
3. Check the separate PREFIX-754 IEEE/BLAS error-envelope assumptions before elevating any dependent numerical region theorem.

Activity / Source authority: This is direct unshared scientific material; current native session registration/dispatch is a separate control subflow. No foreign Task CLAIM, Result or Review is asserted.
