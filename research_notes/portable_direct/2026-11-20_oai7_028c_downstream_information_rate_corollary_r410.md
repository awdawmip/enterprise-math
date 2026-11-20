# OAI7 r410 — Downstream information-rate corollary of stronger Gaussian coverage

Date: 2026-11-20. Mathematical status: author-side analytic audit and corollary; **not** independent Native Review, accepted Result, Task DONE or mother-objective completion. Driver author `EM-DVR-DEBB5E`; original OAI7 researcher `EM-EMF6D046-5A2844` preserved.

## Frozen exact dependencies

- `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a:preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/information.tex` (Proposition "Information cost of one batch", including its posterior exact-start kernel and candidate-list argument).
- Same commit `build/schedule.tex` (original terminal coverage proposition, `q_T L_*>=c_0 T`, `e_0=beta_0/50`, fixed `beta_0=1/200`, `eta_0=1/100`, smoothing and displacement).
- r409: `awdawmip/enterprise-math@45252fc33c03ed0642eae71d8de9239b03fc1975:research_notes/portable_direct/2026-11-20_oai7_028c_absolute_margin_near_critical_coverage_r409.md` (author-side stronger `alpha_0(T)=1/100-M^7/logT`).

## Corollary (one explicit information-rate certificate)

Assuming the stated r409 mathematical lemma, keep **the original** walk, terminal law, all batch choices, word length `L_T=2^floor(log_2(T^(2/5)))`, and prior residue variables `X'_T,O'_T`. For all sufficiently large `M`, every selected batch satisfies the original proposition's conclusion with the *explicit permissible choice*

```text
K_0 = 64,
m_T = ceil(64 (T/L_T) log T),
c_1 = c_0/32000,
E_C I(X'_T; W_(L_T)(t_*) | O'_T) / L_T >= c_1 / log T.
```

This is an explicit certified positive constant in the unmodified downstream information proof. It is **not** asserted to dominate the best achievable original `c_1` over all choices of `K_0`; the source permits any sufficiently large fixed `K_0`.

## Verification of all changed quantitative steps

Write `alpha=alpha_0(T)`. The r409 exponent satisfies `0.009<=alpha<0.01` for all sufficiently large source batches, since `logT>=100^(ceil(M/2))` and `M^7/logT->0` uniformly. The `eta_0=0.01` favorable-coordinate posterior argument in the frozen information.tex uses only the all-exact-start bad-coordinate fraction and hence carries over verbatim.

The posterior mixture of exact-start terminal laws has at most `4p^(1-alpha)` poorly covered candidates (formerly `4p^(1-beta_0)`), for each favorable selected factor `pi`. The original disjoint-word-hit argument is unaffected by `alpha`: for each remaining candidate, one conditional package rejects it with probability at least `cL/p`, `c=tau_0/8=1/32`. Conditioned on `(O,X)`, the `m_T` packages are independent, so

```text
E[ |L_pi(P)| | O,X ] <=4p^(1-alpha)+p exp(-c L m_T /p).
```

Because `p<=2T`, `L m_T/p >=32logT`, hence `c L m_T/p >= logT`, and the second term is `<=p/T<=2<=p^(1-alpha)` for sufficiently large `T`. Therefore the right side is `<=5p^(1-alpha)`. Every favorable selected coordinate costs at most `(1-alpha)log p+log5` conditional entropy; a nonfavorable one costs at most `log p`. The same posterior/tower bound gives expected at most `2eta_0 q` nonfavorable selected coordinates. Consequently

```text
E_C H(X | O,P)
 <=(1-alpha)qL_*+2eta_0 alpha q log(2T)+q log5
 <=(1-0.96 alpha) qL_*
```

eventually, since `L_*>=logT`, `2eta_0 log(2T)/L_*->0.02`, `log5/(alpha L_*)->0`, uniformly. The frozen schedule independently guarantees `E_C H(X|O)>=(1-2e_0)qL_*`, with `2e_0=0.0002`. Thus

```text
E_C I(X;P|O) >= (0.96alpha-0.0002)qL_* >=0.008 qL_*.
```

The source's conditional-package subadditivity and its exact displacement-to-terminal mutual-information transport require no change:
`I(X;P|O)<=m_T [I(X';W|O')+2H(s)]`, and `H(s)=O_D(T^(1/4))`.
For large `T`, `m_T<=128(T/L)logT` and `qL_*>=c_0 T`, hence

```text
E_C I(X';W|O') >= (c_0/16000) L/logT - O_D(T^(1/4))
               >= (c_0/32000) L/logT
```

for sufficiently large `M`, because `L>T^(2/5)/2`, so `T^(1/4)=o(L/logT)`. This is uniform over the batches and the hypothetical zero-avoiding walks. The final telescoping upper bound and contradiction remain the *same original proof*. No new Gaussian-prime avoidance theorem, altered prime set, or world-model assertion is needed.

## Interpretation / limitations

r409's stronger residue-exception exponent **passes the next mathematically load-bearing information argument**, including the exact-start posterior mixture, and supplies an explicit alternative positive information rate. The original paper already proved a positive information rate sufficient for its final contradiction; this corollary does not automatically strengthen its qualitative final sieve conclusion. Both the r409 lemma and this derived result remain author-side and need genuinely independent review before Native admission.
