# EC49FET — Group-aware prefix dual closes all EC49FEQ H3-mixed 23-path type B/C inventories

Date: 2026-11-08. Frozen original scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Status: **AUTHOR FINITE EXACT PROOF / UNREVIEWED / NOT CANONICALLY ADMITTED**.

## Theorem and exact finite scope

Fix the original signed/native ordered X6 microstep alphabet, the nine-state DFA, endpoint displacement `(2,0,0,0,0,0)`, complete forward BRC cache keys (at most five) and one path per mandatory observer signature. In Type B, H2 requests {1,2,4,8}, H3 requests {1,8,16}, and four distinct H4–H9 windows request {16,32}, the remaining two requesting {1,2,4,8}. Total **23** paths. Allow every path to use any valid full key from its prescribed five-key inventory and allow mixing within a window. Count the union of all nonempty **signed ordered native six-axis microstep prefixes**.

**Result:** Every one of the **12,276 EC49FEQ Type B signature-feasible five-key inventories** has `C_native >= 94` for any legal 23-path selection. By the EC49FEF operation-word involution `(c d)(f g)` preserving signed prefix cost and observer signature rank, the same holds for the corresponding **12,276 Type C mirror configurations**. Hence **24,552/24,552** finite feasible typed configurations exclude `C_native<=93`. This is a complete finite exclusion for these two H3-mixed models; it does not assert a new mother-problem-wide optimum. The existing 94-edge witness in a different path/signature model is unchanged.

## Inherited verified frontier and newly certified cases

Source EC49FES (`research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FES_H3_MIXED23_SIEVE_20261108/README_EC49FES.md`, exact `EC49FES_REPORT.json` blob `6dbfaa2cb4d6f236f0f5743788cab7fdf626e896`) independently ruled out 12,251 of the Type B inventories by conservative exact depthwise packing, leaving 25 enumerated indices. This EC49FET step creates **25 new independent *integer-only checkable* feasible dual certificates**; each proves the integer edge cost **at least 98**, resolving the exact remaining 25. It does not replace prior FES evidence or claim review.

Residual indices and certified lower numerators (all denominators Q=1,000,000):

`449:100000000/1000000; 450:98000000/1000000; 452:100000000/1000000; 610:100000000/1000000; 612:97999994/1000000; 614:100000000/1000000; 1726:108000000/1000000; 1728:108000000/1000000; 1748:111000000/1000000; 1750:111000000/1000000; 2724:98000000/1000000; 4481:100000000/1000000; 4482:100000000/1000000; 4498:98000000/1000000; 4500:98000000/1000000; 4532:100000000/1000000; 4534:100000000/1000000; 6635:106000000/1000000; 6636:106000000/1000000; 6652:106000000/1000000; 6654:106000000/1000000; 6844:105000000/1000000; 6846:105000000/1000000; 6878:105000000/1000000; 6880:105000000/1000000`.

The minimum exact rational lower certificate is 97,999,994/1,000,000 = 97.999994 (index 612), proving integer cost at least 98.

## New group-aware prefix covering relaxation and theorem

Let mandatory observation groups be g=1,...,23. For each group g, finite set W_g comprises **all** admissible original words of that window, signature and five-key inventory. Each word is expanded into its ordered signed microsteps; denote its nonempty prefix set P(w). For any integer-feasible selection, define x_w=1 for exactly one chosen word in W_g and y_p=1 when native signed prefix p occurs in any selected word.

The valid and stronger group-aware covering inequalities are

`sum_{w∈W_g: p∈P(w)} x_w <= y_p` for every g,p, and `sum_{w∈W_g}x_w=1` for every group.

(They aggregate over a *group*, because exactly one word is selected per group.) For any **nonnegative integer** dual weights T_(g,p) and charges gamma_g and any positive integer Q, suppose the following **integer inequalities** hold:

`sum_g T_(g,p) <= Q` for each signed native prefix p;

`gamma_g <= sum_{p∈P(w)} T_(g,p)` for every word w in W_g.

Then for every legal integer selected system S, by summing group inequalities,

`sum_g gamma_g <= sum_(g,p∈P(w_g)) T_(g,p) <= sum_{p∈∪_g P(w_g)} Q = Q*C_native(S)`.

This proof uses only integer arithmetic and the original native signed prefix semantics. The certificate checker reconstructs every W_g from the six original atomic ops, complete BRC key count equations, length/end point, original nine-state DFA, and then rechecks **every** listed inequality. It does **not** trust the floating LP dual values; LP/HiGHS was used only as a **candidate certificate finder**. Integer rounding/flooring is followed by full exact revalidation. In the 25 cases, sum gamma_g > 97 Q, whence C_native>=98; in particular no C_native<=93 system exists in these inventories.

## Complete experimental and reproducibility record

The 25 original support-feasible residual inventories are fixed by `CASES_EC49FET.json`. The 25 full sparse rational dual certificates (nonzero integer numerators and their deterministic group/prefix-pair incidence indices) are in `certificates/strong_<index>.json`. `WORD_MODEL_EC49FET.py` is an independent pure-Python enumerator; `VERIFY_EC49FET.py` is the **source-independent exact mathematical verifier**, using Python standard library only. Run from the top folder:

```
python3 VERIFY_EC49FET.py certificates/strong_*.json > evidence/INDEPENDENT_FINAL_VERIFICATION.jsonl
```

`REGENERATE_EC49FET.py` is a numerical finder (requires scipy/numpy) for optional regeneration:

```
python3 REGENERATE_EC49FET.py CASES_EC49FET.json regenerate/
```

The actual execution verified **25/25** certificates, including all **60,800** enumerated candidate words and **439,602** distinct group-prefix pairs; **274,882** nonzero integer weights were read and exactly checked. Reports in `EC49FET_REPORT.json` include per-case certificate SHA256, counts and bound fractions. `evidence/INDEPENDENT_FINAL_VERIFICATION.jsonl` contains actual passing output. Nonzero sparse certificates have numerical-generation provenance; their **truth is fully certified by independent exact integer checks**.

## Source scope and next problem

References: EC49FEQ type B/C exact inventory census; EC49FER exact 98 for one fixed inventory; EC49FES stronger depthwise 12251/12276 exclusion; EC49FEF word involution. All under original signed native X6 microstep semantics and frozen scientific pin above. Author-side mathematical proof is distinct from independent Driver review, Source Result admission and any task CLAIM or owner lease.

Next scientific unit: test different mixed-window placements / other 23-path allocations and, in general, altered observation signatures and path counts. Target remains `<=5` full BRC keys and `C_native<=93`; candidate constructions require direct exact X6-DFA-BRC and native-prefix verification.