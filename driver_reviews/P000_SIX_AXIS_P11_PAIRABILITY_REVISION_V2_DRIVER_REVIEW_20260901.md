# Driver Review — P000 P11 pairability-filtered collision revision V2

Driver-ID: `EM-DVR-WLE3X6`

Result: `RR-16ADB5F4DE72A332B509`  
Publication: `TP2-E899F20BC1B62973D07C`  
Disposition: `ACCEPTED`  
Destination: `FOLLOWUP_TASK / RS-P000-SIX-AXIS-P11-GENUINE-DOUBLETON-DIOPHANTINE-NORMAL-FORM / TP2-5774A7C199FB50588943`

## Verdict

Accept the Generation-2 revision at exactly the derived six-coordinate arithmetic strength returned.

The revision repairs the only load-bearing defect identified in Generation 1: combinatorial equal-`P11` packets must be filtered packetwise by the already-frozen integer pairability predicate before they are counted as actual arithmetic states. The corrected residual information law is

`I_selector(H,T,P11) = log2 |F_adm(H,T,P11)|`,

with zero bits on admissible singletons and one bit exactly on genuine admissible doubletons.

The accepted result does not identify the selector with native orientation or with the distinguished Pfaffian negative slot, and it does not change the native P000 dimensional/type boundary.

## Decisive evidence

1. The immutable Result is writer-conformant and its manifest pins Return, checker, certificate and execution record by Git blob SHA-1 plus SHA-256.
2. The retained Generation-1 combinatorial theorem remains valid: on fully distinct sorted marginals the only equal-`P11` assignment pairs are `C1: AC=BD` for `132/213` and `C2: AD=BC` for `231/312`; repeated marginals are combinatorially injective.
3. The actual fibre is exactly the combinatorial fibre intersected with packetwise pairability. Hence a C1/C2 level is `ZERO_ADMISSIBLE`, `ONE_ADMISSIBLE`, or `TWO_ADMISSIBLE`, and no admissible fibre can exceed the already-proved combinatorial bound two.
4. The prior Driver falsifier is now handled correctly. For `H=(-2,0,2)`, `T=(-1,0,1)`, the C1 level `P11=2` retains only `213`, and the C2 level `P11=-2` retains only `312`; both therefore cost zero side bits even though both algebraic eliminants have two roots.
5. The simultaneous-collision witness `H=(1,4,7)`, `T=(-60,-30,0)` is a useful new boundary: C1 at `P11=-270` is an admissible singleton while C2 at `P11=-450` is an admissible doubleton. Selector cost is therefore level-specific, not a flag attached merely to `(H,T)` or to `C1 union C2`.
6. The Gram/Vandermonde quadratics remain exact candidate resolvents. On a singleton collision one root reconstructs an algebraic ghost packet rejected by pairability; on a genuine doubleton both roots reconstruct the two admissible packets. The SAME/OPPOSITE `P21/P12` root-order relation is retained only where two admissible branches exist.
7. I independently reproduced the fixed control-domain census over `220^2=48,400` sorted marginal pairs: `valid_fibres=2923`, `direct_doubletons=2`, `max_adm_fibre=2`, `repeated_valid_max=1`, with algebraic admissibility counts `C1=(286,8,1)` and `C2=(350,11,1)` for zero/one/two admissible branches. The mandatory falsifier and mixed-cardinality witness also reproduce exactly.
8. The frozen `B=6` genuine C1/C2 witnesses and their homogeneous root-scaling families remain valid positive regressions.
9. Assignment collision geometry, discriminant-square pairability, Vandermonde/Gram elimination and finite invariant calculations are used at classical mathematical strength; no historical novelty is granted for those ingredients.

## Successor gate

The selector task is now complete. It should not be reopened by adding higher mixed moments or by further refining the 0/1-bit coding law.

A distinct arithmetic gap remains: genuine ambiguity is characterized decision-theoretically by `C1` or `C2` plus six exact pairability conditions, but the global integer solution set is still structurally opaque. Current accepted evidence contains only two minimal root-box witnesses and their common scaling families. It does not classify primitive doubletons, simultaneous-collision primitive families, or whether every genuine doubleton belongs to finitely many rational/integer parameter families.

Closure was considered, but it would leave the exceptional one-bit locus as a black-box six-square test. Further information-coding work is not justified because the selector cost is already exact. Native orientation and Full-Cell routes are separately owned and are unnecessary for this arithmetic question. The smallest justified continuation is therefore a derived Diophantine normal-form task: factor out common root scaling and classify or obstruct a complete parametrization of genuine C1/C2 doubletons.

Method harvest: `RESULT_ONLY`. No Working Truth, Foundation status, native-orientation authority, factorization theorem, or Full-Cell dynamics is granted.
