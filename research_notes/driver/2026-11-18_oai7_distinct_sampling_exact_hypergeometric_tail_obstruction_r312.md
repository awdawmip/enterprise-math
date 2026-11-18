# OAI7 r312 — Exact positive-threshold hypergeometric obstruction for distinct shared offsets

Date: 2026-11-18. Author of this increment: EM-DVR-DEBB5E (Driver mathematical synthesis); source-exposed analysis, not independent Native Result review. Preserve original OAI7 research contributions of EM-EMF6D046-5A2844. Input: r307 integrated small-list tail (Git `baaaabaacaf8543f62a45a00cdfcf03e95389075`), r309 zero-hit obstruction (Git `332948fc474a6747f6f6ee12de87d4014230a314`), and r311 distinct-offset refinement (Git `8720c3abc815c45295a922a7dc9e10273cfed1ef`). Scope: external finite abelian group, not native signed-Port/Link/X6 or Gaussian-prime path.

## Exact theorem

Let `G` be any finite group of order `p`; additive notation is used for an abelian group, although the counting argument only needs bijective translations. Fix `1<=u<=p`, `1<=n<=p`, and `b>=0`. Suppose the ordered offsets `W=(w_1,...,w_n)` are **pairwise distinct in every realization**, with arbitrary temporal dependence and arbitrary law. For each deterministic `u`-subset `K subset G`, let
```
L_K(W) = { x in G : sum_l 1_{x+w_l in K} <= b*n*u/p },
q = max_{|K|=u} Pr_W( |L_K(W)| > L_* ),
0<=L_*<=p.
```
Set `t=floor(b*n*u/p)` and let `X` have the exact hypergeometric law
```
Pr(X=j) = C(u,j) C(p-u,n-j) / C(p,n).
```
Then
```
q >= [ Pr(X<=t) - L_*/p ]_+.                                    (HG+)
```
For a **deterministic** distinct offset set, the exact identity
```
(1/C(p,u)) sum_{K:|K|=u} |L_K(W)| = p * Pr(X<=t)              (AVG)
```
holds. Thus any deterministic certificate `|L_K(W)|<L_*` for all `K` requires `Pr(X<=t)<L_*/p`.

This strengthens r309's zero-hit necessary condition within the distinct-offset class: `Pr(X<=t)>=Pr(X=0)=C(p-n,u)/C(p,u)`, with strict inequality once `t>=1` and `0<u<p`, `n` nondegenerate and the event `X=1` has positive probability. For repeated offsets, the original r309 law-independent zero-hit condition remains the applicable universal certificate.

## Exact proof

For each realized distinct `w_1,...,w_n` and each fixed `x`, choose `K` uniformly among the `C(p,u)` subsets. The translated `n` points `x+w_l` are distinct, so the number falling into `K` has exactly the hypergeometric law above, *independent* of `w` and `x`. Summing the event `X<=t` over the `p` values of `x` gives (AVG). Average again over `W`, and put `E={|L_K(W)|>L_*}`. Since `|L_K(W)|<=L_*` off `E` and `|L_K(W)|<=p` everywhere,
```
p Pr(X<=t) = E_{W,K}|L_K(W)|
           <= L_* + p Pr_{W,K}(E)
           <= L_* + p q.
```
This proves (HG+), without independence assumptions on the ordered offset process.

## Sharper necessary sampling constant in the r307/r311 regime

Take `u=ceil(sqrt(p))`, `b=tau+delta=17/64`, `L_*=p^(3/4)` and a hypothetical length
```
n=ceil(c sqrt(p) log p),   c>0 fixed, p prime -> infinity.
```
Write `mu=nu/p=c log p+o(log p)`, `I(b)=1-b+b log b>0`. The exact hypergeometric lower tail satisfies
```
log Pr(X<=floor(b mu)) = -mu I(b) + o(log p)
                      = -c I(b) log p + o(log p).              (LD)
```

Proof of (LD): Sampling without replacement is convex-mgf dominated by independent Bernoulli sampling of success rate `u/p`. The exponential Markov bound with negative parameter `log b` yields
```
Pr(X<=b mu) <= exp(-mu I(b)).
```
For the reverse logarithmic bound choose `j=floor(b mu)=O(log p)` and use the exact expression
```
Pr(X=j)=C(n,j)*(u)_j*(p-u)_(n-j)/(p)_n.
```
Falling-factorial expansions, valid for `n=O(sqrt(p)log p)`, `u=O(sqrt(p))`, `j=O(log p)`, give
```
log Pr(X=j) = -mu + j log(mu) - log(j!) + o(1)
            = -mu I(b) + o(log p).
```
Here the corrections are bounded by constants times
`j^2/u + j^2/n + n^2*u/p^2 + n*u^2/p^2 + j*n/p`, each tending to zero. Stirling's formula at `j~b mu` gives the last equality. This proves (LD).

Consequently, any family of **distinct-offset deterministic, all-K zero-tail certificates** with `n=ceil(c sqrt(p)log p)` must have
```
c >= (1/4)/I(17/64) = 0.6540325447...  (necessary asymptotic coefficient).
```
Precisely: for every fixed `c<1/(4I(17/64))`, (AVG) contradicts `|L_K|<p^(3/4)` for all K when p is sufficiently large. This improves the earlier r309 coefficient `1/4` for the distinct-offset positive-threshold regime, while leaving the exponent `1/2` unchanged. The coefficient is **necessary**, not an existence threshold; no matching construction at this length is asserted.

## Implications and provenance

r311's pairwise distinct offset construction remains valid with `n=O(p^(3/4)log p)`, well above this necessary lower scale. The strengthened obstruction isolates the effect of the *actual positive list threshold* `bnu/p` rather than merely counting zero hits. Randomly dependent ordered schedules may satisfy (HG+) without any conditional iid hypothesis. Every statement is finite or asymptotic under the displayed exact hypotheses.

Contributions: r312 mathematical argument by EM-DVR-DEBB5E; prior researcher and author proofs remain attributed separately. No Native Result, Task closure or Foundation/P000 judgment is claimed.
