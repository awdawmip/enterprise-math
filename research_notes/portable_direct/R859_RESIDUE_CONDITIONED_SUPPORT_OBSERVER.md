# R859 candidate - Residue-conditioned support observer and fixed-modulus separation

2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.
Continuation of immutable R858 2adc0d9bd49e1ae7fa0c8384116f9d72eb480b94:research_notes/portable_direct/R858_RATIONAL_MULTI_RESOURCE_SUPPORT_CUTS.md, and R857 a8ee68c2476dd38092f7c4e09af8584fc0f9cbf0. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389 retained; P000 V5 and joint observer read at pin; residual companion at pin returned 404, ACTIVE global residual contract retained without repinning. Global entries and worldview verified at dab4822933640aade5f4cfb9d9f6f1034b18abbc. Current continuation, portable, method and activity contracts read. Existing lane EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91 metadata verified; no private execution authority established. R858 original RUNNING query SUCCEEDED, empty filtered snapshot at 2026-11-28T03:25:20.830536Z, Source changed during collection. Current request r3-20261128-r859-running-read admitted QUEUED; no shared claim or mutation. Independent auxiliary derivation.

## 1. Residue-conditioned support (exact finite-horizon observation)

Reuse R857/R858 independent explicit finite nonempty local option sets E_i in Z_nonnegative^r, original option identities, additive rational costs, local analytic feasibility already filtered. Let F(w) be the sum of an original suffix word; h is an integer budget. Negative budget is DEAD. Coordinatewise common baselines may be removed as R856, but not needed.

Choose integer modulus q>=2 and a finite bank N of signed integer normals a in Z^r. For each residue v in (Z/qZ)^r (representatives 0..q-1) define support B_i(v,a)=max a.F(w) over suffix words with F(w) congruent v. Unreachable residues are absent (not zero supports). Terminal table has only zero residue and all zero supports. Backward recurrence
 B_i(v,a)=max_{z in E_i} [a.z+B_(i+1)(v-z mod q,a)]
over reachable children. This follows from partitioning the original suffix words by their first original option; every finite maximum is attained. Different normals can have different witnesses; no independent mixing of options is assumed. The full reachable residues are retained jointly, not as marginal sets.

For h>=0 and reachable v<=h, define lower l=v, upper u_j=h_j-((h_j-v_j) mod q). Every feasible word in that residue lies in this box. For each normal a, define t_j=a_j*l_j for a_j>=0 and a_j*u_j otherwise, L=sum t_j. If L>B_i(v,a), discard the class. For each a_j>0, a valid upper cap is floor((B_i(v,a)-L+t_j)/a_j), rounded DOWN to the residue v_j modulo q. Intersect all such caps with u_j, using the original box for the minima. Discard if any resulting cap is below l_j. Negative signs in the normal are essential and are paid with upper rather than lower box bounds. Let K_i(h) be the componentwise maximum of the final caps over surviving residues; if none, DEAD.

Proof of exact language preservation: every old feasible word belongs to a reachable residue, lies in its box, satisfies every support inequality, and survives every discard and cap; hence it lies below K_i(h). Conversely K_i(h)<=h. If no class survives, no original feasible word exists. A surviving residue need not contain a feasible word, and K need not be minimal. Applying K before the next local choice and then subtracting that choice's entire vector preserves the feasible suffix words by the left quotient of R857. Retain the cheapest prefix per equal K key and recover the original option sequence; this is exact additive optimization, not a continuous rounding or capacity relaxation. A single pass suffices for soundness; no fixed-point claim. Composition with any R856/R858 language-preserving cap is valid.

Dense preprocessing O(r |N| q^r sum_i |E_i|) integer operations, storage O((n+1) q^r (r+|N|)); each canonicalization O(r |N| q^r) plus lookups and original witness recovery. Sparse reachable tables can replace q^r by actual residue counts. Integer bit lengths are polynomial in explicit option and normal bit lengths and log n, log q. This is fixed-modulus fixed-resource preprocessing, not a general polynomial bound on outer DP keys. Input encoded in binary; q^r is numeric, not polynomial in log q.

## 2. Exact small-box theorem

If 0<=h_j<q for all j, and N contains the normal (-1,...,-1), then K_i(h) is precisely the minimal joint observer of R857, including DEAD. For any residue v<=h, the only candidate in the box is v itself. All nonnegative suffix points in that residue are v+q b, b>=0 integral. Thus the maximum of -sum F equals -sum v iff an original suffix word attains v, and is strictly smaller otherwise. The discard test with that normal is exactly this equality test. Other valid cuts cannot discard v if attained. The componentwise maximum of the surviving v is therefore exactly C_i(h). No assumption that maxima are simultaneous. This yields an exact tractable oracle for bounded budgets even when individual option values are arbitrarily large; q may be chosen as 1+max h, with corresponding numeric preprocessing cost.

## 3. Full affine lattice and convex hole

Strengthen R858's hole to E={(0,2),(2,0),(1,3),(3,1),(4,5)}, h=(1,1). No option meets the budget, but (1,1) is a convex midpoint of (0,2),(2,0), both exact marginal sets include 1, and the difference lattice is all Z^2: differences (1,1),(4,3) from (0,2) have determinant -1. Consequently even the exact joint affine lattice, full convex hull and exact marginal predecessor observations do not reject the point. Modulo 2, residue (0,0) has only the box point (0,0) and actual minimum sum 2; residue (1,1) has only (1,1) and actual minimum sum 4; residue (0,1) has only (0,1) and actual sum 9; (1,0) is unreachable. The normal (-1,-1) rejects each reachable class. This is a structural joint reachability deficit, not an approximation error.

## 4. Exponential separation from all continuous support and exact marginals

For m>=2 let T=2^m, L=T-1, P=T/2-1. Process m-1 prefix bits (0,0) or (2^i,0), i=0..m-2; then a special item with (0,0),(0,1),(T,2); then m ordinary bits (0,0) or (2^i,0), i=0..m-1. Budget (L+P,1). Prefix/ordinary zero bits cost 1, nonzero cost 0; special choices cost 2,1,0 respectively. Exact optimum 1: high option forbidden by second budget, take all bits and special middle option. No other choices can cost less.

At a prefix stage with remaining prefix bit sum R, every actual residual h1 lies between L+R and L+P (and h2=1). The suffix first-coordinate marginal contains every integer 0..L+R+T (the low ordinary bits plus remaining prefix bits cover 0..L+R and the high option adds T; intervals overlap or touch). The second marginal is {0,1,2}. The suffix joint affine lattice is full Z^2 because of differences (1,0),(0,1). The continuous capped maximum in first coordinate is h1: all low bits plus a half high special option permits L+R+T/2, and convex scaling toward zero gives h1. The second coordinate attains 1 via middle option alone. Thus even the strongest R858 coordinate-cap LP observer, exact marginals and full affine lattice leave every such budget unchanged, including after repeated application. At the cut before special item, 2^(m-1) distinct prefix budgets survive. This is a lower bound on those cap-based DP representations in the specified order, not on arbitrary algorithms.

Use q=2 and normals (1,0),(0,+/-1),(-1,-1),(2,-T), with any additional valid normals. In classes with second residue zero, feasible box upper h2 is 0, and the maximum of 2F1-T F2 is 2(L+R) (either high or zero special). Hence F1<=L+R. In second residue one the special must be (0,1), so support of (1,0) is at most L+R. Both bounds remain valid when conditioning also on first residue. The actual word selecting all remaining bits and middle special attains (L+R,1), so K_i(h) is exactly this cap for every prefix budget. At the special item the high choice is rejected; the others both lead to (L,0) under canonicalization. For each subsequent low bit the remaining maximum is attained with all remaining bits, and the support (1,0) clips both choices to the same remaining maximum; (0,1) clips second to zero. Thus exactly one stored key at every stage, with original witness and optimum 1. The modulus is fixed; the normal has O(m) bits. Processing uses polynomial bit cost in the explicit construction. We do not claim general native Port realization.

## 5. Executed exact evidence

Deterministic JavaScript BigInt script below. 180 small independent explicit-option problems (2..3 capacities, 1..5 items, 1..4 options, coordinates 0..6, costs 0..8, q=2..4) with full enumeration of optimal cost and witness checking. For each suffix, every conditional support compared with enumeration and four budget queries checked word by word; two queries lie in the small-box domain and are checked against exact minimal observer including DEAD. The full-lattice hole and the fixed-modulus family are tested; m<=6 additionally exhaustively checked, m=15 prefix states explicitly enumerated, m=100 residue DP with analytic optimum (no exponential exhaustive claim). Counts below are actual author checks, not independent review.

Results: {"instances":180,"feasible":77,"words":13589,"languageChecks":35340,"smallBoxChecks":1410,"transitions":1630,"merges":667,"supportChecks":2950,"witnessChecks":84,"failures":0,"peaks":[{"m":2,"items":4,"peak":1,"opt":"1"},{"m":3,"items":6,"peak":1,"opt":"1"},{"m":4,"items":8,"peak":1,"opt":"1"},{"m":5,"items":10,"peak":1,"opt":"1"},{"m":6,"items":12,"peak":1,"opt":"1"},{"m":15,"items":30,"peak":1,"opt":"1"},{"m":100,"items":200,"peak":1,"opt":"1"}],"explicitPrefixStatesM15":16384}

Next: exploit character/kernel representations to avoid q^r when only a few mixed congruences matter; investigate adaptive support selection and joint residue-conditioned LP exactness classes. General native BRC joint moment observer, shared bundle propagation and Port realization remain open; no native BRC experiment or new P000 assumption.

```js
function experiment(){
 const ck=(b,m)=>{if(!b)throw Error(m)}, min=(a,b)=>a<b?a:b,max=(a,b)=>a>b?a:b;
 const floor=(a,b)=>a>=0n?a/b:-((-a+b-1n)/b), mod=(a,q)=>(a%q+q)%q;
 const dot=(a,b)=>a.reduce((s,x,j)=>s+x*b[j],0n),add=(a,b)=>a.map((x,j)=>x+b[j]),sub=(a,b)=>a.map((x,j)=>x-b[j]),le=(a,b)=>a.every((x,j)=>x<=b[j]),key=a=>a.join(",");
 const stats={instances:0,feasible:0,words:0,languageChecks:0,smallBoxChecks:0,transitions:0,merges:0,supportChecks:0,witnessChecks:0,failures:0};
 let seed=859;const rnd=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return (seed>>>8)%n};
 function normals(r){let a=[];for(let j=0;j<r;j++)for(let sign of [-1n,1n])a.push(Array.from({length:r},(_,k)=>j===k?sign:0n));a.push(Array(r).fill(-1n));a.push(Array(r).fill(1n));for(let j=0;j<r;j++)for(let k=0;k<r;k++)if(j!==k)a.push(Array.from({length:r},(_,l)=>l===j?1n:l===k?-1n:0n));return a}
 function observer(items,r,q,N){
  let n=items.length,zero=Array(r).fill(0n),tables=Array.from({length:n+1},()=>new Map());
  tables[n].set(key(zero),{v:zero,b:N.map(()=>0n)});
  for(let i=n-1;i>=0;i--)for(let s of tables[i+1].values())for(let o of items[i]){
   let v=add(s.v,o.d).map(x=>mod(x,q)),k=key(v),b=N.map((a,l)=>s.b[l]+dot(a,o.d)),old=tables[i].get(k);
   if(old)old.b=old.b.map((x,l)=>max(x,b[l]));else tables[i].set(k,{v,b});
  }
  function canon(h,i){
   if(h.some(x=>x<0n))return null;
   let out=null;
   for(let {v,b} of tables[i].values()){
    if(!le(v,h))continue;
    let u=h.map((x,j)=>x-mod(x-v[j],q)),cap=u.slice(),ok=true;
    for(let k=0;k<N.length;k++){
     let a=N[k],terms=a.map((x,j)=>x*(x>=0n?v[j]:u[j])),low=terms.reduce((s,x)=>s+x,0n);
     if(low>b[k]){ok=false;break}
     for(let j=0;j<r;j++)if(a[j]>0n){let t=floor(b[k]-low+terms[j],a[j]);cap[j]=min(cap[j],t-mod(t-v[j],q))}
    }
    if(!ok||!le(v,cap))continue;
    out=out?out.map((x,j)=>max(x,cap[j])):cap;
   }
   return out;
  }
  return {canon,tables};
 }
 function solve(items,A,q,N){
  let {canon}=observer(items,A.length,q,N),h=canon(A,0),dp=new Map(),peak=0;
  if(h)dp.set(key(h),{h,c:0n,w:[]});peak=dp.size;
  for(let i=0;i<items.length;i++){
   let next=new Map();
   for(let s of dp.values())for(let k=0;k<items[i].length;k++){
    stats.transitions++;let o=items[i][k],h=canon(sub(s.h,o.d),i+1);if(!h)continue;
    let z=key(h),c=s.c+o.c,old=next.get(z);if(old)stats.merges++;
    if(!old||c<old.c)next.set(z,{h,c,w:[...s.w,k]})
   }dp=next;peak=Math.max(peak,dp.size)
  }
  let best=null;for(let s of dp.values())if(!best||s.c<best.c)best=s;return {best,peak}
 }
 function words(items,r){let f=[{d:Array(r).fill(0n),c:0n}];for(let t of items)f=f.flatMap(s=>t.map(o=>({d:add(s.d,o.d),c:s.c+o.c})));return f}
 function verify(items,A,s,opt){ck((s===null)===(opt===null),"feasibility");if(s){let d=A.map(()=>0n),c=0n;ck(s.w.length===items.length,"length");s.w.forEach((k,i)=>{let o=items[i][k];d=add(d,o.d);c+=o.c});ck(c===opt&&s.c===opt&&le(d,A),"optimum/witness");stats.witnessChecks++}}
 for(let trial=0;trial<180;trial++){
  let r=2+trial%2,n=1+rnd(5),q=BigInt(2+trial%3),N=normals(r);
  let items=Array.from({length:n},()=>Array.from({length:1+rnd(4)},()=>({d:Array.from({length:r},()=>BigInt(rnd(7))),c:BigInt(rnd(9))})));
  let f=words(items,r),A=Array.from({length:r},()=>BigInt(rnd(6*n+1))),opt=null;stats.words+=f.length;stats.instances++;
  for(let w of f)if(le(w.d,A)&&(opt===null||w.c<opt))opt=w.c;
  if(opt!==null)stats.feasible++;
  verify(items,A,solve(items,A,q,N).best,opt);
  let ob=observer(items,r,q,N);
  for(let i=0;i<=n;i++){
   let F=words(items.slice(i),r),br=new Map();
   for(let w of F){let k=key(w.d.map(x=>mod(x,q))),v=N.map(a=>dot(a,w.d)),old=br.get(k);br.set(k,old?old.map((x,j)=>max(x,v[j])):v)}
   ck(br.size===ob.tables[i].size,"residue count");
   for(let [k,b] of br){ck(key(b)===key(ob.tables[i].get(k).b),"conditional support");stats.supportChecks++}
   for(let t=0;t<4;t++){
    let small=t<2,h=Array.from({length:r},()=>BigInt(rnd(small?Number(q):6*n+1))),v=ob.canon(h,i),feasible=F.filter(w=>le(w.d,h));
    for(let w of F){ck(le(w.d,h)===(v!==null&&le(w.d,v)),"language");stats.languageChecks++}
    if(small){let exact=feasible.length?Array.from({length:r},(_,j)=>feasible.map(w=>w.d[j]).reduce(max)):null;ck((v===null)===(exact===null)&&(!v||key(v)===key(exact)),"small box minimal");stats.smallBoxChecks++}
   }
  }
 }
 const item=ds=>ds.map(d=>({d:d.map(BigInt),c:0n}));
 const hole=[item([[0,2],[2,0],[1,3],[3,1],[4,5]])],h=[1n,1n];
 ck(observer(hole,2,2n,normals(2)).canon(h,0)===null,"full-lattice hole");
 function family(m){
  let T=1n<<BigInt(m),L=T-1n,P=T/2n-1n,items=[];
  const bit=i=>[{d:[0n,0n],c:1n},{d:[1n<<BigInt(i),0n],c:0n}];
  for(let i=0;i<m-1;i++)items.push(bit(i));
  items.push([{d:[0n,0n],c:2n},{d:[0n,1n],c:1n},{d:[T,2n],c:0n}]);
  for(let i=0;i<m;i++)items.push(bit(i));
  return {items,A:[L+P,1n],N:[...normals(2),[2n,-T]]}
 }
 let peaks=[];
 for(let m of [2,3,4,5,6,15,100]){
  let {items,A,N}=family(m),s=solve(items,A,2n,N);verify(items,A,s.best,1n);ck(s.peak===1,"one key family");peaks.push({m,items:items.length,peak:s.peak,opt:s.best.c.toString()});
  if(m<=6){let f=words(items,2),opt=f.filter(w=>le(w.d,A)).map(w=>w.c).reduce(min);ck(opt===1n,"family exhaustive");stats.words+=f.length}
 }
 let prefix=new Set([0n]);for(let i=0;i<14;i++){let b=1n<<BigInt(i);prefix=new Set([...prefix,...[...prefix].map(x=>x+b)])}
 ck(prefix.size===16384,"prefix states");
 return {...stats,peaks,explicitPrefixStatesM15:prefix.size};
}
console.log(experiment());
```
