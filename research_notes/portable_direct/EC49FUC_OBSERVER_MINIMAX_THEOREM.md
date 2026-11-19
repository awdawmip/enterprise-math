# EC49FUC — Exact observer-channel defect and minimax sample complexity at the clipping interface

Date: 2026-11-20.  Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED**.

**Scientific input is frozen:** `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, the inherited BRC16943 pricing/Bellman input. Immediate parent: [EC49FUB PR #2817](https://github.com/awdawmip/enterprise-math/pull/2817), scientific proof commit `ee7207d628241f1b16603f1fc7bfa0cbb6ae8c9b`. The result is about an **external price-prior conditional readout**, not a newly verified native Bellman branch.

## 1. Exact interface experiment

Let `m_*=1469/64`, `L=951/1280`, `U=3/4`, `W=U-L=9/1280`, and `E=1048576/18958647`. For every finite real `epsilon<=E`, let `nu_epsilon` be the atomless probability measure on `[L,U]` with density

```text
f_epsilon(z) = (1-epsilon*m_* z) /
               (W*(1-epsilon*m_*(L+U)/2)).
```

The inherited EC49FUB one-sided conditional laws at the clipping boundary are

```text
H_-:  mu_- = nu_epsilon
H_+:  mu_+ = (1-q_epsilon)*nu_epsilon + q_epsilon*delta_U,

q_epsilon = 575*(41217719*epsilon-2359296) /
                 (45529434409*epsilon-2630615040).
```

In particular `0<q_epsilon<1` on the whole allowed half-line, `q'_epsilon<0`, and

```text
q_E = 3310244525/8132285009,
q_0 = 115/223,
q'_epsilon = -581059943674675200/
             (45529434409*epsilon-2630615040)^2 < 0.
```

This paper keeps the EC49FUB **one-sided weak-limit** convention: a conditional probability distribution at the single value `m=m_*` is not canonically prescribed by the joint density. Both hypotheses are the left/right limiting experiments, not an assertion about a unique on-boundary conditional law.

## 2. General observation-channel theorem

**Theorem A (exact residual through an observer).** Let `Y` be any standard Borel observation space and `K(z,dy)` any Markov observation channel shared by the two hypotheses. Set `K_U=K(U,·)` and `K_nu=integral K(z,·) nu_epsilon(dz)`. Their observed measures obey the signed-measure identity

```text
K mu_+ - K mu_- = q_epsilon*(K_U-K_nu)
```

and consequently

```text
TV(K mu_+, K mu_-) = q_epsilon*TV(K_U,K_nu).
```

For a **deterministic measurable readout** `T:[L,U]->Y`, this becomes

```text
TV(T#mu_+,T#mu_-)
  = q_epsilon*(1-nu_epsilon({z:T(z)=T(U)})).
```

The entire one-sample distinguishability loss is therefore exactly the continuous mass collapsed onto the same readout as the top atom. A readout resolving `U` from `nu_epsilon`-almost every continuous point retains total variation `q_epsilon`; a readout mapping almost all of the interval to `T(U)` erases it.

*Proof.* Subtract the two mixtures: `mu_+-mu_-=q(delta_U-nu)`. A Markov kernel acts linearly on signed finite measures. Total variation is absolutely homogeneous. In the deterministic case `K_U=delta_{T(U)}`, and for any probability `P`, `TV(delta_y,P)=1-P({y})`; apply this with `P=T#nu`. QED.

**Corollary A1 (information asymmetry).** With the identity readout,

```text
D_KL(mu_- || mu_+) = -log(1-q_epsilon);
D_KL(mu_+ || mu_-) = +infinity.
```

The first formula follows since the absolutely continuous density ratio is `1/(1-q)`; the second follows from the positive `U` atom under `mu_+` and zero atom under `mu_-`. In particular, the phase indicator `I=1_{Z=U}` is sufficient for deciding the *fixed-common-epsilon* binary experiment: under `H_-`, `I=0` surely; under `H_+`, `I~Bernoulli(q)`; conditioned on `I=0` both laws for the remaining `Z` coincide with `nu_epsilon`.

## 3. Finite-resolution quantization, exactly

For `0<=delta<=W`, let the two-bin detector return `T_delta(Z)=1_{Z>=U-delta}`. Since `nu` has no atom at `U`, its upper-bin probability is

```text
rho_epsilon(delta)
  = delta*(1-epsilon*m_*(U-delta/2)) /
    (W*(1-epsilon*m_*(L+U)/2)).
```

**Theorem B (exact binning loss).** For every finite admissible epsilon and every `0<=delta<=W`,

```text
TV(T_delta#mu_+,T_delta#mu_-)
      = q_epsilon*(1-rho_epsilon(delta)),
lost_TV = q_epsilon*rho_epsilon(delta),
Bayes_error_equal_priors = (1-q_epsilon*(1-rho_epsilon(delta)))/2.
```

For `delta=0` the exact top-atom detector loses no information; for `delta=W` the constant detector loses all information. The formula is analytic in `delta` and `epsilon` on the stated domain. For fixed epsilon and `delta->0+`,

```text
lost_TV =
  q_epsilon * (1-epsilon*m_*U) /
  (W*(1-epsilon*m_*(L+U)/2)) * delta + O(delta^2).
```

*Proof.* Integrate the affine density over `[U-delta,U]`. Then use Theorem A with the top-bin fiber `T_delta^{-1}(1)`. The equal-prior binary Bayes risk for observed probability measures `P,Q` is `(1-TV(P,Q))/2`. QED.

Exact benchmarks: for `epsilon=0,delta=W/4`, `rho=1/4` and observed `TV=345/892`, versus full-resolution `q_0=115/223`. At the admissible endpoint epsilon `E` and `delta=W/4`, the exact values are

```text
rho_E(W/4) = 1547881/6614596
observed_TV = 16772065588485375/53791779891391364.
```

These examples distinguish mass lost by a **specified external detector** from an alteration of the original native Cell state.

## 4. Exact repeated-observation law and a sharp nuisance-parameter minimax result

Assume `n>=1` **independent draws** from one of the one-sided laws, with a common fixed epsilon under the competing hypotheses. Let `N_U` count observations equal to `U`. Then

```text
H_-:  N_U=0 surely;
H_+:  N_U~Binomial(n,q_epsilon).
```

**Theorem C (sharp sample distinguishability).** At each fixed admissible epsilon,

```text
TV(mu_+^{tensor n}, mu_-^{tensor n})
       = 1-(1-q_epsilon)^n,
R_n^*(epsilon) = (1-q_epsilon)^n/2
```

for equal hypothesis priors and 0-1 loss. An optimal rule is: decide `H_+` iff at least one exact atom `Z=U` was observed.

*Proof.* Partition the sample space into `A={N_U=0}` and its complement. Under `H_-`, `A` has probability one. Under `H_+`, `P(A)=(1-q)^n`; conditional on `A`, the observations have exactly law `nu^{tensor n}`, the same as under `H_-`. The complementary component is singular to the `H_-` law. Thus the product-law TV and likelihood-ratio optimality follow directly. QED.

**Theorem D (exact minimax over unknown real tilt).** Let one deterministic or randomized test be used without knowing epsilon, and define its worst-case equal-prior risk over all common parameters `epsilon<=E`. Then

```text
inf_tests sup_{epsilon<=E} risk_n(test,epsilon)
      = (1-q_E)^n/2
      = ( (4822040484/8132285009)^n ) / 2.
```

The same formula remains valid if the two hypotheses are separately allowed adversarial epsilons in the admissible half-line. The atom-presence test attains this bound: its false-positive probability is zero for every epsilon, and its false-negative probability is `(1-q_epsilon)^n <= (1-q_E)^n`. For the lower bound, the adversary can select the *same* endpoint parameter `epsilon=E` under both hypotheses, where Theorem C establishes the irreducible Bayes risk. This proves minimax equality without making the nuisance parameter observable.

For target uniform worst-case error `0<r<1/2`, the minimum required positive integer sample count is

```text
n_min(r) = ceil( log(2*r)/log(1-q_E) ).
```

For example, `n=5` gives a worst-case Bayes error of approximately `0.036648931016`; the decimal is only a display of the exact rational expression.

## 5. Research significance and limits

The **BRC-style positive branch mass carrier** consists of continuous mass `A`, clipped mass `B`, their ratio `q=B/(A+B)`, the conditional continuous law `nu`, and the distinguished clipped port `U`. Theorem A is a precise test for whether a proposed observer quotient preserves the branch interface: the source label can be removed from the *single-sample phase test* exactly when the declared readout retains the atom-versus-continuous distinction, or its loss is quantified by the formula above. This is not a claim that the same compression is sufficient for arbitrary later native operations.

All claims are exact within the inherited external price experiment. The independent native 228-query Bellman optimum, the frozen input, P000 (native six-dimensional Cell space and its three-dimensional slices), and the ACTIVE residual-fidelity worldview are unchanged. No native coordinate transfer, physical interpretation, formal Task CLAIM, Result, or Review is established here.

**Verification:** accompanying `EC49FUC_OBSERVER_MINIMAX_VERIFY.py` uses Python standard-library `Fraction` to recompute the inherited rational `q` from `A,B`, endpoint bounds, quantizer integral, exact benchmarks, and the (n)-sample risk formula. Finite rational probes are regression only; Theorems A–D are analytic proofs for **all finite real epsilon<=E**, all measurable channels of the specified kind, and all positive integer n.

**Next research:** (i) classify channels retaining the interface under sequential operations rather than only this declared hypothesis test; (ii) derive sharp robust minimax risks for specified nonzero detector bin width/noise, where exact point-mass detection is unavailable; (iii) independently reconstruct the actual frozen native `z<11/16` Bellman branch before claiming any new native switching boundary.
