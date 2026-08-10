# R004 precision genesis — Supplement 03: sharp finite measurement-dependence cost

Status: `PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART SPECIALIZATION`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_02.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 02 established that locality plus measurement-setting independence blocks the selected exact rational Bell target. This supplement quantifies the residual escape route:

> if locality is kept but the latent seed distribution is allowed to depend on the chosen setting pair, exactly how much setting dependence is needed for this target?

The answer, for the max-total-variation normalization declared below, is exactly `2/15`.

## 1. Setting-dependent local completion

Keep the same sixteen deterministic local response tables

\[
\lambda=(A_0,A_1,B_0,B_1),
\qquad A_x,B_y\in\{-1,+1\}.
\]

Now allow a different latent distribution `mu_s` for each joint setting

\[
s\in\{00,01,10,11\}.
\]

The response functions remain setting-local; only the seed distribution changes with the setting pair.

Define the setting-dependence size

\[
\boxed{
M=\max_{s,t}\operatorname{TV}(\mu_s,\mu_t)
}
\]

with total variation

\[
\operatorname{TV}(p,q)=\frac12\sum_\lambda|p(\lambda)-q(\lambda)|.
\]

This normalization is stated explicitly because measurement-dependence literature uses several related conventions. Relaxing measurement independence in Bell models is established prior art [SRC-HALL-2010-MEASUREMENT-INDEPENDENCE].

## 2. Relaxed CHSH inequality

Take `mu_00` as a reference distribution. If all four correlations were evaluated with that one distribution, ordinary local CHSH gives magnitude at most `2`.

For a binary function `f(lambda) in {-1,+1}`,

\[
|E_p f-E_q f|
\le
\sum_\lambda |p(\lambda)-q(\lambda)|
=2\operatorname{TV}(p,q).
\]

The observed CHSH expression differs from the `mu_00` reference expression in only the other three setting terms. Each change is at most `2M`. Therefore

\[
\boxed{|S|\le2+6M.}
\]

### Integer form

Let every setting distribution be represented by nonnegative integer weights with the same total weight `W`, and define

\[
D=\max_{s,t}\sum_\lambda|w_s(\lambda)-w_t(\lambda)|.
\]

Then

\[
M=\frac{D}{2W}
\]

and the relaxed inequality is exactly

\[
\boxed{|N_{\mathrm{CHSH}}|\le2W+3D.}
\]

No floating-point optimization is needed in the theorem statement or proof.

## 3. Lower bound for the rational singlet target

Supplement 02's exact rational target has

\[
|S|=14/5.
\]

Substitute into the relaxed inequality:

\[
14/5\le2+6M.
\]

Hence

\[
6M\ge4/5
\]

and therefore

\[
\boxed{M\ge2/15.}
\]

So a setting-local pre-sampled model cannot recover the target by an arbitrarily small violation of measurement independence in this normalization.

## 4. Exact denominator-60 witness: the bound is sharp

R004 also gives an explicit local completion attaining equality.

Index the sixteen deterministic tables lexicographically over `(A_0,A_1,B_0,B_1) in {-1,+1}^4`. Only indices `2,3,5,7,8,10,12,13` receive nonzero weights. The four equal-total weight rows are:

- `00`: `(10,7,6,7,7,6,7,10)` on those indices;
- `01`: `(6,7,10,7,7,10,7,6)`;
- `10`: `(10,7,10,3,3,10,7,10)`;
- `11`: `(10,3,10,7,7,10,3,10)`.

Every row has total

\[
W=60.
\]

Every pair of setting rows has L1 distance

\[
D=16,
\]

so

\[
\operatorname{TV}=\frac{16}{120}=\frac{2}{15}.
\]

Evaluating the local response tables at the selected setting reproduces exactly three times the twenty-atom joint counts from Supplement 02. Thus it reproduces the same observable target and gives

\[
|N_{\mathrm{CHSH}}|=168
=2\cdot60+3\cdot16.
\]

Therefore both the relaxed inequality and the measurement-dependence lower bound are saturated:

\[
\boxed{M_{\min}=2/15.}
\]

The numerical linear program used during discovery is not part of the proof. The repository contains the explicit integer witness above, and exact verification reduces to finite summation.

## 5. Operational no-signalling is strictly weaker than local latent factorization

The twenty-atom rational target has balanced marginals. For every Alice setting `x`, her outcome counts are `10/10` independently of Bob's setting `y`; symmetrically Bob's `10/10` marginals are independent of `x`.

Thus the finite target is exactly **no-signalling at the observable level**.

At the same time, `|S|=14/5>2` proves there is no setting-independent local latent decomposition.

Hence R004 gets an exact finite separation:

\[
\boxed{
\text{observable no-signalling}
\not\Rightarrow
\text{Bell-local latent factorization}.
}
\]

This matters for the geometry route. A future finite causal/space model cannot identify “no controllable signal crosses the bridge” with the stronger hidden-variable factorization required by Bell locality. Those are different interfaces and must be represented separately.

## 6. Updated generative-identifiability ladder

The current finite hierarchy is now:

1. arbitrary pre-sampling survives deterministic towers;
2. arbitrary pre-sampling survives finite rational stochastic kernels;
3. arbitrary pre-sampling survives finite adaptive interventions;
4. setting-local + setting-independent pre-sampling fails on the rational Bell target;
5. keeping locality but allowing setting dependence restores a completion only after paying the exact target-specific price `M=2/15`;
6. none of this rules out genuinely nonlocal completions or other ontology changes.

So the research question has shifted again. It is no longer merely “is there a loophole?” but:

> which causal restrictions does Enterprise Math derive, what quantitative resource does violating each restriction cost, and which of those restrictions is independently pressure-tested by physical experiments?

That is a substantially more falsifiable program than treating “new information was created” as an uninterpreted ontological sentence.
