# R9 exact carrier-guard information contract

Task: `RS-CFD-SPECTRAL-HYBRID-20260910`

## Statement
Let `C` be the certified finite Fourier carrier and let `x` be a mutable coefficient array. The exact step-boundary predicate needed by R8 is only

`support(x) subseteq C  <=>  for every i notin C, x[i] == 0`.

Therefore coefficients inside `C` carry no information for this route decision.

### Worst-case lower bound
In a deterministic exact black-box coefficient-query model with no trusted write barrier, dirty bit, mutation log, or stronger host attestation, every coefficient in `C^c` must be queried in the worst case. If one outside coefficient `j` is not queried, the all-zero outside state and an otherwise identical state with one nonzero coefficient at `j` are observationally indistinguishable to the guard but require opposite routing decisions.

For independently mutable state and Source arrays, the lower bound is consequently `2|C^c|` outside-coefficient value queries per pre-`integrate()` certificate. R8's two-object boundary is thus minimal in *mutable objects*; reducing from state+Source to Source-only requires an additional state-preservation contract such as R7. This is a finite-array route theorem, not a PDE theorem.

## Implementation distinction
Logical query optimality does not imply fastest NumPy memory traffic. R8's reference checker uses boolean complement indexing (`x[mask] != 0`), which is exact but materializes/gathers the outside subset. A contiguous whole-array predicate (`(x != 0) & outside_mask`) examines mathematically irrelevant inside-carrier coefficients but can stream memory more efficiently. A compiled loop can preserve complement-only value reads without NumPy gather allocation.

The local deterministic benchmark therefore compares all three exact implementations; it does not infer native spectralDNS speedup.

## Activation boundary
This theorem assumes the R8 synchronous boundary: state and Source are certified immediately before `integrate()`, no external mutation occurs during the fixed RK4 call, and arbitrary ordinary between-step mutation is allowed because the next boundary rescans both. As in R8, custom/asynchronous mid-stage mutation invalidates the certificate.

## Native-host consequence
For the intended sparse-carrier regime, do not select a guard implementation from logical scan counts alone. Benchmark at least the existing boolean-complement implementation and a contiguous/compiled exact predicate inside the pinned native host, while retaining unchanged dense callback, Nyquist, pressure/diffusion, RK4 and fallback semantics.
