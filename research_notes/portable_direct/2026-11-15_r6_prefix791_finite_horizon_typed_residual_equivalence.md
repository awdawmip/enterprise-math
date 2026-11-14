# PREFIX-791 / R6 — Finite-depth certificate for all-future typed residual equivalence

Date: 2026-11-15 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_INTEGER_REGRESSION / UNREVIEWED / NOT_ADMITTED.
Context: independent external finite-state path-count observer continuation of PREFIX-790.
Scientific input remains frozen at awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Prior own activity, as historical provenance only: EM-DIRECT-E77192, RA-66BBE259AEE1AD543D9454A3 and MCP-d9aca4ec6e00440eba66035326ea5a4e.
No execution ownership of RS-X6-NATIVE-TIME-DYNAMICS is claimed.

## Question and exact model

PREFIX-790 derived the minimum continuation row for a single finite prefix/suffix cut. This note asks when finitely many typed continuation probes already certify equality for **every** finite future operation sequence, even if the compatible graph has cycles.

Take a finite directed **multigraph** on n>=1 residual states S; parallel edges are distinct paths. Each edge has a label a in a finite alphabet A, a signed integer additive weight w, and a target state. A label may encode any declared Port/Link/source/event-type observation, but only labels actually included in A are covered. The full allowed history-dependent guard must already have been represented by S and its transitions. Every state s has an integer nonnegative terminal multiplicity f_s, including zero. For an exact ordered word z=a_1...a_k define

    C_s(z;X) = sum over paths from s with ordered labels z of
               (product of edge multiplicities) X^(sum of edge weights) f_(last state),

with C_s(empty;X)=f_s. Finite path multiplicity and the signed Laurent exponent are both retained. No convergence or infinite sum is used: each fixed z has finite length. Let M_a(X) be the n x n matrix with entry (s,t) equal to the sum of X^w over all a-labelled edges s->t; let f be the terminal column. Thus

    C_s(z;X) = e_s^T M_(a_1)(X)...M_(a_k)(X) f.

For m>=1 define pi_m(X^w)=Z^(w mod m) into the integer group algebra Z[Z]/(Z^m-1). The coefficients of pi_m(C_s) are **exact nonnegative integer counts for each weight residue**. They are not counts reduced modulo m.

## Theorem 791.1 — n-1 is a sufficient all-horizon certification depth

For any two states s,t in this fixed n-state graph, the following are equivalent:

(A) C_s(z;X)=C_t(z;X) for every finite typed word z in A*.

(B) C_s(z;X)=C_t(z;X) for every typed word of length <=n-1.

The same equivalence holds when each C is replaced everywhere by pi_m(C) for **any fixed m>=1**. Consequently, when either equality fails, a distinguishing typed word has length <=n-1, and in the modular case a specific residue count differs. The statement is uniform over arbitrary finite edge multiplicities, signed integer weights, cycles and all finite label alphabets.

### Proof: exact integer-weight histograms

Work in the field K=Q(X). Every matrix M_a and the vector f are defined over this field. Write W_0=span_K{f} and

    W_(h+1)=W_h + sum_(a in A) M_a W_h.

Then W_h is exactly the span of all vectors M_z f for words |z|<=h (order follows the matrix product). This increasing chain lies in K^n. If W_0=0, all continuation outputs vanish. Otherwise dim W_0>=1, and whenever W_(h+1) differs from W_h its dimension increases by at least one. Once equality W_(h+1)=W_h occurs, W_h is invariant under each M_a, so the chain has permanently stabilized. Hence W_(n-1) equals the span of all future vectors M_z f.

Put d=e_s-e_t. Condition (B) is d^T M_z f=0 for all |z|<=n-1, equivalently d annihilates W_(n-1). It therefore annihilates every M_z f. This yields (A); the reverse implication is immediate. Equality in K=Q(X) is exactly equality of Laurent polynomials with integer coefficients because their embedding is injective. QED.

### Proof: exact weight-residue count histograms

Use the rational group algebra

    R_m=Q[Z]/(Z^m-1).

Since characteristic is zero, the cyclotomic factors Phi_d(Z), d|m, are distinct and pairwise coprime. The Chinese remainder theorem gives a finite product of fields

    R_m is isomorphic to product_(d|m) Q[Z]/(Phi_d(Z)).

For every component field K_d, apply the preceding n-dimensional span proof to the matrices pi_m(M_a) and f. Agreement through word length n-1 yields agreement for all words in every component. The CRT isomorphism returns agreement in R_m, and the natural embedding of the integer residue-count vectors into R_m is injective. Conversely, all-word agreement trivially implies short-word agreement. This proof also covers m=1. QED.

## Corollary 791.2 — an exact finite-depth cut-state quotient

For a declared graph and one declared observer (exact weighted count, or exact count at each residue m), define s~t when the corresponding continuation signatures agree on all |z|<=n-1. Theorem 791.1 makes this exactly the same as agreement on **all** finite future typed-word count queries.

At a PREFIX-790 cut, prefixes may therefore be grouped by these state signatures to evaluate such suffix queries, while preserving each prefix's own weight and multiplicity. This is the coarsest partition by equality of these exact future readouts, in the ordinary sense that any coarser partition identifies a pair separated by a named future word. It is an observer-readout quotient, not automatically an edge-by-edge quotient automaton: a reduced transition rule separately requires a transition-congruence or a direct realization certificate.

The word-depth bound is independent of modulus m. Its algorithmic cost can still be exponential in n through |A|^(n-1) word enumeration. Matrix-space/rank methods offer an alternative exact implementation over Q(X) or the cyclotomic components, with their own coefficient-growth cost.

## Exact scope and information-loss witness

There are two states u,v with terminal multiplicities f_u=f_v=1, and just one Port-a self-loop of weight zero at u. At the empty word both states report one zero-weight path. For the word Port-a, u reports one and v reports zero. Therefore current-readout equivalence does not justify merging typed histories when the Port-a operation remains allowed.

The quotient certifies only the selected alphabet and output type. A new history-sensitive guard, unrepresented signed-source label, different time observation, or access to full path identities changes the declared observer and may require refinement. Projection to Boolean support alone is not covered by the field proof. The result operates on an external finite integer-path model and does not construct native X6 cells or establish physical event admission.

## Reproducibility

Companion executable: research_notes/portable_direct/PREFIX791_R6_TYPED_FINITE_HORIZON_CHECK.py.
Companion result: research_notes/portable_direct/PREFIX791_R6_TYPED_FINITE_HORIZON_RESULTS.json.

The Python standard-library checker uses exact integer Laurent-histogram dynamic programming (no floats), deterministic seed 79120261115, 64 exhaustive binary two-state one-label/terminal graph cases and 512 seeded two-to-five-state typed multigraph cases. For every word length up to n+2, it compares exact integer histograms with independently computed modulo-m weight-residue histograms, m in {2,3,5,6,7}; it checks that any pair agreeing through n-1 also agrees at all sampled longer words. The final run: 576 graphs, 2,584 state pairs, 1,280,680 exact residue-projection checks, 108 exact-histogram and 553 modular-histogram matched-pair assertions, all passed. Regression demonstrates the implementation and selected cases; the theorem is the algebraic argument above.

## Unfinished native bridge and next discriminating action

Read the exact frozen and current native BRC/X6 Cell, Link, Port, signed-source, event-time, triadic-closure, and transition-guard records. Choose a genuinely authorized finite native event submodel and identify the finite set of states that preserves **all** history-dependent guards for its specified future operations. Compare explicit native continuation signatures through n-1 and record a shortest witness where a proposed quotient fails. If a uniform finite native state set cannot be justified for the intended horizon, retain horizon-specific residual states rather than imposing this bound on the native system.

Do not redo PREFIX-789 modular ghost-path or PREFIX-790 cut compatibility proofs. Scientific status remains author-proved external algebra with exact regression, independent review open.
