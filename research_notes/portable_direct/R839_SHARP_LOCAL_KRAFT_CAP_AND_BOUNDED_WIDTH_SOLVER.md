# R839 — Sharp local Kraft cap and exact bounded-width joint grading solver

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.
Independent portable TASK_RESEARCH: EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91; own session metadata recovered by r3-20261127-r839-own-read, no run, execution_authorized=false. Previous owner inventory r3-20261127-r838-running-read SUCCEEDED with empty RUNNING projection at 2026-11-27T07:27:27.634466Z and Source drift; new r3-20261127-r839-running-read RUNNING at last check before derivation. No shared ownership or Result mutation. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447, joint observer blob 3923890d77a02d84b772f789e6912dd14f220d14 verified directly (generated startup 404). Global entry snapshot 6ab8a50939dd1a11c41d71593caa39e7e0b0cf46, ACTIVE worldview and current research/portable rules read. This is an auxiliary combinatorial observer and certificate problem; original signed joint moments, road matrices, branch/provenance, temporal order and common depth retained. No native BRC experiment or physical reference calculation.

Direct sources: R835 5bbb0f700911cefec0c28aa434b0d73be0a4d6cf:research_notes/portable_direct/R835_NEIGHBOR_PREFIX_REGRADING_HIGH_GIRTH_OBSTRUCTION.md (neighbor Kraft and connected enumeration); R836 2bcc65992adb4ae3b77cb1125554a25399c5752e:research_notes/portable_direct/R836_JOINT_NEIGHBOR_KRAFT_CONVEX_CERTIFICATE.md; R837 9d062156808e49e28ff18098f507ddd7c409bc1a:research_notes/portable_direct/R837_RATIONAL_GRID_PAYMENT_SEARCH_AND_SHARP_ROUNDING.md; R838 94778c5966f1dcd32c19cd051d21e7fbb0ce6604:research_notes/portable_direct/R838_JOINT_INTEGER_GRADING_PAYMENT_NP_COMPLETENESS.md (one-anchor exact NP-complete decision). The following is a restricted constructive continuation, not a novelty claim against all external literature.

## 1. Local cap: no loss at ANY R834 analytic cover or bundle partition

Let G be the finite simple original-label dependency graph or supergraph of R835. For v let
    M_v = max({0} union {deg(x)-1 : x in N(v)}).
For every nonnegative integer grading L satisfying all open-neighborhood Kraft constraints, the simultaneous componentwise truncation
    L'_v = min(L_v,M_v)
also satisfies all those constraints. In particular all lengths can be bounded by max(0,Delta-1), where Delta is maximum graph degree.

Proof: for any neighborhood N(x) of size k>=1, its integer Kraft lengths admit a binary prefix code (including the empty codeword if k=1). Form its finite binary trie and contract every unary internal vertex. The resulting full binary tree retains exactly the k labeled leaves, each depth no larger than its original length. Any root-to-leaf path of depth h in a full binary tree has h sibling subtrees, each containing a distinct other leaf, so h<=k-1. These contracted depths l_v are themselves valid Kraft lengths. For v in N(x), M_v>=k-1; hence min(L_v,M_v)>=l_v and its Kraft sum is <=sum 2^(-l_v)<=1. Empty neighborhoods impose no constraint. This argument applies to each neighborhood simultaneously even when their independently contracted trees differ: the single global vector dominates every needed local witness. Isolated labels can be set to 0.

For fixed R>1 and nonnegative b_f, activity u_f=b_f R^(L_f+2) is coordinatewise increasing in L. Reducing L to L' can only reduce every bundle activity w_H=prod(1+u_f)-1. Therefore every old R834 payment d remains feasible with exactly the same radius and margin, for arbitrary fixed bundles and anchor cover. The same Q_A-based tail bound holds; this is not a claim that its exact value strictly decreases. R835 enumeration applies to the new grading; P'_U(1)=P_U(1) for EVERY original label subset, all original joint moments and labels retained. General-t interpolation is changed. The cap is structural and independent of numerical bit length, in contrast to the activity-derived cap in R838's NP membership argument. It also bounds integer powers at a variable rational R>1 arbitrarily near 1: their bit length is polynomial in the explicit input. It does not solve general integer/payment feasibility.

Sharpness as a uniform truncation: for any k>=2 take star K_(1,k). Set center length 0, and leaf lengths (1,2,...,k-2,k-1,k-1) (for k=2 the two leaves have length 1). Center Kraft sum equals 1; leaf neighborhoods are singletons. Replacing all leaf lengths by their minimum with k-2 strictly increases that sum past 1. Indeed any componentwise shortening of one of its leaves fails. Thus the k-1 local depth guarantee cannot be improved uniformly by a coordinatewise shortening theorem. This does not rule out reallocation that lengthens other leaves.

## 2. Exact joint solver on bounded-width instances, one analytic anchor

Fix rational R>1, positive rational b_v, eta in (0,1), one analytic anchor containing all labels or all bundles (any partition). All propagation products are empty. Minimal payments d_H=w_H, and the product of 1+w_H is exactly prod_v (1+b_v R^(L_v+2)). Therefore exact joint feasibility is equivalent to minimizing that product over Kraft-legal L and comparing with 2-eta. Section 1 proves that finite local domains {0,...,M_v} give the exact global optimum. For a multi-bundle partition with the same single anchor, the optimum is independent of that partition. If feasible, reconstruct the exact minimal payments d_H directly.

Form a constraint graph C with an edge uv whenever u and v belong to a common N(x), equivalently there exists a length-two walk u-x-v with distinct endpoints. C is a subgraph of G squared. Place unary rational positive objective factors F_v(l)=1+b_v R^(l+2) and, on each N(x), a hard factor 1 on legal Kraft assignments and absent/infeasible otherwise. Empty constraint scopes can be ignored. The min-product over this factorization is precisely the global objective; multiplying positive factors preserves minimization.

Given an elimination ordering of induced width t on C (or a width-t tree decomposition from which such an ordering is constructed), eliminate one variable v at a time. Multiply all current factors whose scopes contain v; for each assignment to the union of their remaining variables take the exact minimum over v's domain, omitting assignments without a feasible choice. Store the minimizing v as a backpointer. Replace those factors by this table, leave other factors unchanged. At the end multiply remaining constants, then reverse the backpointers to recover an optimal full grading. By induction, for every retained assignment each eliminated factor represents the minimum over its eliminated variables; disjoint eliminated variable sets and positivity permit multiplication. This is standard variable elimination applied to the particular joint Kraft objective. Every factor's scope is an induced clique of the chosen elimination order, so the time and space are bounded by O(poly(N) D^(t+1)), D=max(1,Delta), with exact rational bit arithmetic. Input table construction is included (each neighborhood is a clique). At most O(n) original objective factors multiply along disjoint eliminated sets, hence numerator and denominator bit length O(n(B+Delta B)) when B bounds the input rational bit length (and constant factors), polynomial in explicit N. Hard constraints can use integer dyadic sums with denominator 2^max(M_v). The implementation below uses exact BigInt numerator products for R=2 and a common denominator D0; the denominator D0^n is assignment-independent. A supplied decomposition/order establishes the width guarantee; no claim of polynomial-time finding arbitrary optimal treewidth. Greedy ordering in replay has observed widths only.

If G has a supplied width-w decomposition, replace every bag X by union_{x in X} ({x} union N(x)). This covers G squared; bags containing a vertex y are the union of original connected bag subtrees for y and its neighbors, each intersecting y's subtree by edge coverage. Thus width at most (w+1)(Delta+1)-1. In particular bounded degree and bounded treewidth give a polynomial exact joint solver for this one-anchor case, with no continuous witness and no radius shrink. This addresses the tractable frontier suggested by R838 without contradicting its NP-completeness for general subcubic graphs.

## 3. Complete degree-2 solution and subcubic conflict reduction

If Delta<=2, set L_v=1 when v belongs to a degree-two neighborhood, otherwise 0. This is feasible: degree-two neighborhoods contain two length-one labels, degree-one neighborhoods contain one nonnegative length. Any feasible grading must have both labels in every degree-two neighborhood length>=1, since a length-zero label exhausts the whole capacity and every other finite length has strictly positive mass. Hence this is the unique coordinatewise least feasible vector. It gives the globally best activities simultaneously for ANY fixed analytic cover and partition, so the R837 payment search may be run on this grading without any integer search (still a grid/promise algorithm for general covers, not exact real feasibility).

If Delta<=3, all lengths may be taken in {0,1,2}. Set a_v=1 if v belongs to a neighborhood of size at least two, else 0. Every degree-three neighborhood requires at most one length-one label; with other two labels at length two the sum is 1, and conversely two length-one labels would exhaust capacity before the third. Build conflict graph C3 by placing a triangle on each degree-three neighborhood (duplicate edges harmless). All C3 endpoints have a_v=1. Then feasible capped gradings can be optimized by choosing a vertex cover S of C3, setting L_v=2 on S and a_v off S. For arbitrary feasible L, {v:L_v>=2} covers C3 and this construction is coordinatewise no larger than L. Conversely any cover gives valid degree-three, degree-two and singleton constraints. For one anchor the exact optimum reduces to multiplicatively weighted vertex cover:
    base = prod_v (1+b_v R^(a_v+2)),
    optimum = base * min_{S vertex cover of C3} prod_{v in S} (1+b_v R^4)/(1+b_v R^3).
Restrict S to vertices incident to C3 edges, as every factor ratio is >1. This is also a maximum product-weight independent-set optimization using complement; no floating point log weights required. For a bipartite original G, C3 has separate graphs on its two parts, but each can contain triangles. Thus bipartiteness alone does not remove the R838 hardness. The degree-two/three boundary is sharp for one-anchor exact joint feasibility by the existing R838 reduction.

## 4. Exact executed verification

All labeled simple graphs with 1..4 vertices and all on 5 vertices having max degree <=3, including isolates; 843 graphs. For each graph enumerate all length vectors with each coordinate 0..(max_v M_v+1). Check cap on every feasible vector. For two positive rational weight profiles b_v=1/128 or (1+(7v+edgeMask) mod 11)/128 at R=2, compare the min-product elimination solver with direct brute force over the larger domains, verify recovered assignment and exact objective, then compare with conflict-cover exhaustive search. Verify sharp star witnesses for k=2..16. Exact integer dyadic sums and BigInt objective numerator comparisons; no float approximation. Stats from execution:

{
  "graphs": 843,
  "capVectors": 592062,
  "feasibleVectors": 108070,
  "optimizationCases": 1686,
  "bruteVectors": 1184124,
  "dpRows": 95268,
  "maxWidth": 3,
  "degree3ConflictCases": 1686,
  "sharpStars": 15
}

All assertions passed. Finite experiments support the stated bounded domains only; general cap, sharpness and algorithm correctness follow from the written proof. The one-anchor implementation has not yet been extended to arbitrary analytic cover payments or benchmarked on large graphs. No native Port realization or BRC dynamics executed.

Reproduction (JavaScript):
```javascript
function replay(){
 const nbs=(n,edges)=>{const A=Array.from({length:n},()=>[]);for(const [u,v] of edges){A[u].push(v);A[v].push(u)}return A};
 const caps=A=>A.map(N=>Math.max(0,...N.map(v=>A[v].length-1)));
 const valid=(A,L)=>{const m=Math.max(0,...L),C=1n<<BigInt(m);return A.every(N=>N.reduce((s,v)=>s+(1n<<BigInt(m-L[v])),0n)<=C)};
 const cost=(L,b,D)=>L.reduce((p,l,i)=>p*(BigInt(D)+BigInt(b[i])*(1n<<BigInt(l+2))),1n);
 function each(dom,fn){let L=[];function rec(i){if(i===dom.length){fn(L);return}for(let x=0;x<=dom[i];x++){L.push(x);rec(i+1);L.pop()}}rec(0)}
 function solve(A,b,D){
   const M=caps(A),n=A.length,F=[],back=[];let width=0,rows=0;
   function tab(scope,fn){let map=new Map();each(scope.map(v=>M[v]),x=>{let y=fn(x);if(y!==null)map.set(x.join(","),y)});return {scope,map}}
   for(let v=0;v<n;v++){F.push(tab([v],x=>BigInt(D)+BigInt(b[v])*(1n<<BigInt(x[0]+2))));let N=A[v];if(N.length)F.push(tab(N,x=>valid([N.map((_,i)=>i)],x)?1n:null))}
   const rem=new Set(Array.from({length:n},(_,i)=>i));
   while(rem.size){let v=null,S=null,B=null;for(const u of rem){let C=F.filter(f=>f.scope.includes(u)),T=[...new Set(C.flatMap(f=>f.scope))].filter(x=>x!==u).sort((a,b)=>a-b);if(S===null||T.length<S.length){v=u;S=T;B=C}}
     width=Math.max(width,S.length);let choices=new Map(),ix=new Map(S.map((u,i)=>[u,i]));
     let nf=tab(S,x=>{let best=null,arg=null;for(let l=0;l<=M[v];l++){rows++;let p=1n;for(const f of B){let k=f.scope.map(u=>u===v?l:x[ix.get(u)]).join(","),z=f.map.get(k);if(z===undefined){p=null;break}p*=z}if(p!==null&&(best===null||p<best)){best=p;arg=l}}if(best!==null)choices.set(x.join(","),arg);return best});
     for(const f of B)F.splice(F.indexOf(f),1);F.push(nf);back.push({v,S,choices});rem.delete(v)
   }
   let p=1n;for(const f of F){let z=f.map.get("");if(z===undefined)return null;p*=z}
   let L=Array(n);for(const t of back.reverse())L[t.v]=t.choices.get(t.S.map(u=>L[u]).join(","));
   return {p,L,width,rows}
 }
 let stats={graphs:0,capVectors:0,feasibleVectors:0,optimizationCases:0,bruteVectors:0,dpRows:0,maxWidth:0,degree3ConflictCases:0,sharpStars:0};
 const ok=(x,s)=>{if(!x)throw Error(s)};
 for(let n=1;n<=5;n++){let E=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)E.push([i,j]);for(let mask=0;mask<2**E.length;mask++){let A=nbs(n,E.filter((_,i)=>mask&(1<<i)));if(n===5&&A.some(N=>N.length>3))continue;stats.graphs++;let M=caps(A),K=Math.max(0,...M)+1;
   each(Array(n).fill(K),L=>{stats.capVectors++;if(valid(A,L)){stats.feasibleVectors++;ok(valid(A,L.map((l,i)=>Math.min(l,M[i]))),"cap")}});
   for(let t=0;t<2;t++){let b=Array.from({length:n},(_,i)=>1+(t===0?0:(i*7+mask)%11)),D=128;let best=null;
     each(Array(n).fill(K),L=>{stats.bruteVectors++;if(valid(A,L)){let p=cost(L,b,D);if(best===null||p<best)best=p}});
     let z=solve(A,b,D);stats.optimizationCases++;ok(z&&z.p===best&&valid(A,z.L)&&cost(z.L,b,D)===best,"DP");stats.dpRows+=z.rows;stats.maxWidth=Math.max(stats.maxWidth,z.width);
     if(A.every(N=>N.length<=3)){let base=A.map(N=>N.some(v=>A[v].length>=2)?1:0),C=[];for(let N of A)if(N.length===3)for(let i=0;i<3;i++)for(let j=i+1;j<3;j++)C.push([N[i],N[j]]);
       let best2=null;for(let s=0;s<2**n;s++){if(!C.every(([u,v])=>(s&(1<<u))||(s&(1<<v))))continue;let L=base.map((l,i)=>(s&(1<<i))?Math.max(l,2):l);ok(valid(A,L),"conflict");let p=cost(L,b,D);if(best2===null||p<best2)best2=p}ok(best2===best,"conflict optimum");stats.degree3ConflictCases++}
   }
 }}
 for(let k=2;k<=16;k++){let A=nbs(k+1,Array.from({length:k},(_,i)=>[0,i+1])),L=[0,...Array.from({length:k},(_,i)=>Math.min(i+1,k-1))];ok(valid(A,L),"star");ok(!valid(A,L.map((x,i)=>i?Math.min(x,k-2):x)),"sharp");stats.sharpStars++}
 return stats;
}
console.log(replay());
```

Next: exact bounded-width integration of multi-anchor rational-grid payments with the local grading cap, including the scope/bit-complexity tradeoff when analytic anchor size or factor-bundle footprint increases. Retain the open native Port realization and complete joint moment observer/FPTAS mother objective.
