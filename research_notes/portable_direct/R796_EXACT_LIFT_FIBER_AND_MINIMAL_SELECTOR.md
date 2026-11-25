# R796 — Exact lift-fiber coordinates and sharp four-node selector size

2026-11-25. AUTHOR_ANALYTIC_PROOF_WITH_EXACT_FINITE_CERTIFICATE / NOT_REVIEWED. Independent portable continuation; no Task/CLAIM/Result/Review change. Existing researcher EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91; own registration metadata recovered, no RUN and execution_authorized=false. Owner query r3-20261125-2122-owner-read last observed RUNNING (read job status, not an owner). Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389 P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer contract 3923890d77a02d84b772f789e6912dd14f220d14 read. Frozen generated package and Heartbeat companion unavailable (404). ACTIVE worldview and current portable/continuation rules consulted; global entry blobs matched immutable main 26e490984a0f5be1fef6e89440b2dc6d779c50dc.

Exact sources:
- 1a2471a8b10ac6f0a8d7eadeb05f27def385aff3:research_notes/portable_direct/R795_INTRINSIC_FIXED_RANK_PORT_SELECTOR.md
- 3782f55c36083bcda76cf4020eb846b033b0b971:research_notes/portable_direct/R779_FOUR_CUT_PAIRED_EXCHANGE.md
- 6dcc39ca328ee24ca8493100a27cc1bf209b7446:research_notes/portable_direct/R792_SHARED_PORT_PREFIX_VERTEX_COVER.md

## 1. Exact multiplicity and provenance coordinate for R795

Population: all full binary lift edge assignments of the NEW R795 fixed-rank network, for one fixed prefix x and selected boundary S=A xor D, where A is the set of private labels a_e, G=(V,E) is a finite simple graph, m=|E|. The label count trees are exactly the R792 ones (one internal bit assignment given selected incidences, as each subtree count is the sum of its leaves). Each R795 selector has local count on (u,v,a) of (1,1,2) for prefix 3, (0,1,1) for prefix 5, and (1,0,1) for prefix 6, verified directly on all 128 edge configurations per prefix. There are no other local outputs. This is the unsigned unweighted branch-count carrier, not physical signed/amplitude BRC.

Write P={e:a_e in S}, U=S intersect V. If |S|!=m the fiber is empty. Otherwise form a graph H on U. For every e not in P, intersect the admitted public endpoints of e at its prefix with U. If none, the fiber is empty. If both, add an ordinary edge to H; if exactly one, put one distinct stub at that endpoint. All vertices of U, including isolated ones, must be included. Let f be the number of e in P with prefix 3. For each connected component C of H let v_C,e_C,h_C be its vertex, ordinary-edge, and stub counts.

**Theorem.** The fiber is empty iff an empty endpoint row occurs or at least one component has e_C+h_C != v_C (or |S|!=m). Otherwise every component is a tree with one stub or a unicyclic component without stubs. If c is the number of unicyclic components, the number of full lifts equals 2^(f+c).

Proof: each edge-slot not already paid privately must select exactly one admissible public endpoint, and every public vertex in U must be selected exactly once. Orient every ordinary edge toward its selected endpoint, treat each stub as already pointing to its unique vertex. The required total incoming count per vertex is one. Hence e_C+h_C=v_C necessary. Connectedness gives e_C>=v_C-1; nonnegative h_C leaves only e_C=v_C-1,h_C=1 or e_C=v_C,h_C=0. In the first case orient all edges away from the unique stub root: each other vertex has a unique parent, giving one solution, necessarily so by propagating away from the occupied root. In the second case orient the unique cycle consistently in either direction, and orient every attached tree away from the cycle. These are the only solutions (remove leaves, whose only available incoming edge is forced, then solve cycle). Different components independent. Private selection at prefix 3 contributes two distinct lifts; every other local selected endpoint contributes one. Count trees then fill uniquely, establishing the product, including empty public U. Nothing from signed/weighted branch histories is being canceled.

**Stronger coordinate theorem.** Fix canonical label orders, edge orders and one ordered representative of each two-choice private lift and of the two cycle orientations. The entire fiber is in bijection with {0,1}^{f+c}, by one bit per flexible-private selector and per unicyclic component. All other internal edge bits reconstruct uniquely as above using the R795 local table and deterministic tree sums. Encoding/decoding is O(n+m) combinatorial operations given indexed labels and original network/prefix/boundary, plus O(n+m) bits for an explicitly recovered lift. Count can be represented exactly by the exponent or output as a binary integer of f+c+1 bits. Minimal fixed-length rank/unrank code conditional on this retained source and boundary is f+c bits by cardinality, attained by the bijection. This is not a claim that the source itself is redundant.

For future finite Port-only gluing operations where branches are distinguished by their complete edge assignments, use addition over alternative boundary states and multiplication over independent modules with identified interface bits. The local fiber count functions suffice for this count observer since every consistent global assignment restricts uniquely to component assignments and conversely; the bit coordinates permit recovery of actual local assignments if component source, boundary, prefix and composition choices are retained. Other BRC weights, ordered event histories and signed amplitudes remain separate. Counts are integer positive-branch multiplicities, not cancellations or native dynamics.

Example: triangle with all prefixes 3. S=V selects all public labels, ordinary H is one cycle, so exactly two lifts. S=A selects all private labels, H empty and f=3, so eight lifts. More generally a matching source with all prefix 3, S=A has 2^m distinct lifts despite one observed boundary state. The residual is extensive and encoded with precisely m bits for this fiber.

## 2. Minimality of R795 within the exact one-uncertain-node model

Claim: in a loop-free subcubic three-port graph, with exactly three labeled dangling boundaries u,v,a, unused lift ports zero, one uncertain vertex with p=t=1 and even target w, all others fixed prefix p=0 with reserve 0,1,2 and even targets, any gadget realizing R795's three support relations requires at least four vertices. All four-vertex witnesses in this enumerated class have the same count profile after sorting the three supports: (2,1,1), (1,1,0), (1,0,1) in boundary order D=0,5,6. Thus the double private lift in the full-support prefix cannot be eliminated with another four-node gadget in this class.

Justification of exhaustive domain: R779 paired exchange forces all three boundary ports into the same connected component (the two public swaps pair each with a). The uncertain vertex must also lie in that component; otherwise the component's boundary support cannot vary among three nonempty prefixes. Discard disconnected fixed components for the lower bound. For n<=4 connected vertices with uncertain vertex numbered 0, the internal edge multiset is enumerated over all unordered pairs without loops, including parallel edges, with n-1 <= m_int <= floor((3n-3)/2); the upper bound comes from counting three boundary incidences. Enumerate all n^3 allocations of the three labeled boundaries and discard degree>3. A fixed local accepted set is one of four singleton sets, four complements of a singleton, or all four even triples, exactly the nine choices in R779. The uncertain vertex excludes one even code x xor w for each prefix, so its three exclusions range over any three of four (one excluded-missing code w). Choosing a canonical incident-port ordering loses no witnesses because permutations biject the even codes and preserve the enumerated fixed and uncertain families. Enumerate all 2^(m_int+3) assignments, pins zero; count every legal boundary state for all four uncertain exclusions, then inspect each triple of exclusions. Desired D supports are {0,5,6}, {0,5}, {0,6}, encoded by masks 97,33,65. No restriction on which physical prefix realizes which of these three supports. This is complete finite coverage, not a heuristic negative search. The four-vertex example R795 supplies attainment. Extra disconnected components cannot occur in a minimal four-vertex witness because the boundary component itself needs four vertices. This does not rule out larger unique-lift selectors, different uncertain stock laws, or multiple uncertain vertices.

## 3. Executed exact verification

Dependency-free JavaScript, integer bit masks and exact counts within safe integer range. Minimality enumeration independently includes parallel edges and every allowed fixed local relation; count test enumerates every nonempty labeled simple source graph on 2--4 vertices, all prefixes, and every cardinality-m boundary candidate; direct weighted incidence-assignment DP uses local counts obtained from literal XOR constraints, independent of the component formula. Tree uniqueness used analytically, not by explicitly expanding every tree vertex.

Actual output:
```json
{
  "minimal": [
    {
      "n": 1,
      "topologies": 1,
      "configs": 4,
      "hits": 0,
      "profiles": {}
    },
    {
      "n": 2,
      "topologies": 6,
      "configs": 216,
      "hits": 0,
      "profiles": {}
    },
    {
      "n": 3,
      "topologies": 78,
      "configs": 25272,
      "hits": 0,
      "profiles": {}
    },
    {
      "n": 4,
      "topologies": 1176,
      "configs": 3429216,
      "hits": 48,
      "profiles": {
        "[[2,1,1],[1,1,0],[1,0,1]]": 48
      }
    }
  ],
  "fibers": {
    "graphs": 71,
    "prefixes": 4161,
    "queries": 443718,
    "positive": 122100,
    "zero": 321618,
    "cycleQueries": 689,
    "maxExponent": 6,
    "local": {
      "3": [
        1,
        1,
        2
      ],
      "5": [
        0,
        1,
        1
      ],
      "6": [
        1,
        0,
        1
      ]
    }
  }
}
```

```javascript
function minimal(){
 const Q=[0,3,5,6],F=[...Q.map(a=>[a]),...Q.map(a=>Q.filter(b=>a!==b)),Q],ans=[];
 for(let n=1;n<=4;n++){
  let pairs=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)pairs.push([i,j]);
  let topologies=0,configs=0,hits=0,profiles={};
  function check(edges){
   let m=edges.length,seen=new Set([0]);for(let i=0;i<n;i++)for(const [u,v] of edges)if(seen.has(u)||seen.has(v)){seen.add(u);seen.add(v)}
   if(seen.size!==n)return;
   for(let a=0;a<n;a++)for(let b=0;b<n;b++)for(let c=0;c<n;c++){
    let P=Array.from({length:n},()=>[]);edges.forEach(([u,v],i)=>{P[u].push(i);P[v].push(i)});
    [a,b,c].forEach((v,i)=>P[v].push(m+i));if(P.some(p=>p.length>3))continue;topologies++;
    let rows=[];
    for(let mask=0;mask<1<<(m+3);mask++){let z=P.map(p=>p.reduce((s,k,i)=>s+(((mask>>k)&1)<<i),0));if(z.every(x=>Q.includes(x)))rows.push([z,mask>>m])}
    function fix(f){
     if(f.length<n-1){for(let y of F)fix([...f,y]);return}
     let by=Q.map(()=>Array(8).fill(0));
     for(let [z,d] of rows)if(f.every((y,i)=>y.includes(z[i+1])))Q.forEach((e,i)=>{if(e!==z[0])by[i][d]++});
     let masks=by.map(row=>row.reduce((s,v,d)=>s+(v?1<<d:0),0));
     for(let k=0;k<4;k++){
      configs++;let ix=[0,1,2,3].filter(i=>i!==k),ordered=ix.sort((i,j)=>masks[j]-masks[i]);
      if(ordered.map(i=>masks[i]).join(",")!=="97,65,33")continue;
      hits++;let key=JSON.stringify([97,33,65].map(m=>{let i=ix.find(i=>masks[i]===m);return [0,5,6].map(d=>by[i][d])}));profiles[key]=(profiles[key]||0)+1;
     }
    }fix([]);
   }
  }
  function gen(edges,k,left){if(!left){check(edges);return}for(let i=k;i<pairs.length;i++)gen([...edges,pairs[i]],i,left-1)}
  for(let m=n-1;m<=Math.floor((3*n-3)/2);m++)gen([],0,m);
  ans.push({n,topologies,configs,hits,profiles});
 }
 return ans;
}
function counts(){
 let local={};
 for(let x of [3,5,6]){
  let a=[0,0,0];for(let b=0;b<128;b++){
   let [s,t,j,k,u,v,p]=Array.from({length:7},(_,i)=>(b>>i)&1);
   let z=[s+2*t,s+2*u+4*j,t+2*v+4*k,j+2*k+4*p];
   if(z.every(q=>[0,3,5,6].includes(q))&&z[0]!=(x^5)&&z[1]!=3&&z[2]!=6&&z[3]!=6){
    let S=u+2*v+4*(p^1);if(![1,2,4].includes(S))throw Error("rank");a[[1,2,4].indexOf(S)]++;
   }
  }local[x]=a;
 }
 let r={graphs:0,prefixes:0,queries:0,positive:0,zero:0,cycleQueries:0,maxExponent:0,local};
 const pc=x=>{let c=0;while(x){x&=x-1;c++}return c};
 for(let n=2;n<=4;n++){
  let pairs=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)pairs.push([i,j]);
  for(let g=1;g<1<<pairs.length;g++){
   let E=pairs.filter((_,i)=>g>>i&1),m=E.length;r.graphs++;
   for(let p=0;p<3**m;p++){
    r.prefixes++;let x=[],z=p;for(let i=0;i<m;i++){x.push([3,5,6][z%3]);z=Math.floor(z/3)}
    let a=new Map([[0,1]]);
    for(let i=0;i<m;i++){
     let next=new Map(),[u,v]=E[i];for(let [S,c] of a)for(let [j,k] of [u,v,n+i].entries()){
      let w=local[x[i]][j];if(w&&!(S>>k&1)){let T=S|(1<<k);next.set(T,(next.get(T)||0)+w*c)}
     }a=next;
    }
    function predict(S){
     let U=S&((1<<n)-1),adj=Array.from({length:n},()=>[]),stub=Array(n).fill(0),f=0;
     for(let i=0;i<m;i++){
      if(S>>(n+i)&1){if(x[i]===3)f++;continue}
      let [u,v]=E[i],left=!!(U>>u&1)&&!!local[x[i]][0],right=!!(U>>v&1)&&!!local[x[i]][1];
      if(!left&&!right)return [0,0];if(left&&right){adj[u].push(v);adj[v].push(u)}else stub[left?u:v]++;
     }
     let seen=new Set(),c=0;
     for(let u=0;u<n;u++)if((U>>u&1)&&!seen.has(u)){
      let stack=[u],v=0,e=0,h=0;seen.add(u);
      while(stack.length){let k=stack.pop();v++;e+=adj[k].length;h+=stub[k];for(let j of adj[k])if(!seen.has(j)){seen.add(j);stack.push(j)}}
      e/=2;if(e+h!==v)return [0,0];if(e===v)c++;
     }
     return [2**(f+c),c];
    }
    for(let S=0;S<1<<(n+m);S++)if(pc(S)===m){
     r.queries++;let [v,c]=predict(S);if(v!==(a.get(S)||0))throw Error(JSON.stringify({n,E,x,S,v,real:a.get(S)}));
     if(v){r.positive++;r.maxExponent=Math.max(r.maxExponent,Math.log2(v));if(c)r.cycleQueries++}else r.zero++;
    }
   }
  }
 }
 return r;
}
console.log(JSON.stringify({minimal:minimal(),fibers:counts()},null,2));
```

## 4. Next

Study robust compatibility under richer branch-count observers: which lower envelopes of counts can be computed via the implicit cut coordinates rather than expanding prefixes, and whether source plus exterior separator width admits exact quantified DP. Investigate larger selectors with one lift per admitted boundary, or prove a structural obstruction. Preserve native BRC weights/signs, original histories and common-depth coordinate independently. No Foundation or formal Result admission.
