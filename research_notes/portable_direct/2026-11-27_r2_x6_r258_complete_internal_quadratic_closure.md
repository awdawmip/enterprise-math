# X6 R258 — exact affine-line sweep closes all remaining internal quadratics

2026-11-27. Author proof and exact BigInt computation; NOT_REVIEWED. Independent informed TASK_RESEARCH. Native read r2-20261127-0711-x6-read SUCCEEDED, observed 2026-11-26T23:12:08.300449Z, Source e59d205c8495d5e5cacd7a4a385ccde9894f6b83, NO_CANONICAL_PUBLICATION_DIRECTORY (directory absence only). Native live owner projection and own researcher binding unconfirmed. No CLAIM, Result, Review or shared state change. P000 V5, ACTIVE worldview, joint relation/residual fidelity retained. This is auxiliary weight coefficient arithmetic, not a native spatial geometry.

## 1. Inputs and inherited scope

Frozen executable R247 7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md. Same Port 10, 1935 integer directions, weights (17t,B,22t,D), six-pair joint BRC, strict 3/2, 47 necessary support labels, 49 components, 51 endpoints, 98 directed germs, 2225 linear masks. Use inherited necessary-wall theorem, complete linear suffix mask bank and capacity relaxation G, R250 full internal location and product closure, R253 >=3 mixed endpoints for all 34 possible internal nonsingular targets. R254-R257 of this turn have closed all 28 c=29,30 targets and excluded >=4 mixed endpoints for all 34. Only six c=27,28 targets with exactly three mixed endpoints remain. See fixed sources:
- R254 f1fccb394d012ac8039977842bb5cb339805f264:research_notes/portable_direct/2026-11-27_r2_x6_r254_three_polar_incidence_four_null_descent.md.
- R255 8cf5d54bd2d3fdfaf8796d0251b54971fc5ea0f9:research_notes/portable_direct/2026-11-27_r2_x6_r255_four_anchor_event_sweep.md.
- R256 4e3000bbdd07c087351f7e00f4aed1fb8d41b71e:research_notes/portable_direct/2026-11-27_r2_x6_r256_all_internal_four_mixed_exclusion.md.
- R257 8a5a88d731d990b4b3805353359a09758c886fd2:research_notes/portable_direct/2026-11-27_r2_x6_r257_c29_internal_closure.md.

## 2. Exact two-parameter kernel search by affine-line sweeps

For three distinct noncollinear mixed endpoints p,r,s the nonsingular conic must have Q(p)=Q(r)=Q(s)=0. Cramer's integer coordinates C(x)=(det[x,r,s],det[p,x,s],det[p,r,x]) are a common scalar times its basis coordinates. Every candidate up to branch exchange is F=alpha uv+beta vw+gamma wu with alpha beta gamma!=0 and alpha>0; set alpha=1. Thus the complete nonsingular family is covered by the affine two-parameter chart (beta,gamma) with both nonzero. There is no missing alpha=0 nonsingular point.

For each target germ use three homogeneous linear jet rows on (alpha,beta,gamma); as in R255 constant and quadratic jet entries may be multiplied by 2, and each by a positive gcd reciprocal, without changing lexicographic sign. Define the primary row as the first not identically zero row in the full three-anchor kernel. A row parallel to (1,0,0) has constant nonzero sign in this chart; every other primary row determines one affine event line. Group proportional rows using canonical primitive h with sign-positive leading entry, preserving their two oriented bit sets P_h,N_h. Add beta=0 and gamma=0 as artificial event lines even if their groups carry no germ bits.

Fix an event line h=(a,b,c), with either b or c nonzero. With pivot j in {1,2} and k the other index, choose q0=(m,0,0) with q0[j]=-sign(h[j])*a and q1=(0,0,0) with q1[j]=-sign(h[j])*h[k], q1[k]=m, m=|h[j]|. Then q(lambda)=q0+lambda*q1 has alpha=m>0 and ranges over the entire event line in the affine chart after dividing by m. Restrict all three jet rows to q(lambda), and use the exact R255 first-active event sweep. Each germ has at most one isolated event in this line, higher jets determine its exact sign at that event. Retain an explicit zero set Z for jets identically zero along the whole line. These can occur only in the primary group of that line; at any nonsingular coefficient no germ has all jets zero. Include both rank-zero coordinate events (or mark the entire line singular if one coordinate is identically zero). Test the true line masks on every nonsingular open interval and every nonsingular isolated event. The two forbidden coordinate lines are not themselves candidate conics.

Additionally, on every open line interval all other primary rows are nonzero (any intersection is included as a restricted first-row event, since the primary rows not proportional to h do not vanish identically on it). The adjacent open chamber on one side has the same mask away from the group and positive group bits P_h; the chamber on the other side has positive group bits N_h. Evaluate both, replacing all group bits, including any identically-zero residues on the line. Sufficiently small perturbations of a generic point realize these two chamber masks with alpha>0, beta gamma!=0 (the two coordinate lines were included). Every chamber of the finite nonempty affine arrangement has an open boundary segment or ray along some event line: from an interior point a generic transverse direction toward a line first exits across an open line segment, avoiding the finite intersection points. Hence the two incident chamber evaluations cover every open chamber. Every point outside open chambers lies on a line, whose exact event sweep covers its higher-jet sign. This proves exhaustive coverage of all nonsingular forms without a full two-dimensional sign grid or arbitrary independent sign choices. It also supplies a reusable rank-three kernel algorithm: at most O(N^2) line-parameter events, O(N^2 log N) rational comparisons across all lines, and O(N^2) jet restrictions/bit updates, excluding bit-length costs and downstream capacity checks. This is an arithmetic-count bound, not a full bit-complexity bound.

For each complete strict mask require exactly the selected three mixed endpoints, all other endpoints monochromatic. Then both branch label counts must be <=15, and G(X,4) AND G(Y,4) must hold. The visited set deduplicates the entire target partition up to simultaneous exchange (same partition has a unique mixed triple). All label identities and germ orientations retained, no residual deletion.

## 3. Executed all six remaining targets

Common prefix 3,275,335, total 3,380,819 exact G checks, incremental 105,484. Zero cutoff, zero survivors. Columns: target hex, candidate triples, collinear discarded, line sweeps, line intervals, nonsingular event points tested, mask visits (includes adjacent chambers and nonsingular line intervals/points), visits with exactly chosen three mixed endpoints, unique complete mixed partitions, direct-capacity passing distinct partitions, incremental G checks.
```
3cc35cfff0003f3dff0000fcf 455 11 13911 413406 357717 1578259 517114 75005 160 76310
33cf3202fffc0c300ffffe30 364 12 11610 366647 319566 1402757 385548 53597 34 5954
2cb3010fffe7d304fffc030 220 6 6152 166002 142280 632010 253726 36165 35 12629
2cb3010fffefd304fffc030 220 6 6318 174833 150406 666422 271170 38518 20 329
2cb3010fffefd30cfffc030 220 6 6532 187556 162121 715940 299164 42274 18 188
32cb3010fffe7c304fffc030 220 6 6538 189664 163896 723766 259957 36518 27 10074
TOTAL 1699 47 51061 1498108 1295986 5719154 1986679 282077 294 105484
```
All direct-capacity passing partitions were rejected by G. Thus ALL 34 potential internal target sets are fully excluded for a sole full-rank quadratic (R253-R258 combined). The inherited R250 product/semidefinite/location results now imply: in the stated frozen Port-10 problem, conditional on the inherited necessary-wall and complete linear suffix capacity theorems, any correct depth-six decision tree with exactly one quadratic observation must place it at the ROOT, and it must be nonsingular indefinite. The general root case is still open, so the unrestricted minimal joint observation count K6 remains 1–2. No claim that root case is solved, or of independent acceptance of the inherited chain.

## 4. Reproduction

Fetch first JavaScript block from frozen R247 as src. Execute:
```javascript
const patch=`ceiling=100000000;let roots=[];
for(let [a,b] of ordered){let ca=can(a,5),cb=can(b,5);if(ca&&cb)throw Error("linear");if(ca===cb)continue;let t=ca?b:a;if(count(t)<=30)roots.push(t)}
let initialChecks=checks,result=[];
for(let t of roots.filter(t=>count(t)<29)){
 let L=tag.map(v=>v&t).filter(Boolean),E=P.map((_,i)=>({i,bits:G.filter(([u,v,b])=>u===i&&(b&t)).reduce((a,[u,v,b])=>a|b,0n)})).filter(x=>x.bits),M=E.filter(x=>(x.bits&(x.bits-1n))!==0n),TG=G.filter(g=>g[2]&t);
 let visited=new Set(),survivors=[],triples=0,collinear=0,lines=0,intervals=0,points=0,visits=0,mixed=0,direct=0,before=checks;
 const form=(x,y)=>[x[0]*y[1]+x[1]*y[0],x[1]*y[2]+x[2]*y[1],x[2]*y[0]+x[0]*y[2]];
 for(let a=0;a<M.length;a++)for(let b=a+1;b<M.length;b++)for(let c=b+1;c<M.length;c++){
  let ids=[M[a],M[b],M[c]], [p,r,s]=ids.map(o=>P[o.i]),D=dot(p,cross(r,s));triples++;if(!D){collinear++;continue}
  let adj=[cross(r,s),cross(s,p),cross(p,r)],C=P.map(q=>adj.map(h=>dot(h,q))),J=TG.map(([i,j,bit])=>{let p=C[i],q=sub(C[j],p);return {bit,rows:[form(p,p),form(p,q),form(q,q)].map(x=>norm(x))}});
  let H=new Map();function group(row,bit){if(!row[1]&&!row[2])return;let h=norm(row,true),key=h.join();if(!H.has(key))H.set(key,{h,pos:0n,neg:0n});let v=H.get(key);if(row.find(Boolean)>0n)v.pos|=bit;else v.neg|=bit}
  group([0n,1n,0n],0n);group([0n,0n,1n],0n);
  for(let {bit,rows} of J){let h=rows.find(nz);if(!h)throw Error("all jets");group(h,bit)}
  let others=M.filter(o=>!ids.includes(o));
  function test(X){visits++;let Y=t^X;for(let {bits} of ids)if(!(X&bits)||!(Y&bits))return;
   for(let {bits} of others)if((X&bits)&&(Y&bits))return;mixed++;
   let [A,B]=canon(X,Y);if(visited.has(A))return;visited.add(A);
   if(count(A)>15||count(B)>15)return;direct++;
   if(can(A,4)&&can(B,4))survivors.push([A.toString(16),B.toString(16),ids.map(x=>x.i)])
  }
  for(let {h,pos,neg} of H.values()){
   lines++;let j=h[1]?1:2,k=3-j,m=abs(h[j]),s=BigInt(sg(h[j])),q0=[m,0n,0n],q1=[0n,0n,0n];
   q0[j]=-s*h[0];q1[j]=-s*h[k];q1[k]=m;
   let ev=new Map(),X=0n,Z=0n,groupBits=pos|neg,regular=true;
   function event(n,d){let z=gcd(n,d);n/=z;d/=z;if(d<0n){n=-n;d=-d}let key=n+"/"+d;if(!ev.has(key))ev.set(key,{n,d,changes:0n,tiePos:0n,tieZero:0n,forbid:false});return ev.get(key)}
   for(let i=1;i<3;i++){if(!q1[i]){if(!q0[i])regular=false}else event(-q0[i],q1[i]).forbid=true}
   for(let {bit,rows} of J){
    let R=rows.map(h=>[dot(h,q0),dot(h,q1)]),row=R.find(nz);if(!row){Z|=bit;continue}
    let [a,b]=row;if(!b){if(a>0n)X|=bit;continue}
    if(b<0n)X|=bit;let e=event(-a,b);e.changes|=bit;let z=0;for(let [a,b] of R){z=sg(a*e.d+b*e.n);if(z)break}
    if(z>0)e.tiePos|=bit;else if(!z)e.tieZero|=bit;
   }
   if(Z&~groupBits)throw Error("unrelated identically zero germ");
   function interval(){intervals++;if(regular){if(Z)throw Error("zero germ full rank");test(X)}
    // On the open line interval all other primary rows are nonzero.
    test((X&~groupBits)|pos);test((X&~groupBits)|neg);
   }
   interval();
   for(let e of [...ev.values()].sort((a,b)=>sg(a.n*b.d-b.n*a.d))){
    if(regular&&!e.forbid){points++;if(Z||e.tieZero)throw Error("zero germ full rank point");test((X&~e.changes)|e.tiePos)}
    X^=e.changes;interval()
   }
  }
 }
 result.push({t:t.toString(16),triples,collinear,lines,intervals,points,visits,mixed,uniqueMixed:visited.size,direct,survivors,checks:checks-before})
}
return {initialChecks,checks,result};`;
const old='return {points:P.length,germs:G.length,linearPartitions:Q.length,result:rank4("two_anchor_kernel",[])};';
if(!src.includes(old))throw Error("pin mismatch");
console.log(Function(src.replace(old,patch).replace(/experiment\(data\)\s*$/,"return experiment(data)"))());
```

## 5. Next root problem and reusable insight

The internal case is finished at author proof/calculation level. Do not repeat. For root T=ALL and suffix depth five, the branch capacities are 31 labels each, so split budget becomes 62-47=15. This is larger than the internal budgets 0..3; the same incidence relaxation may not prune enough without stronger constraints. Reuse exact coupled local banks, four-anchor sweeps and affine-line sweep only after deriving a valid root mixed-anchor condition or identifying root masks. Candidate avenue: exploit necessary label capacity conflicts and positive dependence certificates on oriented first-active coefficient rows, including exact residual on boundaries; investigate whether minimum mixed-anchor counts can be proved by combining constraints rather than enumerating all split-label subsets. The root remains the only unresolved location. Activity association and independent mathematical review pending.
