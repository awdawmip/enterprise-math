# R025 Precision-Exponent Phase Atlas

Researcher-ID: `EM-R025-1B6E63`  
Status: `FROZEN EMPIRICAL/DERIVED ATLAS / NOT CANONICAL`

## 1. Primary phase coordinates

The data are best organized by five exact coordinates rather than raw `(M,p)` alone:

1. root index `k=floorRoot_p(Mx)`;
2. rational basin phase `phi=d/G`;
3. refinement-root scale `c=r^(1/p)` used only as a symbolic real boundary variable, not theorem arithmetic;
4. p-th-power alignment predicate `r=a^p`;
5. exponent sparse-phase predicate `Mx<2^p`.

These coordinates expose three distinct phase systems.

---

## 2. Precision sawtooth phase

For fixed physical rational x and exact integral coordinate `n=Mx`, the root-index phase is

`k^p <= Mx < (k+1)^p`.

Within one k-phase:

`W_p(M,x)=((k+1)^p-k^p)/M`,

so `W` is exactly proportional to `1/M`.

At the phase boundary `Mx=(k+1)^p`, k increments and the numerator jumps. Therefore the exact precision law is a descending sawtooth. Its large-scale envelope obeys

`W ~ p*x^((p-1)/p)*M^(-1/p)`.

### Practical precision multipliers

Across enough phases:

| p | ×2 precision envelope factor | ×10 precision envelope factor |
|---:|---:|---:|
| 2 | `2^-1/2 ≈ 0.7071` | `10^-1/2 ≈ 0.3162` |
| 3 | `≈0.7937` | `≈0.4642` |
| 4 | `≈0.8409` | `≈0.5623` |
| 8 | `≈0.9170` | `≈0.7499` |
| 16 | `≈0.9576` | `≈0.8660` |
| 32 | `≈0.9786` | `≈0.9306` |

These are envelope display values, not substitutes for the exact plateau law.

High p therefore creates long precision plateaus: to move from root k to k+1 requires crossing an `M` threshold proportional to `(k+1)^p/x`.

---

## 3. Exponent root-index phase

For fixed coordinate n>1:

`k_p=1 <=> n<2^p`.

The entry exponent is exactly `bit_length(n)`.

Inside k=1:

- DOWN = 1;
- UP = `2^p`;
- spread = `2^p-1`;
- 50/50 mean = `(1+2^p)/2`;
- unbiased upper probability = `(n-1)/(2^p-1)`;
- unbiased variance = `(n-1)(2^p-n)`.

Thus high p simultaneously creates:

- exponentially wider endpoint spread;
- exponentially stronger 50/50 upward midpoint target for fixed small n;
- exponentially rarer upper events under the unbiased law;
- growing stochastic variance/sample complexity.

The phase boundary in `(M,p)` for fixed physical x is

`Mx = 2^p`, or `M = 2^p/x`.

---

## 4. Stochastic observability phase

For the exact fixed family `n0=1000,r=3,depth=16`, distance-weighted collapse remains a martingale with mean 1000 for every p tested. But the terminal distribution becomes increasingly rare-event dominated.

| p | terminal support | CV (display) | P(final < 1000) | N for 10% relative RMS |
|---:|---:|---:|---:|---:|
| 2 | 9749 | 0.0367 | 0.49865 | 1.34e-1 |
| 3 | 505 | 0.134 | 0.59559 | 1.79 |
| 4 | 250 | 0.480 | 0.58622 | 23.0 |
| 6 | 98 | 1.65 | 0.69860 | 2.72e2 |
| 8 | 45 | 7.75 | 0.92166 | 6.01e3 |
| 10 | 28 | 31.0 | 0.97925 | 9.62e4 |
| 12 | 24 | 262.7 | 0.99848 | 6.90e6 |
| 16 | 19 | 2.42e4 | 0.9999803 | 5.87e10 |
| 20 | 17 | 4.05e6 | 0.999999625 | 1.64e15 |
| 24 | 17 | 8.26e8 | 0.999999892 | 6.81e19 |
| 32 | 17 | 4.24e13 | 0.999999999984 | 1.80e29 |

The support can get **smaller** while Monte Carlo observability gets dramatically worse. Branch cardinality is therefore not a proxy for probabilistic sample complexity.

This is a major precision/exponent-policy separation:

- BRC support asks **which worlds remain possible**;
- unbiased probability asks **how mass is distributed over those worlds**;
- high p can yield a tiny support but extreme weight imbalance.

---

## 5. BRC refinement phase diagram

For constant p,r after the first positive p-power endpoint state, let `r` be classified by two exact predicates:

- `aligned(p,r)`: `r=a^p` for an integer a;
- compare `r` with `2^p`.

| Region | Condition | Root-index geometry | Branch cardinality | Recoalescence |
|---|---|---|---|---|
| Freeze island | `r=a^p` | `k -> ak` exact | constant after first collapse | no new branch |
| Funnel | `1<r<2^p` | interval maps to interval | `~r^(t/p)` scale, subbinary | structurally frequent |
| Boundary | `r=2^p` | aligned `k->2k` | frozen | interval contiguity can break but no branching |
| Binary sea | `r>2^p`, not pth power | parent child pairs disjoint | exact doubling | zero |

Important: aligned freeze islands also occur above the boundary, e.g. `p=2,r=9,16,25,...`.

### Fixed-r interpretation

For fixed r, increasing p raises `2^p`. Eventually `r<2^p`, forcing a nontrivial fixed r into the funnel phase. Thus exponent growth can **increase** BRC recoalescence even though p-th-power anchors are becoming sparser in coordinate space.

This distinguishes coordinate sparsity from branch-support collision geometry.

---

## 6. Policy phase map

| Policy | Local drift | Multi-layer structural type | High-p k=1 behavior |
|---|---|---|---|
| ALWAYS_DOWN | nonpositive | interior/reductive | collapses toward 1 on each ambiguous k=1 step |
| ALWAYS_UP | nonnegative | closure/extensive | jumps to `2^p` |
| NEAREST | phase-dependent | metric selector | after sufficiently high p relative to n, chooses 1 |
| FARTHEST | opposite local endpoint to NEAREST | metric selector | after sufficiently high p, chooses `2^p` |
| PRNG_50_50 | `G/2-d` expected drift | deterministic seed realization / biased law | midpoint expectation `~2^(p-1)` |
| STOCHASTIC_UNBIASED | zero conditional drift | martingale under identity tower | rare upper event probability `~(n-1)/2^p`; variance grows |
| ALTERNATING | forced sign schedule | feedback-sensitive | may create large oscillatory excursion |
| PHASE_THRESHOLD(alpha) | deterministic phase cut | antitone in alpha | breakpoints remain exact rational phases |
| ALL_ENDPOINTS | no weights | exact support semantics | controlled by refinement phase trichotomy |

---

## 7. Order-defect phase map

| Policy algebra | r=1, p|q | r=1, incomparable | refinement inserted |
|---|---|---|---|
| DOWN / interior | commutes/absorbs | can fail | comparable can fail |
| UP / closure | commutes/absorbs | can fail | comparable can fail |
| NEAREST | can already fail | can fail | can fail |
| FARTHEST | can already fail | can fail | can fail |

Therefore a single exponent divisibility label is insufficient once policy and precision lift are treated as part of the dynamics.

---

## 8. Negative boundaries that must be preserved

1. p-power covariance H4 is false.
2. p-power-free refinement kernel H6 is false.
3. nearest/farthest one-step complement is not a fixed multi-layer affine complement.
4. exact unbiasedness does not imply fast empirical convergence; high-p rare-event distributions can make naive seed averages misleading by many orders of magnitude.
5. root-index monotonicity in p does not imply monotonicity of gap/error/variance.
6. ALL_ENDPOINTS support cardinality does not determine probability-law difficulty; the Boolean BRC support layer and weighted stochastic layer must remain semantically distinct.
