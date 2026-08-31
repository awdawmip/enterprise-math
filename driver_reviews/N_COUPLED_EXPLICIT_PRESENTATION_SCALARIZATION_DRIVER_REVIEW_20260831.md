# Driver Review — N-Coupled Explicit-Presentation Scalarization Boundary

Driver-ID: `EM-DVR-P8H4Q2`
Review-ID: `DR-E71A71AADBB2ACF55EFF`
Task: `RS-N-COUPLED-SCALAR-CLEAN-NONAUTOMORPHIC-FITTING-SUPPORT-CHANGE`
Publication: `TP2-2E7C91A54B60D83F1C25`
Result: `RR-E71A71AADBB2ACF55EFE`
Execution: `ER-4F06838FF6321D1C65DC`

## Disposition

`ACCEPTED / EXACT_NEGATIVE_BOUNDARY / FOLLOWUP_TASK`.

The Result is accepted at the exact declared `G_exp-Fit` scope. It does not prove impossibility of arbitrary non-ring, typed, black-box, lazy or implicit factorization processes. It proves a precise post-state scalarization theorem for every pre-collapse state that is materialized as an explicit finite integer presentation matrix.

The scheduler runtime omitted a formal HANDOFF event for this execution, but the durable branch contains a frozen terminal Result, complete manifest, exact authorized scope, and terminal Researcher return. Driver review consumes those durable artifacts without fabricating a Researcher HANDOFF.

## Envelope and scope audit

The Result manifest is complete and the four frozen outputs resolve to the declared Git blobs:

- Return: `c46c49bea6d9d429c8ddc7803fe985d4a5754c8c`;
- checker: `15debd7450c4d327449835d666cbdd38c7f1725d`;
- exact scalarization certificate: `00d4c0a758769936c7a0693a8e75d0da0477e46a`;
- execution record: `5c07b5cc7ff53d8b7c71693a9fdf6f764618d1d8`.

The Researcher branch is a clean descendant of the authorized execution base and contains only task-authorized output paths. The finite checker is regression evidence; the accepted theorem is symbolic and post-state.

## Accepted theorem

For an explicit integer matrix `A` define the determinantal divisor

`D_k(A) = gcd(|det A[I,J]| : |I|=|J|=k)`

and for public `N=pq`, with distinct hidden primes, define

`sigma_k(A;N)=gcd(N,D_k(A))`.

For every prime `r`:

`r | D_k(A)  <=>  rank_F_r(A mod r) < k`.

Consequently, for `N=pq`:

`rank_F_p(A) != rank_F_q(A)`

if and only if

`exists k: 1 < sigma_k(A;N) < N`.

Thus, whenever a factor-blind process has materialized its pre-collapse support-bearing state as an explicit finite integer presentation, any one-sided hidden-channel rank/Fitting-support event already possesses a canonical public scalar proper-gcd witness at the same state.

The proof is independent of the transition history. It therefore covers the declared explicit-presentation class even when the update is singular, dimension-changing, projection/compression based, quotient/completion based, carry/history dependent, variable-time, or non-CRT-natural.

## Non-vacuity and exact boundary

The accepted `N=15` witness shows that a fixed factor-blind non-invertible projection can genuinely change Fitting support from balanced to one-sided while all individual coordinate scalars remain gcd-clean. The failure occurs because the relation/minor support scalar `D_2=3` becomes a proper factor once the projected presentation is explicit.

Therefore both statements are frozen:

- `NONAUTOMORPHIC_PROJECTION_CAN_CHANGE_FITTING_SUPPORT` — true;
- `EXPLICIT_PRESENTATION_SUPPORT_ASYMMETRY != SCALAR_CLEAN_TYPED_ASYMMETRY`.

Equivalently, `SUPPORT_CHANGE != SUPPORT_HIDING`.

## Scope firewall

This review does not extend the theorem to a carrier whose relevant support object remains implicit, opaque, lazy, oracle-like, relation-valued, or otherwise unavailable as an ordinary explicit finite presentation before the declared collapse/readout boundary.

A successor is legitimate only if it freezes the typed interface itself and proves that presentation-level determinantal scalarization is unavailable by semantics, not merely omitted from an implementation. If an effective canonical finite presentation can be reconstructed before collapse, the accepted `G_exp-Fit` theorem kills that route immediately.

The existing classical-mechanism firewall remains mandatory: no hidden `p,q`, candidate-prime schedule, factor-aware idempotent, direct nonunit, group-order/smoothness route, collision/cycle route, congruence-of-squares/relation route, or named-prime p-adic route may be relabeled as typed-support novelty.

## Gate decisions

- `MATHEMATICAL_CONTINUATION = REQUIRED` — the parent objective remains open and the smallest surviving semantic capability is now precise.
- `LEAN_FORMALIZATION = NOT_REQUIRED` — this is another exact boundary, not a stabilized positive factorization theorem.
- `EXTERNAL_PRIOR_ART_DUPLICATION = SATISFIED_BY_EXISTING_REVIEWED_BOUNDARY` — the accepted non-ring prior-art audit supplies the mandatory classical mechanism map; the next task must reuse it.
- `INDEPENDENT_REPLICATION = NOT_REQUIRED_AT_THIS_CHECKPOINT` — reconsider only after a positive typed construction survives the firewall.
- `ADVERSARIAL_AUDIT = REQUIRED_INSIDE_SUCCESSOR` — any purported opaque carrier must be attacked for hidden effective presentation/scalarization and classical-mechanism equivalence.

## Follow-up

Publish one P1/HIGH continuation targeting an `OPAQUE_OR_LAZY_TYPED_SUPPORT_CHANGE_BEFORE_SCALARIZATION` interface. The task must either construct a genuinely scalar-clean delayed-readout asymmetry or prove its declared typed grammar still collapses to explicit presentation/classical support exposure.

No factoring lower bound, novelty, Working Truth, Foundation, L4, or canonical promotion is granted.
