# General two-bit scalar counting: a fixed-dimensional route

This symbolic unit gives an exact polynomial-bit complexity route for a scalar
coefficient with two signed bits and an arbitrary supplied modulus R. It removes
the earlier divisibility restriction at the level of an abstract algorithm by
reducing the problem to established fixed-dimensional lattice-point counting.
It does not add an executable BRC counting backend.

MIXED_MOMENT_LATTICE_REDUCTION.md contains two explicit reductions. The first
turns each mixed-floor monomial into an unweighted count in at most eight
dimensions with at most sixteen inequalities. The second partitions pair
assignments: two selected bits need sixteen counts in dimension six. For any
fixed number h of selected bits, the latter uses 4^h counts in dimension 2+2h.
The classical polynomial-bit consequence follows from the cited Barvinok–Woods
theorem for fixed dimension and the proved input/output length bounds. It is
not a claim that those constants are small or that a practical speedup was
measured. Growing h is outside this polynomial bound; no impossibility result
is inferred for that case.

The scalar contract retains both displacement orientations, their exact
multiplicity, and the external raw scale 4^-g. Supplied modulus and residue are
counting inputs, not free order or target-address discovery. Scalar Walsh
weights do not replace arbitrary chronological noncommuting matrix products.
One fast coefficient does not bound the number of Gram queries or implement
the complete QFT/Shor output distribution.

This package contains the proof, scoped primary-paper reading record and
source-specific shared-context review, together with portable continuation and
dependency instructions. The reviewer found no substantive error within the
stated symbolic scope. This is not formal independent admission. No scientific
arithmetic, host numerical experiment, lattice backend invocation or new paid
professional query was performed for this unit.

READING_EVIDENCE.json records the root author's actual reading of selected
sections of Barvinok and Woods, *Short rational generating functions for lattice
point problems*, arXiv:math/0211146v1. It does not claim a local PDF-byte hash,
full-paper reading, or a separate reading of the earlier BP99 proof cited by
that paper. The application is not presented as a literature-first result.

The inherited two-bit proof and its review are available byte-for-byte in
published hybrid source 55e8e66b76d062c6c72432f0f5b364c3e9b1bba8. Their earlier
missing mixed-floor evaluator remains unimplemented by the current typed code;
the new theorem-based route bypasses that recurrence rather than implementing
it. See DEPENDENCIES.md and CONTINUE.md for precise source pins and next steps.

This is a zero-gzip symbolic package. An empty readable-evidence index means
there are no new binary scientific results to restore. The delivery ZIP holds
all selected text sources and an exact member index, with no fabricated run,
native cost, startup receipt or raw scientific payload. Publication and original
Drive-byte verification are recorded separately after those actions occur.
The research goal remains active and P000 is unchanged.

Global-Knowledge-Sync: main@a3609ca / GLOBAL_KNOWLEDGE_V1
