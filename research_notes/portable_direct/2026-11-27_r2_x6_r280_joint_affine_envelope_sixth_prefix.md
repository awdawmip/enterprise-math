# X6 R280 — complete affine envelope compression and sixth-pencil continuation

2026-11-27. Independent informed TASK_RESEARCH, author proof/computation, NOT_REVIEWED. Native topic lookup r2-20261127-2315-x6-read SUCCEEDED at 15:15:24.574880 UTC, Source 82eb41339f5a47a3ce329f43acd2578a94d96cf3, NO_CANONICAL_PUBLICATION_DIRECTORY, metadata only, no owner projection. Own researcher binding unconfirmed; no CLAIM, formal Result, Review or shared control mutation. Activity association pending. P000 V5, ACTIVE worldview, joint-relation and residual fidelity retained. Auxiliary BRC weight-coefficient algebra, not a native spatial plane or dynamics.

## Frozen inputs
- R247@7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md
- R275@001076e59298e45715cb58c87ab3395c53d005a8:research_notes/portable_direct/2026-11-27_r2_x6_r275_monic_block_compression_and_strict_prefix.md
- R276@33fba542db5f810e803d770b7046b5e26ac1ebb9:research_notes/portable_direct/2026-11-27_r2_x6_r276_strict_fifth_pencil_packed_frontier.md
- R277@a1df3c1aa315909d8c109ef8551f24a460a44b1f:research_notes/portable_direct/2026-11-27_r2_x6_r277_incremental_slope_projection_sixth_prefix.md
- R279@410d1b57f46a2245ce3453d0b3087606905a3b1e:research_notes/portable_direct/2026-11-27_r2_x6_r279_interval_dominance_verified_sixth_prefix.md

Same frozen Port 10, 1935 directions, six-pair BRC, 47 support tags, 51 endpoints, 98 directed germs, 2225 pure-linear suffix masks. Capacity exclusions inherit R247 necessary-wall and complete suffix premises. Strict words c=1 only. Previous classified 177750/667787, survivors 1387, next [2250,0]. Do not replay earlier capacity decisions.

## Theorem: full affine-envelope state
In the exact R277 strict-row state (P,M,I), for each positive-A row define g=-(Bf+C)/A and for each negative-A row take -g. Both transformed lines have slope -B/|A| and intercept -C/|A|. Each side uses its maximum envelope (neg side then negated). Sort slopes increasingly, retain maximal intercept among equal slopes, and keep a stack of lines with strictly increasing activation coordinates. For a previous line a and new line b, intersection is (c_a*d_b-c_b*d_a)/(m_b*d_a-m_a*d_b) where each line=(m*f+c)/d and d>0. Pop a when its activation is at or after that intersection: before its activation an older line dominates a; at or after it b dominates a. The new line is larger than a after intersection, and smaller before. Induction yields the exact maximum envelope on all R, including ties by continuity. Discard lines whose open active interval does not intersect the nonempty open I (retain a line covering each open subinterval; continuity preserves event-point values). Empty sides remain empty. Keep I, retained upper/lower rows, seen keys and original endpoint words/germ masks. The feasible set equals the uncompressed feasible set, hence intersecting arbitrary future constraints preserves equality. Removed rows remain implied even when their keys repeat. No merging of different words or germ masks. This improves R279 pairwise dominance by allowing several lines jointly to dominate one. Sorting costs O(m log m) comparisons, stack O(m) intersection comparisons, clipping O(m) comparisons, with exact rational cross products; integer bit cost, base row generation, branch copying, suffix bank and recursive capacity work are separate. No wall-clock improvement claimed.

## Executed calculation
Start 2250, size 150, suffix cap 12000000. Exact BigInt arithmetic; compressed vs raw feasibility and projected rational endpoints compared for every algebra-tested extension; first 100 also checked against R275 full elimination. Pairwise R279 dominance baseline measured on same base states. Pair counts are sixth-extension grow calls only; no runtime speed comparison. R276 support projection tests repeated. Results:
```json
{"hist":{"direct":4371,"alg":6866,"recursive":611,"surv":2,"visits":11850,"checkedAgainstOld":100},"checks":2251156,"next":[2400,0],"groups":[[18,2,0,36],[6,5,43],[48,21,29,23,46],[4,14,16,12,3,8],[26,19,34,20,25,28,39,1,37],[10,15,11,45,49,9,38,42,40,44,47,50]],"stats":{"prefixes":150,"rawRows":8469,"hullRows":545,"pairRows":632,"hullIntersections":14439,"pairDominanceTests":46554,"compared":7479,"rawPairs":3466211,"hullPairs":1732223},"partial":false}
```
Cumulative classified 189600/667787; survivors 1389; unknown 478187. Necessary-condition survivors only. Next [2400,0].
All newly surviving words (prefix index: hex mask of sixth words):
```text
2262:4100000000000000
```

## Reproduction
Use the R277 reconstruction from the pinned four notes. Insert this code immediately before function grow:
```javascript
let pairCalls=0,stats={prefixes:0,rawRows:0,hullRows:0,pairRows:0,hullIntersections:0,pairDominanceTests:0,compared:0,rawPairs:0,hullPairs:0};
function cmp(a,b){let d=a[0]*b[1]-b[0]*a[1];return d<0n?-1:d>0n?1:0}
function envelope(rows,st){
 let lines=rows.map(r=>({r,m:-r[1],c:-r[2],d:abs(r[0])}));
 lines.sort((a,b)=>cmp([a.m,a.d],[b.m,b.d])||cmp([b.c,b.d],[a.c,a.d]));
 let H=[];
 for(let l of lines){
  if(H.length&&cmp([H[H.length-1].m,H[H.length-1].d],[l.m,l.d])===0)continue;
  let at=null;
  while(H.length){
   let a=H[H.length-1];at=[a.c*l.d-l.c*a.d,l.m*a.d-a.m*l.d];stats.hullIntersections++;
   if(at[1]<=0n)throw Error("slope order");
   if(a.at===null||cmp(at,a.at)>0)break;
   H.pop();
  }
  H.push({...l,at:H.length?at:null});
 }
 return H.filter((l,i)=>(!st.hi||!l.at||cmp(l.at,st.hi)<0)&&(!st.lo||i===H.length-1||cmp(H[i+1].at,st.lo)>0)).map(l=>l.r)
}
function pairPrune(st){
 function cutOK(b,c){if(st.lo?b*st.lo[0]+c*st.lo[1]<0n:b>0n)return false;if(st.hi?b*st.hi[0]+c*st.hi[1]<0n:b<0n)return false;return true}
 function dom(p,r,side){stats.pairDominanceTests++;return cutOK(side*(r[1]*p[0]-p[1]*r[0]),side*(r[2]*p[0]-p[2]*r[0]))}
 function keep(rows,side){return rows.filter((r,i)=>!rows.some((p,j)=>i!==j&&dom(p,r,side)&&(j<i||!dom(r,p,side))))}
 return {pos:keep(st.pos,1n),neg:keep(st.neg,-1n)}
}
function prune(st){let pos=envelope(st.pos,st),neg=envelope(st.neg,st),p=pairPrune(st);stats.prefixes++;stats.rawRows+=st.pos.length+st.neg.length;stats.hullRows+=pos.length+neg.length;stats.pairRows+=p.pos.length+p.neg.length;return {...st,pos,neg}}
function same(a,b){return a===null||b===null?a===b:cmp(a,b)===0}
function both(st,raw,N){let before=pairCalls,a=grow(st,N);stats.hullPairs+=pairCalls-before;before=pairCalls;let b=grow(raw,N);stats.rawPairs+=pairCalls-before;stats.compared++;if(!!a!==!!b||a&&(!same(a.lo,b.lo)||!same(a.hi,b.hi)))throw Error("envelope mismatch");return !!a}
```
Increment pairCalls in grow's pair function before return cut. Replace base construction by let raw=grow(empty,R);if(!raw)throw Error("old bank infeasible");let st=prune(raw);. Replace let good=!!grow(st,N); by let good=both(st,raw,N);. Add stats to both return objects. Set ceiling=12000000, start=2250,size=150. If cutoff occurs next is first unclassified local index. Retain prior banks and this bank, do not repeat classified prefix. Next continue sixth line from [2400,0], then singleton and mixed zero words; K6=1–2. Independent review and activity association remain pending.
