# R5 — Complete minimax early-stopping profile by realized corruption budget

Date: 2026-11-18 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Extends the same-directory fixed-order early-stop minimax theorem. Scientific input remains frozen at 435e77af0d180eac32bd1f9c4c464bc4010b7551, exact 256x101 scalar count JSON SHA-256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b.

## 1. A stronger conditional-cost theorem

A fixed-order policy chooses its entire sequence of actions before observing any response. It may stop at an observation-dependent time and decode, but it must remain **certainly correct against at most f arbitrary unmarked corruptions**. Define W(f,r) as the minimum, over such sound fixed-order policies, of their worst-case **actually charged** stopping cost conditional on the realized transcript containing at most r corruptions under the true hypothesis, for any integer 0<=r<=f. Good observations may be any point of their declared nonempty good-response sets, even when corruption count is zero.

For a finite fixed prefix s, define d_s(a,b) as the number of query positions whose correct-response sets for distinct hypotheses a,b are disjoint. Let M(q) be the minimum total cost of a fixed batch satisfying d_s(a,b)>=q for every a!=b.

**THEOREM (conditional corruption profile).**
For arbitrary finite H,K, positive action costs, nonempty good-response sets, and integers 0<=r<=f,

**W(f,r) = M(f+r+1).**

The case r=f recovers the preceding minimax no-early-stop theorem. The case r=0 is a distinct sharp **clean-branch stopping** optimum, even though the decoder must be robust to f errors on other branches.

**Proof (necessity).** Fix a chosen action schedule and a prefix s for which some pair a,b has d_s(a,b)<=f+r. At every nonseparating position, choose a response in G(a,k) intersect G(b,k). Partition the d separating positions into sets A,B with |A|<=r and |B|<=f; such a partition exists since d<=r+f. On A choose a good response under b (so a takes at most r corruptions); on B choose a good response under a (so b takes at most f corruptions). This one transcript is consistent with true a and <=r actual corruptions, and simultaneously with candidate b and <=f possible corruptions. All its earlier subprefixes remain ambiguous. A decoder required to be f-sound cannot halt at any of them. For every prefix failing universal (f+r+1)-separation there thus exists an <=r-corruption run reaching beyond that prefix. Consequently the conditional worst-case cost of the schedule is at least the cost of its first globally (f+r+1)-separating prefix. Positive prices ensure the usual monotonicity in prefix length.

**Proof (sufficiency).** When a prefix satisfies all d_s(a,b)>=f+r+1, any transcript produced under true a with <=r actual corruptions cannot be compatible with a distinct b with <=f corruptions: every separated position is bad for at least one candidate, which would force d<=r+f. Thus the ordinary f-sound decoder (stop when exactly one hypothesis is compatible with <=f corruptions) must have stopped by this prefix on all <=r-corruption runs. Any q-cover fixed batch can be used as an initial prefix of an *ultimately f-sound* fixed schedule: repeat its entire batch 2f+1 times if necessary, ensuring final pairwise distance at least 2f+1. Therefore minimizing conditional worst-case stopping cost over schedules is exactly M(f+r+1). QED.

This proof uses actual realized corruption counts as a conditional **adversarial restriction**, not an average or stochastic model. It still allows the adversary to choose good readings within their admissible intervals.

## 2. Exact R5 profiles for every f and r

The source-pinned full-256 fixed-batch dual certificates establish for **every positive integer q** the following multicover optima in two real-noise chambers:

M_fifth(q) = 735 q, attained uniquely (up to order) by q copies each of 216,223,296;

M_critical(q) = 957 q, attained uniquely by q copies each of 217,218,224,298.

The dual lower bound is independent of f: each of the certified mutually constraining witness pairs requires q separating readings, and the weighted budget inequality yields 735q or the four pairwise-disjoint witness sets yield 957q. The repeated budgets cover all 32,640 named pairs. These are previously saved baseline certificates, now used at the new parameter q=f+r+1.

**COROLLARY A.** At every real tau in
25845652773852463277015040000 <= tau < 58182461585441404127941754880,

**W_fifth(f,r;tau)=735(f+r+1)**.

**COROLLARY B.** At every real tau in
1876919155234970890319953920000 <= tau < 1882951873548292168718745600000,

**W_critical(f,r;tau)=957(f+r+1)**.

Both statements hold for *all integers* 0<=r<=f and f>=0, not only the checked f=8 instances.

## 3. Concrete complete f=8 profiles

With decoder robustness fixed at f=8:

| Realized corruption cap r | Required separation q=9+r | Fifth chamber W (735q) | Near-critical W (957q) |
| ---: | ---: | ---: | ---: |
| 0 | 9 | 6615 | 8613 |
| 1 | 10 | 7350 | 9570 |
| 2 | 11 | 8085 | 10527 |
| 3 | 12 | 8820 | 11484 |
| 4 | 13 | 9555 | 12441 |
| 5 | 14 | 10290 | 13398 |
| 6 | 15 | 11025 | 14355 |
| 7 | 16 | 11760 | 15312 |
| 8 | 17 | 12495 | 16269 |

This quantifies both effects of observation-dependent stopping: **no gain in the absolute worst case r=f**, and an exact linear saving when fewer than f corruptions are realized. At f=8 and zero actual errors, stopping avoids 5880 fifth-chamber or 7656 near-critical units compared to a full f=8 fixed batch; the decoder remains f=8 sound.

## 4. Exact finite validation and source scope

The local checker VERIFY_R5_CONDITIONAL_ERROR_PROFILE.py uses the unmodified frozen integer table, confirms SHA256 and 32,640 unordered pairs, validates the selected-budget pairwise coverage at the most demanding integer endpoint of each chamber, tests the named action-exclusive pairs at both endpoints, and computes cyclic prefixes for all nine realized corruption caps r=0,...,8. In each case the first prefix to achieve q=f+r+1 separations across all pairs is the last query of q rounds. Its immediate predecessor admits a concrete candidate pair with only q-1 separations. The local test completed with exit status 0 and stderr R5_CONDITIONAL_ADAPTIVE_STOP_PROFILE_F8_ALL_R; exact per-r summaries are in RESULTS_CONDITIONAL.json.

The universal theorem is a mathematical proof. The numerical verification covers the specified finite frozen scalar observer and f=8, r=0..8; the all-f/all-r corollaries also rely on the preserved independently reproducible all-q fixed-batch dual certificates. Original 954-event derivation is not rerun. The work does not declare any native X6 signed, temporal, joint-relation or provenance direction redundant.

## 5. Next scientific decision

The previously open fixed-query-order early-stopping minimax problem is now characterized for every conditional realized corruption count. The original mother target remains the *fully adaptive next-query choice* under f=8, full 256 hypotheses, fifth chamber, with current exact bounds 8335<=C_8^*<=8343. A next discriminating construction should branch on actual observations and preserve all 256 error counters plus the shared low/high fiber-product residual. Author contribution is independent GitHub preservation; no formal CLAIM, native Result/Review, or protected Activity write is asserted. Historical R5 contribution identifier: EM-DIRECT-AEEFF0. Independent review: NOT_REVIEWED.

References: this directory's RESEARCH.md; source-pinned PR #2427 fifth-chamber fixed-batch all-f certificate at commit 06450ad3a3b37fef64d32bcd0a5bf89143c904ac; prior near-critical all-f four-witness certificate in EnterpriseMath_R5_sharp_identifiability_and_allf_fixed_batch_20261118.zip; exact 256-state input SHA above; current P000 and portable research norms.