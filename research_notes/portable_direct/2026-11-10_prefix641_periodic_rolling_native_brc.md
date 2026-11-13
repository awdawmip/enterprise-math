# PREFIX-641 — Periodic-gate exact window moments on the frozen native BRC action graph

Date: 2026-11-10 Asia/Shanghai. Status: AUTHOR_SIDE / PROVED ALGEBRAIC IDENTITY + EXECUTED FINITE CHECKS / UNREVIEWED.

Researcher-ID: EM-X6-EDB9A0. Research-Activity-ID: RA-A639EC84B9738E69545C008C. Formal parent RS-X6-NATIVE-ROTATION-DYNAMICS, TP2-6A1F9D8C2047E3B51C01, observer-side contribution; no formal CLAIM/Result. Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.

## Exact native problem

Continue PREFIX-635–640, retaining the original 48 STAR phases, 96 labelled ports, 576 original actions, and the Aho–Corasick observer of original action-ID motifs P0=(485,316,52,174), P1=(52,174). This is the seven-state AC, 672-product-state, six-component raw-moment observer (Z,U0,U1,V00,V01,V11). The transfer aggregates labelled paths only after the AC match events are applied. It is sufficient for these six moments; it is not a lossless listing of individual path histories.

The question: for periodic rational gate inputs, compute all length-L rolling-window six-moment queries without reconstructing the entire matrix product on each window.

## Theorem (exact periodic block factorization)

For any p>=1, L>=1 and periodic nonnegative rational gates g_(i+p)=g_i, let T_i be the frozen original BRC/AC six-jet transfer at step i. It is p-periodic. For any start index t, r=t mod p, q=floor(L/p), s=L mod p, define

Q_r = T_r T_(r+1) ... T_(r+p-1),       R_(r,s) = T_r ... T_(r+s-1), R_(r,0)=I,

where all subscripts are read mod p and products preserve original action time order. Then

M_(t,L) = T_t ... T_(t+L-1) = Q_r^q R_(r,s).

**Proof.** The original labelled BRC/AC step depends on time only through the gate value, so equality of gates p apart gives equality of their full six-jet operators. Split the ordered L factors into q complete p-step blocks and s further steps. Every complete block starts at phase r and equals Q_r. The original jet product is associative, including counts of matches crossing internal period boundaries because the AC state is transported between blocks. The remaining s factors are R_(r,s). Fraction-free representation N_i=b_i T_i gives the same identity with integer numerators and positive common denominators, normalized once at output. All statements hold for zero gates and overlapping patterns. QED.

The starting 96-port mass vector r_t changes with t and is separately updated/recovered; the chosen window operator depends only on t mod p. The six-field moment quotient retains the intended observables, not all individual labelled paths.

## Implementation and complexity

Precompute p native integer steps, each phase's p-step operator Q_r, its exact power by repeated squaring, and a remainder. Matrix-matrix compositions: O(p^2+p log(1+L/p)). Each queried window uses a current source mass vector times exactly one precomputed sparse operator, followed by six rational normalizations, with at most 4,284 matrix nonzero positions by the earlier frozen two-pattern certificate. W queries require O(p^2+p log(1+L/p)+W) operator-field operations with known initial state and compact period representation, plus W native start-state updates. For fixed p this is O(log L+W) matrix-composition / vector-application operations. If the gate input is an uncompressed array, certifying the periodic promise costs O(L) input comparisons. Exact integer bit cost, reconstruction of a remote start-state r_t, and expansion of every path are separately charged.

## Actual proof-oriented checks

Run the archived actual Python checker from `PREFIX641_code_results.tar.gz.b64`; it reuses frozen semantics in PREFIX640_fraction_free_rolling_jet.py and PREFIX638_native_jet_support.py. The archive contains the program, full JSON of all twelve workloads, and the actual test log. Two independent numerical comparators are the prior two-stack fraction-free window queue and an original-action-by-original-action Fraction AC DP oracle. A further full-transfer comparison directly multiplies chronological step matrices.

Gate families: all-one p=1; positive rationals (1,2/3,5/4) p=3; zero-containing (1,0,3/2,5/3) p=4. Each family runs (L,W)=(8,8),(32,16),(64,32),(128,16). **432 exact pairwise comparisons of all six query outputs and 40 complete six-field operator identities passed** (program exit 0).

Selected single-run Python end-to-end timings in seconds, including operator/queue preprocessing, queries, native state advancement and output normalization, excluding the same four-step shared initial source setup:
- p=1, L=128, W=16: periodic 0.096913; integer queue 2.994698; native DP 4.098549. Speedups approximately 30.9x and 42.3x in this run.
- p=3, L=64, W=32: periodic 0.376086; integer queue 1.683860; native DP 4.333429.
- p=4 (contains zero gate), L=64, W=32: periodic 0.322999; queue 1.733622; DP 4.128291.
- p=4, L=8, W=8: periodic 0.230750; queue 0.174208; DP 0.111226, showing short-window precomputation overhead.

For all-one L=128,W=16 the periodic method uses 9 matrix compositions vs queue's 268. Timings are single-run observations; the universal identity rests on the proof, not on the measurements.

## Exact evidence and continuation

Archive path: `research_notes/portable_direct/PREFIX641_code_results.tar.gz.b64` (base64-encoded gzip tar containing checker, complete 12-case JSON and execution log). Runtime dependencies: PRIOR existing PREFIX-640 complete research archive and its identical PREFIX-638 original-action dependency, cited at awdawmip/enterprise-math@ac6ca238ff925fa0f3e309e72cee402fd0bf33df; downloadable local complete package also prepared.

Run from a directory containing `PREFIX640_fraction_free_rolling_jet.py` and `PREFIX638/PREFIX638_native_jet_support.py`: `python PREFIX641_periodic_window_jet.py`.

Next discriminating question: eventually-periodic inputs with finite prefix h; identify the distinct window transfer classes that cross that prefix and their optimal reuse, and measure gate-certification and exact bit costs for very large L. The parent task's arbitrary-triad signed C6 and physical Cell/path rotation dynamics remain separate open questions.

No mathematical review, Foundation promotion or physical-model native rotation claim is made by this author-side result.
