# R805 — Boundary-charge residual transport and exact bridge separation

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation, not a shared Task claim or formal Result. Prior source R804 at dd46114ebeeaf96aff4e1fc8566763037d50235c:research_notes/portable_direct/R804_CYCLE_SUPPORTED_ANTISYMMETRIC_RESIDUAL.md, directly read, and frozen P000 V5 and joint-observer contract at a72226e2430ffa4786321ac86e7f0c599d5f0389, blobs dc84bdae6595b5e237a2ad50d8b21916adb2e447 and 3923890d77a02d84b772f789e6912dd14f220d14. ACTIVE worldview and current global entries (entry blobs verified together at 0a0be01ad4828a54dd3d74e2684c39d87ad06bc8) and continuation/portable/associated research policies read. Own recovery r3-20261126-0624-own-metadata verified original RESEARCHER session pointers, no RUN and execution_authorized=false. Owner inventory original request r3-20261126-0624-owner-read last observed RUNNING at research start; no absence of other owners inferred. This is a finite auxiliary signed CHARACTER observation of a positive counting model, not a native signed BRC computation, spatial slice theorem, or dynamics result.

## 1. Exact boundary-charge law

Reuse R804's road kernel multigraph K=(V,F), including loops and parallel roads, nonnegative symmetric matrix S_e and P_e=S_e+jj^T/2. Let eta_e=1/D_e in (0,1], and W(r) the R804 occupancy weight (r consists of incidence bits, not just vertex bits). Let A(r) consist of edges with both incidences occupied. At each occupied vertex all nonzero incidences share a sign sigma_v; introduce an independent fair auxiliary sign at an empty vertex as in R804. For T subset V, define Q_T as the unnormalized character observation with inserted product of sigma_v over v in T. Equivalently an empty vertex in T contributes zero after its auxiliary sign is summed. Define Q_empty=Q. Then exactly

 Q_T(J)= sum_r W(r) sum_{F' subset A(r) intersect J, partial F'=T} prod_{e in F'} eta_e,

where J is the set of retained antisymmetric channels, partial is the odd-degree vertex set, and loops count twice. Proof: expand each active retained factor 1+eta_e sigma_u sigma_v, multiply by the inserted character, and sum all independent signs. The sign exponent is even iff the odd-degree set is T. All surviving terms are nonnegative. This generalizes R804's empty-charge cycle law to nonempty charges. An arbitrary nonnegative function of incidence occupancy can multiply W without changing the identity. Original full P matrices and source paths remain necessary for stronger observers.

## 2. Exact feasible-charge criterion and bridge law

For free scalar character observations, every F' with partial F'=T has strictly positive coefficient: take all incidences occupied (a charged isolated vertex cannot occur as the boundary of F'). Thus Q_T(J)>0 iff each connected component of (V,J) contains an even number of vertices of T. Necessity is the handshake lemma. Sufficiency: select a spanning tree in each component, and include each parent edge iff its descendant side has odd T parity; the resulting forest edge set has boundary T.

For feasible T in the full graph, fix any bridge e and one side U of its component after deleting e. Every F' with partial F'=T satisfies

  1_{e in F'} = |T intersect U| mod 2.

Sum degrees modulo two over U; internal edges cancel and e is the sole crossing. Therefore:
* neutral bridge (even charge on U): delete J_e exactly for this character, keeping S_e.
* charged bridge (odd charge): all surviving terms require J_e; deletion gives Q_T=0. Replace P_e by the pure J_e factor exactly under this character, even though J_e alone is a signed matrix and not a positive physical mass. In the positive expansion this means forcing both endpoint incidences occupied and multiplying by S_e(1,1)*eta_e=1/2. Toggle the endpoint charge at each side, remove e, and contract each side independently with its forced occupied boundary incidence. The product of the two side character contractions times 1/2 equals the original observation. The vertex factors must still see the forced incidence; omitting it would introduce an erroneous empty-vertex activity.
* a nonbridge always appears in some T-join: toggle an incident simple cycle in any given T-join. Thus deleting its antisymmetric channel strictly decreases Q_T for the free character if T is feasible.

The bridge assertion holds for arbitrary nonnegative occupancy observations before the final sum; strictness is only guaranteed in the free case. For a family of charges, delete a bridge's anti-channel exactly for every member iff all feasible charges have even parity across that bridge. Infeasible charges are identically zero. This is an exact observer-specific compression criterion; R804's bridge deletion is recovered for T=empty. Charged bridges are not redundant. A charged bridge gives an exact rank-one separation in the parity-resolved observer even if its symmetric determinant is nonzero; neutral bridge rank-one separation additionally needs the R803 symmetric determinant to vanish or an explicit approximation payment.

## 3. Two-charge path certificate

For distinct s,t let T={s,t}. For fixed occupancy, any T-join contains a simple s-t path gamma. Choose one deterministically (e.g. ordered edge IDs) and remove its edges. The remainder has empty boundary. The map to (gamma,remainder) is injective, its weight factors, and relaxing edge disjointness and occupancy increases the nonnegative sum. Hence

 0 <= Q_{s,t}/Q <= min(1, sum_{simple s-t paths gamma in K} prod_{e in gamma} eta_e).

The bound 1 also follows because the inserted character is +/-1. No path implies zero. A path gamma gives a lower certificate: on occupancies activating all its edges, symmetric difference with gamma bijects even sets and T-joins; for each term its weight ratio is at least prod_gamma eta_e, since each eta_e<=1. Therefore
 Q_{s,t}/Q >= prod_gamma eta_e * Pr_Q(gamma subset A(r)),
where Pr_Q is the occupancy marginal of the full positive model, with weight W(r) times the even-subgraph polynomial normalized by Q. On a tree the path is unique and the exact relation is equality with this lower expression, because the only even set is empty and the unique T-join is the path. This identifies both the transport attenuation and the occupation gate, and avoids pretending that path strength alone determines the signed character. The same path upper bound can use the retained graph J and denominator Q_empty(J).

For a loopless simple graph max degree Delta>=2, eta_e<=rho and alpha=(Delta-1)rho<1, if graph distance is d>=1 the simple path sum is at most Delta*rho*alpha^(d-1)/(1-alpha), by bounding each length-l path count by Delta(Delta-1)^(l-1). For heterogeneous weights one may use a nonbacktracking-walk resolvent on directed edges when the weighted successor row sum is less than one. These are computable sufficient estimates, not universal decay on arbitrary short-road kernels.

## 4. Exact computation and future observation scope

For feasible T, choose one T-join F_T by the tree parity construction; all T-joins are the affine translate F_T XOR cycle space. There are 2^r terms, r=|F|-|V|+components. Each term retains its exact occupied edge gates; perform the same binary occupancy contraction as R804. The earlier O(poly(N) 8^r) arithmetic bound therefore applies to one charge, without rebuilding the cycle basis. On trees, one term suffices, and the R804 binary messages with forced incidences compute it in linear graph/arithmetic operations. Explicit road input, rational bit complexity, and the number of requested charges are counted separately. Do not conflate a full character family with a single scalar: there can be exponentially many charges. For a declared observation family, identify neutral vs charged bridges by a single postorder parity pass per charge, or carry bitsets for multiple charges. Character inversion of a finite vertex-sign marginal is standard Fourier inversion on {+1,-1}^V; empty auxiliary signs must be explicitly retained and are not a replacement for native endpoint-label provenance. The full incidence occupancy and original matrices remain available.

## 5. Actual finite verification

Executed the following deterministic JavaScript BigInt script in the current turn. It compares the direct 3-label endpoint contraction with the positive parity expansion for all vertex charges (including infeasible ones), tests every single-edge cut against the bridge/charge criterion, and verifies the path upper bound by exact integer cross-products. Input activities are b/16, b in {14,15,16}, roads scaled by 16^ell, doubled matrices avoid half-integral coefficients. Includes all labeled bipartite graphs for part sizes (1,1),(1,2),(2,1),(2,2),(2,3),(3,3), and triangle/theta/loop-bridge/square-tail weighted kernels with road lengths 1,2,4,8. No performance or native BRC experiment is claimed.

Actual output: {"graphs":602,"kernels":16,"characterChecks":35336,"singleCutChecks":155012,"bridgeChargedChecks":15200,"bridgeNeutralChecks":15200,"pathChecks":8502,"mismatches":0}

```javascript
function verify(){
 const I=()=>[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]];
 const M=b=>[[2n*BigInt(b),16n,16n],[16n,16n,0n],[16n,0n,16n]];
 const mul=(a,b)=>a.map(r=>b[0].map((_,j)=>r.reduce((s,x,k)=>s+x*b[k][j],0n)));
 const make=(u,v,seq)=>{let p=I();for(const b of seq)p=mul(p,M(b));return {u,v,p,s:16n**BigInt(seq.length),d:p[1][1]+p[1][2]}};
 const parity=x=>{let z=0;while(x){z^=1;x&=x-1}return z};
 const check=x=>{if(!x)throw Error("exact mismatch")};
 let stats={graphs:0,kernels:0,characterChecks:0,singleCutChecks:0,bridgeChargedChecks:0,bridgeNeutralChecks:0,pathChecks:0,mismatches:0};
 function test(n,E,b,kind){
   const N=1<<n,m=E.length,K=1<<m;
   let direct=Array(N).fill(0n),coeff=Array(K).fill(0n),bound=Array(K).fill(0);
   const masks=Array(n).fill(0);
   function rec(k,w){
     if(k===m){
       let act=0,neg=0;
       for(let v=0;v<n;v++){if(masks[v]){w*=16n;act|=1<<v;if(masks[v]===2)neg|=1<<v}else w*=2n*BigInt(b[v]);}
       for(let t=act;;t=(t-1)&act){direct[t]+=parity(t&neg)?-w:w;if(!t)break;}
       return;
     }
     const {u,v,p}=E[k];let a=masks[u],c=masks[v];
     for(let i=0;i<3;i++)for(let j=0;j<3;j++)if(p[i][j]){
       masks[u]|=i;masks[v]|=j;
       if(masks[u]!==3&&masks[v]!==3)rec(k+1,w*2n*p[i][j]);
       masks[u]=a;masks[v]=c;
     }
   }
   rec(0,1n);
   function exp(k,act,f,w){
     if(k===m){for(let v=0;v<n;v++)w*=act>>v&1?32n:2n*BigInt(b[v]);coeff[f]+=w;return;}
     let {u,v,p,d,s}=E[k],U=1<<u,V=1<<v;
     for(const [i,j,z] of [[0,0,2n*p[0][0]],[0,1,2n*p[0][1]],[1,0,2n*p[1][0]],[1,1,d]])if(z)exp(k+1,act|(i?U:0)|(j?V:0),f,w*z);
     exp(k+1,act|U|V,f|(1<<k),w*s);
   }
   exp(0,0,0,1n);
   let q=Array(N).fill(0n),cut=Array.from({length:m},()=>Array(N).fill(0n));
   for(let f=0;f<K;f++){
     let t=0;for(let j=0;j<m;j++)if(f>>j&1)t^=(1<<E[j].u)^(1<<E[j].v);
     bound[f]=t;q[t]+=coeff[f];for(let j=0;j<m;j++)if(!(f>>j&1))cut[j][t]+=coeff[f];
   }
   function components(skip=-1){
     let seen=0,cs=[];
     for(let v=0;v<n;v++)if(!(seen>>v&1)){let c=1<<v,old=0;while(old!==c){old=c;E.forEach((e,j)=>{if(j!==skip&&((c>>e.u&1)||(c>>e.v&1)))c|=(1<<e.u)|(1<<e.v)});}seen|=c;cs.push(c);}
     return cs;
   }
   let cs=components(),cuts=E.map((_,j)=>components(j));
   for(let t=0;t<N;t++){
     let feasible=cs.every(c=>!parity(c&t));check(direct[t]===q[t]&&(q[t]>0n)===feasible);stats.characterChecks++;
     for(let j=0;j<m;j++){
       let feasibleCut=cuts[j].every(c=>!parity(c&t));
       check((cut[j][t]>0n)===feasibleCut&&cut[j][t]<=q[t]);
       if(feasible){
         let bridge=cuts[j].length>cs.length;
         check((cut[j][t]===q[t])===(bridge&&feasibleCut));
         if(bridge){if(feasibleCut)stats.bridgeNeutralChecks++;else{check(cut[j][t]===0n);stats.bridgeChargedChecks++;}}
       }
       stats.singleCutChecks++;
     }
   }
   let D=E.reduce((s,e)=>s*e.d,1n);
   for(let u=0;u<n;u++)for(let v=u+1;v<n;v++){
     let sum=0n;
     function dfs(x,visited,num,den){
       if(x===v){sum+=num*(D/den);return;}
       E.forEach(e=>{let y=e.u===x?e.v:e.v===x?e.u:-1;if(y>=0&&!(visited>>y&1))dfs(y,visited|(1<<y),num*e.s,den*e.d)});
     }
     dfs(u,1<<u,1n,1n);
     check(q[(1<<u)|(1<<v)]*D<=q[0]*sum);stats.pathChecks++;
   }
   stats[kind]++;
 }
 for(const [p,q] of [[1,1],[1,2],[2,1],[2,2],[2,3],[3,3]]){
   let a=[];for(let i=0;i<p;i++)for(let j=0;j<q;j++)a.push([i,p+j]);
   for(let f=0;f<1<<a.length;f++)test(p+q,a.filter((_,j)=>f>>j&1).map(([u,v])=>make(u,v,[])),Array.from({length:p+q},(_,i)=>14+(i+f)%3),"graphs");
 }
 for(const [n,edges] of [[3,[[0,1],[1,2],[2,0]]],[2,[[0,1],[0,1],[0,1]]],[2,[[0,0],[0,1],[1,1]]],[5,[[0,1],[1,2],[2,3],[3,0],[3,4]]]])for(const l of [1,2,4,8])test(n,edges.map(([u,v],j)=>make(u,v,Array.from({length:l},(_,i)=>14+(i+j)%3))),Array.from({length:n},(_,i)=>14+i%3),"kernels");
 return stats;
}
console.log(JSON.stringify(verify()));
```

## 6. Next

Use the affine charge coordinate to build multi-terminal residual propagation and explicit error allocation on a prescribed family of boundary observations. For the free scalar, develop a polynomial heterogeneous nonbacktracking certificate and graph-aware selection of cut edges; investigate direct positive sampler for the tilted cluster model. General FPRAS remains open. Keep original paths, prefix joint relation, signed native BRC, common depth, time order and provenance separately.
