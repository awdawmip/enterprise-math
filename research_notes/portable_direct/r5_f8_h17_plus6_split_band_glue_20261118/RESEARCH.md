# R5: exact 17-configuration eight-error minimax and split-band fiber-product structure
Date: 2026-11-18 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Research provenance: independent author-side GitHub science, not an authenticated Task CLAIM, Result, independent Review or native X6 acceptance.

## Exact frozen scientific scope
Scientific input commit 435e77af0d180eac32bd1f9c4c464bc4010b7551; 954-event-derived radius-two indexed-center scalar readout. Precomputed 256 configurations x 101 physical query budgets (k=214,...,314) integer table SHA256: 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. Use the original exact table from the previous R5 reproducibility bundle; no alteration to scientific pin. A good measurement of configuration h at k lies within eta of integer N_h(k). At most f measurements are arbitrary unlabeled errors. Put tau=2eta and L=25845652773852463277015040000, U=58182461585441404127941754880. Work in L <= tau < U. State distinctions below are relative to this declared scalar query language: full signed/branch/provenance X6 relational data retain separate types.

## Theorem A: exact H17 eight-error optimum
H17=(18,24,82,34,17,0,1,2,3,144,208,255,50,66,4,5,6).
For every real tau in [L,U), the guaranteed-identification minimax cumulative physical budget is C_8(H17;tau)=8335. Exactly five distinct query budgets are necessary and sufficient for this optimal value; the five actions k=214,215,216,223,296 suffice with repeated adaptive queries.

Proof lower bound: the verified H16 subset has C_8(H16;L)=8335, so increasing the hypothesis population or noise tolerance cannot improve its worst-case optimum. The existing H12 subset four-action lower bound is 8343, hence H17 needs at least five query-budget types to attain 8335.

Proof upper bound: at integer right endpoint tau=U-1, read exact centers from the frozen table. For query k and observed y, S(y)={h: |N_h(k)-y|<=eta}. A response support is dominated by a maximal support under inclusion; such maximal supports arise from integer center windows of span U-1 with a left endpoint at some distinct center. The exact maximal support masks are in ACTIONS_H17_PLUS6.txt, with 8,9,9,4,4 masks respectively. Each hypothesis has a saturating mismatch counter e_h in {0,...,9}; e_h=9 eliminates h. The finite minimax Bellman recurrence is V(e)=0 when at most one h remains alive, otherwise V(e)=min_k [ k + max_{S in maximal-supports(k)} V(T_{k,S}(e)) ]. T increments every still-live counter incompatible with S. Discard an action with stationary successor (it cannot force finite identification); every other successor increments at least one live mismatch, making recursion acyclic. C++17 engine VERIFY_EXACT_H17.cpp stores 17 four-bit counters in unsigned __int128 (68 bits) with exact integer state transitions and hash-keyed memoization.

Actual full solver output: EXACT_RESTRICTED n=17 f=8 V=8335 memo=34854233 calls=961302354 transitions=961302353 seconds=223.774. Captured independent exit code 0. Since all centers are integers, for any real tau<U, the response-support family is contained in that for tau=U-1; the same strategy remains valid. This proves equality throughout the chamber. Regression on f=0,...,8 returned 735+950f; f=7 used 10,559,609 cached states, exit 0. Independent explicit-tuple Python recursive oracle agreed in 16 cases on actual three-configuration subsets, f=0,...,3. Upstream 954-event generation was not rerun: the fixed source table is SHA256-checked.

## Theorem B: 256-configuration split-band fiber-product scalar observer
The eight effective source gap positions are (3,8,9,10,15,17,25,27), encoded as h bits 0,...,7. Let u(h)=h & 0x8F (bit positions 0,1,2,3,7), v(h)=h & 0xF0 (positions 4,5,6,7), shared bit b=h & 0x80 (effective gap 27).

For EVERY h=0,...,255, all eight low-budget counts N_h(214),...,N_h(221) factor exactly through u; all 93 high-budget counts N_h(222),...,N_h(314) factor exactly through v. Low observer yields 32 distinct signatures, and N_h(214) alone injectively identifies u. High observer yields 16 distinct signatures; the pair (N_h(223),N_h(294)) injectively identifies v. The compatible pairs satisfy u&0x80=v&0x80, and every compatible pair occurs exactly once with inverse h=u | (v&0x70). Therefore the 256 named scalar configurations are EXACTLY the fiber product U_low x_{shared bit} V_high, giving (32*16)/2=256 pairs and two K_(16,8) complete bipartite components. The common bit is a concrete required compatibility residual in composing the two observer bands.

The executable VERIFY_R5_SPLIT_BAND_GLUE.py validates the full exact 256x101 integer count table and all fiber multiplicities, factors and decoder claims, returning PASS_R5_SPLIT_BAND_FIBER_PRODUCT_256_BY_101. This is an observer-specific exact quotient/descent certificate, not erasure of the full native X6 joint field.

## Theorem C: exact future-observer obstruction
For hypotheses h=5 and h=6, N_5(k)=N_6(k) at every one of the 93 high budgets k=222,...,314. At all eight low budgets k=214,...,221, |N_5(k)-N_6(k)|>U, with minimum 217549739175592676504371200000 at k=221. Thus for any f arbitrary unlabeled errors, any strategy that can distinguish 5 and 6 has an adversarial branch containing at least 2f+1 low-band queries. The adversary gives high-band readings consistent with both, and at low-band queries balances conflicting readings so both hypotheses have at most f mismatches after <=2f low queries. For f=8 this forces at least 17 low-band queries and physical budget >=17*214=3638 on some branch. A high-band-only quotient cannot support subsequent low-band observation; the distinction is a necessary future residual.

## Reproduction and next frontier
Provide EXACT_R5_ALL_101_BUDGETS.json from the pinned R5 bundle. Run:
  python3 GENERATE_H17_ACTIONS.py EXACT_R5_ALL_101_BUDGETS.json ACTIONS_H17_PLUS6.txt
  python3 VERIFY_R5_SPLIT_BAND_GLUE.py EXACT_R5_ALL_101_BUDGETS.json
  c++ -std=c++17 -O3 VERIFY_EXACT_H17.cpp -o verify_h17
  ./verify_h17 ACTIONS_H17_PLUS6.txt 8
  python3 VERIFY_H17_SMALL_ORACLE.py EXACT_R5_ALL_101_BUDGETS.json ./verify_h17

Exact action masks, solver code, source-checker, and results are preserved together with this proof. All arithmetic and coverage are integer/exhaustive in the declared finite domain. Author proof plus execution; independent human/Driver review remains NOT_REVIEWED. Full 256-hypothesis exact eight-error minimax remains 8335<=C*_8<=8343. Next: test larger mixed low/high configuration unions or construct a full 256-state adaptive strategy, exploiting the shared-bit fiber product without suppressing labeled hypotheses, branch provenance, action scope or mismatch counters.
