# R005-B — Prime–Collapse Field Geometry: first exact results

Status: `PROVED WIP / DRAFT OWNER RECORD / NOT CANONICAL`  
Date: `2026-08-10`  
Base: `main@9cac1e34020becca7c07ec73166a157dc2195a53`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`

## 1. Dimension separation

Three meanings of “dimension” must remain distinct.

1. **Power/collapse exponent dimension.** For a primitive nontrivial collapse exponent `p>=2`, the p-power basin is
   `I_{p,k}={n in N : k^p<n<(k+1)^p}`.
2. **Ambient geometric dimension.** A discrete space such as `Z^d`, `A_d`, HCP or Barlow carries adjacency/metric structure. It does not acquire an intrinsic primality predicate merely from dimension.
3. **Multiplicative factor dimension.** For `r>=2`, let
   `S_r(n)={(a_1,...,a_r): a_i>1 and product a_i=n}`.
   This is relation/correspondence data and is not the same object as ambient dimension or collapse exponent.

No theorem below identifies these three notions.

## 2. Universal factor-screen horizon

Define

`F_p(k)=isqrt((k+1)^p-1)`.

This is the **universal square-root screening horizon** for the whole basin: every composite `n` in `I_{p,k}` has a nontrivial factor at most `isqrt(n)<=F_p(k)`.

It is not automatically the basin-specific smallest required horizon. For example, in the square basin `16<n<25`, `F_2(4)=4`, but every composite has least prime factor at most 3. Thus the actual composite population can permit a smaller bound.

## 3. T-B1 — square self-alignment uniqueness

### Theorem B1.1 — parity law

Let `x=k+1`.

- If `p=2m`, then
  `F_{2m}(k)=x^m-1=(k+1)^m-1`.
- If `p` is odd, then
  `F_p(k)=isqrt(x^p)-1_{x is a square}`.

For the even case, `(x^m-1)^2 <= x^(2m)-1 < (x^m)^2`, giving the exact integer square root. For odd `p`, `x^p` is a square exactly when `x` is a square; subtracting one changes the floor square root only in that perfect-square case.

### Corollary B1.2 — unique coordinate self-alignment

For every `k>=0`,

`F_2(k)=k`.

For every `p>2` and `k>=1`,

`F_p(k)>k`.

Hence `p=2` is the unique primitive nontrivial exponent whose universal factor-screen horizon equals the p-basin coordinate for every basin.

For even powers define the shifted horizon map

`E_m(x)=F_{2m}(x-1)+1=x^m`.

Then `E_a o E_b=E_{ab}` and the square case `m=1` is the identity element. The power-map composition itself is elementary mathematics; the Enterprise-specific content is its role as the exact factor-horizon map.

## 4. T-B2 — exact p-power basin prime count

Let

- `A=k^p`,
- `U=(k+1)^p-1`,
- `F=F_p(k)`,
- `Q_F=product_{prime ell<=F} ell`,
- `H_{p,d}(k)=floor(U/d)-floor(A/d)`.

Then the exact finite inclusion–exclusion identity is

`P_p(k)=sum_{d|Q_F} mu(d) H_{p,d}(k) + #{q prime : A<q<=F}`.

For every `k>=2`, `F<A`, so the correction vanishes:

`P_p(k)=sum_{d|Q_F} mu(d) H_{p,d}(k)`.

Reason: after sieving by every prime `<=F`, every composite in the basin is removed. The only removed basin elements that must be restored are primes that themselves lie at or below `F`.

This formula is exact but the naive divisor enumeration is exponential in `pi(F)`; it is a correctness/exploration identity, not an efficient prime-counting algorithm.

## 5. T-B3 — finite local carry state

Let the number of interior integers be

`L_p(k)=(k+1)^p-k^p-1`.

Write

- `r=k^p mod d`,
- `s=L_p(k) mod d`.

Then

`H_{p,d}(k)=floor(L_p(k)/d)+epsilon_{p,d}(k)`,

where

`epsilon_{p,d}(k)=1_{r+s>=d}`.

Thus, relative to the full-width baseline, the remaining boundary carry is always one bit for every exponent `p`.

This refutes the naive possibility that higher `p` intrinsically requires an unbounded carry state.

A second decomposition preserves the polynomial degree structure. Since

`L_p(k)=sum_{j=1}^{p-1} binom(p,j) k^j`,

define

`B_{p,d}(k)=sum_{j=1}^{p-1} binom(p,j) floor(k^j/d)`.

Then

`H_{p,d}(k)=B_{p,d}(k)+chi_{p,d}(k)`,

where `chi_{p,d}(k)` depends only on `k mod d` and satisfies

`0 <= chi_{p,d}(k) <= 2^p-2`.

At `p=2`, this `chi` is exactly the existing square carry in `legendre.py`.

This proves residue sufficiency and a fixed-p finite bound. **Minimality of the residue state is not yet proved**; a coarser quotient may exist for particular `(p,d)` families.

## 6. T-B4 — Möbius carry decomposition and the sharper square-specialness theorem

Let

`Psi_F(N)=sum_{d|Q_F} mu(d) floor(N/d)`.

Equivalently, `Psi_F(N)` counts the integers `1<=m<=N` coprime to `Q_F`.

For `k>=2`, substituting the polynomial carry decomposition gives

`P_p(k)=sum_{j=1}^{p-1} binom(p,j) Psi_F(k^j) + sum_{d|Q_F} mu(d) chi_{p,d}(k)`.

Let `m=floor(p/2)`. For every `1<=j<=m`,

`k^j <= F_p(k)`.

Therefore every integer `2,...,k^j` has a prime factor at most `F`, so

`Psi_F(k^j)=1`.

Hence the factor horizon automatically collapses the low-degree part of the Möbius baseline to the constant

`C_p^low=sum_{j=1}^{floor(p/2)} binom(p,j)`.

### Corollary B4.1 — complete degree visibility is unique to p=2

For `p=2`, the basin-width polynomial has only degree `j=1`, and that degree lies inside the forced visibility range. Consequently the entire deterministic polynomial baseline collapses to

`P_2(k)=2 + sum_{d|Q_k} mu(d) chi_{2,d}(k)`.

For every `p>2`, `floor(p/2)<p-1`; therefore at least one polynomial degree lies outside the universally forced visibility range. Small basins may have accidental extra visibility, but complete all-basin forced visibility is unique to the square exponent.

This is a stronger structural explanation than `F_2(k)=k` alone:

**square collapse is simultaneously the exact coordinate self-alignment point and the unique exponent where factor visibility consumes every degree of the basin-width polynomial, leaving only a constant Möbius baseline plus local carry.**

## 7. Multiplicative factor dimension: exact negative boundary

For `n>=2`, define ordered nonunit support

`S_r(n)={(a_1,...,a_r): a_i>1, product a_i=n}`.

Then

`S_r(n) != empty  iff  Omega(n)>=r`,

where `Omega(n)` is the total number of prime factors counted with multiplicity.

Therefore

`max{r:S_r(n)!=empty}=Omega(n)`.

So a “factor dimension” defined only as maximal nonunit factor arity is exactly classical `Omega(n)` under another name. It is not a new invariant.

A potentially richer R005-B state must preserve more than support existence, for example witness multiplicity, ordered/unordered shape, divisor incidence, or the actual factorization hypergraph.

Prime characterization remains the classical relation rewrite

`n prime iff S_2(n)=empty`.

## 8. T-B7 — ambient geometry negative boundary

A bare unrooted nearest-neighbor lattice graph `Z^d` is vertex-transitive under translations. Any unary predicate intrinsic to the bare graph and invariant under all graph automorphisms must therefore be constant on vertices.

Hence a nontrivial “prime point” predicate cannot be intrinsic to the bare lattice graph alone.

Three enrichments must be distinguished:

1. coordinate-prime labels: externally imported arithmetic labels;
2. prime norm: requires an origin/norm or equivalent extra structure;
3. Gaussian/Eisenstein primality: requires an internal multiplicative/ring structure.

Thus the Foundation boundary is

`intrinsic geometry != intrinsic primality`

unless multiplication/divisibility or another arithmetic enrichment is supplied.

## 9. T-B5 — primality-safe quotient criterion

For a quotient/observation `q:N->Y`, primality descends to the quotient exactly when it is constant on every fiber:

`q(n)=q(m) => (prime(n) iff prime(m))`.

Equivalently, `ker(q)` must refine the kernel of the prime/composite label.

This is not a new Enterprise theorem; it is a direct specialization of the existing A2/P023 observation-kernel and future-safe quotient machinery.

Small collision: 5 and 6 share the same square-root basin coordinate (`R_2=2`) but have different primality labels. Therefore the root/basin coordinate by itself is not primality-safe.

## 10. R005-A bridge — test witness versus factor witness

R005-A and R005-B should be joined at the observation/certificate layer, not by identifying their objects.

- R005-A: an algorithm/test/certificate language partitions integers by test witnesses and can have pseudoprime mixed fibers.
- R005-B: a collapse/factor language partitions integers by collapse observables and factor witnesses and can have prime/composite mixed fibers.
- A nontrivial factor tuple is a direct compositeness witness.
- A mixed fiber in either language is information loss relative to the primality label.

Bridge proposal:

`test witness fiber <-> factor witness fiber`

with A2/P023 providing the generic criterion for when an observation language is sufficiently refined to preserve the required prime/composite output.

The bridge becomes genuinely useful if one can prove that a bounded test witness language and a bounded factor/carry language induce the same repaired fibers on a declared domain. That equivalence is not yet proved.

## 11. Ownership map

- **A0:** p-power basins, roots/collapse coordinates and scale behavior; `F_p(k)` is a derived arithmetic observable over this layer.
- **A2 / P023:** primality-safe quotient/fiber criterion and any minimal repair of a coarse collapse signature.
- **A4:** factor-support tuples/hypergraphs are multivalued witness/correspondence data; do not collapse them into one deterministic kernel without a reduction theorem.
- **A5 / P012 / P022:** ambient discrete geometry and the negative boundary that bare geometry alone does not define primality.
- **P017:** consumes the `p=2` specialization as part of the Legendre pressure test; the current numbered status remains `OPEN / ACTIVE RESEARCH` and none of these results proves Legendre's conjecture.
- **P018:** centered-prime-radius / factor-proof-slack results remain a square/near-diagonal comparator and are not generalized here without their stated hypotheses.
- **P018/P023 power-free action basis:** relevant as prior canonical machinery for deciding which observations separate exact states; R005-B should consume rather than duplicate it.
- **R005-B owner surface:** `src/enterprise_math/prime_collapse_field.py`, `tests/test_prime_collapse_field.py`, and the exact finite atlas experiment.

## 12. Prior-art boundary

The following are established mathematics and must not be presented as R005-B inventions:

- Möbius inversion and inclusion–exclusion;
- least-factor primality screening by the square root;
- primes in short intervals / between consecutive powers;
- Gaussian and Eisenstein primes and splitting/irreducibility in their rings;
- factorization theory of atoms/monoids, including factorization-length invariants;
- `omega(n)`, `Omega(n)`, almost-prime stratification;
- generic quotient/fiber factorization criteria.

Representative sources checked for this pass:

1. R. C. Baker, G. Harman, J. Pintz, *The Difference Between Consecutive Primes, II*, Proc. LMS 83 (2001), 532–562, DOI `10.1112/plms/83.3.532`.
2. M. Cully-Hugill, *Primes between consecutive powers*, arXiv:`2107.14468`.
3. A. Dudek, *An Explicit Result for Primes Between Cubes*, arXiv:`1401.4233`.
4. A. Geroldinger, Q. Zhong, *Factorization Theory in Commutative Monoids*, arXiv:`1907.09869`.
5. B. Huang, J. Liu, Z. Rudnick, *Gaussian primes in almost all narrow sectors*, arXiv:`1903.04005`.
6. M. Pandey, *On Eisenstein primes*, arXiv:`1607.00469`.

Analytic prime-distribution results answer a different question from the exact finite factor-horizon/carry identities here. In particular the square case must not be advertised as solved by these finite decompositions.

## 13. Foundation Feedback candidates

### FF-B1 — factor-horizon visibility layering law

Candidate type: `reusable_tool + layering_law`.

Payload: a p-power basin has an exact universal factor horizon `F_p(k)`; that horizon forces Möbius visibility of every width-polynomial degree up to `floor(p/2)`, and `p=2` is the unique exponent with complete forced degree visibility.

Initial routing: `APPLICATION_LOCAL_OR_NOT_READY` until prior-art novelty of this exact packaging and its reuse outside R005 is checked.

### FF-B2 — bare-geometry primality boundary

Candidate type: `negative_boundary`.

Payload: vertex-transitive bare lattice geometry cannot carry a nonconstant intrinsic unary prime predicate; arithmetic enrichment is required.

Initial routing: likely A5-facing boundary, but canonical promotion should wait for owner/steward review.

### FF-B3 — factor-dimension collapse to Omega

Candidate type: `negative_boundary`.

Payload: maximal nonunit factor arity equals classical `Omega(n)`. Any claimed new factor dimension must preserve richer witness data.

## 14. Executable verification

`src/enterprise_math/prime_collapse_field.py` implements exact integer primitives for:

- factor horizon;
- one-bit width carry;
- polynomial carry and p=2 compatibility;
- forced visibility degree;
- direct and exact Möbius p-basin prime counts for bounded experiments.

`tests/test_prime_collapse_field.py` exhaustively regresses the identities over bounded integer grids and checks exact direct-vs-Möbius prime counts on small basins.

`experiments/r005b_prime_collapse_atlas.py` emits an exact JSON atlas for `p=2..8` and configurable small `k`. Its displayed carry spectrum is exact through an explicit modulus cutoff; the cutoff is an exploration window, not a truth approximation.

No floating-point value is used as a truth source.

## 15. Answer to the two motivating questions

### Is this merely “drawing primes in basins”?

No. There is an exact arithmetic coupling: the universal least-factor screening horizon of a p-power basin is itself a collapse-derived integer observable, with a closed parity law. The square exponent is uniquely self-aligned (`F_2(k)=k`) and uniquely forces visibility of every degree in the basin-width polynomial, producing the complete `constant + Möbius carry` decomposition.

For `p>2`, the factor horizon and basin coordinate separate. This is a provable mismatch regime, not merely a different picture of the same prime labels.

### Is there already one common prime field across collapse, geometry and factor dimensions?

Not yet in a strict intrinsic sense.

A rigorous common **arithmetic** layer is plausible:

`collapse coordinate × factor horizon × factor-support/certificate state × prime label`.

The ambient geometry axis is different. Bare geometry contributes metric/adjacency organization but not intrinsic primality; it can join the prime field only after a declared arithmetic enrichment such as a norm, multiplication, divisibility relation, or ring structure.

Therefore the present evidence supports a two-level Enterprise Prime Toolkit:

1. an intrinsic arithmetic prime field combining collapse/screening/carry/factor witnesses;
2. optional enriched geometric realizations consuming that arithmetic field.

Promoting all three “dimensions” into one undifferentiated primitive would currently be mathematically unjustified.
