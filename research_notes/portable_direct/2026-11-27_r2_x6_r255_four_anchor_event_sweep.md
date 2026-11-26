# X6 R255 — full four-anchor rational event sweep closes all fourteen c=30 internal targets

2026-11-27. Author proof/exact BigInt calculation, NOT_REVIEWED. Same informed TASK_RESEARCH, frozen inputs and inherited necessary-wall/full linear suffix capacity premises as R254 at f1fccb394d012ac8039977842bb5cb339805f264:research_notes/portable_direct/2026-11-27_r2_x6_r254_three_polar_incidence_four_null_descent.md (readback blob 403779f9d26475acd267a192fde56f9616558ce0). Native read r2-20261127-0711-x6-read, Source e59d205c8495d5e5cacd7a4a385ccde9894f6b83, NO_CANONICAL_PUBLICATION_DIRECTORY, no native owner projection evaluated, own identity unconfirmed. No CLAIM/shared state mutation. P000 V5 and joint relation/residual fidelity retained. This is auxiliary coefficient arithmetic.

## Complete rank-two kernel and efficient sweep

R254 proved at least four mixed endpoints in all c=30 targets. For any four selected mixed endpoints p,r,s,k, discard if any triple collinear (a nonsingular conic cannot have three collinear null points). Put C(q)=(det[q,r,s],det[p,q,s],det[p,r,q]), proportional by common nonzero D=det[p,r,s] to the basis coordinates of q. If (u,v,w)=C(k), all three are nonzero. All nonsingular Q vanishing on the four anchors, modulo overall nonzero scalar, are given by
F_lambda(x,y,z)=w*x*y+u*lambda*y*z-v*(1+lambda)*z*x, lambda real, lambda!=0,-1.
Indeed the fourth condition alpha*u*v+beta*v*w+gamma*w*u=0 allows alpha=w after overall rescaling; beta=u*lambda and gamma=-v*(1+lambda), with u,v,w nonzero. Conversely those forms satisfy all four zero constraints and their three polar coefficients have nonzero product except at the two forbidden parameters. C scales all actual basis coordinates by the same D, so homogeneous quadratic signs are preserved, up to allowed global branch exchange. This covers the whole nonsingular four-anchor kernel, including forms with additional mixed endpoints. The missing projective point alpha=0 is singular and excluded by the inherited scope.

For every target germ use the exact affine coefficient pairs for its three jet entries (constant, linear in lambda). The code stores twice the constant and quadratic epsilon coefficients, and the actual cross coefficient for the middle entry; multiplying individual entries by positive factors preserves the first nonzero sign. Select the first not identically zero row (h,m). If m=0 its sign is constant; otherwise it changes only at lambda=-h/m. For lambda tending to -infinity its sign is -sign(m); store this bit in X as appropriate. Group equal events by reduced rational number with positive denominator. At an event, evaluate the entire jet of each affected germ exactly; for all unaffected bits keep their existing sign. Test the event mask unless the parameter is forbidden; then flip all affected bits to obtain the sign mask of the next open interval. An all-zero jet at a nonsingular parameter would contradict the line-factor theorem and is asserted absent. No floating arithmetic, sampling omission or epsilon truncation. Include the two forbidden points in the sorted sweep, testing the intervals on both sides. With N germs, there are at most N+2 distinct events and at most 2(N+2)+1 total parameter cells, fewer when forbidden points omitted. Sorting costs O(N log N) exact rational comparisons per kernel; building all jet/event rows and updating sign bit masks costs O(N) arithmetic operations plus rational gcd/bit costs, apart from branch capacity tests. This is an event sweep rather than evaluating all N germs afresh in every cell; no bit-complexity speedup claim beyond the explicit arithmetic operation count.

Filter each exact partition by requiring all four chosen anchors genuinely mixed, requiring all label germs monochromatic (c=30 split budget zero), and equal 15-label branch counts. Apply inherited G(A,4) AND G(B,4) to every distinct remaining mask up to global branch exchange, using original target bits. Because every nonsingular candidate must have four actual mixed endpoints, all successful Q in the c=30 range are covered. No dependence on finding exactly four mixed endpoints.

## Actual exact result

Common prefix 3,275,335 checks; total 3,275,476 checks, incremental 141; no cutoff, no survivors. Columns: target hex, four-anchor subsets, discarded collinear subsets, valid parameter cells, all four mixed cells, zero split-label cells, distinct direct-capacity passing partitions, incremental G checks.
```
33cb3010fffe7d304ffff030 715 84 39659 15077 22 0 0
32cb3010fffe7d304fffe030 495 51 27638 11612 54 0 0
2cb3018fffefdb0cfffc030 715 57 39684 19321 14 0 0
3cd3fffef0003a3dfb8001fcf 2380 187 140161 46951 39 1 47
3fdf4cfef004183cfb0033fcf 1001 63 68058 32242 67 0 0
24f3018fffeffb0cfffc030 1001 85 54412 22235 5 0 0
2cf3018fffeffb0cfffc030 1001 85 56244 22889 5 0 0
3fdffcfef004183dfb0003fcf 1820 88 122824 46775 94 0 0
3cd35dfff0003f3dffc001fcf 2380 215 137757 44983 23 0 0
3cd3fffff0003f3dffc001fcf 3060 231 187855 57349 23 0 0
3fd3fffef0003a3dfb0003fcf 1820 124 118512 41455 39 1 47
33cb3012fffc5c304ffffa30 715 84 39719 9709 3 0 0
3fdffcfef004383dfb0003fcf 1820 88 125820 47703 21 0 0
3fdffcfef0003a3dfb0003fcf 1820 124 121670 41856 33 1 47
TOTAL 20743 1566 1280013 460157 442 3 141
```
All three direct-capacity passing target partitions were rejected by G. Therefore all 14 targets with c=30 are completely excluded for a sole internal full-rank quadratic, assuming the inherited R250/R253/R254 premises. This is the first full closure of an entire target class in the internal nonsingular case. The remaining 20 targets have c=27,28,29 and require >=3 mixed endpoints; apply this sweep with their positive split budgets to all >=4 cases, and extend R254 for exactly three. General root case open; K6=1–2.

## Reproduction

Frozen R247: 7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md. Fetch first JavaScript block as src.
```javascript
const patch=`ceiling=100000000;let roots=[];
for(let [a,b] of ordered){let ca=can(a,5),cb=can(b,5);if(ca&&cb)throw Error("linear");if(ca===cb)continue;let t=ca?b:a;if(count(t)<=30)roots.push(t)}
let initialChecks=checks,result=[];
for(let t of roots.filter(t=>count(t)===30)){
 let L=tag.map(v=>v&t).filter(Boolean),E=P.map((_,i)=>({i,bits:G.filter(([u,v,b])=>u===i&&(b&t)).reduce((a,[u,v,b])=>a|b,0n)})).filter(x=>x.bits),M=E.filter(x=>(x.bits&(x.bits-1n))!==0n),TG=G.filter(g=>g[2]&t);
 let visited=new Set(),survivors=[],quads=0,collinear=0,cells=0,mixed=0,labelOK=0,direct=0,before=checks;
 for(let a=0;a<M.length;a++)for(let b=a+1;b<M.length;b++)for(let c=b+1;c<M.length;c++)for(let d=c+1;d<M.length;d++){
  let ids=[M[a],M[b],M[c],M[d]], [p,r,s,k]=ids.map(o=>P[o.i]),D=dot(p,cross(r,s));quads++;if(!D){collinear++;continue}
  let adj=[cross(r,s),cross(s,p),cross(p,r)],C=P.map(q=>adj.map(h=>dot(h,q))),[u,v,w]=C[ids[3].i];if(!u||!v||!w){collinear++;continue}
  // coefficient rows on Q/2 in lambda: alpha=w, beta=u*lambda, gamma=-v*(1+lambda).
  const form=(x,y)=>[w*(x[0]*y[1]+x[1]*y[0])-v*(x[2]*y[0]+x[0]*y[2]),u*(x[1]*y[2]+x[2]*y[1])-v*(x[2]*y[0]+x[0]*y[2])];
  let ev=new Map(),X=0n;
  function event(n,d){let z=gcd(n,d);n/=z;d/=z;if(d<0n){n=-n;d=-d}let key=n+"/"+d;if(!ev.has(key))ev.set(key,{n,d,changes:0n,tiePos:0n,tieZero:0n,forbid:false});return ev.get(key)}
  event(0n,1n).forbid=true;event(-1n,1n).forbid=true;
  for(let [i,j,bit] of TG){
   let p=C[i],q=sub(C[j],p),J=[form(p,p),form(p,q),form(q,q)],row=J.find(nz);if(!row)throw Error("all jets zero");
   let [h,m]=row;if(!m){if(h>0n)X|=bit;continue}
   if(m<0n)X|=bit;
   let e=event(-h,m);e.changes|=bit;let z=0;for(let [h,m] of J){z=sg(h*e.d+m*e.n);if(z)break}
   if(z>0)e.tiePos|=bit;else if(!z)e.tieZero|=bit;
  }
  function test(x){cells++;for(let {bits} of ids)if(!(x&bits)||!((t^x)&bits))return;mixed++;
   for(let l of L)if((x&l)&&((t^x)&l))return;labelOK++;
   if(count(x)!==15)return;
   let [A,B]=canon(x,t^x);if(visited.has(A))return;visited.add(A);direct++;
   if(can(A,4)&&can(B,4))survivors.push([A.toString(16),B.toString(16),ids.map(x=>x.i)])
  }
  test(X);
  for(let e of [...ev.values()].sort((a,b)=>sg(a.n*b.d-b.n*a.d))){
   if(!e.forbid){if(e.tieZero)throw Error("zero germ at nonsingular lambda");test((X&~e.changes)|e.tiePos)}
   X^=e.changes;test(X)
  }
 }
 result.push({t:t.toString(16),quads,collinear,cells,mixed,labelOK,direct,survivors,checks:checks-before})
}
return {initialChecks,checks,result};`;
const old='return {points:P.length,germs:G.length,linearPartitions:Q.length,result:rank4("two_anchor_kernel",[])};';
if(!src.includes(old))throw Error("pin mismatch");
console.log(Function(src.replace(old,patch).replace(/experiment\(data\)\s*$/,"return experiment(data)"))());
```
Activity association and independent mathematical review pending.
