# R858 candidate - Rational multi-resource support cuts and convex observer boundary

2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.

Continues R857 a8ee68c2476dd38092f7c4e09af8584fc0f9cbf0:research_notes/portable_direct/R857_MINIMAL_JOINT_SUFFIX_OBSERVER_PAIRWISE_CUTS.md, read directly. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389 retained; P000 V5 and joint observer read at that pin, residual companion 404 at that pin, ACTIVE global residual semantics read without repinning. Global entries verified at 8230f7dc82c1875929e2284bc6e5658f245c2219; current portable, continuation, method and activity protocols read. Existing lane EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91 metadata verified; private execution authority not established. R857 original owner query SUCCEEDED, RUNNING filter empty at 2026-11-28T02:18:38.022411Z (Source changed during collection). Current R858 owner query r3-20261128-r858-running-read admitted QUEUED. Independent portable research, no shared task mutation.

## 1. Rational support observer

Use the R857 explicit independent joint option tables, normalized nonnegative integer resource vectors e_k(z) and additive nonnegative rational costs; local analytic feasibility already filtered. At stage i the exact suffix sum set S_i consists of all joint sums F of original legal option words. For target j, positive integer d and nonnegative integer coefficients a_l (a_j=0), define the attained support
 B_i(j,d,a) = sum_{k>=i} max_z [d e_kj(z) - sum_l a_l e_kl(z)].
This is the exact maximum over S_i because one can choose the maximizing local option independently for each item, while retaining each item's full joint vector. The maximizing choices may differ by normal. B may be negative, even under coordinatewise normalization. For remaining budget h>=0, every feasible word satisfies
 F_j <= floor((B_i + sum_l a_l h_l)/d).
Take the minimum of this quantity and h_j, simultaneously across any finite set of normals. Call the resulting map P_i. It preserves the full feasible suffix language: any old feasible F obeys each cut by nonnegativity of a and integrality of F_j; conversely P_i(h)<=h. Negative resulting coordinate proves DEAD. Use R856 lattice saturation H_i before and after P_i; each operation preserves the language exactly. After choosing the same original local option subtract its full vector, then apply next-stage compression. The left quotient argument of R857 proves feasibility and exact cost optimization by retaining the cheapest prefix per equal stored key. No idempotence or minimality of finite cut map is assumed. No constraint or analytic radius relaxation.

For a bank of L normals, backward support precomputation uses O(r L sum_k |O_k|) integer arithmetic, each transition O(rL) plus gcd clipping, lookup and witness bookkeeping. Bit lengths polynomial in explicit input and coefficient bit lengths. With S_i reached keys, total transitions <=sum_i S_i |O_i|. For fixed r, an enumerable bank of small rational coefficients gives inexpensive discovery; general state count remains potentially exponential. The bank used in tests includes denominators 1,2,3 and numerators 0..2, plus R857 pairwise cuts.

## 2. Automatic optimal continuous support, and its exact limit

Let P=conv(S_i)=sum_k conv(E_k), where E_k is the finite local option set. Equality follows by distributing convex combinations independently (product weights), and the reverse inclusion by convexity. An extended LP uses x_kz>=0, sum_z x_kz=1, F=sum_kz x_kz e_k(z), F<=h. If feasible, for each j the continuous maximal coordinate is
 U_j(h)=max{F_j:F in P,F<=h}.
Dualize the other coordinate constraints, retaining the target cap separately. The LP without F_j<=h_j is feasible and bounded since P is compact. Standard finite LP strong duality gives its maximum as min_{lambda>=0} [sum_{l!=j} lambda_l h_l + sum_k max_z(e_kj(z)-sum_{l!=j}lambda_l e_kl(z))]. Intersecting with the target cap gives U_j=min(h_j, that value): if the unrestricted maximizer exceeds h_j, a segment to an originally feasible point attains h_j. Rational optimal duals exist for rational data. This LP thus automatically discovers an optimal support normal (or target cap); floor U_j is the strongest coordinate cap obtainable from this real relaxation. If the extended LP is infeasible, no discrete word is feasible; equivalently separation from the downward budget orthant can be certified by a nonnegative lambda with min_{F in P} lambda.F > lambda.h. LP has sum |O_k| variables and explicit polynomial-sized constraints; exact rational LP is polynomial in input bit length. This is an alternative theorem, not an executed LP solver in this round.

If for a given h the capped polytope P intersect {F<=h} has all its coordinate maxima attained at actual members of S_i (in particular if its vertices are members of S_i), then U=C_i, the minimal R857 joint observer. Otherwise the discrete hole can survive every linear cut: one item with options (0,2),(2,0),(1,3),(3,1), h=(1,1). Every option violates h; the convex midpoint (1,1) is feasible, both exact marginal sets contain 1 and both gcds are 1. No valid linear inequality for S_i can exclude that midpoint, and no coordinate cap preserving the convex feasible set can reduce h. Consequently even all rational support cuts plus exact marginals cannot in general produce DEAD. This is a discrete joint reachability obstruction, not a numerical error. Keep the original word set, including signed/phase provenance and any native coordinates, separate.

## 3. Exponential separation from pairwise cuts

Let m>=2, T=2^(m-1), W=2T-1. Prefix m-1 binary items have choices 0 or (2^i,0,0), i=0..m-2. Tail consists of two interleaved m-bit families, choices 0 or (2^i,2^i,0) and 0 or (2^i,0,2^i), in increasing i. All zero choices cost 1 and nonzero choices cost 0. Budget (3T-1,T,T). At the cut before the tail, prefix sums p run through 0..T-1, hence h=(3T-1-p,T,T). Tail satisfies F1=F2+F3, with each of F2,F3 attaining all 0..W and F1 all 0..2W. R857 pair bounds B(1,2)=B(1,3)=W, B(2,1)=B(3,1)=0, B(2,3)=B(3,2)=W. No pair or lattice cut changes these h. At an earlier prefix stage with remaining prefix sum R, the first residual lies in [2T+R,3T-1], below the pair cap T+W+R; other caps are inactive, so all T prefix states actually survive pair-only DP. Even exact marginal predecessor values do not change them.

The multi-support normal (d=1,a2=a3=1,target=1) has B=R before tail and 0 in tail. At every prefix stage it yields h1=2T+R, hence a single key; subtracting either next prefix option preserves at least the next cap. During tail, h1=h2+h3 after clipping and cutting: h2,h3 clipped independently, their sum is a multiple of the common gcd for F1 and is <= its maximum. The old h1 after subtraction is >= that sum, so H1 cannot reduce below it; the cut makes equality. In each family at the stage with next exponent t, the total selected lower bits belongs to [0,2^t-1]. Clipping to its suffix lattice and maximum gives at most two possible budgets; the closed family has one. By induction using the R856 exact transition, at most four joint keys occur at any stage (including between interleaved bits). All pair cuts are harmless for these keys: each pair bound follows from the family sums and their maxima. Thus S_pair >= T and S_multi <=4, with exact optimum 2: each family must omit at least one bit as W>T, and taking every prefix and every low tail bit satisfies all capacities at cost 2. No exponential enumeration is used for the wide family. This is a fixed-order auxiliary explicit-option family, not a claim for general Port realizability or an optimal order.

## 4. Executed exact evidence and continuation

Deterministic JS BigInt experiment below: 240 small independent option instances (1..3 resources, 1..6 items, 1..4 options, integer nonnegative costs), both pair and rational multi solvers versus full enumeration and witness recovery; 50 independent small suffix families, 15 budget queries each, direct word-by-word rational cut equivalence; constructed family m=2..6, m=15 pair and multi, m=100 multi only, optimum analytic 2. Counters are actual author checks, not independent review. No native BRC run; this is a finite-horizon auxiliary capacity observer, retaining original joint option identities and all original scientific sources.

Results: {"instances":240,"feasible":113,"leaves":14172,"transitions":4754,"checks":493,"strictMulti":83,"cutChecks":11865,"failures":0,"pairPrefix":16384,"pairPeak":32768,"multiPeak":4,"widePeak":4,"wideItems":299}

Next: construct a tractable discrete refinement of the LP observer (e.g. bounded-width residue classes or integral decomposition of Minkowski sums) and characterize when joint lattice plus support cuts suffice. Test against the explicit convex hole. General shared-bundle propagation, native BRC and Port correspondence remain open.

```js
function experiment(){
 const ck=(b,m)=>{if(!b)throw Error(m)}, min=(a,b)=>a<b?a:b,max=(a,b)=>a>b?a:b,gcd=(a,b)=>{while(b)[a,b]=[b,a%b];return a},floor=(a,b)=>a>=0n?a/b:-((-a+b-1n)/b);
 const stats={instances:0,feasible:0,leaves:0,transitions:0,checks:0,strictMulti:0,cutChecks:0,failures:0};let seed=858;const rnd=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return (seed>>>8)%n};
 function solve(items,A,mode,track=true){
  let n=items.length,r=A.length,zero=()=>A.map(()=>0n);
  let base=items.map(t=>A.map((_,j)=>t.reduce((s,o)=>min(s,o.d[j]),t[0].d[j])));
  let E=items.map((t,i)=>t.map(o=>({d:o.d.map((x,j)=>x-base[i][j]),c:o.c})));
  let normals=[];
  for(let j=0;j<r;j++)for(let l=0;l<r;l++)if(j!==l){let a=zero();a[l]=1n;normals.push({j,a,d:1n,multi:false})}
  if(mode==="multi")for(let j=0;j<r;j++)for(let d of [1n,2n,3n]){
   let ls=A.map((_,l)=>l).filter(l=>l!==j);
   function rec(k,a){if(k===ls.length){if(a.some(x=>x!==0n))normals.push({j,a:a.slice(),d,multi:true});return}for(let v=0n;v<=2n;v++){a[ls[k]]=v;rec(k+1,a)}}
   rec(0,zero())
  }
  if(mode==="family")normals.push({j:0,a:[0n,1n,1n],d:1n,multi:true});
  let G=Array.from({length:n+1},zero),M=Array.from({length:n+1},zero),B=Array.from({length:n+1},()=>normals.map(()=>0n));
  for(let i=n-1;i>=0;i--){
   for(let j=0;j<r;j++){G[i][j]=E[i].reduce((s,o)=>gcd(s,o.d[j]),G[i+1][j]);M[i][j]=M[i+1][j]+E[i].reduce((s,o)=>max(s,o.d[j]),0n)}
   normals.forEach(({j,a,d},k)=>{let vals=E[i].map(o=>d*o.d[j]-a.reduce((s,v,l)=>s+v*o.d[l],0n));B[i][k]=B[i+1][k]+vals.reduce(max)})
  }
  const H=(h,i)=>h.map((x,j)=>G[i][j]?min(M[i][j],x/G[i][j]*G[i][j]):0n);
  function canon(h,i){if(h.some(x=>x<0n))return null;let v=H(h,i),p=v.slice(),pair=v.slice();normals.forEach(({j,a,d,multi},k)=>{let b=floor(B[i][k]+a.reduce((s,x,l)=>s+x*v[l],0n),d);p[j]=min(p[j],b);if(!multi)pair[j]=min(pair[j],b)});if(track&&p.some((x,j)=>x<pair[j]))stats.strictMulti++;if(p.some(x=>x<0n))return null;return H(p,i)}
  let h=canon(A.map((a,j)=>base.reduce((s,b)=>s-b[j],a)),0);if(!h)return null;
  let dp=new Map([[h.join(","),{h,c:0n,w:[]}]]),peak=1,peaks=[1];
  for(let i=0;i<n;i++){let next=new Map();for(let s of dp.values())for(let k=0;k<E[i].length;k++){if(track)stats.transitions++;let o=E[i][k],h=canon(s.h.map((x,j)=>x-o.d[j]),i+1);if(!h)continue;let key=h.join(","),c=s.c+o.c,old=next.get(key);if(!old||c<old.c)next.set(key,{h,c,w:[...s.w,k]})}dp=next;peak=Math.max(peak,dp.size);peaks.push(dp.size)}
  let best=null;for(let s of dp.values())if(!best||s.c<best.c)best=s;return best?{...best,peak,peaks}:null;
 }
 function brute(items,A){let opt=null;function rec(i,s,c){if(i===items.length){stats.leaves++;if(s.every((x,j)=>x<=A[j])&&(opt===null||c<opt))opt=c;return}for(let o of items[i])rec(i+1,s.map((x,j)=>x+o.d[j]),c+o.c)}rec(0,A.map(()=>0n),0n);return opt}
 function verify(items,A,s,opt){stats.checks++;ck((s===null)===(opt===null),"feasibility");if(s){ck(s.c===opt,"optimum");let v=A.map(()=>0n),c=0n;ck(s.w.length===items.length,"witness size");s.w.forEach((k,i)=>{let o=items[i][k];v=v.map((x,j)=>x+o.d[j]);c+=o.c});ck(c===opt&&v.every((x,j)=>x<=A[j]),"witness")}}
 for(let k=0;k<240;k++){let r=1+k%3,n=1+rnd(6);let items=Array.from({length:n},()=>Array.from({length:1+rnd(4)},()=>({d:Array.from({length:r},()=>BigInt(rnd(12))),c:BigInt(rnd(15))})));let A=Array.from({length:r},()=>BigInt(rnd(n*10+1)));let opt=brute(items,A);stats.instances++;if(opt!==null)stats.feasible++;for(let mode of ["pair","multi"])verify(items,A,solve(items,A,mode),opt)}
 // Every rational support cut preserves feasibility of all enumerated words, including negative intercepts.
 for(let k=0;k<50;k++){let E=Array.from({length:1+rnd(4)},()=>Array.from({length:2+rnd(2)},()=>[BigInt(rnd(5)),BigInt(rnd(5)),BigInt(rnd(5))]));let F=[[0n,0n,0n]];for(let item of E)F=F.flatMap(s=>item.map(o=>s.map((x,j)=>x+o[j])));let d=1n+BigInt(rnd(4)),a=BigInt(rnd(5)),b=BigInt(rnd(5));let B=E.reduce((s,t)=>s+t.map(o=>d*o[0]-a*o[1]-b*o[2]).reduce(max),0n);ck(B===F.map(o=>d*o[0]-a*o[1]-b*o[2]).reduce(max),"support exact");for(let q=0;q<15;q++){let h=[0,0,0].map(()=>BigInt(rnd(15)));let u=min(h[0],floor(B+a*h[1]+b*h[2],d));for(let f of F){ck(f.every((x,j)=>x<=h[j])===(f[0]<=u&&f[1]<=h[1]&&f[2]<=h[2]),"cut language");stats.cutChecks++}}}
 function family(m){let T=1n<<BigInt(m-1),items=[];let add=d=>items.push([{d:[0n,0n,0n],c:1n},{d,c:0n}]);for(let i=0;i<m-1;i++)add([1n<<BigInt(i),0n,0n]);for(let i=0;i<m;i++){let w=1n<<BigInt(i);add([w,w,0n]);add([w,0n,w])}return {items,A:[3n*T-1n,T,T]}}
 for(let m=2;m<=6;m++){let {items,A}=family(m);let s=solve(items,A,"family",false),p=solve(items,A,"pair",false);ck(s.peak<=4,"family peak");ck(p.peaks[m-1]>=2**(m-1),"pair prefix");verify(items,A,s,2n);verify(items,A,p,2n)}
 let {items,A}=family(15),p=solve(items,A,"pair",false),s=solve(items,A,"family",false);verify(items,A,p,2n);verify(items,A,s,2n);stats.pairPrefix=p.peaks[14];stats.pairPeak=p.peak;stats.multiPeak=s.peak;
 ({items,A}=family(100));s=solve(items,A,"family",false);verify(items,A,s,2n);stats.widePeak=s.peak;stats.wideItems=items.length;
 // All linear support cuts plus exact marginals can miss a discrete hole.
 let F=[[0n,2n],[2n,0n],[1n,3n],[3n,1n]],h=[1n,1n];
 ck(F.every(v=>v.some((x,j)=>x>h[j])),"discrete hole");ck(F.every((_,j)=>j>=2||F.some(v=>v[j]===1n)),"marginal hole");
 return stats;
}
console.log(experiment());
```
