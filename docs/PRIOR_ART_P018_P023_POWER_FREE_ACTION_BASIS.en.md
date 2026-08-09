# Prior Art Note — P018/P023 Power-Free Future-Action Basis

Status: `RESEARCH PROVENANCE NOTE / NOVELTY_UNVERIFIED`  
Scope: bounded quotient-root state identification, minimum distinguishing action families, and power-free arithmetic

## 1. Conservative novelty position

The P018/P023 bridge must not present the following general ideas as Enterprise Math inventions:

- selecting a minimum family of tests/observations that distinguishes every pair of states;
- state-identification and distinguishing-sequence problems in finite-state systems;
- the generic Test Cover optimization problem and its computational-complexity theory;
- power-free / k-free integers, their decomposition, or their classical counting asymptotics.

Those are established mathematical and algorithmic structures.

The project-specific candidate is narrower: for the structured observations

`O_a(q) = R_r(floor(q/a))`,

on the bounded exact state domain `0,...,N`, the generic distinguishing-test optimization collapses to an exact forced basis consisting of the positive `r`-power-free integers up to `N`.

Historical priority for that exact specialization has **not** been established.

## 2. Minimum Test Cover is prior art

Crowston, Gutin, Jones, Saurabh and Yeo study the parameterized Test Cover problem, whose objective is to select tests so that every pair of items is distinguished by at least one selected test. [SRC-CROWSTON-TEST-COVER-2012]

Gutin, Muciaccia and Yeo study kernelization and complexity boundaries for the same generic Test Cover problem. [SRC-GUTIN-TEST-COVER-KERNELS-2012]

Therefore #233 does not claim novelty for the minimum-test / pairwise-distinguishing formulation itself. Its significance is structural: the quotient-root family admits a closed arithmetic characterization of every forced test/action rather than requiring a generic combinatorial optimization algorithm.

## 3. Power-free arithmetic is prior art

Power-free integers and their counting theory are classical. Mossinghoff, Oliveira e Silva and Trudgian provide a modern primary-source treatment of the distribution of `k`-free numbers and use the standard main scale `x/zeta(k)`. [SRC-MOSSINGHOFF-KFREE-2019]

Accordingly, #233 does not claim to invent `r`-power-free integers, their factor-removal interpretation, or their asymptotic density.

The Lean proof deliberately uses only a finite strong-descent existence argument for

`q = b * t^r`,

with `b` `r`-power-free; it does not rely on a new factorization theorem.

## 4. Exact Enterprise Math specialization

The branch proves, in warning-fatal Lean, the local law

`O_a(q-1) != O_a(q)  iff  q = a * t^r`

for some positive integer `t`.

Hence an `r`-power-free boundary `b-1 | b` can only be distinguished by action `a=b`. Conversely every positive boundary has a finite-descent decomposition `q=b*t^r` with `b` power-free, so those forced actions are sufficient.

Thus for any action set `A`,

`A separates every exact state in 0,...,N`

if and only if

`A contains every positive r-power-free b<=N`.

This makes the power-free set the unique least separating action family under inclusion.

## 5. Novelty boundary

The safest current classification is:

- **ADOPT** generic Test Cover / distinguishing-family problem language;
- **ADOPT / COMBINE** classical power-free integer structure and counting;
- **NOVELTY_UNVERIFIED** for the exact quotient-root closed-basis theorem and its use as a future-action-language specialization of P023.

Search performed during the current research session did not locate the exact quotient-root/power-free action-basis statement in the checked literature. That absence is not evidence of historical novelty. A broader dedicated literature review or external expert review is required before any priority claim.

## 6. Source registration

The primary sources used for this classification are registered in `sources_p018_p023_power_free_action_basis.json`; the project-side relation is registered in `lineage_p018_p023_power_free_action_basis.json`.
