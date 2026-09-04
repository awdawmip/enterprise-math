# BRC rotation-atlas research reference

Read REPORT.md first for theorem proofs, mathematical typing, and limitations.
This is a research extension, not a replacement of the repository's Boolean BRC.

## Run

Use Python 3.10 or newer and SymPy. The executed version was SymPy 1.14.0.

```bash
python -m pip install sympy==1.14.0
python check_brc_atlas.py --output verification.json
```

Run without `-O` because the verification script uses assertions. No network or
repository checkout is needed during tests. All checks are exact. Runtime depends
on hardware. `elapsed_seconds` is informational and is not a proof datum.

## Files

- `atlas_brc.py`: constant-arithmetic optimal chart-fibre compiler, frame-aware
  positive histogram algebra, exact compression carry, scoped sector norm,
  finite-frame commutative transfer lift.
- `generic_atoms.py`: automatic exact Q(parameters)[y] valuation atoms, structural
  verifier, parameter-permutation action, sparse regular guards, rational
  specialization with explicit collision refusals.
- `check_brc_atlas.py`: deterministic replay with independent brute-force, exact
  LP, FCC rotation and previous polynomial-kernel comparisons.
- `factor_atoms.py`, `pinned_polynomial_kernel.py`: unchanged predecessor code,
  reused as the independent rational-polynomial reference.
- `verification.json`: actual observed output, not CI or Lean certification.
- `HANDOFF.json`: immutable GitHub source locator and content identities.

The full chart fibre is stored by constraints. Optional enumeration is bounded.
Multiple chart gauges are NOT additional physical paths. Six trace variables
are NOT an assertion that all N^6 are legal primitive native Cell addresses.
`length` stores operation count, NOT the complete original time history.
`Guard.polynomial` may expand a large product; ordinary checks use sparse factors.
The two-active-axis norm interface deliberately rejects undeclared global usage.
