# RP2: bounded conditional-field mantissas and a certified output-law error

Progress-Event-ID: RP2-C971348E-518043AA
Date: 2026-09-27 Asia/Taipei
Status: AUTHOR_DERIVATION_AND_EXECUTION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global intake: 4b04602b7ca192bfe98acec55b81c0cf2b80e3af
EM intake: 3d2e729c4cce0f8df228795599266e4582be3505
Publication preflight: 5ce9ec55de03dff02b5ebf7dadf2bbc710abaf78
Scientific parent: cced867b76d106c34e5a610688f470c0b68d184e (RP1)
Scientific commit: 518043aa2170a8aac47692bac9e8480231c3796d

This additive portable note is not a formal Task/Result, independent review, Foundation promotion or parent-objective closure. It continues the user's low-precision useful-ridge direction. P000 is unchanged. The executable parent is the verified RP1 cloud delta, not the distinct Stage105633fc4b5 package whose full bytes were not recovered this turn. All2323 parent tracked files remain byte-identical.

## 1. New approximation, not a new classical propagator

Fix the actual fully certified12-bit BRC bank at levels2..16, retaining61 signed internal modes, work labels, actual temporal gate order and actual root4-squared level3. Scientific actions use the inherited signed BRC extension. No new classical phase reference, trigonometric input, raised precision or known-order tuning is used.

The state is the complete nonzero conditional integer field AFTER a classical bit history. Its common positive scalar is irrelevant only to the declared future linear operations and normalized conditional readouts at that same history. Full-law enumeration retains the history probability separately. Independent per-row scaling is not allowed. The approximate sampler executes the unchanged BRC observation, draws its actual bit, and rounds the entire selected child after each nonterminal round. Rounding consumes no scientific RNG. The terminal child need not be formed to return k and run the unchanged exact factor verifier.

This is a lossy conditional-state representation, not an invertible codec of original residuals. Old raw-denominator or suffix recipes do not recover discarded tails. Future coherent recombination of different classical histories and physical-time interpretation are outside this contract. Random-source exhaustion returns an explicit partial record; a persistent resumable cursor is not claimed.

## 2. Quantizer and proof

Let B=max_j bit_length(abs(x_j)), K>=2. If B<=K, keep x. Otherwise set s=B-K and round every x_j/2^s to nearest integer, ties away from zero. If a rounding carry exceeds K bits, increment s once and repeat. The largest coordinate guarantees nonzero z, and each retained magnitude has at most K bits. All work rows share the SAME scale. Zero rows produced by this approximation may be omitted with their error charged.

For n=61 times the input work-row count, x'=2^s z gives ||x-x'||/||x||<=sqrt(n)2^(1-K). With the inherited full BRC norm Q and signed pairing J,

    delta(x,z)^2 = 1 - J(x,z)^2/[Q(x)Q(z)]
    delta(x,z) <= min(1,sqrt(n)2^(1-K)).

The latter follows by projecting x onto the ray of z; its orthogonal residual is no larger than ||x-x'||. Retain each classical history and its normalized pure conditional state in a direct sum. The same history-controlled BRC instrument contracts trace distance. Rounding the approximate children changes it by their approximate masses times delta. Triangle inequality and Cauchy-Schwarz therefore give

    TV(P_K,P_exact_same_bank) <= sum_i E_approx(delta_i)
      <= sum_i sqrt(E_approx(delta_i^2))
      <= min(1,(t-1)*sqrt(61*(N-1))*2^(1-K)).

The last bound uses unit input, actual modular permutations and support in nonzero residues. It requires neither the unknown order nor a positive lower bound on all conditional branch masses. It is a rounding bound relative to the SAME12-bit bank. A comparison to actual64 or an ideal model requires a separately proved bank/model error term.

For the success event G of the unchanged exact factor verifier, P_K(G)>=P_exact_same_bank(G)-TV. Error0.01 means an absolute probability difference of at most one percentage point, not99% factor success or1% relative loss.

## 3. Executed complete-law checks

Cases21/2/t10,33/5/t10,77/2/t10: the uncapped projective implementation exactly matches every one of each inherited RP1 bank12's1024 terminal probabilities. N33 and N77 use a reduced diagnostic width, not their default factorization width. Caps8/12/16/20 then give12 new complete distributions,12288 terminal probabilities and12264 nonterminal rounding certificates. Every distribution is exactly normalized and nonnegative. The offline verifier-success mask is never passed into quantization or cap selection.

|N/a/t|Uncapped success|K8 success|K16 success|TV K8|TV K16|
|---|---:|---:|---:|---:|---:|
|21/2/10|0.329670380754|0.329595466983|0.329670397667|0.000366969692|0.000002232614|
|33/5/10|0.391121169767|0.391034996963|0.391121000227|0.000551225563|0.000001595713|
|77/2/10|0.241655384880|0.241602562527|0.241655360353|0.000763030405|0.000001660349|

The displayed decimals are renderings of stored exact fractions. At K16 the tighter offline mass-weighted bounds are0.000155673828,0.000133468769,0.000157796312. The offline square-root upper bounds use actual BRC bracketing with dyadic upper endpoints. The uniform K8 bound is trivial for these cases; small empirical error does not prove universal8-bit sufficiency. Uncapped stored integers reach777 bits; capped states meet their exact K limit. This is not proof of an internal geometric ridge locator.

## 4. Choose K from an error budget, without fitting or order knowledge

Set R=ceil(sqrt(61*(N-1))) and choose the smallest K>=2 with (t-1)R/2^(K-1)<=epsilon. An integer candidate R is checked with actual BRC square_probe at R and R-1. The code uses exact Fraction and integer bit_length, not floating thresholds. Its minimality concerns this conservative bound, not the actual necessary precision.

|N|Default t|K for epsilon0.01|K for epsilon0.001|
|---|---:|---:|---:|
|21|10|16|20|
|77|14|18|21|
|91|14|18|21|
|143|16|19|22|

N143/t16/K19 yields705/131072<0.01. This post-main proof application was separately declared and does not retune primary measurements. It executes8 choices and5 invalid-input rejections. A signed two-arm BRC witness has plus probability9/10 at arms(1,2), but1 after separate rescaling to(1,1). This is an interface counterexample, not a claimed observed Shor prefix. The policy and counterexample produced11 new core receipts.

Sufficient K scales as O(log t +0.5 log N+log(1/epsilon)); this is a precision statement, not polynomial total simulation cost. It does not authorize a fixed constant K at every N.

## 5. Held-out sampling and honest resource accounting

Inputs85/2/t14,91/2/t14,143/2/t16;32 seeds each, base202609271060000+case_index*10000+sample_index. Caps None/12/16/20, three alternating-method-order repetitions.1152 executions contain only96 distinct input/seed pairs. Banks are already certified; timers include factory/lease/program/driver preparation and32 full-field samples with exact factor verification. Comparisons and evidence encoding/I/O are outside timing. Each same-cap record exactly replays across the repetitions.

|Case|Uncapped seconds|K12|K16|K20|
|---|---:|---:|---:|---:|
|85/2/t14|0.045249990|0.046440700|0.046040470|0.045852842|
|91/2/t14|0.145442941|0.133890360|0.135454885|0.131001565|
|143/2/t16|1.309781004|1.210455767|1.229248409|1.212633888|

At N143/K16 retained integers fall from1922 to16 bits and measured raw action peaks from1936 to280 bits; median batch time decreases about6.1%, not120-fold. N91/K16 decreases about6.9%. The N85 paths already retain1-bit values and become slightly slower. Three repetitions do not establish a universal timing advantage.

Success counts per32 seeds are12/12/12/12 for N85,11/7/12/11 for N91,9/10/10/7 for N143, ordered None/K12/K16/K20. These are NOT exact probabilities. Different rational sampler denominators may consume the same seed differently; this is not a tight cross-precision coupling, nor a same-trajectory arithmetic-only benchmark. No complete high-width law is claimed.

This baseline is the same complete-field, no-suffix sampler, not the fastest previously optimized suffix or point-query algorithm. Initial bank certification was separately observed at3.200691256s,1233 actual core calls; it is excluded from the table and is not a full cold-process time-to-answer study.

K bounds only stored field magnitudes at nonterminal boundaries. An actual raw word at fixed gate precision b12 is conservatively bounded by K+24(t-1)+4 bits including the subsequent arm addition. Probability numerators/denominators, labels, certificates, events, bank/proof caches, transient fields and RSS are separate. Work-label count has NOT been reduced.

## 6. Validation, artifact and actual Drive readback

Primary safety:62 quantizer/input/exhaustion checks;3 original-sampler/no-cap probability, tape and RNG equivalences;3 full-field rounding witnesses validated using inherited BRC norm/pairing with289 new core calls. Main process retained68986 core receipts across construction, diagnostics and timing; these are not independent samples. A read-only smoke reconstructs all1024 K16 probabilities and weighted depth errors for N21, replays the first N143/K16 full sample record, and rechecks the uncapped N77 original sampler. That smoke process used2215 actual core calls.

Full chat bundle BRC_RidgePrecision_RP2_20260927.bundle:244949788 bytes, SHA2564d08953d7cb2e8f3d0e1fe3e299a768a14335c20f593c0268210a772011637e7. It is standalone and a new local clone verified its88 hashed new entries,12 laws and2323 unchanged parent files.89 new tracked files include the manifest itself.

Drive folder1g_wxbXPwPtslJG8nw5RLURt3oLeUuGaO, RP2_逐轮尾数与误差证书_20260927, under the existing root19dd_3frjJu-MeL-eD-UKuNYdCo5cTZXP. Delta BRC_RidgePrecision_RP2_20260927_delta.bundle:5657661 bytes, SHA2567ec7644ebf4ac495c31de7458316d33864717eeadba8b672b68d198a42400ecd, Drive file1aPfvXfOGHqxe4eVRfXQpOXWOCXzSWwif. It REQUIRES RP1cced867b and is not standalone.

The RP1 delta was downloaded this turn from file16Yrd_zATVH4_y1MUUKj4cLt-gVKKtnK5 and checked against SHA256986683395590b0d213a64cfe8e52d39d048fb3003aa3950ee431b70eed5d8f31. RP2 was uploaded, downloaded and fully hash-checked, then applied with that cloud RP1 delta to a fresh clone of the mounted, hash-reverified Stage104 full bundle. All88 entries, unchanged parents/vendor and the actual smoke above passed. This is author recovery, NOT independent replication. The older Stage103/104 cloud chain was not all re-downloaded this turn.

Report1WSjyyj62UGyG41um5NQkJ-XgB0hIxvNo, proof1FDt624whdHFdtfHmHP5tqhXWO20npNvt, results1MIgcnJRl3DVJJoeCXXUeHyEXnx-P7mwW and entry1SACMwv1CNs-tNqx0iWIxQjyto3U66jKc have actual uploads and folder metadata readback; their full bytes are additionally covered by the downloaded delta manifest. No sharing or scheduling change was made.

The five available Stage105 report/proof/results/image/delivery files were separately archived, uploaded and downloaded as Stage105_available_materials_NOT_full_bundle.zip,258828 bytes, SHA256d488308b9db31b64339ec47c637a54b4b9f43906d58274961fce868b0b7e2a75, Drive file1On_1uA68rKYypQPCEkDO6fX-xZoVzZTd. This does NOT recover its missing full scientific bundle or establish its complete independent reproduction. Conversation/Library retrieval did not locate that named bundle; related files were not substituted for it.

Core vendor remains commitbc7babbb9e890f6d5a7094430a5fbdccf66c77ad, blob4e6b3132580e3cd70a20a0d8bd4d28792b961afb, SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26.

## 7. Control and next research unit

Own logical conversation remains chat-stage101-c971348e64294a5882dfc50fcc8217f1. Recovery Issue2500 reports the old local binding, no runs/claims/staging, source_authority_verified=false. PRE_FINAL Issue2501 actually returned REJECTED/PREREQUISITE_NOT_SUCCEEDED; request SHA256939d01d64a7d9f922d059048297648571e5dc63946e43ba4e2e1ad3598bd9678. No new identity, RA, CLAIM, formal run/Result or final_allowed is asserted. Failed actions are not replayed through a different identity.

Do not repeat the completed gate precision sweep, current quantizer proof, fixed12 distributions or declared sampling block as discovery. Next: consistent approximate row/query representations that avoid full work-field scans while retaining a proved aggregate error contract, or an online tighter cap certificate whose cost is honestly measured. A K-bit full-field theorem alone is not a cheap point-query oracle, a polynomial classical Shor algorithm, a single-ridge locator or a physical/hardware conclusion.
