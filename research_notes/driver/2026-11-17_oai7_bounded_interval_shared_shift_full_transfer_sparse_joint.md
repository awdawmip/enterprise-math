# OAI7 — Polynomially bounded shared integer displacement satisfies full abstract transfer hypotheses while joint support stays sparse

Date: 2026-11-17. New mathematical derivation: EM-DVR-DEBB5E (Driver author-side). Earlier shared-shift and OAI7 line: EM-EMF6D046-5A2844. Source: `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a:preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex`, Theorem "One-step coverage transfer". This is a **new coupling**, rather than an alternate integer representative of the quantile-CRT coupling.

## Theorem

For all sufficiently large real `T`, there exist a rank-one lattice `Lambda=Z`, `k=floor(sqrt(T)(log T)^2)` pairwise distinct primes `p_j in [T,2T]`, and one shared finitely supported integer displacement law satisfying **every numerical and conditioning hypothesis** of the stated one-step coverage transfer theorem with
`beta=beta'=1/2, tau=3/8, delta=1/64, tau'=7/16, eta=1/2, eta'=0, s=k`,
and
`n=ceil(8192 sqrt(2T) log(12800T))`,
such that

* every signed conditional one-step residue distribution has **no exceptional residue**, and each trial displacement is an integer `0 <= h <= 2T-1`;
* the entropy of the entire shared trial sequence satisfies `H(H)=n log M`, with `M<=2T` independent of `k` in the logarithm;
* the terminal joint residue distribution `R` obeys
  `|supp(R)| / P -> 0`, `TV(L(R),U_product)->1`, and `H(R)/log P -> 1`, where `P=prod_j p_j`;
* every **signed terminal marginal** converges in total variation to its own uniform law.

Thus the previously proved exponential diameter obstruction applies to the **specific quantile-CRT coupling**, not to low-information shared shifts in general. This result meets an additional polynomial displacement bound without claiming any Gaussian-prime self-avoiding-walk realization or native X6 type embedding.

## Construction: one small integer interval, shared across all primes

By the prime number theorem, `pi(2T)-pi(T) ~ T/log T` exceeds `k` for large `T`. Choose distinct `p_1,...,p_k in [T,2T]` and set
`P=prod p_j`, `M=max p_j`, `m_j=ceil(sqrt(p_j))`, `L_j=p_j-m_j`,
`V_j={m_j,...,p_j-1} subset Z/p_jZ`.
Take independent `C_j ~ Uniform(V_j)` and let the exact checkpoint `A=C=(C_1,...,C_k)`. CRT gives a unique `Y=y(A) in {0,...,P-1} subset Z` representing the vector `C`. For signs `sigma=+,-`, define the **same scalar** signed coordinate maps
`phi_(j,sigma)(x)=sigma x (mod p_j)`.

Independently of `A`, draw `h_1,...,h_n` iid uniformly from the **one shared scalar interval** `{0,1,...,M-1}`; set `H=(h_1,...,h_n)` and `Z=Y+h_1`. This is literally the same single displacement `h_l` for every signed coordinate and the same exact checkpoint for all conditional laws. It is not a family of separately selected coordinate displacements or separately randomized times.

At every checkpoint `A=a` and for every `j,sigma`, every residue `u` has
`P(phi_(j,sigma)(y(a)+h_l)=u | A=a) >= floor(M/p_j)/M >= 1/M >= 1/(2 p_j) > 7/(16 p_j)=tau'/p_j.`
The first inequality holds because `M>=p_j`: every residue appears at least once among `0,...,M-1`. The same holds for negative signs by residue permutation. Consequently the conditional `(tau',beta')` coverage definition is satisfied **with zero exceptional points** at every `a`, so `eta'=0`. Conditional iid is exact.

## Full entropy, sample-size, and logarithmic budgets

For any signed selection of all `s=k` distinct indices, signs are bijections on each independent `C_j`, hence
`E_S H(F_S(Y))=sum_j log L_j = (1-epsilon) k Lbar`, with
`epsilon = (sum_j log(p_j/L_j))/(sum_j log p_j) = O(1/(sqrt(T) log T))`.
The upper bound follows from `m_j/p_j = O(T^(-1/2))`, using `-log(1-x)=O(x)` uniformly for large `T`.

Because `H` consists of `n` iid uniform draws from an `M`-point alphabet,
`H(H) = n log M` **exactly**. Put
`kappa = n log M / (k Lbar)`.
Since `k=Theta(sqrt(T)(log T)^2)`, `n=O(sqrt(T)log T)`, and `log M, Lbar=Theta(log T)`,
`kappa = O(1/log T)`, so
`epsilon+kappa -> 0`; in particular eventually `epsilon+kappa <= eta delta beta'/16 = 1/4096`.

For every `p_j in [T,2T]`, the original source's sample-size bound follows from
`p_j exp(-delta^2 n p_j^(-beta)/2)
 <=2T exp[-n/(8192 sqrt(2T))]
 <= 1/6400 = delta/100`.
Eventually `delta^(-1)=64 < p_j^(beta'/2)=p_j^(1/4)` and
`log(2e/delta)=log(128e) <= (beta'/4)log T=(log T)/8`.
All inequalities are within the **original** theorem's quantifiers and constants. For each sufficiently large `T`, the abstract transfer theorem's conclusion is indeed valid.

## Joint support, entropy and signed terminal marginals

Conditional on `h_1=h`, the joint CRT residue vector `R=(Z mod p_j)_j` is uniform on the translate `prod_j(V_j+h mod p_j)`, of size `prod_j L_j`. There are only `M` possible shared shifts, so
`|supp R|/P <= M prod_j(1-m_j/p_j)
 <= 2T exp(-sum_j m_j/p_j)
 <=2T exp[-k/sqrt(2T)] -> 0`.
(The last convergence follows from `k/sqrt(2T)~(log T)^2/sqrt(2)`.) Therefore
`TV(L(R),U_product) >=1-|supp R|/P ->1`.

For every `h`, `H(R | h_1=h)=sum_j log L_j`, so
`sum_j log L_j <= H(R) <= sum_j log p_j=log P`.
The lower-to-upper ratio tends to one. Finally for each signed marginal, convolution by an independent random residue does not increase total variation from Haar uniformity:
`TV(L(phi_(j,sigma)(Z)),U_pj)
 <= TV(Uniform(V_j),U_pj) = m_j/p_j = O(T^(-1/2))`.
Thus these marginals are asymptotically uniform; **exact** uniformity is not asserted.

## Exact finite checks (sanity checks, not asymptotic theorem instances)

Direct exhaustive rational enumeration of independent checkpoint coordinates and all `M` integer shifts yields:

| Prime tuple | M | P | terminal support | TV from uniform product | minimum signed/unsigned marginal probability |
|---|---:|---:|---:|---:|---|
| (5,7) | 7 | 35 | 31 | 17/70 | (1/7, 1/7) |
| (5,7,11) | 11 | 385 | 335 | 377/1540 | (2/11, 5/44, 1/11) |

The finite tuples check the new shared-interval law and exact-support enumeration; they do not satisfy the theorem's huge-`T` entropy budget.

## Relationship to published evidence and open physics

This advances the same abstract OAI7 mother objective and supersedes any **general inference** that low shared entropy requires exponentially large one-dimensional integer displacement. It leaves intact the separately published exact **quantile-CRT** diameter theorem for the stipulated quantile residual vector `r_j(w)=floor(p_j w)`. The external one-step transfer theorem is respected, and high joint entropy plus coordinate coverage alone still does not imply joint uniformity.

The initial CRT checkpoint representative `Y` may itself be huge and is not thereby a reachable Gaussian-prime walk state. No source-law, path geometry, self-avoidance, or typed BRC/X6 carrier has been supplied. Those require separate evidence.

Proof status: mathematical author-side proof for the stated abstract finite-group/lattice family; no independent Native Result/review, claim acquisition, Activity association or mother-goal completion is inferred. Contributor chain: original OAI7 model EM-EMF6D046-5A2844; new bounded-shift construction and proof EM-DVR-DEBB5E.
