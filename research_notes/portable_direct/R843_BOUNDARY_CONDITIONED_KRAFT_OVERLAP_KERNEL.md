# R843 — Exact boundary-conditioned Kraft elimination for high-degree overlapping scopes

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.
Independent informed portable TASK_RESEARCH. Own metadata verified for EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91, session MCP-ec17f2f30fb8409f8e664eb29ae6c08c; original registration r3-20261124-0124-own-research-registration-v1; no runs, execution_authorized=false. R842 owner read SUCCEEDED, empty RUNNING projection as of 2026-11-27T11:19:29.752108Z with Source drift. R843 owner request r3-20261127-r843-running-read last observed WAITING_RESOURCE/EVENT_READ_CONTROL_BUSY; no shared Task/owner mutation. Global entries verified at immutable main ff36286ec9308f69725659db948ef8374c235a21; ACTIVE worldview and applicable current research/journal/activity rules read. Source current continuation/portable/method/residual rules read separately. Frozen scientific pin unchanged a72226e2430ffa4786321ac86e7f0c599d5f0389, P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447, joint observer blob 3923890d77a02d84b772f789e6912dd14f220d14 directly read; generated foundation startup 404. Global P000 V4 read in full. Auxiliary certificate computation only; original labels, signed joint moments, road matrices, ordered steps, branch provenance and common depth remain intact.

Source: R842 edd03391fce92cd723465472ce6105e027f75657:research_notes/portable_direct/R842_EXACT_KRAFT_CARRY_STREAMING_AND_STAR_SOLVER.md; R839 f5840f229dc8d90cb25f1f6674751d0814f7ddd6:research_notes/portable_direct/R839_SHARP_LOCAL_KRAFT_CAP_AND_BOUNDED_WIDTH_SOLVER.md. The new result extends the isolated high-degree Kraft scope to overlapping scopes, with exact conditional optimization and recovered global assignments. No external priority assertion.

## 1. Boundary-conditioned local theorem

Fix rational R>1, positive rational b_i. A Kraft scope contains d labels, partitioned into k private labels P and r fixed boundary labels B, k+r=d. The boundary lengths are fixed nonnegative integers, potentially deeper than the private cap. Private lengths may take all integers 0..C with a common C>=0. Minimize prod_(i in P)(1+b_i R^(L_i+2)) subject to sum_(i in P union B) 2^(-L_i)<=1. Empty product is 1; infeasible minimum is +infinity. Let M=max(C,0,max_(i in B)L_i). The local value and an attaining private assignment can be computed using O((M+1)(d+1)^3) exact rational operations, including preprocessing, independently of 2^M and of (C+1)^k.

Proof: sort private labels by nonincreasing b. R842 exchange identity permits nondecreasing private lengths without changing the fixed boundary or common cap. Let c_l count fixed labels of length l and B_l=sum_(j>=l)c_j. At depth l keep (i,s), where i private labels have been assigned, and s is the number of available nodes at that depth SATURATED at the remaining total label count k-i+B_l. Initially (0,min(1,d)). At depth l assign the c_l fixed labels and x next private labels, with 0<=x<=min(k-i,s-c_l) and x=0 if l>C. Set j=i+x, rem=k-j+B_(l+1), and transition
    (i,s) -> (j,min(rem,2(s-c_l-x))).
Multiply objective by the next x private factors at depth l. At depth M require rem=0. Recover by backpointers.

The state is exact: for actual available slots a, s=min(a,k-i+B_l). Subtracting the same c_l+x and doubling commutes with saturation at the new remaining count: if a<=remaining the claim is immediate, otherwise both doubled counts are >=rem. A selection c_l+x is possible iff it fits s, since it never exceeds remaining. Induction shows each feasible depth profile has exactly this saturated path; conversely every path is realized in the binary prefix tree by assigning the indicated leaves to available slots and expanding unused slots, with all surplus slots free to remain unused. Kraft's theorem gives equivalence between such tree profiles and the original inequality. Fixed boundary labels of the same depth are interchangeable for this *local feasibility/value* observer; they remain individually identified in the global input and reconstructed grading. No full-tree assumption is needed: fixed labels can force unused capacity. The proof includes k=0, r=0, d=0 (empty scope) and infeasible boundary choices. Each depth has O((d+1)^2) states, O(d+1) choices per state; precompute or accumulate segment products. Backpointer reconstruction is polynomial. Bit lengths are polynomial in explicit input, d and M, since all products use each private factor at most once. The theorem does not claim polynomial complexity in log M if M is supplied succinctly; R839 caps M by Delta-1 in the application.

A useful local quotient: conditional minimum depends on the multiset of fixed boundary lengths (c_l), not which boundary label bears each length. Thus identical boundary histograms may reuse a table computation without changing the global label-indexed constraints. With r fixed boundary labels and maximum length M, at most binomial(M+r,r) histograms exist; individual caps only reduce this count. This is an optional cache, not used in the replay.

## 2. Global overlap-kernel theorem for one analytic anchor

Let G be the original simple dependency graph with maximum degree Delta, all neighborhood Kraft constraints, one analytic anchor and any fixed bundle partition. The minimum exact anchor payment product is min_L prod_v(1+b_v R^(L_v+2)); bundle grouping cancels in the product because 1+w_H is precisely the product of original factors in H. The minimal payment for each bundle is w_H, so compare this optimum with 2-eta. R839 permits L_v<=M_v=max({0} union {deg(x)-1:x in N(v)}). Delete empty and singleton Kraft constraints (always satisfied for L>=0). Classify a label as private if it occurs in exactly one remaining scope, shared if it occurs in at least two, and free otherwise. Free optimal length is zero. A private label in scope S has common cap |S|-1 by R839, regardless of its own degree. No private label affects another remaining Kraft factor.

For each scope S form an exact table F_S on its shared labels, with value equal to the conditional private minimum of section 1. Assign +infinity when infeasible. The exact global optimum equals
    prod_free(1+b_v R^2) * min_Lshared [prod_shared(1+b_v R^(L_v+2)) prod_S F_S(Lshared|S)].
Proof: conditioning on all shared lengths separates all private label sets, which are disjoint; every private objective occurs once and every scope is enforced. Conversely, optimal local private witnesses assemble with any feasible shared assignment, exactly attaining the table objective. Recover all original lengths, then bundle payments and verify original constraints. This is a lossless optimization reduction, not a reduction of the underlying joint observation graph.

Let h=max_S |S intersect shared|, D=max(1,Delta), and t be the width of a supplied variable elimination order on the shared primal graph (join shared labels appearing in a common scope). Local preprocessing is bounded by O(sum_S D^|S intersect shared| (M_S+1)(|S|+1)^3), where M_S<=max(0,Delta-1). Elimination needs O(poly(N) D^(t+1)) rational operations and polynomial-size backpointers per table entry. Since h<=t+1 for nonempty scopes under a supplied order, fixed t implies polynomial bit complexity even with unbounded original degree and scope size. Include explicit graph, weight bit lengths and supplied order in N; all reconstructed products contain each factor once, so exact arithmetic has polynomial bit length. An empty shared kernel has no elimination. No general bounded-treewidth theorem for arbitrary multi-anchor payments is asserted.

## 3. Unbounded-degree example and structural extension

Start with a path on H>=3 hubs and attach k>=2 private leaves to every hub. Original maximal degree k+2; original neighborhood primal contains a clique of that order. The only shared variables are interior hubs (each appears in two nontrivial hub scopes). Every hub scope has at most two shared labels, and its shared pairs have indices differing by two. Thus the shared primal is two disjoint paths (some isolated vertices), width <=1. Ascending hub order works. The theorem gives an exact polynomial solver uniformly in H and k, for arbitrary positive rational weights, with no radius loss or grid. More generally take a bounded-degree, bounded-treewidth backbone and attach arbitrarily many leaves per vertex, so all backbone vertices have degree >=2 in the resulting graph. The shared primal is contained in the common-neighbor graph on the backbone. Expanding backbone tree decomposition bags by their closed backbone neighborhoods gives a width bound (w+1)(Delta_backbone+1)-1. Consequently the result covers unbounded original degrees whenever the backbone width and degree are bounded. This is strictly beyond the isolated R842 star scope and addresses the shared-label part of R842's next question. It does not resolve arbitrary incidence forests with large overlap kernels, nor R841's general multi-anchor expanded chain width.

## 4. Exact executed replay

The following replay uses only BigInt scaled integer products and dyadic integer Kraft tests; denominators are common across the fixed R and M instance. Local test: d=2..6, r=0..min(2,d), private cap d-1, fixed boundary lengths all 0..d+1, two weight profiles, R=2 and 4/3. Compare complete private-domain enumeration against the saturated-slot DP and validate recovered lengths. Global test: hub paths H=1..4, k=1..2 with total labels <=9, two weight profiles, two radii, compare all capped length assignments against overlap-kernel elimination and exact recovered assignments. One larger path H=10,k=12,R=4/3 is solved and its recovered assignment verified (no brute-force global comparison at that size). These are exact optimal values, not a measured runtime comparison or an actual BRC dynamic experiment. Full R841 mixed-incidence implementation remains open.

```json
{
  "localCases": 900,
  "localFeasible": 644,
  "localInfeasible": 256,
  "localBruteLeaves": 827296,
  "slotTransitions": 1478538,
  "globalCases": 28,
  "globalBruteLeaves": 264360,
  "globalLarge": {
    "n": 130,
    "scopes": 10,
    "shared": 8,
    "maxCap": 13,
    "tableEntries": 1232,
    "eliminationBag": 2,
    "recovered": true
  }
}
```

```javascript
function replay(){
 const stats={localCases:0,localFeasible:0,localInfeasible:0,localBruteLeaves:0,slotTransitions:0,globalCases:0,globalBruteLeaves:0,globalLarge:null};
 const prod=a=>a.reduce((p,x)=>p*x,1n);
 const each=(caps,fn)=>{let a=[];function rec(i){if(i===caps.length){fn(a.slice());return}for(let l=0;l<=caps[i];l++){a[i]=l;rec(i+1)}}rec(0)};
 function weights(nums,M,rn,rd){const D=97n*rd**BigInt(M+2);return nums.map(b=>Array.from({length:M+1},(_,l)=>D+BigInt(b)*rn**BigInt(l+2)*rd**BigInt(M-l)))}
 function kraft(L,M){return L.reduce((s,l)=>s+(1n<<BigInt(M-l)),0n)<=1n<<BigInt(M)}
 function local(priv,fixed,cap,F){ // priv in nonincreasing b order
  const k=priv.length,d=k+fixed.length,M=Math.max(cap,0,...fixed);
  const c=Array(M+1).fill(0);for(const l of fixed)c[l]++;
  const tail=Array(M+2).fill(0);for(let l=M;l>=0;l--)tail[l]=tail[l+1]+c[l];
  let map=new Map([["0,"+Math.min(1,d),{v:1n,L:[]}]]);
  for(let l=0;l<=M;l++){
   const next=new Map();
   for(const [key,o] of map){const [i,s]=key.split(",").map(Number);let seg=1n;
    for(let x=0;x<=Math.min(k-i,s-c[l],l<=cap?k:0);x++){
     if(x)seg*=F[priv[i+x-1]][l];const j=i+x,remaining=k-j+tail[l+1],t=Math.min(remaining,2*(s-c[l]-x));if(l===M&&remaining!==0)continue;
     stats.slotTransitions++;const q=j+","+t,v=o.v*seg;
     if(!next.has(q)||v<next.get(q).v)next.set(q,{v,L:o.L.concat(Array(x).fill(l))});
    }
   }map=next;
  }
  return map.get(k+",0")??null;
 }
 for(let d=2;d<=6;d++)for(let r=0;r<=Math.min(2,d);r++)for(let profile=0;profile<2;profile++)for(const [rn,rd] of [[2n,1n],[4n,3n]]){
  const cap=d-1,M=d+1,k=d-r,nums=Array.from({length:k},(_,i)=>1+(profile?((i*7+3)%11):0)).sort((a,b)=>b-a),F=weights(nums,M,rn,rd),priv=nums.map((_,i)=>i);
  each(Array(r).fill(M),fixed=>{
   let best=null;each(Array(k).fill(cap),L=>{stats.localBruteLeaves++;if(kraft([...L,...fixed],M)){const v=prod(L.map((l,i)=>F[i][l]));if(best===null||v<best)best=v}});
   const o=local(priv,fixed,cap,F);if((o?.v??null)!==best)throw Error("local optimum");if(o&&(!kraft([...o.L,...fixed],M)||prod(o.L.map((l,i)=>F[i][l]))!==o.v))throw Error("local recovery");
   stats.localCases++;if(o)stats.localFeasible++;else stats.localInfeasible++;
  })
 }
 function global(G,nums,rn,rd,brute){
  const n=G.length,scopes=G.filter(a=>a.length>=2),occ=Array(n).fill(0);for(const s of scopes)for(const v of s)occ[v]++;
  const cap=G.map(a=>Math.max(0,...a.map(v=>G[v].length-1))),M=Math.max(...cap),F=weights(nums,M,rn,rd),shared=cap.map((_,i)=>i).filter(i=>occ[i]>=2);
  let factors=[],localTables=[],entries=0,peak=0;const assignment=Array(n).fill(0),keys=(s)=>s.map(v=>assignment[v]).join(",");
  for(const s of scopes){const p=s.filter(v=>occ[v]===1).sort((a,b)=>nums[b]-nums[a]||a-b),h=s.filter(v=>occ[v]>=2).sort((a,b)=>a-b),tab=new Map(),recover=new Map();
   each(h.map(v=>cap[v]),L=>{for(let i=0;i<h.length;i++)assignment[h[i]]=L[i];const o=local(p,L,s.length-1,F);if(o){tab.set(keys(h),o.v);recover.set(keys(h),o.L)}entries++});
   factors.push({s:h,t:tab});localTables.push({h,p,recover});
  }
  for(const v of shared)factors.push({s:[v],t:new Map(F[v].slice(0,cap[v]+1).map((x,l)=>[String(l),x]))});
  for(let v=0;v<n;v++)if(occ[v]===0)factors.push({s:[],t:new Map([["",F[v][0]]])});
  let history=[];
  for(const v of shared){const used=factors.filter(f=>f.s.includes(v));factors=factors.filter(f=>!f.s.includes(v));const h=[...new Set(used.flatMap(f=>f.s))].filter(x=>x!==v).sort((a,b)=>a-b),t=new Map(),choice=new Map();peak=Math.max(peak,h.length+1);
   each(h.map(x=>cap[x]),L=>{h.forEach((x,i)=>assignment[x]=L[i]);let best=null,bestL=null;
    for(let l=0;l<=cap[v];l++){assignment[v]=l;const vals=used.map(f=>f.t.get(keys(f.s)));if(vals.some(x=>x===undefined))continue;const z=prod(vals);if(best===null||z<best){best=z;bestL=l}}
    if(best!==null){t.set(keys(h),best);choice.set(keys(h),bestL)}
   });factors.push({s:h,t});history.push({v,h,choice});
  }
  const vals=factors.map(f=>f.t.get(""));if(vals.some(x=>x===undefined))throw Error("unexpected infeasible global");const value=prod(vals);
  for(const {v,h,choice} of history.reverse())assignment[v]=choice.get(keys(h));
  for(const {h,p,recover} of localTables){const L=recover.get(keys(h));if(!L)throw Error("missing recovery");p.forEach((v,i)=>assignment[v]=L[i])}
  if(!G.every(s=>kraft(s.map(v=>assignment[v]),M))||prod(assignment.map((l,i)=>F[i][l]))!==value)throw Error("global recovery");
  if(brute){let best=null;each(cap,L=>{stats.globalBruteLeaves++;if(G.every(s=>kraft(s.map(v=>L[v]),M))){const z=prod(L.map((l,i)=>F[i][l]));if(best===null||z<best)best=z}});if(best!==value)throw Error("global optimum")}
  return {n,scopes:scopes.length,shared:shared.length,maxCap:M,tableEntries:entries,eliminationBag:peak,recovered:true};
 }
 function path(h,k){const G=Array.from({length:h*(k+1)},()=>[]);function edge(a,b){G[a].push(b);G[b].push(a)}for(let i=1;i<h;i++)edge(i-1,i);for(let i=0;i<h;i++)for(let j=0;j<k;j++)edge(i,h+i*k+j);return G}
 for(let h=1;h<=4;h++)for(let k=1;k<=2;k++)if(h*(k+1)<=9)for(let p=0;p<2;p++)for(const [rn,rd] of [[2n,1n],[4n,3n]]){const G=path(h,k);global(G,G.map((_,i)=>1+(p?(i*7+3)%11:0)),rn,rd,true);stats.globalCases++}
 const G=path(10,12);stats.globalLarge=global(G,G.map((_,i)=>1+(i*7+3)%11),4n,3n,false);
 return stats;
}
console.log(JSON.stringify(replay(),null,2));
```

Next: extend boundary-conditioned optimization to arbitrary separable boundary messages or multi-anchor certificate costs, and test whether original incidence-tree decompositions can order the R841 product chains without large width growth. Native Port realizability, exact joint moment oracle and general Port FPTAS remain open.
