# EC49FQS — Two exact native BRC price slices and a 25-node parameter certificate

Date: 2026-11-16. Mathematical status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Frozen input: \`awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. Parent: EC49FQR PR #2568@444c69119e9ec7175642687b1380a0f0e92af0ad (Draft/unmerged). The predecessor's 89 exact Bellman certificates are retained unchanged.

## Native finite problem

Fix native BRC class 16943: 310 source configurations, 141 distinguishable full named-root profiles with multiplicities \`m_i\`, 144 terminal observations and 84 named-root observations (228 physical labels; 209 distinct partitions). A correct finite adaptive decision tree identifies the full named-root profile. Terminal price \`t>0\`, root price \`r>0\`, \`x=r/t\`, prior \`p_lambda(i)=(1-lambda)/141+lambda*m_i/310\` for \`0<=lambda<=1\`. Define dimensionless global optimum \`v(lambda,x)=V(lambda;r,t)/t\`. The following are feasible complete-tree cost planes:

\`\`\`text
A=(1-lambda)*(6*x+290)/141+lambda*(6*x+751)/310     [first labels 32,34]
B=(1-lambda)*(5*x+293)/141+lambda*(5*x+704)/310     [first labels 140,142]
C=(1-lambda)*(5*x+295)/141+lambda*(5*x+685)/310     [first labels 16,23]
F=min(A,B,C)
beta=620/3299
gamma(x)=310*(3-x)/(7557-169*x)
\`\`\`

Each tuple \`(U_R,U_T;M_R,M_T)\` is an actual full-tree accumulated root/terminal count under 141 equally weighted profiles and 310 raw configurations, respectively.

## Theorem 1 — two new exact all-real-prior slices

For \`x=35/16\` and \`x=37/16\`, **for every real** \`lambda in [0,1]\` and for all correct finite adaptive trees using the legal native observations, \`v(lambda,x)=F(lambda,x)\`. Exact transitions:
- \`gamma(35/16)=4030/114997\`;
- \`gamma(37/16)=3410/114659\`;
- common second transition \`beta=620/3299\`.

For either x, the complete sets of optimal physical first labels are \`{32,34}\` on \`[0,gamma)\`; \`{32,34,140,142}\` at gamma; \`{140,142}\` on \`(gamma,beta)\`; \`{16,23,140,142}\` at beta; and \`{16,23}\` on \`(beta,1]\`.

An unrestricted **integer** subset-Bellman computation obtained the following objectives. For prior \`lambda=a/b\`, weight of profile i is \`310*(b-a)+141*a*m_i\` and the total weight is \`310*141*b\`; \`v=objective/(310*141*b*t)\`.

| Root/terminal prices | lambda | Exact integer optimum | Exhaustive optimal first physical labels |
|---|---|---:|---|
| 35/16 | 0 | 1503500 | 32,34 |
| 35/16 | 4030/114997 | 173786064480 | 32,34,140,142 |
| 35/16 | 620/3299 | 5038670250 | 16,23,140,142 |
| 35/16 | 1 | 1570035 | 16,23 |
| 37/16 | 0 | 1507220 | 32,34 |
| 37/16 | 3410/114659 | 173560870560 | 32,34,140,142 |
| 37/16 | 620/3299 | 5047849350 | 16,23,140,142 |
| 37/16 | 1 | 1571445 | 16,23 |

**Complete proof.** The exact native source files are fixed by SHA256. An unrestricted weighted Bellman recurrence enumerates distinct induced query partitions, recursively resolves all positive-mass nontrivial child subsets, prunes only using feasible upper and admissible lower bounds, and exhaustively checks all 228 physical query indices at the root. A second independently coded Bellman recurrence reproduces all eight exact objectives and all first-label sets. A full correct tree is supplied and replayed for every tied first label at each anchor, obtaining the A/B/C accumulated observation vectors. For fixed x, the cost of a fixed tree is affine in lambda, and its unrestricted optimum is concave as an infimum of affine functions. The feasible A/B/C trees match the true Bellman value at the endpoints of, respectively, \`[0,gamma]\`, \`[gamma,beta]\` and \`[beta,1]\`; concavity and feasibility sandwich the entire real intervals to equality. A fixed-first-label restricted Bellman value is likewise concave, so a label optimal strictly inside an interval must also be optimal at both endpoints (apply nonnegative concavity to the difference against the certified affine optimum). The intersections of exhaustive endpoint sets yield exactly the stated first-label classification.

## Theorem 2 — certified 25-price continuous two-parameter rectangles

Adjoin \`35/16,37/16\` to the predecessor's exact 23-node set G23, yielding G25 of 25 rational price nodes in \`[1,3]\`. For every pair \`a<b\` of consecutive G25 nodes, the exact global optimum is F on each of the rectangles:
- \`a<=x<=b, 0<=lambda<=gamma(b)\` (A);
- \`a<=x<=b, gamma(a)<=lambda<=beta\` (B);
- \`a<=x<=b, beta<=lambda<=1\` (C).

Proof: each fixed-tree expected-cost difference against its designated A/B/C feasible tree is bi-affine in \`(lambda,x)\`. Four-corner exact optimality implies interior nonnegativity by bi-affine convex interpolation. The only potentially unresolved parts lie in the 24 bands \`a<x<b, gamma(b)<lambda<gamma(a)\`. Their combined bounding area is the exact rational

\`\`\`text
S25 = 3218137345754103957378935 / 426045785417908030352880504.
Certified fraction >= 1-S25/2
  = 848873433490061956748382073 / 852091570835816060705761008
  = 99.6223249406636618... % of [1,3] x [0,1].
\`\`\`

This is an exact rational area certificate. It identifies where a still-better native tree could potentially exist, not a claim of outside mathematical admission.

## Theorem 3 — sharpened all-price regret

Let P be the feasible F policy for \`1<=x<=3\` and the inherited exact high-price policy for \`x>=3\`. For every \`0<=lambda<=1\`, \`x>=1\`:

\`\`\`text
0 <= P(lambda,x)-v(lambda,x) <= M25
M25 = (25/4) / (sqrt(7219)+sqrt(57583/8))^2
    = 0.000216759989763344483959... terminal-price units.
\`\`\`

Proof: concavity in x makes secants between exact G25 endpoints global lower bounds, while F is feasible. The exact envelope on each adjacent \`[a,b]\` is \`M(a,b)=50*(b-a)/(sqrt(K(a))+sqrt(K(b)))^2\`, \`K(x)=7557-169*x\` (the inherited chord-envelope identity). Exactly five unsplit intervals have width 1/8; their largest left endpoint is x=2, and for fixed width the envelope increases to the right, so \`[2,17/8]\` maximizes among them. Every other grid interval has width at most 1/12, whence \`M<=50/(12*4*7050)<50/(8*4*7219)<=M(2,17/8)\`, a strict rational comparison. The K endpoints of the dominant interval are 7219 and 57583/8. For x>=3 use the inherited exact high-price theorem.

## Reproduction and limitations

Original SHA256s: \`frozen_original_master.txt=cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e\`; \`EC49FPG_PROFILE.csv=a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f\`. Eight new full Bellman certificates were independently recomputed with all 228 first physical labels and all tied-first full tree replays. The 89 inherited certificates were checked against their file-by-file SHA256 manifest. Exact area and envelope comparisons were checked with rational arithmetic. A separate exact native Bellman probe at \`(x,lambda)=(73/32,7130/229487)\` obtained F and first labels \`{32,34,140,142}\` at one off-grid parameter point, without claiming the entire price slice.

Complete self-contained 97-anchor local archive: \`EC49FQS_TWO_SLICES_25GRID_COMPLETE_EVIDENCE_20261116.tar.xz\`, with independent verification program, frozen inputs, original generator, detailed paper, logs and per-file SHA256 manifest. The companion GitHub JSON index records exact case digests and archive hash. This GitHub branch is portable scientific evidence; **formal Task RS-EC49AS is not published** at the most recent control continuation read \`r4-ec49fqs-20261116-0922-continuation-read\` (FAILED / CANONICAL_REJECTED: unknown current immutable task publication). No formal CLAIM, Result or native Activity checkpoint is asserted.

**Next:** test x=33/16 within the new worst interval \`[2,17/8]\`, or derive a uniform parametric Bellman lower bound on the remaining 24 phase-curve bands. In particular determine whether \`lambda=310*(3-x)/(7557-169*x)\` is the exact whole-domain A/B transition. Preserve the frozen science and distinct P000/native acceptance boundaries.
