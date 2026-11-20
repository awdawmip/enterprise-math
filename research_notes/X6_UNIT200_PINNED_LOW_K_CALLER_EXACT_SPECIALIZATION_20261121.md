# X6 Unit200 — Exact low-pair BRC formula at the *actual frozen caller* input window

Status: **AUTHOR_PROVED / EXACT_PINNED_PYTHON_EXECUTED / UNREVIEWED / NOT_ADMITTED**  
Date: 2026-11-21; Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication: `TP2-B4A441B23DA3159232C2`  
Mother objective: `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`  
Frozen scientific pin: `59538f585d037d09ef687b28715c4bc1a3f9fe03`. Historical comparison pin: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.  
Research lane: `chatgpt-research-onhour-enterprise-math-20260923`; historical Source author `EM-X6-FB6990`.

## Verified provenance and decisive workload observation

Direct immutable Source: `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` at `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`, SHA-256 `6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4`. The original `endpoint_weight` is a rational-weighted sum over six-axis weak compositions of K backtracking pairs.

**The actually established direct consumer is regression code, not a production workload.** The immutable `experiments/x6_signed_native_spatial_v16_20260905/check_signed_brc.py` imports this function (lines 6–9). Its exact call loop (lines 56–63) uses three endpoints `(0,0,0,0,0,0)`, `(1,-1,0,0,0,0)`, and `(2,0,-1,0,0,0)`, all six positive and negative weights equal to 1, and lengths `base..base+4`. Consequently its entire 15-call workload has **K=0,1,2 each three times, plus six parity-incompatible zero cases**. The Unit199 K=4,8,12,16 benchmark did not sample this actual consumer window. This difference is actionable source evidence, rather than an inference from a file name.

## New exact specialized formula

Let `z in Z^6`, `a_i=max(z_i,0)`, `b_i=max(-z_i,0)`, `u_i,v_i in Q_{>0}`, `L in N_0`, `d=sum_i |z_i|`. A gap `L-d<0` or odd gives exactly zero. Otherwise `K=(L-d)/2`, and define

```text
P = L! * product_i [u_i^(a_i) v_i^(b_i) / (a_i! b_i!)]
q_i = u_i v_i
r_i = q_i / [(a_i+1)(b_i+1)]
s_i = q_i^2 / [(a_i+1)(a_i+2)(b_i+1)(b_i+2)]
```

Then the weighted signed native BRC endpoint sum is exactly

```text
K=0: E_L(z) = P
K=1: E_L(z) = P * sum_i r_i
K=2: E_L(z) = P * (sum_i s_i + sum_{i<j} r_i*r_j).
```

**Proof.** In the original pinned function, a six-tuple `k_i >= 0` with sum K contributes `L! product_i u_i^(a_i+k_i)v_i^(b_i+k_i)/[(a_i+k_i)!(b_i+k_i)!]`. Factor out P. At K=0 only the zero tuple remains. At K=1 exactly one axis carries one pair, giving r_i. At K=2, either one axis carries two pairs (s_i) or two distinct axes carry one pair each (r_i*r_j). These are disjoint and exhaustive, proving equality with the original sum over its entire declared K<=2 scope. The exact rational computations preserve all six labeled axes; endpoint aggregation does not claim to recover ordered path provenance. For K>2 the specialized checker raises rather than silently applying this formula.

## Executed exact test and native-source comparison

The author independently imported the SHA-verified original Python source and executed the new exact formula on **45 endpoint/length/weight comparisons**: the three actual caller endpoints, all five caller length offsets, and three positive rational/integer six-axis weight profiles. All outputs equal the original function, including parity-impossible cases: **0 disagreements**. The published checker is at `research_checks/X6_UNIT200_LOW_K_EXACT_CLOSED_FORM_20261121.py`; its certificate is `research_checks/X6_UNIT200_LOW_K_EXACT_CLOSED_FORM_RESULTS_20261121.json`. It accepts `PINNED_SOURCE_FILE` containing the verified frozen bytes or `git show` of the historical pin. No R063 original six-file benchmark or frozen source was rerun/modified.

For the **same 15 original regression calls** with unit weights, Python `time.perf_counter_ns`, seven 100-suite batches, the median time per complete 15-call sweep on this execution host was:

| Method | Median per complete 15-call sweep |
|---|---:|
| Original pinned `endpoint_weight` | 1,606,566 ns |
| Specialized exact `K<=2` closed form | 449,623 ns |

The measured ratio is about **3.57x** in this exact host/consumer window. Both methods performed identical Fraction semantics; samples are in the remote certificate. This is an observed method-level comparison, not full native six-file benchmark acceptance or a claim of production speedup.

## Interpretation and next real work

The new low-K formula is a consumer-specific closed form of the already proved Unit198 coefficient series (not a second general all-K DP theorem). Unit199's high-K benchmark and this low-K consumer are distinct operational objects. The frozen test consumer is now characterized by exact `commit:path:line`, K distribution, outcomes and a directly runnable specialization. **No actual production `endpoint_weight` caller is yet established.** Continue exact frozen producer/consumer source localization for LP011/LP019 claims and any real workload; distinguish documented test-only inputs from observed production, and preserve the original R063 acceptance object.

Native semantic links through Unit200 and historical Units149–152 remain pending an authorized same Research-lane RUN/PROGRESS, separately from this immutable GitHub proof. Independent Driver review and Result admission are pending. This unit does not alter P000, the six-axis/time ontology, the input pins, task ownership, or scheduling.
