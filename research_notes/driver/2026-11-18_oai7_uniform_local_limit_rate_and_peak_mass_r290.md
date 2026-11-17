# OAI7 — Quantitative uniform local limit at the exact-residue-uniform minimum-diameter shift

Date: 2026-11-18 (Asia/Shanghai). Mathematical extension: **EM-DVR-DEBB5E**, in the same OAI7 directed context. Original OAI7 model and shared-shift contribution: **EM-EMF6D046-5A2844**. Author-side proof, not an independent Native Result review.

## Pins and exact model

Refine the verified local-CLT proof at `awdawmip/enterprise-math@15fc264baed37125817310f855b08bfda8f8be00:research_notes/driver/2026-11-18_oai7_optimal_shared_shift_local_clt_exact_entropy_r289.md`, whose exact Git blob is `8469b8f749e9f310a97e231d780d98991ad07617`; preceding entropy-scale proof is `@bd3df21e7d6a33c7fc467d87c4b0b074e5cc570f`. The unique minimum-diameter scalar law, up to translation, is `S=U_1+...+U_k` for **independent** `U_j~Uniform{0,...,p_j-1}` and **pairwise distinct primes** `p_j in [T,2T]`. This is a single scalar shared displacement in the external integer-residue model, not a claim of native X6/Port or Gaussian-prime-walk realizability.

Define `mu=sum_j(p_j-1)/2`, `sigma²=sum_j(p_j²-1)/12`, and `g(z)=(2 pi)^(-1/2) exp(-z²/2)`. Natural log units.

## Theorem: an absolute O(1/k) local Gaussian error

There exist **absolute** `T_0>=2` and `C>0` such that for every `T>=T_0`, every `k>=2` and every existing distinct-prime tuple `p_1,...,p_k in [T,2T]`,

```math
\boxed{
\sup_{s\in\mathbb Z}\left|
\sigma\Pr(S=s)-g\left(\frac{s-\mu}{\sigma}\right)
\right|\le\frac Ck.
}
```

In particular, writing `M=max_s P(S=s)`,

```math
\boxed{
\sigma M=\frac1{\sqrt{2\pi}}+
O\left(\frac1k+\frac1{\sigma^2}\right)
=\frac1{\sqrt{2\pi}}+O(k^{-1}),
}
```

uniformly in the prime tuple. The second equality uses `sigma² >= k(T²-1)/12`. Thus the earlier Fourier anti-concentration estimate `M<=C_0/(T sqrt(k))` has the asymptotically **sharp leading peak constant** `1/sqrt(2 pi)` in normalized variance units.

### Proof: quantitative Fourier L1 comparison

For each centered summand `X_p=U_p-(p-1)/2`, the real characteristic factor is

```math
f_p(t)=\frac{\sin(pt/2)}{p\sin(t/2)},\qquad
\Phi_T(t)=\prod_{j=1}^k f_{p_j}(t).
```

From the previous r289 proof, `sigma²\asymp kT²`, uniformly in the tuples. Fourier inversion and Gaussian inversion imply for each integer site `s`,

```math
\left|\sigma\Pr(S=s)-g((s-\mu)/\sigma)\right|
\le \frac1{2\pi}
\left(
\int_{-\pi\sigma}^{\pi\sigma}
|\Phi_T(u/\sigma)-e^{-u²/2}|\,du
+
\int_{|u|>\pi\sigma}e^{-u²/2}\,du
\right).
```

We bound the two integrals uniformly. For sufficiently large `k`, put `B=k^{1/8}` and split into four frequency regions. The finitely many `2<=k<k_0` can be absorbed into the same constant using the established uniform upper bound `sigma max_s P(S=s)<=C_0` from r288; this also handles any fixed choice of `T>=T_0`.

**Region I: `|u|<=B`.** Here `|p_j u/\sigma|<=C B/\sqrt k=O(k^{-3/8})`. Uniform Taylor expansion of the *real positive* factors yields

```math
\log f_p(t)=-(p²-1)t²/24+O(p^4t^4).
```

Summing gives

```math
\log\Phi_T(u/\sigma)=-u²/2+E_T(u),\qquad
|E_T(u)|\le C\frac{u^4}{k},
```

since `sum_j p_j^4/sigma^4=O(1/k)`. In this region `|E_T(u)|<=Ck^{-1/2}`, so for large `k`,

```math
|\Phi_T(u/\sigma)-e^{-u²/2}|
\le (C/k)u^4e^{-u²/4}.
```

Its `u`-integral is `O(1/k)`.

**Region II: `B<|u|<=sigma/(2T)`.** The same r288 low-frequency symmetrization gives `|\Phi_T(u/\sigma)|<=e^{-c u²}`. The Gaussian also decays. Their integrated tails are `O(e^{-c B²})=O(e^{-c k^{1/4}})=O(1/k)`.

**Region III: `sigma/(2T)<|u|<=4\pi\sigma/T`.** The uniform sinc bound for `p_j in [T,2T]` gives `|f_{p_j}(u/\sigma)|<=\rho<1`. The scaled interval length is `O(\sqrt k)`, hence the product contribution is `O(\sqrt k\rho^k)=O(1/k)`. The Gaussian tail is already exponentially small because `u\gtrsim\sqrt k`.

**Region IV: `4\pi\sigma/T<|u|<=\pi\sigma`.** By `|f_p(t)|<=\pi/(T|t|)`,

```math
\int_{4\pi\sigma/T}^{\pi\sigma}
|\Phi_T(u/\sigma)|\,du
\le
\sigma\int_{4\pi/T}^{\pi}
\left(\frac{\pi}{Tt}\right)^kdt
=O\left(\frac{\sqrt k\,4^{-k}}{k-1}\right)=O(1/k).
```

The Gaussian tails here and beyond `\pi\sigma` are negligible. Summing Regions I–IV proves the uniform `C/k` bound.

**Sharp peak coefficient.** The upper peak bound follows from `g(z)<=g(0)`. Choose an integer `s_0` closest to `\mu`, so `|s_0-\mu|<=1/2`, and use `g((s_0-\mu)/\sigma)=g(0)+O(\sigma^{-2})` for a matching lower bound. This gives the displayed `\sigma M` expansion.

## Finite convolution checks (not proof of the rate constant)

| Prime tuple | k | exact-convolution `sigma M` | difference from `1/sqrt(2 pi)` |
|---|---:|---:|---:|
| 101,103 | 2 | 0.404284715 | +0.005342434 |
| 101,103,107 | 3 | 0.374992069 | -0.023950211 |
| 101,103,107,109,113 | 5 | 0.386541672 | -0.012400608 |
| 101,103,107,109,113,127,131,137,139,149 | 10 | 0.392436609 | -0.006505671 |

The theorem is proved analytically; these are only numerical arithmetic checks of its qualitative behavior. The rate is **absolute but not optimized**; no explicit best `C` is asserted.

## Research boundaries and attribution

This quantifies the lattice local CLT of r289; it does not establish an `O(1/k)` *entropy* error, physical walk construction or typed native BRC/X6 portability. No Native freeze/review/CLAIM, Source/Activity admission, Task completion or parent-objective completion is implied. Prior OAI7 research contributor `EM-EMF6D046-5A2844` and author-side strengthening `EM-DVR-DEBB5E` remain distinct. Same-context authorship disqualifies calling this an independent adversarial review.
