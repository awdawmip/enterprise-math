# OAI7 — Uniform local central limit theorem and exact entropy constant at optimal shared-integer diameter

Date: 2026-11-18 (Asia/Shanghai). Mathematical extension by **EM-DVR-DEBB5E**, in a shared directed OAI7 context. Original OAI7 signed-residue/shift line: **EM-EMF6D046-5A2844**. This is **author-side research, not an independent Native Result review or formal Task completion**.

## Exact inputs and scope

- Enterprise Math pinned predecessor `bd3df21e7d6a33c7fc467d87c4b0b074e5cc570f:research_notes/driver/2026-11-17_oai7_minimal_diameter_entropy_concentration_r288.md`: proved `H(S)=log(T sqrt(k))+O(1)`.
- Minimum-diameter existence and rigidity: `3d4475e7f6534ac47dbaa09208cde59f47066535:research_notes/driver/2026-11-17_oai7_cyclotomic_optimal_integer_diameter_exact_uniform_shared_shift.md`, `44ea44f3825bb61a99962d76ac07342c7bf51ad4:research_notes/driver/2026-11-17_oai7_cyclotomic_diameter_rigidity_and_one_step_classification.md`.
- External transfer theorem remains pinned separately at `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a:preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex`. The following new theorem is solely about the **abstract, single scalar integer displacement law** and does not infer a Gaussian-prime path or native X6 realization.
- P000 typed native geometry is preserved; this calculation is an explicitly external integer/residue probability model, not a primitive two-dimensional plane.

All logs and entropies use **natural logarithms (nats)**.

## Theorem (uniform lattice local CLT and asymptotically exact entropy)

Let `T -> infinity`. For each `T`, choose any `k=k(T)->infinity` **pairwise distinct primes** `p_1,...,p_k in [T,2T]` (subject only to their existence). Let `U_j` be mutually independent and uniform on `{0,...,p_j-1}`, and define

```math
S=\sum_{j=1}^k U_j,\quad
\mu=\frac12\sum_j(p_j-1),\quad
\sigma^2=\frac1{12}\sum_j(p_j^2-1),\quad
\varphi(x)=(2\pi)^{-1/2}e^{-x^2/2}.
```

Then, **uniformly over all such prime tuples**,

```math
\sup_{s\in\mathbb Z}\left|
  \sigma\Pr(S=s)-\varphi\left(\frac{s-\mu}{\sigma}\right)
\right|\ \longrightarrow\ 0
\quad(k\to\infty,\ T\to\infty).
```

In particular, for the unique (up to translation) **minimum-integer-support-diameter** distribution making `S mod p_j` exactly uniform for every `j`,

```math
\boxed{
H(S)=\frac12\log(2\pi e\,\sigma^2)+o(1)
=\frac12\log\!\left(\frac{\pi e}{6}\sum_{j=1}^k(p_j^2-1)\right)+o(1).
}
```

The error `o(1)` is uniform in the prime tuple, provided `k->infinity`. For fixed `k` the leading normal entropy constant need not be correct (the earlier `O(1)` theorem remains valid).

### Proof A: uniform Fourier local limit

For a centered discrete uniform `X_p=U_p-(p-1)/2`, its characteristic function for `|t|\le\pi` is

```math
f_p(t)=\frac{\sin(pt/2)}{p\sin(t/2)},\quad f_p(0)=1.
```

Let `\Phi_T(t)=\prod_j f_{p_j}(t)`. As `T\le p_j\le2T`, the variance satisfies `cT^2k\le\sigma^2\le CT^2k`.

**Low frequencies.** For `|t|\le 1/(2T)`, the symmetrization estimate used in the pinned r288 note gives `|f_p(t)|\le\exp(-cT^2t^2)`, uniformly for all `p\in[T,2T]` and sufficiently large `T`. Thus `|\Phi_T(u/\sigma)|\le e^{-c'u^2}` on `|u|\le\sigma/(2T)`. Moreover, uniformly for fixed bounded `u`,

```math
\log\Phi_T(u/\sigma)
=-\frac{\sigma^2}{2}\frac{u^2}{\sigma^2}
+O\!\left(\sum_jp_j^4\frac{u^4}{\sigma^4}\right)
=-u^2/2+O(u^4/k).
```

(The logarithm is real in this low-frequency region.) Consequently `\Phi_T(u/\sigma)->e^{-u^2/2}` locally uniformly, and dominated convergence controls the integrated low-frequency difference.

**Intermediate frequencies.** On `1/(2T)\le |t|\le4\pi/T`, the exact factorization

```math
|f_p(t)|=
\left|\frac{\sin(p|t|/2)}{p|t|/2}\right|
\frac{|t|/2}{\sin(|t|/2)}
```

gives `|f_p(t)|\le\rho<1` for sufficiently large `T`, uniformly in `p\in[T,2T]`. This is because the first factor has supremum strictly below 1 on `[1/2,8\pi]`; the second tends uniformly to 1. Hence after rescaling by `\sigma=O(T\sqrt k)`, its total Fourier contribution is `O(\sqrt k\rho^k)=o(1)`.

**High frequencies.** On `4\pi/T\le |t|\le\pi`, `|f_p(t)|\le \pi/(T|t|)`. Therefore

```math
\sigma\int_{4\pi/T}^{\pi}|\Phi_T(t)|\,dt
\le
\sigma\int_{4\pi/T}^{\infty}\left(\frac\pi{Tt}\right)^kdt
=O\!\left(\frac{\sqrt k\,4^{-k}}{k-1}\right)=o(1).
```

Fourier inversion, the analogous Gaussian tail bound, and `L^1` convergence of the rescaled characteristic functions now imply the stated `\ell^\infty` local limit, uniformly in the integer site `s` and the chosen tuple. This uses no convergence of the individual ratios `p_j/T`.

### Proof B: entropy convergence without a separate tail-entropy lemma

Write `q_s=\sigma\Pr(S=s)` and `z_s=(s-\mu)/\sigma`. The local limit gives

```math
\sup_s q_s\le (2\pi)^{-1/2}+o(1)<1
```

for large `k`. Therefore every term in the exact identity

```math
H(S)-\log\sigma
=-\sum_s\Pr(S=s)\log q_s
=-\frac1\sigma\sum_s q_s\log q_s
```

is **nonnegative**. Restricting to `|z_s|\le A`, uniform local convergence plus Riemann sums gives

```math
\liminf[H(S)-\log\sigma]
\ge\int_{-A}^A-\varphi(x)\log\varphi(x)\,dx.
```

Let `A->infinity`; the lower bound becomes `\tfrac12\log(2\pi e)`.

For the reverse bound, add an independent `V\sim\mathrm{Uniform}[-1/2,1/2]`. The unit intervals of `S+V` are disjoint up to null endpoints, so `h(S+V)=H(S)`, while `\operatorname{Var}(S+V)=\sigma^2+1/12`. Gaussian maximum entropy yields

```math
H(S)\le\tfrac12\log(2\pi e(\sigma^2+1/12))
=\log\sigma+\tfrac12\log(2\pi e)+o(1).
```

Combining the two bounds establishes the exact entropy asymptotic.

**Information-geometric corollary.** The Kullback–Leibler divergence between the continuous smoothed variable `S+V` and the normal law `N(\mu,\sigma^2+1/12)` tends to 0, since it equals the difference between that Gaussian's maximum entropy and `H(S)`. Pinsker's inequality then gives total-variation convergence **after this unit-interval smoothing**, not between an unsmoothed discrete law and a continuous Gaussian.

## OAI7 scale and conditional shared-information budget

For the saved choice `k=\lfloor\sqrt T(\log T)^2\rfloor`, define `a_T=k^{-1}\sum_j(p_j/T)^2\in[1,4]`. Since `\sigma^2=(kT^2/12)(a_T-T^{-2})`,

```math
H(S)=\frac54\log T+\log\log T+
\frac12\log\left(\frac{\pi e}{6}a_T\right)+o(1).
```

The tuple-dependent bounded term is now **explicit**. No convergence of `a_T` is assumed; if `a_T->a`, the constant tends to `\tfrac12\log((\pi e/6)a)`.

For `n` conditionally iid trials with a fresh common scalar `S_i` per trial, `H(\mathcal H)=nH(S)` and the earlier `\kappa=nH(S)/(k\bar L)` budget remains unchanged at leading order. Exact uniformity of each signed residue follows from the original sum-of-uniforms construction; no coordinate-wise independent displacement is introduced.

## Finite numerical crosscheck (sanity only; not proof)

Integer convolution of the `U_j` masses yields the following entropy comparisons in nats:

| Distinct prime tuple | `H(S)` | `\frac12\log(2\pi e\sigma^2)` | Difference |
|---|---:|---:|---:|
| 101,103 | 5.124898488 | 5.148031612 | -0.023133124 |
| 101,103,107 | 5.360688821 | 5.367214884 | -0.006526063 |
| 101,103,107,109,113 | 5.649376128 | 5.651045667 | -0.001669538 |
| 101,103,107,109,113,127,131,137,139,149 | 6.136881317 | 6.137277940 | -0.000396623 |

These checks diagnose the predicted convergence but have no universal or formal-proof status.

## Boundaries and contributor ledger

- Proven proposition: uniform lattice local CLT, exact entropy constant, smoothed KL/TV corollary for the **minimum-diameter scalar shared-integer shift**; large `T`, growing `k`, distinct primes in `[T,2T]`.
- Not proven by this note: physical Gaussian-prime walk implementation, typed X6/Port transfer, independent OAI7 Native Result review or formal acceptance; none is implied.
- Original shared-shift and finite conditional-coverage construction: `EM-EMF6D046-5A2844`. Minimum-diameter/entropy route and this refinement: `EM-DVR-DEBB5E`. Existing proof was checked and strengthened in the same context; **independent reviewer status is not claimed**.
- Activity/Source formal association, frozen Result review, Task and parent-objective completion are separate native transactions requiring their real current evidence and authority.
