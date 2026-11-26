# R812 — Exact charged block interfaces and degree-paid FPTAS beyond cactus

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation, no shared CLAIM, RUN or Result. Fixed predecessor 85602229b2bfd5a6ad6e4c8190e1e5fcc2aa46d6:research_notes/portable_direct/R811_CYCLE_PAID_CACTUS_ANTICHANNEL_FPTAS.md; R810 at 4432797b505566a8172ccd2f8dbe2f2b3919e9d1, R809 at f8e92e90a85ede6f922ebcda716adbb0528e4192, same directory. Frozen foundation pin a72226e2430ffa4786321ac86e7f0c599d5f0389; P000 V5 and joint-observer contract read by exact blobs dc84bdae6595b5e237a2ad50d8b21916adb2e447 and 3923890d77a02d84b772f789e6912dd14f220d14. ACTIVE worldview, current account entries at 0cda44c99fad2dbc67b77059d573bc6d7605daaf, project continuation and portable research, method and applicable account policies read. Own metadata receipt r3-20261126-r812-own-metadata and original registration r3-20261124-0124-own-research-registration-v1 identify EM-DIRECT-82A007 / TASK_RESEARCH, no active own RUN, execution_authorized=false. Owner inventory r3-20261126-r812-running-read was RUNNING at derivation, not evidence of empty inventory. All results concern the auxiliary positive combinatorial observer, not native signed BRC execution. Keep full road matrices, original branch sources, time order, and common-depth repair coordinates. Local interfaces are exact for the declared joint occupancy/parity partition and not a claim of full-state redundancy.

## 1. Exact affine block factorization for every charge

Use the R809 physical simple road graph G=(V,E), retained anti-channel set J subset E, incidence variables x_e in {00,01,10,11}, rational S_e >=0 with S_e(11)>0, 0<eta_e<=1, and original d_v=deg_G(v). At nonisolated vertices a_v>=1-2^(-2d_v-1), a_v<=1. Let delta_v=1-a_v. Isolated factors are positive constants. R809 gives
 Q_T(J)/2^n = sum_x prod_e S_e(x_e) prod_v (1-delta_v I(all incident bits zero)) sum_{F subset J, boundary F=T} eta(F) I(x_e=11 for e in F).
All retained F have positive contribution to the all-occupied assignment. T is feasible iff every component of (V,J) contains an even number of T vertices; otherwise Q_T=0 exactly. For feasible T choose F0 with boundary T by a spanning-forest parity solve.

Partition E into edge sets of the vertex-biconnected blocks of (V,J), treating every bridge as a singleton, and add each edge outside J as its own singleton. Groups are edge disjoint but may meet at vertices. The binary cycle space of J is the direct sum of the block cycle spaces: an even subgraph decomposes into simple cycles, each contained in one block, and each block's even subgraph is even globally. Thus all F with boundary T are exactly the independent choices F_B=(F0 intersect B) xor C_B, C_B in the cycle space of B (F_B empty for outside-J singleton). The local charge t_B=boundary(F0 intersect B) is independent of the representative F0. This affine decomposition covers arbitrary shared-edge cycles within a block, not just cactus cycles. Define H_B(x_B)=sum_{F_B: boundary F_B=t_B} eta(F_B) I(x_e=11 for e in F_B), with H=1 on outside-J singletons. The parity factor is exactly prod_B H_B. No approximation or independence assumption on x is used.

## 2. Exact joint interface coordinate

For group B let U_B be vertices incident to B and at least one other group, b_B=|U_B|, and k_{Bv}=number of edges of B incident to v. Keep one bit z_{Bv}=1 iff all ports of B at v are empty. For each binary interface z define the nonnegative rational table
 h_B(z)=sum_{x_B with interface z} prod_{e in B} S_e(x_e) H_B(x_B) prod_{v internal to B} g_v(x_B).
Internal means all incident edges of v are in B. Zero entries are omitted, not replaced by approximate positive values. The all-occupied assignment ensures at least one positive entry in every group for feasible T. At shared v the original empty condition is exactly AND of the z_{Bv} over its incident groups. Therefore
 Q_T(J)=2^n (prod isolated a_v) sum_{z} prod_B h_B(z_B) prod_{v shared} [1-delta_v prod_{B touching v} z_{Bv}].
The table retains the joint interface, not the separate one-port marginals. This identity proves sufficiency for this partition, all its interface restrictions and deletions/shrinkings of shared vertex factors. Full source objects remain available for other observers.

## 3. Constructing tables from original input

Let r_B=|B|-|V_B|+1 for a connected group. For given z, enumerate the 2^r_B affine parity supports using a spanning tree and chord selection. For each support force x_e=11 on its edges; enumerate the at most 4^r_B chord occupancy states. The rest is a tree. At a vertex, for a fixed parent-port bit and fixed chord bits, multiply child messages to obtain total weight U and all-ports-empty weight V. With internal factor the resulting weight is U-delta_v V; with prescribed interface bit it is V (z=1) or U-V (z=0). Compute both parent-bit messages once per vertex, multiplying edge weights in the child sums. This gives exact h_B in O(2^b_B 8^r_B poly(input)) rational operations, including affine support generation. The finite verifier below intentionally uses exhaustive support and small-tree recomputation rather than a production memoized DP.

Stronger analytic construction when a tree decomposition of group B of width t_B is supplied: for each interface pattern use a nice decomposition with introduce-edge operations. Each introduced edge has up to five joint choices (four x states with f=0, plus x=11 with f=1 if retained), weight S_e(x) eta_e^f. A bag vertex keeps two bits: parity of selected incident f and OR of occupied incidence bits from processed edges. Introduce vertex initializes both zero, introduce edge updates both endpoint states, join combines parity by XOR and occupancy by OR while multiplying partial weights and summing over pairs. When forgetting v, enforce parity t_B at v, and either multiply g_v or enforce the prescribed interface bit. Each edge appears once and each vertex factor is applied once. Empty root yields h_B(z). With at most 4^(t_B+1) states per bag, join at most 16^(t_B+1) pairs, so cost O(2^b_B 16^(t_B+1) poly(input/decomposition size)). This permits arbitrarily high rank inside bounded-width blocks, e.g. ladders of growing length. For fixed b_B and logarithmic supplied t_B or logarithmic r_B the respective table construction is polynomial. Explicit rational road matrices from R803 have polynomial bit cost in their explicit input sequences. Both constructions have rational bit complexity polynomial when their operation bounds are polynomial: expand sums over a finite number of weighted assignments, denominators divide products of input denominators, and numerators have input bit length plus O(number of edges/vertices) counting bits. No binary-compressed lengths or succinct table input theorem is claimed.

## 4. Degree-paid block deletion recursion

Assume fixed b0 bounding all b_B. Domains consist of any nonempty subset of positive table entries. Shared factors may be deleted or shrunk. For query group B remove it and all active shared factors involving it; common base cancels. For each admissible z restore factors with z_{Bv}=1 in a fixed order. Each factor restoration multiplies the common base weight by 1-delta_v p_{v,z}, where p_{v,z} is the probability that all remaining groups at v have their bit 1, in the then-current subinstance. Compute by exact conditional chain, with infeasible conjunctions zero and deterministic conjunctions exact. Recursive children remove at least the queried group. This is R810's exact deletion mechanism at a new, scope-typed joint coordinate.

Charge a call for vertex v by c=d_v-k_{Bv}>=1 (number of original incident edges outside B); at most c other groups participate. Use h_L=2^(-L), base L=0 normalized table, and skip nontrivial conjunctions at c>L by p=0, otherwise query at L-c. The original d_v remains fixed even after pinnings/deletions. By product telescoping the log-weight error contributed by that factor is <= h_L c 2^c delta_v/a_v (skipping also satisfies this). For any k>=1,c>=1,
 c 2^c/(2^(2(k+c)+1)-1) <= 2/(2^(2k+3)-1).
Proof: c<=2^(c-1), so numerator <=2*4^(c-1); denominator =4^(c-1)*2^(2k+3)-1 >=4^(c-1)*(2^(2k+3)-1).
Define exact load A_B=sum_{v in U_B} c 2^c delta_v/a_v. Then event error at most (A_B/2) h_L: each positive state's log-weight error bounded by A_B h_L, normalized event derivative under log interpolation bounded by one quarter the oscillation (at most twice that). In particular contraction induction holds if every A_B<=2. For cyclic biconnected groups k_{Bv}>=2, giving A_B<=2 b_B/127. For singleton groups k=1, b_B<=2, giving A_B<=4/31. Hence b0=127 is a uniform sufficient fixed interface bound; the exact load criterion can cover other fixed interface bounds. This is a sufficient algorithmic threshold, not a necessity or a sharp hardness boundary.

Each state generates at most c children for v at cost c. There are <=2^b0 states. For M=2^(b0+1)*max(1,b0), sum of child branching weights M^(-cost) <= 2^b0 b0/M <=1/2 since c/M^c<=1/M. Thus recursion tree <=2 M^L nodes by induction. Polynomial nonrecursive work per node; rational expression arithmetic has polynomial bit complexity for L=O(log(number of groups/epsilon)), using fixed state count and depth, and summing operand bit lengths with at most constant replication per depth. This theoretical exponent may be large; no practical performance promise.

## 5. Charged FPTAS theorem and scope

In a feasible subinstance choose an admissible maximal base table entry. Conditional on all other groups, at most b0 factors change and all lie in [7/8,1]. Thus reference state probability >=p0=(7/8)^b0 / 2^b0, also after averaging. Pin these reference states sequentially; if their exact probabilities are p_i, exact total is the known reference weight divided by prod p_i (times 2^n and isolated factors). Approximate each p_i to absolute error p0 epsilon/(8 max(1,number of groups)), using L=O(log(groups/epsilon)); sum log relative errors <=epsilon/4 for 0<epsilon<=1. The resulting relative partition error is <=epsilon. Zero Q_T is detected exactly by component parity. Therefore for any fixed b0 with load A_B<=2, polynomial table preprocessing as in section 3 gives deterministic FPTAS for EVERY specified boundary charge T, including nonzero. Uniform sufficient b_B<=127, with bounded or logarithmic cycle rank per block, or supplied bounded/logarithmic-width block decomposition, suffices. E can be arbitrarily dense or of unbounded treewidth because edges outside J are singletons. No bound on total cycle rank, total number of overlapping cycles, length of any low-width block, or degree of G. E=J is allowed. For example arbitrarily many large ladder blocks with <=127 attachment vertices each, even with other original occupancy edges between these attachments, fall in scope; tree decompositions of ladders have constant width. This goes beyond R811's edge-disjoint cycles and zero charge. It does not subsume R811's arbitrary-interface cactus case and does not solve general arbitrary-interface overlapping-cycle models. Computing q_T from two FPTAS calls is immediate by relative-error composition; no simultaneous enumeration of exponentially many T is claimed.

## 6. Exact verification and limits

Actually ran the JS BigInt verifier below twice. Five small explicit graphs: theta, theta with external edges (one retained bridge), two shared-vertex cycles with external edges, chorded square with bridge, K4; two modes (identity or heterogeneous road lengths 0,1,2). Integer-scaled weights preserve all compared partitions and probabilities; eta denominators 1 or 3; vertex weights scaled by 2^(2d+1). Enumerated all charges; infeasible charge zero, exact local tree tables vs independent local enumeration, whole grouped partition vs direct original parity/occupancy enumeration, exact deletion marginals vs brute grouped distribution under unpinned and first-group pin, and truncation budgets 0..3 for state/port events. Checked coefficient inequality for k=1..8,c=1..64 (512 cases). Output {"instances":10,"charges":160,"zeroCharges":160,"localTableEntries":1568,"partitionChecks":160,"marginalChecks":1672,"truncationChecks":12832,"recursionNodes":5857,"longThetaEntries":0}. All passed; longThetaEntries=0 records no large-instance benchmark. The finite verifier checks rank-based tables and recursion on small graphs, not the tree-decomposition implementation, the general threshold by finite testing, or native BRC. General claims follow from the analytic proof; independent review pending.

```javascript
function verify(){
 const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a<0n?-a:a},f=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);let g=gcd(a,b);return[a/g,b/g]},add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]),div=(a,b)=>f(a[0]*b[1],a[1]*b[0]),sub=(a,b)=>f(a[0]*b[1]-b[0]*a[1],a[1]*b[1]),eq=(a,b)=>a[0]*b[1]===a[1]*b[0],zero=f(0),one=f(1),sum=a=>a.reduce(add,zero);
 const stats={instances:0,charges:0,zeroCharges:0,localTableEntries:0,partitionChecks:0,marginalChecks:0,truncationChecks:0,recursionNodes:0,longThetaEntries:0};
 const ck=(b,m)=>{if(!b)throw Error(m+" "+JSON.stringify(stats));};
 const cases=[
 [4,[[0,1],[0,2],[2,1],[0,3],[3,1]],[[0,1,2,3,4]]],
 [5,[[0,1],[0,2],[2,1],[0,3],[3,1],[1,4],[2,4]],[[0,1,2,3,4],[5],[6]],63],
 [6,[[0,1],[1,2],[2,0],[2,3],[3,4],[4,2],[4,5],[0,5]],[[0,1,2],[3,4,5],[6],[7]],127],
 [5,[[0,1],[1,2],[2,3],[3,0],[0,2],[2,4]],[[0,1,2,3,4],[5]]],
 [4,[[0,1],[1,2],[2,3],[3,0],[0,2],[1,3]],[[0,1,2,3,4,5]]]
 ];
 const bit=(x,i)=>(x>>i)&1;
 function build(n,E,G,J,mode){
  let m=E.length,d=Array(n).fill(0); E.forEach(([u,v])=>{d[u]++;d[v]++});
  let den=d.map(v=>2n**BigInt(2*v+1)),w=E.map((_,i)=>(mode===0?[2,0,0,1]:[[2,0,0,1],[7,4,4,2],[81,44,44,24]][i%3]).map(BigInt)),eta=E.map((_,i)=>mode&&i%3===2?3n:1n);
  let at=Array.from({length:n},(_,v)=>G.flatMap((B,b)=>B.some(e=>E[e].includes(v))?[b]:[]));
  let bd=G.map((B,b)=>at.flatMap((a,v)=>a.includes(b)&&a.length>1?[v]:[]));
  let bdMask=G.map((B,b)=>bd[b].reduce((a,v)=>a|(1<<v),0));
  function boundary(F){let t=0;for(let e=0;e<m;e++)if(bit(F,e)){let [u,v]=E[e];t^=(1<<u)|(1<<v);}return t;}
  function treeValue(B,F,b,z){
   let V=[...new Set(B.flatMap(e=>E[e]))],parent=Array(n).fill(-1),tree=[],chords=[],root=V[0],seen=new Set([root]);
   while(seen.size<V.length){let e=B.find(e=>seen.has(E[e][0])!==seen.has(E[e][1]));if(e===undefined)throw Error("disconnected");let [u,v]=E[e];if(seen.has(v))[u,v]=[v,u];parent[v]=u;seen.add(v);tree.push([e,u,v]);}
   chords=B.filter(e=>!tree.some(t=>t[0]===e));
   const vals=e=>bit(F,e)?[3]:[0,1,2,3];
   const port=(e,s,v)=>E[e][0]===v?bit(s,1):bit(s,0);
   let total=0n;
   function go(i,weight,occupied){if(i<chords.length){let e=chords[i];for(let s of vals(e)){if(!w[e][s])continue;let [u,v]=E[e];go(i+1,weight*w[e][s],occupied|(port(e,s,u)<<u)|(port(e,s,v)<<v));}return;}
    function msg(v,inbit){let all=1n,empty=(inbit||bit(occupied,v))?0n:1n;for(let [e,u,t] of tree){if(u!==v)continue;let a=0n,h=0n;for(let s of vals(e)){if(!w[e][s])continue;let k=w[e][s]*msg(t,port(e,s,t));a+=k;if(!port(e,s,v))h+=k;}all*=a;empty*=h;}
     return bit(bdMask[b],v)?(bit(z,v)?empty:all-empty):den[v]*all-empty;
    }
    total+=weight*msg(root,0);
   }
   go(0,1n,0);return total;
  }
  function local(B,b,Flist){
   let table=new Map(),brute=new Map(),Bmask=B.reduce((a,e)=>a|(1<<e),0),V=[...new Set(B.flatMap(e=>E[e]))];
   for(let z=bdMask[b];;z=(z-1)&bdMask[b]){
    let t=0n;for(let F of Flist){let a=1n;for(let e of B)if(bit(J,e)&&!bit(F,e))a*=eta[e];t+=a*treeValue(B,F,b,z);}table.set(z,t);if(!z)break;
   }
   function rec(i,w0,occ,A){if(i===B.length){let h=0n;for(let F of Flist)if((F&A)===F){let t=1n;for(let e of B)if(bit(J,e)&&!bit(F,e))t*=eta[e];h+=t;}for(let v of V)if(!bit(bdMask[b],v))w0*=den[v]-(bit(occ,v)?0n:1n);let z=bdMask[b]&~occ;brute.set(z,(brute.get(z)||0n)+w0*h);return;}
    let e=B[i],[u,v]=E[e];for(let s=0;s<4;s++)if(w[e][s])rec(i+1,w0*w[e][s],occ|(bit(s,1)<<u)|(bit(s,0)<<v),A|(s===3?1<<e:0));
   }
   rec(0,1n,0,0);for(let [z,t] of table){ck(t===(brute.get(z)||0n),"tree local");stats.localTableEntries++;}
   return [...table].filter(([z,t])=>t>0n);
  }
  function direct(T){let total=0n;function rec(i,w0,occ,A){if(i===m){let h=0n;let a=A&J;for(let F=a;;F=(F-1)&a){if(boundary(F)===T){let t=1n;for(let e=0;e<m;e++)if(bit(J,e)&&!bit(F,e))t*=eta[e];h+=t;}if(!F)break;}for(let v=0;v<n;v++)w0*=den[v]-(bit(occ,v)?0n:1n);total+=w0*h;return;}let [u,v]=E[i];for(let s=0;s<4;s++)if(w[i][s])rec(i+1,w0*w[i][s],occ|(bit(s,1)<<u)|(bit(s,0)<<v),A|(s===3?1<<i:0));}
   rec(0,1n,0,0);return total;}
  const representatives=new Map();for(let F=J;;F=(F-1)&J){let t=boundary(F);if(!representatives.has(t))representatives.set(t,F);if(!F)break;}
  for(let T=0;T<(1<<n);T++){
   if(!representatives.has(T)){ck(direct(T)===0n,"infeasible charge");stats.zeroCharges++;continue;}
   let F0=representatives.get(T),tables=G.map((B,b)=>{let M=B.reduce((a,e)=>a|(1<<e),0)&J,t=boundary(F0&M),fs=[];for(let F=M;;F=(F-1)&M){if(boundary(F)===t)fs.push(F);if(!F)break;}return local(B,b,fs);});
   let factors=at.flatMap((a,v)=>a.length>1?[{v,ids:a}]:[]),dom=tables.map(t=>t.map(([z])=>z));
   function brute(dd,fs,b=-1){let Z=0n,P=new Map(),zv=Array(G.length).fill(0);function rec(i,a){if(i===G.length){for(let g of fs)a*=den[g.v]-(g.ids.every(j=>bit(zv[j],g.v))?1n:0n);Z+=a;if(b>=0)P.set(zv[b],(P.get(zv[b])||0n)+a);return;}if(dd[i]===null){rec(i+1,a);return;}for(let [z,w] of tables[i])if(dd[i].includes(z)){zv[i]=z;rec(i+1,a*w);}}
    rec(0,1n);return {Z,P};}
   ck(brute(dom,factors).Z===direct(T),"whole partition");stats.partitionChecks++;stats.charges++;
   const memo=new Map();
   function dist(dd,fs,b,L){let key=JSON.stringify([dd,fs,b,L]);if(memo.has(key))return memo.get(key);stats.recursionNodes++;
    let inc=fs.filter(g=>g.ids.includes(b)),rest=fs.filter(g=>!g.ids.includes(b)),out=new Map();
    for(let [z,w] of tables[b])if(dd[b].includes(z)){let a=f(w),live=rest.slice(),d2=dd.slice();d2[b]=null;
     if(L!==0)for(let g of inc){if(!bit(z,g.v))continue;let ids=g.ids.filter(i=>i!==b),free=ids.filter(i=>d2[i].some(t=>!bit(t,g.v))),p=one,c=E.filter((e,i)=>e.includes(g.v)&&!G[b].includes(i)).length;
      if(free.some(i=>!d2[i].some(t=>bit(t,g.v))))p=zero;
      else if(free.length&&L>=0&&c>L)p=zero;
      else{let next=d2.slice();for(let i of free){let q=dist(next,live,i,L<0?-1:L-c);p=mul(p,sum([...q].filter(([t])=>bit(t,g.v)).map(([,v])=>v)));next[i]=next[i].filter(t=>bit(t,g.v));}}
      a=mul(a,sub(one,div(p,f(den[g.v]))));live.push({v:g.v,ids});
     }
     out.set(z,a);
    }
    let norm=sum([...out.values()]);for(let [z,a] of out)out.set(z,div(a,norm));memo.set(key,out);return out;
   }
   let dsets=[dom,dom.map((a,i)=>i===0?[a[0]]:a)];
   for(let dd of dsets)for(let b=0;b<G.length;b++){
    let exact=brute(dd,factors,b),p=dist(dd,factors,b,-1);
    for(let z of dd[b]){ck(eq(p.get(z),f(exact.P.get(z),exact.Z)),"exact recursion");stats.marginalChecks++;}
    for(let L=0;L<=3;L++){let q=dist(dd,factors,b,L);let evs=[...dd[b].map(z=>[z]),...bd[b].map(v=>dd[b].filter(z=>bit(z,v)))];
     for(let ev of evs){let diff=sub(sum(ev.map(z=>p.get(z))),sum(ev.map(z=>q.get(z))));ck((diff[0]<0n?-diff[0]:diff[0])*(2n**BigInt(L))<=diff[1],"budget error");stats.truncationChecks++;}
    }
   }
  }
  stats.instances++;
 }
 for(let [n,E,G,J] of cases)for(let mode=0;mode<2;mode++)build(n,E,G,J??((1<<E.length)-1),mode);
 for(let k=1;k<=8;k++)for(let c=1;c<=64;c++)ck(BigInt(c)*2n**BigInt(c)*(2n**BigInt(2*k+3)-1n)<=2n*(2n**BigInt(2*(k+c)+1)-1n),"coefficient");
 return stats;
}
console.log(JSON.stringify(verify()));
```

## 7. Next

Remove the fixed interface-size restriction without losing the exact charged block observer. In particular investigate a per-interface-event recursion that does not enumerate 2^b states, or a decomposition into smaller parity-coupled interfaces with explicit error payments. Benchmark the tree-decomposition table constructor and long theta/ladder instances before making any practical speed claim. Preserve the full source matrix and signed branch data.
