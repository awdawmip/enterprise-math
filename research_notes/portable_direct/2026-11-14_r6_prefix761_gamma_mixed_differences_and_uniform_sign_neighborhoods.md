# PREFIX-761 / R6 — Strict Gamma mixed differences and certified uniform-q sign neighborhoods

Date: 2026-11-14. Author-level continuation of PREFIX-760. Frozen scientific source: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Existing mathematical dependencies: PREFIX-755–759 (survival monotonicity, first-kill row 25), PREFIX-760 (exact Fraction signs). This document applies **only** to the external two-independent-Gamma-clock auxiliary; it is not native X6 dynamics. Proof status: `AUTHOR_ANALYTIC_PROOF_WITH_EXACT_RATIONAL_ARITHMETIC / UNREVIEWED / NOT_ADMITTED`.

## Setup

Let `T_x` be the stopped 189-layer frozen BRC count, `0 <= x <= 1/2`; let `C_x | T_x=m ~ Gamma(m,1)`, and take independent clocks `C_p,C_z`. Define `Y(p,z)=max(C_p,C_z)`, `H_x(t)=Pr(C_x>t)`, `M_r(p,z)=E[Y(p,z)^r]` for real `r>0`, `mu=M_1`, `M2=M_2`, and `V_q=q^2(M2-mu^2)-q*mu`. The exact finite survival representation is

```text
H_x(t) = exp(-t) * sum_{i=0}^{188} S_i(x)*t^i/i!,
S_i(x) = Pr(T_x>i).
```

We use the previously established strict survival stochastic order and first nontrivial layer:
`S_25(x)=1-x^25-(1-x)^25`, and for `0<=x0<x1<=1/2`, `H_x1(t)-H_x0(t)>=D_x exp(-t)*t^25/25!>0` for all `t>0`, with `D_x=S_25(x1)-S_25(x0)>0`. The normalized Bernstein coefficients `a_{i,k}/binom(i,k)` are in `[0,1]`, and `S_i(x)` is nondecreasing on `[0,1/2]`.

## Theorem 761.1 — strict submodularity of every positive raw moment

For every real `r>0` and `0<=p0<p1<=1/2`, `0<=z0<z1<=1/2`, define

```text
Delta_p Delta_z M_r =
  M_r(p1,z1)-M_r(p0,z1)-M_r(p1,z0)+M_r(p0,z0).
```

Then

```text
Delta_p Delta_z M_r
= -r * integral_0^infinity t^(r-1)
    * (H_p1(t)-H_p0(t))*(H_z1(t)-H_z0(t)) dt
<= -D_p*D_z * r*Gamma(r+50)/((25!)^2 * 2^(r+50))
< 0.
```

**Proof.** Independence gives `Pr(Y(p,z)>t)=H_p(t)+H_z(t)-H_p(t)H_z(t)`. The nonnegative-moment tail integral `M_r=r integral t^(r-1)Pr(Y>t)dt` is absolutely finite here because each Gamma shape is bounded by 189. Taking the two finite parameter differences eliminates the two single-clock terms, leaving the displayed negative product. Both survival differences are strictly positive for all `t>0` by the row-25 witness. Substituting their lower bounds and integrating `exp(-2t)t^(r+49)` yields the explicit strict bound. No variance monotonicity is assumed. QED.

Thus each gain `M_r(p1,z)-M_r(p0,z)` is **strictly decreasing** as the second-clock parameter `z` increases; this is a statement about increments of raw moments, not about increments of variance.

**Concrete rational witness.** At `p0=z0=0, p1=z1=1/4`:
```text
D_p=D_z=D=281263154558295/281474976710656.
-(Delta_p Delta_z M_1) >= D^2 * binom(50,25)/2^51 > 0.056.
-(Delta_p Delta_z M_2) >= 51*D^2 * binom(50,25)/2^51 > 2.858.
```
These two are analytical lower certificates for the *full* 189-layer model under the inherited row-25 hypothesis, not numerical evaluations of its actual mixed differences.

## Lemma 761.2 — uniform derivative bound for variance increments

Fix `p0=0, p1=1/4`. Put `dmu(z)=mu(p1,z)-mu(p0,z)>0`, `dM2(z)=M2(p1,z)-M2(p0,z)>0`, `dVar(z)=dM2(z)-dmu(z)*(mu(p1,z)+mu(p0,z))`.

For `0<=z<=1/2`, the original Bernstein coefficient interval `0<=b_{i,k}<=1` gives

```text
S_i'(z)=i*sum_k (b_{i,k+1}-b_{i,k})*B_{i-1,k}(z),
0<=S_i'(z)<=i.
```

The lower derivative bound follows from the previously proved monotonicity on the half-interval; the absolute upper bound follows directly from `|b_{i,k+1}-b_{i,k}|<=1`. Let

```text
A = sum_{i=0}^{188} i = 17766,
B = 2*sum_{i=0}^{188} i(i+1) = 4500720.
```

Differentiate the finite tail integrals and use `0<=1-H_p<=1`. This gives `0<=mu_z'<=A`, `0<=M2_z'<=B`, `-A<=dmu'<=0` and `-B<=dM2'<=0`. The latter two follow directly by differentiating `r int t^(r-1)(H_p1-H_p0)(1-H_z)dt`.

Since `0<dmu<=E[C_p1]-E[C_p0]<=189`, `0<=mu(p,z)<=E[C_p]+E[C_z]<=378`, and `0<=d_z(mu(p1,z)+mu(p0,z))<=2A`, the product rule gives the global rational Lipschitz certificate

```text
|dVar'(z)| <= B + A*(4*189) + 189*(2*A)
            = B + 6*189*A = 24647364 =: L.
```

All integrals and derivatives are finite polynomials times exponentials and support the stated differentiations. QED.

## Corollary 761.3 — nonpoint sign regions for ALL real q>=2

PREFIX-760's original `Fraction` certificates assert at `z=0` that `dVar>367` and `dmu<112`, and at `z=1/4` that `dVar<-159`. Applying the preceding `L`:

1. For every `z in [0,1/100000]`, `dVar(z)>367-L/100000 = 3013159/25000`; moreover `dmu(z)<112`. Hence, **for every real `q>=2`**,
   ```text
   V_q(1/4,z)-V_q(0,z)
     = q*(q*dVar(z)-dmu(z))
     > q*(2*3013159/25000-112)
     = q*1613159/12500 >0.
   ```
2. For every `z in [49999/200000,50001/200000]`, `dVar(z)<-159+L/200000 = -1788159/50000` and `dmu(z)>0`. Hence, **for every real `q>0`**,
   ```text
   V_q(1/4,z)-V_q(0,z)
     < -q^2 *1788159/50000 <0.
   ```

The sign reversal of PREFIX-760 therefore holds uniformly on two explicit *continuous* intervals, not only at isolated rational points. The intervals need not be maximal; the global variance behavior between them remains open. The earlier `q=2` root brackets remain valid.

## Reproducibility, provenance and next frontier

Arithmetic verified with Python 3 standard-library `Fraction`, `comb`, `factorial`: `PREFIX761_R6_MIXED_DIFFERENCE_CHECK.py` and `PREFIX761_R6_MIXED_DIFFERENCE_RESULTS.json`. The exact check covers `A,B,L`, the two rational endpoint margins, `D`, and the r=1,2 Gamma-integral constants; it **does not independently rerun** the 189-layer BRC recurrence or the PREFIX-760 moment engine. Analytic proof is written above and uses the cited source lemmas as inherited premises. This is not an independently reviewed project Result.

Reusable next action: implement an endpoint-only interval certificate using strict decreasing raw-moment increments and monotone `mu`, `M2`: for `z in [a,b]`, `dVar(z)` lies between `dM2(b)-dmu(a)*(mu(p1,b)+mu(p0,b))` and `dM2(a)-dmu(b)*(mu(p1,a)+mu(p0,a))`. Exact `K_{ij}`, `L_{ij}` kernels from PREFIX-760 can compute those endpoints for genuine still-uncertified `1/768` cells. This proposed interval method has not yet been executed on those cells; it does not add historical coverage.
