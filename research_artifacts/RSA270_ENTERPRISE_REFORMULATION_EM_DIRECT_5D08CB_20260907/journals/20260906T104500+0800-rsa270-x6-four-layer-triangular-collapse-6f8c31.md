# RSA-270 X6 four-layer triangular collapse and local-modulus no-go

Progress-Event-ID: `20260906T104500+0800-rsa270-x6-four-layer-triangular-collapse-6f8c31`
At: `2026-09-06T10:45:00+08:00`
Scope: `enterprise-math / RSA-270 / X6 layer replacement for Fibonacci / BRC collapse`
Source: `current ChatGPT TASK research; exact integer derivation; bounded Python checks; current project/global repositories; classical Legendre/Jacobi representation identities`
Kind: `PROGRESS`

## Event

Continued the user's explicit instruction to avoid large-compute search and try multi-layer collapse on RSA-270.

1. Safe modular Fermat endpoint filtering was organized as sequential BRC support collapse. On a 16-branch priority set with `j=0..65535` (1,048,576 `(k,j)` states), exact quadratic-residue necessary-condition layers reduced survivors monotonically to zero by modulus 79, proving no exact square-difference endpoint in that finite window without bulk big-integer square tests. This is standard modular Fermat/QR filtering and is not a new factor signal.

2. Naive nearest-X6-layer branching does not naturally recoalesce. Using native L1 balls `B_d(r)=sum_{j=0}^d 2^j C(d,j) C(r,j)`, branching at each step across `d=2..6` and lower/upper neighboring balls produced exactly 10, 100, 1000, 10000, 100000 distinct residual states through depths 1..5. At depth 4, 450,000 sibling-difference gcd tests against RSA-270 produced no nontrivial factor. A separate set of 245 N-dependent radii/ball/shell/residual coordinates and all pairwise differences also produced no nontrivial gcd. Therefore unproved state merging would erase future factor operations and is forbidden by the observer-preservation rule.

3. Dimension-descending L1 collapse `6->5->4->3->2->1` shrinks RSA-270 bit lengths `895->747->597->448->297->149->1`; the 448-bit residual is not a factor (`gcd=1`). Calibration on 128 generated 895-bit semiprimes showed the factor-scale residual is mainly degree/scale telescoping, not a stable factor signature.

4. A factor-complete X6 L2 shell observer was identified. For a four-axis native coordinate fiber,

`R4(N)=#{z in Z^4: z1^2+z2^2+z3^2+z4^2=N}`.

For odd N, Jacobi gives `R4(N)=8 sigma(N)`. Hence for a distinct odd semiprime `N=pq`,

`R4(N)=8(1+p+q+N)`,

so `S=p+q=R4(N)/8-N-1` and the factors are recovered from `x^2-Sx+N=0`. This is an exact reduction, not yet a fast algorithm; computing exact `R4(N)` is factoring-equivalent on semiprimes.

For RSA-270 specifically `N == 7 (mod 8)`, the one-, two- and three-square support strata vanish; therefore the first nonempty support stratum of the X6 squared shell is support size 4. Its global six-axis cardinality is `C(6,4) R4(N)=15 R4(N)`, making the minimal-support X6 shell stratum itself a factor-complete composite-indexed observer.

5. The user's original “replace Fibonacci by Enterprise layer counts” idea admits an exact four-layer formulation using the 2D native L1 ball:

`B2(r)=2r^2+2r+1=4 T_r+1`, where `T_r=r(r+1)/2`.

Legendre's four-triangular-number theorem says `t4(m)=sigma(2m+1)`. Therefore, for every odd N,

`C_X(N)=#{(a,b,c,d)>=0: B2(a)+B2(b)+B2(c)+B2(d)=2N+2}=sigma(N)`.

For RSA semiprime `N=pq`, `C_X(N)=N+1+p+q`; the exact four-layer branch total directly determines the factors.

Moreover the divisor-sum Lambert expansion gives the exact two-layer recoalescence law

`sum_m t4(m) q^m = sum_{a,b>=0} (2a+1) q^(2ab+a+b)`.

At target `m=(N-1)/2`, surviving collapsed endpoints satisfy

`2ab+a+b=(N-1)/2 <=> (2a+1)(2b+1)=N`.

Thus the four Enterprise-layer branch tree is mathematically known to collapse to weighted factor-pair branches. The unresolved algorithmic issue is to execute this recoalescence without first enumerating the four-layer tree or already solving the factor equation.

6. Exact local-modulus no-go for the four-layer model: for odd prime `ell` not dividing N, since `2 B2(r)-1=(2r+1)^2`, the pair-sum support modulo ell is already all of `F_ell`. More strongly, direct finite-field counting gives

`#{a,b,c,d mod ell: sum B2(ai)=2N+2 mod ell} = ell(ell^2-1)`

for every `ell` not dividing N, independent of N. For prime powers the nonsingular Hensel lift similarly depends only on the modulus while the target is a unit; CRT extends this to any odd modulus coprime to N. Hence repeated fixed/local modular multiplicity collapse cannot reveal RSA factors: it becomes N-independent unless the chosen modulus already shares a factor with N, in which case gcd has already solved the problem. The factor information is therefore global integer-boundary/provenance data, not local modular support/mass.

7. A current parallel project frontier supplied a compressed cyclic Frobenius path-field observer `D_{N,r,c}(X)` in `(Z/NZ)[X]/(X^r-1)`. A low-budget RSA-270 check used three masks (two-term, six-term geometric, six-mark Golomb) for 60 instances through `r=21`; no coefficient produced a nontrivial gcd. The run was deliberately stopped rather than scaling r into a large-compute search. This matches the existing finite observation that fixed-small-r hit rates decay with factor scale.

Status: RSA-270 is not factored. The strongest new positive result is the exact Enterprise-layer factor-complete observer and four-layer-to-factor-pair recoalescence identity; the strongest new negative result is that local modular collapse provably erases the N-dependent information needed for that observer.

## Artifacts

- Global prior checkpoint: `journal/enterprise-math/2026-09-05/20260905T211800+0800-rsa270-semiprime-tree-neighbor-audit-7f31c2.md`.
- Parallel current frontier: `journal/enterprise-math/2026-09-06/20260906T103843+0800-x6-layer-gcd-lucas-frobenius-frontier.md` at global main `d759890879f7bdbb55f4f09a83cb3311faef5939`.
- Current project source consulted through `awdawmip/enterprise-math@9c07be963f684b2c868acec0c6f48bd38b2ed3c5`, including centered X6 native foundation and joint-observer preservation rules.
- Classical identity status: Legendre/Jacobi formulas are prior art; no novelty claim is made for the representation identities themselves.

## Next

Do not return to broad `(k,j)` or large-r brute force. Treat the exact four-layer Enterprise-ball branch population as a Weighted/N-BRC object and search for an integer-boundary/provenance-preserving recoalescence operator whose output is the Lambert factor-pair state without enumerating `O(sqrt(N))` layer radii. In parallel, integrate the current multinomial-Lucas sublattice frontier: seek a structured global aggregation that retains hidden p/q sublattice distinction while avoiding fixed-small-modulus collapse. Any proposed compression must pass the observer/future-operation safety test and an equal-cost comparison with standard factorization baselines.