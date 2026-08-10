# R004 precision genesis — Supplement 24: backward semantic liveness for certificates

Status: `PROVED_WIP + EXECUTABLE_REFERENCE + P023_RECURSIVE_SPECIALIZATION`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_23.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 23 supplied typed certificate composition and safe demotion rules. The next question was how long a strong certificate distinction must remain live in a staged future program. This supplement shows that no new minimization theory is required: certificate state itself is another finite carrier to which the P023 future-safe quotient principle applies.

## 1. Deterministic staged certificate program

Consider finite certificate carriers of the same reference size and a staged deterministic program

`C_0 --f_0--> C_1 --f_1--> ... --f_(n-1)--> C_n`.

At every point i, let `o_i` be the typed observation that the remaining program must expose at that point.

Define the complete suffix signature backwards:

`Sigma_n(c)=o_n(c)`,

and

`Sigma_i(c)=(o_i(c), Sigma_(i+1)(f_i(c)))`.

Let

`Theta_i=ker Sigma_i`.

Then `C_i/Theta_i` is the unique coarsest exact certificate quotient sufficient for the whole remaining suffix.

This is exactly the deterministic future-signature construction already owned by P023, now applied to certificate state rather than physical/problem state.

## 2. Backward recurrence without storing full suffix words

Let `P_(i+1)` be the partition into `Theta_(i+1)` classes. Two certificate states c,c' may be merged at point i iff

`o_i(c)=o_i(c')`

and

`f_i(c), f_i(c')`

lie in the same `P_(i+1)` class.

Thus the minimal partition is computed by the one-step backward recurrence

`P_i = ker(c |-> (o_i(c), [f_i(c)]_(P_(i+1))))`.

No explicit exponential suffix word needs to be materialized.

## 3. Exact erasure gate

Suppose the compiler considers a candidate certificate erasure

`e_i:C_i->D_i`.

It is safe at point i iff every pair collapsed by e_i is suffix-indistinguishable:

`ker e_i subseteq Theta_i`.

Equivalently, the partition induced by e_i must refine `P_i`.

If the gate fails, there is an exact counterexample pair

`e_i(c)=e_i(c')`

but

`Sigma_i(c) != Sigma_i(c')`.

The compiler can return this pair as a fail-closed witness explaining which future behavior would be lost by demoting now.

## 4. Semantic last use

A certificate distinction is **live** at program point i exactly when some pair separated by `Theta_i` would be merged if that distinction were erased.

Consequently a strong certificate should not be demoted at program start merely because a weaker representation will eventually suffice. It may be retained through its last future-sensitive use and then collapsed immediately afterwards.

Minimal example: certificate state is a witness count in `{0,1,2}`. Before an exact-count observation, the suffix partition is discrete. After the last exact-count use, if all remaining futures ask only MAY/nonzero support, the suffix partition becomes

`{{0},{1,2}}`.

Thus COUNT -> MAY demotion is correct precisely after the final count-sensitive use.

The same rule applies to richer certificates:

- retain a module presentation while a future extension/composition needs it; later demote to exponent profile if only resource mass remains;
- retain an A3 projective direction while future exterior-field replacement depends on direction; later demote to rank/profile if only capacity budgeting remains;
- retain witness labels while future composition uses identity; later demote to MAY once all label-sensitive stages are past.

## 5. No semantic resurrection without new information

Suppose an erasure e identifies two certificate states that have different remaining suffix signatures. Any deterministic downstream computation that receives only e(c) receives the same input on both cases and therefore cannot recover the distinction.

This is not a separate novelty claim; it is the ordinary factorization/no-resurrection content of the future-safe quotient principle.

A later stronger certificate can appear only if a stage injects genuinely new side information or an explicit reconstruction witness. Automatic demotion never licenses automatic upward lifting.

## 6. Forward world synthesis / backward certificate liveness

The Representation Compiler now has a useful directional split.

### Forward

From exact world state plus a declared future language, stabilize/refine until the minimal safe carrier is obtained.

### Backward

From the terminal/staged future requirements, pull back suffix distinctions to determine how much certificate structure remains live at every program point.

These are not competing algorithms. They are two uses of the same future-compatibility principle on different carriers.

## 7. Validation

Independent exhaustive checks used a three-state certificate carrier and every deterministic two-stage program.

- all `27^2` pairs of stage functions;
- all `5^3` triples of set-partition-valued observations;
- total **91,125** complete staged programs.

For every program point, the backward recurrence partition exactly matched the partition obtained by literal complete suffix signatures.

Then every candidate erasure partition was tested at every point. Across **1,366,875** erasure checks,

`ker e subseteq Theta_i`

was exactly equivalent to literal suffix-signature safety, with zero mismatches.

These are finite exact WIP checks, not fresh full-repository CI or canonical-main claims.

## 8. Ownership and next frontier

Generic future-safe quotient / suffix indistinguishability remains P023. R004's project-local addition is only the recursive compiler application to certificate state, explicit last-use semantics and executable staged witness extraction.

The next step is to combine this backward liveness with the generator obstruction clutter. At each program point, the live suffix quotient induces a monotone **suffix adequacy predicate on primitive generators**. The hard question is whether minimal generator cuts can be updated incrementally as the suffix shrinks, yielding a dynamic instruction-retirement schedule without recomputing the full cut hypergraph from scratch.
