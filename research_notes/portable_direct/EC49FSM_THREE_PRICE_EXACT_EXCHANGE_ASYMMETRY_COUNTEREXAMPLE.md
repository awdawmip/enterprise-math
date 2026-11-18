# EC49FSM — exact three-price counterexample to q32/q34 exchange symmetry

Source: frozen BRC16943 input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; 141 named states, 310 original configurations and 228 physically named observations. All prices are normalized by baseline t>0; q32 discount a, q34 discount b, q140 discount z. Uniform prior, exact complete adaptive native identification trees. Define `F(a,b,z)=141V(a,b,z)/t`.

**Exact counterexample:**

| (a,b,z) | Exact global Bellman F | Optimal root | (U,N32,N34,N140) | independently checked Bellman state count |
|---|---:|---:|---|---:|
| (3/4,1/2,1/2) | 693/4 | q32 | (320,141,60,22) | 7421 |
| (1/2,3/4,1/2) | 663/4 | q34 | (311,28,141,51) | 7189 |

Both entries were computed by exact integer-scaled full 228-observer Bellman dynamic programming and independently verified by a second frozen-input decoding/DP implementation. Witness affine costs replay directly:
`320 - (3/4)141 - (1/2)60 - (1/2)22 = 693/4`,
`311 - (1/2)28 - (3/4)141 - (1/2)51 = 663/4`.
The enumerated Bellman lower bounds coincide with these complete-tree witnesses, so the listed values are global finite-instance optima.

Their difference is exactly `15/2`. Consequently,
`F(3/4,1/2,1/2) != F(1/2,3/4,1/2)`.
Thus swapping q32 and q34 discounts is **not** an invariance of the original BRC16943 model once q140 has an independent discount. In particular, a three-price solution cannot generally be obtained by replacing (a,b) with merely their minimum and maximum, nor by directly reusing the earlier two-observer symmetric saturation formula.

As a control comparison at z=0, exact Bellman gives equal values `F(3/4,1/2,0)=F(1/2,3/4,0)=719/4` with respective roots q32 and q34. The q140 price perturbation differentiates the original named q32/q34 observation relationships. This is a finite-instance exact asymmetry statement; no global description of the three-dimensional phase diagram is claimed.

Reproduce using `EC49FSA_THREE_OBSERVER_SOLVER.solve({32:a,34:b,140:z})` and independently `EC49FSA_FSB_INDEPENDENT_CHECK.certify(...)`, retaining the frozen source files shipped with the EC49FSL local package. Independent values are checked at exact rational arithmetic, not floating point.

Next: identify the exact q140-discount threshold at which `F(3/4,1/2,z)` and `F(1/2,3/4,z)` first separate and prove the full finite breakpoint partitions for these two directed lines.

Research status `AUTHOR_PROVED / EXACT_FINITE_CROSSCHECKED / NOT_REVIEWED`. This portable scientific note does not assert a canonical CLAIM, Activity checkpoint, Result or Review.
