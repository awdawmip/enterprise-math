# Stage102: executed static-bank reuse, byte-budget cache and full recovery

Progress-Event-ID: STAGE102-C971348E-52E8FFAC
Date: 2026-09-27 Asia/Taipei
Status: AUTHOR_EXECUTED / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global read snapshot: f44ed5959c92e6e088c61c102951d1ab2c5e98d4
Project read/preflight snapshot: d8447e4dc9c6500720c671649798e4ae08df2ae2
Scientific parent: 77ea65ba63bb30651382fbe215064a5f0e0644ba
New local scientific commit: 52e8ffac7853ee53a50d06d6cfdaf3542c59571c

This additive research note is a portable scientific checkpoint, not a Task/Result, independent review, Foundation promotion or parent-objective closure. P000 and the residual-faithful position are unchanged. All scientific actions reuse the actual inherited BRC signed/certified linear extension. No new classical phase/reference computation or ideal-root substitution was executed. All parent tracked files remain byte-identical.

## 1. Executed mixed-sampling improvement

The first byte-budget-cache prototype was slower despite hits. Its three epoch medians (seconds) were parent 1.6416/1.6681/1.5108, sequential 8MiB 2.1234/2.1607/2.0192, compiled 8MiB 2.1356/2.1444/2.0063. Negative results are preserved. Duplicate bank fingerprinting was one cause: 128 constructors took median 0.553551963s in the parent, 1.058610966s in the naive wrapper, and 0.560618820s after binding the already-computed parent fingerprints. Removing newly introduced work alone did not create a net improvement.

The successful increment is LiteralBankHandle: retain the exact immutable literal-word/coefficient payloads and their existing fingerprint values, but still check actual rotor type, scalar type/value, apply method, payload identity and same-root binding at each constructor. Retaining payload references prevents object-ID reuse. Foreign or changed scientific objects fail closed. Equal-content replacement tuples are conservatively rejected. The parent constructor code, defaults, keyword defaults and closure remain identical; only its local dependency binding is replaced. Parent module globals and scientific functions are unchanged.

Fixed cases (N,a,t): (15,2,4),(15,4,4),(15,7,4),(15,14,4),(15,2,8),(21,2,6),(21,8,6),(21,4,6),(21,2,10),(33,2,6),(33,5,6),(35,2,6),(39,2,8),(55,2,8),(65,2,8),(77,2,8). Last four are additional model-local held-out cases, not independent external validation. Each epoch interleaves eight cycles of these 16 cases, totaling 128 samples. seed=2026092700+epoch_source*100000+cycle*1000+case_index. epoch_source is 0,1,0: epoch 1 has new seeds; epoch 2 deliberately replays epoch 0 after the new-seed workload.

Seven repetitions with alternating method order; median seconds:

| Method | First epoch | New-seed warm epoch | Replay first seeds |
|---|---:|---:|---:|
| parent | 1.664753561 | 1.649544732 | 1.511236606 |
| static_parent | 1.124890427 | 1.131611685 | 0.996196832 |
| static_seq8m | 1.109164723 | 1.097668882 | 0.981380804 |
| static_full8m | 1.111431773 | 1.095119841 | 0.987328314 |

static_parent adds no cross-round full-row cache. The main 32-35% measured batch-time reduction is already due to static identity reuse, not phase multiplication. static_seq8m adds an 8MiB sequential full-row cache; static_full8m also uses inherited compiled operators. Bank and optional table are already loaded, while first-epoch handle/factory/executor setup is included. Equality checks and evidence encoding are outside timers. This is not a generic Shor or hardware speedup.

Fresh-process single-sample initial-prototype medians were parent 2.644809168s, sequential 8MiB 2.634635548s, compiled 8MiB 2.717216031s. Bank construction/certification costs about 2.5s; packed table load median 0.086627262s. These are NOT static-handle fresh-process tests. OS caches were not forcibly cleared; batch benefits do not eliminate initial bank certification.

## 2. Actual sampling census and exact cache keys

Across the 384 executions in the three-epoch census: 3998 whole-word requests, 1341 empty-word identities, 39 distinct ordered words including empty, 566 distinct full(word,row) inputs including 558 nonempty. Eighty nonempty keys repeat across different N/a/t cases. Every unique output was directly compared with the unchanged parent evaluator. First epoch 73/128 samples and new-seed epoch 68/128 samples used no nonempty phase action. Each epoch has 120/128 samples ending with a retained full suffix-restoration recipe. These 39 words do not replace the Stage101 exhaustive-tree census of 512 operators and do not bound all seeds or t. Maximum input/output integers are 2347/2860 bits.

For fixed actual bank B, ordered word w and complete 61-component canonical integer row x, cache M_B[(w,x)]=F_B(w,x), where F returns the parent's raw numerator ABI. Dictionary hashes only index; full tuples must compare equal. Type validation precedes lookup, excluding bool/int aliases. The inherited signed-dyadic factor, input denominator, endpoints, branches and history remain outside the cache and intact. Cross-work-label reuse is valid only because F_B depends exactly on w and x in this fixed namespace, not because norms or initial components agree.

Induction: a hit returns a previously exact F_B value; a miss evaluates that same function. Eviction, budget rejection or clearing only changes derived memo state. Thus every finite call sequence, full field, conditional probability, actual random request/rejection path and RNG state is unchanged. Empty words return x directly. This assumes a fixed verified bank and single-threaded execution, without scientific parameter changes during a sample; it is not a sandbox against arbitrary hostile Python mutation.

## 3. Byte budget: executed curve and mathematical boundary

Replay of the exact Stage101 full-recovery trace has 3038 requests, 17 empty identities, 3021 nonempty requests, and 1531 distinct nonempty inputs. Hence there are 1490 potentially reusable nonempty evaluations. Stage101's 1499 count additionally included nine empty-identity repeats.

| Budget | Nonempty hits / 1490 | Maximum entries | Peak conservative bytes |
|---|---:|---:|---:|
| 64 KiB | 5 | 10 | 65536 |
| 1 MiB | 65 | 78 | 1048576 |
| 4 MiB | 192 | 207 | 4194304 |
| 8 MiB | 340 | 335 | 8388600 |
| 16 MiB | 683 | 562 | 16777168 |
| 32 MiB | 1490 | 946 | 33554208 |
| 64 MiB | 1490 | 1531 | 66834296 |

32MiB is an observed sufficient budget for this trace, not a proved minimum or a universal choice. Variable-size eviction is not equivalent to the prior fixed-766-entry policy. All 7*3038 raw full-row outputs were compared with parent outputs.

Let A(C)=getsizeof(actual OrderedDict)+sum of complete entry charges, including all key/value tuples, integers and bookkeeping. Shared objects are conservatively overcounted. Let R(C) be an independent recursive identity-deduplicated reachable-object measurement. All reachable edges are charged, so R(C)<=A(C). On insertion evict LRU entries until A(C)<=B; release an empty dictionary. An individually oversized entry is evaluated but skipped without flushing useful smaller entries. Therefore at every public-call return R(C)<=A(C)<=B. This does not bound transient insertion/evaluation memory, allocator/RSS, live full residual fields, operation tables or inherited proof/local caches.

## 4. Full recovery and digest compatibility

N=21,a=2,t=10: complete control tree, all suffix restorations, common denominator reconstruction and requested digest. Three fresh-tree repetitions per method, alternating order, with bank/program already constructed. Full comparisons occur after timers. There are 2047 prefixes, 1024 terminals, 6140 final signed rows, 374540 final components and a 5409-bit denominator. Root-word semantic count remains 13803.

| Full path | Median seconds |
|---|---:|
| legacy reconstruction and decimal digest | 27.349295956 |
| exact-shift reconstruction, legacy digest | 20.736394268 |
| exact-shift reconstruction, binary V1 digest | 6.104829205 |
| exact-shift reconstruction, both digests | 21.124490071 |
| binary path plus sequential 8MiB cache | 6.175809505 |

Common-denominator reconstruction medians: old 6.710026259s, exact shift 0.285812993s. Decimal digest median 15.205785386s, binary V1 0.532383698s. About 4.48x full-verification throughput applies only when binary V1 satisfies the consumer's obligation. Keeping the old digest or both digests must retain its cost.

After the budget curve, predeclared Amendment C compared three paired binary runs: contemporaneous no-row-cache median 6.1815s versus 32MiB median 5.9989s. All 1490 nonempty repeats hit, but extra end-to-end savings are only about 3%, not the hit rate or isolated-operation saving.

Legacy full-state SHA256 remains 794a2b3118078012149153202ce1c06057d5e9229d5f0752a8b107039bcde41d.
Binary V1 SHA256 remains 9baee467d9aa8bd1ab34650132d44ea5a7d25c15edb6fdbdccb7696ff3b28e32.

Stage102 adds the strict inverse of the existing Stage101 binary encoding. It retains domain/version, dimension, denominator, row count, ordered endpoint labels and every signed component. Each integer has a sign byte, eight-byte magnitude length and shortest unsigned big-endian magnitude; zero is uniquely nonnegative with empty magnitude. Length delimitation, canonical integer form and strictly increasing labels give D(E(state,den))=(state,den), hence injective encoding. SHA256 is not an injectivity proof or full-state replacement. Negative zero, leading zeros, duplicate/out-of-order labels, truncation and trailing bytes are rejected; size bounds reject the whole document, never truncate a scientific value.

## 5. Evidence, integrity and delivery

Main comparisons execute 37632 samples but contain only 256 distinct(case,seed) combinations; repetitions are method controls and deliberate replay. Initial 16128 comparisons use matching digests of complete event/recipe/RNG encodings; later 21504 use direct complete encoded-field/random-tape/RNG comparison. Additionally: 384 direct census comparisons, eight full sampled-field restoration checks after clearing caches, 21 complete recovery runs, 38893 direct full-prefix comparisons, 7116260 final signed-component comparisons, 22156 direct raw action comparisons, 412 safety checks, and seven static identity/parameter mutation rejection classes. Four actual direct BRC actions preserve 710 native core calls. Prototype failures are retained, not counted as passes.

Vendor pin: bc7babbb9e890f6d5a7094430a5fbdccf66c77ad, src/enterprise_math/brc_weighted_recurrent.py, blob 4e6b3132580e3cd70a20a0d8bd4d28792b961afb, SHA256 7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26.

Standalone chat-delivered bundle: BRC_Heartbeat_Stage102_20260927.bundle
Bytes: 172861575
SHA256: 521fc97c22b9f5a38eb6ab5b913b71502d303468a973ad095cd9c90c750e4766
Commit: 52e8ffac7853ee53a50d06d6cfdaf3542c59571c
Entrypoint: START_HERE_STAGE102.md
55 new tracked files, comprising 54 hashed files plus the manifest. Includes full parent history, source, frozen plans/amendments, raw positive/negative timings, complete sample/row evidence and proofs. A fresh local clone verified all 54 manifest entries, unchanged parent files, exact BRC vendor, full smoke event/RNG and recovered states. This is author replay, not independent scientific replication. The complete 172MB bundle has NOT been uploaded to this GitHub repository or a cloud drive; this source note preserves the results, proof boundary and exact artifact identity.

Replay: git clone BRC_Heartbeat_Stage102_20260927.bundle Stage102; cd Stage102; python -S -m stage102.verify --smoke. Full experimental replay in another fresh clone: python -S -m stage102.run_all. Timings vary by machine; a rerun writes new evidence rather than asserting original byte-identical timings.

## 6. Control status and smallest continuation

Same real logical conversation: chat-stage101-c971348e64294a5882dfc50fcc8217f1. Stage102 status Issue2487 succeeded on v0.6.8 and reports existing local Researcher session MCP-96f924f41c514d25a77e39b46abe2044, start_request_id stage101-session-c971348e-02. It explicitly grants no Source research authority. No new CLAIM/run/RA or independent review is asserted. The earlier session_start was not succeeded. Stage102 pre_final Issue2490 was actually read back: adapter_status REJECTED, error PREREQUISITE_NOT_SUCCEEDED, request_sha256 af3c5fbcad8f8e787c3eb541b9f5f316cbb7b41e18b469e9c5a8713941c11bb8. No final_allowed receipt was obtained; no identity switch, fabricated closure or rejected-write replay was used.

Next portable unit: test invalidation/reissue lifecycle for multiple actual banks and expanded t, with explicit cold certification and byte-budget accounting. Do not repeat the completed census, representation proof or fixed-bank experiment merely to restore conversation context. This research note and chat bundle preserve the verified frontier while native registration/formal admission remains unresolved.
