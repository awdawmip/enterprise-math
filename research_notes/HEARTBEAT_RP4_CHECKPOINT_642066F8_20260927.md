# RP4: exact rolling checkpoints, nonlinear boundaries and measured time to a verified factor

Progress-Event-ID: RP4-C971348E-642066F8
Date: 2026-09-27 Asia/Taipei
Status: AUTHOR_DERIVATION_AND_EXECUTION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global read snapshot: 9f0e65baf6f9d575ead1112546c0304a211099c5
EM control intake: 2e6b196d184c98f2849d1bd133bdd57cc96abb1a
Publication preflight: 452ffb73180f459d4c08302aad754ac512dc1bab
Scientific parent: 182592bf660e5f1536cea24b6a2072145c69636e (RP3)
Scientific commit: 642066f84730cfb709b858bdc3da5ae30f7f279d

This additive portable research note is not a formal Task/Result, independent review, Foundation promotion or parent-objective closure. P000 and actual BRC-only constraints are unchanged. All 2504 parent tracked files remain byte-identical. Actual science uses the inherited b12 bank, complete61 signed modes, exact dyadic exponents, modular labels and ordered feedback. Primary tail cap is K16; finite diagnostic laws also use K6. No new classical phase reference, precision increase or known-order/factor tuning was used.

## 1. Same nonlinear target, less repeated reconstruction

RP3 defines a_hb(z)=[u_h(z)+(-1)^b T_h u_h(P_i^-1 z)]/2 and u_hb(z)=Q_K(a_hb(z)) at each nonterminal boundary; the terminal exception remains unchanged. RP4 stores a COMPLETE map C_g of every nonzero already-truncated row at one measured classical prefix g. A sparse forward layer applies the original gate to each source row, relabels by P_i, joins the two arms and applies the original quantizer at its original boundary. This equals u_g by induction. Backward queries substitute C_g only for compatible descendants; shallow or incompatible histories fall back to the original recurrence.

A missing row denotes zero ONLY in a complete checkpoint. Ordinary memo misses recurse. Each complete layer is committed atomically. If the64-row checkpoint cap is exceeded, the incomplete layer is not committed and the old complete anchor remains. No row is discarded to fit the budget. Checkpoint and512-entry memo limits are not byte/RSS limits. New whole attempts clear both. The sampler, actual rejection probabilities, RNG functions and factor verifier are inherited unchanged.

Forward-layer and backward-query induction prove the identical canonical row function for every legal query in scope, not only measured seeds. Hence under the same random tape, proposals, bits, rejected trials, factors and RNG states agree. RP3's accepted law, survival Z and same-bank error bound min(1,(t-1)*8*2^(1-K)) are unchanged: checkpoints add no approximation term. Error from the b12 bank to b64/ideal remains separate.

The nonlinear boundary cannot be moved: at K2, padded61-dimensional x=(7,1), y=(-6,0), Q2(x)=(6,0), so Q2(Q2(x)+y)=0 while Q2(x+y)=(1,1). Actual inherited BRC squared norms0 and2 verify the witness with two new core calls. This is an interface counterexample, not a claimed standard Shor prefix. Linear stretches between quantizer boundaries may still use existing exact ordered compilation.

## 2. Conditional resource theorem and actual overflow

At fixed checkpoint depth k, construction takes at most2^k-1 forward input-row visits and a depth-i query at most2^(i-k+1)-1 recursive visits without memo. This reuses the existing C6438C prefix-checkpoint framework while preserving every nonlinear Q_K boundary.

For rolling interval g, IF every required complete map fits R nonzero rows, one whole attempt uses at most(t-1)R forward input-row visits. Each of two local queries per bit is at depth at mostg-1, giving at most2t(2^g-1) recursive visits. Actual word action/bit costs, modular columns, labels, exponents, temporaries, dictionary/memo storage, certification and retries are charged separately. R small is a premise, not a consequence of setting a cap. If a complete layer does not fit, queries stay exact but the bounded-gap premise fails and exponential recursion can return. Under iid fresh trials, time to a survivor is E[C_trial]/Z; use the verified-factor probability, not Z, for time to an actual factor.

Pressure test N251/a6/t16, two length14 prefixes (all zero and alternating01), eight specified work labels, K16: cap8 halts checkpoint advancement at depth3 with8 rows; cap64 at depth6 with64 rows. All32 requested complete rows equal RP3, also after memo clearing. No approximate pruning occurred. Stress execution retained151949 core records. This is not a general bounded-support theorem or a factorization benchmark.

## 3. Five-round interleaved sampling comparison

Predeclared cases(77,2,14),(143,2,16),(119,2,14),(187,2,16), eight seeds each, base202609270710000+case_index*10000+j. Methods: parent RP3 query512, fixed midpoint(t//2), rolling every4, same-target full field. Five rotated/reversed interleaved repetitions:640 executions,32 distinct case/seed pairs. Bank already built; each batch includes fresh program/factory/query setup, complete checkpoint construction, retries, postprocessing and event collection. Comparison/encoding/file I/O excluded; GC enabled. All three query methods give identical full events/tape/RNG. The full-field sampler has the same target but different random trajectories. Median seconds per8 accepted outputs:

|N/a/t|RP3 query|Fixed midpoint|Rolling4|Full field|
|---|---:|---:|---:|---:|
|77/2/14|0.531737|0.401042|0.173132|0.197215|
|143/2/16|1.191138|0.790980|0.336944|0.363546|
|119/2/14|0.121656|0.099542|0.078520|0.055294|
|187/2/16|0.460587|0.412361|0.156494|0.108543|

Rolling reduces this batch time35.5%-71.7% versus RP3, but is faster than full field in only two of four cases. No universal winner. For N143 the computed recursive nodes fall6136->448, but INCLUDING construction actual gate applications RISE4689->5966; forward input-row visits1080, peak checkpoint15 rows. Reduced node counts are not a decrease in every operation or a generic Shor speedup. Timing core records144691. All raw unfavorable results retained.

## 4. Actually run until a verified factor

After the primary block, freeze AMENDMENT_TIME_TO_FACTOR.json and use NEW seeds202609270725000+case_index*10000+j, eight starting runs per case. Three interleaved repetitions of RP3/rolling4/full field, each run stops only when the unchanged verifier returns a nontrivial exact divisor. Each run allows32 output samples, each output100 whole trials. All runs completed within limits; no censored failures omitted.288 factor-run executions contain32 distinct case/seed pairs and975 sample calls. Bank already built. Median seconds per batch of eight completed factor runs:

|N/a/t|RP3 query|Rolling4|Full field|
|---|---:|---:|---:|
|77/2/14|3.107101|1.242352|0.840746|
|143/2/16|2.558742|0.803559|1.437451|
|119/2/14|0.470220|0.264887|0.273252|
|187/2/16|1.238215|0.498312|0.604948|

RP3 and rolling have the identical random paths and stop points, so this is a paired implementation comparison. Full-field paths differ: output counts per batch query/full are42/31,17/30,24/29,19/31. Do not turn these small-sample stopping-time differences into a proved average superiority against full field. This is not a new cold-process study; initial certified-bank construction is separately recorded. Factor block core records193622. It is not a comparison against every earlier suffix/full-field optimization.

## 5. Verification and actual source recovery

Complete small diagnostics N21/t6 andN33/t6, K6/16, fixed64/rolling64/rolling2:73152 full-row comparisons and2838 local probability/acceptance checks. Six invalid settings/mapping writes, memo/all-cache clearing, reverse request order, incompatible prefixes and random-source exhaustion were checked. Final safety process records363452 core calls. A t5 plan was rejected by the inherited even-width interface, corrected to t6 with original plan/error preserved. A45-second tool interruption left two complete trees preserved before repeating safety for complete counters. A stress-script syntax error was fixed before any scientific execution, with its log retained. No favorable timing selection or scientific source alteration followed the main measurements.

The mounted RP2 and RP3 large full bundles did not match their previously recorded byte counts/hashes. They were not used or overwritten, and no cause is inferred. Source was recovered from the hash-reverified mounted Stage104 full bundle plus the RP1/RP2/RP3 deltas. The recovered RP3 passed its91-file manifest and2412 prior parent-byte checks. RP4 then preserved all2504 RP3 tracked files. This was integrity recovery, not replay of prior complete scientific experiments.

RP4 has280 new tracked files,279 hashes plus the manifest. An independent local extraction and a cloud-downloaded extraction each verified the compact-source pins and all279 entries, then ACTUALLY replayed N143/t16/K16 query/fixed/rolling full sample events/tape/RNG and N251 cap64 overflow plus two fallback rows. Each smoke used5282 core calls. Stored trace comparisons also include96 full sample/factor comparisons. A fresh full-bundle clone verified279 entries and2504 unchanged parents; its separate check did NOT repeat the smoke. All of these are author checks, not independent scientific replication.

## 6. Artifacts and actual Drive mirror

Scientific commit642066f84730cfb709b858bdc3da5ae30f7f279d; entry START_HERE_RP4.md.
Compact standalone RP4 run ZIP: BRC_RidgePrecision_RP4_RUN_20260927.zip,12283280 bytes,SHA2560e914b326d1105e54e7f596323f239de2b2e97e8161b9e648eaf45e29b646707. Includes1952 payload files plus compact manifest, all current RP4 evidence and required run sources. No parent bundle is needed for RP4 reproduction; full Git history and historical large experimental evidence are NOT included.
Full standalone Git bundle: BRC_RidgePrecision_RP4_20260927.bundle,260342478 bytes,SHA256867036e45034e79840a1e8bf41aa28640c7bd5a6b262ffd8bb806f98ee07fa65. Contains parent history; chat delivery, not separately uploaded to Drive.
Delta: BRC_RidgePrecision_RP4_20260927_delta.bundle,3953586 bytes,SHA256bd900e37ba8e5b4f61a5265b46f330cbd3b12e6b6360aa0d9cad9ca1eddead9b. Requires RP3 parent182592bf, NOT standalone.

Drive root19dd_3frjJu-MeL-eD-UKuNYdCo5cTZXP; folder1NzGPm9XoRESHepUTBNHQUOQ2dcgaRYuR, RP4_滚动检查点与验证因子成本_20260927. Compact ZIP file1drbbHsgJSyzoKkD94Ce4RiiBu0XYvLFn was actually uploaded, metadata-read, downloaded, hash-checked and extracted for the complete smoke described above. Delta file1NXO-aqYgwBJ_QtlEHuZTBTHPU1mU0JUS was uploaded, downloaded, full-hash checked and git-bundle verified against the parent; no separate delta-chain smoke is claimed. Report1gDTsjct9uK530FHjz0ndIrATlqgOYl7U, proof1WlHIVOR154XPoJ5lnbVoWFdx5dZXxkvf, results1IzEaHmqnJ6eV9briJ43XKhyT46X7dkfx, entry1gjnK37XsjxFXURX_IhYkEafO8K3HWHiT were uploaded and folder metadata read back; their complete bytes are covered by the downloaded compact manifest. No sharing/schedule change or bearer URL storage.

Original core vendor: bc7babbb9e890f6d5a7094430a5fbdccf66c77ad, src/enterprise_math/brc_weighted_recurrent.py, blob4e6b3132580e3cd70a20a0d8bd4d28792b961afb, SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26. Exact checkpoint ancestor read: enterprise-math@951cc16c, research_notes/directed_recovery/20260927_C6438C/qft_row_queries/point_queries/CHECKPOINT_ROW_TRADEOFF.md, blob48f292b99fd253cbaf82105722620da917d84d91. BGL PRL128220503(2022), arXiv2112.08499 is the inherited amplitude-query sampling antecedent; only primary abstract/publication metadata were checked this turn. No worldwide novelty of checkpointing or rejection sampling is claimed.

## 7. Control and exact next unit

Actual logical conversation remains chat-stage101-c971348e64294a5882dfc50fcc8217f1. Recovery2517 succeeded only as local pointer read, Source authority unverified, old failed start stage101-session-c971348e-02, no runs/claims/staging. PRE_FINAL2518 was submitted on the same actual session prerequisite; its outcome is recorded separately in final delivery, not predeclared here. No new identity, RA, CLAIM, formal run/Result or independent review is asserted. Source persistence is not native registration or mathematical admission.

Completed units: exact nonlinear checkpoint substitution, fixed/rolling implementations, full finite row checks, declared sampling and time-to-factor blocks, explicit overflow, complete compact cloud recovery. Do not repeat them as discovery. Next: when complete support exceeds the row budget, construct a deterministic partial checkpoint with a proved aggregate pruning/merging error and correct sampling, separately charging certification, lost mass, mantissa error, gate error, retries and factor verification. Do not reuse complete-checkpoint missing-row-as-zero semantics without that new approximation proof. Parent research remains open.
