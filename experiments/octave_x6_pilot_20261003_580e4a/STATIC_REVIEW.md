# Pre-execution static review

Scope: source inspection and syntax-only validation. No motion simulation,
fitting, BRC propagation, or numerical result has run at this checkpoint.

An independent static pass identified and the author corrected:

- Initialization confounding: add full/diagonal matched-quantized-initial controls
- Missing float holdouts: score all four unseen initial states separately
- Misreading resolution: label retained-model delta sweep initial-grid convergence
- Smoke/full overwrite: isolate smoke output and require fresh full-run directory
- Stale status/provenance: run-ID-bound states, input/output hash verification,
  full-horizon and finite-value checks, final status after plot completion
- False success after errors: caps are BOUNDED_PARTIAL; certificate/data errors FAIL
- Cost labeling: distinguish total validation-pipeline cost and component timers
- Residual naming: squared local rounding error is not called physical energy
- Resource scope: soft cooperative walltime limits and retained-fraction bit cap
- Phase aliasing: retain wrapped proxy and aligned unwrapped final drift
- OOD exchange: scale coupling consistently with the changed evaluation K
- Python optimized mode: rejected, because the certificates use assertions
- Source integrity: four canonical dependency files have exact Git blob/SHA256
  manifest entries and are checked before the scientific run

Python syntax compilation and Bash syntax checking passed. GNU Octave has not
parsed or executed the scripts yet; Octave-specific runtime behavior, actual
truth tolerances, fit conditioning, exact-run costs, output images, and all
quantitative claims remain unverified. No static review is described as a
scientific PASS or as independent empirical validation.

The mathematical scope stays narrow: the integer decomposition preserves a
chosen rational AR2 response and is exactly equivalent to its undecomposed
representation. The experiment does not derive a unique native physical kernel
or confer Foundation acceptance. Resolution repeats are paired conditions; only
two initial states receive exact certificates and only one noise realization is
tested in this pilot.
