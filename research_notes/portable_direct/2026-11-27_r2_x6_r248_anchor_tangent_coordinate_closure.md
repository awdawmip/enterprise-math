# X6 R248 — coordinate tangent kernels at a fixed anchor; zero-germ closure

2026-11-27. Informed independent TASK_RESEARCH, author derivation + exact BigInt computation, NOT_REVIEWED. Native read request r2-20261127-0208-x6-read SUCCEEDED, observed 2026-11-26T18:08:44.525520Z, Source e7ccfa2cc710ee5623a417d00986c8eed1e2fcf5, NO_CANONICAL_PUBLICATION_DIRECTORY. This is directory absence only, not an active-owner or researcher-binding projection. No CLAIM, Result, Review, task or protected-state mutation. Activity association pending.

## Sources and frozen scope
- R247: 7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md, blob fdbef2ee6e6c32573f3a1ccd171cb5337de520fa. Its complete embedded JavaScript and exact data were read and reused without altering direction population, necessary-wall inputs, linear suffix bank, or rank-four arrangement/recursion algorithm.
- R238: a64888948bdacb5ba4e691d3eb2b783ed43f56ea:research_notes/portable_direct/2026-11-26_r2_x6_r238_one_support_factor_root_family_closure.md, blob 9b05af42eef4b4351130e2a6f8a53f8995b749e9. Read full proof: zero germ on a nondegenerate support interval implies that support's linear factor divides Q; all Q=L_i M already excluded as unique quadratic root with five arbitrary linear suffix queries.
- Same frozen Port 10, 1935 integer directions, six-pair BRC, positive weights (17t,B,22t,D), 47 necessary support labels, 49 components, 51 endpoint rays, 98 directed interval germs, 2225 linear suffix partitions. This is static auxiliary weight-coefficient arithmetic, not a native spatial plane. All exclusions inherit the necessary-wall theorem and the completeness/capacity argument of R247 and its pinned predecessors; no independent review claimed.

## Algebraic reduction of the single-anchor kernel
The single zero constraint Q(p18)=0 at p18=(0,1,0) sets the B^2 coefficient to zero:
Q=a t^2+c D^2+d tB+e tD+f BD.
The symmetric determinant is -(a f^2 - d e f + c d^2)/4. At p18 the polar/tangent linear form, up to a nonzero factor, is d t+f D, since the gradient is (d,0,f). A full-rank member has (d,f) not both zero. R247 closed the subspace f=-12c; this turn tests two different four-dimensional kernels f=0 and d=0. For f=0, det A=-c d^2/4; for d=0, det A=-a f^2/4. These are exact continuous coefficient families, including singular cases, not samples.

## Exact calculation and closure
Reused signed first-active rank-four face enumeration and suffix capacity recursion from R247. Only the jet rows and the result label were changed; all arithmetic BigInt, original branch-exchange canonicalization and rank/coverage checks retained. Actual outputs from two executions:

| Field | f=0 | d=0 |
|---|---:|---:|
| primary groups | 48 | 51 |
| ray visits | 49732 | 58927 |
| edge visits | 199916 | 237048 |
| facet visits | 399832 | 474096 |
| open masks | 16867 | 20045 |
| open direct | 15289 | 18517 |
| open recursive exclusion | 1578 | 1528 |
| open checks | 4079285 | 3676013 |
| boundary optimistic masks | 116737 | 138349 |
| boundary direct | 99947 | 121860 |
| boundary recursive exclusion | 16709 | 16413 |
| boundary relaxed survivors | 81 | 76 |
| boundary checks | 5054923 | 5088585 |
| survivor kernel dimensions (1,2,3) | 38,37,6 | 36,34,6 |
| refined distinct full masks | 42 | 40 |
| refined recursive exclusion | 39 | 37 |
| refined relaxed survivors | 3 | 3 |
| refined checks | 425498 | 408210 |
| total checks | 9559706 | 9172808 |

All unknown lists empty in both runs. Counts across different families can overlap; they are not counts of distinct conics. There are precisely the SAME three relaxed full-mask pairs in both runs (the order of bits is the pinned R247 order):
```json
[
["33cf3303c4c003300cff3fd0","3cc30ccfc3b3ffccfc000c02f","33000000",[24,25,28,29],[11,13]],
["33cf3303c4c003300fff3fd0","3cc30ccfc3b3ffccfc000c02f","30000000",[28,29],[13]],
["33cf3303c4c003300fff3fd0","3cc30ccfc383ffccfc000c02f","300000030000000",[28,29,56,57],[13,26]]
]
```
Each row contains branch masks, complement zero mask, zero germ indices, and support labels (zero based). Exact bit decoding in this turn confirmed the following nondegenerate components:
- germs 24,25, support 11, normal (22,0,-1), endpoints (0,1,0),(1,17,22);
- germs 28,29, support 13, normal (74,0,-1), endpoints (1,9,74),(1,4,74);
- germs 56,57, support 26, normal (40,0,-3), endpoints (0,1,0),(3,38,40).
All three masks necessarily contain a zero germ on support 13. By R238, Q must be divisible by 74t-D, and the entire such family was already excluded. This closes all six relaxed occurrences without additional refinement or claiming the relaxed masks themselves are infeasible. Consequently under the inherited proof premises, both four-dimensional kernels are fully excluded as the sole quadratic root of a depth-six correct tree. Any remaining full-rank single-anchor quadratic must have d f nonzero (and f != -12c by R247). No general five-dimensional closure yet.

## Further author lemma: pole/residue representation
On t>0 set x=B/t, y=D/t. For f nonzero put R=a f^2-d e f+c d^2=-4 det A. Exactly
Q/t^2=(d+f y)(x+(c/f)y+(ef-cd)/f^2)+R/f^2.
If R nonzero, y=-d/f is not a zero on this chart; the zero set elsewhere is
x=-(c/f)y-(ef-cd)/f^2-R/[f^2(d+f y)].
Its second derivative as an auxiliary coefficient curve is -2R/(d+f y)^3, nonzero and constant-sign on each side of the pole. The identity follows by multiplication; differentiating the rational expression twice gives the stated derivative. If R=0 it factors into two real linear forms, already excluded by R242. This provides an exact parameterization for the remaining five-dimensional kernel: after normalizing f=1, the pole y=-d, two affine graph coefficients, and nonzero residue R give four independent projective parameters. At t=0 the homogeneous jets must still be retained; the rational chart does not eliminate those observations. Next: classify sign constraints on these four parameters using fixed anchor-fan directions and cached capacity conflicts; do not assume the pole is outside the positive domain or replace full germs by endpoints.

## Reproduction (actual patch applied to the immutable R247 source)
Read the R247 markdown above at the exact commit. Extract its first JavaScript block into string s. For f=0 the actual changes were:
```javascript
s=s.replace("D*(D-12n*B)","D*D")
   .replace("2n*D*z-12n*(B*z+D*y)","2n*D*z")
   .replace("z*(z-12n*y)","z*z")
   .replace('rank4("two_anchor_kernel",[])','rank4("single_anchor_f_zero",[])');
```
For d=0 start from the original s:
```javascript
s=s.replace("[t*t,D*(D-12n*B),t*B,t*D],[2n*t*x,2n*D*z-12n*(B*z+D*y),t*y+B*x,t*z+D*x],[x*x,z*(z-12n*y),x*y,x*z]",
"[t*t,D*D,B*D,t*D],[2n*t*x,2n*D*z,B*z+D*y,t*z+D*x],[x*x,z*z,y*z,x*z]")
.replace('rank4("two_anchor_kernel",[])','rank4("single_anchor_d_zero",[])');
```
In both executions replace the terminal expression by return:
```javascript
s=s.replace(/experiment\(data\)\s*$/,"return experiment(data)");
const out=Function(s)();
```
Read out.result.open, boundaryOptimistic, refined, dimHist, totalChecks; full intermediate masks and provenance are returned by the unchanged original function. Verify zero masks for every refined survivor using
```javascript
const ALL=(1n<<98n)-1n;
for(const [a,b] of out.result.refined.survivors){
  const A=BigInt("0x"+a), B=BigInt("0x"+b);
  if(A&B)throw Error("overlap");
  const zero=ALL^(A|B);
  if((zero&(3n<<28n))!==(3n<<28n))throw Error("missing support 13");
  // Map germ 2*j or 2*j+1 to component j in R247 parts, preserving split order.
}
```
The actual independent bit decoding yielded the indices and support normals above. The two complete enumeration runs and bit decoding were executed in the tool JavaScript runtime. The new pole/residue identity is hand-derived, not an extra numerical experiment. No new formalization or canonical mathematical admission. Open: general single-anchor kernel, generic full-rank root and unique quadratic below linear ancestors, unrestricted K6 remains 1–2.
