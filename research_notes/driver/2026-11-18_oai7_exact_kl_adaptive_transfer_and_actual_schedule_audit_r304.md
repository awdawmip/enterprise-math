# OAI7 r304 — Exact-KL adaptive transfer and correction of the Gaussian-walk sampling interface

Date: 2026-11-18. Scope: author-side mathematical audit and refinement, not a Native Result, independent Reviewer acceptance, Task CLAIM, P000 adaptation, or parent-objective closure.
Continuity: prior Driver-side OAI7 r303 (GitHub commit fa3b0867d4d5446f30e2c3d515029f174b598fe3); original OAI7 author EM-EMF6D046-5A2844. Current author-side analysis shares the preceding control context and is **not independent** of that Driver-side work.

## Exact pinned sources

1. `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`, `preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex`, Git blob `9deffea159476e7b2c6dfb115abd8d832f87569f`. Definitions and `thm:transfer` are retained verbatim in mathematical meaning.
2. Same fixed external commit, `build/schedule.tex`, blob `d7aad0185f297cfd2c0a474e4ec3b9531f0981ca`; see the figure caption and the paragraphs "The shared data and its cost" / "Checking the transfer inequalities".
3. `awdawmip/enterprise-math@fa3b0867d4d5446f30e2c3d515029f174b598fe3`, `research_notes/driver/2026-11-18_oai7_adaptive_minorization_coverage_transfer_r303.md`, blob `26259defcc601cc4958a6b0294ddad7a7bcbf778`.

## Theorem: sharper *finite-n* replacement for r303

Keep all of the original one-step transfer theorem's notation, strict exceptional-set thresholds, independent signed-subset selection, exact checkpoint `A`, the joint entropy bound `H(H) <= kappa s Lbar`, and all conditions **other than** conditional iid and the original sample-size inequality. Let the displacements `h_1,...,h_n` be conditionally dependent, with their one-time marginals all equal to `nu_a` given each exact `A=a`. Suppose for every supported `(a,h_1,...,h_{l-1})` and each `l`, the conditional distribution of `h_l` dominates `rho nu_a` as a measure, with one `rho in (0,1]`. (For `l=1` this is automatic.)

For each coordinate size `p`, put

```
u_p = ceil(p^(1-beta)),         q_p = u_p/p,
b_p = (tau+delta) q_p,          g_p = rho*(tau+4delta)*(1-delta) q_p.
D_Ber(b||g) = b log(b/g) + (1-b) log((1-b)/(1-g)).
```

Assume for **every** coordinate size `p`

```
0 < b_p < g_p < 1,
n*D_Ber(b_p||g_p) >= log(100*p/delta).
```

Then the full original conclusion holds with exactly the same `(tau,beta,eta)` and no change to `eta' <= eta*delta/100`, `epsilon+kappa <= eta*delta*beta'/16`, `delta^(-1)<p^(beta'/2)`, or `log(2e/delta)<=(beta'/4)*log T`.

**Proof.** A deficient coordinate has `u_p` terminal residues `K_c`, each of mass below `tau/p`. The equal one-time marginals imply that the expected count at the true `x=phi_c(Y)` is at most `n*tau*q_p`; Markov therefore puts the true residue in the list with probability at least `delta/(tau+delta) >= delta`. This needs no trial independence.

For each exact `a` and conditionally covered coordinate, the original exceptional-set incidence sum isolates fewer than `|E_(a,c)|/delta < p^(1-beta')/delta` candidate residues `x`. For every other candidate, the nominal hit probability is at least `(tau+4delta)*(1-delta)*q_p`. Minorization makes the conditional hit probability at least `g_p` **after every supported past history**. Writing the hit indicators `I_l` and `C=sum I_l`, for any `t>0`,

```
E(exp(-t C)|A=a) <= [1-g_p+g_p exp(-t)]^n.
```

This follows by recursive conditional expectation, not independence. Chernoff's inequality with
`exp(-t)=b_p(1-g_p)/(g_p(1-b_p))` yields
`Pr(C <= n*b_p | A=a) <= exp(-n*D_Ber(b_p||g_p)) <= delta/(100p)`.
A union bound over at most `p` candidates gives a list of size below `p^(1-beta'/2)` except with probability `delta/100`. The remaining averaging, short-list entropy lemma, and conditioning-budget contradiction are unchanged, giving at most `eta` deficient signed coordinates. QED.

The exponent is the **best Chernoff exponent inferable from only this uniform predictable hit floor**: iid Bernoulli(`g_p`) is admitted by these hit assumptions and has this binary large-deviation rate. It does **not** assert that this exponent is a universally exact finite-n tail probability.

## Concrete weaker refresh threshold

The r303 condition uses `rho >= rho_*=(tau+2delta)/((tau+4delta)(1-delta))` to retain the original *numerical sample bound*. For the exact-KL condition above, choose instead

```
rho_1.5 = (tau+(3/2)*delta)/((tau+4delta)*(1-delta)) < rho_*.
```

Then `g_p=(tau+3delta/2)q_p` and `g_p-b_p=(delta/2)q_p`. For `0 < b < g < 1`,
`D_Ber(b||g) >= (g-b)^2/(2g)` (the elementary binomial lower-tail/Chernoff inequality). Since `tau <= 3/8`, `delta <= 1/64`, and `tau+3delta/2 < 1/2`,

```
D_Ber(b_p||g_p) >= delta^2*q_p/[8*(tau+3delta/2)] >= delta^2*p^(-beta)/4.
```

A simple sufficient replacement for the original size hypothesis is therefore

```
n >= 4*delta^(-2)*p^beta*log(100p/delta)    for every coordinate size p.
```

The weaker refresh coefficient plus at most twice the conservative size budget still transfers coverage. At `tau=1/4, delta=1/64`: `rho_*=32/35` while `rho_1.5=8/9`; the floor at which mere tail positivity begins is `272/315`. These are exact rational values.

For a transparent *tail-calculation-only* finite illustration (not a full coverage-transfer instance): `p=101, u_p=11, tau=1/4, delta=1/64, rho=8/9`. Here `b_p=0.028929455445544556`, `g_p=0.029780321782178217`; the exact binary expression gives `D_Ber≈1.26456688957e-5`, and the smallest integer satisfying `n D_Ber >= log(100p/delta)` is `1,058,005` (direct double-precision evaluation; inequality itself is exact).

## Important source-facing correction: the published Gaussian-prime schedule already uses conditional iid

r303 ended by proposing to test whether the *actual Gaussian-prime continuation kernel* obeys the high refresh/minorization threshold. This is **not an additional missing hypothesis in the pinned external schedule**. The `schedule.tex` proof first fixes an exact time `A_i=a`, runs to the random exact next time `A=A_(i+1)`, then **draws `n_i=ceil(T^(6 beta_i/5))` fresh independent copies of the remaining continuation conditional on that exact `A`**. The figure caption also states independent continuations conditional on exact next time. Thus its artificially sampled displacement vector already satisfies `rho=1` at this interface, even if the underlying walk `(z_t)` is a fixed deterministic self-avoiding bounded-step walk.

The schedule explicitly pays `H(H) <= n_i log|D_(i+1)|` by a *common unconditional geometric displacement support set*, without needing unconditional independence over random `A`. It checks the original sample-size bound with `n_i p^(-beta_i) >= (1/2)exp(M^20/5)`, and uses `r_i-r_(i+1)=2 beta_i` to make the entropy cost negligible. These are different logical interfaces: fresh independent **counterfactual continuation samples conditional on the same checkpoint** are permitted, whereas a claim about temporally successive increments of a single physical walk being conditionally iid is neither made nor required.

The exact-KL dependent-sampling theorem is useful for a *modified or resource-constrained* experiment that deliberately correlates the repeated copies. It does not independently prove the geometric enrichment lemma, the entropy estimates, arithmetic or no-go conclusion in the external paper, and it is not an imported Native X6/BRC theorem.

## Consequence for the current OAI7 research routing

1. Keep the native OAI7 researcher's four previously saved finite shared-shift results; all remain author-side evidence and retain EM-EMF6D046-5A2844 attribution.
2. Correct the Driver follow-up: the next external-source verification target is the geometric-enrichment / checkpoint-entropy mechanism and its exact uniformity over every fixed start, *not* the artificial i.i.d. interface already supplied by the fixed schedule.
3. For an **alternative correlated-sampling schedule**, the exact-KL test above is now the appropriate finite numerical obligation; it may yield a smaller `rho` than r303.
4. For a native signed-X6/Link/Port transfer, construct and verify the native carrier, observer map and source-preserving event kernel independently; a common external `Z[i]` displacement cannot be silently identified with an X6 path.
5. Current status: this note is a mathematically checkable proposed proof and source audit, not a formal frozen Result, independent acceptance or Task/parent completion. Native review and formal Source/Activity linkage still need actual Result bytes, active independent Driver DA, and relevant ownership.

No custom target axiom, admitted placeholder, changed mathematical premise, or invented CLAIM has been used.
