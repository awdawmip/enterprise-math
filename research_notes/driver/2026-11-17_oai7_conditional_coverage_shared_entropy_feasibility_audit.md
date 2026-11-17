# OAI7 / coverage-transfer — exact conditional support and common-data entropy feasibility

Date: 2026-11-17. Scope: mathematical Driver audit and new derived necessary bound, not a native Result acceptance or a replacement of the independent author record. Driver contribution: EM-DVR-DEBB5E. OAI7 construction and executable checks: the author of `RS-OAI7-028-C-20261007-6F2A81`, session `MCP-c618a61189764f23846a391a08518a1a`; retain original source attribution. Underlying transfer theorem: `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`, `preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex`.

## Audited claims and source pins

- Original author's [shared-bit marginal repair and finite obstruction](https://github.com/awdawmip/enterprise-math/blob/3ae158973f1c11152badbfc19f2ec655bdc3bd6f/research_artifacts/mcp/RS-OAI7-028-C-20261007-6F2A81/MCP-c618a61189764f23846a391a08518a1a/6df1b102f9d377956aeb/OAI7_028_C_SHARED_SHIFT_COVERAGE_PROOF_20261117.md), and [biased Bernoulli threshold and information cost](https://github.com/awdawmip/enterprise-math/blob/3ae158973f1c11152badbfc19f2ec655bdc3bd6f/research_artifacts/mcp/RS-OAI7-028-C-20261007-6F2A81/MCP-c618a61189764f23846a391a08518a1a/6df1b102f9d377956aeb/OAI7_028_C_BERNOULLI_SHIFT_COST_20261117.md).
- The original transfer theorem has finite `A`, `Y=y(A)`, conditionally iid `h_1,...,h_n | A=a ~ nu_a`, common `H=(h_1,...,h_n)`, terminal `Z=Y+h_1`, and $T\le p_j\le 2T$. At every `a`, at least fraction `1-eta'` of the `2k` signed marginals have conditional `(tau',beta')` coverage. The same theorem imposes `H(H) <= kappa*s*Lbar`, `epsilon+kappa <= eta*delta*beta'/16`, and the sample-size inequality for every `p_j`.
- Direct inspection confirms the author's exact two-shift probabilities and interval `a=tau(p-m)/p <= q <= 1-a` for unconditional marginals. At the interval endpoints, equality to the probability floor is permitted; outside, exactly `m` residues violate the floor. No claimed contradiction of the external transfer theorem follows from this marginal construction.

## Lemma 1: least entropy of one covered finite marginal

Fix an alphabet of size `p`, `0<beta'<1`, and `0<tau'<1`. Put
\[
 t_p=\lceil p^{1-\beta'}\rceil,\quad r_p=p-t_p+1,\quad \alpha_p=\tau'/p.
\]
Suppose a distribution `X` has strictly fewer than `p^(1-beta')` residues with mass below `alpha_p`. Then at least `r_p` residues have mass at least `alpha_p`. For `r_p>=1`,
\[
\boxed{H(X)\ge b_p:=
 -(r_p-1)\alpha_p\log\alpha_p
 -[1-(r_p-1)\alpha_p]\log[1-(r_p-1)\alpha_p].}
\]
This is sharp as an entropy bound for the coverage premise alone: put mass `alpha_p` on `r_p-1` symbols, mass `1-(r_p-1)*alpha_p` on a final one, and zero on the rest. The large mass is at least `alpha_p` because `r_p*alpha_p <= tau'<1`.

**Proof.** In descending order, any distribution with `r_p` masses at least `alpha_p` satisfies `sum_(i=1)^j x_i <= 1-(r_p-j)*alpha_p` for `j<=r_p`. The displayed extremal vector attains each bound and hence majorizes the distribution. Shannon entropy is Schur-concave. For `r_p=1`, the bound is zero, as expected. In particular,
\[
 b_p\ge (p-\lceil p^{1-\beta'}\rceil)(\tau'/p)\log(p/\tau').
\]

## Theorem 2: unavoidable per-trial entropy charge under the transfer hypotheses

Use **exactly the conditional experiment and coverage hypotheses** of the original One-step coverage transfer theorem. In particular, `eta' <= eta*delta/100 < 1`; at each `A=a` at least one signed coordinate `c` is conditionally covered. For its modulus `p_c`, translating by `phi_c(y(a))` preserves the covered-law entropy, so
\[
 H(\nu_a)\ge H(\phi_c(h_1)\mid A=a)\ge b_{p_c}\ge b_*,
 \qquad b_*:=\min_{1\le j\le k} b_{p_j}.
\]
Conditional independence and the chain rule now give the exact lower bound
\[
\boxed{\;H(\mathcal H)\ge H(\mathcal H\mid A)
 =n\mathbb E_a H(\nu_a)\ge n b_* .\;}
\]
Consequently a **necessary** condition for the original entropy-budget premise is
\[
\boxed{\kappa s\overline L\ge n b_*.}
\]
This result does not require the conditional laws to have independent coordinates, only their stated independence *across samples given the same* `A`.

For a uniform, explicit but weaker inequality, set
\[
 C_T=\max\{0,1-T^{-\beta'}-1/T\}.
\]
Since `T<=p_j<=2T`, the preceding lemma yields
\[
\boxed{\kappa s\log(2T)\ge n\tau' C_T\log(T/\tau').}
\]
The theorem's own sample-size requirement gives, for every `p_j`,
\[
n\ge {2\over\delta^2}p_j^{\beta}\log(100p_j/\delta)
\ge {2\over\delta^2}T^{\beta}\log(100T/\delta).
\]
Thus, whenever `C_T>0` and `kappa>0`, the original premises jointly require
\[
\boxed{s\ge {2\tau' C_T\over \kappa\delta^2}
 {\log(T/\tau')\over\log(2T)}
 T^{\beta}\log(100T/\delta).}
\]
Using `kappa<=eta*delta*beta'/16` yields the still stronger necessary bound
\[
\boxed{s\ge {32\tau'C_T\over \eta\delta^3\beta'}
 {\log(T/\tau')\over\log(2T)}
 T^{\beta}\log(100T/\delta).}
\]
Since `s<=k`, these are also lower bounds on the number of available coordinate indices `k` under the *simultaneous* source hypotheses. For fixed positive `tau',delta,beta,beta',eta` and increasing `T`, the lower bound grows on the order of `T^beta log T`. This is a feasibility constraint, not a refutation of the transfer implication.

## Exact shared-bit incompatibility with conditional coverage

For the author's displacement `h=Bm(1,...,1)`, conditional on the author's choice `A=Y`, each signed `phi_c(Y+h)` has at most two residue values. Therefore at least `p-2` values have conditional probability zero, and conditional `(tau',beta')` coverage fails whenever
\[
p-2\ge p^{1-\beta'}.
\]
The example `p=101`, `beta'=1/2` meets this inequality. For `tau'=7/16` the coverage-only entropy minimum from Lemma 1 uses `r_p=91` constrained residues and equals approximately `2.422939090849` nats per conditionally covered sample; the author's marginal Bernoulli entropy `0.637084540827` nats is correctly calculated for a **different, unconditionally repaired** marginal. Repeating a single bit across the `n` trials to avoid the linear entropy charge destroys conditional independence. Taking conditionally iid bits retains independence but still gives only two support values per conditional signed marginal.

## Review and continuation status

The independently checked original author's **unconditional** two-shift counting, exact threshold, and entropy accounting are mathematically consistent with the inspected source. The new inequalities isolate the conditional iid/common-data-budget interface as a necessary feasibility test, without changing the original author's propositions, proof scope, or contribution attribution. Next useful audit: determine whether the intended Gaussian-walk application has sufficiently growing `k,s` and a concrete `nu_a` to satisfy both conditional coverage and the lower bound, and examine the current native Result/publication before any immutable review. This file is a mathematical evidence note, not a source-native Result, REVIEW, accepted Task or closed mother objective.
