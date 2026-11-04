# D25 — exact three-jet decomposition of the ORIGINAL 216 half sum

Date: 2026-11-05. Research lane: `chatgpt-research-onhour-enterprise-math-20260923`. Status: AUTHOR-PROVED / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED. This is a portable scientific unit, not a native H0/B0 benchmark or formal Result.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`.

## The exact original observable

For a prime `p=6n+1>=7`, set `N=3n=(p-1)/2`, `K=2n=(p-1)/3`, `Q=4n`. Define

`a_k = binom(2k,k)^2 binom(3k,k) / 216^k = (1/2)_k(1/3)_k(2/3)_k / (2^k k!^3)`,

`W_half = sum_{k=0}^N (6k+1)a_k`, and `W_full = sum_{k=0}^{p-1}(6k+1)a_k`.

Every denominator used below is invertible in `Z_(p)`. Define the terminating *integer-centered* coefficient for `0<=k<=K`:

`b_k = (-N)_k (-K)_k (-Q)_k / (2^k k!^3)`.

For these indices put

`L_k = sum_{j=0}^{k-1} [1/(2(j-N)) + 1/(3(j-K)) + 2/(3(j-Q))]`,

`J_k = sum_{j=0}^{k-1} [1/(4(j-N)^2) + 1/(9(j-K)^2) + 4/(9(j-Q)^2)]`.

For the *single-zero-factor* block `K<k<=N` define

`b*_k = (-N)_k (-Q)_k (-K)_K (k-K-1)! / (3*2^k*k!^3)`,

`L*_k = sum_{j=0}^{k-1}[1/(2(j-N))+2/(3(j-Q))] + (1/3)sum_{0<=j<k, j!=K} 1/(j-K)`.

Note `b*_k` is p-integral and the exact p-adic valuation of `a_k` on this block is one.

**Theorem (exact modulo p³, all p=6n+1>=7).** For every `0<=k<=N`,

```
a_k = b_k [1+p L_k+(p²/2)(L_k²-J_k)]    (mod p³), 0<=k<=K;
a_k = p b*_k [1+p L*_k]                  (mod p³), K<k<=N.
```

Set

```
S0 = sum_{k=0}^K (6k+1)b_k
S1 = sum_{k=0}^K (6k+1)b_k L_k
     + sum_{k=K+1}^N (6k+1)b*_k
S2 = (1/2)sum_{k=0}^K (6k+1)b_k(L_k²-J_k)
     + sum_{k=K+1}^N (6k+1)b*_k L*_k.
```

Then the **unmodified ORIGINAL 216 half sum** has the exact observer-preserving jet

`W_half = S0 + p S1 + p² S2 (mod p³)`.

### Proof

The three exact rational identities are

`1/2=-N+p/2`, `1/3=-K+p/3`, `2/3=-Q+2p/3`.

For `k<=K` every integer factor of the three base rising factorials is a p-unit. Dividing each shifted factor by its unshifted value gives a product of `1+p u_i`, with the three explicitly listed types of `u_i`. The elementary product expansion through degree two is

`prod_i(1+p u_i) = 1+p sum_i u_i + (p²/2)[(sum_i u_i)^2-sum_i u_i²] (mod p³)`.

For `K<k<=N` the `(-K+p/3)_k` factor at index `j=K` is **exactly** `p/3`; all other base factors are p-units because `N< p`, `Q<p`, and `k<=N<Q`. Remove that one factor, leaving `b*_k`, then expand the remaining units through degree one. Multiplication by `p` makes higher orders vanish modulo `p³`. Multiplying by the unchanged weights `6k+1` and summing yields the three displayed sums. QED.

### Direct bridge to the live LIFT residue

Consume the previously proved original high-shell theorem `W_full-W_half=p² T_A(p) (mod p³)`, where the signed, indexed original-shell `T_A` is retained from `20261105_onhour_d25_weighted_shell_literature_reduction.md` and the reversed 4F3 series. Then:

`W_full-p = [S0+p S1-p] + p²[S2+T_A(p)] (mod p³)`.

Under the already-established first-digit condition `W_half=p (mod p²)`, let

`D0=((S0+p S1-p)/p²) mod p`.

The exact unresolved third-digit condition becomes

`D0+S2+T_A(p)=0 (mod p)`.

It has three separate signed carriers: the first two parametric jets, the **quadratic/joint** jet on the unit block plus the first jet on the single-zero block, and the original upper-shell boundary. In particular, the zero factor at `k=K` forces the two different Taylor orders and is preserved under this reduction.

This is a finite exact representation of the live residual, not a claim of the all-prime cancellation. The accepted first-digit lemma is used only to justify the division in `D0`. No ordinary Hesse term, native Frobenius or `kappa` is identified with these arithmetic carriers.

## Independent computation on ORIGINAL terms

Executed Python standard-library checker `d25_half_sum_three_jet_checker_20261105.py` computes `S0,S1,S2` by modular factorial/rising-factor recurrences and independently recomputes `W_half,W_full` from the **original integer binomial coefficients**. All 80 primes `7<=p<=997, p=1 mod6` passed the `p³` jet equality and the exact original upper-shell divisibility; failures: 0. The p³ LIFT cancellation was checked on all 80, as finite evidence, not as an all-prime proof.

| p | D0 | S2 mod p | Original T_A mod p | signed sum mod p |
|--:|--:|--:|--:|--:|
| 7 | 5 | 4 | 5 | 0 |
| 13 | 3 | 0 | 10 | 0 |
| 19 | 11 | 18 | 9 | 0 |
| 139 | 122 | 4 | 13 | 0 |
| 373 | 240 | 240 | 266 | 0 |

At 373 the recorded integer identity is `240+240+266=746=2*373`. At 13 it is `3+0+10=13`. These are original-index and original-weight certificates.

## Next exact scientific action / ownership

Try an actual finite terminating creative-telescoping or hypergeometric transformation *on the centered polynomial with its first and second parameter derivatives* that proves `D0+S2=-T_A`. This targets the complete third digit directly. The original fixed p373 native divided-power H0/B0, `[X]U mod139129`, rank, semilinear F and eta, signed odd observer, native kappa/Delta-R plus independent replication remain **NOT_RUN / PENDING_OWNER** in existing issue #1559; this author-side arithmetic is not substituted for them.

Source continuation receipt `onhour11-20261105-0358-current-cont` is SUCCEEDED with `execution_authorized=false`; prior service session `MCP-491afa3ba2b94ec9b900ed3df6e345a3` had a registered activity, but no native CLAIM/open/run/checkpoint. Do not resurrect or borrow the maintenance conversation.