# RSA-270 second-layer BRC factor search

Progress-Event-ID: `rsa270-second-layer-brc-search-5b8c41`
At: `2026-09-06T07:40+08:00`
Scope: `enterprise-math / RSA-270 / semiprime BRC tree`
Source: `ChatGPT project conversation; current enterprise-math main a72226e; N-only exact-integer experiments`
Kind: `NEGATIVE`

## Event

Continued the prior RSA-270 64-branch square-shell audit by adding the proposed second-layer square-difference observer. RSA-270 was treated as N-only throughout; no unknown factor information was assumed. Public status checked in-turn still lists RSA-270 as unfactored.

Core branch law used:

`A_k=4*k*N`, `x0=ceil(sqrt(A_k))`, `d_{k,j}=(x0+j)^2-A_k`.

A branch endpoint factors only when `d_{k,j}=y^2`, since `(x-y)(x+y)=4*k*N`. More generally every branch satisfies `x_i^2 == d_i (mod N)`, so any set of branches whose `d_i` product is a square yields a congruence of squares and a gcd factor test. This is the correct valuation-parity/recoalescence extension of the tree; mathematically it overlaps the classical congruence-of-squares / quadratic-sieve principle and is not a novelty claim.

Exact search results:

1. Direct `j=0` scan was extended through `k=10,000,000`; no `d_{k,0}` was an exact square. On `2,000,001 <= k <= 10,000,000`, the lowest shell ratio observed was about `2.232133913565956e-7` at `k=8,219,381` (`d` 439 bits). The best second-layer normalized square defect on that interval was about `2.2905974750828442e-8` at `k=5,363,375`; its absolute nearest-square error was still 205 bits and `gcd(x-y,N)=gcd(x+y,N)=gcd(error,N)=1`.
2. Among `k<=2,000,000`, a particularly deep shell appeared at `k=171,177`, `rho~=3.315651077982316e-7`, with `d` only 437 bits. The prior `k=20` shell had `rho~=0.0148576573` and a 446-bit `d`, so multiplier expansion can shave roughly 9-11 residue bits in favorable branches, but not enough to make the residues small in an RSA-270 sense.
3. A targeted second-layer scan over 37 selected multiplier branches (prior low branches, lowest-shell branches, and lowest initial second-layer-defect branches), `0<=j<=100,000`, found no exact square endpoint. The best normalized defect was about `3.802970104147986e-8` at `(k,j)=(1,965,050,84,078)`; direct gcd tests were trivial. For deep-shell branches the shell advantage vanishes immediately as `j` grows because `d_{k,j}=d_{k,0}+2*x0*j+j^2`; e.g. high-smoothness candidates on the `k=171,177` line had residues around 477 bits versus the 437-bit `j=0` residue.
4. In the 1,000 lowest-shell `j=0` branches for `k<=2,000,000`, 346 pairwise products `d_i*d_j` were exact squares. Every such recoalescence was trivial: the pair multipliers had the same squarefree multiplier kernel (square-scaling class), and the resulting gcds were `1` and `N`. Therefore the BRC observer must retain multiplier square-class/provenance and reject these scalar-duplicate cycles before calling a parity collision factor-bearing.
5. After collapsing the 1,000 low-shell set by squarefree multiplier kernel, 828 distinct classes remained. Stripping all prime factors `<=10^6` left no fully smooth relation; the best remaining cofactor was 366 bits, and there were no shared residual factors across distinct multiplier square classes.
6. A separate smoothness-directed search over `k<=2,000,000` used small-prime valuation score rather than shell depth. Among 1,500 retained candidates, exact stripping through `10^6` improved the best residual to 348 bits (at `k=1,623,461`). Merging these with the low-shell population gave 2,315 nodes; after removing factors `<=10^6`, pairwise gcd audit found no shared residual factor across distinct multiplier square classes. Thus this finite population has no one-large-prime/two-branch cycle above the `10^6` factor base.
7. A classical Pollard p-1 stage-1 miracle check through `B1=10^6` returned gcd 1.
8. To test whether the enriched second-layer tree could statistically predict the unknown factor ratio before exact factorization, two independent batches totaling 600 synthetic 895-bit semiprimes near the RSA-270 scale were generated with known factor ratios in roughly `[1,2]`. Using the 64 `j=0` second-layer square-defect coordinates, leave-one-out kNN did not beat the median baseline after replication/combination: baseline MAE about `0.24119`; kNN MAE about `0.25556` (k=5), `0.24897` (k=10), `0.24512` (k=20), `0.24315` (k=30). RSA-270's 20 nearest synthetic second-layer neighbors had factor ratios spread roughly `1.1504..1.9875`, so no defensible factor-ratio estimate was obtained.

BRC/tool reuse resolution: `T0_BRC -> REUSE_APPLIED` with branch identity, future-operation and valuation-parity provenance retained. `domain.prime_toolkit` was checked; its large-integer factor witness baseline explicitly is not safe for large factorization, so no claim of executing an adequate existing RSA-270 factorizer is made. The second-layer valuation relation is an extension/application of BRC observation, not a new top-level family.

Interpretation: the second layer is mathematically meaningful, but demanding one branch to hit a square is still a generalized Fermat/Lehman-style endpoint search and has vanishingly small hit probability at this scale. The stronger multi-branch valuation-parity form is the right continuation, but a competitive RSA-270 attack needs a relation generator producing much smaller/smoother norms (quadratic-sieve/MPQS/GNFS-class polynomial selection or a genuinely stronger Enterprise construction), not merely a larger raw `j` window.

## Artifacts

No source-repository mutation. Conversation-local Python exact-integer experiment only. Global knowledge prior checkpoint: `journal/enterprise-math/2026-09-05/20260905T211800+0800-rsa270-semiprime-tree-neighbor-audit-7f31c2.md`.

## Next

Build a BRC-typed smooth-relation engine whose branch state is `(polynomial/multiplier provenance, residue, exact small-prime valuation parity, large-prime endpoints)`; explicitly quotient square-scaling trivial cycles; benchmark relation yield and norm size first on factorable RSA challenge numbers, then only apply to RSA-270 if the method materially beats ordinary multiplier-QS baselines. The key unresolved unit is norm reduction: current best finite search still leaves 348-366 bit residual cofactors after a `10^6` factor base, far from a usable relation matrix.