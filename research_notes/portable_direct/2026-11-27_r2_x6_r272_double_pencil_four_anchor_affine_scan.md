# X6 R272 — noncommon-zero double-pencil four-anchor affine scan

2026-11-27. Independent informed TASK_RESEARCH, author proof and exact BigInt computation, NOT_REVIEWED. Native read r2-20261127-1613-x6-read SUCCEEDED 2026-11-27T08:13:26.125836Z at Source 7999d97ec0485a6d1915ed9847f59c77397798e0, NO_CANONICAL_PUBLICATION_DIRECTORY, directory absence only; active owner projection and own researcher binding not established. Identity-only client check succeeded without research authority. No CLAIM, formal Result, Review or shared control mutation; Activity association pending. P000 V5, ACTIVE worldview, joint relation and residual fidelity retained. All coordinates below are auxiliary observation coefficient coordinates, not native spatial geometry.

## Frozen question and new unit
R271 f1ec411dfb652bbeab5e288af796eefb7a14280c:research_notes/portable_direct/2026-11-27_r2_x6_r271_common_zero_root_closure.md closes c=0 at author proof/calculation level; R258 closes internal quadratic positions. Keep the same Port 10, 1935 integer directions, six-pair BRC, weights (17t,B,22t,D), strict 3/2, 47 support labels, 51 endpoints, 98 directed germs, 2225 linear suffix masks and R247 executable at 7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md (blob fdbef2ee6e6c32573f3a1ccd171cb5337de520fa). All capacity exclusions inherit the necessary-wall and complete pure-linear suffix premises. No change to the frozen scientific input. Study c!=0, normalized c=1 by branch exchange and division. Target: two distinct pencils through p24=(0,0,1) with two finite sampled zeros on each. This is independent of the strict-sign extension of R259 and does not assume other endpoints nonzero.

## Exact one-parameter theorem
Let v=(T,U), w=(V,W) be independent primitive pencil directions, H=det(v,w)!=0. Write X=det((t,B),w), Y=det(v,(t,B)), Z=H D. The invertible auxiliary map gives (t,B)= (X v+Y w)/H. Four distinct sampled zeros on these two pencils are p_i=(r_i v,A_i) for i=1,2 and p_j=(r_j w,A_j) for j=3,4, with positive integer r_i (for the frozen data). Set h_i=A_i/r_i. A normalized quadratic in (x=X/H,y=Y/H,D) with D² coefficient 1 has independent coefficients on xD,yD,x²,y²,xy. Its two pencil restrictions must be monic products (D-h1 x)(D-h2 x) and (D-h3 y)(D-h4 y). Consequently the entire family is
Q=D²-(h1+h2)xD-(h3+h4)yD+h1 h2 x²+h3 h4 y²+lambda xy, lambda real.
The four constraints are independent, because each pair of distinct ordinates uniquely determines its line's slope and intercept. Conversely every real lambda has the four required zeros and c=1. With F=r1*r2*r3*r4>0, multiplication by F H² gives the integer-coefficient affine family
F Z²-(A1 r2+A2 r1)r3 r4 XZ-(A3 r4+A4 r3)r1 r2 YZ+A1 A2 r3 r4 X²+A3 A4 r1 r2 Y²+k XY, k=F lambda.
This covers all full-rank forms in the stated family; scanning even singular forms is a conservative relaxation. No assumption of exactly four zero endpoints.

## Complete full-jet scan
For each directed germ p->q set v=q-p. Each evaluation is an affine pair (a,b) meaning a+b k. The exact jet is (Q(p), Q(q)-Q(p)-Q(v), Q(v)). Collect every rational event -a/b for nonzero b across all 98*3 rows, deduplicate and sort by integer cross products. Evaluate at each event, one mediant between consecutive events, and one rational sample outside each extreme. Every row has constant sign on each open interval, and every event is evaluated exactly, so the lexicographic sign of all three rows is constant on each open interval; a row identically zero is retained as zero. This covers the entire real parameter, including all tangency and additional-zero strata. Only global branch exchange is deduplicated (symmetric capacity criterion). No loss of joint signs or residuals. An identically zero germ is unassigned, giving a necessary relaxation only. Each branch has 31 support-label capacity and must pass the frozen can(mask,5) recursion. Failure excludes every parameter of that mask. All samples here use BigInt and rational denominator positive, no floating-point sign test.

## Actual computation
Executed t=0 paired with B=9t or B=4t. Frozen endpoint IDs [[0,2,18,36],[5,6,43],[21,23,29,46,48],[1,19,20,25,26,28,34,37,39]] for t=0, B=9t, B=4t, B=17t respectively. All 6*3 + 6*10 = 78 four-anchor families were covered (including any extra zero endpoints). Result {"events":12259,"samples":24596,"bank":5453,"direct":4851,"excluded":602,"checks":968117}, CUT=null, surviving masks []. The number of visits counts per-family cells and masks, not globally distinct coefficient sets. The 5453 per-family deduplicated masks include 4851 direct support count exclusions and 602 recursive exclusions. 968117 actual capacity bank checks; shared caching retained. Repeated identical run returned identical aggregates. No independent review. 
Per-family data (I,J,events,samples,bank,direct,excluded,survivors,checks):
```json
[[[0,2],[5,6],162,325,72,66,6,[],6863],[[0,2],[5,43],163,327,66,63,3,[],141],[[0,2],[6,43],159,319,64,53,11,[],15763],[[0,18],[5,6],153,307,73,47,26,[],41989],[[0,18],[5,43],160,321,77,68,9,[],423],[[0,18],[6,43],157,315,78,51,27,[],51786],[[0,36],[5,6],162,325,71,65,6,[],47],[[0,36],[5,43],163,327,65,63,2,[],0],[[0,36],[6,43],162,325,65,56,9,[],188],[[2,18],[5,6],154,309,74,48,26,[],29413],[[2,18],[5,43],159,319,78,73,5,[],141],[[2,18],[6,43],157,315,78,48,30,[],36352],[[2,36],[5,6],162,325,72,66,6,[],6769],[[2,36],[5,43],163,327,66,64,2,[],94],[[2,36],[6,43],162,325,67,58,9,[],9088],[[18,36],[5,6],157,315,72,39,33,[],46069],[[18,36],[5,43],160,321,77,58,19,[],22767],[[18,36],[6,43],156,313,76,49,27,[],53014],[[0,2],[21,23],159,319,67,67,0,[],0],[[0,2],[21,29],157,315,68,68,0,[],0],[[0,2],[21,46],158,317,68,68,0,[],0],[[0,2],[21,48],157,315,67,67,0,[],0],[[0,2],[23,29],158,317,66,66,0,[],0],[[0,2],[23,46],158,317,62,62,0,[],0],[[0,2],[23,48],159,319,65,65,0,[],0],[[0,2],[29,46],158,317,66,66,0,[],0],[[0,2],[29,48],159,319,67,67,0,[],0],[[0,2],[46,48],159,319,67,67,0,[],0],[[0,18],[21,23],153,307,72,66,6,[],6957],[[0,18],[21,29],153,307,73,63,10,[],9645],[[0,18],[21,46],151,303,74,58,16,[],33845],[[0,18],[21,48],153,307,68,59,9,[],33414],[[0,18],[23,29],155,311,71,71,0,[],0],[[0,18],[23,46],156,313,73,70,3,[],6910],[[0,18],[23,48],156,313,72,47,25,[],38389],[[0,18],[29,46],156,313,74,72,2,[],4591],[[0,18],[29,48],157,315,72,61,11,[],5052],[[0,18],[46,48],156,313,73,42,31,[],125115],[[0,36],[21,23],158,317,66,66,0,[],0],[[0,36],[21,29],159,319,67,67,0,[],0],[[0,36],[21,46],158,317,67,67,0,[],0],[[0,36],[21,48],158,317,67,67,0,[],0],[[0,36],[23,29],158,317,66,66,0,[],0],[[0,36],[23,46],159,319,64,64,0,[],0],[[0,36],[23,48],159,319,65,65,0,[],0],[[0,36],[29,46],159,319,66,66,0,[],0],[[0,36],[29,48],159,319,66,66,0,[],0],[[0,36],[46,48],159,319,65,65,0,[],0],[[2,18],[21,23],155,311,73,66,7,[],4732],[[2,18],[21,29],149,299,72,58,14,[],7710],[[2,18],[21,46],156,313,76,65,11,[],13632],[[2,18],[21,48],156,313,71,60,11,[],9493],[[2,18],[23,29],156,313,73,72,1,[],47],[[2,18],[23,46],154,309,74,71,3,[],2319],[[2,18],[23,48],156,313,74,50,24,[],36023],[[2,18],[29,46],149,299,72,70,2,[],2366],[[2,18],[29,48],154,309,73,62,11,[],4959],[[2,18],[46,48],157,315,75,43,32,[],81892],[[2,36],[21,23],158,317,67,67,0,[],0],[[2,36],[21,29],157,315,68,68,0,[],0],[[2,36],[21,46],159,319,68,64,4,[],282],[[2,36],[21,48],159,319,68,68,0,[],0],[[2,36],[23,29],157,315,65,65,0,[],0],[[2,36],[23,46],159,319,65,65,0,[],0],[[2,36],[23,48],159,319,66,66,0,[],0],[[2,36],[29,46],156,313,67,67,0,[],0],[[2,36],[29,48],159,319,67,67,0,[],0],[[2,36],[46,48],159,319,66,63,3,[],141],[[18,36],[21,23],151,303,71,64,7,[],18223],[[18,36],[21,29],152,305,72,65,7,[],329],[[18,36],[21,46],154,309,73,66,7,[],13585],[[18,36],[21,48],155,311,68,58,10,[],21258],[[18,36],[23,29],155,311,72,64,8,[],2601],[[18,36],[23,46],157,315,72,70,2,[],2319],[[18,36],[23,48],156,313,71,46,25,[],44923],[[18,36],[29,46],157,315,74,73,1,[],0],[[18,36],[29,48],156,313,71,59,12,[],11683],[[18,36],[46,48],157,315,74,43,31,[],104775]]
```

## Reproduce
Read first JavaScript block from the exact pinned R247 source, replace its final return inside experiment (the rank4("two_anchor_kernel",[]) result) with the following patch, and replace terminal experiment(data) with return experiment(data). Execute in ordinary JavaScript; no native time or spatial calculation asserted. The exact original P,G,tag and linear suffix bank remain unchanged.
```javascript

ceiling=30000000;
const det=(a,b)=>a[0]*b[1]-a[1]*b[0];
const directions=[[0n,1n],[1n,9n],[1n,4n],[1n,17n]];
const ids=directions.map(v=>P.map((p,i)=>i).filter(i=>i!==24&&!det(P[i],v)));
const pairs=xs=>xs.flatMap((x,i)=>xs.slice(i+1).map(y=>[x,y]));
function scan(v,w,I,J){
 let H=det(v,w),rad=(i,u)=>{let j=u[0]?0:1;return P[i][j]/u[j]};
 let [i,j]=I,[k,l]=J, r=rad(i,v),s=rad(j,v),m=rad(k,w),n=rad(l,w);
 let F=r*s*m*n,A=P[i][2],B=P[j][2],C=P[k][2],D=P[l][2];
 function val(p){
  let x=det(p,w),y=det(v,p),z=H*p[2];
  return [F*z*z-(A*s+B*r)*m*n*x*z-(C*n+D*m)*r*s*y*z+A*B*m*n*x*x+C*D*r*s*y*y,x*y];
 }
 for(let u of [...I,...J])if(val(P[u]).some(Boolean))throw Error("anchor");
 const jets=G.map(([u,v])=>{let a=val(P[u]),b=val(P[v]),c=val(sub(P[v],P[u]));return [a,b.map((x,i)=>x-a[i]-c[i]),c]});
 let events=new Map();
 for(let rows of jets)for(let [a,b] of rows)if(b){let q=norm([-a,b]);if(q[1]<0n)q=scale(q,-1n);events.set(q.join(),q)}
 let E=[...events.values()].sort((a,b)=>sg(a[0]*b[1]-b[0]*a[1]));
 let samples=E.length?[[E[0][0]-E[0][1],E[0][1]]]:[[0n,1n]];
 for(let i=0;i<E.length;i++){samples.push(E[i]);if(i+1<E.length)samples.push([E[i][0]+E[i+1][0],E[i][1]+E[i+1][1]]);else samples.push([E[i][0]+E[i][1],E[i][1]])}
 let bank=new Map(),before=checks, direct=0,excluded=0,survivors=[];
 for(let [p,q] of samples){let a=0n,b=0n;
  for(let i=0;i<jets.length;i++){let z=0;for(let [u,v] of jets[i]){z=sg(u*q+v*p);if(z)break}if(z>0)a|=G[i][2];else if(z<0)b|=G[i][2]}
  let key=canon(a,b).join();if(!bank.has(key))bank.set(key,[a,b,p,q]);
 }
 for(let [a,b,p,q] of bank.values()){if(count(a)>31||count(b)>31){direct++;continue}if(!can(a,5)||!can(b,5)){excluded++;continue}survivors.push({p:String(p),q:String(q),a:a.toString(16),b:b.toString(16)});}
 return {I,J,events:E.length,samples:samples.length,bank:bank.size,direct,excluded,survivors,checks:checks-before};
}
let out=[],cut=null;
for(let t of [1,2])for(let I of pairs(ids[0]))for(let J of pairs(ids[t])){if(cut)break;try{out.push(scan(directions[0],directions[t],I,J))}catch(e){if(e!==CUT)throw e;cut={I,J,t}}}
return {ids,out,cut,checks};
```

## Next
Extend this full-jet one-parameter scan to remaining pairs of multi-endpoint pencils, particularly t=0 paired with B=17t, B=0 and 2B=5t; retain the explicit four-anchor family partition. The general c=1 root is still open, including fewer than two doubled pencils and the strict-word extension of R259. K6 remains 1–2. Do not recompute the 78 families except for specific independent verification. 
