# EC49DH — Affine-collinear positive BRC weights can saturate every native X6 return fiber

Date: 2026-11-01. **AUTHOR_ANALYTIC_PROOF / EXACT_NATIVE_X6_FINITE_CERTIFICATE_PASS / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED.** This is an author-side research result, not a Source-native CLAIM, accepted Result, or independent review.

## Fixed scientific inputs and model

GLOBAL_KNOWLEDGE_V1 canonical main \`390e9c2d78163e7c7453131d145e817224828693\`; Enterprise Math canonical main \`738596c45bf5942e05bf68f7f5a5452343185b31\`; predecessor EC49DG, PR #1730 commit \`e7a1904d7ae356ef1a29d55412ac31991b7b3404\`. P000/ACTIVE worldview unchanged. Current native service 0.6.11 returned research_authority_granted=false, executor_binding_configured=false, UPSTREAM_CODE_REVIEW_REQUIRED, native quota 5/5. Active owner/CLAIM was not verified.

Prefixes are **literal ordered native signed six-axis primitive steps** of fixed even length n and displacement D=(2s,2v,0,0,0,0), v>=0, |s|+v<=h. Suffixes are returning words of exactly h or 1..h **complete** operations:
a=(-1,-1), b=(-2,-2), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1), e=(+3,+1,+1,-3).
Four final joint adjacent-subword labels retain both A=(+1,+2), B=(+2,+1), **including prefix/suffix seams**. There are three separate additive observation channels per final label and complete suffix: W_x(prefix+suffix), W_y(prefix+suffix), and unweighted count 1; negative primitive steps have weight 1, positive +Ej carries x_j or y_j.

The explicit **strictly positive** axis weight pair is
x=(2,3,1,2,3,4), y=(5,7,3,5,7,9)=2x+(1,1,1,1,1,1).
All 20 triple determinants det[[x_i,x_j,x_k],[y_i,y_j,y_k],[1,1,1]]=0; the six single-axis weight points lie on an affine line.

## Theorem and exact scope

**Claim (conditional on EC49DB/DE's author-side six-feature/tag upper-bound lemma).** For every integer h>=2, and all (h+1)^2 return displacement fibers, at n=2h+8 the observer reaches rank 3r for both future languages: r=4 for boundary delta=h-|s|-v=0; exact-h r=5 for odd positive delta and r=6 for positive even delta; cumulative 1..h r=6 for all positive delta. Consequently
dim O_exact(h)=3(11h²+15h+8)/2;
dim O_cum(h)=18h²+24h+12;
n_sat(h)=2h+8, and rank persists at larger even n. The historical six-feature upper-bound lemma needs independent review; all explicit rank-lower constructions below are separately reproducible. This theorem asserts the above **one collinear weight pair**, not every collinear parameter choice.

## All interior fibers: nine finite exact seeds plus uniform lift

Nine seed types suffice: exact and cumulative depth h0=2 at (s0,v0)=(-1,0),(0,0),(0,1),(1,0), plus exact h0=3 at (0,0). Each of the nine seed sets consists of literal length 2h0+8 signed-X6 paths beginning (-3,+3). From actual complete returning suffixes choose r distinct suffix/final-label rows; independently check a 3r-square integer minor of the Wx,Wy,count observation matrix.

For the fixed positive collinear x,y, all nine determinants are nonzero modulo **both** primes 1000003,1000033. Seed order (mode,h0,s0,v0,r): residues (p1,p2):
eq,2,-1,0,5: (199995,705970);
le,2,-1,0,6: (979494,632225);
eq,2,0,0,6: (854152,973287);
le,2,0,0,6: (703295,27691);
eq,2,0,1,5: (629574,314932);
le,2,0,1,6: (917662,14192);
eq,2,1,0,5: (71164,656443);
le,2,1,0,6: (975073,532524);
eq,3,0,0,5: (498096,626651).
Nonzero residue of an integer determinant proves nonzero exact rational determinant, not a floating-point inference. The adjacent compact evidence archive contains the actual standard-library Python verifier and nine literal seed lists.

**Exact arbitrary-h lift.** Choose seed by EC49DD's nine-case routing: in cumulative language h0=2, use positive-E1/negative-E1/positive-E2/zero seed according to s>0,s<0,s=0 and v>0,or origin. In exact language, use zero h0=2 when delta is positive even, zero h0=3 for odd delta at origin, otherwise the nonzero h0=2 seed for odd delta. Given any seed prefix p=(-3,+3)p_tail, choose x,y>=0 counting additional axis units and d=h-h0-x-y>=0, and replace
p' = (-3,+3)^d (axis)^(2x) (-3) (+2)^(2y) (+3) p_tail.
Here axis=+1 if s>0, axis=-1 if s<0; zero-base uses the sign of s. Extend each complete-operation future word u with a^x b^y, e^x b^y, or b^y as routed; in exact mode append (ae)^(d/2), where d is even. These are the exact integer recipes implemented by lift() in the executed verifier. Direct axis sums give prefix length 2h+8 and endpoint (2s,2v,0,0,0,0), and each extended suffix returns exactly. All inserted (-3,+3), -3 separators and future tails are tag-safe; old ordered prefix/future A/B responses, including seams, are unchanged. For each selected row the new positive-weight observation is scaled by nonzero Kx or Ky, independent of the prefix-column choice; count rows remain identical. Thus the entire lifted 3r-square determinant is Kx^r Ky^r times the corresponding seed determinant, nonzero over Q for **every h**. The infinite-h conclusion is this explicit monomial identity, not extrapolation of finite tests.

## All boundary fibers: explicit twelve-path determinants

When delta=0, each fiber has exactly one relevant shortest full returning suffix. Four final-tag classes each require three true paths whose [Wx,Wy,1] rows are independent.

For s<=0, including s=0,v=h, and for positive-E1 corner s=h,v=0, use these *four-positive-step cores*, three per tag: neither 3333,3334,3344; A-only 1233,1234,1244; B-only 2133,2134,2144; both 1213,1214,2123. Cancel each core's positive steps by its negative-tail opposite steps; append endpoint-necessary -1 or +1/+2 primitives. The selected suffix is e^(-s)b^v (s<=0) or a^h (positive E1 corner). It cannot change labels, and the four exact integer 3x3 determinants are respectively -18,-420,-420,+420. Endpoint/suffix factors are positive monomials, preserving nonzero rank for all h.

For s>0,v>0, choose four length 2h+2 label-isolating bases (in label order neither,A-only,B-only,both):
1^(2s) (-3,+3) 2^(2v);
1^(2s) 2^(2v) (-3,+3);
2^(2v) 1^(2s) (-3,+3);
(1,2) 1^(2s-1) 2^(2v-1) (-3,+3).
For each base prepend **three** safe (+Ej,-Ej) gates, comprising k copies of E3 and 3-k copies of E4, with k=0,1,2. These paths are all length 2h+8, and suffix a^s b^v preserves their final tags. The weight vectors, after factoring out positive base and suffix factors, are (x3^k*x4^(3-k), y3^k*y4^(3-k),1), for k=0,1,2. Their exact determinant is 20. Hence all four 3x3 blocks are invertible and boundary full rank is 12 for every h. Products of several neutral gates recover full rank even though all *single-axis* points (x_j,y_j) are affine-collinear.

## Sharp minimum length and extension

On extreme D=(-2h,0,0,0,0,0), the only returning suffix is e^h, because +2 is the largest E1 displacement per future operation and only e attains it. At prefix length 2h+6 exactly three positive primitives are possible. To observe **both** A and B, those three positives must be 121 or 212 without an intervening negative step; hence their BRC product pair belongs to at most two possibilities. The three rows Wx,Wy,count restricted to tag-both have rank at most two, so the four-label 12-dimensional target cannot be reached (total rank <=11). At shorter even lengths the positive-count obstruction is at least as strong; native parity excludes odd n. Thus n_sat(h)>=2h+8 independently of an old EC49DF sharpness claim. To extend any full rank witness by 2 primitive steps, prepend (+E6,-E6): it is tag-safe, endpoint-neutral, and multiplies channel weights by positive constants.

## Actual verification and boundary of claims

Executed \`python3 VERIFY_EC49DH.py --seeds fixed_seeds.json --hmax 12\` under Python 3 stdlib returned PASS: 9 seed matrices, 165 boundary matrices (h=2..12), and 649 interior matrices for **each** future language, total 1472 nonzero integer minors checked modulo both stated primes. Verifier recomputes all signed-X6 endpoints, literal path lengths, four ordered joint A/B labels including seams, and both positive BRC weights. Exact all-h validity comes from finite nonzero seed determinants + tag/monomial-preserving symbolic lift + uniform boundary determinants; the finite run audits implementation only.

The complete original evidence archive includes the full proof, executed script, all literal seeds, verifier output, next question, and SHA256 manifest; SHA256 \`eea20ee5e0956cbe3a067547e8f2578f3ef12b34ec7299e334816d8441e42266\`. The adjacent GitHub code-certificate archive is expected to contain exactly the executed checker, seeds, execution JSON and follow-up; verify its own SHA and extraction manifest upon publication. Result remains AUTHOR_PROOF/UNREVIEWED/NOT_ADMITTED and has no physical propagation, phase-cancellation or external-world interpretation.

**Next EC49DI:** classify the actual rank-degenerate subset within the positive affine-collinear parameter family y=a x+b, using determinantal ideals or minimal true-defect examples; independently audit the inherited six-feature upper-bound statement and the nine-case lift. Do not mechanically increase horizon after the uniform result.
