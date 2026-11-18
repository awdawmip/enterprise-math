# OAI7 r310 — Sublinear fully correlated shared schedule from a Fourier discrepancy certificate

Date: 2026-11-18. Research status: Driver-authored, human-checkable analytic existence proof; not a frozen Native Result, independent review, or project promotion. Author of this increment: EM-DVR-DEBB5E. Prior finite shared-shift results belong to EM-EMF6D046-5A2844. This is an **external finite cyclic residue model**, not a Gaussian-prime walk or native X6/Link/Port construction.

## Inputs and target

- Original exact finite-group transfer: `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a:preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex`. Its signed set `S` uniformly selects `s` distinct **base indices** and independent signs (not `s` arbitrary members of `2k` signed coordinates).
- Prior integrated worst-set tail criterion: `research_notes/driver/2026-11-18_oai7_integrated_list_tail_transfer_r307.md` (verified historical commit `baaaabaacaf8543f62a45a00cdfcf03e95389075`).
- Prior hypergeometric necessary sample bound: `research_notes/driver/2026-11-18_oai7_list_tail_hypergeometric_lower_bound_r309.md` (commit `332948fc474a6747f6f6ee12de87d4014230a314`).

Question: Can a single low-entropy, entirely dependent shared sample vector produce a zero worst-list tail with **n=o(p)** from a starting ensemble whose every signed marginal is actually deficient? r307's existing fully dependent example sampled all `p` cyclic offsets and started with uniform marginals.

## Theorem (a nonuniform-start, sublinear-sample witness)

Fix `tau=1/4`, `delta=1/64`, `beta=beta'=1/2`, `eta=1/2`, and let `p>=2^70` be any prime. Set
```text
G=Z/pZ,    u=ceil(sqrt(p)),    k=s=8192,
n=ceil(16 p^(3/4) log(8p)),    b=tau+delta=17/64.
```
Here all logarithms are natural. There exist fixed offsets `a_1,...,a_n in G` (repeats permitted) such that the following experiment satisfies **every assumption** of r307, with `xi=0` and `R_0=0`.

Let `Lambda=Z^k`, `phi_(j,+)(v)=v_j mod p` and `phi_(j,-)(v)=-v_j mod p`. Fix any `B subset G` of cardinality `u`, and let the integer representatives `Y_j`, independently over `j`, be uniform on `G\B`. Put `A=Y`. Independently take a *single* uniform seed `U in G`, and define the full-lattice shared shifts
```text
h_l = ( [U+a_l]_p, ... , [U+a_l]_p ) in Z^k,  l=1,...,n,
H = (h_1,...,h_n),    Z=Y+h_1,
```
where `[.]_p` denotes the representative in `{0,...,p-1}`.

Conclusions:

1. Each `Y+h_l` has the same full-`Lambda` law as `Z`. The sample vector is entirely dependent: `H` is determined by one `p`-valued seed, and `H(H)=log p`.
2. For **every** fixed signed coordinate and every deterministic `u`-set `K subseteq G`, every realization of `H` obeys `|L_{c,K}(H)|<p^(3/4)`, with the list defined by r307. Consequently `q_c=0` and `R_0=0`.
3. All `2k` signed marginals of `Y` **fail** `(tau,1/2)` coverage, having exactly `u>=sqrt(p)` zero-mass residues. Every signed marginal of `Z` is exactly uniform on `G`, and hence has `(tau,1/2)` coverage.
4. The original shared entropy hypotheses hold with `epsilon=log(p/(p-u))/log p`, `kappa=1/8192`, and `epsilon+kappa<1/4096=eta delta beta'/16`. The logarithmic hypothesis `log(2e/delta)<=(beta'/4)log p` also holds.
5. `n<p` for the specified range, and asymptotically `n=O(p^(3/4)log p)=o(p)`. Thus the construction uses strictly fewer shared samples than the r307 full cycle, while paying the same `log p` information cost.

The statement is an existence theorem for the offsets, with a finite randomized search and exact spectral verification procedure below; it does not provide a precomputed list for a particular enormous prime.

## Lemma: one offset multiset simultaneously controls all residue sets

For any prime `p` and positive `n`, there exists a multiset `a_1,...,a_n in G` for which
```text
max_{t in G, t != 0} | sum_l exp(2 pi i t a_l/p) |^2 <= 4 n log(8p).   (F)
```
To prove this, independently sample the offsets uniformly. For any nontrivial character `t`, the real and imaginary parts of its `n` independent unit-modulus summands are centered and lie in `[-1,1]`. Hoeffding and the union bound on the two parts give
```text
Pr( |sum_l exp(2 pi i t a_l/p)| >= lambda )
    <= 4 exp(-lambda^2/(4n)).
```
Set `lambda^2=4n log(8p)`, then union bound over `p-1` nonzero characters gives failure probability at most `(p-1)/(2p)<1/2`. Hence an offset multiset satisfying (F) exists. Repeated independent draws followed by checking (F) constitute a finite Las Vegas construction with success probability greater than `1/2` per attempt; this proof makes no arithmetic equidistribution assumption.

For a set `K subset G` of size `u`, write
```text
C_K(x) = sum_l 1_K(x+a_l),    mu=n u/p.
```
Discrete Fourier inversion and Parseval (with the unnormalized Fourier transform) yield
```text
sum_{x in G} | C_K(x)-mu |^2
  = (1/p) sum_{t!=0} |Ahat(t)|^2 |1_Khat(t)|^2
 <= 4 n log(8p) u.                                              (V)
```
The final step uses `(1/p)sum_t |1_Khat(t)|^2=u`. Therefore, for each `0<=b<1`,
```text
# {x : C_K(x) <= b mu}
   <= 4 p^2 log(8p)/[(1-b)^2 n u].                              (L)
```
This is simultaneous over *all* `u`-sets `K` once (F) holds; no union bound over `binom(p,u)` sets is needed. Negating all offsets preserves (F), so the same estimate applies to the negative signed coordinates.

Substituting the theorem's `b=17/64`, `u>=p^(1/2)` and `n>=16p^(3/4)log(8p)` into (L) gives
```text
# {x : C_K(x) <= b mu}
 <= [1/(4(47/64)^2)] p^(3/4)
 = (1024/2209) p^(3/4) < p^(3/4).                              (S)
```
Changing every offset by the same `U` merely translates the set of `x` in (S). This gives the deterministic worst-set small-list assertion, for both signs and each realization of `U`.

## Entropy, coverage and size verification

The original external theorem samples `S` by distinct base indices. Since the `Y_j` are independent uniform over `p-u` residues, for **every** such signed set `S`,
```text
H(F_S(Y)) = s log(p-u) = (1-epsilon)s log p.
```
The map `U -> H` is injective (already `h_1` determines `U`), hence `H(H)=log p=kappa s log p`. For `p>=2^70`, `u/p<=2/sqrt(p)`, so
```text
epsilon = -log(1-u/p)/log p
        <= 4/(sqrt(p)log p) < 1/8192.
```
Thus `epsilon+kappa<2/8192=1/4096`. Also `log(2e/delta)=log(128e)<(1/8)log p` at `p>=2^70`.

A signed `Y` marginal is uniform on a size-`p-u` subset, with exactly `u` absent residues, all below `tau/p`; hence it fails coverage. Because each `[U+a_l]_p` is uniform over `G` and independent of `Y`, the terminal signed residue of `Z` is uniform. All full-lattice marginals `Y+h_l` agree because the integer-valued diagonal shift is uniform on the same `p` representatives for every `l`. The shift vector's dependence across `l` affects none of these equal-marginal assertions.

Finally, `16p^(3/4)log(8p)+1<p` for `p>=2^70` (divide by `p` and note `16log(8p)/p^(1/4)+1/p<1` at `2^70` and decreases thereafter). This confirms strict sublinear sampling.

## Exact obligations, significance and limits

- This is a human-proof-valid **probabilistic existence** result with an explicit spectral certificate; the chosen offsets are not claimed numerically instantiated. A verifier can search `a_l` and check (F), then (V)–(S) analytically. The Fourier calculation depends only on elementary finite-group orthogonality and Hoeffding's inequality.
- Starting residue marginals are genuinely deficient and the shared sampling is genuinely dependent. This is stronger than the uniform-start/full-cycle illustration in r307.
- r309's `(beta'/2-o(1))p^beta log p` lower bound is for *almost-sure worst-set certificates*. Here `n=O(p^(3/4)log p)` exceeds that lower-bound scale for `beta=beta'=1/2`, so the two results are consistent. The exponent gap `1/2` vs `3/4` remains open for this general spectral design.
- Existence of this abstract schedule does not establish a realizable bounded-step Gaussian-prime path. No native X6/BRC observer, signed-Port, carrier or joint-path claim is made.
- Mathematical contributor here: EM-DVR-DEBB5E. Original OAI7 researcher and all prior contributions retain their own attributions. Native Result/review/Task completion are separately gated.

No `sorry`, `admit`, or custom-target axiom is used.
