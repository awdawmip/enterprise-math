# R872 — Unbounded attachment unions via weighted defect factors (exact counting)

Date 2026-11-29 Asia/Shanghai. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED. Independent informed portable auxiliary integer relation model, no native BRC/Port attribution, no shared task claim. Own recovery metadata verified EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91, execution_authorized=false. Current owner read r3-20261129-r872-running-read subsequently SUCCEEDED, snapshot as of 2026-11-28T17:18:56.700482+00:00, RUNNING filter empty, complete event pages revalidated; no execution authority. Predecessor exact read 32cdc04826f4c184bb9b369eba1d0743c35dacfa:research_notes/portable_direct/R871_SIGNED_BOUNDARY_DEFECT_COMPOSITION.md; reuse R870 connected-support logarithm and R871 pinned local oracle. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 and joint observer read; generated startup, heartbeat and residual companion paths 404, no repin. Current global rules at 1c7c6e3ea2df3a7472c53785d5fd63b9dce0b2ef, P000 V4 and ACTIVE worldview read. Source control main 9af1b7dc26c6a470a56a5ffaeaa2f4495a5bd3a3.

## 1. Scope and theorem

Use the R869/871 reference X, original loopless indexed graph and finite explicit distinct integer domains. Here assume the full graph is bipartite, with fixed signs s_u=-s_v along every edge. Put y_v=s_v(x_v-X_v), c_e=X_u+X_v-t_e; each original edge slack is |c_e+s_u(y_u-y_v)|, and reference variation is |y_u-y_v|. Let k0=sum |c_e|<=K, B=K+k0<=2K, so every feasible assignment has total variation <=B. Restrict domains if desired without changing reference.

Partition into a connected parent H and pairwise vertex-disjoint connected child regions J_i; no edges between distinct children. Each child has nonempty attachment scope A_i of distinct parent vertices incident to its cross edges, |A_i|<=a. Parent internal graph is (q,B)-edge-unbreakable (as in R870), n>(B+1)q. For B=0 handle separately by constant parent label. Assume exact child tables N_i(sigma,k), k=0..K, are supplied or computable by a polynomial-times-parameter local oracle (e.g. R871 where applicable): they count child assignments including all cross-edge slack for fixed parent signature. They are queried only at tuples whose gauge labels differ pairwise by <=B; others have zero feasible entry, by paths via the child. A connected child supplies a path between any two attachments using only that child's internal and cross edges. Child paths for distinct children share no edges. Child oracle complexity is explicitly additional; no general recursive decomposition or oracle for arbitrary children claimed.

Then the exact slack histogram of the full graph is computable in f(K,q,a)*poly(explicit input and table size), independent of the size of the UNION of all A_i. The count includes each full assignment once; original signed residuals recover from parent labels and individual child witnesses, not from a histogram alone. This theorem is for counting; arbitrary binary-encoded unary cost optimization remains open here.

## 2. Charged factor-split variation and bounded-degree interaction

R870 gives a unique parent majority r and <=q exceptions, each |y_v-r|<=B (for B>=1 n>2q). For any full feasible assignment, define
V*=sum_{e in H}|y_u-y_v| + sum_i 1{y is nonconstant on A_i} <= B.
Proof: for each nonconstant A_i take two unequal labels and the path via J_i; integer variation on that path is >=1, by telescoping. These paths and parent edges are edge-disjoint. Keep all actual slack in the child factors; V* is a filter, NOT an extra slack charge.

Augment the parent adjacency by making each A_i a clique (parallel incidences retained in factors). A defect polymer is one connected component of vertices with y!=r in this augmented graph, with actual labels. Distinct components are disjoint and nonadjacent, hence cannot touch a common parent edge, unary factor or child scope. Each support S has <=q vertices. Its augmented simple cut is at most a^2 B: each crossing parent edge charges at least one unit to V*, and each crossing child scope charges one split unit; each such scope has at most floor(a^2/4) crossing pairs. The stronger a B cut bound is not asserted in general. More importantly the number of distinct outside neighbors is <=a B, because one split scope has at most a outside vertices. Use the safe cut bound a^2 B for enumeration. For each labelled polymer define v(P) as the sum of parent variation on incident edges plus the number of incident nonconstant child scopes, with all outside labels set to r. Each proper nonempty support has an original parent edge leaving it (H connected), so v(P)>=1. Distinct polymers have disjoint affected factors and sum v=V*. Require total support size <=q and sum v<=B; actual feasible assignments pass both tests. Conversely any such independent family gives one parent assignment, and the original factor polynomials below enforce all remaining constraints. No parent assignment with different background is counted twice because support size<=q and n>2q.

Enumerate connected supports by deterministic include/exclude frontier search from each vertex, pruning >q included vertices or >a^2 B crossing edges into excluded vertices. In any branch that survives, each excluded frontier vertex is adjacent to an included one, so at most a^2 B excluded decisions, and <=q included decisions. At most 2^(q+a^2 B+1) supports containing a fixed root, and at most (2B)^q labelings for each. Each admissible polymer has <=aB outside neighbors, so conflict graph degree <=(q+aB)2^(q+a^2 B+1) max(1,2B)^q. All preprocessing is FPT-polynomial even with arbitrarily many attachments, using explicit factor incidence scans. Do not infer bounded degree of original parent graph.

## 3. Weighted generating function without division-by-zero

For each child define polynomial f_i(t; sigma)=sum_{k=0}^K N_i(sigma,k)t^k. Parent edges are factors t^{actual slack} (zero if slack>K); parent unary domain factors are 0 or 1. All coefficients are nonnegative. Choose integer H0> product of original domain sizes (or product of parent domain sizes times product over children of upper bounds for their total assignment counts). Then evaluating at t=H0 gives a carry-free encoding: digits 0..K of the full product-sum equal the exact slack histogram, since every coefficient is below H0. Truncation per factor is safe because slack nonnegative. Degree at most K times number of non-unary factors, hence integer bit length polynomial in explicit input, K and log H0.

Fix background r. Let b_f be each factor evaluated at the constant background; bad factors have b_f=0. Set W=product_f max(1,b_f), h0=#bad. For candidate P let F(P) be the factors whose scopes intersect its support, b'_f(P) their actual evaluation with outside at r. Drop candidates having any b'_f=0. Define
w(P) = W * product_{f in F(P)} b'_f(P) / product_{f in F(P)} max(1,b_f),
h(P)=number of bad factors in F(P).
This is a nonnegative INTEGER, because the divisor divides W. (For a child query outside the bounded-offset domain return 0.) A compatible independent set I touches disjoint factor sets, so it is valid only if sum h=h0. Its full weighted contribution is exactly W^(1-|I|) product w(P). This also handles arbitrarily many zero baseline factors, including those repaired simultaneously by one parent defect. Counts of bad factors are ordinary integers up to input size; no parameter-only bound on h0 is assumed.

Form weighted independence polynomial
Z(z,u,b,j)=sum_{I independent} product w(P) z^{sum v}u^{sum |S|} b^{sum h}j^{|I|}.
Truncate z at B,u at q,b at h0; all exponents nonnegative. Use R870 connected-support Mobius log: log Z=sum over connected induced supports T, |T|<=B, of sum_{U subset T} (-1)^{|T|-|U|}log Z_{G[U]}, mod z^(B+1). Proof: coefficient of a monomial using exactly vertex support T is isolated by Mobius inversion; disconnected supports have zero because independence polynomials multiply on disconnected graphs and log adds. Each candidate contributes positive z-degree so no larger support contributes. Enumerate connected sets in bounded-degree conflict graph in f(K,q,a)*poly(input); calculate truncated logs with exact rationals or scale by B!, then exponentiate by z*dZ/dz=Z*z*d(log Z)/dz. The other degrees are polynomially bounded (h0 may be linear in input); coefficients have polynomial-times-parameter bit length as |I|<=B. For coefficient A_{v,s,h0,j}, add W*A/W^j, exactly integral by disjoint factor sets. Sum over backgrounds, v<=B,s<=q,j<=B and extract base-H0 digits 0..K. B=0 only constant parent assignments, evaluated directly. This proves the theorem, including zero count and arbitrary domain pinning. No independence of joint attachments is assumed. Local table entries and original factor provenance remain the extension interface.

## 4. Complexity and remaining work

Given exact child oracle, signatures need only one explicit scalar anchor and (2B+1)^(a-1) offsets (R871, path gauge). Tables may store arbitrary parent attachment union size by factorization; no D^(union size) joint table. Candidate enumeration and factor evaluation cost f(K,q,a)*poly(input), as does exact integer weighted cluster expansion and digit recovery. The explicit code below uses cut bound a*B for its tested scopes a<=3 (then valid); general implementation should use a^2 B as in the proof. Its variation charge and weighted log use exact BigInt. Cost minimization with binary-encoded arbitrary unary costs is not proved by this encoding: an extra cost digit exponent could have exponential bit length. Next: combine per-factor min-plus budget tables with defect replacement without losing the effects of removed baseline factors, then recursive region decomposition. General K-only counting for arbitrary graphs remains open. For original assignment recovery, exact conditional counts permit self-reduction via domain pinning; no extra native interpretation is asserted.

## 5. Exact author checks

Seed 872, 100 deterministic small cases plus K=0 case; binary gauge domains, some pinned, parent star, child singleton attached to one to three distinct leaves, reference total slack 0 or 1, K=0..2. Independent brute force over all original vertex assignments. Star is (B,B)-edge-unbreakable for n>2B (a cut not containing center has size equal to its cut capacity). Large tree: 101 parent vertices, 100 independent child leaves, 100 distinct parent attachments, 200 edges. Binary gauge, K=2, zero reference. Independent tree count by choosing disagreement edges and root label: exactly 2*C(200,k) for k=0,1,2. All checks succeeded. Code is auxiliary integer arithmetic, not native BRC.

```json
{
  "cases": 101,
  "brute_assignments": 18384,
  "polymers": 834,
  "connected_supports": 978,
  "zero_baseline_factors": 139,
  "large": {
    "parent_vertices": 101,
    "child_vertices": 100,
    "attachments": 100,
    "edges": 200,
    "K": 2,
    "counts": [
      "2",
      "400",
      "39800"
    ]
  }
}
```

```javascript
function verify872(){
 const abs=Math.abs, assert=(b,m)=>{if(!b)throw Error(m)}, stats={cases:0,brute_assignments:0,polymers:0,connected_supports:0,zero_baseline_factors:0,large:null};
 function product(D,cb,x=[]){if(x.length===D.length){cb(x);return}for(const y of D[x.length]){x.push(y);product(D,cb,x);x.pop()}}
 function solve(D,E,F,K,B,q,H){
  const n=D.length, a=Math.max(2,...F.map(f=>f.scope.length)), A=Array.from({length:n},()=>new Set());
  const connect=S=>{for(const u of S)for(const v of S)if(u!==v)A[u].add(v)};
  E.forEach(e=>connect(e.slice(0,2)));F.forEach(f=>connect(f.scope));
  const factors=[...D.map((d,i)=>({scope:[i],eval:x=>d.includes(x[0])?1n:0n})),...E.map(([u,v,c,s])=>({scope:[u,v],eval:x=>{let k=abs(c+s*(x[0]-x[1]));return k<=K?H**BigInt(k):0n}})),...F];
  const supports=new Map();
  if(B>0)for(let root=0;root<n;root++){
   function visit(S,X){let cut=0;for(const u of S)for(const v of A[u])if(X.has(v))cut++;if(cut>a*B||S.size>q)return;
    let v=-1;for(const u of S){for(const w of A[u])if(!S.has(w)&&!X.has(w)){v=w;break}if(v>=0)break}
    if(v<0){let b=[...S].sort((x,y)=>x-y);supports.set(b.join(","),b);return}
    if(S.size<q){S.add(v);visit(S,X);S.delete(v)}X.add(v);visit(S,X);X.delete(v)
   }visit(new Set([root]),new Set())
  }
  let out=0n;
  for(const r of new Set(D.flat())){
   const base=factors.map(f=>f.eval(f.scope.map(()=>r))), bad=base.filter(x=>x===0n).length;stats.zero_baseline_factors+=bad;
   let W=base.reduce((z,x)=>z*(x||1n),1n), P=[];
   for(const S of supports.values()){
    let U=new Set(S), near=new Set(S);for(const u of S)for(const v of A[u])near.add(v);
    const affected=factors.map((f,i)=>f.scope.some(v=>U.has(v))?i:-1).filter(i=>i>=0);
    const divisor=affected.reduce((z,i)=>z*(base[i]||1n),1n), h=affected.filter(i=>!base[i]).length;
    product(S.map(v=>D[v].filter(x=>x!==r&&abs(x-r)<=B)),vals=>{
     const map=new Map(S.map((v,i)=>[v,vals[i]])), y=v=>map.get(v)??r;
     const v=E.reduce((z,[u,w])=>z+abs(y(u)-y(w)),0)+F.reduce((z,f)=>z+Number(f.scope.some(u=>y(u)!==y(f.scope[0]))),0);
     if(v<1||v>B)return;
     let w=W/divisor;for(const i of affected){let f=factors[i];w*=f.eval(f.scope.map(y));if(!w)return}
     P.push({S,near,v,h,w,size:S.length});
    })
   }
   stats.polymers+=P.length;
   const G=P.map(()=>new Set()), by=Array.from({length:n},()=>[]);
   P.forEach((p,i)=>p.S.forEach(v=>by[v].push(i)));P.forEach((p,i)=>{for(const v of p.near)for(const j of by[v])if(j!==i)G[i].add(j)});
   const key=(v,s,h,j)=>[v,s,h,j].join(","), un=k=>k.split(",").map(Number),zero=key(0,0,0,0),one=new Map([[zero,1n]]);
   function add(M,k,x){let z=(M.get(k)||0n)+x;if(z)M.set(k,z);else M.delete(k)}
   function mul(M,N){let R=new Map();for(const [k,x] of M)for(const [l,y] of N){let [v,s,h,j]=un(k),[w,t,i,p]=un(l);if(v+w<=B&&s+t<=q&&h+i<=bad)add(R,key(v+w,s+t,h+i,j+p),x*y)}return R}
   let fact=1n;for(let i=1;i<=B;i++)fact*=BigInt(i);
   function log(T){let Z=new Map();function go(i,S,v,s,h,j,w){for(let a=i;a<T.length;a++){let b=T[a],p=P[b];if(v+p.v>B||s+p.size>q||h+p.h>bad||S.some(c=>G[b].has(c)))continue;let z=w*p.w;add(Z,key(v+p.v,s+p.size,h+p.h,j+1),z);go(a+1,[...S,b],v+p.v,s+p.size,h+p.h,j+1,z)}}go(0,[],0,0,0,0,1n);
    let L=new Map(),power=new Map(one);for(let i=1;i<=B;i++){power=mul(power,Z);if(!power.size)break;let c=(i%2?1n:-1n)*fact/BigInt(i);for(const [k,w] of power)add(L,k,c*w)}return L
   }
   const seen=new Set(), L=new Map();
   function conn(S){let a=[...S].sort((x,y)=>x-y),id=a.join(",");if(seen.has(id))return;seen.add(id);stats.connected_supports++;
    function sub(i,T){if(i===a.length){if(!T.length)return;let s=(a.length-T.length)%2?-1n:1n;for(const [k,w] of log(T))add(L,k,s*w);return}sub(i+1,T);sub(i+1,[...T,a[i]])}sub(0,[]);
    if(S.size<B){let near=new Set();for(const u of S)for(const v of G[u])if(!S.has(v))near.add(v);for(const v of near)conn(new Set([...S,v]))}
   }
   if(B)for(let i=0;i<P.length;i++)conn(new Set([i]));
   const Z=new Map(one);
   for(let v=1;v<=B;v++){let row=new Map();for(const [k,x] of L){let [j,s,h,c]=un(k);for(const [l,y] of Z){let [w,t,i,d]=un(l);if(j+w===v&&s+t<=q&&h+i<=bad)add(row,key(v,s+t,h+i,c+d),BigInt(j)*x*y)}}for(const [k,x] of row){let div=fact*BigInt(v);assert(x%div===0n&&x>=0n,"exp");if(x)Z.set(k,x/div)}}
   for(const [k,x] of Z){let [v,s,h,j]=un(k);if(h!==bad)continue;let z=W*x,div=W**BigInt(j);assert(z%div===0n,"denominator");out+=z/div}
  }
  const counts=[];for(let k=0;k<=K;k++){counts.push(out%H);out/=H}return counts;
 }
 function check(n,E,children,D,K,k0,brute=true){
  const B=K+k0,q=B;assert(n>(B+1)*q||B===0,"promise size");
  // Parent star; each child vertex attaches only to parent leaves (all same bipartition), gauge y.
  const H=BigInt(2)**BigInt(n+children.length)+1n;
  const F=children.map(({scope,c,domain})=>({scope,eval:y=>domain.reduce((z,x)=>{let k=y.reduce((t,w,i)=>t+abs(c[i]+w-x),0);return z+(k<=K?H**BigInt(k):0n)},0n)}));
  let got=solve(D,E,F,K,B,q,H), expected=Array(K+1).fill(0n);
  if(brute){product([...D,...children.map(c=>c.domain)],x=>{stats.brute_assignments++;let k=E.reduce((z,[u,v,c,s])=>z+abs(c+s*(x[u]-x[v])),0);children.forEach((f,i)=>f.scope.forEach((v,j)=>k+=abs(f.c[j]+x[v]-x[n+i])));if(k<=K)expected[k]++});assert(got.every((x,i)=>x===expected[i]),"brute "+JSON.stringify({n,E,children,D,K,k0,got:got.map(String),expected:expected.map(String)}));stats.cases++}
  return got
 }
 let state=872;const rand=n=>{state=(Math.imul(state,1664525)+1013904223)>>>0;return state%n};
 for(let i=0;i<100;i++){
  let K=1+rand(2),k0=i%4===0?1:0;if(k0&&K===2)K=1;
  let B=K+k0,n=Math.max(5,(B+1)*B+1),E=Array.from({length:n-1},(_,j)=>[0,j+1,0,1]),children=[];
  for(let j=0;j<1+rand(4);j++){let leaves=[...Array(n-1)].map((_,v)=>v+1),scope=[];let len=1+rand(Math.min(3,n-1));for(let a=0;a<len;a++)scope.push(leaves.splice(rand(leaves.length),1)[0]);children.push({scope,c:scope.map(()=>0),domain:rand(5)===0?[1]:[0,1]})}
  if(k0)E[0][2]=i%8===0?-1:1;
  let D=Array.from({length:n},()=>rand(5)===0?[1]:[0,1]);check(n,E,children,D,K,k0)
 }
 // K=0, restricted domains and baseline-invalid child factors.
 check(5,Array.from({length:4},(_,j)=>[0,j+1,0,1]),[{scope:[1,2],c:[0,0],domain:[1]}],[[0,1],[0,1],[0,1],[0,1],[0,1]],0,0);
 let n=101,E=Array.from({length:100},(_,j)=>[0,j+1,0,1]),children=Array.from({length:100},(_,j)=>({scope:[j+1],c:[0],domain:[0,1]})),got=check(n,E,children,Array.from({length:n},()=>[0,1]),2,0,false);
 assert(got.map(String).join(",")==="2,400,39800","large");
 stats.large={parent_vertices:n,child_vertices:100,attachments:100,edges:200,K:2,counts:got.map(String)};
 return stats
}
console.log(JSON.stringify(verify872(),null,2));
```
