# R807 — Sharp activation envelope and exact cactus cut allocation

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable research; no shared claim or Result. Direct continuation of R806 at 27475d1940a1a3405969be768bb13f0cdb35a1f9:research_notes/portable_direct/R806_MULTI_CHARGE_CUT_AND_FINITE_NONBACKTRACKING_CERTIFICATE.md (immutable readback blob f28684644f6590583e8142436911dbd9937df5f6). Same frozen foundation commit a72226e2430ffa4786321ac86e7f0c599d5f0389; P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer blob 3923890d77a02d84b772f789e6912dd14f220d14 read. Global canonical snapshot 27baed547f04761b75781c9bf5b2f4008af052ba, ACTIVE worldview and applicable current rules. Own metadata request r3-20261126-0823-own-metadata verified the existing RESEARCHER SID; no RUN or execution authority. Owner query r3-20261126-0823-owner-read was in flight at latest observation before this derivation; no shared ownership assumed.

## 1. Sharp full-activation envelope for the scalar observer

Use R804–R806 nonnegative charge expansion on a finite simple road kernel G=(V,E). For any edge subset A, set
 Z(A)=sum_{F subset A, boundary F=empty} prod_{e in F} eta_e,
with 0<=eta_e<=1; zero edges may be removed. Keep the original occupancy weight W(r)>=0, independent of anti-channel deletion, and active edge set A(r). Thus Q=sum_r W(r)Z(A(r)), Q_J=sum_r W(r)Z(A(r) intersect J), Q_J>0 for retained set J. Let K(J)=Z(E)/Z(J).

Theorem: 1<=Q/Q_J<=K(J), and this is the optimal uniform multiplicative upper bound over arbitrary nonnegative occupancy weights if all-active occupancy is allowed. In particular 0<= (Q-Q_J)/Q <=1-1/K(J), or (Q-Q_J)/Q_J <=K(J)-1. This improves R804's cycle-product bound whenever overlapping cycle terms produce slack. It is a scalar-observer certificate, not a bound on all charged observations.

Proof: for edge e=uv not in S, the parity expansion gives Z(S+e)=Z(S)(1+eta_e c_S(u,v)), where c_S is the normalized two-charge sum, equivalently the two-point correlation under weights prod_{f in S}(1+eta_f sigma_x sigma_y) on independent uniform signs. Correlation is nonnegative and at most one. It is monotone under adding any nonnegative edge. Here is a self-contained justification: write 1+eta sigma_x sigma_y=(1+eta)[(1-p)+p 1_{sigma_x=sigma_y}] with p=2eta/(1+eta). Expansion and summation over signs gives an edge-set law proportional to 2^{k(F)} prod_{e in F} p_e prod_{e notin F}(1-p_e), where k includes isolated vertices. Given F, signs are independent fair per component, so c_S(u,v)=Pr(u and v connected). For 0<p_e<1 the single-edge conditional open probability is p_e if its endpoints are already connected by the other edges and p_e/(2-p_e) otherwise. Both are increasing in p_e and in the other-edge set by inclusion. Couple two finite heat-bath chains using the same chosen edge and same uniform draw, starting with nested empty sets; inclusion is preserved, and each chain converges to its stationary law (finite irreducible aperiodic chain). Connectivity probabilities are therefore ordered. Missing or forced edges p=0 or 1 follow by continuity of the finite spin expression with positive partition denominator. This proves the needed monotonicity without any external theorem assumption.

Now let R(A)=Z(A)/Z(A intersect J). Add one edge e to A. If e not in J the denominator is unchanged and numerator grows. If e in J, the ratio is multiplied by (1+eta_e c_A(u,v))/(1+eta_e c_{A intersect J}(u,v))>=1. Thus R(A)<=R(E). Q/Q_J is a convex combination of R(A(r)) with weights W(r)Z(A(r) intersect J)/Q_J. Equality is attained by concentrating W on all-active r. For actual fixed physical/Port occupancy weights this proves a bound, not that equality is attained.

## 2. Marginal cut cost, diminishing returns and polynomial certificate

Let C=E minus J. The exact logarithmic uniform budget f(C)=log K(E minus C) is normalized, nonnegative, monotone and submodular. Indeed, the marginal for adding e=uv outside C equals log(1+eta_e c_{J-e}(u,v)), which decreases as C grows by correlation monotonicity. This exact cost is generally not additive. Logs are only readouts: comparisons can remain rational.

For any order e1,...,eh of C set J0=E, Ji=J(i-1)-ei. Then
 K(Jh)=prod_i [1+eta_ei c_{Ji}(u_i,v_i)].
The next factor is 1 if endpoints disconnect (a bridge of the current retained graph), even when the edge was not an original bridge. This gives adaptive zero-budget deletion. For a computable rational upper bound, replace c_{Ji} by min(1,p_{Ji}(u_i,v_i)), where p is the simple-path product sum from R805; use R806's finite nonbacktracking path bound on Ji instead of enumerating simple paths if desired. No spectral restriction. The resulting product upper-bounds K, not just Q/Q_J. With exact simple-path sums this certificate is at most the R804 cycle product: every simple cycle meeting C contributes its weight to exactly the first removed edge on it, and 1+sum w <= prod(1+w). For finite nonbacktracking walks take the smaller of any available valid bounds. A fixed ordering can be evaluated by at most |C| calls to the finite vector recurrence in R806, polynomial in explicit rational input length. Exact K computation is not asserted polynomial in general.

## 3. Cactus: sharp uniform budget and polynomial exact resource allocation

A cactus here is a finite simple graph in which each edge is in at most one simple cycle. Its even edge sets are precisely unions of distinct simple cycles: split any even graph into cycles, and the graph's cycles are edge-disjoint; conversely any such union is even. Hence Z(A)=prod_{gamma subset A}(1+w_gamma), w_gamma=prod_{e in gamma}eta_e. Therefore the sharp envelope is
 K(E minus C)=prod_{gamma:gamma intersects C}(1+w_gamma).
For the scalar uniform certificate, every bridge has zero cost. Once any edge of a cycle is cut, all other edges of that cycle may be cut without increasing K. With unit positive reward per cut edge and target budget K<=1+epsilon, an optimum consists of all bridges and complete selected cycles. More generally for nonnegative integer rewards b_e, replace cycle length by sum of rewards. Let B be the total reward and start DP at bridge reward with cost 1. For each cycle gamma of reward b_gamma and factor k_gamma, update DP[x]=min(old[x],old[x-b_gamma]*k_gamma) (missing entries +infinity). Choose largest reward with DP<=1+epsilon. Induction on cycle list proves exact optimality for the stated uniform certificate. Compare rational products by integer cross multiplication; graph block extraction linear, DP O(mB) arithmetic operations and O(B) live states, with rational bit length bounded by the sum of edge input bits (plus linear overhead). With unit rewards B=m, this is polynomial O(m^2); binary-coded arbitrary rewards give a pseudo-polynomial bound. It optimizes certificate-feasible edge count, not general graph contraction width or actual fixed-W error.

## 4. Overlapping cycles: an unbounded improvement

For K_{2,k} with every eta=1/2, even edge sets select an even number of the k internally disjoint two-edge roads. With J empty,
 K=Z(E)=[(5/4)^k+(3/4)^k]/2,
whereas R804's simple-cycle product is (17/16)^{k(k-1)/2}. The exact sharp log budget grows linearly in k, whereas the old certificate's log grows quadratically. This is an unbounded gap; neither value is a measurement of actual W-dependent error. Display-only numerical examples: [{"k":10,"sharp":4.684769630432129,"old":15.303904344202078},{"k":20,"sharp":43.369672505389644,"old":100576.92585917668},{"k":50,"sharp":35032.46160840359,"old":1.7903994463147614e+32},{"k":100,"sharp":2454546732.6488633,"old":2.1293481544858145e+130}].

## 5. Exact calculation evidence

Executed the JavaScript BigInt verifier below. It uses denominator 4 per edge, including the boundary eta=1; evaluates all even subsets by parity and a subset zeta transform; checks full-activation envelope for every pair (A,C) in each graph; verifies decreasing exact marginal via cross multiplication and telescoping; tests all cuts on 32 cactus cases with 3 edge-disjoint cycles meeting at a common vertex and 0–2 bridges; compares DP with all cuts for every minimum requested cut size. Also verifies the K2,k formula for k=1..6 by direct even-subset enumeration. Graphs: all labeled simple graphs on 2..4 vertices and all 64 K2,3 subgraphs. Seeds set heterogeneous rational weights deterministically. Actual output: {"graphs":138,"activationRatioChecks":31380,"diminishingChecks":12337,"sequentialChecks":1488,"cactusCases":32,"cactusBudgetChecks":399,"cactusExactChecks":111616,"thetaChecks":6,"mismatches":0}. No independent review or native BRC run; no FPRAS implementation or general optimizer performance claim.

```javascript
function verify(){
 const stats={graphs:0,activationRatioChecks:0,diminishingChecks:0,sequentialChecks:0,cactusCases:0,cactusBudgetChecks:0,cactusExactChecks:0,thetaChecks:0,mismatches:0};
 const check=x=>{if(!x)throw Error("mismatch "+JSON.stringify(stats))};
 function partition(n,E,seed){let m=E.length,N=1<<m,Z=Array(N).fill(0n),weights=E.map((_,i)=>BigInt(1+(seed+i*3)%4)),D=4n**BigInt(m);
  for(let s=0;s<N;s++){let b=0,w=1n;for(let e=0;e<m;e++)if(s>>e&1){b^=(1<<E[e][0])^(1<<E[e][1]);w*=weights[e]}else w*=4n;if(!b)Z[s]=w;}
  for(let e=0;e<m;e++)for(let s=0;s<N;s++)if(s>>e&1)Z[s]+=Z[s^(1<<e)];return {Z,D,weights,N};}
 function test(n,E,seed){let {Z,N,weights}=partition(n,E,seed),all=N-1;
  for(let C=0;C<N;C++)for(let A=0;A<N;A++){check(Z[A]*Z[all^C]<=Z[all]*Z[A&~C]);stats.activationRatioChecks++}
  for(let J=0;J<N;J++)for(let K=J;;K=(K-1)&J){for(let e=0;e<E.length;e++)if(K>>e&1){let b=1<<e;check(Z[J]*Z[K^b]>=Z[K]*Z[J^b]);stats.diminishingChecks++;}if(!K)break;}
  for(let C=0;C<N;C++){let J=all,num=1n,den=1n;for(let e=0;e<E.length;e++)if(C>>e&1){let K=J^(1<<e);let loss=Z[J]-Z[K];check(loss>=0n&&4n*loss<=weights[e]*Z[K]);num*=Z[J];den*=Z[K];J=K;}check(num*Z[J]===den*Z[all]);stats.sequentialChecks++;}
  stats.graphs++;
 }
 for(let n=2;n<=4;n++){let E=[];for(let u=0;u<n;u++)for(let v=u+1;v<n;v++)E.push([u,v]);for(let s=0;s<1<<E.length;s++)test(n,E.filter((_,i)=>s>>i&1),s)}
 let E=[];for(let u=0;u<2;u++)for(let v=2;v<5;v++)E.push([u,v]);for(let s=0;s<64;s++)test(5,E.filter((_,i)=>s>>i&1),s);
 for(let k=1;k<=6;k++){let E=[];for(let v=2;v<2+k;v++)E.push([0,v],[1,v]);let m=E.length,N=1<<m,Z=0n;for(let s=0;s<N;s++){let b=0,w=1n;for(let i=0;i<m;i++)if(s>>i&1){b^=(1<<E[i][0])^(1<<E[i][1]);w*=1n}else w*=2n;if(!b)Z+=w;}check(2n*Z===5n**BigInt(k)+3n**BigInt(k));stats.thetaChecks++}
 const less=(a,b)=>a[0]*b[1]<b[0]*a[1],eq=(a,b)=>a[0]*b[1]===b[0]*a[1],mul=(a,b)=>[a[0]*b[0],a[1]*b[1]];
 for(let seed=0;seed<32;seed++){
  let lens=seed%2?[3,3,4]:[3,4,4],E=[],blocks=[],v=1;
  for(let l of lens){let mask=0,last=0;for(let i=0;i<l;i++){let nxt=i===l-1?0:v++;mask|=1<<E.length;E.push([last,nxt]);last=nxt;}blocks.push({mask,l});}
  let bridges=seed%3;for(let i=0;i<bridges;i++)E.push([0,v++]);
  const {Z,D,weights,N}=partition(v,E,seed),all=N-1;
  for(let b of blocks){let p=1n;for(let i=0;i<E.length;i++)if(b.mask>>i&1)p*=weights[i];let d=4n**BigInt(b.l);b.factor=[d+p,d];}
  let dp=Array(E.length+1).fill(null);dp[bridges]=[1n,1n];for(let b of blocks){let a=dp.slice();for(let i=0;i<=E.length-b.l;i++)if(dp[i]){let z=mul(dp[i],b.factor);if(!a[i+b.l]||less(z,a[i+b.l]))a[i+b.l]=z;}dp=a;}
  let brute=Array(E.length+1).fill(null);for(let C=0;C<N;C++){let f=[1n,1n];for(let b of blocks)if(C&b.mask)f=mul(f,b.factor);check(eq(f,[Z[all],Z[all^C]]));stats.cactusExactChecks++;let c=0;for(let k=C;k;k&=k-1)c++;if(!brute[c]||less(f,brute[c]))brute[c]=f;}
  for(let k=0;k<=E.length;k++){let a=null,b=null;for(let j=k;j<=E.length;j++){if(dp[j]&&(!a||less(dp[j],a)))a=dp[j];if(brute[j]&&(!b||less(brute[j],b)))b=brute[j];}check(a&&b&&eq(a,b));stats.cactusBudgetChecks++;}stats.cactusCases++;
 }
 return stats;
}
console.log(JSON.stringify(verify()));
```

## 6. Next

Extend the sharp activation envelope to selected boundary-charge ratios, or prove its limitations by explicit counterexample: charge-specific activation conditioning and normalization need independent treatment. Develop a practical ordering algorithm for adaptive nonbacktracking marginal certificates, and bounded-treewidth exact budget optimization beyond cactus. General tilted-cluster FPRAS remains open. Preserve complete P matrices, original prefix/branch sources, signed native BRC, time order and common depth; these observer-specific certificates do not delete the original records.
