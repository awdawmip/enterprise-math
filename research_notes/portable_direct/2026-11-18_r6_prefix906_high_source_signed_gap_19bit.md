# PREFIX-906 — High-source signed gaps: uniform collision lift and exact 19-bit census

Date: 2026-11-18 (Asia/Shanghai). Lane: 进取数论研究6; independent portable-direct BRC auxiliary mathematics.
Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d (unaltered).
Predecessor: PREFIX-905 (certified union 7,686,920,802).
Status: AUTHOR_PROVED / EXACT_FULL_FINITE_CHECKED / INDEPENDENT_INTEGER_RECOUNT / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Ownership: no claim of shared X6 TASK CLAIM; current live owner must be established through original canonical continuation receipt.

## Exact model

Set p=32, N=2^32 and Q={262145,262147,...,524287} (|Q|=131072). Legal, named directed XOR trajectories are Z_x=(x,x) and F_x^k=(x,x XOR 2^k), 0<=x<N, 0<=k<32. Observations are Phi_(a,b)(u,v)=(u mod a,v mod b) for a,b in Q. Full trajectory identity includes the source bit and both endpoints. The two-port map is a deliberately auxiliary observer and does not erase native X6 identity.

## Theorem 906-A — Uniform high-source gap collision

For every a,b in Q with a>b, assume that integers m,i,j,s exist satisfying

* m odd, 1<=m<=8191;
* 18<=i<=30, 1<=j<=17, s in {+1,-1};
* m(a-b)=2^i+s*2^j.

Then two distinct admissible named XOR trajectories have identical two-port observations. The same conclusion holds when b>a, by swapping the ports and reversing both legal trajectories.

Proof. Write H=2^i, h=2^j, A=ma, B=mb, t=2h. Thus t<=2^18<=H. In the plus case choose x=(h-(A mod t)) mod t; in the minus case choose x=(-A) mod t. Set y=x+A. Then 0<=x<t<=H and x XOR H=x+H. For plus, y mod t=h, so y XOR h=y-h; for minus, y mod t=0, so y XOR h=y+h. Therefore
  F_x^i=(x,x+H), F_y^j=(y,y-s*h)
have start difference A=ma and end difference (y-s*h)-(x+H)=A-H-s*h=B=mb. Both observations agree.

The construction is valid *uniformly over the whole declared Q*: x<t<=262144, H<=2^30, hence x+H<2^32. Moreover y<=8191*524287+262143=4,294,696,960 and y+h<=4,294,828,032<4,294,967,296. Also y-s*h>=0 from the bit conditions. Since y>x and i!=j, the two named transitions are distinct. This proves the theorem. Reversal interchanges the two observations and preserves XOR legality and provenance.

The bound m<=8191 and j<=17 supports these uniform endpoint inequalities; no physical time-reversal claim is made.

## Theorem 906-B — Exhaustive specified new-gap domain and exact union

Let D_old consist of all positive dyadic gaps 2^h (1<=h<=17), all signed two-source gaps 2^i +/- 2^j (1<=j<i<=17), and all gaps covered by PREFIX-905 (odd multiplier 3..8191 with 1<=j<i<=17), each deduplicated. Define D_906 as the set of even d with 2<=d<=262142, d not in D_old, such that m*d=2^i +/- 2^j with odd 1<=m<=8191, 18<=i<=30 and 1<=j<=17.

Exact exhaustive generation yields |D_906|=857. For each d there are 131072-d/2 pairs a>b in Q with a-b=d; each has the explicit witness from Theorem 906-A. Reversed pairs are disjoint and equally certified.

The prior certified union C_905 is the union of (i) the PREFIX-897 E-set, (ii) rows/columns touching the 192-member P-panel, and (iii) precisely all D_old gap pairs. Its known size is 7,686,920,802. Membership in E is the exact predicate
  ab<33*2^32 or a in U or b in U or lcm(a,b)<2^32 or
  33*ceil(2^32/a)>b or 33*ceil(2^32/b)>a,
where the original PREFIX-897 U is the 552-member set constructed in the executable program. P={510000+k+194*r: k in {1,3,5}, 0<=r<64}.

The independently reproduced complete positive-gap census (all integers, each actual witness checked) is:

| Category | Positive-gap ordered pairs |
|---|---:|
| All D_906 pairs | 79,950,454 |
| Previously E | 35,590,676 |
| Touch P | 189,860 |
| E intersect P | 5,519 |
| Previously certified E union P | 35,775,017 |
| New relative to C_905 | 44,175,437 |

By disjoint gap exclusion and reversal,
  Delta_906 = 2*44,175,437 = 88,350,874,
  |C_906| = 7,686,920,802 + 88,350,874 = 7,775,271,676,
  |Q^2 minus C_906| = 17,179,869,184 - 7,775,271,676 = 9,404,597,508.

The complement is exactly the still-uncovered domain of this enumerated certificate union, not an assertion of injectivity.

## Independent concrete witness

For a=376529, b=376455, m=7085, i=19, j=1, s=+1, the gap is d=74 and m*d=524290=2^19+2.
The two named legal trajectories are
  F^19_1=(1,524289),
  F^1_2667707966=(2667707966,2667707964).
Their start difference is 2,667,707,965=7085*a and their end difference is 2,667,183,675=7085*b. The pair lies outside C_905; d=74 belongs to D_906 and not to the preceding gap set.

## Evidence and reproduction

Two separate implementations were executed locally on exact integer arithmetic:
1. NumPy int64 enumerator (PREFIX906_R6_HIGH_SOURCE_SIGNED_GAP_RESULTS.json, local full 857-row output): constructs and checks every directed XOR witness across all 79,950,454 a>b parameter pairs and recomputes E/P intersections. The serialized 857-row numeric array has SHA256 3dc0d13a37e4ad37fc8ae5cea2d4189f6e79dc6b7a6ec96ee93e9ec3eac882c0.
2. Independently coded C++17 integer/gcd verifier PREFIX906_R6_INDEPENDENT_INTEGER_CHECK.cpp: re-generates the 857 gaps and performs all 79,950,454 per-pair witness and old-union tests; observed output was:
  79950454 35590676 189860 5519 35775017 44175437
  PASS; gap_types=857; new_ordered=88350874; total=7775271676

Compiler: g++ -O3 -std=c++17; all tested integer quantities fit signed 64-bit. This file is a complete reproducible checker, including the source of the original U/P membership sets. The JSON summary preserves the expected totals, model, witness and the local full-row digest; it is not a substitute for running the checker.

## Scientific meaning and next discriminating question

This result expands a proven finite family of collisions in a provenance-preserving BRC two-port observation model. P000 Heartbeat World X6 six-spatial-axis ontology, separately typed time and the source firewall are unchanged. This auxiliary result is not by itself a full-state native-world descent certificate.

The mother question B_fix,odd(32) in {19,20} remains open. A useful next direction is a generalized two-flip modular-difference construction allowing different multiples for the start and end differences; another is applying the full exact two-flip classifier to the remaining 9,404,597,508 parameter pairs. Check existing certified sets before assigning any new net exclusion count.
