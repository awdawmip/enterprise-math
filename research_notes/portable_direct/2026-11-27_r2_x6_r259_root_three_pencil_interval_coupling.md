# X6 R259 — root three-pencil interval coupling and exact partial-mask pruning

2026-11-27. Independent informed TASK_RESEARCH, author derivation and exact BigInt calculation, NOT_REVIEWED. Native task read r2-20261127-0806-x6-read SUCCEEDED at 2026-11-27T00:06:49.510247Z, Source 60122a1647c3012f8143b89e0c416dcf5b60dbe1, NO_CANONICAL_PUBLICATION_DIRECTORY. Directory observation only: active owner and own research identity not established. No CLAIM, Result, Review or shared control mutation. Activity association pending. Current P000 V5, ACTIVE worldview and joint relation/residual preservation retained. All coordinates below are auxiliary weight coordinates, not native spatial axes.

## Frozen question
R258 b0960b0e767177f2b6bb7437275bf19aa662f7f0:research_notes/portable_direct/2026-11-27_r2_x6_r258_complete_internal_quadratic_closure.md reports all internal locations closed at author proof/calculation level. Reuse, do not recompute. The root full-rank indefinite case remains. Frozen executable: R247 7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md. Port 10, weights (17t,B,22t,D), 1935 directions, six-pair joint BRC, strict 3/2, 47 labels, 49 components, 51 endpoints, 98 directed germs, 2225 linear masks. All capacity exclusions inherit necessary-wall and linear suffix completeness premises. The current unit addresses only forms nonzero at all 26 endpoints on the three projective lines below; forms zero elsewhere are allowed. No claim of global root closure.

## Exact three-pencil theorem
Let Q=a t^2+b B^2+c D^2+d tB+e tD+f BD. On the three concurrent auxiliary projective lines t=0, B=kt, B=0 with k>0, their common endpoint is p24=(0,0,1). Assume Q(p24)=c!=0 and all specified finite endpoint values on these lines nonzero. Divide Q by c, exchanging global branch signs if needed. On each line write q(y)=y^2+L y+K, where y=D/B on t=0 and y=D/t on the others. Then L_infty=f/c, L_0=e/c, L_k=L_0+k L_infty; K_infty=b/c, K_0=a/c, K_k=(a+k d+k^2 b)/c. The constants K are independently adjustable because k!=0. For prescribed finite positive ordinates i and negative ordinates j (sign relative to c), the allowable L are exactly the open interval I given by all inequalities (y_i-y_j)(y_i+y_j+L)>0. Proof: the positive samples require K> -y_i^2-L y_i and the negative samples require K< -y_j^2-L y_j. These strict constraints have common K iff each lower bound is below every upper bound, precisely the stated inequalities. Empty sign classes give no pair restriction. Thus I=(max_{y_i>y_j}(-y_i-y_j), min_{y_i<y_j}(-y_i-y_j)), with missing bounds infinite. All three strict sample-sign words are simultaneously realizable by a real quadratic iff all three intervals are nonempty and I_k intersects I_0+k I_infty. Necessity is the slope identity; sufficiency is selection of slopes in the intervals, then independent constants as above, reconstructing all coefficients. With strict sample signs the feasible region in c=1 chart is open; nonsingular forms occur in any nonempty such region, since determinant polynomial is not identically zero there (e.g. identity matrix). If signs include both signs then those nonsingular forms are indefinite. This theorem is exact for these point signs, not for all remaining germs or entire decision-tree correctness.

On each line the ordered strict signs have at most two variations, since the normalized binary quadratic has at most two real zeros between consecutive points. Ordering D/(t+B) puts infinity last. The common point must have the same sign on all three lines. No local germ can disagree with a nonzero starting endpoint by continuity. Therefore assign all directed germs of selected endpoints to their point sign, without deleting any unassigned germ or label. Partial positive/negative masks are subsets of complete masks; monotonicity of G gives an exclusion whenever count exceeds 31 or G(mask,5) fails on either side. Additional sign words may be rejected by the exact interval theorem before exploring any remaining endpoints. This uses joint coupling of the three slopes, not three independent sign banks.

## Exact frozen run
Three lines t=0, B=17t, B=0 cover 26 distinct endpoints and 47 of 98 directed germs. Normalize branch exchange by p18 positive; p24 may be either sign. First two lines yield 506 compatible capacity-passing assignments. Third line yields 39,974 compatible combined words, 1,877 direct capacity failures and 6,034 recursive failures. Of the 32,063 remaining, 10,805 violate the shared-slope theorem, leaving 21,258 partial words. No cutoff in the final run. A prior pilot at 8,000,000 checks was incomplete; its counts are superseded, not added. Exact BigInt comparisons and existing pure linear suffix bank. Final output (rerun of the exact code below):
```json
{"hist":[{"ids":[18,2,0,36,24],"patterns":22,"input":1,"visit":22,"compatible":11,"direct":0,"recursive":0,"algebra":0,"surv":11,"checks":204},{"ids":[26,19,34,20,25,28,39,1,37,24],"patterns":92,"input":11,"visit":1012,"compatible":506,"direct":0,"recursive":0,"algebra":0,"surv":506,"checks":102729},{"ids":[10,15,11,45,49,9,38,42,40,44,47,50,24],"patterns":158,"input":506,"visit":79948,"compatible":39974,"direct":1877,"recursive":6034,"algebra":10805,"surv":21258,"checks":14679057}],"checks":14781990,"lineHist":{"mix,-,-":4,"mix,-,mix":312,"mix,mix,-":180,"mix,mix,mix":18541,"mix,mix,+":113,"mix,+,mix":177,"+,mix,mix":1913,"+,mix,+":10,"+,+,mix":8},"capacityRange":[12,31,4,27]}
```
Counts are partial endpoint words, not full root sign masks or excluded disjoint coefficient cells beyond the stated restrictions. Remaining words need extension to 51 endpoints/98 germs, including zeros outside selected lines and high-order residuals. Among retained words all three lines cannot be simultaneously monochromatic. 22 words have exactly one mixed line (4+10+8), a mixed line here means differing signs at its sampled points, not a mixed endpoint. This supplies a compact root incidence constraint but not a forced mixed endpoint.

## Reproduction
Read the first JavaScript block of the pinned R247 file as src, replace its final return statement inside experiment with the following patch, and replace final experiment(data) with return experiment(data), then execute Function(src)(). The complete pinned input and G are unchanged. The final run returned the output above. No code writes or native-world dynamics claimed.
```javascript
ceiling=25000000;
let normals=[[1n,0n,0n],[17n,-1n,0n],[0n,1n,0n]];
let E=P.map((p,i)=>G.filter(g=>g[0]===i).reduce((a,g)=>a|g[2],0n));
let cmp=(x,y)=>sg(x[0]*y[1]-y[0]*x[1]),add=(x,y)=>[x[0]*y[1]+y[0]*x[1],x[1]*y[1]],mul=(x,k)=>[x[0]*k,x[1]];
let groups=normals.map((h,k)=>P.map((p,i)=>i).filter(i=>!dot(h,P[i])).sort((i,j)=>sg(P[i][2]*(P[j][0]+P[j][1])-P[j][2]*(P[i][0]+P[i][1]))));
function bound(ids,k,a,b){
 let pos=(a&E[24])?a:b,neg=(a&E[24])?b:a,lo=null,hi=null;
 let finite=ids.filter(i=>i!==24),y=i=>[P[i][2],P[i][k===0?1:0]];
 for(let i of finite)if(pos&E[i])for(let j of finite)if(neg&E[j]){
  let u=y(i),v=y(j),z=mul(add(u,v),-1n),c=cmp(u,v);
  if(c>0&&(!lo||cmp(lo,z)<0))lo=z;
  if(c<0&&(!hi||cmp(hi,z)>0))hi=z;
 }
 return [lo,hi];
}
function good(a,b){
 let [p,r,s]=groups.map((ids,k)=>bound(ids,k,a,b));
 if([p,r,s].some(([l,u])=>l&&u&&cmp(l,u)>=0))return false;
 let lo=p[0]&&s[0]?add(mul(p[0],17n),s[0]):null,hi=p[1]&&s[1]?add(mul(p[1],17n),s[1]):null;
 return !(lo&&r[1]&&cmp(lo,r[1])>=0||hi&&r[0]&&cmp(hi,r[0])<=0);
}
let states=[[E[18],0n]],hist=[];
for(let k=0;k<groups.length;k++){
 let ids=groups[k],patterns=[],n=ids.length,union=ids.reduce((a,i)=>a|E[i],0n);
 for(let m=0;m<2**n;m++){let changes=0;for(let i=1;i<n;i++)if(((m>>i)^(m>>(i-1)))&1)changes++;if(changes>2)continue;let a=ids.reduce((s,id,i)=>s|((m>>i)&1?E[id]:0n),0n);patterns.push([a,union^a])}
 let out=[],visit=0,compatible=0,direct=0,recursive=0,algebra=0,both=0,before=checks;
 for(let [a,b] of states)for(let [p,q] of patterns){visit++;if((a&q)||(b&p))continue;compatible++;let A=a|p,B=b|q;
 if(count(A)>31||count(B)>31){direct++;continue}
 if(!can(A,5)||!can(B,5)){recursive++;continue}
 if(k===2&&!good(A,B)){algebra++;continue}
 out.push([A,B]);}
 hist.push({ids,patterns:patterns.length,input:states.length,visit,compatible,direct,recursive,algebra,surv:out.length,checks:checks-before});states=out;
}
let lineHist={},cntHist={};for(let [a,b] of states){let signs=groups.map(ids=>ids.every(i=>E[i]&a)?"+":ids.every(i=>E[i]&b)?"-":"mix").join(",");lineHist[signs]=(lineHist[signs]||0)+1;let k=count(a)+","+count(b);cntHist[k]=(cntHist[k]||0)+1;}
return {hist,checks,lineHist,capacityRange:[Math.min(...states.map(([a,b])=>count(a))),Math.max(...states.map(([a,b])=>count(a))),Math.min(...states.map(([a,b])=>count(b))),Math.max(...states.map(([a,b])=>count(b)))]};
```

## Next
Use the surviving words as a necessary filter for root search; extend the exact slope interval coupling to additional lines B=kt. Their constant terms also obey one quadratic polynomial in k, so independent interval feasibility on more than three lines is only a relaxation unless the shared intercept constraints are imposed. Retain strict/weak endpoint conditions and lexicographic germ residuals for exceptional zero strata; c=0 and zero points on the three lines are separate outstanding cases. Consider sparse linear-inequality certificates on the surviving words and capacity conflict caching. K6 remains 1–2. No independent review or formal Task completion.
