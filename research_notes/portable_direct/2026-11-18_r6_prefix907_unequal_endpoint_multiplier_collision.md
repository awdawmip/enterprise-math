# PREFIX-907 — Unequal endpoint-multiplier signed-gap collision and exact 19-bit union

Date: 2026-11-18 (Asia/Shanghai). Research lane: 进取数论研究6; independent portable BRC named-XOR observer.
Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Predecessor: PREFIX-906, certified union size C906=7,775,271,676.
Evidence status: AUTHOR_PROVED / COMPLETE_DECLARED_FINITE_EXACT_CHECK / TWO_INDEPENDENT_IMPLEMENTATIONS / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Model

Take p=32, N=2^32, and Q={262145,262147,...,524287} (|Q|=131072). Legal provenance-retaining directed tracks are Z_x=(x,x) and named F^i_x=(x,x XOR 2^i), 0<=x<N, 0<=i<32. The declared auxiliary two-port observer is Phi_(a,b)(u,v)=(u mod a,v mod b), for a,b in Q. The source names, direction and full integer endpoints remain distinct before observation; no claim is made about native X6 Cell-state collapse.

## Theorem 907-A — Unequal-multiplier collision construction

For any a,b in Q, positive integers k,ell, distinct source indices 0<=j<i<32, sign s in {+1,-1}, suppose

  k*a-ell*b=2^i+s*2^j.

Write A=k*a, H=2^i, h=2^j and t=2*h. If the following constructed endpoints are in the admissible interval [0,N), two distinct named trajectories collide:

  x=(h-(A mod t)) mod t, y=x+A, for s=+1;
  x=(-A) mod t, y=x+A, for s=-1;

  F_x^i=(x,x+H), F_y^j=(y,y-s*h).

Indeed 0<=x<t<=H, so x XOR H=x+H. In the plus case y mod t=h, hence y XOR h=y-h; in the minus case y mod t=0, hence y XOR h=y+h. Therefore the trajectories have start difference y-x=k*a, and endpoint difference (y-s*h)-(x+H)=ell*b. This proves agreement in both modular observations. They are distinct by their source indices and positive start difference.

The endpoint hypothesis is automatically satisfied for the **declared census** below: k=3, ell=1, 18<=i<=22, 1<=j<=17. Specifically x<2*h<=2^18, x+H<=2^18-1+2^22<2^32, y<3*524287+2^18<2^32, and y+h<3*524287+3*2^17<2^32. For s=+1 the low bit j of y is 1 and y-h is nonnegative. Reversal of both legal directed flips with port interchange gives a collision for the reversed ordered parameter pair (b,a), without treating physical time as reversible.

PREFIX-905/906 used equal multipliers on both ports, k=ell=m. This new theorem allows different endpoint multiples, and the finite application below uses k=3,ell=1.

## Theorem 907-B — Exact new union against PREFIX-906

Let R be all ordered pairs (a,b) in Q^2 for which there exist
  i in {18,19,20,21,22}, j in {1,...,17}, s in {+1,-1}
satisfying
  3*a-b=2^i+s*2^j.
The C++ exact verifier enumerates all 170 source/sign combinations and all 131072 values of a, constructs the actual directed named XOR witness for each admissible b, and deduplicates (a,b). It finds
  |R|=2,905,419.

Let C906 be the **explicit previously certified union** from PREFIX-906, exactly composed of:
  E = {ab<33N or a in U or b in U or lcm(a,b)<N or 33 ceil(N/a)>b or 33 ceil(N/b)>a},
  all pairs with a or b in the exact 192-member panel P,
  all pairs whose |a-b| belongs to the 258 PREFIX903/904 gap types,
  all pairs whose |a-b| belongs to the 276 novel PREFIX905 odd-multiple gap types,
  all pairs whose |a-b| belongs to the 857 novel PREFIX906 high-source gap types.
Here U is the same 552-member PREFIX-897 special-modulus set explicitly re-generated in the verifier; P={510000+t+194r:t in {1,3,5}, 0<=r<64}.

Set A=R\C906, and R^T={(b,a):(a,b) in R}. C906 is symmetric under exchanging a and b. The independent integer census finds
  |A|=1,576,800,
  |A intersect A^T|=188.
Thus the newly proven distinct ordered pairs obtained by R and its reversed witness family, after deduplication against C906, are

  Delta907=|A union A^T|=2*1,576,800-188=3,153,412.

Therefore
  |C907|=7,775,271,676+3,153,412=7,778,425,088,
  |Q^2 minus C907|=17,179,869,184-7,778,425,088=9,401,444,096.

The latter finite complement is the exact domain not covered by this enumerated family of collision certificates, not a proven injective family.

## Constructed witness not in C906

Take a=272007, b=521109, k=3, ell=1, i=18, j=15, s=+1.
Then k*a-ell*b=816021-521109=294912=2^18+2^15. Set x=3179, y=819200.

  F^18_3179=(3179,265323),
  F^15_819200=(819200,786432).

Both are legal named XOR flips, their start difference is 816021=3a and endpoint difference is 521109=b. Direct exact membership checks of E/P and all old gap classes show (272007,521109) not in C906.

## Verification and evidence

The published C++17 verifier reconstructs every old exclusion class, tests all 2,905,419 candidate-pair witnesses, deduplicates 64-bit encoded pairs, and evaluates full old-union membership using 64-bit products/lcm to avoid 32-bit overflow. The code was actually compiled with g++ -O3 -std=c++17 and completed:

  candidate=2905419 novel_oriented=1576800 reverse_overlap=188 new_union=3153412
  PASS total_union=7778425088 remaining=9401444096

A separately implemented Python exact-integer membership/counting enumeration independently obtained the same 2,905,419 / 1,576,800 / 188 / 3,153,412 counts. All operations are integer exact and the declared candidate family was exhaustively enumerated. This is an author proof and machine computation, not independent mathematical review or formal admission.

## Ontology and next scientific question

P000 Heartbeat World remains the six-dimensional signed native Cell space with separately typed time and triadic closure. The observer above is auxiliary; its collisions retain explicitly named source provenance in the full trajectory and do not assert equivalence of future native X6 operations.

This construction suggests a general two-multiplier geometry: test small distinct (k,ell) for additional nonoverlapping coverage or derive a residue/fiber reduction that proves collision for all remaining Q^2 candidate pairs. Preserve genuine injective modulus witnesses if found. The mother objective B_fix,odd(32) in {19,20} is still open. Shared native X6 Task/CLAIM, Source Activity, Result/Review and theorem admission require their separate verified authority and must not be inferred from this portable paper.
