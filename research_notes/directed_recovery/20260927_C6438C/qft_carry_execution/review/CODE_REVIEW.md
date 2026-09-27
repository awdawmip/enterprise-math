# Carry executor source review

Status: FINAL SOURCE-SPECIFIC STATIC REVIEW; all three initial findings
below were resolved in the revised source and checked again. The original
findings are retained as review history, not current unresolved blockers.
No scientific execution, new ordinary matrix arithmetic or external query
was performed by this reviewer. Shared author context; not admission.

Initial source reviewed: `carry_executor.py`, SHA-256
`41e7691e99b768f05ce4943aa95ea8be86d760b5fa9a741b2db9c7861470622c`.
The inherited Gram/native/codec contracts and bounded fixture selection are
documented separately in `TEST_PLAN.md`.

## Correctness of the new recurrence

The high-to-low loop uses the correct carry equation and maps the old high
boundary carry to the new low boundary carry. It starts from the encoded
pure e0 projector in carry 0, keeps the alternative carry matrix distinct,
and returns only low carry 0. Each accepted local pair applies the current
complete feedback on the relevant sides, preserving the native gate tuple
order. The sign rule `history[j] and x != y` equals the product of the two
path signs; it correctly gives positive sign when both bits are one.

The inherited `_combine` contributes exactly one factor 1/4 per layer.
There is no second final division. Explicit zero matrices handle empty
contribution branches. Negative displacements use a transpose only after a
positive contraction. Bounds exclude both overflow endpoints +/-2^depth.
`sum_coefficients` uses the signed observer then multiplies the normalized
numerator by four to undo `_combine`'s recurrence-specific factor; this is
exact dyadic wiring even when normalization has removed factors of two.
Duplicate displacements are rejected, and the method explicitly does not
certify modular-list completeness.

No arithmetic or operator-order defect was found in those paths. This is a
source argument; actual full-entry comparisons still belong to the checker.

## Initial findings, subsequently resolved

1. **Bind the actual D61 execution caches.** `CompleteNativeWord.apply_numer`
   reads `_forward_nonzero` and `_inverse_nonzero`, while the initial
   `phase_snapshot` only captures `columns` and `inverse_columns`. Replacing
   an execution cache can therefore change the actual action without
   triggering `_check`. This needs no replacement of a Python method.
   Include the two immutable sparse execution tuples in the snapshot for
   D61 words, using a missing-value marker for the D6 restricted class.
   The executor need not defend against arbitrary hostile Python, but its
   advertised ordinary program-field guard should bind the fields actually
   consumed by native execution.

2. **Constrain the inherited public Gram route or label it honestly.**
   Inherited `gamma`, `mass`, `probabilities` and `advance` can still perform
   the old recursive cached computation, and `advance` changes the history
   while the carry contract fixes it. In particular, `evidence()` currently
   reports zero coefficient/cache entries unconditionally. Disable these
   public legacy entry points on the carry-only class, or expose and report
   their distinct behavior and cache size explicitly. The planned checker
   calling only coefficient/sum paths is unaffected by this API concern.

3. **Limit metric interpretation to observed objects.** Size observation
   happens at the seed, each completed boundary layer and the final sum.
   It does not measure transient native vectors or pre-cancellation terms;
   `max_numerator_bits` and `max_denominator_bits` must not be described as
   peaks over the whole execution. Also `coefficient_queries` includes the
   recursive positive dispatch of a negative input, so it is a method-call
   count, not the number of external requests. `positive_contractions`
   remains a direct count of actual carry contractions.

The initial module already limits its two-matrix slot measure by explicitly
excluding alternative terms, native temporaries and receipts. Keep this
qualification when reporting overall storage or comparing with old caches.

## Scope of later execution evidence

The most useful order control is the existing reachable N21/h101/i3/d7
case documented in the test plan. Its correct and reversed products have
equal traces but opposite signs at a retained residual matrix entry. Full
matrix equality, not just trace or next-bit probability equality, is needed.
At least one D61 result should be checked against two-sided embedding of
the exact D6 result after fresh admission of the complete phase bank.

Only files in the new `review/` directory are edited by this reviewer. The
executor, inherited frozen science, raw evidence and remote repositories
are not modified here.

## Final source and checker read

The final executor read has SHA-256
`f017b1fb1516e8faa97afd39d663e4eda6d21cad95f65bb2ccf5a79d7ff3b810`.
Both D61 execution tuples are now in `phase_snapshot`; the four public
legacy Gram routes raise; exported evidence calls `_check` and reports the
actual old cache length. Bit metrics explicitly describe only completed
boundaries and sums. Recursive dispatch is identified as a method-call
count. These changes resolve the three findings above and the subsequent
request to guard evidence export.

The checker read has SHA-256
`9cfdf2287422653979dcf8d64d92c4ee236f6c3d5a080cf98cecb926bf8f2eca`.
Its explicit path reference applies the same admitted native words in
chronological order, keeps all residual coordinates, and applies the
single required factor `4^-depth` to outer products. The comparison uses
complete exact matrices. The D61 checks compare both explicit path sums
and the two-sided embedding `J C6 J^T`; native intermediate letters are
not assumed to stay in the six-dimensional word-boundary subspace.

The reachable N21/a2/history101/d7 order control is trace-blind but not
entry-blind: its correct and reversed products have equal diagonal entries
and opposite signs at entry (0,2). The checker explicitly asserts both
facts. The D61 `_forward_nonzero` mutation control is valid because the
actual word class permits assignment to that attribute; it restores the
original tuple after the expected guard rejection.

Assembled Gamma cases now compare parent mass with the old Gram route;
positive-mass depth-three cases additionally compare both next-bit masses
and probabilities through the same native signed observer. Zero parent
mass is explicitly undefined, and terminal cases have no next-bit query.
At the top level `gamma_cases[*].history` is the declared full four-bit
tape, while `depth` and the nested executor/Gram reports bind the actual
prefix `history[:depth]`. This is a labeling distinction, not a changed
history in the calculation. It was documented without modifying the
already running, source-bound checker.

The author-run summary reports 134 coefficient matrices, two complete
D61 matrices, ten assembled Gamma matrices, sixteen rejected negative
controls and 8,859 actual native core calls, with unchanged dependencies.
Its payload SHA-256 is
`df00de760c8ca3d69b4f1fdd869a9c3e298582c7ae72d4fa4bba24a760b7ed57`;
gzip SHA-256 is
`25f53b75d91f6601174783f9aaefc4d0f1f69d4ba85f9519ca5786c410e8c89e`.
These are the author's existing results read by this reviewer, not an
independent rerun. The checker code and reported scope are consistent;
no further substantive defect was found in the bounded path reviewed.

The separate alias completeness and verifier review is in
`ALIASES_REVIEW.md`. This review does not certify hostile Python monkeypatch
resistance, a generic simulator speedup, or independent admission.

Global-Knowledge-Sync: main@06788df / GLOBAL_KNOWLEDGE_V1
