# OAI7 r311 — Distinct shared offsets and the sharp signed-index budget

Date: 2026-11-18. Status: Driver-authored mathematical extension of the external finite cyclic residue witness, **not** Native Result admission or a Gaussian-prime/X6 walk theorem.
Author of r311: EM-DVR-DEBB5E. Preserve OAI7 initial researcher EM-EMF6D046-5A2844 and their separately recorded contributions.
Immediate input: r310, `research_notes/driver/2026-11-18_oai7_sparse_sublinear_correlated_shared_schedule_r310.md`, fixed Git commit `0e14b422d86160a4525f0dad734d96a6aabf3441`, blob `b7d53c16ea1c3e8ca0deb0c16f380d5dee950508`. Conditional transfer criterion: r307, `research_notes/driver/2026-11-18_oai7_integrated_list_tail_transfer_r307.md` at `baaaabaacaf8543f62a45a00cdfcf03e95389075`.

## Precise refinement

Fix the r310 parameters `tau=1/4, delta=1/64, beta=beta'=1/2, eta=1/2`, prime `p >= 2^70`, `u=ceil(sqrt(p))`, and

```
n=ceil(16 p^(3/4) log(8p)),  G=Z/pZ,
s=k=4097, b=tau+delta=17/64.
```

There exist **pairwise distinct** offsets `a_1,...,a_n in G` such that the r310 experiment with `Y_j` independent uniform on `G\B` (`|B|=u`), `U` an independent uniform single seed in `G`, and diagonal integer shifts
`h_l=([U+a_l]_p,...,[U+a_l]_p)` satisfies **all r307 hypotheses** with `xi=0`, `q_c=R_0=0`, including full-lattice equality of the laws of all `Y+h_l` and genuinely deficient starting signed marginals. In each realization, all `n` diagonal lattice shifts are distinct. In particular the construction requires only **4097** distinct signed base indices, rather than r310's 8192, while retaining the sublinear schedule length and single-seed entropy `H(H)=log p`.

Moreover, for *any* fully shared schedule with `H(H)=log p`, the r307 entropy budget under these fixed parameters and strictly positive start deficit `epsilon>0` requires `s>=4097`. Thus `s=4097` is the least feasible signed-index sampling count **within the r307 entropy hypotheses and this one-p-valued-seed entropy class**; it is not a universal lower bound for alternative shift-entropy structures or direct coverage-transfer proofs.

## Proof of distinct-offset certificate

Take `n<p` (verified below), and sample the `n` offsets *uniformly without replacement* from `G`. For a nontrivial additive character `chi_t(a)=exp(2 pi i t a/p)`, the real and imaginary parts each have population mean zero and lie in `[-1,1]`. Sampling without replacement is dominated by sampling with replacement for the moment generating function of any real sum of population values (the standard finite-population convex-order/Hoeffding comparison). Applying Hoeffding's lemma and the exponential Markov bound to real and imaginary parts therefore yields the same estimate used in r310:

```
P(|sum_l chi_t(a_l)| >= lambda) <= 4 exp(-lambda^2/(4n)).
```

Set `lambda^2=4n log(8p)`. Union bound over the `p-1` nontrivial characters gives failure probability at most `(p-1)/(2p)<1/2`. Hence a **distinct** offset set exists for which

```
max_{t!=0} |sum_l chi_t(a_l)|^2 <= 4n log(8p).  (F-distinct)
```

For any `K subset G`, `|K|=u`, Fourier inversion/Parseval then gives, exactly as in r310,
```
# {x: sum_l 1_K(x+a_l) <= b n u/p}
    <= 4p^2 log(8p)/((1-b)^2 n u)
    <= (1024/2209) p^(3/4) < p^(3/4).
```
The same estimate holds with `-a_l` and for arbitrary translation by `U`; it is simultaneous over every deterministic `K` and every realization of `U`. Thus `q_c=0` for every signed coordinate, and `R_0=0`. Distinctness is retained after adding `U` and under sign reversal. The equal full-lattice marginals, independence of `Y` and `U`, strictly deficient `Y` signed marginals and exactly uniform `Z` signed marginals follow unchanged from r310.

## Sharp entropy threshold and remaining quantitative checks

For the selected r307 parameters,
```
eta*delta*beta'/16 = 1/4096.
```
The `s` signed coordinates in r307 select `s` **distinct base indices**. Taking `k=s=4097` and the independent `Y_j` above gives `H(F_S(Y))=s log(p-u)` for every allowed signed set, hence
```
epsilon = -log(1-u/p)/log p > 0,
kappa = H(H)/(s log p) = 1/4097.
```
Since `u/p <= 2/sqrt(p)` and `-log(1-x)<=2x` for `x<=1/2`,
```
epsilon <= 4/(sqrt(p) log p)
        <= 4/(2^35 * 70 log 2)
         < 1/(4096*4097).
```
Therefore `epsilon+kappa<1/4096` as required. Conversely, when `H(H)=log p`, every permissible `kappa` satisfies `kappa>=1/s`. If `s<=4096` and `epsilon>0`, then `epsilon+kappa>1/4096`. This proves sharpness of `s=4097` for the stated entropy-budget class.

The logarithmic bound `log(128e)<(1/8)log p` and `n<p` for `p>=2^70` follow from the original r310 inequalities. The distinct-offset version uses the identical `n`, `u`, and `b` so no size coefficient changes are required.

## Validation scope and continuation

This proof changes **two exact quantitative properties** of the r310 witness: pairwise distinct offsets and sharp `s=4097` for the stated one-seed/positive-deficit budget. The `n=O(p^(3/4)log p)` bound and deterministic worst-set small-list certificate remain as in r310. It establishes an external finite-cyclic distributional construction, not bounded-step walk realizability, provenance-safe native signed-Port/Link transfer, or formal Task/Result completion. The `p^(1/2)` vs `p^(3/4)` schedule-length exponent gap remains a distinct mathematical problem.

Proof uses standard finite-population Hoeffding convex domination, elementary Fourier orthogonality and exact entropy accounting. No custom axioms and no external numerical approximation are proof premises.
