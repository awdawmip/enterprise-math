# X6 layer relation birthday and fast multipoint frontier

Status: `RESEARCH NOTE / EXACT RELATION SEMANTICS + FINITE EXPERIMENTS / NOT FOUNDATION / NO FACTORING BREAKTHROUGH CLAIM`
Date: `2026-09-06`
Project: `Enterprise Math / 进取数论`

## Provenance

This project-native note repairs two Enterprise Math progress events that were captured in the account-level GLOBAL_KNOWLEDGE journal but were not yet represented in the project repository:

- `20260906T120200+0800-x6-layer-relation-birthday-multipoint`
- `20260906T120500+0800-x6-relation-fast-multipoint-prototype`

Source journal paths:

- `journal/enterprise-math/2026-09-06/20260906T120200+0800-x6-layer-relation-birthday-multipoint.md`
- `journal/enterprise-math/2026-09-06/20260906T120500+0800-x6-relation-fast-multipoint-prototype.md`

Source GLOBAL_KNOWLEDGE snapshot used for reconciliation: `fd4ad4ae07d5343a35e58403456d6f6c801da25c`.

## 1. Static scalar layer scheduling is insufficient

For the cyclic Frobenius layer

`P_{N,r}(X)=(1+X)^N mod (X^r-1,N)=sum_i c_i X^i`,

cheap pre-query scalar observers of `N` did not reliably predict whether a width `r` would separate the hidden CRT branches of a balanced semiprime `N=pq`.

An exact finite observer-fiber witness was found at `r=127`: two semiprimes can share the tested tuple built from `N mod r`, `N mod (r-1)`, X6 shell/scalar data and several small-base modular powers, while one instance is factor-separating and the other is not. Thus these static scalar summaries erase the hidden prime-branch provenance needed to decide width success.

This agrees with the later exact adaptive-width barrier recorded in the multiresolution note: `N mod r` retains only a quadratic-character class of the hidden relative Frobenius orientation, not the orientation itself.

## 2. Upgrade from zero support to coefficient relations

The stronger observer does not ask only whether some coefficient `c_i` is zero modulo exactly one hidden prime factor. It asks whether two retained Cell coefficients satisfy a relation modulo exactly one CRT branch.

For equality,

`c_i = c_j (mod p)` but `c_i != c_j (mod q)`

implies

`gcd(N,c_i-c_j)=p`,

and symmetrically for `q`.

Finite tests at `r=127` showed that all-pair coefficient relations are much denser factor witnesses than coefficient zero support. This is naturally explained by a birthday scale: with about `r` coefficient samples modulo a hidden factor `p`, there are order `r^2` pair relations, so constant collision probability appears around

`r^2/p = Theta(1)`,

hence

`r = Theta(sqrt(p)) = Theta(N^(1/4))`

for balanced semiprimes.

This scale is important but not itself new factoring complexity: Pollard rho already exploits the same `sqrt(p)` birthday scale.

## 3. Exact reflection quotient

Binomial symmetry induces the exact cyclic involution

`c_i = c_{N-i mod r}`.

For odd prime `r`, the indices split into one fixed orbit and `(r-1)/2` two-element orbits. These mandatory equalities occur in both CRT branches and therefore cannot distinguish a factor.

Quotienting by this *known* reflection fiber is operation-safe for the declared relation observer: retain one representative per reflection orbit together with its orbit provenance. The reduced coefficient population has

`m=(r+1)/2`

Cells.

The quotient removes deterministic common collisions before searching for branch-specific collisions.

## 4. Scaled relation channels

For fixed nonzero integer `lambda`, use the relation

`c_i = lambda c_j (mod s)`

inside a hidden CRT branch `s|N`.

Let

`F(Y)=product_j (Y-c_j)`.

For `lambda>=2`, define

`F_lambda(Y)=product_j(Y-lambda c_j)=lambda^m F(Y/lambda)`.

Then for a retained Cell `i`,

`F_lambda(c_i)=product_j(c_i-lambda c_j)`.

For `lambda=1`, use

`F'(c_i)=product_{j!=i}(c_i-c_j)`

to remove the trivial self relation.

A proper gcd

`1 < gcd(N,F_lambda(c_i)) < N`

is an exact factor witness by CRT: the row product vanishes modulo exactly one hidden branch.

Finite direct `N`-only experiments with several fixed `lambda` channels achieved high hit rates around widths proportional to `N^(1/4)`. However generic distinct multiplier sets performed similarly or sometimes better than `{1,2,3,4,5,6}`. Therefore no intrinsic six-axis advantage of the multiplier count is established.

Freeze:

`RELATION_CHANNEL_COUNT_6 != NATIVE_X6_OPTIMALITY_THEOREM`.

## 5. Preserve the Cell row, collapse only the partner population

A global discriminant can accidentally multiply a `p`-collision from one Cell with a `q`-collision from another and return `gcd=N`. The safer BRC port retains the row label `i` and relation label `lambda`, while aggregating only over partner `j`:

`g_i^(lambda)=product_j(c_i-lambda c_j)`

(or `F'(c_i)` at `lambda=1`).

BRC typing:

- population: reflection-quotient Cell labels `i`;
- hidden branch identity: CRT factor branch `p` versus `q`;
- retained port: `(i,lambda)`;
- collapsed fiber: partner label `j` inside that fixed row;
- declared next operation: one `gcd(N,g_i^(lambda))`.

This quotient is safe for that declared one-gcd observer. It is not a complete state for arbitrary future partner localization; a later localization request must retain or reconstruct the relevant product-tree provenance.

## 6. Fast multipoint realization is exact

The apparent `O(m^2)` pair population does not have to be explicitly materialized.

An executable prototype implemented:

1. a monic subproduct tree for the points `c_i`;
2. exact modular polynomial multiplication with a chunk-split FFT path, cross-checked against naive exact modular multiplication;
3. fast monic polynomial remainders using reversal and Newton series inversion;
4. a remainder-tree multipoint evaluator;
5. evaluation of `F'(c_i)` and every `F_lambda(c_i)` followed by gcd extraction.

Because every divisor polynomial in the subproduct tree is monic, the reversed constant term is `1`; the Newton inverse does not require inversion of an unknown possibly nonunit element of `Z/NZ`.

The multipoint implementation reproduced the factorability outcomes of the explicit row-product implementation on semiprime tests. Thus the relation semantics admit a standard fast-polynomial realization without enumerating all pair differences.

## 7. Engineering and classical boundary

The proof-of-concept Python implementation did not beat simpler code at moderate sizes. Around `r~1009`, tree construction/reversed-inverse precomputation/multipoint overhead dominated the naive pair loop. On larger finite semiprime tests the X6/Frobenius layer prototype remained hundreds of times slower than a Brent-Pollard-rho implementation in the same Python session.

The correct classical boundary is therefore:

- Pollard rho: birthday collision, expected `O(sqrt(p))=O(N^(1/4))` steps for a balanced semiprime;
- Pollard-Strassen and successors: fast polynomial/multipoint factorization machinery already reaches deterministic `N^(1/4+o(1))` and better exponents in later work;
- current Enterprise relation cloud: a deterministic structured birthday cloud with exact BRC/provenance typing, but no proved complexity or wall-clock advantage.

No algorithmic speedup is claimed.

## 8. Durable frontier

Retain the following as reusable research content:

`FROBENIUS_LAYER_COEFFICIENTS`
`-> SAFE_REFLECTION_QUOTIENT`
`-> CELL-LABELED_RELATION_ROWS (i,lambda)`
`-> FAST_SUBPRODUCT/REMAINDER-TREE_MULTIPOINT_EVALUATION`
`-> gcd CRT branch witness`.

The result is useful as an exact relation-observer interface and as a BRC example of preserving the observer-critical Cell label while safely batching a partner fiber.

Do not promote it as a new general-purpose factorization class unless a future theorem proves a stronger coefficient-distribution property or an implementation establishes a genuine Pareto advantage over classical collision factorization.

This note is a persistence repair: the source events remain immutable account-level journal provenance, while this file is the required Enterprise Math project-repository durable representation.
