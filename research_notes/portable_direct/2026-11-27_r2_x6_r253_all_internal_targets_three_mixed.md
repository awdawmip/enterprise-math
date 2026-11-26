# X6 R253 — all 34 internal quadratic targets require three mixed endpoints

2026-11-27. Author proof and exact BigInt computations, NOT_REVIEWED. Continuation of R252, same informed TASK_RESEARCH mode, frozen scientific inputs and inherited capacity premises. Native read r2-20261127-0607-x6-read SUCCEEDED at 2026-11-26T22:07:43.203648Z, Source 673771a11b75db41a98bbaaebba8305fe8f28e30, NO_CANONICAL_PUBLICATION_DIRECTORY. No own identity/active owner projection established; no CLAIM, Result, Review or shared task-state mutation.

Source R252: 9aa4711f9113ed8edb5f607adb6fe99d86c82f54:research_notes/portable_direct/2026-11-27_r2_x6_r252_tangent_polar_incidence_capacity.md, blob 7d2b726a12f39ec1b26950a6bd19695e1c862317. Executable frozen R247: 7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md. All Port 10, 1935 directions, weights (17t,B,22t,D), six-pair BRC, 47 necessary labels, 49 components, 51 endpoints, 98 directed germs and 2225 linear mask inputs unchanged. This is auxiliary coefficient arithmetic, not native geometry.

## 1. Completed remaining exactly-two-mixed targets

The two c=27 targets left by R252 were executed separately, using the saved R252 reproduction with a target-specific filter and fresh caches. All searches completed, no cutoff.
Table: target hex, candidate endpoint pairs, label-exception/endpoint sets, branch visits, direct-capacity passing partitions, forced-component conflicts, oriented local pattern pairs before label exceptions, incremental can checks, relaxed survivors.
```
3cc35cfff0003f3dff0000fcf 105 307125 6114230 89098 1216895 637 26016362 0
33cf3202fffc0c300ffffe30 91 266175 8901176 160084 788291 445 40710893 4
```
Total checks including fresh common prefix 3,275,335 per run: 29,291,697 and 43,986,228. Every pair had a nonempty local bank. Four remaining capacity-relaxation partitions, listed as positive/negative hex masks and required mixed endpoint pair:
```
3c00000b37c0c0000cff030 300f32024c8000300f300e00 18 33
3c00000b37c0c0000cfd030 300f32024c8000300f302e00 18 33
3c000003b7c0c0000cfd030 300f3202c48000300f302e00 18 34
3c000003b7c0c0000cff030 300f3202c48000300f300e00 18 34
```
The survivors are not feasible quadratic observations, as shown below. Each pair of partitions differs only in germ bit 0x2000.

## 2. Exact coefficient infeasibility via positive dependence

For required zero endpoints p,r let B be an integer basis of the four-dimensional coefficient kernel, in monomial order (t²,B²,D²,tB,tD,BD). Write q=B^T z with z in R^4 (B stored as four row basis vectors). For each desired strict sign s in {-1,+1} on a directed germ, the first jet row that is not identically zero in this kernel, oriented by s and divided by its positive integer gcd, must have nonnegative scalar product with z. This is a necessary weak inequality even if that particular value is zero and later jet coefficients decide the actual sign. If five such oriented rows h_i satisfy a strictly positive integer dependence sum_i w_i h_i=0 and four of them span R^4, then all five h_i·z must vanish, whence z=0. Thus the whole mask is impossible for a nonzero Q; no higher jets need be erased or approximated.

For p18=(0,1,0), p33=(3,53,25), the kernel basis and a certificate common to the first two masks:
```
B=[[-625,0,9,0,0,0],[-53,0,0,3,0,0],[-25,0,0,0,3,0],[-1325,0,0,0,0,9]]
bit     s    h                                  w
10      +    [3497,-14,26,-155]                  513650
20      +    [-325,-26,-10,-725]                 106135
200     -    [-1908,2,-9,-103]                   507432
400     -    [-1624,1,-7,-164]                   77061
200000  -    [-3999,53,-43,1325]                 167145
det(h1,h2,h3,h4)=34097580
```
For p18=(0,1,0), p34=(2,34,83), the kernel basis and a certificate common to the last two masks:
```
B=[[-6889,0,4,0,0,0],[-17,0,0,1,0,0],[-83,0,0,0,2,0],[-1411,0,0,0,0,2]]
bit     s    h                                  w
10      +    [-3120,-29,-20,-2457]               18338719
20      +    [-13728,-29,-156,-2797]             2364765
200     -    [-77875,102,-375,6341]              876148
8000    +    [-6889,-17,-83,-1411]               5014100
100000  -    [9360,29,72,2587]                   20561160
det(h1,h2,h3,h4)=-41944766400
```
All weights strictly positive, both weighted row sums exactly zero. The certificates were found by exact alternating-minor enumeration, ignoring bit 0x2000 so each covers both signs at that germ. First four determinant nonzero in each case. Before extracting these short certificates an independent exact ray-enumeration check on the weak cones was performed: all four had 36 distinct oriented primary rows; 7074,7074,7079,7079 nonzero triple-cross-product tests respectively, no feasible nonzero rays, full row rank. A nontrivial pointed cone with full spanning normals has an extreme ray (slice by the sum of its normals to get a compact polytope), so this agrees with the short certificates. The certificate itself suffices and is much cheaper to recheck.

## 3. Consequence

Combining R251, R252 and this completed c27 extension, every one of the 34 possible internal targets for the sole full-rank quadratic in a depth-six tree needs at least three distinct mixed endpoints. Three distinct collinear zeros force a real factor, so the mixed triple is noncollinear. Quadratic evaluation at the three points gives three independent constraints. Thus the entire internal case now reduces to a finite union of three-dimensional coefficient kernels, under the inherited necessary-wall and complete linear suffix capacity premises. No target excluded merely for having more than two mixed endpoints; complete internal closure still open. The general quadratic root case also open; K6=1–2.

Useful next representation: for noncollinear null endpoints p,r,s write x=u p+v r+w s. Then Q(x)=2(alpha uv+beta vw+gamma wu) with alpha=B(p,r), beta=B(r,s), gamma=B(s,p). Full rank iff alpha beta gamma !=0. At p a tied tangent direction (u,v,w) satisfies alpha v+gamma w=0, and its nonzero second residual has sign -sign(alpha beta gamma) (substitute v=-gamma w/alpha). The same holds at r,s. This is a direct proof and permits coupling the three local banks by the same three polar signs and the same tangent residual. Use this and exact rank-three kernel enumeration, or search for a further mixed-endpoint obstruction. This next search has not been executed in R253.

## 4. Reproduction of c27 completion and certificate verification

Read R247 first JavaScript block as src; read R252 first JavaScript block as code. The executed two calls were:
```javascript
for(const target of ["3cc35cfff0003f3dff0000fcf","33cf3202fffc0c300ffffe30"]){
 const patched=code.replace('for(let t of roots.filter(t=>${mode}===1?count(t)<29:count(t)===${c0}))','for(let t of roots.filter(t=>t.toString(16)==="'+target+'"))');
 if(patched===code)throw Error("patch mismatch");
 console.log(Function("src",patched+"\nreturn run(src,2,27)")(src));
}
```
To verify the short certificates against the frozen input, insert this patch in R247 at its final return (same replacement convention as R252). It verifies the exact mask signs, independent null anchors, actual first-active rows, positive dependence and determinant; no numerical solver needed.
```javascript
const patch=`let T=BigInt("0x33cf3202fffc0c300ffffe30");
const C=[
 {p:18,r:33,a:["3c00000b37c0c0000cff030","3c00000b37c0c0000cfd030"],B:[[-625,0,9,0,0,0],[-53,0,0,3,0,0],[-25,0,0,0,3,0],[-1325,0,0,0,0,9]],bits:["10","20","200","400","200000"],s:[1,1,-1,-1,-1],H:[[3497,-14,26,-155],[-325,-26,-10,-725],[-1908,2,-9,-103],[-1624,1,-7,-164],[-3999,53,-43,1325]],w:[513650,106135,507432,77061,167145],d:34097580},
 {p:18,r:34,a:["3c000003b7c0c0000cfd030","3c000003b7c0c0000cff030"],B:[[-6889,0,4,0,0,0],[-17,0,0,1,0,0],[-83,0,0,0,2,0],[-1411,0,0,0,0,2]],bits:["10","20","200","8000","100000"],s:[1,1,-1,1,-1],H:[[-3120,-29,-20,-2457],[-13728,-29,-156,-2797],[-77875,102,-375,6341],[-6889,-17,-83,-1411],[9360,29,72,2587]],w:[18338719,2364765,876148,5014100,20561160],d:-41944766400}
];
const dt=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n),det3=(a,b,c)=>dot(a,cross(b,c)),cross4=(a,b,c)=>Array.from({length:4},(_,i)=>BigInt(i%2?-1:1)*det3(...[a,b,c].map(r=>r.filter((_,j)=>i!==j)))),det4=(a,b,c,d)=>-dt(cross4(a,b,c),d);
const mon=[[0,0],[1,1],[2,2],[0,1],[0,2],[1,2]],phi=p=>mon.map(([i,j])=>p[i]*p[j]),polar=(p,q)=>mon.map(([i,j])=>p[i]*q[j]+p[j]*q[i]);
let result=[];
for(let c of C){
 let B=c.B.map(x=>x.map(BigInt)),H=c.H.map(x=>x.map(BigInt)),w=c.w.map(BigInt);
 if(!nz(cross(P[c.p],P[c.r])))throw Error("same anchors");
 for(let x of B)if(dt(phi(P[c.p]),x)||dt(phi(P[c.r]),x))throw Error("kernel");
 // The four columns c,d,e,f give a nonzero diagonal minor in each listed basis.
 if(!det4(...B.map(x=>x.slice(2))))throw Error("basis rank");
 for(let i=0;i<5;i++){
  let bit=BigInt("0x"+c.bits[i]);if(!(bit&T))throw Error("not target");
  for(let a of c.a)if(((BigInt("0x"+a)&bit)?1:-1)!==c.s[i])throw Error("mask sign");
  let [u,v]=G.find(g=>g[2]===bit),p=P[u],q=sub(P[v],p);
  let js=[phi(p),polar(p,q),phi(q)].map(h=>B.map(x=>BigInt(c.s[i])*dt(h,x)));
  let h=norm(js.find(nz));if(h.join()!==H[i].join())throw Error("row mismatch");
 }
 if(w.some(x=>x<=0n))throw Error("not positive");
 let sum=Array.from({length:4},(_,i)=>H.reduce((s,h,j)=>s+w[j]*h[i],0n));
 if(nz(sum)||det4(...H.slice(0,4))!==BigInt(c.d)||!c.d)throw Error("certificate");
 result.push({p:c.p,r:c.r,det:String(c.d),sum:sum.map(String),verified:true});
}
return result;`;
const old='return {points:P.length,germs:G.length,linearPartitions:Q.length,result:rank4("two_anchor_kernel",[])};';
console.log(Function(src.replace(old,patch).replace(/experiment\(data\)\s*$/,"return experiment(data)"))());
```

Activity association and independent mathematical review pending.
