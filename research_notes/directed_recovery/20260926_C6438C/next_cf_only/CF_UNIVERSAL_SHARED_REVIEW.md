# Shared-context check of the CF-only all-width support proof and driver

Status: AUTHOR SHARED-CONTEXT STATIC/SYMBOLIC CHECK / UNREVIEWED / NOT_ADMITTED.
Activity RA-CAAAC604CB513AEA8BBC1DFC; researcher EM-DIRECT-C6438C.
This is not an independent review, formal proof certificate or new execution.

The root requested a separate same-context check of the denominator bound,
continued-fraction candidate boundary, pure-two-power case and retry semantics.
The following files were read completely at these SHA256 values:

- ROOT_CF_ALL_WIDTH_SUCCESS.md:
  d51885d7fd5440fb2f2636f7c0559f9c348a0e5015f9a297ecd7daa1b20b1a17
- POWER_OF_TWO_ANALYSIS.md:
  149b58c3ddc1a7d2cc503a38e8e9046104fd6dc969159e187d15750dadc276af
- PHASE_PRODUCT_STRUCTURE.md:
  18798bc7ddf23bb9fc263870d94567ca359e4ae3f95b53337f5319f38fd93590
- cf_universal_factorization.py:
  23b683976b30953fe275b71202022df272a29a0d9d97f05e361aad3afa5ed8dd
- check_cf_universal.py:
  dde63b267a1fc3cc3154c4b523cd69e37b71c17e53f8a4d9075b6696fbc3fef9

The inherited complete_factorization/general_streaming/general_driver and both
typed precheck/success contracts had also been read in the earlier same-session
integration check. No reviewed implementation was modified by this review.

## Findings

No substantive logical or implementation defect was found in the scoped claim.
In particular:

1. The near-rank-two argument uses the complete rational orthogonal matrix. At
   most two eigenvalues can have distance from 1 above eta. A cyclotomic factor
   of degree at least four would have nonzero integer Phi_L(1) bounded strictly
   below one. The argument does not confuse two clean input columns with the
   full residual carrier, nor assume actual phase words commute.

2. In the odd-part-three nearest-history identity, the outcome sign supplies
   the next low bit correctly. The conjugate-plane factor is
   `1+mu_i^2 exp(-i alpha_i)`, not an expression with an omitted sign. For
   i>=2, |alpha_i|<=pi/12; the weaker pi/6 margin still gives smallest singular
   value greater than 1/2 when mu has order three or six. The comparison with
   the complete ideal feedback must use **185/2^32**, including the K33 omitted
   tail. The reviewed proof does so; 177/2^32 is used only for the truncated
   planar comparison. The first two rounds and order-at-least-twelve case are
   handled separately and do not rely on that small-angle margin.

3. For pure-two-power order, the first t-s bits are forced zero, the next bit is
   exactly fair and has no active phase history, and later complete instruments
   preserve its total mass. The odd reduced numerator case has denominator r;
   the even case has denominator below r. Hence good-base CF success is exactly
   1/2, on the admitted even-width contract. This does not assert that every
   lattice output is positive or ideal-uniform.

4. In the other classes, Q>=N^2>r^2 gives the strict continued-fraction
   approximation criterion. The relevant denominator r satisfies r<=N-1 and
   is therefore within the real generator cap. Earlier convergent denominators
   are smaller (an initial duplicate 1 is harmless); none can be a positive
   multiple of the minimal order. No unknown order or nearest-good k is passed
   to the runtime.

5. B(t) is a bound on one common dyadic denominator of the complete real
   unnormalized terminal coordinates. Both H4 operations per round and all
   possible retained phase positions are counted; common-factor reduction can
   only lower the exponent. Nonzero actual vector therefore gives mass at least
   2^(-2B). The proof-only primitive spectral component is used to establish
   nonzero support, so a further factor 1/r must not be charged to the real
   coordinate lower bound. The reviewed proof avoids double counting it.

6. The new driver pins the K33 provider and calls the unchanged sparse CF
   postprocessor through general_driver. It does not import the hybrid
   postprocessor. The support lower bound is strictly positive for every finite
   admitted width, and choosing the larger of it and the existing uniform TV
   success bound is valid. The integer attempt count implements
   ceil(1/gamma)*node_bits. With node_bits=s+ceil(log2 n_initial), at most
   floor(log2 N)-1 random split nodes, the union allocation is conservative.

7. Explicit base policy or a smaller attempt cap does not inherit the default
   uniform-random guarantee. Source exhaustion, zero phase, bad-base failure
   and retry exhaustion retain partial/unresolved results. Wilson certificates,
   perfect-power multiplicity, even factors and typed product conservation are
   still required; retry failure does not become primality.

8. Deterministic result replay now reports stochastic_budget_verified=false,
   making clear that its verified flag covers prime/product claims rather than
   independently replaying probability statements or proving RNG uniformity.

The local test script visibly exercises original-CF success, unchanged zero
readout, bad-base partial output, EOF without fabricated postprocessing, and
rejection of hidden unresolved factors. This review did not rerun those tests;
their real execution and receipts are the root's separate evidence.

## Retained limits

The conclusion is positive support and a finite conditional retry guarantee for
the specified compiled K33 algorithm. It is not a claim of polynomial classical
factoring time, practical performance at arbitrary input sizes, physical Born
sampling, independently admitted mathematics, or uniformly small ideal-Shor TV
at every width. Those limitations do not negate the scoped correctness claim.

The previously proposed finite-field determinant observer is preserved only as
FINITE_FIELD_OBSERVER_PLAN.md. No 176-mask enumeration or determinant
computation was started, and the symbolic CF-only proof does not depend on it.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1

## Final pre-freeze addendum (2026-09-26)

The historical hashes above are retained. The final changed files were checked:
`PHASE_PRODUCT_STRUCTURE.md` SHA256
`65a16d2aa2cad9427318be5e0bb56c83ed4b6684636c19f5745c9eb041a75baa`
adds the scoped d=3 closure reference to `ROOT_CF_ALL_WIDTH_SUCCESS.md` without
changing its phase-product lemmas or claiming arbitrary-history Phi3/Phi6
exclusion; `check_cf_universal.py` SHA256
`7a7e6306b6b092207ba1a559d2e3c31237244f800c540f626eefa1b4bfafdeac`
adds the N=55, fixed-base-2 fixture with factors 5 and 11. The recorded final
summary has 5 COMPLETE and 3 PARTIAL examples, 20 actual BRC calls, and the
`hide_unresolved_rejected` negative control. These changes do not alter the
review conclusions. This remains a shared-context author review, not an
independent scientific admission.
