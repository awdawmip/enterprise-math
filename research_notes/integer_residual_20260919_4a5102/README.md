# Integer + typed residual refactor candidate

Status: CANDIDATE / LOCAL_SLICE_VALIDATED / NOT_FULL_REPOSITORY_MIGRATION.
Researcher-ID: EM-DIRECT-4A5102. Research-Activity-ID: RA-1094DE57986E6E3FDCEA65DA.

This directory is a self-contained, executable source slice. From this directory run `python tools/run_validation.py` and `python tools/audit_numeric_surface.py src/enterprise_math --output evidence/ast_audit.json`. Python 3.13.5 was actually used: 31 tests, 29,412 enumerated/random parameter cases, zero failures/errors/skips. These are implementer-run finite checks, not independent researcher acceptance, formal proof, or full-repository regression.

The original core.py, division.py and exact_arithmetic.py are reused byte-for-byte from awdawmip/enterprise-math@a6ef14fdc1dec284f9ca40875ae3acfb85e1b4b7. The isolated __init__.py MUST NOT replace the production package initializer. Production consumers have not been switched. This source snapshot is a recoverable candidate, not Foundation promotion, Working Truth or a formal task/CLAIM.

The exact rational readout obeys S*n=d*q+r, 0<=r<d, x=q/S+r/(d*S). Negative values use floor division. Refinement is q_new=t*q+floor(t*r/d), r_new=(t*r) mod d, S_new=t*S. Arithmetic reads the exact source instead of feeding back a truncated value.

RootResidual keeps n*S**p=k**p+R; R is a polynomial residual, not an additive root tail. RationalInterval returns UNKNOWN for unresolved overlap. PhaseLabel retains exact rational turns and original winding, but is not a complex amplitude or QFT implementation. NativeProjection6 retains six integer coordinates, literal denominator, common depth and caller-owned path key; it does not define a new native metric, direction or rotation. Origin preserves scalar expression order only, not complete native trajectories or authenticated provenance.

Literal source identity stays separate from the reduced rational value observer: 2/4 and 1/2 may have the same value without representing the same native state or history. Scalar JSON readouts use integer strings and explicitly do not serialize the full path graph. Existing Fraction arithmetic is exact and is not automatically an error; the new constructor requires an explicit integer-pair adapter, never a float roundtrip. Positive-weight BRC is not complex phase cancellation.

The reciprocal 1/7 test obtains digits 142857 from residues 1,3,2,6,4,5,1. The modular refinement test checks a**t mod N for 400 finite parameter cases. Neither result claims a fast order-finding algorithm or an efficient classical Shor simulation. Exactness does not bound bit growth or branch count.

Next unfinished unit: scan the complete current working tree, classify actual approximate consumers, connect the adapter to the first real research flow, and run that flow's original regressions. Do not reimplement the three already verified upstream files. General algebraic closure, rotations, transcendental bounds, complex amplitudes, native path-owner integration and full migration remain unfinished. Incomplete GitHub search results are not a no-float inventory. Old float-only inputs cannot recover intended exact source values without original integers/text/expressions.

The user-delivered standalone Git bundle additionally contains the Chinese design/migration README, policy, source manifests, local logs and an additive integration.patch. Its standalone commit is 7f5e275956d80dc977f453552b02c602c112de7b; bundle SHA-256 is 30448ba2d15141930aa0a49fe3f5ac3eb45ce518ad52a0ac10795295500b7274. This is not a claim that the binary bundle itself is stored at this GitHub path.
