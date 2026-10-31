# PREFIX-405 execution, source, limitations, next unit

**Date:** 2026-11-01. **Scope:** external auxiliary static complex three-amplitude five-Port inverse model, normalized I1=1.

Frozen input snapshots:
- GLOBAL_KNOWLEDGE_V1: awdawmip/chatgpt-global-knowledge main@eeb6afada377b79c8148e040e1a5b74e00b436be.
- Enterprise Math: awdawmip/enterprise-math main@1fde72896593e8b10c9abb356983a265d2a4600f.
- Previous frontier: research_notes/2026-11-01_prefix404_dual_144_and_all_noisy_two_parameter_fiber.md.

**Actual execution:** Python 3.13.5 standard-library Fraction/isqrt checker (research_notes/prefix405_exact_solver.py) returned PASS_PREFIX405_COMPLETE_NO_SEMIDECISION_AND_ROBUST_NONCONVEXITY. It found the robust six-band NO with **two initial root boxes and two I4 exclusion leaves**, rechecked the NO partition with its own verifier, and recovered exact original complex Y witnesses in both signed YES bands. A distinct SymPy 1.14.0 checker (research_notes/prefix405_independent_sympy.py) reconstructed original A*A3^-1, checked the two observation vectors, midpoint, and strict rational margin, and returned PASS_PREFIX405_INDEPENDENT_ORIGINAL_MATRIX_AND_ROBUST_GAP.

**Exact evidence:** research_notes/prefix405_solver_output.json stores two leaf descriptors, verified YES source amplitudes and the exact margin 217169319/100000000. The generic finite NO certificate is reconstructible from the solver code, J2=[9999/10000,10001/10000], Cu=[19999/10000,20001/10000], J3=[0,1/10000], Cv=[9999/10000,10001/10000], J4=[40,42], J5=[22,23], root precision denominator 1000 and the two I4 leaves. The solver can exhaustively regenerate and check this result.

**Remote/source identity evidence:** Git blob SHA-1 of the actual locally executed source research_notes/prefix405_exact_solver.py is 53217652a2212b6d08a1f4c720f3dfea3fe6e643, and of the locally executed independent source research_notes/prefix405_independent_sympy.py is ccc1971e812bfc6480534ab99859c6f76de92de6. During publication these exact byte identities were checked against remote GitHub readback. The source bytes are separately SHA-256 ebdd19f6b9f85e69e705a81c25aa162d238668bd45c6840669be264953740128 and 85250d66e4bbbac843829d384b0e84116c7fc2a4733f320ef3c4d08cf7c4f4bc.

**Mathematical coverage:** The rational branch-and-bound method is sound for all rational finite six-band inputs, terminates on every NO input, and on every YES input possessing a strictly feasible source. A pure boundary-only YES may remain UNKNOWN; no general CAD has been executed and no bit-complexity claim is asserted. The open six-band NO witness and the nonconvexity midpoint are exact rational counterexamples. Numerical sampling was not substituted for interval proofs.

**Observer/BRC scope:** REUSE_APPLIED: keep full complex sources, branch labels and five original Ports plus both coherent readouts. No typed BRC operation or native P000 X6/the three-dimensional research slice bridge is claimed.

**Authority:** GitHub authorized account is awdawmip. Enterprise Math native service 0.6.11 replied research_authority_granted=false; current task/owner listing failed with CONTROL_QUOTA. This material is author-side research evidence only: UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING. It does not assert native CLAIM, Source Result, reviewer action or Foundation admission.

**PREFIX-406 next:** Build an actual complete exact YES witness generator for boundary-only algebraic sources (tangencies, collapsed bands, isolated irrational points), combine with the finite NO certificates, test generic 0-dimensional degeneracies and study mathematical/bit complexity. Preserve all observer/provenance branches and original model typing. The complete author-side Chinese proof, raw execution logs and local complete evidence archive are also retained in the run's evidence package.
