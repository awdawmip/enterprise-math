# X6 R254 — coupled three-polar local masks and four-null descent for all c=30 internal targets

2026-11-27. Author proof and exact BigInt computation, NOT_REVIEWED. Independent informed TASK_RESEARCH. Current native read r2-20261127-0711-x6-read SUCCEEDED, observed 2026-11-26T23:12:08.300449Z, Source e59d205c8495d5e5cacd7a4a385ccde9894f6b83, NO_CANONICAL_PUBLICATION_DIRECTORY (directory observation only, native owner projection not evaluated). Own researcher binding unconfirmed; no CLAIM, Result, Review or shared task-state mutation.

Frozen scientific inputs: R253 8d608e9c00ddc782f9b6276d8a2aecf4e5bf6464:research_notes/portable_direct/2026-11-27_r2_x6_r253_all_internal_targets_three_mixed.md; R252 9aa4711f9113ed8edb5f607adb6fe99d86c82f54; executable R247 7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md. Port 10, 1935 integer directions, weights (17t,B,22t,D), six-pair joint BRC, strict 3/2, 47 necessary support labels, 49 components, 51 endpoints, 98 directed germs, 2225 linear masks unchanged. Inherit R250 necessary-wall/complete linear suffix bank and capacity relaxation, R251 label split budget, R253 at least three mixed endpoints for all 34 targets, and nonsingular reduction from earlier product closure. Auxiliary coefficient arithmetic, not a native spatial model. P000 V5, ACTIVE worldview, joint relation and residual preservation retained.

## 1. Coupled local bank for three actual mixed null anchors

Let p,r,s be distinct actual mixed endpoints. Nonsingularity forbids three collinear zeros. In basis (p,r,s), Q=2(alpha uv+beta vw+gamma wu); full rank iff alpha beta gamma!=0. For a germ from one of these anchors toward q with coordinates (u,v,w), the first derivative signs are respectively sign(alpha v+gamma w), sign(alpha u+beta w), sign(beta v+gamma u). For a tied derivative the exact second sign is -sign(alpha beta gamma), by R253 (all nonradial tangent directions). Thus local masks at all three endpoints are coupled by a single coefficient vector, not three independently selected gradient signs or tangent signs.

Compute (u,v,w) by Cramer's rule with common positive denominator |det[p,r,s]|: the integer numerators are dot products with sign(det) times (r cross s,s cross p,p cross r). Divide each local linear row by positive gcd only, so branch signs are preserved. Add the three coordinate event normals to the set of local first-derivative rows: their signs determine full rank and the exact tangent residual. The resulting central arrangement in auxiliary R^3 is essential. Every nonzero ray/edge/chamber sign pattern is represented by the flags v; (v,±(v cross h)); (v,±(v cross h),±h), where v is the cross product of two independent event normals and h is a normal incident to that ray. Indeed each chamber closure is a full-dimensional pointed polyhedral cone with a ray and an incident facet; in the quotient transverse to that ray the sectors are bounded by the incident lines. Faces follow from the same argument in their spans. A sufficiently small positive infinitesimal parameter realizes each finite lexicographic flag. Canonicalizing a ray direction is valid up to simultaneous coefficient reversal because both adjacent directions are enumerated; normalize alpha>0, reversing the entire local sign mask if needed. Exclude coordinate-zero flags and require both local signs at each of the three anchors. For tied first derivatives insert the uniform exact second sign, so no zero germs or omitted tangent distinctions. This gives the complete coupled local bank, with original germ identities.

## 2. Exactly-three-mixed relaxed incidence test, c(T)=30

R251 implies that no label can split, since both suffix branches must contain at most 15 labels and nonsingular Q has no zero germs. For a proposed triple of actual mixed endpoints, join all target germs of each label and join all germs at each endpoint outside that triple. Connected components must be monochromatic. Prescribe the signs of the three local banks from section 1; reject contradictions, enumerate both assignments on every free component and prune only when a branch exceeds 15 distinct labels. At the end use inherited G(X,4) AND G(Y,4), deduplicating complete target partitions only up to simultaneous exchange. Every true Q with exactly three mixed endpoints is covered: its actual triple is noncollinear, its coupled local mask is in the bank and its complete partition respects every equality. The search permits arbitrary signs on unprescribed components, so exclusion of all relaxed masks is sufficient. No claim of sufficiency of the capacity relaxation.

## 3. Executed exact search

The 14 c=30 targets were run together, no cut or unknown; common prefix 3,275,335 checks, total 4,448,691 checks. Every row has zero survivors. Columns: target hex, triples, collinear excluded, distinct oriented coupled patterns (sum over triples), component conflicts, assignment branch visits, distinct direct-capacity passing partitions, incremental capacity checks.
```
33cb3010fffe7d304ffff030 286 9 2728 1955 1169 82 4444
32cb3010fffe7d304fffe030 220 6 2316 1675 1507 164 6949
2cb3018fffefdb0cfffc030 286 6 3287 2401 1008 35 1192
3cd3fffef0003a3dfb8001fcf 680 14 6422 5649 7015 842 41100
3fdf4cfef004183cfb0033fcf 364 6 3813 2638 103173 14699 738499
24f3018fffeffb0cfffc030 364 8 3741 3060 779 28 1521
2cf3018fffeffb0cfffc030 364 8 3741 3060 779 28 940
3fdffcfef004183dfb0003fcf 560 7 5219 4600 25063 3443 121681
3cd35dfff0003f3dffc001fcf 680 16 6616 5937 1621 180 8225
3cd3fffff0003f3dffc001fcf 816 16 7838 7490 650 54 1128
3fd3fffef0003a3dfb0003fcf 560 10 5483 4847 12426 1629 63981
33cb3012fffc5c304ffffa30 286 9 2457 1775 1162 105 5677
3fdffcfef004383dfb0003fcf 560 7 5219 4600 25063 3443 77202
3fdffcfef0003a3dfb0003fcf 560 10 5084 4516 24518 3389 100817
TOTAL 6586 132 63964 54203 205933 28121 1173356
```
Consequently all 14 c=30 targets require at least FOUR mixed endpoints under inherited premises. The remaining 20 targets (c=27,28,29) still require at least THREE from R253; exactly-three search has not been executed on them.

## 4. Four-null descent

For a fourth distinct null endpoint k, none of its three coordinates u0,v0,w0 in the basis (p,r,s) can vanish: otherwise three distinct null points would be collinear. Its zero condition is alpha u0 v0+beta v0 w0+gamma w0 u0=0, an independent constraint on the three polar coefficients. Set A'=alpha u0 v0, B'=beta v0 w0, C'=gamma w0 u0. The full kernel is A'+B'+C'=0, each coordinate nonzero. Thus each candidate four-anchor subset determines a rank-two linear coefficient space (one projective parameter), with three forbidden rank-deficient points. With A'=1 by simultaneous nonzero scaling, B'=lambda, C'=-1-lambda, lambda!=0,-1. All directed germ jet coefficients become affine in lambda. The R243 first-active event lemma applies with one possible isolated root per germ (including tangent ties) and the two rank-deficient points; each open interval and isolated event can be handled exactly. This gives at most 2(N+2)+1 parameter cells on the real axis for N target germs, before excluding forbidden points and using symmetry/deduplication. A zero higher jet cannot be treated as a new sign event unless the preceding active coefficient vanishes; no loss of residuals. This covers ALL Q with at least four mixed endpoints by a finite union of four-anchor choices (not just exactly four). The rank-two search has not yet been executed. It is a direct route to complete closure of the 14 high-label targets without enumerating higher mixed sets separately.

## 5. Reproduction

Fetch the first JavaScript block from frozen R247 as src. Replace its final return with the following exact patch and replace terminal experiment(data) with return experiment(data). Run with JavaScript BigInt. The executed check ceiling was 100,000,000, not reached; a cutoff would throw rather than return a completed result.
```javascript
const patch=`ceiling=100000000;let roots=[];
for(let [a,b] of ordered){let ca=can(a,5),cb=can(b,5);if(ca&&cb)throw Error("linear");if(ca===cb)continue;let t=ca?b:a;if(count(t)<=30)roots.push(t)}
let initialChecks=checks,result=[];
const axes=[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]];
function local3(ids,t){
 let [p,r,s]=ids.map(i=>P[i]),D=dot(p,cross(r,s));if(!D)return null;
 let adj=[cross(r,s),cross(s,p),cross(p,r)].map(x=>scale(x,BigInt(sg(D))));
 let loc=G.filter(([u,v,b])=>ids.includes(u)&&(b&t)).map(([u,v,b])=>{
  let [x,y,z]=adj.map(a=>dot(a,P[v])),j=ids.indexOf(u);
  let h=j===0?[y,0n,z]:j===1?[x,z,0n]:[0n,y,x];
  if(!nz(h))throw Error("local parallel");return {j,b,h:norm(h)};
 });
 let prim=uniqueRays([...axes,...loc.map(x=>x.h)]),raw=[];
 for(let i=0;i<prim.length;i++)for(let j=i+1;j<prim.length;j++)raw.push(cross(prim[i],prim[j]));
 let out=new Map();
 function add(vs){
  let sign=h=>{for(let v of vs){let z=sg(dot(h,v));if(z)return z}return 0};
  let [a,b,c]=axes.map(sign);if(!a||!b||!c)return;
  let tangent=-a*b*c,X=0n,Y=0n,A=[0,0,0],B=[0,0,0];
  for(let {j,b,h} of loc){let z=(sign(h)||tangent)*a;if(z>0){X|=b;A[j]++}else{Y|=b;B[j]++}}
  if(A.some(x=>!x)||B.some(x=>!x))return;
  out.set(X+","+Y,[X,Y]);
 }
 for(let v of uniqueRays(raw)){add([v]);for(let h of prim)if(!dot(v,h)){let w=cross(v,h);for(let f of [-1n,1n]){let u=scale(w,f);add([v,u]);for(let g of [-1n,1n])add([v,u,scale(h,g)])}}}
 return [...out.values()];
}
for(let t of roots.filter(t=>count(t)===30)){
 let L=tag.map(v=>v&t).filter(Boolean),E=P.map((_,i)=>({i,bits:G.filter(([u,v,b])=>u===i&&(b&t)).map(([u,v,b])=>b)})).filter(x=>x.bits.length),M=E.filter(x=>x.bits.length>1);
 let visited=new Set(),survivors=[],triples=0,collinear=0,patterns=0,conflicts=0,branches=0,direct=0,before=checks;
 for(let k=0;k<M.length;k++)for(let l=k+1;l<M.length;l++)for(let m=l+1;m<M.length;m++){
  let ids=[M[k].i,M[l].i,M[m].i];triples++;let pats=local3(ids,t);if(pats===null){collinear++;continue}patterns+=pats.length;if(!pats.length)continue;
  let comps=E.flatMap(({i,bits})=>ids.includes(i)?bits:[bits.reduce((a,b)=>a|b,0n)]);
  for(let v of L){let x=v,rest=[];for(let y of comps){if(x&y)x|=y;else rest.push(y)}rest.push(x);comps=rest}
  comps.sort((a,b)=>count(b)-count(a));
  for(let [pa,pb] of pats){let a=0n,b=0n,free=[],bad=false;
   for(let x of comps){if((x&pa)&&(x&pb)){bad=true;break}if(x&pa)a|=x;else if(x&pb)b|=x;else free.push(x)}
   if(bad){conflicts++;continue}
   function rec(k,a,b){branches++;if(count(a)>15||count(b)>15)return;
    if(k===free.length){let [x,y]=canon(a,b);if(visited.has(x))return;visited.add(x);direct++;if(can(x,4)&&can(y,4))survivors.push([x.toString(16),y.toString(16),ids]);return}
    rec(k+1,a|free[k],b);rec(k+1,a,b|free[k])
   }rec(0,a,b)
  }
 }
 result.push({t:t.toString(16),triples,collinear,patterns,conflicts,branches,direct,survivors,checks:checks-before})
}
return {initialChecks,checks,result};`;
const old='return {points:P.length,germs:G.length,linearPartitions:Q.length,result:rank4("two_anchor_kernel",[])};';
if(!src.includes(old))throw Error("pin mismatch");
console.log(Function(src.replace(old,patch).replace(/experiment\(data\)\s*$/,"return experiment(data)"))());
```

Next: enumerate all four-anchor rank-two kernels for c=30, using capacity on actual complete masks and requiring selected anchors really mixed; also extend exactly-three coupled graph search to c=29,28,27 by allowing 30-c(T) split labels as in R252. Root case remains open. K6=1–2. No independent review or Activity association yet.
