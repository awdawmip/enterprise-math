# Complete-native SO trace bank: versioned next implementation plan

Status: **SHARED_CONTEXT_SOURCE_REVIEW_AND_SYMBOLIC_DESIGN / NOT_EXECUTED / NOT_ADMITTED**.
This plan changes no frozen code, certificate, or evidence. It proposes a
cheaper complete-word squared-norm bound for the existing uniform omission
policy. It neither changes propagation nor makes the underlying Gram oracle
efficient. No scientific arithmetic or professional query was run for this note.

## 1. Read source and immutable boundary

The mathematical starting point is
`sep27-qft-uniform/theory_review/UNIFORM_WORD_CERTIFICATE_REVIEW.md`, SHA-256
`c3df002344d86711c4a86f63e2b7ec54c8e421d6017e8d209894b20453d0cccf`.
The following actual source was read:

| Source | SHA-256 / relevant interface |
|---|---|
| `word_certificates/word_certificates.py` | `c3e8156b5c7573778cd1e781f23e82394c83842a9f4655b59c9659035dc62ce3`; `WordCertificateBank`, `_program_view`, `_certify_word`, `SignedExpressions` |
| `uniform_execution/uniform_feedback.py` | `755d398a19881508112c9e360c94bf10133681af8d3cbdbb103accdecc306e28`; exact bank-type gate, `prepare_next`, strict restore |
| `new_word_compiler/compiled_streaming.py` | `d0f980b7ff5fb41438e9e0ad40af65a190bcd6f83660c821f8362643190a558c`; `normalized_word`, `replay_complete_word`, `CompleteNativeWord` |
| `optimization/carrier_codec/carrier_codec.py` | `c25149e0ab4ce92a59d2ca40cb697fe6505cd1dc8d406e9c5a2d92cb2b28c953`; full-column restriction and exact complement identity |
| frozen `stage80/fixed_phase.py` | `d9981004a89c651f072ff88732c8b402baf83c16690a0cfacfa9c32199fde254`; actual `primitives`, `apply_word`, `FixedRotor`, `QuarterTurn` |
| new boundary implementation | `875133020ba713af755d19b121f416938193835c3e2c9b7e6ab228c19b814c83`; outer guard semantics are reusable, its old bank type is not |

The compiler's `PositivePathObserver.evaluate` was also read. It constructs
actual positive paths with separate sign endpoints, executes `core_power`, and
retains every input term and endpoint. Its Fraction calculation is an identity
check against actual output; it is not a replacement propagator. Its
`positive_determinant` merely counts non-H4 letters, so it is useful only after
the primitive determinant proof and source binding below.

The parent supplied the current actual startup-guard PASS, and the boundary
startup record was read. This note grants no additional admission authority.

## 2. Complete determinant and trace proof

Use the entire D=61 carrier. For the actual orthogonal word G define

    B = (I-G)^T(I-G) = 2I-G-G^T,
    t_G = D-tr(G),       tr(B)=2t_G.

All eigenvalues of B lie in [0,4]. If det(G)=+1, nonreal eigenvalues of G
occur in conjugate pairs and yield paired identical B eigenvalues. The -1
eigenvalue of G has even multiplicity, so it too contributes an even number
of eigenvalues 4 to B. Thus every nonzero B eigenvalue occurs at least twice,
and

    ||I-G||^2 <= min(4,t_G).                         (SO)

This is an upper bound; without a separate structural proof it is not the
exact norm. Orthogonality implies t_G>=0, which the observed scalar must also
satisfy. A negative observed value is an error; it must not be clipped to zero.

There are two honest fallback cases:

1. If complete real orthogonality and det(G)=-1 are certified, G has an odd
   number of -1 eigenvalues. Therefore `||I-G||^2=4` exactly, in either odd or
   even dimension. Return bound 4 with method `DET_MINUS_ONE_EXACT`; do not
   reinterpret the old reflection's failed half-trace value 2 as a valid bound.
2. If complete orthogonality is certified but orientation is unavailable,
   use `min(4,2t_G)`. Missing orthogonality or native provenance is an admission
   failure, not this fallback. The strict fixed native alphabet below should
   always determine orientation; this general fallback is an explicitly
   separate future input profile.

If t_G=0, PSD B has zero trace, so G=I and bound 0 is exact. An empty word is
also an immediate structural example, but the proposed cold implementation
still executes the full admission/profile below. No target angle is used.

### Primitive provenance instead of a free determinant oracle

The actual `primitives()` receipt gives H4 as one half of

    [ 1  1  1  1 ]
    [ 1 -1  1 -1 ]
    [ 1  1 -1 -1 ]
    [ 1 -1 -1  1 ].

Its character columns are orthonormal, it is symmetric, and its trace is
zero. Hence H4 has two +1 and two -1 eigenvalues and determinant +1. The same
actual receipt gives negation -1 and the swap columns `(0,1),(1,0)`, each
having determinant -1. Embedding on any ordered distinct coordinate tuple is
permutation conjugacy with identity on its complement. Consequently a legal
normalized word satisfies

    det(G) = (-1)^(n_neg+n_swap).                    (P)

The proposed orientation certificate retains actual primitive columns/receipt
hash, native source binding, legal normalized temporal word, coordinate
validation, and the structural parity derivation. It never accepts an incoming
unproved `determinant=+1`, gate-name assertion, phase-index assertion, or cached
count unrelated to the replayed word. Counts/parity are exact syntactic
bookkeeping, separately labelled; they are not presented as an executed
generic determinant or a BRC spectral calculation.

`FixedRotor` gives an independent family-level consistency check: the temporal
word is `word + D + reverse(word) + D`, representing
`D_0 G_0^T D_0 G_0`. Each orthogonal determinant occurs in a pair, so the product
has determinant +1. Quarter turn is a swap followed by one negation, also +1.
The generic admission must still bind the actual complete word; it cannot
trust an object merely because it was called FixedRotor. In particular a
`CompleteNativeWord` accepts legal det-minus-one words too.

### Inverse and codec reuse

For G inverse equal to G^T, `2I-G-G^T` and the trace are unchanged. A single
bound therefore covers both directions. Complete forward and inverse columns,
transpose equality and inverse recovery remain in the native admission; reuse
is not permission to skip those source checks. An optional `inverse=True`
lookup may return the same bound/word-pair certificate with its direction
binding. It must not claim that forward and inverse matrices themselves equal.

Compute the trace on all 61 columns, including residual diagonal entries.
The codec may be used only after full forward/inverse block admission. The
current codec additionally proves identity on the complement, so its trace
defect equals the restricted trace defect; the new bank need not depend on
that shortcut. A six-dimensional trace without the complement proof is not
an acceptable substitute.

## 3. Concrete cheaper observation profile

Retain the old cold path's fresh `CompleteNativeWord` construction with the
replay cache explicitly cleared, all 61 forward/inverse/recovery basis tests,
program-to-replay equality, sparse application cache binding, complete
phase-binding comparison, and codec revalidation. Primitive orthogonality plus
actual word replay already proves complete orthogonality. This is the reason
the new profile can omit the old extra signed orthogonality-residual matrix;
it is not a claim that the raw host dot-product test alone supplies native
provenance. Keep the inherited dot-product/transpose checks unchanged.

Remove the separately stored/observed `I_minus_G`, B, and `B^2-sB` matrices.
Instead select one deterministic, source-bound trace evaluation profile:

    TRACE_BALANCED_DYADIC_V1:
    d_j := observe((1), (-1,G_jj)), j=0,...,60;
    sum these 61 values by a fixed balanced binary tree of signed observers;
    carry an unpaired node unchanged, with a structural reference;
    t_G := the final actual observed value;
    observe(4-t_G) to choose min(4,t_G) for SO;
    s := the chosen observed value t_G or literal universal bound 4.

Each observation has at most two additive terms and at most two factors per
term, so its positive-path graph has at most five states and depth two.
Duplicate **identical signed factor sequences** may share a receipt, as in
the frozen `SignedExpressions`; equal numerical results alone may not share
unrelated provenance. Every diagonal and tree node retains its source indices
and receipt/reference. Before caching this uses at most 61 deficit plus 60
sum plus one clipping-margin observations for an SO word. These are count
bounds, not predictions of actual new core calls or wall time. Empty/zero
expressions still require the selected profile's actual observed zero receipt.

Alternatively one trace graph could sum 62 terms at once, but it has 65 states
at depth two. Fewer observer invocations need not be cheaper inside the actual
kernel. The bounded first implementation should use the fixed small-fanin
profile and report both graph sizes and invocation counts; it must not call a
large graph automatically faster.

All scientific scalar additions, products used by the certificate, and its
clipping comparison are returned by `PositivePathObserver`. Fraction objects
only encode actual column values, exact denominators, and independent identity
checks. The existing scalar range checks inspect actual signed endpoints. For
the known det-minus-one profile, the exact literal bound 4 follows structurally;
an optional diagnostic trace is paid separately and not required to establish
that bound. Unknown-orientation fallback, if later implemented, observes
`2t_G` and its clipping margin explicitly.

The uniform policy's existing actual signed test remains

    8s-s^2-16e^2 <= 0,      0<=s<=4, 0<=e<=1.          (C)

It controls `sqrt(s/2-s^2/16)`, which is increasing on [0,4]. It must not be
applied to an unclipped value above 4. The no-new-prefix-covariance property
must remain explicit; probability/Gram queries are otherwise unchanged.

## 4. New bank schema and strict restore

Suggested independent module/class: `so_trace_certificates.py::SOTraceBank`.
Do not subclass the frozen bank solely to slip through its exact-type gate.
Suggested immutable record:

    SOTraceRecord(phase_index, s, bound_valid, bound_method,
                  bound_is_exact, certificate_sha256)

Methods remain `check(program)`, `get(m)`, `evidence()`, and
`restore(program,evidence)`. An inverse lookup may be added explicitly.
New logical schemas should be separate, for example
`BRC_COMPLETE_NATIVE_TRACE_BOUND_V1` and `BRC_SO_TRACE_BANK_V1`.

Required logical fields: full carrier dimension; exact normalized word and
forward/inverse column hashes and denominator; complete native replay binding;
actual primitive/source binding and orientation derivation; trace profile,
diagonal/tree observation references and signed receipts; actual t_G where
observed; clipping branch; method and scalar s; bound-valid/exactness flags;
codec binding; and implementation/source hashes. Bank identity still excludes
N, a, work powers and history, since this bound concerns only the complete
words. Program admission for those fields remains a separate dependency.

`bound_valid` means a proved squared-norm upper bound. It does not mean the
policy will omit the word. `bound_is_exact` is false for generic SO trace
bounds, true for the certified negative-det branch, and true at certified
t_G=0. The old rank-two bank's `accepted` and
`norm_squared_equals_s_if_accepted` must not be silently reused with the new
meaning. A legacy-shaped `.accepted` alias, if absolutely needed, belongs only
to the new versioned interface and must mean `bound_valid`, with explicit
method/exactness fields in every record.

Restore first validates strict object/field types (not bool-as-int), phase keys,
word coordinates, rational-string encoding, schema and hash. It then performs
fresh native word admission and the complete chosen observation profile and
compares canonical logical bytes. Rehashing a changed scalar, orientation,
receipt, column, codec or boolean must not make it admissible. Reject duplicate
JSON keys if raw JSON text is accepted. Dynamic timings/cache indices/call IDs
are not logical identity; return the new replay's real setup receipts. A
failed fresh replay retains its evidence and billed work, as the current
`CertificateReplayError` does. Hash validation alone is never admission.

Trusted in-process checks may reuse the immutable bank after complete binding
checks; scientific setup and warm host checks stay separate in the accounting.
The existing ordinary trusted-Python/no-monkeypatch boundary remains explicit.

## 5. Minimum uniform/boundary integration

The frozen `UniformFeedbackGram.__init__` requires
`type(bank) is WordCertificateBank`, and the frozen boundary's outer check
repeats that requirement. Therefore merely passing the new bank cannot work;
weakening these old guards or monkeypatching their module globals is excluded.

Implement a separate `SOTraceUniformFeedbackGram` from the frozen adaptive
transaction base, with the short frozen uniform `prepare_next` logic copied
and source-attributed. Its only policy-level changes are: require exact
`SOTraceBank` type, require `record.bound_valid`, and bind the new bound method
and schema. Preserve the ordered oldest-word candidate, remaining-budget
charge, reference fallback, zero-mass semantics and actual test (C). If using
the boundary guard, implement a new versioned boundary subclass around this
new uniform class; its full checks require `SOTraceBank`. Retain the internal
adaptive snapshot/committed-ledger checks and synchronous outer guard contract.
No compatibility adapter may assert an instance has the old exact type.

Give the new policy, cursor schema, source hash and bank hash distinct names.
Strict restore deterministically replays history and the pending decision
through the new class. Old uniform/boundary cursors are intentionally rejected;
matching honest selected words, charges and probabilities can be compared,
but old/new certificate hashes and serialized ledger bytes need not match.
Rollback, pending same-bit retry, failed replay evidence and detached interim
snapshots must remain as in the validated transaction contract. Guard-depth
unwinding does not add a KeyboardInterrupt ledger-rollback promise.

For the existing three rank-two words, the old successful witness proves its
s equals `D-trG`; the new SO value is therefore the same after clipping.
Provided their actual native orientation is checked, the same uniform
decisions are expected. This is a mathematical equivalence, not a new run.
For other SO words the new method can validate a bound although the old
rank-two equation fails. The resulting changed decision is a new valid policy
outcome, not a claim that the old algorithm executed it.

## 6. Small executable next fixture and accounting

First implement only the new bank and a bounded checker:

1. Reuse one admitted t4 bank with actual m2/m3/m4 words. Build new cold bank
   at full D61 and with the existing six-coordinate codec. Compare bound
   values with the frozen old records and with one paid old bank build if a
   same-process cold comparison is needed. Keep all three actual scalar
   receipts; do not substitute the recorded old values for observation.
2. Add empty identity, single-coordinate negation, and the legal two-plane
   word `swap(0,1),neg(1),swap(2,3),neg(3)` as bank-only fixtures. They test
   respectively SO bound0, negative-det exact4, and SO bound4 that is valid
   but not exact (the actual two quarter turns have squared norm2). The last
   case does not satisfy the old `B^2=4B` witness. These are symbolic expected
   results until their native run; none implies useful omission at budget1/3.
3. Verify inverse sharing from actual bound forward/inverse columns. Reject
   wrong/rehashed parity, primitive binding, scalar, clipping branch, receipt,
   residual column, codec, bool phase and bool-valid-as-int. Invalid gate
   indices/duplicate coordinates fail before propagation. Test a truthful
   det-minus-one record at scalar2 is rejected even if its hash is recomputed.
4. Once the bank passes, run one old/new matched positive history1000 on
   N21/a2/t4 and optionally N21/a4/t4 with epsilon1/3. Compare conditional
   masses/full signed covariances, selected IDs/charges and raw mass, while
   explicitly allowing the new certificate hashes. Restore/retry at a pending
   prefix and reject old schema. This does not require another four-fixture
   complete-law run: the arithmetic/transaction code and conditional proof
   should be reviewed first, and further runs justified by actual differences.

Cold setup records complete native basis actions, primitive/replay cache state,
signed observer graph sizes/depth/term counts, all core receipts, rational
numerator/denominator sizes, serialization sizes and wall time. Count native
column work even when a low-level primitive cache adds zero new core calls.
Warm costs separately include full provenance checks, bound lookups, guards and
the unchanged actual scalar policy test. Gram requests, cache matrices, phase
vector actions, modular-table digit work and history comparisons remain their
own categories; share tables without double-counting cumulative reports.

The new bank stores O(D) scalar trace nodes in place of four extra D-by-D
witness matrices, while full forward/inverse columns remain O(D^2). This is a
proposed certificate-representation reduction. Its total speedup is unmeasured:
full-word replay, kernel graph behavior and strict metadata checks may dominate.
Use paired serial old/new order if measuring; source/evidence serialization
and cold versus warm paths must not be conflated. There is no change to the
large-work-support or general Shor complexity limitation.

## 7. Exact next implementation boundary

The next authorized scientific unit can implement `SOTraceBank` with the
fixed small-fanin trace profile, preserving fresh full-column/codec admission,
then execute only the bank fixtures above. The uniform integration follows
after source review of its exact-type/schema boundary. Gershgorin refinement,
multiple omissions, reduced-carrier-only trace and a generic determinant
algorithm are deliberately outside this minimum design.
