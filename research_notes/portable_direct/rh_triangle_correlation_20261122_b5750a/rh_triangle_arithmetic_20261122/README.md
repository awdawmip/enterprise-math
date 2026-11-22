# Triangle arithmetic / local phase correction

Same-author continuation of `EM-DIRECT-B5750A / TASK_RESEARCH`, Activity `RA-60C6D083A81B19084A74C5BA`. No remote writes or independent review.

- `TRIANGLE_KERNEL_AND_PHASE_COMMUTATION.md`: proofs of the rational divisor kernel, hyperbola form, centered kernel bound, phase/elimination commutation, tree biorthogonality, exact Dirichlet correction cost, local weighted trace bound, and shifted phase Gram.
- `verify_triangle_arithmetic.py`: exact rational checks plus a cache-free certificate for the actual uniform `H=256` phase correction on the new dyadic-local tree.
- `triangle_arithmetic_certificate.json`: all finite outputs, coefficient/sample inputs, exact interval endpoints, local costs and input hashes.

Run from the enclosing research workspace:

```bash
python rh_triangle_arithmetic_20261122/verify_triangle_arithmetic.py
```

Required source files:

- `rh_correlation_rational/certify_matched_nodes.py`
- `rh_correlation_rational/rational_window_certificate.json`
- `rh_triangle_certificate_20261122/dyadic_triangle_certificate.json`

The script recomputes only the complete road prefix through 256, then evaluates phase values at the 44 fixed nodes. It does not read the large scratch pickle and does not regenerate the full road through 32768. Ordinary Python standard-library arithmetic suffices. Runtime in this session was approximately 1.4 seconds.

The actual squared local correction norm is approximately `0.0001600487158140`; its local Green-trace bound is approximately `0.0007085288710058`. Preserving all dyadic skeleton values did not reduce the correction norm in this finite case. The mixed-cutoff interface is proved but no adaptive cutoff optimization has been implemented. No asymptotic arithmetic cancellation is claimed.
