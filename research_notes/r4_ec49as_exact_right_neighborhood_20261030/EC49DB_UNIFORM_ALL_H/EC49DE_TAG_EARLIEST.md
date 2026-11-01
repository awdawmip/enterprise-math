# EC49DE — All-h earliest saturation of the axis-uniform positive-BRC tag observer

**2026-11-01; AUTHOR_ANALYTIC_PROOF / FINITE_EXHAUSTIVE_CHECK_PASS / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED.** Scientific input fixed to GLOBAL_KNOWLEDGE_V1 main `176e1691b5401cba0e81da0b28574b2c9624d406`, Enterprise Math main `e5f31bafe2c7dd421430023f4d717013c424525f`, and preceding EC49DD author draft `6cb32857e7e0d1433297e7b40497da2136a56222`. P000 (global blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`) and protected ACTIVE worldview were read and not changed. Native service 0.6.11 returned research_authority_granted=false, executor_binding_configured=false, and new-job quota 5/5; no active canonical owner or native CLAIM was verified. GitHub storage is author-side evidence, not a Source-native Result/review.

## Precise model and new theorem

Prefix `p`: an ordered length-`n` word in twelve literal signed native X6 steps, with endpoint `D=(2s,2v,0,0,0,0)`, `s in Z`, `v>=0`. Positive adjacent tags: `A=(+1,+2)`, `B=(+2,+1)`; the four final tags are `0` (neither), `1` (B only), `2` (A only), `3` (both). Complete future operation paths are

`a=(-1,-1); b=(-2,-2); c=(+1,+2,-1,-2); d=(+2,+1,-2,-1); e=(+3,+1,+1,-3)`.

Only complete suffixes with endpoint `-D` are observed, with either exactly `h` operations or from `1` through `h`. For each suffix `w` and tag `t`, the count row is `T_(w,t)(p)=1[tag(pw)=t]`. Two positive BRC branch-product rows use axis-uniform positive-step weights `x=alpha*(1,1,1,1,1,1)`, `y=beta*(1,1,1,1,1,1)`, `alpha,beta>0`, negative weights one. Rank is over Q for rational parameters and over R for positive real parameters. The observer is additive and positive; it makes no signed-amplitude or physical-propagation claim.

**Theorem.** For every integer `h>=2`, both exact and cumulative observers first attain all possible returning-fiber ranks simultaneously at the genuine literal prefix length

`n_sat^axis-uniform(h)=2h+6.`

With `delta=h-|s|-v>=0` the rank per fiber at that length is

| delta | exactly h | 1 through h |
|---|---:|---:|
| 0 | 4 | 4 |
| positive odd | 5 | 6 |
| positive even | 6 | 6 |

The summed ranks are `dim_exact=(11h^2+15h+8)/2` and `dim_cumulative=6h^2+8h+4`. All larger feasible even prefix lengths retain these ranks. This proves that the axis-uniform stratum of EC49DD saturates **two primitive steps earlier** than the three-channel nonuniform reference-weight result of EC49DB (the latter remains author-side pending independent review).

## Proof 1 — positive BRC reduction

Every prefix in the fixed `(n,D)` fiber has precisely `Pplus=(n+sum D_i)/2` positive steps. Thus for any fixed complete suffix word `w`, the x-channel row is `alpha^(Pplus+Pplus(w))*T_(w,t)`, and the y-channel row is `beta^(Pplus+Pplus(w))*T_(w,t)`. These are nonzero row scalings independent of the prefix column. Consequently the joint three-channel observer has **exactly the tag/count rank**, at every feasible prefix length, without deleting the underlying path provenance.

## Proof 2 — full abstract tag ranks

Put `F0,F1,F2,F3` for the current mutually exclusive tag indicators; `pA=1[A absent and final primitive letter +1]`, `pB=1[B absent and final primitive letter +2]`. This six-feature vector suffices for every complete suffix: operations end on a negative step, so operation boundaries create no new A/B adjacency. A suffix containing neither c nor d preserves the tag; containing both forces tag 3. A c-only suffix forces A, and creates B beyond the old tag precisely when its first operation is c and `pB=1`; d-only is symmetric with `pA`.

Set `C=F0+F2`, `Dprime=F0+F1`, `I=sum(F0..F3)`. A c-only suffix has nonzero tag rows `C-epsilon*pB` and `I-C+epsilon*pB`, with `epsilon=1` iff the suffix begins c. A d-only suffix has `Dprime-epsilon*pA` and `I-Dprime+epsilon*pA`. Both c and d yield only I; no c/d yields all four F rows.

For any returning complete suffix let `N_b=v`, `N_e-N_a=-s`, `k=|s|+v`. Its a/b/e count is `k+2t` for `t>=0`; writing `j=N_c+N_d`, an exact-h suffix satisfies `delta=2t+j`. If delta=0, j=0 for both languages, giving four F rows. If delta is positive even, exact depth admits j=0 (all F rows) and j=2 with c-first or d-first (exposes pB,pA); rank six. If delta is odd, exact depth requires j>=1: its rows lie in the five-dimensional span `{I,C,Dprime,pA,pB}`. This span is attained by j=1 c-only and d-only words, ordered both with the c/d operation first and after a non-c/d operation; h>=2 guarantees at least one such other operation. Rank five. For cumulative depth with delta>=1, a no-c/d return exists of length <=h (for zero displacement use ae of length two), and c-first and d-first returns also exist within h (at zero displacement use c/d themselves); rank six.

These ranks are formal upper bounds on all literal prefix populations, requiring an actual full-feature witness at the stated n.

## Proof 3 — six universal literal X6 witnesses at n=2h+6

The following **six-step zero-displacement** signed primitive motifs all begin on a negative step. Their feature vectors in the order `(F0,F1,F2,F3,pA,pB)` are

| motif | literal primitive letters | feature vector |
|---|---|---|
| m0 | -3,+3,-3,+3,-3,+3 | (1,0,0,0,0,0) |
| mPA | -1,+1,-2,+2,-1,+1 | (1,0,0,0,1,0) |
| mPB | -2,+2,-1,+1,-2,+2 | (1,0,0,0,0,1) |
| mA | -3,+1,+2,-2,-1,+3 | (0,0,1,0,0,0) |
| mB | -3,+2,+1,-1,-2,+3 | (0,1,0,0,0,0) |
| mAB | -1,+1,+2,+1,-1,-2 | (0,0,0,1,0,0) |

Their integer 6x6 feature determinant is **-1**. For all fibers except positive mixed boundary (`s>0,v>0,delta=0`), use the tag-free base of length 2h

`base=(sign(s)*E1)^(2|s|) (-E3,+E3)^delta (+E2)^(2v)`

(first block omitted when s=0). It has endpoint D, and the E3 separator prevents a positive A/B adjacency when both E1/E2 runs occur. Appending each of the six motifs creates a genuine length-2h+6 prefix in the same fiber. Since each motif begins negatively, no seam A/B is created. Its six history-feature rows are exactly the independent rows above, so the abstract upper rank is attained for every complete-future language.

For positive mixed boundary put `s=u>=1, v>=1, u+v=h`, `U=(+1)^(2u)`, `V=(+2)^(2v)`, `g=(-3,+3)`. Four actual prefixes `U g V g g`, `U V g g g`, `V U g g g`, and `(+1,+2) (+1)^(2u-1) (+2)^(2v-1) g g g` have length 2h+6, endpoint D, and four different tags 0,2,1,3. All returning suffixes on this boundary contain only a,b,e and preserve tags, giving full rank four.

## Proof 4 — minimality and dimensions

At `D=(-2h,0,0,0,0,0)`, the only complete returning suffix of either language is `e^h`. It begins +3 and contains no +2, hence never introduces a new A/B pair. At any feasible literal prefix length `n<=2h+4` there are at most `(n-2h)/2<=2` positive steps, whereas **both** A and B together require at least three positive letters. Therefore the tag-3 row vanishes for every prefix in that fiber and rank is <=3 rather than four. Odd n cannot reach this even endpoint. The six-motif construction matches the lower bound; prepending any number of (-3,+3) neutral pairs preserves all tag and boundary features, proving all larger even lengths. Summing the ranks over `(h+1)^2` fibers gives the stated quadratic formulas.

## Exact executed evidence and limits

The adjacent executable `VERIFY_EC49DE_COMPACT.py` **reuses** `VERIFY_EC49DD.py` for literal signed X6 operations/endpoints/tags. It constructs each proposed path and enumerates **all 97,655 complete operation words of lengths 1..7**; checking h=2..7 covers **199 fibers** and **878,820 exact 0/1 tag-observer rows** in the two future languages. Modular Gaussian elimination mod 1,000,003 gives the complete claimed ranks, independently verifying the six-motif construction and all total dimensions. Output is saved in `EC49DE_COMPACT_RUN.log`. The general h conclusion follows from the above analytical proof, not from finite extrapolation. The longer local checker also cross-checked axis-uniform positive BRC product scaling with alpha=2 and beta=3.

Methodological context only: weighted automaton rank/Hankel representation, Balle et al. ICALP 2021 DOI 10.4230/LIPIcs.ICALP.2021.118; this is not a novelty or independent-proof attestation.

**Next EC49DF:** classify earliest lengths at exceptional *nonuniform* positive weights, especially seek a nonproportional/non-axis-uniform pair with `Q(x,y)=0` from EC49DC yet full three-channel rank; or derive a new necessary equation for genuine rank loss. Independent formalization should verify the six-feature transition table and the six-motif determinant before project admission.
