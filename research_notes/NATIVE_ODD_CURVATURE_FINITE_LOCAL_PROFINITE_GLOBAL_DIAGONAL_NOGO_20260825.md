# Odd-curvature filament: finite local satisfiability, profinite realization, and diagonal integer no-go

Status: `FREE_RESEARCH_EXACT_LOCAL_GLOBAL_COROLLARY / CLASSICAL_PROFINITE_COMPACTNESS_INPUT / NOT_CANONICAL_ENTERPRISE_GEOMETRY`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ODD_CURVATURE_PROFINITE_TRANSPARENT_FRACTAL_PHASE_20260825.md`.

## 1. Setup

Let

`F_B(H,r)=H+(B*r^2+eps(r))/2`

with positive odd `B` in a no-breaker phase

`B=15,39,51 mod60`.

For each prime q, the local transparent set

`T_B(q) subset Z/qZ`

is nonempty.

## 2. Every finite prime system has an ordinary integer solution

Let S be any finite set of primes.

Choose one transparent class

`h_q in T_B(q)`

for every `q in S`.

By the Chinese remainder theorem there exists an ordinary integer H satisfying

`H=h_q mod q`

for every q in S.

For this H,

`q does not divide F_B(H,r)`

for every q in S and every shell r.

Therefore every finite family of prime-channel constraints is simultaneously satisfiable by an ordinary integer transverse parameter.

Freeze:

`EVERY FINITE PRIME SUBSYSTEM IS INTEGER-SATISFIABLE`.

## 3. The full infinite prime system has no ordinary integer solution

Fix any ordinary integer H.

Because B>0,

`F_B(H,r)=H+(B*r^2+eps(r))/2 -> +infinity`

as `r->infinity`.

Choose r large enough that

`F_B(H,r)>1`.

That positive integer has at least one prime divisor q. Hence

`q | F_B(H,r)`.

So H fails the q-transparent condition.

Therefore

`there is no H in Z transparent to every prime channel simultaneously`.

Equivalently, if Z is embedded diagonally into the squarefree prime-channel product,

`Tcal_B intersect Z = empty`.

This is true for every positive odd B whenever the infinite transparent profinite set is defined; it is not special to one no-breaker residue class.

## 4. Yet the profinite system is globally realizable

The compatible squarefree carrier is

`S = product_q F_q`.

Since every local factor T_B(q) is nonempty in a no-breaker phase,

`Tcal_B=product_q T_B(q)`

is nonempty by direct product construction / compactness.

Indeed it has continuum cardinality, Haar measure zero and full Hausdorff dimension in the primorial ultrametric, as proved in the parent note.

Thus:

`finite integer satisfiability`

`+ compatibility of all finite projections`

`-> profinite global realizability`,

but

`NOT -> ordinary integer global realizability`.

Freeze the exact local-global pattern:

`FINITE-SATISFIABLE -> PROFINITELY REALIZABLE -> DIAGONALLY NON-REALIZABLE`.

## 5. Relation to density of Z in its completion

The diagonal integers are dense in the profinite completion: every finite congruence neighborhood contains an integer.

This is exactly why every finite subsystem is solvable.

But a closed inverse-limit set can be nonempty while missing the dense diagonal copy of Z entirely. The present transparent product supplies an explicit structured example selected by the filament arithmetic.

So there is no contradiction between

- integer solutions to every finite wheel;
- a nonempty profinite inverse-limit basin;
- no integer solution to all prime channels at once.

## 6. Native specialization

The actual Enterprise coefficient B=3 is not in this no-breaker regime: channel5 already makes the local factor empty. Hence the native system fails before the profinite-vs-diagonal distinction arises.

The comparison families B=15,39,51 mod60 are useful precisely because they separate

`finite-channel breaker extinction`

from

`pure inverse-limit local-global failure`.

## 7. Boundary

CRT, density of Z in its profinite completion, compactness of products of finite sets, and the fact that an integer >1 has a prime divisor are classical.

No novelty claim is made for those principles.

The research-specific content is their exact realization inside the odd-curvature transparent-filament family and the resulting phase comparison with the native B=3 finite-dimensional extinction.