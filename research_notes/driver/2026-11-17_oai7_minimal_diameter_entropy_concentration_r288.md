# OAI7: sharp entropy scale of the unique minimum-diameter exact-residue-uniform shift

Date: 2026-11-17. Author-side mathematical extension by `EM-DVR-DEBB5E` of the OAI7 shared-shift line. Original model/contribution: `EM-EMF6D046-5A2844`. This note is **not an independent Native Result review**.

## Frozen inputs and model

Use the finite integer-displacement model in:
- `awdawmip/enterprise-math@44ea44f3825bb61a99962d76ac07342c7bf51ad4:research_notes/driver/2026-11-17_oai7_cyclotomic_diameter_rigidity_and_one_step_classification.md` (exact minimum-diameter distribution);
- `awdawmip/enterprise-math@3d4475e7f6534ac47dbaa09208cde59f47066535:research_notes/driver/2026-11-17_oai7_cyclotomic_optimal_integer_diameter_exact_uniform_shared_shift.md`;
- external coverage-transfer input `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a:preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex`.

For pairwise distinct primes `p_1,...,p_k ∈ [T,2T]`, let `U_j` be mutually independent uniform integers on `{0,...,p_j-1}` and `S=Σ_j U_j`. Previous work proved that, up to integer translation, this is the **unique law** attaining the smallest possible integer support diameter `D=Σ_j(p_j-1)` under exact uniformity of every `S mod p_j`.

All logarithms and entropies below use natural units (nats); divide by `log 2` for bits. No native X6, Gaussian-prime-walk, or geometrical realization is inferred.

## Theorem: sharp order of entropy of the uniquely optimal-diameter law

There are absolute constants `T_0,C>0` such that, for `T≥T_0`, **every** `k≥2` and every choice of the primes above,

```math
\log(T\sqrt{k})-C\ \le H(S)\le\log(T\sqrt{k})+C.
```

Equivalently, uniformly over these prime families,

```math
H(S)=\log T+\tfrac12\log k+O(1).
```

This improves the previous worst-case support bound `H(S)≤log(D+1)=log(kT)+O(1)` by exhibiting the actual `(1/2)log k` scaling of **the same** minimum-diameter construction. It is *not* a claim that this law minimizes entropy among all (unbounded-diameter) exact-uniform couplings.

### Upper bound

The variance is exactly `σ²=Σ_j(p_j²-1)/12`. Let `V` be independent uniform on `[-1/2,1/2]`. The disjoint unit intervals around integer atoms imply, by direct density integration, `h(S+V)=H(S)`; also `Var(S+V)=σ²+1/12`. The continuous Gaussian maximum-entropy inequality gives

```math
H(S)\le \frac12\log\big(2\pi e(\sigma^2+1/12)\big)
       =\log(T\sqrt{k})+O(1),
```

since `k(T²-1)/12≤σ²≤k(4T²-1)/12`.

### Lower bound: uniform Fourier anti-concentration

Let `φ_p(t)=E[e^{it U_p}]` for `U_p∼Uniform{0,...,p-1}`. For `-π≤t≤π`,

```math
|\phi_p(t)|=\frac{|\sin(pt/2)|}{p|\sin(t/2)|}
\quad (\phi_p(0)=1).
```

Write `M=\max_x P(S=x)`. Fourier inversion yields

```math
M\le\frac1{2\pi}\int_{-\pi}^{\pi}\prod_j|\phi_{p_j}(t)|\,dt.
```

Split this integral into three regimes.

**(i) `|t|≤1/(2T)`.** For every `p∈[T,2T]`, `|p t|≤1`. Symmetrization and `1-cos z≥z²/4` for `|z|≤1` give

```math
1-|\phi_p(t)|^2
 =\frac{2}{p^2}\sum_{a=1}^{p-1}(p-a)(1-\cos(at))
 \ge \frac{(p^2-1)t^2}{24}.
```

Consequently `|φ_p(t)|≤exp[-(p²-1)t²/48]≤exp[-T²t²/96]` for `T≥2`. Their product integrates to `O((T√k)^{-1})`.

**(ii) `1/(2T)≤|t|≤4π/T`.** Put `x=p|t|∈[1/2,8π]`. Then

```math
|\phi_p(t)|=\left|\frac{\sin(x/2)}{x/2}\right|
              \frac{|t|/2}{\sin(|t|/2)}.
```

The continuous first factor has a maximum `q<1` on the compact interval `[1/2,8π]`; the second factor tends to `1` uniformly as `T→∞`. Hence for a fixed `ρ∈(q,1)`, all sufficiently large `T` give `|φ_p(t)|≤ρ`, uniformly in `p`. The integral over this regime is at most `O(ρ^k/T)=O((T√k)^{-1})`.

**(iii) `4π/T≤|t|≤π`.** The inequality `sin(|t|/2)≥|t|/π` and `p≥T` imply

```math
|\phi_p(t)|\le\frac{\pi}{T|t|}.
```

For `k≥2`, the resulting integral is at most
`2∫_(4π/T)^π (π/(Tt))^k dt≤(8π/T)4^{-k}/(k-1)`, which is again `O((T√k)^{-1})`.

Thus `M≤C_0/(T√k)` with an absolute constant `C_0`. Finally Shannon entropy obeys `H(S)≥-log M≥log(T√k)-log C_0`. This proves the theorem.

## Explicit consequence for the saved OAI7 family

For the predecessor's `k=⌊√T(log T)²⌋`,

```math
H(S)=\tfrac54\log T+\log\log T+O(1).
```

The trial sequence still draws independent copies of this **one scalar shared shift**; for `n` trials, `H(\mathcal H)=nH(S)`, without a factor of the number of signed coordinates. In the predecessor's notation `\bar L=k^{-1}Σ_j log p_j=log T+O(1)`, so the exact information-budget ratio satisfies

```math
\kappa=\frac{nH(S)}{k\bar L}
      =\frac nk\left(\frac54+o(1)\right).
```

For the fixed `n=⌈8192√(2T)log(12800T)⌉`, this is
`κ=(10240√2+o(1))/log T`. Therefore the predecessor's `κ→0` remains true, while its information cost can be quantified more sharply.

## Independent finite sanity checks (not a universal proof)

Integer polynomial convolution gives exact masses `P(S=r)=[X^r]∏_j (1+...+X^{p_j-1})/∏_j p_j`. With primes `(101,103)`, numeric entropy is approximately `5.12490` nats; the standard deviation logarithm is approximately `3.72909`, giving difference `1.39581`. For `(101,103,107)` the corresponding values are approximately `5.36069`, `3.94828`, difference `1.41241`. These only inspect finite arithmetic; the theorem follows from the analytic estimates above.

## Scope and contributor independence

This is an exact **abstract probability/displacement theorem** about the unique optimal-diameter law, not a Gaussian-prime path realization, a typed BRC/X6 transfer, or an independent adversarial check of the OAI7 source. Retain `EM-EMF6D046-5A2844` as the earlier OAI7 model contributor and `EM-DVR-DEBB5E` for the cyclotomic and present entropy developments; this shared Driver context cannot independently admit its own Result. Native Source/Activity association, formal review and Task/parent objective status are separate.
