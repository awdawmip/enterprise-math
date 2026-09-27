# RP3: row-local mantissas, exact whole-trial filtering and an honest query-cost boundary

Progress-Event-ID: RP3-C971348E-182592BF
Date: 2026-09-27 Asia/Taipei
Status: AUTHOR_DERIVATION_AND_EXECUTION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global intake: bd2873d755d8947f7a5566222ccc7b01a4ba89f9
EM control intake: eeb6a16992a6a9d99bfaa7df5a199e19ff77913b
Publication preflight: 9fcdbe1ad147a125464ae35fcf1dff493cec505d
Scientific parent: 518043aa2170a8aac47692bac9e8480231c3796d (RP2)
Scientific commit: 182592bf660e5f1536cea24b6a2072145c69636e

This additive note preserves portable author research, not a formal Task/Result, independent review, Foundation promotion or parent-objective closure. P000 and actual BRC-only semantics remain unchanged. The user-directed objective is low-precision useful output structure, not equality of every high-precision field component. All2412 parent tracked files remain byte-identical. This target differs from RP2's common-scale nearest-rounded conditional field.

## 1. Consistent per-row approximation without a full-field scaling scan

Fix the actually certified12-bit BRC bank, levels2..16,61 signed internal modes, work=1/e0 initial state, actual modular permutations and time-ordered feedback. Level3 remains the square of actual root4. A row is (n,e), representing2^e n with61 signed integer mantissas and an exact integer exponent. Different rows may have different exponents, but every join, norm and gate retains them. This is not independent normalization with the scale erased.

Let B=max_j bit_length(abs(n_j)). For B>K, set s=B-K, truncate each signed magnitude toward zero after division by2^s, and increase e by s. Strip common powers of2 losslessly. The largest component survives; every retained nonterminal mantissa has at most K bits. Terminal rows are not truncated. Q_K is norm-decreasing and satisfies ||Q_K(x)-x||<=rho||x||, rho=sqrt(61)2^(1-K)<=rho_bar=8*2^(1-K). Squaring and summing rowwise retains this same relative bound, without a sqrt(number of work labels) factor.

The deterministic raw recursion is a_hb(z)=[u_h(z)+(-1)^b T_h u_h(P_i^-1 z)]/2 and u_hb(z)=Q_K(a_hb(z)) at nonterminal levels. No full-field maximum, conditional norm or support enumeration is required by the row-query interface. Every answer depends only on bank/K/history/work, not the private walker or request order. Cache misses recurse; they never mean zero. No new classical phase/reference computation or known-order tuning was used.

## 2. Exact killed-trial correction of the approximate target

Reuse the native two-row latent-label proposal: a fresh fair coin proposes z=W or P_i W, query x=u_h(z), y=T_h u_h(P_i^-1 z), let S=||x||^2+||y||^2 and draw b with p_b=||x+(-1)^b y||^2/(2S). Let a=(x+(-1)^b y)/2 and q=Q_K(a), except q=a terminal. Accept this step with the exact rational alpha=||q||^2/||a||^2<=1. On rejection end the WHOLE trial; a subsequent trial begins at the original initial state, with fresh random draws. Attempt and random-source exhaustion are explicit records, not silent successes.

The unconditional surviving mass at(h,z) is exactly||u_h(z)||^2. Proof by induction: proposal mass is S/2; multiplying by the bit probability2||a||^2/S yields||a||^2; multiplying by alpha yields||q||^2. This includes proposal multiplicity when P_i fixes W. Thus the terminal survival probability is Z=sum_(h,z)||u_h(z)||^2 and accepted samples have exactly the joint law||u_h(z)||^2/Z. Neither Z nor a full-field norm is evaluated online. Exactness is to this defined low-precision target, not to the untruncated model.

An actual BRC-norm witness rules out retrying only locally while retaining W: equally weighted norm25 rows(3,4,0,...) and(0,5,0,...) truncate at K2 to norm20 and16. Whole-trial filtering gives label probabilities5/9,4/9; retaining the original labels and retrying locally gives1/2,1/2. This is an interface counterexample, not a claimed standard Shor prefix.

## 3. Output-law and retry-cost guarantees

The history-controlled full BRC instrument is an isometry on the direct sum of histories/work/internal modes. The approximate raw family U_i has norm at most1. For exact V_i, triangle inequality gives eta_(i+1)<=eta_i+rho_bar. There are at most t-1 truncations. For unit V and nonzero U, normalized pure-state trace distance is the distance from V to the line of U, hence at most||V-U||. Measuring outputs therefore gives

    TV(P_RP3,P_exact_same_bank)<=min(1,(t-1)*8*2^(1-K)).

For rho_bar<1, reverse triangle inequality at each truncation gives

    (1-rho_bar)^(2(t-1))<=Z<=1,
    E[whole trials until a surviving sample]<=(1-rho_bar)^(-2(t-1)).

If(t-1)rho_bar<=epsilon<1/2, then Z>=1-2epsilon. For the unchanged exact factor-verification event G, P_RP3(G)>=max(0,P_exact_same_bank(G)-epsilon), and per-trial verified-factor probability is at least(1-2epsilon)max(0,P_exact_same_bank(G)-epsilon). All failed trials and verification costs must be counted. Survival is NOT factorization success. A supplementary bound eta_t^2<=(t-1)(1-Z) follows from squared truncation error being at most the raw mass loss; Z is not a free online certificate.

No fitting, order or factor is used to select K. For absolute rounding-TV budget0.01, t10/14/16 give sufficient K14/15/15, bounds0.0087890625/0.00634765625/0.00732421875, and expected-attempt upper bounds below1.017743/1.012780/1.014760. At t16,K15 the TV bound is15/2048. Additional t128 and2048 checks test the formula only, not a constructed large bank or sampler. Sufficient K=O(log t+log(1/epsilon)) for this fixed61-mode carrier. This does not establish universal fixed K or fixed carrier construction at arbitrary scale.

This is a SAME12-bit-bank truncation bound. Bank-to64/ideal error is separate. It does not prove generic factor success, a geometric ridge locator, cheap row queries, polynomial classical Shor or a physical/hardware advantage. For dyadic gate-denominator budget H_i=i+sum_(j<i)L_j, reachable nonzero exponents lie in[-H_i,0]; exponent storage is O(log(1+H_t)) bits. Aligned temporary integers may have O(K+H_t+max L_i) bits. Probabilities, labels, evidence, caches and RSS are not K-bit resources.

## 4. Complete finite checks

Frozen diagnostics:21/2/t6,33/5/t8,77/2/t8; caps6/8/12/16. All are reduced diagnostic widths, not default factorization widths. Twelve full laws contain2304 terminal probabilities,408704 raw-query/full-field row comparisons,61700 surviving history/work joint-mass checks and20052 truncation certificates. Every accepted law is exactly nonnegative and normalized; all missing/unreachable work rows were included in point-query comparisons. Uncapped queries also match the unchanged full BRC instrument. Six selected complete-row norm/error witnesses were run through the inherited actual BRC norm interface. Safety includes44 input/quantizer/cache/retry/exhaustion checks.

|Case|K12 TV versus no truncation|Full-trial survival Z|Accepted verified-factor probability|
|---|---:|---:|---:|
|21/2/t6|0.000273090413|0.999250324527|0.287663462902|
|33/5/t8|0.000340010014|0.998488621476|0.363584040537|
|77/2/t8|0.000144186598|0.998696493580|0.128785177148|

K16 TVs respectively0.000013515751,0.000019208882,0.000009922270. Displayed decimals render retained exact fractions. These are finite-law calculations, not empirical frequency confidence bounds. Full-field norm sums are used OFFLINE for verification, not granted to the online query sampler.

## 5. Performance: the prototype is not a net speedup

One separate N143/t16/K16 pilot had262108 computed nodes without memo versus1082 with512 entries; full events, attempts, random requests and RNG state matched exactly. These are pilot counts, excluded from the repeated timing medians. No-memo recursive work can be exponential: one depth-i query has at most2^(i+1)-1 visits. Two top-level queries per bit are not a cheap-oracle guarantee.

After the pilot, AMENDMENT_SAMPLING was frozen before formal timing: memo512 retains8 seeds/case, no-memo uses only the same first seed. Two cases N77/a2/t14 and N143/a2/t16, caps12/16, three alternating-order repetitions. Primary108 executions contain16 distinct input/seed pairs. A separately declared same-target full-field comparator adds96 executions of those same16 pairs. The full-field comparator has126 exact transition-target checks. The two samplers have the same target but different random consumption and trajectories; same seeds are not a pathwise coupling.

K16,8 accepted samples per batch, three-repetition medians:

|Case|Point queries with512-entry memo|Same-target full-field filtering|
|---|---:|---:|
|77/2/t14|0.734986274 s|0.468711576 s|
|143/2/t16|1.849465272 s|0.687092820 s|

The current query implementation is slower. The full-field block ran AFTER, not interleaved with, the primary query blocks. Banks were already certified; timers include fresh driver/factory/program/query setup, all recorded trial/retry work, postprocessing and event collection, but exclude result comparison, encoding and file I/O. Helper caches retain ordinary behavior; GC is enabled. No new complete cold-process or time-to-verified-factor comparison is asserted.512 is an entry limit, not a memory-byte bound. The full-field comparator is not claimed to be the fastest inherited suffix/query implementation.

An initial container context ended at its tool limit after four complete laws. Their bytes/logs were preserved; work resumed at the next unfinished case with a rebuilt actual bank. The first context's final global core-call trace was not recovered. The continuing context retained1365212 core-call records plus explicit BRC witnesses. Incomplete work is not counted as completed timing. Final integrity/smoke checks execute delivered code; no favorable timing selection or silent redefinition of prior samples.

## 6. Actual artifacts, Google Drive roundtrip and source ancestry

Full standalone chat bundle BRC_RidgePrecision_RP3_20260927.bundle:256500582 bytes; SHA256 bf962ab7fdfa3d9c355d68b3543f3a5a52d8ef11f34f5405577d9eafc65f74b8.
Drive delta BRC_RidgePrecision_RP3_20260927_delta.bundle:11477330 bytes; SHA256 5b0b7c3a439a6a84f78f08a45f7dfab6a3055da4ebf9c507d237bdcb5320a813; REQUIRES RP2 parent518043aa and is NOT standalone.
Entrypoint START_HERE_RP3.md.92 new tracked files comprise91 hashed entries plus the manifest. Includes source, full signed rows, all exact probabilities, positive/negative results, core-call evidence, plans/amendments, raw timings and resource/recovery limitations.

Drive root19dd_3frjJu-MeL-eD-UKuNYdCo5cTZXP. New folder1h0fp-SKF9bmPQ_QV_M0az933Tcd8RqGA, named RP3_逐行查询与整次校正_20260927_182592bf. Delta file1VG9uUYsj-dMmHMhwMeipoQzVOZI_24gq was actually uploaded, metadata-read, downloaded through Google_Drive.fetch with raw bytes and fully hash-checked. It was fetched into a NEW clone of the hash-reverified mounted RP2 full bundle. All91 manifest entries,2412 unchanged parent files and original vendor passed, followed by actual smoke: all64 probabilities and killed-joint law at21/t6/K12, full N143/t16/K16 attempt/events/random tape, memo clearing and t16/K15 cap. This smoke used3001 actual core calls. A separate new clone of the full RP3 bundle passed the same checks. This is author recovery, not independent replication, and the full older cloud parent chain was NOT re-downloaded this turn.

Separate readable uploads with folder metadata readback: report1_x2TB-rE2TxEKzI91n2DhagMycBVDIy3, proof1-XiW23jaXcZvsC0nquLcoY4oToj33lfc, results1xu9Xol6USutOscUsmynf2L8iQz2cacwR, entry1AfcAevp02ADNGU8IjqGbBXI02RgRBBrt. Their bytes are also covered by the downloaded delta manifest. No sharing or schedule was changed. Final delivery receipt is separate to avoid a self-hash dependency; no bearer URL is stored.

Original BRC vendor: bc7babbb9e890f6d5a7094430a5fbdccf66c77ad, src/enterprise_math/brc_weighted_recurrent.py, blob4e6b3132580e3cd70a20a0d8bd4d28792b961afb, SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26. The two-row proposal is inherited from C6438C@951cc16c/qft_row_queries and Bravyi-Gosset-Liu, PRL128220503(2022), arXiv2112.08499. This turn verified primary abstract/publication metadata, not the complete supplement. Generic rejection sampling is not new here. Novelty-completeness is not claimed.

## 7. Control and precise continuation

Same actual logical conversation chat-stage101-c971348e64294a5882dfc50fcc8217f1. Recovery Issue2512 succeeded only as local readback, source_authority_verified=false, old failed start stage101-session-c971348e-02, no runs/claims/staging. PRE_FINAL Issue2515 actually returned REJECTED/PREREQUISITE_NOT_SUCCEEDED; request SHA2566d35104abed85ca1d118f2c31a8c0ff34b3165e7ecfa08fd8fc5e4fcab557ba1. No new identity, RA, CLAIM, formal run/Result or final_allowed is asserted. Persistence and byte checks are not native registration or scientific admission.

Do not repeat the RP1 gate sweep, RP2 common-field proof, this local quantizer/killed-law proof, twelve full laws or declared16 input/seed pairs as discovery. Next: integrate existing prefix-checkpoint/backward contraction with this same deterministic nonlinear row boundary; prove hit/miss answers identical, include checkpoint construction/storage, recursive work, rejection cost and verified-factor probability, and compare against the same-target full-field baseline. Lower precision alone is not the remaining missing complexity argument.
