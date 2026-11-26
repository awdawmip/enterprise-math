# R809 — Occupancy-paid transport and a normalization reversal at actual Port weights

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation, no shared CLAIM or Result. R808 fixed source 4790a8322ce39b434cfbb786fce8922c2db3c9c3:research_notes/portable_direct/R808_CHARGED_ACTIVATION_ENVELOPE_AND_TWO_PATTERN_EXTREMIZERS.md. R804 fixed source dd46114ebeeaf96aff4e1fc8566763037d50235c:research_notes/portable_direct/R804_CYCLE_SUPPORTED_ANTISYMMETRIC_RESIDUAL.md; R807 fc069513b1b5b6f758cb6e92e661cd9a91920c71. Frozen P000 V5 and joint-observer blobs dc84bdae6595b5e237a2ad50d8b21916adb2e447 and 3923890d77a02d84b772f789e6912dd14f220d14 at original foundation pin a72226e2430ffa4786321ac86e7f0c599d5f0389, directly read. ACTIVE worldview and current portable/continuation/research method and applicable account policies consulted; global entry snapshot c79aaf5d0ce73a25820f63a840ed693f1cd6e53c, entry blobs checked. Existing lane own metadata recovered using r3-20261126-1016-own-metadata, RESEARCHER, no RUN, execution_authorized=false. Active-owner query r3-20261126-1016-running-read last observed RUNNING at derivation (no empty inventory inferred). This is an auxiliary positive combinatorial observer, retaining native signed BRC, full matrices, branch provenance, time order and common depth.

## 1. The physical occupancy model, not arbitrary activation weights

Reuse R804 on a finite simple loopless road kernel G=(V,E). Each vertex has empty-site activity a_v in [7/8,1], otherwise activity 1. Each edge e=uv has two incidence bits i,j and symmetric occupancy matrix S_e=[[A,B],[C,D/2]] with nonnegative entries; A,D>0. It is the R803 symmetric channel from a road of length ell>=0 with internal a in [7/8,1], ell=0 meaning identity transfer. Its antisymmetric factor is eta_e=1/D (0<eta<=1) when both bits are occupied. Orientation fixes B,C. Let W(r)=2^|V| prod_v a_v^{1{all its incidences zero}} prod_e S_e(i,j). Let W(F)=sum_{r: all e in F have both bits occupied} W(r); W(empty)>0. Q_T(J)=sum_{F subset J, boundary F=T} eta(F) W(F), eta(F)=prod_{e in F} eta_e. J retains anti-channels only; W is unchanged. q_T(J)=Q_T(J)/Q_empty(J).

## 2. Exact local activity sandwich

Define alpha_e=(D/2)/(A+B+C+D/2) and beta_e=(D/2)/(A a_u a_v+B a_u+C a_v+D/2). For any F not containing e,
 alpha_e W(F) <= W(F+e) <= beta_e W(F).
Proof: condition on every incidence bit except the two of e. At each endpoint the local ratio of empty to occupied weight t_v is a_v if all other bits are zero, otherwise 1. The four edge weights are proportional to A t_u t_v, B t_u, C t_v, D/2. Thus the conditional probability of double occupancy lies between alpha and beta. Conditioning on all edges in F being doubly occupied merely restricts the other bits, so averaging preserves the bounds. All W(F)>0 by the all-occupied assignment. Iteration gives product lower and upper bounds for forcing any disjoint set of additional roads.

For R803 road matrices beta_e<=32/81 uniformly. Write the symmetric two-coordinate transfer as N(a)=[[2a,2],[1,1]], product [[A,2B],[C,D]]. For ell>=1 the first factor ensures row0>=7/4 row1 entrywise after multiplication, and the last factor ensures column0>=7/8 column1 after multiplication; hence A>=49D/32>=D. For ell=0, A=D=1. Dropping B,C from the denominator and using a_u a_v>=49/64 gives beta<= (1/2)/(49/64+1/2)=32/81. The exact beta may be much smaller. For ell=0 alpha=1/3, beta=1/(1+2a_u a_v). Define kappa^-_e=eta_e alpha_e and kappa^+_e=eta_e beta_e. In particular kappa^+<=32/81.

## 3. Charged increment, path and cycle bounds with actual occupancy payment

For e=uv not in J put b={u,v}; exact parity separation gives
 Q_T(J+e)-Q_T(J)=eta_e sum_{F subset J, boundary F=T xor b} eta(F) W(F+e).
Using section 2, this is between kappa^-_e Q_(T xor b)(J) and kappa^+_e Q_(T xor b)(J). This is a two-sided local transport law, not an independence approximation.

For any feasible T-join H subset J,
 q_T(J)>=prod_{e in H} kappa^-_e.
Proof: map each even F bijectively to F xor H; eta(F xor H)/eta(F)>=prod_{e in H} eta_e because eta<=1. Moreover W(F xor H)>=W(F union H)>=W(F) prod_{e in H minus F} alpha_e>=W(F)prod_{e in H} alpha_e. Sum the termwise bounds. For s!=t this yields the maximum over paths of the lower product.

For the upper path bound, fix s in nonempty even T. Each T-join contains a simple path gamma from s to some other t in T (the connected component has even odd-vertex count). For fixed gamma contained in F, delete gamma; this is injective into joins with boundary T minus {s,t}, and eta(F)W(F)<=prod_gamma kappa^+ times eta(F minus gamma)W(F minus gamma). Summing the relaxed cover yields
 q_T(J)<=sum_{t in T minus {s}} p^+_J(s,t) q_(T minus {s,t})(J),
 where p^+ is the sum of products of kappa^+ along all simple paths. In particular q_{s,t}<=min(1,p^+_J(s,t)). Iteration yields the R806 pairing upper bound with kappa^+ in place of eta.

For deletion C=E minus J, decompose each lost T-join into edge-disjoint simple cycles and paths pairing its odd vertices (successively remove paths between odd vertices until even, then cycles). At least one component touches C. For each candidate such component delete its edges and apply the same injection/payment. Therefore
 0<=Q_T(E)-Q_T(J)<= c^+_C Q_T(E) + sum_{unordered {s,t} subset T} p^+_C(s,t) Q_(T minus {s,t})(E),
 where c^+_C and p^+_C sum the corresponding simple cycles/paths meeting C with product kappa^+. This is the R806 bound with physical activation paid locally, and applies to the unchanged R804 W, not arbitrary W or arbitrary extra occupancy tests. Apply the same decomposition to obtain the R804 multiplicative cycle certificate with kappa^+ weights: for edge-disjoint components the forcing bound iterates, and relaxing disjointness over the recorded cycle list increases the nonnegative sum. More directly, the single-edge charged increment gives the scalar ratio at each deletion <=1+kappa^+_e min(1,p^+_(J-e)(u,v)); telescope over a chosen cut order. The finite nonbacktracking algorithms of R806 apply unchanged to the new rational strengths.

For a simple kernel with maximum degree Delta<=3, set rho=32/81. Then (Delta-1)rho<=64/81<1 regardless of the road lengths, including ell=0 where eta=1. For vertices at graph distance d>=1,
 q_{s,t}<=min(1,Delta rho [(Delta-1)rho]^(d-1)/(1-(Delta-1)rho)).
This follows by counting at most Delta(Delta-1)^(l-1) nonbacktracking walks of length l and summing the geometric majorant (Delta=1 use direct adjacency). Thus actual physical occupancy yields unconditional exponential distance decay in this bounded-degree class, unlike the earlier eta-only criterion. This is a correlation and certificate result, not a general partition-function FPRAS.

## 4. R808 normalization reversal occurs with actual, unmodified Port weights

Take a four-cycle through s=0 and a pendant bridge b=04 to t=4; uncontracted identity roads, eta=1. The graph is bipartite and realized by R799's construction, with c_v=2 deg(v), a_v=1-2^(-c_v-1), all within [7/8,1]. Each edge under W has either (0,0) weight 1 or (1,1) weight 1/2. Write p_b=Pr_W(b active), p_C=Pr_W(all four cycle edges active), p_bc=Pr_W(b active | cycle active). Deleting a single cycle anti-channel leaves a forest; exact expansion gives q'_st=p_b and q_st=(p_b+p_C p_bc)/(1+p_C). Conditional on all other edge bits, bridge activation probability is 1/(1+2a_t) if at least one cycle edge incident to s is active, and 1/(1+2a_s a_t)>1/(1+2a_t) if neither is active. The latter event has positive W mass. When the cycle is active, the first case is certain. Consequently p_b>p_bc and
 q'_st-q_st = p_C(p_b-p_bc)/(1+p_C)>0.
This establishes reversal without arbitrary reweighting, on a connected physically specified instance with c_v from the original construction. Exact values from the verifier: {"q":"82509312/226412519","qPrime":"1662464/4561815","increase":"10444865536/1032852025361985","cycleProbability":"2883584/223528935","bridgeProbability":"1662464/4561815","bridgeGivenCycle":"4/11"}.

## 5. Exact calculations and scope

Actually executed the following JavaScript BigInt verifier. For all labeled simple graphs with n=2..4, two configurations: uncontracted original activities c_v=2deg(v) (isolated c=3), and varied activities 7/8 or 1 with heterogeneous road lengths 0..3 and internal a=7/8 or 1. Plus the 5-vertex connected bipartite reversal example. It enumerates all 4^m incidence assignments, sums W(F) by subset transform, scales every road matrix by a common per-road denominator (2*8^ell), checks exact divisions for parity coefficients, then tests every forced ratio, edge increment for all charges and retained sets, T-join lower bound for all F subset J, and two-point upper bound for all J and vertex pairs. Counts: {"graphs":74,"configurations":149,"occupancyAssignments":32534,"forcedRatioChecks":3052,"uniformBetaChecks":415,"chargedIncrementChecks":49656,"joinLowerChecks":8571,"pairUpperChecks":9236,"reversalChecks":1}. All checks passed; the general cut inequalities use the above proof, not exhaustive cut tests. No native BRC execution, independent review or formal acceptance.

```javascript
function verify(){
  const stats={graphs:0,configurations:0,occupancyAssignments:0,forcedRatioChecks:0,uniformBetaChecks:0,chargedIncrementChecks:0,joinLowerChecks:0,pairUpperChecks:0,reversalChecks:0};
  function ck(ok){if(!ok)throw Error(JSON.stringify(stats))}
  const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a<0n?-a:a};
  const f=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);let g=gcd(a,b);return[a/g,b/g]};
  const add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]),sub=(a,b)=>add(a,[-b[0],b[1]]),cmp=(a,b)=>a[0]*b[1]-b[0]*a[1];
  const str=a=>a.map(String).join("/");
  function instance(n,E,seed,mode){
    let m=E.length,L=1<<n,N=1<<m,deg=Array(n).fill(0);
    for(let [u,v] of E){deg[u]++;deg[v]++}
    const ad=deg.map(d=>mode===0?(1n<<BigInt(d?2*d+1:4)):8n);
    const an=ad.map((d,i)=>mode===0?d-1n:BigInt(7+(seed+i)%2));
    const edges=E.map(([u,v],i)=>{
      let ell=mode===0?0:(seed+3*i)%4,A=1n,b=0n,c=0n,D=1n,s=1n;
      for(let j=0;j<ell;j++){let k=BigInt(7+(seed+i+j)%2);[A,b,c,D]=[A*2n*k+b*8n,A*16n+b*8n,c*2n*k+D*8n,c*16n+D*8n];s*=8n}
      const S=[2n*A,b,2n*c,D];
      const alpha=f(D,S.reduce((a,b)=>a+b,0n)),beta=f(D*ad[u]*ad[v],S[0]*an[u]*an[v]+S[1]*an[u]*ad[v]+S[2]*ad[u]*an[v]+D*ad[u]*ad[v]);
      ck(cmp(beta,f(32,81))<=0n);stats.uniformBetaChecks++;
      return {u,v,S,s,D,alpha,beta,lo:mul(f(s,D),alpha),hi:mul(f(s,D),beta)};
    });
    let W=Array(N).fill(0n);
    for(let mask=0;mask<4**m;mask++){
      let occupied=0,active=0,w=1n;
      for(let i=0;i<m;i++){let x=(mask>>(2*i))&3,e=edges[i];w*=e.S[x];if(x&2)occupied|=1<<e.u;if(x&1)occupied|=1<<e.v;if(x===3)active|=1<<i}
      if(w){for(let v=0;v<n;v++)w*=occupied>>v&1?ad[v]:an[v];W[active]+=w}
      stats.occupancyAssignments++;
    }
    for(let i=0;i<m;i++)for(let F=0;F<N;F++)if(!(F>>i&1))W[F]+=W[F|1<<i];
    let Z=Array.from({length:L},()=>Array(N).fill(0n)),boundary=Array(N).fill(0),lower=Array(N),upper=Array(N);
    lower[0]=upper[0]=f(1);
    for(let F=0;F<N;F++){
      let w=W[F],num=1n,den=1n;
      for(let i=0;i<m;i++)if(F>>i&1){let e=edges[i];boundary[F]^=(1<<e.u)^(1<<e.v);num*=e.s;den*=e.D}
      ck(w*num%den===0n);Z[boundary[F]][F]=w*num/den;
      if(F){let i=31-Math.clz32(F&-F),G=F^(1<<i);lower[F]=mul(lower[G],edges[i].lo);upper[F]=mul(upper[G],edges[i].hi)}
      for(let i=0;i<m;i++)if(!(F>>i&1)){let ratio=f(W[F|1<<i],W[F]);ck(cmp(ratio,edges[i].alpha)>=0n&&cmp(ratio,edges[i].beta)<=0n);stats.forcedRatioChecks++}
    }
    for(let T=0;T<L;T++)for(let i=0;i<m;i++)for(let J=0;J<N;J++)if(J>>i&1)Z[T][J]+=Z[T][J^(1<<i)];
    for(let J=0;J<N;J++){
      for(let F=J;;F=(F-1)&J){ck(cmp(f(Z[boundary[F]][J],Z[0][J]),lower[F])>=0n);stats.joinLowerChecks++;if(!F)break}
      for(let i=0;i<m;i++)if(!(J>>i&1)){
        let e=edges[i],b=(1<<e.u)^(1<<e.v);
        for(let T=0;T<L;T++){let delta=f(Z[T][J|1<<i]-Z[T][J]),base=f(Z[T^b][J]);ck(cmp(delta,mul(e.lo,base))>=0n&&cmp(delta,mul(e.hi,base))<=0n);stats.chargedIncrementChecks++}
      }
      for(let u=0;u<n;u++)for(let v=u+1;v<n;v++){
        function dfs(x,seen,prod){if(x===v)return prod;let sum=f(0);for(let i=0;i<m;i++)if(J>>i&1){let e=edges[i],y=e.u===x?e.v:e.v===x?e.u:-1;if(y>=0&&!(seen>>y&1))sum=add(sum,dfs(y,seen|1<<y,mul(prod,e.hi)))}return sum}
        ck(cmp(f(Z[(1<<u)^(1<<v)][J],Z[0][J]),dfs(u,1<<u,f(1)))<=0n);stats.pairUpperChecks++
      }
    }
    stats.configurations++;
    return {W,Z,edges};
  }
  for(let n=2;n<=4;n++){let E=[];for(let u=0;u<n;u++)for(let v=u+1;v<n;v++)E.push([u,v]);for(let g=0;g<1<<E.length;g++){const e=E.filter((_,i)=>g>>i&1);for(let mode=0;mode<2;mode++)instance(n,e,g,mode);stats.graphs++}}
  let {W,Z}=instance(5,[[0,1],[1,2],[2,3],[3,0],[0,4]],0,0),T=17,J=30;
  const q=f(Z[T][31],Z[0][31]),qp=f(Z[T][J],Z[0][J]),drift=sub(qp,q),pc=f(W[15],W[0]),pb=f(W[16],W[0]),pbc=f(W[31],W[15]);
  ck(cmp(drift,f(0))>0n&&cmp(pb,qp)===0n&&cmp(drift,mul(f(pc[0],pc[0]+pc[1]),sub(pb,pbc)))===0n);stats.reversalChecks++;
  return {stats,example:{q:str(q),qPrime:str(qp),increase:str(drift),cycleProbability:str(pc),bridgeProbability:str(pb),bridgeGivenCycle:str(pbc)}};
}
console.log(JSON.stringify(verify()));
```

## 6. Next

Use the two-sided forcing law to sharpen the actual Port multi-observer cut allocation; examine whether degree-three spatial mixing of the full local occupancy-and-sign specification can support a deterministic approximation algorithm for Q, rather than only the correlation bounds proved here. General tilted-cluster FPRAS remains open. Preserve full matrices and observer scope for future operations.
