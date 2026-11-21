# R284DQ — 八骨架布尔充要条件与单端圆弧间隔证书

Date: 2026-11-22 (Asia/Shanghai)
Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**
Scope: frozen auxiliary 34-bit Port circle-residual observer. Independent portable TASK research; the hypotheses and conclusion concern this exact finite model, not a native X6 evolution theorem.

## Frozen inputs and inherited theorem

Scientific pin: `awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py`, Git blob `b46e0f682b58e47c27094b4bea6fa4e55119a3ee`. The 65,536 source residues have frozen ordered SHA-256 `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`. The modulus is P=17,179,869,143 and there are 64 labeled circular integer arcs.

Use the already certified finite statement R284DN: the four-read observer
`U(i)=(f(i),f(i xor 1),f(i xor 64),f(i xor 65))`
has sharp Chebyshev separation 60 and exactly 256 unordered minimizing pairs. R284DO isolated the fourth upper bit `beta3` and its exact determinant increment `-q3`; R284DP reconstructed all 256 minimizing pairs by checking eight lower source skeletons and 512 source states with 32,768 point-to-arc distance calls. This note derives the eight skeletons symbolically and removes the second endpoint's 64-way arc scan.

## Theorem A — symbolic characterization of all eight lower skeletons

The twelve lexicographically ordered lower variables, each in {1,2}, are
`(u1,a,x,y,u2,w,b,z,u3,g,h,r)`.
For canonical lower representatives `ell&65=0`, one has `r=w=1`. Define `t=6-a in {4,5}`, `s=13-b in {11,12}`, and

`q3=(ts-xw)u3+(su1+xu2)g+(tu2+wu1)h`.

Set `A=q3(w=1)` and `B=q3(w=2)` while leaving every other lower variable fixed. Then

`A=(ts-x)u3+(su1+xu2)g+(tu2+u1)h >= (ts-x)+(s+x)+(t+1)=(t+1)(s+1)>=60.`

All three coefficients used in the inequalities are strictly positive throughout the binary domain. Equality `A=60` holds **if and only if**
`a=b=2, u1=u2=u3=g=h=1`, with `x in {1,2}` arbitrary. Indeed, equality in the final factor inequality forces `t=4,s=11`; equality in the preceding positive-coefficient bounds then forces the five stated variables to 1. Conversely these choices give 60.

Furthermore `B-A=u1*h-x*u3`. On the equality family this is `1-x`, so `(A,B)=(60,60)` when `x=1` and `(60,59)` when `x=2`. Consequently `max(A,B)<=60` is **equivalent** to the exact fixed-variable condition above. The remaining free lower variables are `x,y,z`, each in {1,2}; the canonical `r=w=1` are fixed by the orbit representative convention.

As source-index bits `11,...,0` correspond respectively to the twelve variables, the eight lower indices are exactly
`ell=1056 + 512 X + 256 Y + 16 Z`, for `X,Y,Z in {0,1}`, namely

`{1056,1072,1312,1328,1568,1584,1824,1840}`.

Thus the eight-skeleton enumeration in R284DP follows algebraically rather than by brute-force searching 1,024 lower representatives. The checker also exhaustively verifies the iff statement over the 1,024 canonical representatives as a separate finite crosscheck.

## Lemma B — strict maximizing-arc stability from a single endpoint

For a circle with geodesic distance `rho`, each distance-to-closed-arc function `d_A(x)=min_{a in A}rho(x,a)` is 1-Lipschitz:

`|d_A(x)-d_A(y)| <= rho(x,y)`.

Suppose at `x` a unique farthest arc `A_*` has margin
`m=d_{A_*}(x)-max_{A != A_*}d_A(x)>2*rho(x,y)`.
Then `d_{A_*}(y)-d_A(y)>=m-2*rho(x,y)>0` for every rival A. Hence `A_*` remains the unique farthest arc at y. This is a general circle-arc lemma independent of the frozen Port source.

For each R284DQ pair, the determinant identity sets `y=(x-q3) mod P` with `q3 in {59,60}`, so `rho(x,y)<=60`. The checker evaluates the 64 arc distances only at the first endpoint for each of 256 translated base pairs. Across these 256 first endpoints the **minimum winning margin is 37,469**, strictly greater than 120. The lemma therefore certifies the maximizing arc at the other endpoint without a 64-arc sweep. One further arc-distance evaluation at y checks
`|d_{A_*}(x)-d_{A_*}(y)|=q3 in {59,60}`.
This final branch-value check matters: arc-label stability by itself does not force equality of distance change and source-residue increment.

## Constructive theorem and exact certificate

For each of the eight lower skeletons, take even upper lexicographic indices `h in {0,2,4,6,8,10,12,14}` (fourth upper bit fixed to zero) and the four shifts `G={0,1,64,65}`. These produce exactly 256 distinct base indices `a`; partners are `b=a xor 4096`. Compute the base residue with the frozen determinant, obtain the partner as `(g(a)-q3(a&4095)) mod P`, and use Lemma B plus one partner arc check. Every resulting pair has four-read Chebyshev distance exactly 60. Because R284DN already independently certified 256 **global** minimizing unordered pairs, the 256 constructed pairs are the complete minimum-pair set.

The checker verifies the same canonical SHA-256 for the sorted pair list:

`7c05864095ba5cde368002e67764bc772ca1bfe3fabbcf26af4fb090b7d0996a`.

Results: 256 pairs, 256 first-endpoint source residue evaluations, 256 partner residues by exact increment, 16,384 first-endpoint point-arc distance evaluations plus 256 partner point-arc distance checks = **16,640 total**. The original full population sweep used 4,194,304 point-arc evaluations; R284DP candidate-only verification used 32,768. The comparable operation-count ratios are 252.0769... (full sweep / current) and 1.96923... (R284DP / current); these are not measured wall-clock timings.

The implementation additionally uses 2,048 q3 evaluations for the optional exhaustive 1,024-representative crosscheck and 256 q3 evaluations in pair construction. Building the 64 arcs from the frozen formula incurs its ordinary one-time preprocessing. Counts are deliberately attributed to their exact operation classes.

For the 64 orbit representatives, the four absolute-gap patterns are `(60,60,60,60)`:32 and `(60,60,59,59)`:32. The 256 partner comparisons have winning-label histogram `21:45,32:21,44:37,45:19,55:64,56:43,63:27`, matching R284DP. Exact unbounded integer arithmetic was used. The theorem is author-proved and computationally checked on the declared finite candidate set, reusing R284DN's separate globally exhaustive theorem; independent review remains `NOT_REVIEWED`.

## Reproduction and next research question

- `R284DQ_boolean_skeleton_margin_checker.py` is the standard-library exact checker, importing the already published `R284DP_eight_skeleton_fast_pair_generator_checker.py` and `R284DM_joint_orbit_code_checker.py` from this directory.
- `R284DQ_boolean_skeleton_margin_certificate.json` is its generated result.
- The complete Port frozen source is unchanged; this research does not update P000, the global worldview or existing claims and reviews.

Next: seek interval-cell lookup rules using the established 65-segment exact integer farthest-arc envelope (R284DD) to replace the remaining 256 x 64 first-endpoint arc comparisons with a provenance-preserving event search, and compare preprocessing and state-construction costs. Also check whether the 37,469 margin has an algebraic lower bound uniform across the eight Boolean skeletons and eight upper orbit settings, avoiding finite scans of winner margins.

Control provenance: independent portable source research, not a native CLAIM or formal Result. Historical EM-DIRECT-20B766 is previous attribution, not the present authenticated researcher identity. Current gateway status did not grant research execution; the scope-limited LEASED owner request `r1-20261122-0201-owner-leased-scope-v1` ended `FAILED / SOURCE_TREE_TRUNCATED`. Preserve historical Activity attribution and leave this new source's activity association to an actually authorized original-session/CAS path.