# PREFIX-641 — Fully integer end-to-end rolling query for original labelled BRC moments

**Date** 2026-11-10; **science pin** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d` (unchanged); **status** independent author-side research, proof + exact executable tests, unreviewed. Parent `RS-X6-NATIVE-ROTATION-DYNAMICS`; no formal CLAIM.

## Scope

Retain the original 48 STAR phases, 96 labelled ports, 576 native BRC actions; the same two original action patterns `(485,316,52,174)` and `(52,174)` and their seven-state Aho–Corasick observer. The six original weighted jet coordinates are `(Z,U0,U1,V00,V01,V11)`. This is a positive-path observer, not a signed/complex amplitude or physical X6 rotation claim. P000 and the fixed scientific input are preserved.

PREFIX-640 removed rational intermediates from sparse *matrix products*, but its initial-port propagation and final aggregate evaluation still used `Fraction` objects. Here the **whole query** uses integer port numerators and integer matrix/vector jet products, with rational output conversion only at the final six coordinates.

## Exact theorem

Write the initial original 96-port row `r_0=p_0/d_0`, `d_0>0`, and each gate `g_i=a_i/b_i` with nonnegative integer `a_i` and positive integer `b_i`. For each original outgoing labelled BRC action of step `i`, replace gated weight `g_i` with integer `a_i`, ungated unit weight `1` with integer `b_i`, and ungated zero with zero. Apply those **same source/destination/action** edges to integer port row `p_{i-1}` to form `p_i`. Then `r_t=p_t/(d_0 prod_{i<=t} b_i)` exactly, including gates equal to zero.

Let `N_i=b_i T_i` be the original six-jet product-state operator with the same seven-state observer. Let the start window `t` have length `L`. The exact raw six-moment output equals

```
J(t,L) = [(p_t tensor AC_start) N_(t+1) ... N_(t+L) 1]
         / [d_0 (prod_(i<=t) b_i)(prod_(t<i<=t+L) b_i)].
```

If the ordered window product is stored as the front aggregate followed by the back aggregate in a two-stack queue, apply each of the **at most two** integer matrices to the integer start vector and normalize only after summing the final six integers.

**Proof.** Every original action weight in step i is scaled by exactly b_i; induction through the original labelled BRC port update proves the first identity. Six-jet composition is bilinear: path weight multiplies while motif occurrence-count vectors add, preserving their first and second moments. Scaling each one-step jet by b_i therefore scales an ordered block by the product of b_i. The retained AC state counts patterns crossing the two-stack boundary upon their last action, so multiplying the left then right aggregates enumerates precisely the original paths. Zero gates are handled without division by a gate. QED.

For the frozen probe, the initial integer denominator is four, and exactly five entries of `p_0` equal five; total initial numerator mass is 25.

## Complexity and exact bit scope

Let `W` be the number of sliding windows queried and `M_i=max(a_i,b_i)`. Every original port has at most six labelled exits. Consequently, the total nonnegative integer port numerator is bounded by `25*6^t*prod_(i<=t) M_i`. Each of the six final moment numerators is bounded by `25*6^(t+L)*prod_(i<=t+L)M_i*max(1,L)^2`. This bounds integer bit lengths and explicitly accounts for the denominator `d_0 prod_(i<=t+L)b_i`. It is a valid bound, not a claimed tight BRC growth law.

Prior native support analysis supplies at most 4,284 matrix nonzero positions and 10,500 candidate sparse-join products per two-block multiply in this fixed two-pattern observer. The double-stack queue therefore performs `O(L+W)` bounded-support **integer** matrix compositions and `O(W)` two-sparse-matrix-vector query evaluations; initial original-port propagation from time zero costs `O(t)` fixed-graph steps, giving `O(t+L+W)` arithmetic operations for fixed observer dimensions. Exact big-integer bit cost, `O(L)` cached aggregate storage, construction of the input gates, and `W` six rational output bit lengths still count. Direct original BRC DP takes `O(t+WL)` fixed-dimension layer operations, but can be faster for practical small windows.

## Executed evidence

The **full original executed checker** `PREFIX641_native_rolling_full_cost.py`, its **full result JSON** and the **full 10,179-byte paper** are packed in the adjacent lossless `PREFIX641_core_paper_source_results.tar.gz.b64` (decode with `base64 -d ... | tar xzf -`). The original unchanged dependencies are `PREFIX640_fraction_free_rolling_jet.py` and `PREFIX638/PREFIX638_native_jet_support.py`; see PREFIX-640 and PREFIX-638 research archives. The standalone complete downloadable handoff (including these dependencies and log) is `ENTERPRISE_MATH_PREFIX641_COMPLETE.tar.gz` in the original conversation.

Executed `156` exact checks across the original frozen graph, three gate classes (all one, rational, periodic zeros), lengths 1,3,4,8, and 4–6 consecutive queries. Every integer port-state prefix matched the original `Fraction` update, and **all six** integer rolling outputs matched both the old Fraction queue and independently recomputed original-action DP. Four additional single-run end-to-end workload benchmarks (step construction, initial-port and rolling update, queue rebalance, final exact outputs all included):

| Gates | L | W | Direct native DP, s | Full int queue, s | Fraction queue, s |
|---|---:|---:|---:|---:|---:|
| all one | 4 | 8 | 0.050809 | 0.133289 | 2.000337 |
| all one | 8 | 8 | 0.111751 | 0.206346 | 3.068781 |
| positive rational | 4 | 6 | 0.040307 | 0.126857 | 1.780357 |
| periodic zero | 8 | 6 | 0.090571 | 0.271164 | 2.816480 |

Thus the **int queue is faster than the old Fraction queue** in these four workloads, by approximately 10.4–15.0 times; **direct DP is faster than both** in these four workloads. These timings are single-process observations, not a global crossover assertion. Longer full-Fraction benchmarking attempts did not finish within their execution boundaries; do not count those attempts as successful validation.

Original local SHA256: full checker `7689695fe282c9bf085d8b0b6507906fefcf73c65886a6a10eea6adaab9dc40f`; full JSON `5134f98dee6670a07813e790f1c19f738d8bf567070cec37a22fccd888b5b0b5`. Native runtime identity and exact current task owner **not confirmed**: Source session-start and task-control reads remained QUEUED at last observation. No Result or independent review admitted.

## Next work

Precompile the prior four-period support joins, instrument peak RSS and integer multiplication/bit counts, and perform isolated bounded benchmarks with larger `L,W` to find or reject a *measured* crossover against native DP. If the full-state queue remains slower, exploit the current window's reachable original-source support rather than spending full 672-state matrix work. Preserve signed amplitude and physical rotation as separately open scientific targets.