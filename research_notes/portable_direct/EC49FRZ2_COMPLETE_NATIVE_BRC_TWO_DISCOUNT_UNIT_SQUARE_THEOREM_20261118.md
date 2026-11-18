# EC49FRZ2 — Complete independent two-discount native BRC phase diagram on the entire unit square

**Status:** AUTHOR_PROVED / EXACT_FINITE_BELLMAN_AND_20_NATIVE_FULL_TREE_REPLAY / NOT_REVIEWED.
**Frozen original science:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Source class:** 16943; 141 complete named states, 310 original configurations, all 228 physically named original BRC observations, unchanged complete response partitions. This extends the EC49FRZ 10-phase full diagonal theorem, itself continuing EC49FRX–FRY #2666.

## Exact two-dimensional theorem

Let the prior be uniform over the 141 named states. For baseline price `t>0`, set `p32=(1-a)t`, `p34=(1-b)t` and every other named observation price `t`, with arbitrary **real** `0<=a,b<=1`. A strategy is any complete, original native BRC adaptive decision tree identifying each of the 141 states. Define `M=max(a,b)` and `m=min(a,b)`.

The unrestricted all-tree exact optimum `F(a,b)=141V(a,b)/t` for **every real pair in the entire closed [0,1]×[0,1] square** is:

| Interval for m | Exact F(a,b) |
|---|---|
| [0,1/4] | 296 − 141M − 11m |
| [1/4,1/3] | 297 − 141M − 15m |
| [1/3,2/5] | 304 − 141M − 36m |
| [2/5,1/2] | 306 − 141M − 41m |
| [1/2,5/9] | 310 − 141M − 49m |
| [5/9,3/5] | 315 − 141M − 58m |
| [3/5,2/3] | 321 − 141M − 68m |
| [2/3,3/4] | 337 − 141M − 92m |
| [3/4,4/5] | 343 − 141M − 100m |
| [4/5,1] | 355 − 141M − 115m |

This is a **complete original-native full two-price phase diagram**, including both axes, the diagonal and zero-price boundary cases. There are 20 distinct nonempty open optimal affine chambers (ten on each side of a=b), and a minimal universal menu of **exactly 20 complete original native tree-cost types** suffices and is necessary.

## Proof: the once-per-path root-use saturation lemma

In a reduced legal adaptive tree, an original physically named observation q is called at most once on each state path: its response after the first call is already fixed, so a repeated call cannot split its current state subset. Any redundant repeat can be deleted without raising cost, also at a zero-price endpoint. Consequently, over 141 named state paths the total use satisfies `N32(Q)<=141` and `N34(Q)<=141` for every relevant complete tree Q.

Let `f(s)=F(s,s)`. EC49FRZ proved its **ten-piece exact formula on every real s in [0,1]** via 11 unrestricted, full-228 native Bellman exact vertices, ten complete original-native q32-root tree witnesses and concavity. Each witness has `N32=141`, because q32 is its actual first physical named observation on all 141 paths. Its measured total usage pair (U,K) is one of

`(296,152),(297,156),(304,177),(306,182),(310,190),(315,199),(321,209),(337,233),(343,241),(355,256)`.

Fix `0<=m<=M<=1`. For any complete reduced Q at prices (a,b)=(M,m),

`F_Q(M,m)=F_Q(m,m)-(M-m)N32(Q) >= f(m)-141(M-m)`.

An already verified diagonal-optimal **q32-root** native complete tree has N32=141 and reaches equality. Therefore

`F(M,m)=f(m)-141(M-m)` for all real m,M.

To cover the other half-square, independent **q34-root** complete original-native witnesses were constructed for *all ten diagonal regions*, and each one exactly replays all 141 original named-state paths. Each has `N34=141`, root q34, the same segment-specific (U,K) totals as the corresponding q32-root witness, and depth at most four. The same inequality applied to N34 proves `F(m,M)=f(m)-141(M-m)`. Thus the full square formula follows by substituting the ten diagonal affine lines `f(m)=U_i-K_i m`:

`F(a,b)=U_i-141M-(K_i-141)m`.

The ten values `K_i-141 = 11,15,36,41,49,58,68,92,100,115` are distinct and all strictly below 141. On each interior chamber with a>b the gradient is `(-141,-(K_i-141))`; on b>a it is `(-(K_i-141),-141)`. These give twenty pairwise distinct open-chamber gradients. Every affine-tree menu that globally realizes the exact value must contain an affine type for each such gradient, and the twenty exhibited trees attain all chambers, proving **minimal size twenty**.

## Actual verification and limits

The source-preserving original-data solver performs exact rational finite DP over **all 228 original physical named observers**, with no approximations or omitted named states. Eleven full diagonal rational vertices were independently re-executed and passed; **20 complete trees × 141 named state paths** were replayed, all reached their correct named leaves, had the declared integer (U,N32,N34) and worst depth ≤4. Separate unrestricted exact off-diagonal DP examples, recorded with actual integers, include:
`(a,b)=(3/4,2/3) -> F=2039/12`,
`(2/3,3/4) -> F=2039/12`,
`(1,1/2) -> F=289/2`,
`(1,0) -> F=155`,
`(9/10,3/4) -> F=2822/20`.
The analytic saturation proof establishes the entire continuum; those finite points are corroborating evidence, not a parameter-grid substitution.

**Full self-contained source, all 20 original native trees, proof, actual verification logs and SHA256 manifest**: archive `EC49FRZ2_NATIVE_BRC_COMPLETE_TWO_PRICE_UNIT_SQUARE_EVIDENCE_20261118.tar.xz`, **211632 bytes**, SHA256 `635471c27afc11654efce4f7b79d150a28ad0cc88e04b68f6863aa5ac2c6b0b1`, **38 manifested files**, all verified upon reopening the archive. Reproduce with Python stdlib: `python code/EC49FRZ2_VERIFY_FULL_SQUARE.py --quick` for the twenty trees or `--full` to recompute exact native DP points. The successful standalone complete 11-vertex DP execution log is preserved separately in the archive. The second full-square batch was interrupted after partial valid checks and is not represented as a completed whole batch.

This theorem concerns BRC identification economics with the original named observer response structure and uniform named-state prior. The parameters a,b are price discounts, not physical time/heartbeat counts; this proves no external physical calibration or Shor speed claim. Mathematical admission remains NOT_REVIEWED. The current Source owner/role check returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE / operation_sent=false`; this is portable independent GitHub evidence, not a formal CLAIM/Result/Review/Activity write.

**Next**: independently price a third or more physical named observer, change the uniform prior, or vary the root/terminal price ratio, to find when saturation no longer covers the full parameter domain and classify new Pareto witness sets.
