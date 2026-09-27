# Executed checks and precise performance boundary

The parent objective is QFT/Shor dequantization. This unit removes a measured implementation overhead while preserving the actual native arithmetic. It does not resolve the unknown large-order or Gram-query growth problem.

## Guard implementation and precheck

`boundary_execution/boundary_uniform.py` SHA-256 is `875133020ba713af755d19b121f416938193835c3e2c9b7e6ab228c19b814c83`. It wraps gamma, mass, probabilities, advance, prepare_next, cursor, evidence and report. An outer entry checks the complete strict bank binding; nested entries retain the adaptive snapshot and ledger guard. Numerical methods and the omission policy are inherited unchanged. The premise is synchronous use of ordinary trusted Python objects, with no external program mutation during one outer call. It is not a hostile-object or thread-safe API.

The guard restores depth and owner on BaseException. The inherited provisional history transaction still rolls back only Exception; no new KeyboardInterrupt atomicity is claimed. The new cursor intentionally differs from the old schema/source/policy, and strict replay constructs the new class. No RNG or memoized query cache is restored. Evidence captured before later sampler mutation must be detached because inherited payloads contain live lists.

The final precheck used the actual full-61 native word admission and exact six-coordinate codec. Both N21/a2 and N21/a4, t4/history1000, matched all eight positive transitions. Forty public-entry mutation controls and seven cursor negatives passed, as did pending replay and query-budget rollback followed by retry of the same bit. This run used 1,251 native-core calls and 17.8909774 seconds. Its raw evidence has 14,004,778 bytes and SHA-256 `41cfe8eb1a88c10153c99f6524efcd10a9784cd363da48e8229aed32e1300b71`; its gzip SHA-256 is `e2f1edabc9223bc9216abcca83fd98b065c6ef53439ac62d23ff4c28802a15f9`.

An initial checker attempt failed while assigning directly to a frozen test-fixture dataclass, before the intended negative invocation. Its complete scientific raw stream was not retained. The corrected checker uses dataclasses.replace, and detaches intermediate evidence before continuing. The final counts above cover only the successful final attempt. EARLY_CODE_REVIEW.md and FINAL_SHARED_CONTEXT_REVIEW.md retain this chronology; no earlier failed execution is represented as a pass.

## Matched positive-prefix comparison

`prefix_comparison/compare_guarded_prefixes.py` SHA-256 is `78e70a1a27273ae3651cd3e7807d5774e4168e3c51119f26853634b52fd3aa6b`. Command: `D:/kimi-query-bridge/.venv/Scripts/python.exe -X utf8 D:/em/TEMP/sep27-qft-boundary/prefix_comparison/compare_guarded_prefixes.py`; exit 0.

The three programs are (N,a)=(21,2),(21,4),(65,3), all t=4, epsilon=1/3 and positive history1000. One shared cold certificate bank is paid. Each program then pays a full Uniform warmup with the same history. Measured samplers are fresh, but use the same already-warmed modular tables and primitive cache. The two pairs per fixture execute old/new and then new/old. Every measured run reports zero newly computed modular columns. System load was not controlled; these six paired observations in one process are not independent random timing trials.

The measured calculation starts before the constructor and ends after four advance calls plus terminal mass. It includes constructor and all entry guards. Counter snapshots are taken before evidence capture. Evidence capture is timed separately, and total-through-evidence times are also saved; final JSON/gzip serialization is outside both intervals. Neither evidence capture nor result equality assertions perform a new scientific comparison run.

For every pair, the complete saved correlation table and signed observer stream agree exactly, as do probability plans, selected word/charge/certificate ledgers, terminal mass, actual core-call counts and relevant query/vector counters. Exact old/new cursor equality is intentionally not asserted. The new guard has six complete binding checks in the measured calculation, counting constructor plus five outer calls. The old implementation has 86, 62 and 114 respectively. Scientific core calls remain 73, 116 and 54 per run. No native multiplication, modular propagation or approximation is replaced by host arithmetic.

The complete comparison uses 1,664 native-core calls and 24.86657220008783 seconds before final serialization. Its raw evidence has 15,942,154 bytes, SHA-256 `d45f67df6dc75448a8b1e1e87a33f7a6c4ab1f85069344123a61234caf4a8e6d`; gzip has 640,228 bytes, SHA-256 `a8157798dd3831afd9a760d623e5216774e5c3b27b50f99a522301ec001570b1`. The raw stream retains cold admission, warmups and measured runs separately.

No complete four-fixture probability-law validator was rerun. Its previous frozen result is reused only as prior evidence; current correctness additionally rests on unchanged inherited numerical code, the explicit synchronous guard premise and the bounded current checks. The earlier Uniform whole-checker runtime regression is not erased or reclassified by this narrower matched experiment. Current speed ratios concern this fixed warm-prefix workload only. Cold admission, program construction, storage, replay, query growth and exact arithmetic remain charged.

## Symbolic structure

FINITE_FEEDBACK_AND_MULTIWINDOW.md proves an actual orthogonal-instrument family with exact uniform prefix masses and linearly many active positions; its C=3 variant also has linearly many components with high probability. The family is classically easy and the aggressive cutoff does not claim an ideal-QFT accuracy guarantee. The variance used in its first probability bound is the variance of the one-bit count W_i, and the active count satisfies A_i>=W_i. The determinant argument concerns full-carrier matrix identity and does not exclude separate scalar-sign or reachable-subspace compression.

The multiple-window expression acts on arbitrary full matrices in chronological order. Negative displacements require an input transpose as well as an output transpose. Its explicit scalar fallback is O(GR), and its carry bound depends exponentially on active bits/windows. Order R and target address are not supplied for free. New refinements and next-design documents, when included in the final manifest, are symbolic or planned work, not unrecorded experiments.

All review here is shared-context author review. No formal Task/Claim/Result admission, P000 change, service deployment or persistent scheduler is claimed.

Global-Knowledge-Sync: main@2c42a77 / GLOBAL_KNOWLEDGE_V1
