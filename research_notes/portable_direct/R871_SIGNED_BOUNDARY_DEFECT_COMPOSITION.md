# R871 — Boundary-conditioned signed defect tables and bounded-attachment tree composition

Date 2026-11-29 (Asia/Shanghai). AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED. Informed independent portable auxiliary integer model; no native BRC/Port attribution or shared task CLAIM. Own session recovery metadata confirmed EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91; execution_authorized=false. Current owner read r3-20261129-r871-running-read was RUNNING at last observation. Source predecessor full read: R870, 524f08e5fe50165d35f21cb0bf1dce8e7ee59368:research_notes/portable_direct/R870_BOUNDED_SEPARATION_DEFECT_POLYMERS.md. Reuse R869 signed lift and R870 connected-support log and cost kernel. Frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 and joint observer read; generated startup path returned 404; no repinning. Global main bcdf680c702f044462be567b7a3379f502bd8fac verified entry blobs, current research/role/worldview rules and global P000 V4 read. No changes to those inputs.

## 1. Model and local theorem

Loopless indexed multigraph G, explicit finite distinct integer domains D_v, arbitrary integer unary costs, each edge has target t_e. Given feasible reference X, define d_v=x_v-X_v and c_e=X_u+X_v-t_e. The global budget is S(d)=sum_e |c_e+d_u+d_v|<=K; k0=sum_e |c_e|<=K and B=K+k0<=2K. All feasible assignments satisfy V(d)=sum_e |d_u+d_v|<=B. The reference can be obtained using R868 decision/witness if not supplied. We retain original edge identities, domains, signs and inverse map x=X+d. Restrict any subset of vertex domains (e.g. to prescribed boundary labels) without changing X, c or B. In particular restricted domains need NOT contain zero. The theorem returns an exact histogram and one minimum-cost witness at EACH exact slack k=0..K. A table entry for a restricted instance is exact relative to its stated domain and edge set; no unrelated observer or future change of target is claimed.

Let H be any connected induced block with its internal edges and its own restricted domains. Use the global B (or any valid upper bound on internal V for all local solutions with internal slack<=K). In a bipartite block, choose signs s_u=-s_v on edges; the gauge y_v=s_v d_v has V=sum |y_u-y_v|. Assume H is (q,B)-edge-unbreakable: every cut of capacity<=B has a side of at most q vertices. Then R870 background/defect theorem holds unchanged, even if some restricted domains omit the reference. Its proof uses only V<=B, connectedness and unbreakability, not zero in every domain. If n>(B+1)q, there is a unique majority background r (B=0: all labels constant), with at most q exceptions. Enumerate r from the union of gauge domains. Baseline d_v=s_v r. Otherwise use signed-root bounded-offset enumeration below.

New nonbipartite case: form the signed double cover L with vertices (v,+),(v,-), two edges per original indexed edge between opposite signs. It is connected for connected nonbipartite H: paths lift and an odd closed walk changes the sheet. Lift label z(v,+)=d_v, z(v,-)=-d_v, so TV_L=2 V<=2B. Assume L is (q,2B)-edge-unbreakable. If 2n>(2B+1)q, deleting at most 2B unequal-label lift edges produces at most 2B+1 components. Some component has >q vertices; its cut has capacity<=2B, so complement has <=q. For B>=1 this component has >half the vertices (2n>3q); its constant label is the unique majority. The sheet involution negates labels, so unique majority implies it is 0. For B=0 connectedness gives constant z, hence also 0. Thus at most floor(q/2) ORIGINAL vertices have nonzero d. There is a zero vertex (strict size bound or B=0); along a path from it, ||d_u|-|d_v||<=|d_u+d_v| yields |d_v|<=B. This is an exact symmetry-forced zero background. It has no free scalar enumeration.

For either large case each connected component A of nonbackground original vertices has |A|<=Q (Q=q in bipartite case, floor(q/2) otherwise), boundary <=B and individual deviations within B of the baseline. Indeed every crossing edge has at least one unit of variation; the global sum is <=B. Components are proper. In the bipartite case the path bound is for gauge labels. Each candidate labelled component has v(P)=sum incident |d_u+d_v|>=1, with outside labels at baseline, and slack increment delta(P)=sum incident (|c_e+d_u+d_v|-|c_e|), so |delta(P)|<=v(P). Baseline obeys d_u+d_v=0 on every internal edge, including nonbipartite zero baseline. The set Hbad of vertices at which baseline violates restricted domains must be covered. Reject if |Hbad|>Q. Set baseline cost to 0 there, otherwise actual unary cost, and record h(P)=|A intersect Hbad| and cost increment.

As in R870, enumerate connected sets by deterministic include/exclude frontier search, bounded by Q+B decisions per root (excluded distinct vertices charge cut edges). At most A0=2^(Q+B+1)*max(1,2B)^Q candidates contain a fixed vertex. Conflict graph joins intersecting or adjacent supports; degree <=(Q+B)A0 because each support has at most B outside neighbors. Independent components have disjoint incident edge sets and their v,delta,h,cost increments add. Keep sum v<=B, k=k0_local+sum delta in [0,K], and sum h=|Hbad|. This is a bijection with local feasible assignments, per exact k. For bipartite backgrounds uniqueness is R870: an incorrectly chosen background would leave a defect component containing the true majority component and hence >Q. In nonbipartite case only baseline 0 is used. All signed residuals and original assignments recover from support labels and fixed background; costs and multiplicities are exact.

Use R870 truncated independent-set generating function with exponents (v,delta,h) and connected-support Mobius logarithm; all coefficients needed have t-degree<=B, |delta|<=B, h<=BQ. Formal exponentiation recovers exact counts. Cost kernel retains the cheapest (B-1)(Delta+1)+1 candidates of each (v,delta,h) type for B>=1 (B=0 has only empty set). The replacement proof preserves exact k and coverage, so applies separately to every k, not just global minimum. It cannot be used for counting; count uses all candidates. Return a min witness per k by storing selected labels and filling baseline elsewhere. This proves f(K,q)*poly(input) local histogram/min computation under the stated promise, including arbitrary domain pinning. No general recognition of unbreakability is assumed.

Small blocks: choose spanning-tree root w and signs s by alternating along tree (s_w=1). Every local solution obeys |d_v-s_v d_w|<=B by telescoping signed edge sums along tree paths. Enumerate root from explicit domain, and at most (2B+1) choices per other vertex. In the small branch size is <=(B+1)q (bipartite), or <=(2B+1)q/2 (nonbipartite). Check original edges and costs directly. Works with singleton blocks, arbitrary pinning, B=0 and signed integer domains.

## 2. Attachment signatures: a bounded-offset interface, not D^b

Given a partition into connected blocks, let attachment set A_i consist of distinct vertices incident with cross-block edges. Suppose |A_i|<=b, and the simple graph on blocks (join if at least one cross edge) is a tree. Cross edges may be parallel and children unbounded in number. Each block has the local unbreakability promise above (q uniform upper bound), or is within the corresponding small branch. If A_i is empty the signature is empty. Otherwise choose a boundary root a, choose tree signs in the block rooted there, and enumerate signatures by choosing d_a in its explicit domain and d_v in D_v intersect [s_v d_a-B,s_v d_a+B] for the remaining attachment vertices. This covers every feasible local assignment by the path bound and lists each signature once. Thus at most Dmax*(2B+1)^(b-1) signatures, rather than Dmax^b. The signs are just spanning-tree signs, so this bound also applies to nonbipartite blocks.

For each signature sigma, pin its attachment domains and run the local oracle; record N_i(sigma,k) and M_i(sigma,k) plus local witness. The original reference is intentionally NOT changed to satisfy the pins. For each adjacent block pair, let C_ij(sigma,tau) be the sum of actual |c_e+d_u+d_v| for all indexed cross edges. It is determined by their signatures; signed edge residuals can also be recovered individually. Root the block tree. The subtree message indexed by its root signature and total slack is obtained by sequentially merging children: for every parent signature, child signature, and pair of nonempty entries of slacks k,l, add N_parent*N_child to the entry at k+l+C_ij, and minimize M_parent+M_child there. Ignore slack>K. Charge all unary costs once at their original block, internal edges once locally, and every cross edge once at its merge. At the root sum counts and take minimum over root signatures. This is exact by induction: disjoint block assignments combine iff the signatures supply their cross costs, and each assignment fixes unique signatures and slack allocations. Backpointers yield one full original witness per k. The interface preserves correlation across multiple crossing edges and common attachment vertices; it does not treat their marginals independently.

If Smax=Dmax*max(1,2B+1)^(max(0,b-1)), all local table work is <= (#blocks)*Smax*f(K,q)*poly(input); cross computations and tree merges cost O(Smax^2*(K+1)^2*(#blocks + #cross_edges)) arithmetic operations as a safe upper bound, plus polynomial witness storage/recovery and exact integer bit complexity. Thus a supplied partition gives f(K,q,b)*poly(input), FPT in K alone when q,b are bounded by functions of K. Many children are allowed when the union of their attachment vertices is bounded. General partition existence or finding such a partition in FPT time is open here. Neither arbitrary tree decompositions nor a bound on total attachment count from per-child adhesion alone is asserted.

## 3. Necessary scalar anchor: a matching-interface obstruction

An interface independent of BOTH numerical domain size and the label anchor cannot in general preserve all extension queries. At K=0, take a one-vertex block with domain {0,...,D-1}, attach one outside vertex through x_u+x_v=0. For distinct internal labels a,b, the external singleton domain {-a} distinguishes them: a extends, b does not. Any deterministic interface label through which all these extension queries factor must have at least D classes. This does not rule out symbolic functions or compressed representations of tables, or FPT algorithms with polynomial dependence on explicit D. It shows why the preceding Dmax times bounded-offset representation is a meaningful scope-typed interface rather than claiming a parameter-only finite alphabet.

## 4. Exact author checks

The code below implements both local branches, candidate enumeration, connected-support logarithm, exact slack histograms with BigInt, per-slack cost kernels and tree composition, independently compared to brute original assignments. Small numeric labels/costs use exact safe integers. For the large test: two K7 cores with 30 leaves each, linked by two edges between distinct pairs of leaves; all domains {-1,0,1}, reference zero, unary cost -|d|, K=2. Each lifted K7 core is K7,7 minus a perfect matching: for a cut with smaller side s<=7, boundary >=6s-2 floor(s^2/4)>=6 for s>=1. Consequently cuts <=4 cannot split core; only <=4 lifted pendant leaves can be separated, proving q=4 for each lifted block. Since 74>(2*2+1)*4, zero-background theorem applies. Core labels are zero. There are 56 unpaired leaves (each nonzero contributes 1, two choices) and 2 joined pairs. Each pair has six configurations of total slack 2 (four single nonzero, two opposite nonzero), zero configuration at slack 0, two same-sign configurations at slack 4 excluded. Hence counts [1,112,4*C(56,2)+12]=[1,112,6172], min costs [0,-1,-2]. Large comparison is analytic, not exponential brute force. Original edge count 104; blocks each have two attachment vertices.

Actual output:
```json
{
  "local_cases": 82,
  "partition_cases": 70,
  "brute_assignments": 93214,
  "local_calls": 704,
  "small_calls": 653,
  "polymer_calls": 51,
  "signatures": 622,
  "candidates": 1067,
  "connected_supports": 1571,
  "merge_pairs": 658,
  "large": {
    "vertices": 74,
    "edges": 104,
    "blocks": 2,
    "K": 2,
    "counts": [
      "1",
      "112",
      "6172"
    ],
    "min_by_slack": [
      0,
      -1,
      -2
    ]
  }
}
```

Reproduce via Node or any compatible JavaScript engine:
```javascript
function verify871(){
 const assert=(x,m)=>{if(!x)throw Error(m)}, abs=Math.abs;
 const stats={local_cases:0,partition_cases:0,brute_assignments:0,local_calls:0,small_calls:0,polymer_calls:0,signatures:0,candidates:0,connected_supports:0,merge_pairs:0,large:null};
 const prod=(D,cb,a=[])=>{if(a.length===D.length){cb(a);return}for(const x of D[a.length]){a.push(x);prod(D,cb,a);a.pop()}};
 const slack=(E,x)=>E.reduce((s,[u,v,c])=>s+abs(c+x[u]+x[v]),0);
 const cost=(C,x)=>x.reduce((s,z,i)=>s+C[i].get(z),0);
 const empty=K=>Array.from({length:K+1},()=>({n:0n,m:Infinity,w:null}));
 function put(row,k,n,m,w){if(k>=row.length||k<0)return;row[k].n+=n;if(m<row[k].m){row[k].m=m;row[k].w=w.slice()}}
 function graph(n,E,root=0){const A=Array.from({length:n},()=>new Set()),s=Array(n).fill(0);for(const [u,v] of E){A[u].add(v);A[v].add(u)}s[root]=1;const q=[root];let bip=true;for(let i=0;i<q.length;i++){const u=q[i];for(const v of A[u]){if(!s[v]){s[v]=-s[u];q.push(v)}else if(s[v]===s[u])bip=false}}assert(q.length===n,"connected");return {A,s,bip}}
 function local(D,C,E,K,B,q){
  stats.local_calls++;let n=D.length,out=empty(K),k0=E.reduce((s,e)=>s+abs(e[2]),0);
  if(D.some(d=>!d.length))return out;
  let {A,s,bip}=graph(n,E);
  const record=x=>{let k=slack(E,x);if(k<=K)put(out,k,1n,cost(C,x),x)};
  if((bip?n:2*n)<=(bip?B+1:2*B+1)*q){
   stats.small_calls++;for(const r of D[0])prod(D.map((d,i)=>i?d.filter(x=>abs(x-s[i]*r)<=B):[r]),record);return out;
  }
  stats.polymer_calls++;
  const qeff=bip?q:Math.floor(q/2),sets=new Map();
  for(let root=0;root<n&&qeff>0;root++){
   function go(S,F){let cut=0;for(const [u,v] of E)if(S.has(u)&&F.has(v)||S.has(v)&&F.has(u))cut++;if(cut>B||S.size>qeff)return;
    let z=-1;for(const u of S){for(const v of A[u])if(!S.has(v)&&!F.has(v)){z=v;break}if(z>=0)break}
    if(z<0){if(S.size<n){let a=[...S].sort((a,b)=>a-b);sets.set(a.join(","),a)}return}
    if(S.size<qeff){S.add(z);go(S,F);S.delete(z)}F.add(z);go(S,F);F.delete(z)
   }go(new Set([root]),new Set())
  }
  const rs=bip?[...new Set(D.flatMap((d,i)=>d.map(x=>s[i]*x)))]:[0];
  for(const r of rs){
   const base=s.map(t=>t*r),bad=D.map((d,i)=>!d.includes(base[i])),nb=bad.filter(Boolean).length;if(nb>qeff)continue;
   const bc=C.reduce((a,c,i)=>a+(c.get(base[i])??0),0),P=[];
   for(const a of sets.values()){
    const S=new Set(a),near=new Set(a);for(const u of a)for(const v of A[u])near.add(v);
    prod(a.map(u=>D[u].filter(x=>x!==base[u]&&abs(x-base[u])<=B)),vals=>{
     const x=new Map(a.map((u,i)=>[u,vals[i]]));let v=0,d=0;
     for(const [u,w,c] of E)if(S.has(u)||S.has(w)){let t=(x.get(u)??base[u])+(x.get(w)??base[w]);v+=abs(t);d+=abs(c+t)-abs(c)}
     if(v===0||v>B)return;const h=a.filter(u=>bad[u]).length,dc=a.reduce((z,u,i)=>z+C[u].get(vals[i])-(C[u].get(base[u])??0),0);
     P.push({a,near,vals:vals.slice(),v,d,h,dc})
    })
   }
   stats.candidates+=P.length;
   const G=P.map(()=>new Set()),by=Array.from({length:n},()=>[]);P.forEach((p,i)=>p.a.forEach(u=>by[u].push(i)));P.forEach((p,i)=>{for(const u of p.near)for(const j of by[u])if(j!==i)G[i].add(j)});
   const key=(v,d,h)=>`${v},${d},${h}`,un=k=>k.split(",").map(Number),zero=key(0,0,0),one=new Map([[zero,1n]]);
   const add=(m,k,a)=>{let b=(m.get(k)??0n)+a;if(b)m.set(k,b);else m.delete(k)};
   const mul=(a,b)=>{let m=new Map();for(const [ka,x] of a)for(const [kb,y] of b){let [v,d,h]=un(ka),[w,e,f]=un(kb);if(v+w<=B)add(m,key(v+w,d+e,h+f),x*y)}return m};
   let F=1n;for(let j=1;j<=B;j++)F*=BigInt(j);
   function zLocal(S){const Z=new Map(one);function rec(i,T,v,d,h){for(let j=i;j<S.length;j++){let a=S[j],p=P[a];if(v+p.v>B||T.some(b=>G[a].has(b)))continue;add(Z,key(v+p.v,d+p.d,h+p.h),1n);rec(j+1,[...T,a],v+p.v,d+p.d,h+p.h)}}rec(0,[],0,0,0);return Z}
   function log(S){let Z=zLocal(S);Z.delete(zero);let L=new Map(),pow=new Map(one);for(let j=1;j<=B;j++){pow=mul(pow,Z);if(!pow.size)break;let f=(j%2?1n:-1n)*F/BigInt(j);for(const [k,a] of pow)add(L,k,f*a)}return L}
   const seen=new Set(),L=new Map();
   function conn(S){let a=[...S].sort((a,b)=>a-b),id=a.join(",");if(seen.has(id))return;seen.add(id);stats.connected_supports++;
    function sub(i,T){if(i===a.length){if(!T.length)return;let sign=(a.length-T.length)%2?-1n:1n;for(const [k,x] of log(T))add(L,k,sign*x);return}sub(i+1,T);sub(i+1,[...T,a[i]])}sub(0,[]);
    if(S.size<B){let near=new Set();for(const u of S)for(const v of G[u])if(!S.has(v))near.add(v);for(const v of near)conn(new Set([...S,v]))}
   }
   if(B>0)for(let i=0;i<P.length;i++)conn(new Set([i]));
   const Z=new Map(one);for(let v=1;v<=B;v++){let row=new Map();for(const [k,a] of L){let [j,d,h]=un(k);for(const [l,b] of Z){let [w,e,f]=un(l);if(j+w===v)add(row,key(v,d+e,h+f),BigInt(j)*a*b)}}for(const [k,a] of row){let div=F*BigInt(v);assert(a%div===0n&&a/div>=0n,"integer coefficient");if(a)Z.set(k,a/div)}}
   for(const [k,a] of Z){let [v,d,h]=un(k),j=k0+d;if(h===nb&&j>=0&&j<=K)out[j].n+=a}
   let deg=G.reduce((a,g)=>Math.max(a,g.size),0),L0=Math.max(1,(B-1)*(deg+1)+1),types=new Map();
   P.forEach((p,i)=>{let t=key(p.v,p.d,p.h);if(!types.has(t))types.set(t,[]);types.get(t).push(i)});
   let U=[...types.values()].flatMap(a=>a.sort((i,j)=>P[i].dc-P[j].dc||i-j).slice(0,L0)).sort((a,b)=>a-b);
   function opt(i,S,v,d,h,c){let k=k0+d;if(h===nb&&k>=0&&k<=K&&bc+c<out[k].m){let w=base.slice();for(const a of S)P[a].a.forEach((u,j)=>w[u]=P[a].vals[j]);out[k].m=bc+c;out[k].w=w}
    for(let j=i;j<U.length;j++){let a=U[j],p=P[a];if(v+p.v>B||h+p.h>nb||S.some(b=>G[a].has(b)))continue;opt(j+1,[...S,a],v+p.v,d+p.d,h+p.h,c+p.dc)}
   }opt(0,[],0,0,0,0)
  }
  for(let k=0;k<=K;k++){let a=out[k];assert((a.n>0n)===(a.w!==null),"count/witness");if(a.w)assert(a.w.every((x,i)=>D[i].includes(x))&&slack(E,a.w)===k&&cost(C,a.w)===a.m,"local inverse")}
  return out
 }
 function partition(D,C,E,blocks,K,qs){
  const n=D.length,B=K+E.reduce((a,e)=>a+abs(e[2]),0),id=Array(n).fill(-1),loc=Array(n).fill(-1);
  blocks.forEach((a,i)=>a.forEach((v,j)=>{assert(id[v]<0,"partition");id[v]=i;loc[v]=j}));assert(id.every(i=>i>=0),"coverage");
  const I=blocks.map(()=>[]),X=blocks.map(()=>new Map()),bd=blocks.map(()=>new Set());
  for(const [u,v,c] of E){let i=id[u],j=id[v];if(i===j)I[i].push([loc[u],loc[v],c]);else{bd[i].add(loc[u]);bd[j].add(loc[v]);if(!X[i].has(j))X[i].set(j,[]);if(!X[j].has(i))X[j].set(i,[]);X[i].get(j).push([loc[u],loc[v],c]);X[j].get(i).push([loc[v],loc[u],c])}}
  assert(X.reduce((a,x)=>a+x.size,0)===2*(blocks.length-1),"tree edges");
  const tables=blocks.map((a,i)=>{
   let ds=a.map(u=>D[u]),cs=a.map(u=>C[u]),bb=[...bd[i]].sort((a,b)=>a-b),rows=[];
   function make(vals){stats.signatures++;let pin=new Map(bb.map((u,j)=>[u,vals[j]])),dom=ds.map((d,u)=>pin.has(u)?[pin.get(u)]:d);let sig=Array(a.length).fill(null);bb.forEach((u,j)=>sig[u]=vals[j]);let z=local(dom,cs,I[i],K,B,qs[i]);if(z.some(e=>e.n>0n))rows.push({sig,z})}
   if(!bb.length)make([]);else{let root=bb[0],s=graph(a.length,I[i],root).s;for(const r of ds[root])prod(bb.map(u=>u===root?[r]:ds[u].filter(x=>abs(x-s[u]*r)<=B)),make)}
   return rows
  });
  const seen=new Set();
  function visit(i,p){assert(!seen.has(i),"cycle");seen.add(i);
   let T=tables[i].map(({sig,z})=>({sig,z:z.map(e=>({n:e.n,m:e.m,w:e.w?Object.fromEntries(blocks[i].map((u,j)=>[u,e.w[j]])):null}))}));
   for(const [j,edges] of X[i])if(j!==p){const U=visit(j,i);for(const a of T){const next=empty(K);for(const b of U){stats.merge_pairs++;const c=edges.reduce((z,[u,v,e])=>z+abs(e+a.sig[u]+b.sig[v]),0);for(let k=0;k<=K;k++)if(a.z[k].n)for(let l=0;k+l+c<=K;l++)if(b.z[l].n){let t=next[k+l+c],aa=a.z[k],bb=b.z[l];t.n+=aa.n*bb.n;if(aa.m+bb.m<t.m){t.m=aa.m+bb.m;t.w={...aa.w,...bb.w}}}}a.z=next}}
   return T
  }
  let T=visit(0,-1);assert(seen.size===blocks.length,"tree connected");let out=empty(K);
  for(const a of T)for(let k=0;k<=K;k++){let x=a.z[k];if(x.n){out[k].n+=x.n;if(x.m<out[k].m){out[k].m=x.m;out[k].w=Array.from({length:n},(_,u)=>x.w[u])}}}
  for(let k=0;k<=K;k++)if(out[k].n){let w=out[k].w;assert(w.every((x,i)=>D[i].includes(x))&&slack(E,w)===k&&cost(C,w)===out[k].m,"global inverse")}
  return out
 }
 function brute(D,C,E,K){let out=empty(K);prod(D,x=>{stats.brute_assignments++;let k=slack(E,x);if(k<=K)put(out,k,1n,cost(C,x),x)});return out}
 function compare(a,b){assert(a.length===b.length&&a.every((x,i)=>x.n===b[i].n&&x.m===b[i].m),"hist/opt mismatch")}
 function promise(n,E,B,q){let g=graph(n,E),N=g.bip?n:2*n,EE=g.bip?E:E.flatMap(([u,v,c])=>[[u,v+n,c],[v,u+n,c]]),T=g.bip?B:2*B;assert(N<=20,"promise test size");
  for(let m=1;m<(1<<N)-1;m++){let k=0;for(let x=m;x;x&=x-1)k++;if(Math.min(k,N-k)<=q)continue;assert(EE.filter(([u,v])=>((m>>u)^(m>>v))&1).length>T,"unbreakability")}
 }
 let seed=8712026;function rand(n){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%n}
 function domains(n){let D=Array.from({length:n},()=>[...new Set([0,rand(5)-2,rand(5)-2])]),C=D.map(d=>new Map(d.map(x=>[x,rand(13)-6])));return [D,C]}
 function clique(n){let E=[];for(let u=0;u<n;u++)for(let v=u+1;v<n;v++)E.push([u,v,0]);return E}
 for(let i=0;i<70;i++){let n=3+rand(5),K=rand(3),E=i%2?clique(n):Array.from({length:n-1},(_,j)=>[0,j+1,0]);if(K&&i%4===0)E[0][2]=1;let B=K+E.reduce((a,e)=>a+abs(e[2]),0),[D,C]=domains(n),q=i%2?2*n:B;
  if(i%3===0){let v=rand(n);D[v]=[D[v][rand(D[v].length)]]}
  if(!(i%2))promise(n,E,B,q);
  compare(local(D,C,E,K,B,q),brute(D,C,E,K));stats.local_cases++
 }
 // Explicit lifted unbreakability, including pinned-away reference values.
 for(let i=0;i<12;i++){let n=7+2,K=1,B=1,E=clique(7).concat([[0,7,0],[1,8,0]]),q=2,[D,C]=domains(n);if(i%2===0)D[7]=[D[7][D[7].length-1]];if(i===0)promise(n,E,B,q);compare(local(D,C,E,K,B,q),brute(D,C,E,K));stats.local_cases++}
 for(let i=0;i<70;i++){let sizes=[2+rand(2),2+rand(2),2+rand(2)],blocks=[],E=[],off=0;
  for(const n of sizes){blocks.push(Array.from({length:n},(_,j)=>off+j));for(let u=0;u<n;u++)for(let v=u+1;v<n;v++)E.push([off+u,off+v,0]);off+=n}
  for(let j=1;j<blocks.length;j++){let a=blocks[j-1],b=blocks[j];E.push([a[0],b[0],0]);if(i%2===0)E.push([a[a.length-1],b[b.length-1],0]);if(i%5===0)E.push([a[0],b[0],0])}
  let K=rand(3);if(K&&i%3===0)E[rand(E.length)][2]=1;let [D,C]=domains(off);compare(partition(D,C,E,blocks,K,sizes.map(n=>2*n)),brute(D,C,E,K));stats.partition_cases++
 }
 // Two lifted-unbreakable nonbipartite blocks, each K7 plus 30 pendant vertices.
 let blocks=[Array.from({length:37},(_,i)=>i),Array.from({length:37},(_,i)=>37+i)],E=[];
 for(const a of blocks){E.push(...clique(7).map(([u,v,c])=>[a[u],a[v],c]));for(let j=7;j<37;j++)E.push([a[(j-7)%7],a[j],0])}
 E.push([7,44,0],[8,45,0]);let D=Array.from({length:74},()=>[-1,0,1]),C=D.map(d=>new Map(d.map(x=>[x,-abs(x)]))),z=partition(D,C,E,blocks,2,[4,4]);assert(z.map(x=>String(x.n)).join(",")==="1,112,6172","large count");assert(z.map(x=>x.m).join(",")==="0,-1,-2","large min");stats.large={vertices:74,edges:E.length,blocks:2,K:2,counts:z.map(x=>String(x.n)),min_by_slack:z.map(x=>x.m)};
 return stats
}
console.log(verify871());
```

## 5. Next

Find or refute a K-controlled decomposition into connected blocks with bounded total distinct attachment vertices and unbreakable signed lifts; investigate general small-adhesion tree decompositions with unbounded attachment unions, where child messages could be compiled into defect interactions without enumerating a product of all boundary values. A general K-only exact counting and arbitrary unary cost theorem remains open. Native BRC/Port relation and three-dimensional slice correspondence remain open; this is only an auxiliary integer graph result. No proof of novelty beyond this line's scoped advance or independent review is claimed.
