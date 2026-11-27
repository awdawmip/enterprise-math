# R840 — Exact multi-anchor grid joint solver and radius-gap completeness

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_RATIONAL_CHECKED / NOT_REVIEWED.
Independent informed portable continuation, own EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91; r3-20261127-r840-own-read verified existing session metadata, no run, execution_authorized=false. Owner inventory original r3-20261127-r840-running-read WAITING_RESOURCE (GITHUB_PRIMARY_RATE_LIMIT; read-only automatic resume); no shared task claim or ownership mutation. Global entry same snapshot 4c3402536295b78dff1056a28dded6ae9227468f; ACTIVE worldview, global V4 P000 startup verified against original blob, frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389 P000 V5 dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer 3923890d77a02d84b772f789e6912dd14f220d14 read directly. Current continuation, portable and research-method rules read. This is an auxiliary certificate search problem; no original labels, signed joint moments, road matrices, branch identities, time order or common depth removed. No native BRC experiment. Inherits the oracle and observer hypotheses, not a proof of native Port realizability.

Sources: R839 f5840f229dc8d90cb25f1f6674751d0814f7ddd6:research_notes/portable_direct/R839_SHARP_LOCAL_KRAFT_CAP_AND_BOUNDED_WIDTH_SOLVER.md (sharp local grading cap and one-anchor min-product solver); R837 9d062156808e49e28ff18098f507ddd7c409bc1a:research_notes/portable_direct/R837_RATIONAL_GRID_PAYMENT_SEARCH_AND_SHARP_ROUNDING.md (grid monotone solver and gap); R834 and R835 as pinned in those notes (dependency cover and neighborhood Kraft); R836 continuous relaxation. No external novelty claim.

## 1. Exact multi-anchor finite-domain reduction
Fix finite explicit original dependency graph G, partition H of its labels into nonempty bundles, valid R834 analytic anchor cover A, positive rational b_f, rational R>1 and 0<eta<1. Original labels v have integer grading L_v and neighborhood Kraft sum <=1. R839 permits restriction to 0<=L_v<=M_v=max({0} union {deg(x)-1:x in N(v)}), for ANY fixed cover and partition, without losing feasibility or increasing the tail bound. Define u_f=b_f R^(L_f+2), w_H=prod_{f in H}(1+u_f)-1. Fix nonempty finite positive rational payment domains D_AH, independent of L (an empty domain is infeasible). A geometric choice is a_H=w_H(1)=prod(1+b_f)-1 and D_AH={a_H q^j<=1-eta:j>=0}. For each anchor A enumerate only its margin-valid state vectors x_A=(d_AH:H in A) with Q_A=prod(1+d_AH)<=2-eta. Define T_AH=prod_{K in A except H}(1+d_AK), r_AH=T_AH/(2-T_AH) in [1,infinity). Define cost C_A=(Q_A-1)/(2-Q_A). All are exact positive-rational arithmetic (cost nonnegative). For any bundle H let A_H be its incident anchors. Its entire family of directed R834 inequalities is exactly equivalent to
    w_H * prod_{A in A_H} r_AH <= min_{A in A_H} (d_AH*r_AH).
Indeed divide by the strictly positive r_AH for each directed inequality, and conversely multiply by it. Every bundle has an anchor. This is not the claim that a joint moment factors into marginals: this is only a repackaging of the existing sufficient certificate.

Introduce variables L_v and x_A, unary objective C_A(x_A), hard Kraft factors on N_G(v), and one hard bundle factor on the variable set H union {x_A:A in A_H} using the displayed inequality. Feasible assignments correspond exactly to margin-valid capped integer/grid certificates, in both directions. The min-sum objective sum_A C_A gives the least R834 log-tail coefficient available on these grids. In particular the bound E_k<= R^(-k)/(R-1)*sum C_A is optimized at fixed radius; the original signed observer at t=1 is unchanged. This is an exact grid optimum, not an exact continuous-payment optimum.

## 2. Bounded-width algorithm and cost accounting
Construct the primal constraint graph on L_v and x_A by making each Kraft scope and each bundle scope a clique. Given an elimination order of induced width t, construct exact tables (hard infeasible entries absent), then eliminate each variable by summing current factors containing it and minimizing over its finite domain. Store an attaining choice per remaining assignment; replace those factors with their minimized table. Induction on elimination shows every table is the optimal sum over the already eliminated variables belonging to it conditional on its boundary. Disjoint sets of eliminated variables justify summation, and absent entries implement infeasibility. The final constants give the minimum, and reverse backpointers recover a witness which can be directly checked with the original inequalities. This is standard finite-domain min-sum elimination applied to this particular nonuniform certificate system.

If K is maximum payment-grid cardinality, a=max_A |A|, Delta=max degree of G, then the maximum variable domain is at most D=max(1,Delta,K^a). Work and storage are O(poly(N,B') D^(t+1)), including enumeration of at most K^a anchor states and hard tables; N is explicit input size and B' bounds grid number bit length and computed rational bit lengths. Every factor arithmetic uses products/ratios of at most polynomially many explicit input rationals, powers <=Delta+1; intermediate cost sums contain at most |A| original unary costs (disjoint provenance), so numerator and denominator bit lengths polynomial in N and B'. For geometric grids K=O(1+B/(q-1)) with B input/derived base bit length; B' polynomial in N,B,1/(q-1), by R837. Thus fixed a,t and q>1 give a polynomial bit-time solver, and explicit 1/(q-1) dependence when variable q. No claim of general fixed-parameter tractability in width alone: exponent depends on t and a, nor of finding an optimal order in general.

A structural sufficient width bound: take the incidence graph between variables and hard-factor nodes (Kraft and bundle factors). If it has a supplied width-w tree decomposition and each factor has at most s=max(Delta,max_H(|H|+|A_H|),1) variables, replace each factor vertex in every bag by its complete scope and retain variable vertices. Every factor clique is then covered; the bags containing a variable are its old connected subtree plus subtrees of incident factors, each intersecting it by edge coverage. Hence primal treewidth <=(w+1)s-1. This separates anchor size a, bundle size/footprint s and graph width w; bounded original G treewidth alone does not bound arbitrary artificial-cover scopes.

## 3. Radius-gap completeness without a supplied grading
Use fixed bases a_H=w_H(1), fixed q in (1,2] and eta. The exact joint grid optimum is nondecreasing as R grows on the same grid (feasible sets shrink; costs independent of R). If a real-payment integer certificate exists at R2>R1>1 with this margin, truncate its grading by R839 at no cost, then w_H(R2)>=(R2/R1)^2 w_H(R1) by the nonnegative-coefficient activity polynomial. For q<=(R2/R1)^2 the R837 grid lemma supplies a witness at R1 for that same capped grading; the joint solver finds one without knowing the grading. Its minimum tail coefficient is no greater than the witness cost at R2, since the R837 returned payments are componentwise no larger than that witness and the cost is monotone. Failure at R1 excludes a real integer certificate at every R2>=sqrt(q)R1 with the specified margin, not at R1 itself. In particular rational radius bisection gives certified lower bounds and a multiplicative gray zone. If a continuous grading certificate is known to exist at R0 (nonnegative lengths), R836 rounds it at R0^(2/3), then the same argument applies when R1<=R0^(2/3)/sqrt(q) and R1>1. This latter guarantee is conditional; no continuous witness is needed by this DP algorithm. Fixed positive radius and inherited R835 enumeration/observer hypotheses yield deterministic FPTAS on this structurally bounded, gap-promised certificate class. No general exact integer-real feasibility result, no general Port FPTAS.

## 4. Exact executed verification
The following independent comparison exhausts all capped grading vectors and for each legal vector computes the componentwise least grid witness by direct directed R837 iteration. For fixed grading this also minimizes the tail objective, because that cost is coordinatewise monotone. The main solver uses anchor-state tables, the combined bundle capacity constraint, and min-sum variable elimination. Compare exact rational optimum or infeasibility and check backpointer reconstruction. Inputs: all labeled simple graphs with 2 or 3 vertices, plus the specified four-vertex path, cycle and star; singleton partition or merged first two labels; edge-induced projected anchors (deduplicated), singleton anchors for uncovered bundles; 3 exact weight/margin profiles, R=5/4, q=2. This is finite verification only, with no general-width performance benchmark.
```json
{
  "instances": 78,
  "success": 55,
  "failure": 23,
  "legalGradings": 96,
  "anchorStates": 1216,
  "factorRows": 278106,
  "eliminationRows": 611723,
  "maxWidth": 4,
  "gridUpdates": 154,
  "nonSingletonCases": 39,
  "recoveredWitnesses": 55
}
```
All assertions passed. No floating-point decisions.
```javascript
function replay(){
 const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a<0n?-a:a};
 const F=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b}let g=gcd(a,b);return [a/g,b/g]};
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),sub=(a,b)=>F(a[0]*b[1]-b[0]*a[1],a[1]*b[1]),mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]),le=(a,b)=>a[0]*b[1]<=b[0]*a[1],eq=(a,b)=>le(a,b)&&le(b,a),one=F(1),two=F(2),zero=F(0),prod=a=>a.reduce(mul,one),sum=a=>a.reduce(add,zero),pow=(a,k)=>F(a[0]**BigInt(k),a[1]**BigInt(k));
 const ok=(x,s)=>{if(!x)throw Error(s)};
 const stats={instances:0,success:0,failure:0,legalGradings:0,anchorStates:0,factorRows:0,eliminationRows:0,maxWidth:0,gridUpdates:0,nonSingletonCases:0,recoveredWitnesses:0};
 function each(ds,fn){const x=[];function rec(i){if(i===ds.length){fn(x.slice());return}for(let j=0;j<ds[i];j++){x[i]=j;rec(i+1)}}rec(0)}
 function instance(n,edges,merge,profile){
  const G=Array.from({length:n},()=>[]);for(const [v,w] of edges){G[v].push(w);G[w].push(v)}
  const H=merge?[[0,1],...Array.from({length:n-2},(_,i)=>[i+2])]:Array.from({length:n},(_,i)=>[i]);
  const owner=Array(n);H.forEach((hs,h)=>hs.forEach(v=>owner[v]=h));
  let A=[...new Set(edges.map(([v,w])=>[...new Set([owner[v],owner[w]])].sort((a,b)=>a-b).join(",")))].map(s=>s.split(",").map(Number));
  for(let h=0;h<H.length;h++)if(!A.some(a=>a.includes(h)))A.push([h]);
  const AH=H.map((_,h)=>A.map((a,i)=>a.includes(h)?i:-1).filter(i=>i>=0));
  const b=G.map((_,v)=>F(profile===0?1:1+(v%2),profile===2?48:32));
  const R=F(5,4),q=F(2),eta=profile===2?F(1,2):F(3,4),limit=sub(two,eta),cap=sub(one,eta);
  const M=G.map(N=>Math.max(0,...N.map(v=>G[v].length-1)));
  const activity=(h,L)=>sub(prod(H[h].map((v,i)=>add(one,mul(b[v],pow(R,L[i]+2))))),one);
  const base=H.map(hs=>sub(prod(hs.map(v=>add(one,b[v]))),one));
  const grids=base.map(x=>{let a=[];while(le(x,cap)){a.push(x);x=mul(x,q)}return a});
  const state=A.map(hs=>{let out=[];each(hs.map(h=>grids[h].length),k=>{let d=k.map((j,i)=>grids[hs[i]][j]),Q=prod(d.map(x=>add(one,x)));if(!le(Q,limit))return;let T=d.map((_,i)=>prod(d.filter((_,j)=>i!==j).map(x=>add(one,x))));out.push({k,d,Q,r:T.map(t=>div(t,sub(two,t))),cost:div(sub(Q,one),sub(two,Q))})});return out});
  stats.anchorStates+=state.reduce((s,x)=>s+x.length,0);
  const kraft=(ls)=>le(sum(ls.map(l=>F(1,1n<<BigInt(l)))),one);
  const feasibleBundle=(h,ls,ss)=>{let rr=[],dd=[];AH[h].forEach((a,i)=>{let j=A[a].indexOf(h);rr.push(ss[i].r[j]);dd.push(ss[i].d[j])});let total=mul(activity(h,ls),prod(rr));return dd.every((d,i)=>le(total,mul(d,rr[i])))};
  const domains=[...M.map(m=>m+1),...state.map(s=>s.length)];
  const fs=[],back=[];
  function tab(scope,fn){let map=new Map();each(scope.map(v=>domains[v]),x=>{stats.factorRows++;let y=fn(x);if(y!==null)map.set(x.join(","),y)});return {scope,map}}
  for(let v=0;v<n;v++)fs.push(tab(G[v],x=>kraft(x)?zero:null));
  for(let a=0;a<A.length;a++)fs.push(tab([n+a],x=>state[a][x[0]].cost));
  for(let h=0;h<H.length;h++)fs.push(tab([...H[h],...AH[h].map(a=>n+a)],x=>feasibleBundle(h,x.slice(0,H[h].length),x.slice(H[h].length).map((j,i)=>state[AH[h][i]][j]))?zero:null));
  const rem=new Set(domains.map((_,i)=>i));
  while(rem.size){let v,S,B;for(const u of rem){let C=fs.filter(f=>f.scope.includes(u)),T=[...new Set(C.flatMap(f=>f.scope))].filter(x=>x!==u).sort((a,b)=>a-b);if(S===undefined||T.length<S.length){v=u;S=T;B=C}}
    stats.maxWidth=Math.max(stats.maxWidth,S.length);let ix=new Map(S.map((u,i)=>[u,i])),choices=new Map();
    let nf=tab(S,x=>{let best=null,arg=null;for(let l=0;l<domains[v];l++){stats.eliminationRows++;let z=zero;for(const f of B){let y=f.map.get(f.scope.map(u=>u===v?l:x[ix.get(u)]).join(","));if(y===undefined){z=null;break}z=add(z,y)}if(z!==null&&(best===null||!le(best,z))){best=z;arg=l}}if(best!==null)choices.set(x.join(","),arg);return best});
    for(const f of B)fs.splice(fs.indexOf(f),1);fs.push(nf);back.push({v,S,choices});rem.delete(v)
  }
  let best=zero;for(const f of fs){let v=f.map.get("");if(v===undefined){best=null;break}best=add(best,v)}
  // Independent reference: exhaust only gradings, use R837 least-grid iteration for each.
  let ref=null;
  each(M.map(m=>m+1),L=>{
   if(!G.every(N=>kraft(N.map(v=>L[v]))))return;stats.legalGradings++;
   const w=H.map((hs,h)=>activity(h,hs.map(v=>L[v])));
   if(grids.some(g=>!g.length))return;
   let k=A.map(hs=>hs.map(()=>0));
   for(;;){
    let d=k.map((xs,a)=>xs.map((j,i)=>grids[A[a][i]][j])),Q=d.map(ds=>prod(ds.map(x=>add(one,x))));
    if(Q.some(x=>!le(x,limit)))return;
    let next=k.map(xs=>xs.slice()),changed=false;
    for(let a=0;a<A.length;a++)for(let i=0;i<A[a].length;i++){
     let h=A[a][i],phi=w[h];for(let D of AH[h])if(D!==a){let j=A[D].indexOf(h),T=prod(d[D].filter((_,t)=>t!==j).map(x=>add(one,x)));phi=mul(phi,div(T,sub(two,T)))}
     let j=k[a][i];while(j<grids[h].length&&!le(phi,grids[h][j]))j++;if(j===grids[h].length)return;
     next[a][i]=j;if(j!==k[a][i])changed=true
    }
    stats.gridUpdates++;
    if(!changed){let cost=sum(Q.map(x=>div(sub(x,one),sub(two,x))));if(ref===null||!le(ref,cost))ref=cost;return}
    k=next
   }
  });
  ok((best===null)===(ref===null),"feasibility mismatch");if(best!==null){ok(eq(best,ref),"objective mismatch");let X=Array(domains.length);for(let t of back.reverse())X[t.v]=t.choices.get(t.S.map(u=>X[u]).join(","));ok(G.every(N=>kraft(N.map(v=>X[v]))),"recovered Kraft");ok(H.every((hs,h)=>feasibleBundle(h,hs.map(v=>X[v]),AH[h].map(a=>state[a][X[n+a]]))),"recovered payments");ok(eq(sum(A.map((_,a)=>state[a][X[n+a]].cost)),best),"recovered cost");stats.recoveredWitnesses++}
  stats.instances++;stats[best===null?"failure":"success"]++;if(merge)stats.nonSingletonCases++;
 }
 for(let n=2;n<=3;n++){let E=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)E.push([i,j]);for(let m=0;m<2**E.length;m++)for(let merge of [false,true])for(let p=0;p<3;p++)instance(n,E.filter((_,i)=>m&(1<<i)),merge,p)}
 for(const E of [[[0,1],[1,2],[2,3]],[[0,1],[1,2],[2,3],[3,0]],[[0,1],[0,2],[0,3]]])for(let merge of [false,true])for(let p=0;p<3;p++)instance(4,E,merge,p);
 return stats
}
console.log(replay());
```

Next: remove the exponential dependence on anchor size/footprint using certified partial-product states (and explicitly track the cost of extra discretization), or exploit residual slack to search over cover/partition. Preserve the open original Port realization and joint-moment oracle problem. No mathematical admission, formal Result, independent review or shared task completion.
