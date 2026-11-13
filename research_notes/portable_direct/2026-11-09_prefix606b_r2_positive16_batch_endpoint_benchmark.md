# PREFIX-606B-R2 — Exact 16D BRC batch-endpoint test with shared gate-word products

Date: 2026-11-09 (Asia/Shanghai). Status: EXECUTED EXACT INTEGER BENCHMARK; performance is host/implementation-specific; independent review pending. Frozen original X6-BRC pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.

## Exact problem and reused interface

This benchmark uses the PREFIX-606 fixed six-axis weights (1,1,1,1,0,0) and original 48-phase native-derived Q(z) of the 96-port, 576 tagged-action BRC model. Nonnegative integer gate sequences may vary freely; nonnegative integer 48-phase input vectors vary across queries. The observer is the **complete final 48-phase vector**, not unaggregated 96-port tagged histories.

PREFIX-606 proves a simultaneous, exactly nonnegative 16D realization at all gates z>=0: the first two steps encode via R(z2,z1)=R00+z2 Ra+z1 Rb; the remaining steps use T(z)=T0+zH, with one nonzero transition per row/column, and full final output is E u. The transition T(z) splits into four four-cycles; the only gate-varying edge is T(z)[15,0]=z+3.

## One shared gate word, many phase inputs: an exact algorithm

For a gate suffix w=(w1,...,wm), define four nonnegative integer products

    p_r=product(w_t+3 over t=1..m with (t-1)%4=r),  r=0..3.

The transition T(w_m)...T(w_1) is a 16-by-16 monomial matrix. For a source coordinate j on a particular four-cycle, follow its permutation orbit to find the gate-edge crossing offset r, multiply its ordinary non-gated edge weights, multiply p_r if the cycle contains the gated edge, and write the resulting single transfer coefficient to the uniquely determined output coordinate. This is the exact positive-coefficient 16D version of PREFIX-605's residue-class gate word theorem.

The shared transfer takes O(m) gate-product multiplications and O(16) coordinate entries, then the actual per-input query performs the two-step 16-state loading (R00+z2Ra+z1Rb), a 16-position monomial application, and full 48-output positive decoding E. For nonnegative inputs and gate weights, all terms stay nonnegative. There is no cancellation, floating-point rounding or iterative Krylov approximation.

## Executed deterministic exact verification and timing

Source program: PREFIX606B_R2_positive16_batch_benchmark.py, which imports the already tested exact PREFIX606_R2_positive16_exact_checker.py in the same directory. It constructs the original STAR successor relation, then cross-checks native 48-phase propagation, positive 16-state stepwise propagation, and positive 16-state monomial batch propagation for each of nine deterministic workloads:

- propagation depths n=16,64,256;
- batch sizes 1,20,100 phase inputs per shared gate word;
- independent input/gate values generated from random.Random(606) with fixed integer ranges;
- 5 executed runs per method; Python perf_counter_ns median;
- arbitrary-precision integer arithmetic for all timed algorithms.

Every complete 48-coordinate output matches exactly. Separate monomial-transfer checks compare the positive 16D word product against sequential transitions at suffix lengths 0,1,2,3,4,7,15,63.

All timings include the initial two-step state loading and all 48 final output coordinates, for each input. The 'batch including transfer' measurement also includes one shared O(n) gate transfer construction per group. Matrix and native-incidence construction from the fixed specification is outside the timed region for all four methods.

| n steps | phase inputs | largest output bits | optimized native48 (ms) | positive16 stepwise (ms) | positive16 batch incl. transfer (ms) |
|--:|--:|--:|--:|--:|--:|
|16|1|28|0.1926|0.0423|0.0334|
|16|20|28|5.2544|0.8323|0.4695|
|16|100|29|20.5010|4.7426|2.6499|
|64|1|86|0.8229|0.1336|0.0421|
|64|20|86|18.0892|2.6175|0.8092|
|64|100|87|92.0044|13.2599|2.5482|
|256|1|325|3.7295|0.5302|0.0593|
|256|20|326|78.1251|11.1341|0.5289|
|256|100|326|395.1776|53.3340|2.4581|

For the n=256, 100-query case, the observed Python integer endpoint calculation is about 160.8x faster than the optimized native 48-phase loop in this one five-run-median experiment; the transfer setup is included in the batched result. This is a reproducible experiment, **not** a general language-independent complexity-speedup theorem.

## Exact coverage, bounds and next problem

Algebraic correctness of the positive 16-state method rests on PREFIX-606's five matrix equalities and nonnegativity checks. The monomial transfer follows by iterating a four-cycle with exactly one gated edge, with one product for each gate-position residue class. The finite workload checks the implementation and timings; medians may change with host, interpreter, Python version, cache and integer-size distribution.

Next scientific-engineering unit: benchmark the input and output bridge from the **original 96 ports**. First define the actual 96->48 phase-loading map and 48->96 post-transition observer as in PREFIX-595/597. Then compare native 96-port sparse kernel versus 49/48 positive realization and 16D positive batch realization, explicitly accounting for representation/decoding and retaining a distinct carrier for any original tagged-path information whose observation does not descend to the 48-phase quotient.

No native CLAIМ, Researcher-ID, Result, independent Driver mathematical admission, or Foundation promotion is asserted. The current native identity/owner lookup failed BACKEND_IDENTITY_CHECK_UNAVAILABLE with operation_sent=false; GitHub author-side source is durably published.
