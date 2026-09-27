# RP6: exact coherent value families and counted modular intervals

Progress-Event-ID: RP6-C971348E-4C570759
Date: 2026-09-27 Asia/Taipei
Status: AUTHOR_DERIVATION_AND_EXECUTION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global read snapshot: 52978d9a04c50d038d9f7caef6ef502561d99fe0
EM control intake: ea7426cf4c0a0d6a8d9646cb9f053519c8567fc1
Publication preflight: d565811967777f39ab827fc03deff257fa839abe
Scientific parent: dd2baac15a04da561d9c4affbfa956ae0e7e600b (RP5)
Scientific commit: 4c5707594ae41d184cbb3374b0fb19d43e09f27b

This additive note is not a formal Task/Result, independent review, Foundation promotion or parent-objective closure. P000 and actual BRC-only constraints remain unchanged. All 2965 parent Git files and 2134 inherited compact-runtime files are unchanged. Actual b12 BRC gates, complete 61 signed modes, exact dyadic exponents, modular labels, temporal feedback order and original nonterminal Q_K boundaries are retained. Primary K16. The target is RP3/RP5 no-prune whole-trial filtering, not RP5 top-R pruning. No new classical phase/reference calculation, precision increase or known-order/factor tuning was used.

## 1. Exact value families, including incidence

At a fixed classical history, partition all nonzero work labels into disjoint sets C_i on which the complete canonical Dyad is v_i. Store each v_i once plus the entire label-to-value-ID map. Equality uses all 61 mantissas, their signs and the exact exponent; hashes only locate candidates. Decode(Encode(field)) equals the complete field. This is lossless sharing of an already approximate target, not recovery of discarded low bits.

For the actual permutation P and ordered feedback T, add the conceptual zero value and partition the active union by B_ij={w:u(w)=v_i,u(P^-1 w)=v_j}. Every label in this cell has raw child a_ij,b=(v_i+(-1)^b T v_j)/2. Apply Q_K at its original boundary, then re-intern equal results. Substitution and induction prove the identical row function for all legal inputs in scope. The branch mass is sum_ij |B_ij| norm(a_ij,b)^2; its quantized counterpart uses norm(Q_K a_ij,b)^2. Coherent signed joins precede squaring. Therefore original conditional-bit and whole-trial acceptance probabilities, and same-tape attempts/events/postprocessing/RNG, are unchanged. No new approximation error is introduced; bank-versus64/ideal error remains separate.

For S active labels, G complete distinct values and J nonempty incidence cells, J<=min(2S,(G+1)^2-1). One layer uses at most G times the word length actual internal gate applications and two joins per incidence cell, but still S typed modular requests and explicit label-index work. G small is not guaranteed; this is not a total-time or total-memory bound.

An actual interface counterexample uses N15/a2/t4, history(0,0,0), empty feedback and next multiplier2. The field e0 on labels{1,2} and the field e0 on{1,4} have the same shared value, multiplicity2 and squared norm2, but actual plus-bit probabilities3/4 and1/2. Their intersection with their multiplied support has size1 and0. The inherited prepared evaluator, family evaluator and dedicated positive BRC norm witness agree. This is not asserted to be a prefix reached from the standard initial state. Values and multiplicities alone are insufficient: label incidence must remain.

## 2. Actual compression and its unfavorable counterpart

N251/a6/t16 is a PRIME support-pressure control, not a factoring benchmark. Along the all-zero history, depths6/7/8 have (labels,distinct complete values)=(64,1),(125,2),(125,2). At depth6 vector slots fall3904 to61 while all64 labels remain. Observed recursive retained-object accounting, including a proxy-dictionary charge, is48456 versus5290 bytes; this is not RSS or a64-fold total-memory claim. Alternating(1,0,...) histories give(64,64) and(125,125), and the family representation is larger. No claim that the favorable all-zero history has large sampling probability is made.

## 3. A special exact coherent family with charged membership cost

At the all-zero prefix of length j, the square schedule gives gamma_j=a^(2^(t-j)) modN and gamma_(j-1)=gamma_j^2. Even/odd interval induction yields u_(0^j)(w)=2^-j M_j(w)e0, where M_j(w)=#{0<=q<2^j:gamma_j^q=w modN}. When j<=K, canonical odd parts of these counts fit K bits, so the original Q_K does not alter the formula. Counts, not only membership, are required. Nonzero feedback histories are outside this special formula.

For an arbitrary unit gamma and interval length L, let m=ceil(sqrt(L)). Store all indices r<m for each residue gamma^r, without overwriting short-order collisions. Write q=am+r. For a=0,...,ceil(L/m)-1 query w gamma^(-ma) and count its baby indices r<min(m,L-ma). Uniqueness of this integer decomposition proves the exact multiplicity, including an incomplete last block, without order or factors as inputs. All modular actions and the giant inverse use inherited BRC-certified DemandPermutation/Bezout interfaces.

Construction uses m typed edge requests; one row count uses ceil(L/m)-1 giant inverse requests, plus separately charged inverse certification, lookup and bit costs. Memory includes m indices and up to m residues. At N251/t16/j12, L4096 gives64 stored baby indices and63 giant inverse requests per queried row. This remains O(2^(j/2)) group-level work, not polynomial in j. Querying every label may cost more than building one explicit field. The method is not a general feedback sampler.

1136 full-carrier count/row comparisons passed: N251 at depths6/7/8/12 and short-order/tail-block cases(15,2,100),(21,2,13),(35,2,25). N15/gamma2/L100 returns count25 at label1. References use actual typed exponent enumeration and the actual forward BRC field. Generic baby-step/giant-step and repeated-value compression are prior art, not claimed worldwide novelty; primary abstracts of Viamontes/Markov/Hayes quant-ph/0309060, Bach/Sandlund1612.03456 and inherited BGL2112.08499 were checked, not full-text novelty completeness.

## 4. Exact finite equivalence and negative timing result

Six diagnostics, N21/t6,N33/t6,N77/t8 with K6/16, verify154752 complete padded-domain row comparisons,1531222 nonzero component comparisons,1524 branch/certificate checks and768 terminal probabilities. These are equivalence checks of existing target laws, not six newly discovered distributions. All masses and full rows are retained exactly.

Four new cases143/209/221/253, a2,t16,K16, eight seeds each: base202609270850000+case_index*10000+j. Five synchronous process repetitions each build the actual bank before timing and alternate method order. 320 sample executions contain only32 distinct case/seed settings. Timers include per-sample program/engine setup, all attempts, factor verification and event collection; bank construction/imports, comparisons, encoding and I/O are excluded. Complete attempts/events/random requests/RNG match both methods and all repetitions. Median seconds per8 outputs:

|N|Original no-prune field|Value families|
|---|---:|---:|
|143|0.733524055|0.824929382|
|209|3.152687774|3.382684749|
|221|0.223317519|0.236721116|
|253|3.859449170|4.059290009|

The current prototype is slower in all four cases, by about5.2%-12.5%. N143 first-repetition cumulative label/value inputs1680/1472 and N2534904/4146 show limited repeated complete values; index/hash/allocation overhead is not repaid. The slow N209 baseline observation5.602216117s remains in the raw data. No outlier exclusion or favorable selection was used. Each batch's verified-factor counts3/0/5/3 are identical across methods; they are not exact probabilities or a time-to-factor study. No rejected trials occurred in these fixed timed sample paths. The separate three-seed pilot is excluded.

17 safety checks cover signs/exponents, malformed/immutable maps, cap settings, exhaustion and actual method substitution. The hot norm path is the unchanged inherited signed direct-sum extension, not a newly constructed positive graph per score; dedicated witnesses use the original positive BRC observer. StreamingExecNotEnabledContainerError occurred before timed execution, leading to synchronous blocks. The interval checker initially missed a canonical import; the failed log was preserved, the import corrected and complete checks rerun. No scientific engine edits followed the timed measurements. Source hashes, every process's receipts, full rows, raw timing records and plans are retained.

## 5. Actual artifacts and Drive roundtrip

Standalone run ZIP BRC_RidgePrecision_RP6_RUN_20260927.zip:26407738 bytes,SHA256 f65b9d0168255d9d3b27980a118a1abcaaa444c9fb615d70f4209913805907a2. Contains2251 payload files including2134 inherited and117 new;116 new manifest entries. Runs without a parent bundle, but does not include the entire historical Git/evidence archive. Entrypoint START_HERE_RP6.md.
Delta BRC_RidgePrecision_RP6_20260927_delta.bundle:4548756 bytes,SHA256 b986417dd14c1c6352c87133351a339dda7ab4d1141d6905650f0be5bb6c34e0. Requires RP5 dd2baac1, NOT standalone. No new full historical bundle is claimed.

Drive root19dd_3frjJu-MeL-eD-UKuNYdCo5cTZXP; folder1WLRLUXk09YtX1ATrHhVmxWZhQIYB_u9c (RP6_相干值族与模幂区间_20260927_4c570759). ZIP file1qliS20GIp3wKdEYKBZINIupTewPzmP-x was uploaded, metadata-read, downloaded, fully size/SHA checked and extracted in a NEW directory. All2134 parent pins and116 new manifest entries verified, followed by actual smoke: complete N21/t6/K16 law/every transition, N143 first full sample/attempts/tape/RNG and short-order multiplicity. This cloud smoke used2153 actual core receipts. The source-workspace smoke separately passed. These are author recovery checks, not independent replication.

Delta file1Nu0G2bvm84xQemT8zTYh3wNRMzbnM5ps was uploaded, downloaded, size/SHA checked and git-bundle verified against the parent. No separate delta-chain smoke is claimed. Report1MxtN6qK_NPWhUOecL5HxrH3h6QthO8ME, proof1URqZ8goPiGNMNq4z2z9XBzEAS4tZDEZU, results1BEVLQHQIgul9wvRiccyPxRGTuIJPGzyM and entry1mWLW2q58OvQF2SXd0blPgWC2LXgchuYw were uploaded and directory metadata read back; their complete bytes are covered by the downloaded ZIP. Permissions and schedules are unchanged. No bearer URLs are stored. Final delivery receipt is separate from the hashed package.

Original vendor remains bc7babbb9e890f6d5a7094430a5fbdccf66c77ad:src/enterprise_math/brc_weighted_recurrent.py, blob4e6b3132580e3cd70a20a0d8bd4d28792b961afb,SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26.

## 6. Control and exact continuation

Own logical conversation remains chat-stage101-c971348e64294a5882dfc50fcc8217f1. Recovery2521 is SUCCEEDED only for local pointers, Source authority unverified, existing failed original start stage101-session-c971348e-02 and no runs/claims/staging. PRE_FINAL2526 was submitted on the same prerequisite; actual outcome is recorded separately in final delivery. No new identity, RA, CLAIM, formal run/Result, independent review or final_allowed is asserted. No refused action was replayed through another identity.

Completed: exact complete-value/incidence codec, actual pressure and incidence witnesses, special zero-feedback interval/multiplicity query, finite equivalence, negative declared benchmark and cloud recovery. Do not repeat these as discovery. Next: a certified approximate or parameterized vector family retaining ALL label incidence. An average/projection may increase an individual row norm, so the old rowwise acceptance ratio cannot transfer without a new sampling proof. Charge family fitting, label representation, collision and error certification. No generic cheap row oracle, internal ridge locator, polynomial classical Shor or physical/hardware advantage has been established. Parent research remains open.
