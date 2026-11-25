# R799 — Universal bipartite cycle overlap and exact mixed-moment counting hardness

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable research, own verified session metadata recovered (Researcher EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91); no own run and execution_authorized=false. Owner inventory request r3-20261126-0019-owner-read: SUCCEEDED at pre-publication observation; this read does not grant a claim. No shared Task/CLAIM/Result/Review change. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 and joint-observer contract read; frozen Heartbeat companion returned 404. ACTIVE worldview and current rules consulted; canonical global main entry snapshot 6f3d1effa3f7cd7ca313430455a64a4db53f1ddd. Unsigned integer Port auxiliary branch-count observer only, with source and provenance retained.

Sources: R795 1a2471a8b10ac6f0a8d7eadeb05f27def385aff3:research_notes/portable_direct/R795_INTRINSIC_FIXED_RANK_PORT_SELECTOR.md; R796 3e7108d2ba1a0d36a83957d6c01f9e493029eedb:research_notes/portable_direct/R796_EXACT_LIFT_FIBER_AND_MINIMAL_SELECTOR.md; R798 2e9d7f8540edc05f8b2569278333d467cdcb2855:research_notes/portable_direct/R798_COMMON_PREFIX_JOINT_LIFT_SPECTRUM.md.

## 1. Realization theorem

Let B=(L,R,F) be ANY finite simple bipartite graph, q=|F| and i number of isolated vertices. Construct a simple source graph G with one distinct directed-marked edge (p_f,q_f) for every f in F; all 2q endpoints distinct. For each nonisolated vertex v of B order its incident edges cyclically f_1,...,f_d. Connect q_{f_j} to p_{f_{j+1}} by a length-two path with a fresh middle vertex, including the wraparound. Middle vertices are distinct for all v,j. This forms a simple directed-marked cycle C_v of length 3d, including d=1. For isolated vertices use a disjoint triangle. Same-side cycles are vertex-disjoint; opposite-side cycles share exactly the marked edge iff adjacent in B, and never share a connector edge. G has 4q+3i vertices and 5q+3i edges, maximum degree 3 (marked-edge endpoints have degree 3, connector vertices and isolated triangles degree 2). No loops or parallel edges.

Use the R795 construction on G. For side j define selected boundary S_j as all public vertices of its cycles plus all private a_e for source edges not in its cycles (A-twist as in R795). Since each family consists of disjoint cycles, number of selected public vertices equals number of active public edge-slots, hence |S_j|=m. At the all-flexible prefix each active component is exactly its designated cycle: every other source edge is selected privately even if it touches public labels. The R796 two orientations exist. Thus the R798 overlap graph of the pair is precisely B, with a single shared slot per edge. All cycles can be oriented so their + directions agree at each shared slot: use p_f -> q_f in both families. This construction retains source edge identity, two boundary labels and all prefix variables. It follows that the full class of two-boundary overlap graphs is exactly all finite simple bipartite graphs (after merging parallel interactions as in R798). In particular K_{r,r} gives unbounded overlap treewidth despite source maximum degree 3. This is a structural characterization, not a claim that all individual realizations have large width.

## 2. Exact uniform mixed first moment

Let H_{12}(2,2)=sum_x L_1(x)L_2(x), with all independent prefix weights 1. The R795 local counts (u,v,a) at x=3,5,6 are respectively (1,1,2),(0,1,1),(1,0,1). At z_1=z_2=2, star factors in R798 vanish; each cycle orientation is a binary variable. A private/public connector slot contributes 2+1=3 to the sum over its three prefixes, regardless of direction. A shared slot contributes 2 if the two orientation demands agree and 1 if they disagree. Thus with m=|E(G)|,

H_{12}(2,2)=3^(m-q) Z_B(2), where Z_B(2)=sum_{sigma in {0,1}^{V(B)}} 2^(number of monochromatic edges).

This is exact also for isolated cycles. It is the zero-field two-spin ferromagnetic partition sum at fixed integer coupling. No analytic approximation, signed native cancellation, or marginal independence assumption is used. Single-boundary spectrum factors remain easy by R797 even when this pair is difficult.

## 3. Self-contained polynomial-time Turing reduction from exact independent-set counting

Let J be an arbitrary simple graph with n vertices, m0 edges, d(v) degrees; set M=2m0+1. Add an apex r and M d(v) parallel edges from r to v, retaining every original edge once, giving multigraph J' with N=m0+2M m0 edges. Parallel edges here are an intermediate counting device only. Define cut polynomial P(t)=sum_{sigma on V(J')} t^(cut_{J'}(sigma)). Its degree <=N. For the cut side S not containing r, let c=|delta_J(S)| and D=sum_{v in S}d(v). The cut exponent is c+M D with 0<=c<=m0<M. Since c=D-2|E(J[S])|, S is independent iff c=D. Thus the exact number of independent sets is half the sum of coefficients of P whose index j satisfies j mod M = floor(j/M). The factor 1/2 removes the two complementary spin assignments. This also handles isolated vertices and m0=0.

For k=1,...,N+1 replace each individual edge of J' by k separate two-edge paths with fresh middle vertices; the resulting B_k is a simple bipartite graph with all original vertices on one side. Each path's internal spin sum for Z(2) is 5 if the endpoint spins agree and 4 otherwise (2*2+1*1 vs 2*1+1*2). Hence Z_{B_k}(2)=5^(kN) P((4/5)^k). Use the realization above to evaluate each Z from a uniform Port mixed moment by exact division by 3^(|E(G_k)|-|E(B_k)|). The N+1 rational arguments are distinct; exact polynomial interpolation recovers P. Graph sizes, number of calls and bit lengths are polynomial in the original input (including the exact integer outputs and rational interpolation data). This proves a polynomial-time Turing reduction from #IS, known #P-complete (e.g. Goldberg, Lapinskas, Richerby, arXiv:2005.05070, https://arxiv.org/abs/2005.05070). Membership in #P: guess an actual prefix and two full binary lifts, verify each against its fixed boundary and local constraints. Thus exact uniform H_{12}(2,2) is #P-complete under polynomial-time Turing reductions, even on the constructed R795 subcubic source graphs and with only two fixed boundaries. This concerns exact evaluation, not approximation or all special instances. No hardness claim for H(1,1) follows here.

## 4. Exact finite verification

The script derives the selector table from 384 literal XOR assignments. It constructs every labeled bipartite overlap on part sizes (1,1),(1,2),(2,1),(2,2),(2,3),(3,3), including empty graphs; verifies source simplicity, vertex-disjoint cycles within each side, edge order and exact overlap. It compares direct orientation-pair contraction using the local count table to the spin sum formula. For four small cases, it additionally enumerates ALL actual prefixes and counts lifts by direct endpoint assignment recursion with boundary label uniqueness, using the proved R795 count-tree semantics; it does not re-enumerate every expanded count-tree bit. Independently verifies the cut decoding on all labeled simple J of 1..5 vertices, and the path factor for all four spin pairs. No implementation of rational interpolation is required for the analytic reduction, and none is claimed as executed. BigInt for exact moments.

Actual output:
```json
{
  "table": [
    [
      1,
      1,
      2
    ],
    [
      0,
      1,
      1
    ],
    [
      1,
      0,
      1
    ]
  ],
  "graphs": 602,
  "momentChecks": 602,
  "prefixChecks": 119070,
  "prefixCases": [
    {
      "a": 1,
      "b": 1,
      "q": 0,
      "m": 6,
      "prefixes": 729,
      "moment": "2916"
    },
    {
      "a": 1,
      "b": 1,
      "q": 1,
      "m": 5,
      "prefixes": 243,
      "moment": "486"
    },
    {
      "a": 1,
      "b": 2,
      "q": 2,
      "m": 10,
      "prefixes": 59049,
      "moment": "118098"
    },
    {
      "a": 2,
      "b": 1,
      "q": 2,
      "m": 10,
      "prefixes": 59049,
      "moment": "118098"
    }
  ],
  "complete": [
    {
      "a": 1,
      "b": 1,
      "q": 1,
      "n": 4,
      "m": 5,
      "moment": "486"
    },
    {
      "a": 2,
      "b": 2,
      "q": 4,
      "n": 16,
      "m": 20,
      "moment": "3529831122"
    },
    {
      "a": 3,
      "b": 3,
      "q": 9,
      "n": 36,
      "m": 45,
      "moment": "413360625607935579234"
    }
  ],
  "cutGraphs": 1099,
  "cutMasks": 33866,
  "pathChecks": 4,
  "mismatches": 0
}
```

```javascript
function verify(){
 const table=[];
 for(const x of [3,5,6]){let row=[0,0,0];for(let b=0;b<128;b++){let [s,t,j,k,u,v,a]=Array.from({length:7},(_,i)=>b>>i&1);let z=[s+2*t,s+2*u+4*j,t+2*v+4*k,j+2*k+4*a];if(z.every(y=>[0,3,5,6].includes(y))&&z[0]!=(x^5)&&z[1]!=3&&z[2]!=6&&z[3]!=6){let v1=u+2*v+4*(a^1);if(![1,2,4].includes(v1))throw Error("extra local state");row[[1,2,4].indexOf(v1)]++}}table.push(row)}
 if(JSON.stringify(table)!=="[[1,1,2],[0,1,1],[1,0,1]]")throw Error("local table");
 function realize(a,b,B){
  let n=0,E=[],C=[[],[]],shared=[];
  const vertex=()=>n++;
  const add=(u,v)=>{let i=E.length;E.push([u,v]);return i};
  for(const [l,r] of B){let u=vertex(),v=vertex();shared.push(add(u,v));}
  for(let side=0;side<2;side++)for(let i=0;i<[a,b][side];i++){
   let ids=B.map((_,j)=>j).filter(j=>B[j][side]===i),edges=[],verts=[];
   if(!ids.length){let u=vertex(),v=vertex(),w=vertex();verts=[u,v,w];edges=[add(u,v),add(v,w),add(w,u)]}
   else for(let j=0;j<ids.length;j++){let idx=ids[j],nx=ids[(j+1)%ids.length], [u,v]=E[shared[idx]], [un]=E[shared[nx]],w=vertex();verts.push(u,v,w);edges.push(shared[idx],add(v,w),add(w,un));}
   C[side].push({edges,verts});
  }
  const iso=C.flat().filter(c=>c.edges.length===3).length; // includes degree-one cycles, not used
  if(new Set(E.map(([u,v])=>[Math.min(u,v),Math.max(u,v)].join(","))).size!==E.length||E.some(([u,v])=>u===v))throw Error("not simple");
  const pub=C.map(cs=>new Set(cs.flatMap(c=>c.verts))),active=C.map(cs=>new Set(cs.flatMap(c=>c.edges)));
  for(let s=0;s<2;s++){if(pub[s].size!==active[s].size||pub[s].size!==C[s].reduce((q,c)=>q+c.verts.length,0))throw Error("boundary");for(const c of C[s])for(let j=0;j<c.edges.length;j++){let e=E[c.edges[j]],u=c.verts[j],v=c.verts[(j+1)%c.verts.length];if(e[0]!==u||e[1]!==v)throw Error("cycle adjacency")}}
  let overlap=[];for(let i=0;i<a;i++)for(let j=0;j<b;j++){let common=C[0][i].edges.filter(e=>C[1][j].edges.includes(e));if(common.length>1)throw Error("multiple shared");if(common.length)overlap.push([i,j]);}
  if(JSON.stringify(overlap)!==JSON.stringify(B))throw Error("overlap");
  return {n,E,C,pub,active};
 }
 function factorMoment(R){
  let N=R.C[0].length+R.C[1].length,m=R.E.length,result=0n,owner=R.C.map(cs=>Array.from({length:m},(_,e)=>cs.findIndex(c=>c.edges.includes(e))));
  for(let x=0;x<2**N;x++){let q=1n;for(let e=0;e<m;e++){let i=owner[0][e],j=owner[1][e],sum=0;
    for(let p=0;p<3;p++){let u=i<0?2:(x>>i&1),v=j<0?2:(x>>(R.C[0].length+j)&1);sum+=table[p][u]*table[p][v];}
    q*=BigInt(sum);
   }result+=q;}
  return result;
 }
 function expected(a,b,B,m){
  let s=0n;for(let x=0;x<2**(a+b);x++){let k=0;for(let [i,j] of B)if((x>>i&1)===(x>>(a+j)&1))k++;s+=2n**BigInt(k)}return s*3n**BigInt(m-B.length);
 }
 function exactPrefix(R){
  let m=R.E.length,N=3**m,sum=0n;const p=Array(m).fill(0);
  function count(s,e,used){if(e===m)return 1;let [u,v]=R.E[e],row=table[p[e]];
   if(!R.active[s].has(e))return row[2]*count(s,e+1,used);
   let c=0;if(row[0]&&R.pub[s].has(u)&&!(used&(1<<u)))c+=row[0]*count(s,e+1,used|(1<<u));if(row[1]&&R.pub[s].has(v)&&!(used&(1<<v)))c+=row[1]*count(s,e+1,used|(1<<v));return c;
  }
  for(let k=0;k<N;k++){let t=k;for(let e=0;e<m;e++){p[e]=t%3;t=Math.floor(t/3)}sum+=BigInt(count(0,0,0)*count(1,0,0))}
  return {N,sum};
 }
 let graphs=0,momentChecks=0,prefixChecks=0,prefixCases=[],complete=[];
 for(const [a,b] of [[1,1],[1,2],[2,1],[2,2],[2,3],[3,3]]){
  let P=[];for(let i=0;i<a;i++)for(let j=0;j<b;j++)P.push([i,j]);
  for(let mask=0;mask<2**P.length;mask++){
   let B=P.filter((_,i)=>mask>>i&1),R=realize(a,b,B),want=expected(a,b,B,R.E.length),got=factorMoment(R);
   if(want!==got)throw Error("moment");
   graphs++;momentChecks++;
   if((a===1&&b===1)||(a===1&&b===2&&mask===3)||(a===2&&b===1&&mask===3)){let t=exactPrefix(R);if(t.sum!==want)throw Error("prefix mismatch");prefixChecks+=t.N;prefixCases.push({a,b,q:B.length,m:R.E.length,prefixes:t.N,moment:String(want)});}
   if(mask===2**P.length-1&&a===b)complete.push({a,b,q:B.length,n:R.n,m:R.E.length,moment:String(want)});
  }
 }
 let cutGraphs=0,cutMasks=0,pathChecks=0;
 for(let n=1;n<=5;n++){
  let P=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)P.push([i,j]);
  for(let mask=0;mask<2**P.length;mask++){let E=P.filter((_,i)=>mask>>i&1),m=E.length,M=2*m+1,d=Array(n).fill(0);for(const [u,v] of E){d[u]++;d[v]++}
   let hist=new Map,ind=0;
   for(let x=0;x<2**n;x++){let c=0,h=0;for(const [u,v] of E)if((x>>u&1)!==(x>>v&1))c++;for(let i=0;i<n;i++)if(x>>i&1)h+=d[i];let e=c+M*h;hist.set(e,(hist.get(e)||0)+2);if(E.every(([u,v])=>!(x>>u&1)||!(x>>v&1)))ind++;cutMasks++}
   let got=0;for(const [e,v] of hist)if(e%M===Math.floor(e/M))got+=v/2;if(got!==ind)throw Error("cut decoder");cutGraphs++;
  }
 }
 for(let u=0;u<2;u++)for(let v=0;v<2;v++){let s=0;for(let w=0;w<2;w++)s+=(u===w?2:1)*(v===w?2:1);if(s!==(u===v?5:4))throw Error("subdivision");pathChecks++}
 return {table,graphs,momentChecks,prefixChecks,prefixCases,complete,cutGraphs,cutMasks,pathChecks,mismatches:0};
}
console.log(JSON.stringify(verify(),null,2));
```

## 5. Next
Investigate exact algorithms for the relevant finite-width families beyond forests, especially positive-moment contraction using two states instead of three, and whether the feasibility-only H(1,1) admits a distinct tractability/hardness boundary. Preserve the shared prefix carrier and native signed BRC / event order / common-depth residuals separately. This proof is a mathematical author result, not an accepted formal Result.
