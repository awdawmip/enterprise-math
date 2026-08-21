# R061 Stage 3 — Canonical Unoriented Segment Structure

Researcher-ID: `EM-R061S3-2F9622`

## Ordered bidirectional record

For an endpoint order `(P,Q)` define

`BREC_E(P,Q) = ( T(P->Q), T(Q->P) )`.

Endpoint swap acts by the transposition `(T_f,T_r) -> (T_r,T_f)`.

The orientation-free orbit is therefore

`BSEG_E(P,Q) = { T(P->Q), T(Q->P) }`

as an unordered two-element set for `P!=Q`, and a singleton zero-trace set for `P=Q`.

This object is forced by the current premises: it is exactly the `S_2` orbit of the two independently canonical directed traces. No orientation is selected and no trace is discarded.

## Properties

`BSEG_E` is endpoint-canonical, endpoint-swap invariant, translation covariant, cyclically covariant, axis-glue compatible, algebraically generable from the two Stage 2 positive-axis decodes, and sufficient to recover either directed trace once endpoint order is supplied.

It remains strictly stronger than the unordered endpoint pair because line identity is native component trace.

## Candidate classification

### U0 — inverse quotient of one selected directed trace

`{T,T^{-1}}` is not endpoint-canonical for any nonzero unordered pair. Starting from `T_f` and starting from `T_r` produce different inverse-quotient classes because `T_r != T_f^{-1}` and `T_f != T_r^{-1}`.

### U1 — bidirectional canonical trace pair

Passes all required invariance and typing gates. This is the minimal lossless orientation-free quotient of the ordered pair of canonical traces.

### U2 — select one of the two canonical directions

Not derivable. For every nonzero unordered pair the endpoint-swap action exchanges two distinct canonical traces and has no fixed trace. An orientation-free single-trace selector would require a new tie-break/choice rule. Lexicographic order, shorter/longer directed gauge, carrier orientation, or global-coordinate preference are all extra structure.

### U3 — decorated bidirectional segment

A stronger, still canonical decoration is

`DBSEG_E(P,Q) = { (T_f, Realize(T_f), ell_f), (T_r, Realize(T_r), ell_r) }`.

It is not a different segment identity; it is `BSEG_E` equipped with already frozen path fibers and directed gauges.

## Final classification

`CANONICAL_UNORIENTED_SEGMENT_STRUCTURE = BIDIRECTIONAL_CANONICAL_TRACE_PAIR`.

This does not imply a scalar symmetric metric.
