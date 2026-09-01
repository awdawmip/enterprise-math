# N-Coupled Opaque/Lazy Typed Support Scalarization Delay — Research Return

Researcher-ID: `EM-NCASOT1-5E31B7`  
Task: `RS-N-COUPLED-OPAQUE-LAZY-TYPED-SUPPORT-SCALARIZATION-DELAY`  
Publication: `TP2-6C1A4E92B7D3058F2A41`  
Claim: `chatgpt-ncasot1-20260901-1024-5e31b7`  
Execution: `ER-372A6DB57FEBB5C34219`

## 1. Terminal verdict

`NEGATIVE_BOUNDARY / FINITE_EFFECTIVE_OPAQUE_MODULES_ARE_PRESENTATION_REFLECTIVE`.

Hard-target disposition:

`FINITE_EFFECTIVE_OPAQUE_MODULES_WITH_GENERATOR_COMPLETE_PUBLIC_OPERATIONS_AND_DECIDABLE_EQUALITY_REFLECT_TO_EXPLICIT_PRESENTATIONS_AND_ONE_SIDED_SUPPORT_SCALARIZES`.

The task asked whether semantic opacity/laziness can preserve a genuinely one-sided hidden support state while every pre-readout scalar remains gcd-clean, or whether a precise opaque grammar still collapses to the accepted explicit-presentation obstruction.

This return freezes one exact and broad software-level opaque grammar, `G_fin-reflect`, and proves a no-go. Internal representation may be completely hidden and no presentation matrix is supplied. Nevertheless, if the pre-readout interface exposes a finite generating family, zero, total addition, extensional equality, and ordinary reusable program composition, then the interface itself effectively reconstructs a finite integer presentation. The accepted determinantal-divisor theorem therefore applies before the declared readout.

So ordinary abstract-data-type opacity and laziness do **not** supply the missing capability.

The smallest surviving capability is narrower:

`NONREFLECTIVE_CAPABILITY_SEMANTICS`.

A future positive route must deny at least one load-bearing reflection capability — effective extensional equality, generator-complete finite enumeration, unrestricted replay/duplication/composition of handles, or the finite module/Fitting-support model itself. This return does not prove such stronger capability semantics impossible.

No Working Truth, Foundation authority, L4 promotion, canonical promotion, novelty, or universal factoring lower bound is asserted.

## 2. Frozen controls

The result consumes without strengthening:

1. accepted `G_exp-Fit`: once a support-bearing pre-readout state is materialized as an explicit finite integer presentation matrix, unequal hidden `p/q` rank/Fitting support yields a canonical proper determinantal gcd;
2. accepted distinction `SUPPORT_CHANGE != SUPPORT_HIDING`;
3. reviewed classical firewall excluding order/smoothness, collision/cycle, square-relation, named-prime p-adic, direct nonunit/idempotent/root mechanisms;
4. the requirement that opacity be semantic/interface-level rather than implementation secrecy.

The present result adds only a reflection theorem for a declared opaque interface class.

## 3. Frozen grammar `G_fin-reflect`

Let `N=pq` with distinct hidden primes. A pre-readout state is an opaque handle type representing a finite `Z/NZ`-module `M`. The internal representation is inaccessible.

The public, factor-blind, pre-readout interface exposes:

1. public input `N` only;
2. a zero handle `0_M`;
3. a finite public list of handles `G={g_1,...,g_s}` whose additive closure is all of `M`;
4. a total addition operation `add : M x M -> M`;
5. decidable extensional equality `eq : M x M -> Bool`;
6. ordinary program closure: returned handles may be stored, replayed, duplicated, added repeatedly, and compared for equality by any finite public program.

The interface does **not** expose:

- coordinates;
- a basis;
- relation rows;
- a matrix presentation;
- Smith data;
- annihilators;
- Fitting generators;
- hidden `p,q`;
- a hidden-prime selector.

Lazy evaluation is allowed. The implementation may compute handles only when demanded. Complexity is unrestricted; the question is exact availability, not efficiency.

This grammar captures the most direct attempt to turn the accepted explicit-presentation boundary into an ordinary opaque or lazy abstract data type while retaining enough algebraic operations to carry finite support.

## 4. Theorem A — finite opaque additive closure is effectively enumerable

Starting from

`S_0 = {0_M,g_1,...,g_s}`,

iterate

`S_(j+1) = S_j union {x+y : x,y in S_j}`

and deduplicate using public extensional equality.

Because `M` is finite, this monotone process stabilizes after finitely many strict enlargements. When it stabilizes, the resulting set is closed under addition and contains the declared generating family. Since `G` generates all of `M`, the stable set is exactly `M`.

Thus the full finite carrier is effectively enumerable from the declared pre-readout interface.

No cardinality bound is needed in advance. Termination follows from finiteness, and completeness follows from generator-completeness.

Laziness does not change the proof: the reflection algorithm simply forces the finite set of operation calls required for closure.

## 5. Theorem B — Cayley reflection reconstructs an explicit integer presentation

Let the enumerated carrier be `X=M`. Introduce one free integer generator `e_x` for every handle `x in X`.

Create the finite relation family

`e_0 = 0`,

and, for every ordered pair `x,y in X`,

`e_x + e_y - e_(x+y) = 0`.

Let `A_M` be the integer matrix whose columns are indexed by `X` and whose rows are these relation vectors.

Then

`Z^X / rowspan_Z(A_M) ~= M`

canonically as additive groups, and compatibly with the `Z/NZ`-module structure because `N` annihilates `M`.

### Proof

Define `psi : Z^X -> M` by `psi(e_x)=x`. Every displayed relation lies in the kernel because `0_M=0` and `x+y` is the public addition result. Hence `psi` descends to a surjection

`psi_bar : Z^X / R -> M`.

Conversely define `phi : M -> Z^X/R` by `phi(x)=[e_x]`. The Cayley relation gives

`phi(x+y)=[e_(x+y)]=[e_x]+[e_y]`,

so `phi` is a homomorphism. By construction `psi_bar(phi(x))=x`. On each quotient generator,

`phi(psi_bar([e_x]))=phi(x)=[e_x]`.

Therefore `phi` and `psi_bar` are inverse isomorphisms. QED.

Crucially, the construction reads only the exported handles, addition results and equality tests. It never opens the opaque representation.

Hence `G_fin-reflect` is not genuinely outside the explicit finite-presentation world: it **computably reflects into it**.

## 6. Corollary — one-sided hidden support scalarizes before readout

Tensor the reflected presentation with `F_r` for a prime `r | N`. Right exactness gives

`M tensor F_r ~= coker(A_M mod r)`

up to the harmless row/column orientation convention. Therefore

`dim_F_r(M tensor F_r) = |X| - rank_F_r(A_M mod r)`.

If the opaque state has unequal hidden fiber dimensions,

`dim_F_p(M tensor F_p) != dim_F_q(M tensor F_q)`,

then

`rank_F_p(A_M mod p) != rank_F_q(A_M mod q)`.

The accepted `G_exp-Fit` theorem applies to the reflected explicit matrix. Thus for some determinantal level `k`,

`1 < gcd(N,D_k(A_M)) < N`.

So any one-sided Fitting/rank support event inside `G_fin-reflect` has an effective proper scalar gcd available **before** the declared readout.

This violates the required scalar-clean pre-readout contract.

Therefore:

`FINITE_EFFECTIVE_OPAQUE_MODULE + ONE_SIDED_FITTING_SUPPORT`

implies

`PRE_READOUT_PRESENTATION_REFLECTION + PROPER_SUPPORT_GCD`.

The obstruction is semantic, not representational: hiding the implementation does not hide what can be reconstructed from the public algebraic interface.

## 7. Ordinary opacity and laziness are killed

### 7.1 Opaque wrapper around an explicit matrix

Killed immediately. The wrapper may hide the matrix bytes, but if it exports generator-complete handles, addition and extensional equality, Theorems A-B reconstruct an alternative presentation.

### 7.2 Lazy relation object

Killed under the same interface. Laziness changes evaluation order, not extensional information. A finite closure program forces enough calls to reconstruct the carrier and Cayley relations.

### 7.3 Finite black-box module

Killed if the black box exports finite generators, total addition and equality. No access to its internal coordinate representation is required.

### 7.4 “The API does not expose a `presentation()` method”

Insufficient. The presentation is synthesized from ordinary exported operations. Refusing to provide a convenience method is implementation/API packaging, not a semantic obstruction.

### 7.5 Secret or factor-aware oracle hidden behind opaque handles

Rejected by the task input contract. If the hidden operation table is initialized from `p`, `q`, a CRT idempotent, a hidden place, or another factor-selecting resource, the process is no longer public `N`-only and factor-blind.

## 8. Why this is stronger than the parent boundary but still bounded

The accepted parent theorem required an explicit presentation to be materialized as the pre-readout state.

The present theorem removes that representation requirement for `G_fin-reflect`: the matrix need not be stored, named or exposed. A public program can synthesize one from the opaque interface.

But the result is not universal. It depends on the exact reflection capabilities listed in Section 3. It does not cover every possible typed or implicit state.

This is the intended narrowing:

`EXPLICIT_PRESENTATION`

was already closed;

`ORDINARY_FINITE_OPAQUE_ADT_WITH_REFLECTION_CAPABILITIES`

is now also closed;

the surviving region is

`NONREFLECTIVE_CAPABILITY_SEMANTICS`.

## 9. Smallest surviving capability

At least one of the following must fail before a future positive construction can evade the reflection theorem.

### 9.1 No effective extensional equality

Without equality, a public program may be unable to deduplicate handles or certify closure/stabilization. Mere handle identity is not enough if multiple handles may denote the same abstract state.

### 9.2 No generator-complete finite enumeration route

The interface may expose operations on a typed object without exposing a finite generating family whose closure is all support-bearing state.

### 9.3 No unrestricted replay/duplication/composition

Linear or affine capability semantics may prevent retaining and duplicating arbitrary handles to build the full Cayley table. This is a genuinely stronger semantic restriction than ordinary opacity.

### 9.4 Leave finite module/Fitting support

A typed carrier whose decisive asymmetry is not finite-module support may lie outside both the parent theorem and the present reflection theorem. It must still pass the classical-mechanism firewall.

These are **necessary escape capabilities for this theorem**, not proved sufficient mechanisms.

The most economical next phrase is:

`OPAQUE != NONREFLECTIVE`.

A future task should not ask merely for an opaque object. It should ask whether a public `N`-only **nonreflective capability interface** can carry asymmetry without secretly importing a factor-selecting oracle.

## 10. Classical-mechanism firewall

The accepted prior-art map is reused unchanged.

- no Pollard `p-1`, Williams `p+1`, ECM order/smoothness annihilation;
- no Pollard-rho collision/cycle success event;
- no Fermat/CFRAC/Dixon/QS/NFS congruence-of-squares relation mechanism;
- no named-prime Hensel/p-adic place;
- no direct zero divisor, nonunit, CRT idempotent or nontrivial root endpoint.

The present proof does not instantiate any of these algorithms. Its endpoint is the already-reviewed determinantal support scalarization of the reflected presentation.

No external novelty conclusion is drawn.

## 11. Deterministic finite regression

Checker:

`research_checks/N_COUPLED_OPAQUE_LAZY_TYPED_SUPPORT_SCALARIZATION_DELAY_CHECK_20260901.py`

Certificate:

`research_artifacts/N_COUPLED_OPAQUE_LAZY_TYPED_SUPPORT_SCALARIZATION_DELAY/reflection_certificate_20260901.json`

Executed result in this research run:

`PASS N_COUPLED_OPAQUE_REFLECTION reflection_cases=4 maximal_minors=68290 N15_one_sided_cases=2`

The checker reconstructs Cayley presentations for cyclic opaque groups `Z/d`, `d=2,3,4,5`, from addition tables only and verifies that the gcd of all maximal minors is exactly `d`.

For `N=15` it separately verifies:

- reflected `Z/3`: rank `2` modulo `3`, rank `3` modulo `5`, maximal determinantal divisor `3`, hence proper gcd `3`;
- reflected `Z/5`: rank `5` modulo `3`, rank `4` modulo `5`, maximal determinantal divisor `5`, hence proper gcd `5`.

The `68,290` exact maximal-minor computations are regression evidence only. The general result is the symbolic Cayley-reflection proof above.

## 12. Method/tool disposition

`method_harvest = RESULT_ONLY`.

Reusable idea, not promoted as a global tool in this Result:

`OPAQUE_ADT_REFLECTION_BY_CAYLEY_PRESENTATION` — when a finite algebraic carrier exports generator-complete operations and extensional equality, test whether the supposedly hidden presentation can be reconstructed from its public operation graph.

This method is a direct adversarial extension of the accepted `G_exp-Fit` boundary. It does not warrant a new global tool family before Driver review.

## 13. Scope firewall

This return does **not** prove impossibility of:

- infinite or non-effective carriers;
- equality-free opaque types;
- linear/affine non-copyable capability handles;
- physical or cryptographic hidden resources not reducible to a public deterministic `N`-only program;
- non-module typed states whose asymmetry is not Fitting/rank support;
- all black-box algebra algorithms;
- all implicit computation;
- factoring in any complexity class.

It also does not assert that the surviving nonreflective capability class is realizable without hidden factor information.

## 14. Driver handoff

Recommended disposition:

`ACCEPT_NEGATIVE_BOUNDARY_IF_ENVELOPE_VALID`.

Freeze the new boundary as:

`ORDINARY_FINITE_OPAQUE_OR_LAZY_MODULE_ADT_DOES_NOT_DELAY_SCALARIZATION_WHEN_GENERATORS_ADDITION_EQUALITY_AND_REUSABLE_PROGRAM_CLOSURE_ARE_PUBLIC`.

If the parent objective continues, do **not** publish another generic “opaque/lazy typed support” task. The next mathematical discriminator should be explicitly capability-theoretic:

`PUBLIC_N_ONLY_NONREFLECTIVE_CAPABILITY_ASYMMETRY`

with a hard requirement to state which reflection capability is removed and why that restriction is not merely implementation secrecy or a hidden factor oracle.

No Foundation mutation, Working Truth, canonical promotion, novelty or complexity claim should occur at this checkpoint.
