# Trace collisions: safe inversion merge or a verified factor

Status: SYMBOLIC_CANDIDATE_AND_SOURCE_MATCH; shared-context research, NOT_ADMITTED. No scientific execution, host numerical experiment, external provider query, or remote write. The statements below apply over `Z/NZ`, including prime powers and zero divisors; they do not assume a field or supplied factorization.

## 1. Main result and its exact contract

For `N>1` and units `u,v`, define

`z(u)=u+u^(-1) mod N`.

**Trace-or-factor lemma.** Given certified units and `z(u)=z(v)`, a single exact observation

`d=gcd(u-v,N)`

has the following exhaustive meanings:

| Observed d | Certified consequence | Permitted action |
|---|---|---|
| `N` | `u=v mod N` | Merge identical states |
| `1` | `uv=1 mod N` | Merge inversion partners only for an inversion-compatible future |
| `1<d<N` | d is a proper divisor of N | Stop with a verified factor |

**Proof.** Multiplying the trace equality by the unit `uv` gives

`(u-v)(uv-1)=0 mod N`.                                      (1)

If `d=N`, the first factor vanishes. If `d=1`, the first factor is a unit and cancellation gives `uv=1`. All other gcd values are proper divisors. Thus if `u` is neither `v` nor `v^(-1)`, the gcd is necessarily proper. Conversely, a proper gcd does not imply the states were not inversion partners: an inversion pair can itself expose a factor. It is sound to stop in that case too.

No division by two, cancellation of an unproved unit, CRT computation, known order or factorization is used. The proof covers `N=2` and arbitrary even or odd composite N. For prime N the proper-divisor branch is empty.

This is stronger than demanding that the trace key be globally faithful: a key collision outside the allowed safe equivalence solves the declared search objective. It is not a theorem that all trace collisions are harmless for every observer.

## 2. The allowed future must be explicit

The equality `z(u)=z(u^(-1))` alone is insufficient for arbitrary named or asymmetric actions. For the declared symmetric step with unit `c`, the raw branches have ratios

`u, u, cu, c^(-1)u`

with weights `1/4` each. Inversion fixes the identity branches and exchanges the `+c` and `-c` branches. Also

`gcd(u^(-1)-1,N)=gcd(u-1,N)`.

Therefore inversion is an exact quotient for this kernel and the first-hit proper-factor observer, including its divisor value and stopping depth. More generally the two directions must have matching complete branch-weight histograms, not merely matching total mass. The two identity branches remain `2[1/4]`, not `[1/2]`.

The same argument works with a prescribed sequence of different symmetric unit multipliers. It does not license forgetting orientation if a later step requests only the named `+c` action or reads a particular raw endpoint/provenance label.

### Candidate native interface

Maintain `trace_key -> (one certified unit representative, complete branch-weight histogram, source bindings)`.

For an incoming certified unit `v`, compute its exact trace. If the key is new, retain `v`. On a repeated key, compare with the retained representative `u` using the single gcd in Section 1:

* SAME: recoalesce the histograms.
* INVERSE: recoalesce only under the declared inversion-compatible contract.
* FACTOR: return d with the native gcd/divisibility receipt and stop.

Before any factor-producing conflict, induction gives exactly the inversion-quotient instrument: each merged fiber contains only identical or inversion-equivalent states, and the representative generates the correct multiset of next quotient branches. A non-safe collision never enters the continuing state.

This proves **sound factor search with safe continuation before success**. Conflict-triggered factors may be found where the old instrument would still be live. Consequently the augmented algorithm need not preserve the old factor-output distribution or first-hit time after a conflict. It must report the new event kind, not claim unchanged sampling law. If exact reference-law preservation is required, keep the conflicting states separate instead.

The record must retain an actual representative. A trace integer alone does not provide the gcd input `u-v`, a modular lift, or an extraction procedure. Dictionary size, native inverse/trace cost, gcd calls and multiplicities are charged. There is no promise of a small number of keys or of encountering a useful conflict quickly.

## 3. Prime-power and zero-divisor boundaries

Equation (1) does not imply that one factor vanishes modulo N. That invalid implication would discard the factor-producing cases.

For a prime-power modulus `p^e`, let the truncated valuations of its two factors be alpha and beta. Their product vanishes when `alpha+beta>=e`; both can be strictly below e. Then the first gcd is `p^alpha`, proper whenever the collision is neither equality nor inversion. Over squarefree composite N, different prime components can instead choose different signs of the inversion pair. Both mechanisms are handled by the same gcd lemma; CRT is a proof description, not an algorithm input.

The factor observer itself does **not** generally descend to trace without repair:

`z(u)-2 = (u-1)^2/u mod N`,

so

`gcd(z(u)-2,N)=gcd((u-1)^2,N)`.                             (2)

At `p^e`, the two gcd exponents are respectively `min(e,2 alpha)` and `min(e,alpha)`. They agree for squarefree N, but squarefreeness is not assumed or freely supplied here. For the symbolic prime-power family `N=p^2`, `u=1+p`, one has `z(u)=2` while `gcd(u-1,N)=p`; the trace also equals that of the unit 1, whose difference gcd is N. This is a symbolic family, not a newly executed numeric fixture.

A proper gcd obtained from (2) is always a valid factor. Its value need not equal the original observer value; gcd N is saturation, not proof of no factor. Keeping the representative permits the original gcd observation, or the trace-or-factor test against representative 1. Likewise trace `-2` can be tested against `-1`. These are explicit repair operations, not a trace-only recovery theorem.

## 4. Two successor traces and spurious polynomial roots

Put `z=z(u)`, `k=z(c)` and define the two genuine successors

`t_plus=z(cu)`, `t_minus=z(c^(-1)u)`.

Direct multiplication yields, over the integer polynomial identities and hence every `Z/NZ`,

`t_plus+t_minus=kz`,

`t_plus*t_minus=z^2+k^2-4`.

Thus they are roots of

`X^2-kz X+(z^2+k^2-4)=0`.                                  (3)

The unordered pair of genuine roots is invariant under replacing u by its inverse, exactly as the symmetric kernel requires. However, the set of **all** roots of (3) need not be that pair. A composite ring can mix the two root choices across prime components; prime powers can admit additional roots through nilpotents. Listing all algebraic roots as native branches changes branch count, multiplicity and the reachable process.

**Root-or-factor repair.** If one genuine root `t_plus` is retained or generated with its native lift certificate, every root `x` of (3) satisfies

`(x-t_plus)(x-t_minus)=0 mod N`.

Exactly the Section 1 argument gives:

* gcd `N` of `x-t_plus` means `x=t_plus`;
* gcd `1` means `x=t_minus`;
* a proper gcd is already a factor.

This argument does not require either trace root itself to be a unit. If the two genuine roots coincide, a distinct polynomial root necessarily produces a proper gcd. Repeated-root and characteristic-two cases are therefore included.

But (3) alone supplies neither a root solver nor the genuine reference root needed by this test. A solver may find only a valid genuine root, and its other work can be expensive. The polynomial identity is not a cheap implementation of the two-branch transition. The proposed repair is useful only when the required lift/correlation is available and charged.

For odd N one can formally write `2 t_plus=kz+h` with

`h=(c-c^(-1))(u-u^(-1))`,

whose square is `(k^2-4)(z^2-4)`. Supplying only this square again loses the correlation: arbitrary modular square roots may mix signs. Supplying the actual h repairs it, but costs the corresponding native correlation. For even N, division by two is not an allowed inference; the direct trace formulas or the root-pair sum remain valid.

## 5. A correlated two-coordinate alternative

For a *fixed* base unit c, let

`s_j=z(c^j u)` and `k=z(c)`.

Then for every integer j,

`s_(j+1)=k s_j-s_(j-1)`.                                   (4)

Consequently a certified neighboring pair `(z,w)=(s_0,s_1)` has exact updates

`+c : (z,w) -> (w,kw-z)`,

`-c : (z,w) -> (kz-w,z)`.

This keeps the required correlation without solving a quadratic at each step. The update matrix has determinant one, so both directions work over any composite ring. Powers of the same base can be composed by integer matrix powers; a sequence of unrelated multipliers needs an additional lawful correlation interface.

This is the standard trace/Lucas/Dickson recurrence, not a new number-theoretic mechanism. In conventional notation `D_0(X,1)=2`, `D_1(X,1)=X`, `D_(n+1)=X D_n-D_(n-1)`, and induction gives `D_n(z(c),1)=c^n+c^(-n)`. In particular trace squaring is `z(u^2)=z(u)^2-2`. These identities are derived here; no external novelty or bibliographic search is claimed.

The two-coordinate state usually retains essentially the original lift. Indeed

`w-c^(-1)z=(c-c^(-1))u`.                                   (5)

If `gcd(c-c^(-1),N)=1`, a charged inverse recovers u from the pair. If this gcd is proper, it already factors N. If it is N, then `c^2=1` and `w=cz`, a degenerate case. Thus the neighboring trace pair is a useful correlated representation, but it is not automatically an information compression or a factoring speedup.

Nor does (4) defeat the previous return-sequence rank boundary: it propagates residue traces over a finite ring with a nonlinear gcd readout, not all marked-return bits through a fixed linear readout. Applying a short sum of update matrices to one vector preserves selected linear moments only. It does not preserve the full branch histogram or the nonlinear factor predicate.

## 6. Existing-tool match and next executable boundary

This note reuses the actually inspected sources at EM commit `2e81851d62c869a20b47ae083a24dde1a4c0420c` recorded in `WITNESS_QUOTIENT_CANDIDATE.md`:

* T0 `brc_histogram.py`, blob `9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1`: retain weights and multiplicities under lawful recoalescence. `brc_transport.py`'s affine degree-two moment lease does not include a gcd predicate.
* T4's finite fibers/collision witness interface: the trace key is declared explicitly, and a retained pair of representatives supplies the collision witness. A capacity claim does not make that pair free.
* T8's relation-observation composition law: safe inversion merges require future compatibility. The new extension is a certified successful terminal outcome when the prospective merge is not safe, not an override of that law.

Targeted repository searches for `Dickson` and `Chebyshev` returned no matches through the connector. That is only a limited repository routing observation, not evidence that the mechanism is novel or absent under every other name. No external provider was queried.

The proposed next bounded native check can consume the already planned relative-port instrument: retain one unit per trace key, classify every collision by the native gcd trichotomy, and compare complete histograms with the inversion quotient until the first new conflict-factor event. Preserve that event's two lifts and divisibility receipt. Include a symbolic prime-power-derived fixture only if the coordinator authorizes actual typed input construction; do not replace it by a host arithmetic reference.

An honest outcome may be no useful conflict and no compression gain. The measurable new capability is the terminal conflict certificate. General key count, discovery probability, product-root solving cost and end-to-end factoring complexity remain unresolved.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1.
