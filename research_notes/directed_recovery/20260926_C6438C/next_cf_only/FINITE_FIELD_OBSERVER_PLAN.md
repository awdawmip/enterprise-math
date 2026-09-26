# Deferred alternative: finite-field observation of actual native phase words

Status: DESIGN_ONLY / NOT_EXECUTED / SHARED_CONTEXT / NOT_ADMITTED.
Activity RA-CAAAC604CB513AEA8BBC1DFC; researcher EM-DIRECT-C6438C.

This plan was retained when the CF-only symbolic support proof made the
proposed 176-case enumeration unnecessary. No finite-field phase matrix,
determinant or candidate-mask enumeration was executed for this file. No
published support, phase, completion or sparse artifact was changed.

## Constraint check

The full BRC-only Markdown and JSON were read at Source
f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf: Git blobs
787e74952765b61904f2bd67038291f5f081af83 and
62ffa6bbdafd54496e27284a26a2aeaf2d04df99. They require actual typed BRC
computation and permit a proved extension with retained source and composition/
observation correspondence. Integer arithmetic by itself is not sufficient.

Therefore the candidate observer would not use an external ordinary numerical
propagator, float, trigonometric input or ideal-QFT reference. Its input would be
the *complete actually executed native rational gate columns*, including all
residual input directions, not just their two clean logical columns.

The native phase module reconstructs each FixedRotor only after actual complete
word execution, exact equality with its dyadic macro columns, and complete
inverse recovery. That source link and all native receipts must accompany any
new certificate. The existing field and matrix routines described below are
only prospective derived observers of those certified columns.

## Typed scalar construction

For an odd prime p, construct modular successor on 0,...,p-1 from the already
actual BRC full-adder primitive and typed reduction from
sparse/sparse_modular.py and completion/typed_integer_prechecks.py. Retain every
digit/carry/reduction trace for the p successor transitions. Generate the entire
addition table by repeated certified successor, and multiplication table by
repeated certified addition. These are finite BRC compositions; retain their
table hashes, recursive source recipes and complete canonical tables.

Prove the table outputs are the quotient-ring operations by induction. Establish
the odd-prime premise with an exact typed primality certificate, for example the
already available Wilson interface. Build the nonzero inverse table by finding
and checking the unique product-table entry equal to 1; no ordinary inverse
routine needs to become a scientific arithmetic authority.

Reduce a nonnegative integer coefficient through its bit string using repeated
doubling and addition in the certified field tables. Retain sign as a separate
label and observe it through the additive-inverse table. For a dyadic native
coefficient a/2^b, use the certified inverse of 2 and the same product-table
composition. This proves the homomorphism

    rho_p : Z[1/2] -> F_p,  a/2^b -> rho_p(a) rho_p(2)^(-b).

Signed characters are observed, never replaced by positive mass. This observer
does not generate Shor amplitudes or a new physical evolution. It is leased only
to exact algebraic identities/nonvanishing of the supplied complete gate words.

## Ordered matrix observer

For every complete native gate column, record its exact source identity,
numerator/denominator hash, reduced F_p column and complete matrix hash. Matrix
addition/multiplication then use only the certified field tables; ring
homomorphism proves that observing a concatenation agrees with composing its
observed columns. This is the required BRC word/observer commuting relation,
not a generic matrix implementation relabeled BRC.

The current executor visits controls in increasing c and phase indices
m=i-c+1 in decreasing order. For a selected mask, start T=I and update
T <- V_m T while visiting m from 32 down to 2. Thus the final operator acting on
column vectors is V_2^epsilon2 V_3^epsilon3 ... V_32^epsilon32. The public mask
encoding is j=sum epsilon_m*2^(32-m). This ordering must be checked against the
then-current executor before any execution, even though ideal comparison
rotations commute. Actual phase words must not be reordered.

Compute T^2+T+I or T^2-T+I with the same table operations. Perform pivoted exact
finite-field elimination and retain row swaps, every pivot, multipliers, final
triangular matrix and determinant. If the determinant is nonzero modulo p,
the corresponding determinant over Q is nonzero: a zero element of Z[1/2]
would map to zero. A zero modular determinant is inconclusive, requiring another
odd prime or another proof; it must not be reported as a rational zero.

## Deferred masks, costs and replay boundary

The parent had supplied candidate windows
Phi3: 1431655722..1431655809 and Phi6: 715827839..715827926, totaling 176 masks.
This file does not certify that the windows exhaust all problematic masks. That
upstream geometric reduction would require its own audited proof and exact
index convention before this plan could justify a global conclusion.

For D=61, ordinary table-based dense composition and elimination require roughly
O(176*31*D^3) field operations if naively composing every word, reducible to
O(176*(31*D^2+D^3)) by reusing the already certified rank-one native gate-column
formula. The latter is of order tens of millions of finite table operations,
plus once-only native complete-column reconstruction. These are design operation
counts, not measured performance. Table construction uses O(p^2) entries; p=101
would be a modest first prime, with no assurance that every determinant is
nonzero there. No int64 or NumPy fast path should be introduced without proving
it realizes the same field-table observer and bounding every accumulation.

A future execution package should retain the constraint/source snapshots,
native gate bank payload checksum, field-construction certificates, mask/order,
all matrix hashes, LU traces, prime certificates and a replay script. The final
claim would cover exactly those masks and polynomials with nonzero witnesses;
it would not independently prove all histories, the candidate-window reduction,
Born semantics, performance or theorem admission.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1
