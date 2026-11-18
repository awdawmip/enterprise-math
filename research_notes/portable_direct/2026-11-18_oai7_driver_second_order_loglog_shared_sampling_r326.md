# OAI7 r326 — Second-order log-log savings at the critical shared-schedule coefficient

Date: 2026-11-18. Status: source-exposed, author-side mathematical derivation; independent portable GitHub preservation. This is **not** an independent review, Native Result, Task/CLAIM/Activity transition, or Heartbeat X6 realization. Preserve original OAI7 researcher EM-EMF6D046-5A2844 and the distinct r307/r321–r325 contributions. In particular, r321 supplies the first-order lower coefficient and r325 supplies the finite-independence estimate used here.

## Theorem: a shorter critical schedule with vanishing worst-set failure

Let `b=17/64`, `J=1-b+b log b`, `c_*=1/(4J)`, `x_0=1/W_0(e^{-1})`, `a_b=b+x_0`, all logarithms natural, and `L=log p`. Let `w=w(p)` be any positive function on primes such that `w(p) -> +infinity`, `w(p)=o(log L)` as `p->infinity`. For every sufficiently large prime `p`, put

```text
u = ceil(sqrt(p)),          rho = u/p,
n = ceil(c_* sqrt(p) [L - 2 log L + w(p)]),
mu = n rho,
t = 2 ceil(a_b mu/2),       k = s = 4096 t + 1.
```

Use the *same* r325 construction: `Y_j` independent and uniform on standard integer representatives of `F_p \ B_0`, with `|B_0|=u`; `P(z)` a uniformly random polynomial over `F_p` of degree at most `t-1`; and the single common integer vector `h_l=([P(l)]_p,...,[P(l)]_p)` for `0<=l<n`. Use all `2k` signed homomorphisms `phi_(j,+/-)(v)=+/-v_j mod p`.

Then the full-lattice terminal variables `Y+h_l` have identical laws, each terminal signed marginal is uniform, and each initial signed marginal omits `u` residues. Moreover `t<=n<p` and the shared entropy is exactly `H(H)=t log p=O(L^2)`; the original r307 entropy/logarithmic conditions hold for all sufficiently large `p`. For every signed coordinate `c`, uniformly over **each fixed deterministic** `u`-element test set `K` chosen before the random common schedule, the original r307 short-list tail obeys

```text
q_c <= (C_b/sqrt(c_*) + o(1)) exp[-w(p)/4] -> 0,

C_b = 1/[(1-b) sqrt(pi b)] + 2/sqrt(2 pi a_b)
    = 1.8969235863934224...
```

Consequently the original integrated-tail requirement `R_0 <= max_c q_c < 111/4352` eventually holds. This improves the r325 `n=ceil(c_* sqrt(p) L)` upper construction by

```text
n_r325 - n_r326
  = c_* sqrt(p) [2 log log p - w(p)] + O(1),
```

while preserving vanishing worst-set failure and the same `O((log p)^2)` seed-entropy order. This is a *second-order constructive upper bound*, not a matching second-order lower theorem.

A concrete choice `w(p)=4 log log L=4 log log log p` (for sufficiently large `p`) gives

```text
n = ceil(c_* sqrt(p) [log p - 2 log log p + 4 log log log p]),
q_c = O(1/log log p) -> 0.
```

## Proof

The point-mass / finite-independence theorem r325 (R325.1) applies because `t` is even, `t>=a_b mu`, `mu>=2/b`, and `t<=n` eventually. For each fixed start `x`, sign `c`, and deterministic `K` of size `u`, the polynomial evaluations give `t`-wise independent Bernoulli(`rho`) hits, so

```text
Pr[X_(c,K,x) <= b mu]
 <= exp[-J mu]/sqrt(mu)
    * {exp(b mu rho)/[(1-b) sqrt(pi b)] + 2/sqrt(2 pi a_b)}.
```

Summing over all `p` starts and applying Markov at the unchanged short-list size threshold `p^(3/4)`, uniformly in the deterministic `K`, gives

```text
q_c <= p^(1/4) exp[-J mu]/sqrt(mu)
       * {exp(b mu rho)/[(1-b) sqrt(pi b)] + 2/sqrt(2 pi a_b)}.
```

Since `u>=sqrt(p)`, the ceiling in `n` yields

```text
mu >= c_* [L - 2 log L + w(p)],
p^(1/4) exp[-J mu] <= L^(1/2) exp[-w(p)/4]
```

using the **exact identity** `J c_*=1/4`. Also `mu=c_* L(1+o(1))`, `mu rho=O(L/sqrt(p))->0`. Thus the braces tend to `C_b` and `sqrt(mu)=sqrt(c_* L)(1+o(1))`, proving the stated uniform `q_c` bound and its rate.

For large `p`, `n=O(sqrt(p) L)<p`, `t=O(L)<=n`. The first `t` evaluations recover the polynomial coefficients by Vandermonde inversion, hence `H(H)=t log p`. The original `S` in r307 selects `s=k` **distinct base indices** with one sign per index. Therefore `H(F_S(Y))=s log(p-u)`, and its relative entropy deficit is `epsilon=-log(1-u/p)/log p=O(p^(-1/2)/L)`. Since `k=s=4096t+1`, the exact information slack `1/4096-t/s=1/[4096(4096t+1)]` is `Theta(1/L)`, which eventually strictly exceeds `epsilon`. The r307 log-size prerequisite also holds. The sample vector remains one common displacement schedule, with no post-sampling test-set adaptation.

## Fixed second-order offset at the r307 positive-tail budget

If instead `n=ceil(c_* sqrt(p) [L - 2 log L + d])` for a **fixed** real `d`, the same argument gives

```text
limsup_(p->infinity) max_c q_c <= (C_b/sqrt(c_*)) exp(-d/4).
```

For `Q=111/4352`, the sufficient strict inequality is

```text
d > d_Q := 4 log[C_b/(Q sqrt(c_*))] = 18.08557231667795...
```

For example `d=20` yields `limsup q_c <= 0.0158043903380... < Q`. This finite additive shift is sufficient for eventual admissibility, whereas `w(p)->infinity` establishes the stronger `q_c->0`. Neither statement gives a finite-p certified cutoff without a separate explicit numerical threshold check.

## Provenance and unresolved questions

- Mathematical base: r307 integrated-tail theorem at `baaaabaacaf8543f62a45a00cdfcf03e95389075`.
- Necessity: r321 universal leading coefficient `c_*` at `3c411d17ca496dfcfcdb91082643597981f6b9d2`; no second-order necessity is claimed.
- Shared polynomial schedule / pointwise tail: r322–r324; the precise Lambert-W point-mass prefactor is r325, `6634ecc793d149a55c88ceb6a9780a2f3ec5eac3:research_notes/portable_direct/2026-11-18_oai7_driver_lambertw_critical_tail_seed_bound_r325.md`.
- New contribution r326: second-order log-log improvement and its fixed-offset admissibility test, conditional only on the stated earlier proven transfer and moment bounds. The finite-group model is external; an ordered native six-axis Heartbeat path and Gaussian-prime-walk transfer remain separate source-typed questions.
- Original OAI7 Task `RS-OAI7-028-C-20261007-6F2A81` has its own immutable publication, old researcher source and current canonical runtime. This note gives no new CLAIM, formal review or parent completion.

No sorry/admit, custom target axiom, simulation-only assertion or undocumented independence assumption is used.
