# N-Coupled Opaque/Lazy Typed Support Scalarization Delay — Research Return

Researcher-ID: `EM-NCASOT1-5E31B7`  
Task: `RS-N-COUPLED-OPAQUE-LAZY-TYPED-SUPPORT-SCALARIZATION-DELAY`  
Publication: `TP2-6C1A4E92B7D3058F2A41`  
Claim: `chatgpt-ncasot1-20260901-1024-5e31b7`  
Execution: `ER-372A6DB57FEBB5C34219`

## Verdict

`NEGATIVE_BOUNDARY / FINITE_EFFECTIVE_OPAQUE_MODULES_ARE_PRESENTATION_REFLECTIVE`.

Hard-target disposition:

`FINITE_EFFECTIVE_OPAQUE_MODULES_WITH_GENERATOR_COMPLETE_PUBLIC_OPERATIONS_AND_DECIDABLE_EQUALITY_REFLECT_TO_EXPLICIT_PRESENTATIONS_AND_ONE_SIDED_SUPPORT_SCALARIZES`.

This closes ordinary finite opaque/lazy abstract-data-type wrapping as an escape from the accepted explicit-presentation theorem. It does **not** close all implicit computation. The smallest surviving capability is `NONREFLECTIVE_CAPABILITY_SEMANTICS`.

## Frozen grammar `G_fin-reflect`

Let `N=pq` with distinct hidden primes. A pre-readout state is an opaque handle type representing a finite `Z/NZ`-module `M`; no coordinates, basis, relation matrix, Smith data, Fitting generators, `p`, `q`, or hidden-prime selector are exposed.

The public factor-blind interface exposes only:

1. `N`;
2. a zero handle;
3. a finite generator-complete handle list `G`;
4. total addition on handles;
5. decidable extensional equality;
6. ordinary reusable program closure: handles may be stored, duplicated, replayed, repeatedly added, and compared.

Lazy evaluation is allowed. Complexity is unrestricted. Opacity is genuine: the implementation representation is never opened.

## Theorem A — finite opaque closure is enumerable

Set `S_0={0}∪G` and iterate

`S_(j+1)=S_j ∪ {x+y : x,y∈S_j}`,

deduplicating by public extensional equality. Since `M` is finite, the monotone process stabilizes. Since `G` generates `M`, the stable set is exactly `M`. No size bound is needed in advance.

Therefore the full opaque carrier is effectively enumerable from the pre-readout interface. Laziness only changes when calls are forced; it does not remove the finite closure computation.

## Theorem B — Cayley reflection reconstructs a presentation

Index the enumerated carrier by `X=M`. Introduce one free integer generator `e_x` for each `x∈X`. Add the finite relations

`e_0=0`

and, for every ordered pair `x,y∈X`,

`e_x+e_y-e_(x+y)=0`.

Let `A_M` be the integer relation matrix with these rows and columns indexed by `X`.

Define `ψ: Z^X -> M` by `ψ(e_x)=x`. Every displayed relation is in `ker ψ`, so `ψ` descends to a surjection `ψ̄: Z^X/R -> M`. Conversely define `φ(x)=[e_x]`. The Cayley relations give `φ(x+y)=φ(x)+φ(y)`. Then `ψ̄φ=id_M`, while `φψ̄([e_x])=[e_x]` on every quotient generator. Hence

`Z^X / R ≅ M`.

The construction queries only exported handles, addition and equality. It never opens the opaque representation. Thus `G_fin-reflect` computably reflects to an explicit finite integer presentation.

## Corollary — one-sided support scalarizes before readout

For every prime `r|N`,

`M ⊗ F_r ≅ coker(A_M mod r)`

up to the harmless row/column orientation convention, so

`dim_F_r(M⊗F_r)=|X|-rank_F_r(A_M mod r)`.

If the opaque state has unequal hidden fiber dimensions for `p` and `q`, then the reflected presentation has unequal ranks modulo `p` and `q`. The accepted `G_exp-Fit` theorem then gives a determinantal level `k` with

`1 < gcd(N,D_k(A_M)) < N`.

Therefore any one-sided Fitting/rank support event in `G_fin-reflect` already has an effective proper scalar gcd before the declared readout.

So:

`FINITE_EFFECTIVE_OPAQUE_MODULE + ONE_SIDED_FITTING_SUPPORT`

implies

`PRE_READOUT_PRESENTATION_REFLECTION + PROPER_SUPPORT_GCD`.

This kills ordinary opacity, lazy thunks, and finite black-box modules whenever generators, addition, equality and reusable program composition remain public.

## What survives

A future positive construction must deny at least one reflection capability:

- no effective extensional equality;
- no generator-complete finite enumeration route;
- no unrestricted replay/duplication/composition of handles, e.g. genuinely linear/affine capability semantics;
- or leave the finite module/Fitting-support setting.

These are necessary escape capabilities for this theorem, not proved sufficient mechanisms. In particular, an oracle whose hidden operation table is initialized using `p`, `q`, a CRT idempotent, or a hidden place violates the public `N`-only contract rather than providing a positive construction.

The boundary is:

`OPAQUE != NONREFLECTIVE`.

Do not issue another generic “opaque/lazy” successor. If the parent objective continues, the next discriminator should be explicitly capability-theoretic: `PUBLIC_N_ONLY_NONREFLECTIVE_CAPABILITY_ASYMMETRY`.

## Classical firewall

The reviewed prior-art exclusions remain unchanged: no Pollard/Williams/ECM order-smoothness route; no rho collision/cycle route; no Fermat/CFRAC/Dixon/QS/NFS square-relation route; no named-prime p-adic route; no direct zero-divisor, nonunit, idempotent or nontrivial-root endpoint.

The present proof uses none of those mechanisms. Its endpoint is only the already-accepted determinantal scalarization applied to the reflected presentation.

## Deterministic regression

Checker:

`research_checks/N_COUPLED_OPAQUE_LAZY_TYPED_SUPPORT_SCALARIZATION_DELAY_CHECK_20260901.py`

Certificate:

`research_artifacts/N_COUPLED_OPAQUE_LAZY_TYPED_SUPPORT_SCALARIZATION_DELAY/reflection_certificate_20260901.json`

Executed result:

`PASS N_COUPLED_OPAQUE_REFLECTION reflection_cases=4 maximal_minors=68290 N15_one_sided_cases=2`

The checker reconstructs Cayley presentations for `Z/d`, `d=2,3,4,5`, from addition tables and verifies the maximal determinantal divisor is `d`. For `N=15`, reflected `Z/3` has ranks `2 mod 3`, `3 mod 5` and support gcd `3`; reflected `Z/5` has ranks `5 mod 3`, `4 mod 5` and support gcd `5`. The finite scan is regression evidence only; the general result is the symbolic proof above.

## Scope firewall and handoff

This Result does not prove impossibility of infinite/non-effective carriers, equality-free opaque types, non-copyable capability handles, external physical/oracular hidden resources, non-module typed states, all black-box algebra, or factoring in any complexity class.

`method_harvest=RESULT_ONLY`. Reusable but unpromoted method: `OPAQUE_ADT_REFLECTION_BY_CAYLEY_PRESENTATION`.

Recommended Driver disposition:

`ACCEPT_NEGATIVE_BOUNDARY_IF_ENVELOPE_VALID`.

No Working Truth, Foundation authority, L4/canonical promotion, novelty, or complexity claim is granted.
