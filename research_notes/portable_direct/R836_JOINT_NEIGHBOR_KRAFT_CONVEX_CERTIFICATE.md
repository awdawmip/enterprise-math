# R836 - Joint neighbor-Kraft and analytic-payment optimization

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.
Independent portable TASK_RESEARCH, own session metadata verified by r3-20261127-r836-own-read, EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91, execution_authorized=false, no own run. Owner inventory r3-20261127-r836-running-read was RUNNING during derivation; no shared task or Result mutation. Frozen science inherited from R835: a72226e2430ffa4786321ac86e7f0c599d5f0389, P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer 3923890d77a02d84b772f789e6912dd14f220d14 read. Current global entries at dc968e3a5a8e8201a859955158ba950741b96bc2, current ACTIVE worldview, portable and research method rules read. Frozen heartbeat machine companion path returned 404; current human method companion read; science pin unchanged. Auxiliary independent-group combinatorial observer only; no native BRC dynamics or residual attribution. Retain every original signed label, moment, road, branch, time and common-depth datum.
Dependencies: R835 5bbb0f700911cefec0c28aa434b0d73be0a4d6cf:research_notes/portable_direct/R835_NEIGHBOR_PREFIX_REGRADING_HIGH_GIRTH_OBSTRUCTION.md; R834 6fd1421bb2e12caf06677625b23706d5d04444bf:research_notes/portable_direct/R834_DEPENDENCY_COVER_QUOTIENT_AND_COST_REGRADING.md; R825 6ee4743d62741ab9898036d556175202ab6c76d8:research_notes/portable_direct/R825_ADAPTIVE_PREFIX_ENTROPY_PAYMENT.md. Reuse their exact oracle, independence and positive baseline hypotheses, not an independent review of them.

## 1. Fixed-radius joint convex feasibility

Fix the original explicit dependency supergraph G, a partition into analytic bundles H, and an analytic anchor cover A of their dependency graph. Original labels v have positive b_v=|alpha_v| lambda_v; zero-activity labels can be omitted for the declared observer only (retain original data). Assume exact polynomial-bit/time joint moment oracle, as in R835. Fix R>1. Relax prefix lengths to real ell_v>=0, and set u_v=b_v R^(ell_v+2). Set d_AH=exp(y_AH)>0, w_H=prod_{v in H}(1+u_v)-1, Q_A=prod_{H in A}(1+d_AH), T_A|H=prod_{K in A minus H}(1+d_AK). Fix a margin eta in (0,1). The joint constraints
    sum_{v in N(i)} exp(-ln(2)*ell_v) <= 1,
    log Q_A <= log(2-eta),
    log w_H + sum_{D in A_H minus A} log[T_D|H/(2-T_D|H)] <= y_AH
are convex in (ell,y). Empty neighborhoods impose no constraint. Proof: log(1+exp(y)) is convex (softplus), and log w_H is a log-sum-exp over nonempty subsets of H, each term being affine in ell. Its value and gradient do not require enumerating subsets: compute s=sum log(1+u_v), w=exp(s)-1; derivative of log w w.r.t. ell_v = (1+1/w)*ln(R)*u_v/(1+u_v). The log-sum-exp form proves convexity and the product form permits evaluation with a stable expm1/log1p implementation or certified precision. The function h(z)=z-log(2-exp(z)), z<log 2, has h'=2/(2-exp(z))>0 and h''=2 exp(z)/(2-exp(z))^2>0. Hence h(log T) is convex. Subtracting the affine y proves the result. There are polynomially many explicit variables and constraints for a given cover. The objective minimizing the R834 log bound can also be convexified: (Q-1)/(2-Q)=1/(2-exp(z))-1, convex increasing on z<log2, with z=log Q. This is a real relaxation, not an assertion of a uniform polynomial-time exact convex solver (numerical conditioning, bit complexity and strict feasibility matter). Feasibility is downward monotone in R; radius search can be performed at fixed R values. Joint optimization over R and ell is not claimed convex.

## 2. Safe integer recovery with a universal radius loss

Given a feasible relaxed point at R, choose L_v=ceil(ell_v). The neighborhood Kraft sums only decrease. For R_0=R^(2/3)>1, since 2(L_v+2)<=3(ell_v+2), R_0^(L_v+2)<=R^(ell_v+2). Thus every bundle w only decreases; the same d certifies the integer-graded polynomial at R_0. Any rational radius in (1,R_0] suffices. More precisely one may use R^theta with theta=min_v (ell_v+2)/(L_v+2), and zero lengths stay zero. If all original lengths are integral there is no loss. With polynomial-size rational d, R_0' and bounded/polynomial-bit powers, the final integer witness is checked by exact products and inequalities, with no need to trust the optimizer. For a real witness, rational approximation needs enough slack; no rational boundary witness or complexity guarantee is assumed. For fixed R_0'>1, fixed eta>0, polynomial-size witness and the R835 exact moment oracle, the R835 connected support enumeration gives a deterministic FPTAS, by the unchanged log remainder bound and c_v=L_v+2. Regrading preserves P_U(1) for every U exactly, not P_U(t) at general t.

## 3. Exact fixed-payment elimination for singleton bundles

For singleton bundles, fix rational R>1 and legal rational d, with Q_A<2. Define a cap for every label v:
    C_v=min_{A in A_v} d_Av * prod_{D in A_v minus A} (2-T_D|v)/T_D|v.
The analytic constraints are exactly b_v R^(L_v+2)<=C_v. If C_v<b_v R^2 for some v then infeasible. Otherwise define M_v=max{m integer>=0: b_v R^(m+2)<=C_v}. The integer joint feasibility question for these FIXED payments is equivalent to
    sum_{v in N(i)} 2^(-M_v)<=1 for every i.
Necessity: any allowed L_v<=M_v, so its Kraft sum is at least the one at M. Sufficiency: take L=M, satisfying both systems. No combinatorial code search is needed. Compute M by monotone rational power comparisons (doubling then binary search); for fixed R>1 and polynomial-bit rational caps, M is polynomially bounded, and all powers and dyadic sums have polynomial bit length. Without a fixed positive radius gap this bit-complexity statement needs care. The analogous continuous elimination uses ell_v=log_R(C_v/(b_v R^2)) and exact criterion sum_{v in N(i)} (b_v R^2/C_v)^(ln 2/ln R)<=1. The continuous formula is a real feasibility characterization, not an exact rational arithmetic algorithm. Bundle constraints for H with multiple labels are not separable into these individual caps. This exact integer oracle plus convex relaxation supplies two complementary search modes.

## 4. Strict separation from every uniform-length scheme at R>=4/3

For j>=8, Delta=2^j, take K_{2,Delta}, two hubs of degree Delta and Delta leaves of degree 2 (so the graph has no degree-one vertex). Independent Bernoulli bit per true edge with p=1-1/(100 Delta). I_v is the product of its incident edge bits; moments are p to the number of distinct incident edges, exactly and polynomially computable. Every hub envelope must be >=p^Delta>=99/100. Use R=4/3, hub |alpha|=1/16, other label |alpha|=1/[16 Delta R^(j+2)], and lambda=1 for the witness. Set hub L=1, other L=j. Every Kraft sum is exactly 1. Analytic singleton bundles and edge anchors, d_{A,hub}=1/4, d_{A,other}=1/(8 Delta). All Q_A=(5/4)(1+1/(8 Delta))<=85/64<2 for Delta>=2. Hub u=4/27, other u=1/(16 Delta). The hub constraint is
    (4/27)*[(1+d_other)/(1-d_other)]^(Delta-1) <= 1/4.
Indeed x=2/(8 Delta-1), Delta*x<=2/7. By the binomial bound sum binom(Delta-1,r)x^r <=sum (Delta*x)^r <=7/5, the left side <=28/135<1/4. The other-label constraint is (1/(16 Delta))*(5/3)=5/(48 Delta)<1/(8 Delta). Thus fixed radius, fixed margin, polynomial input and witness give R835 FPTAS. The original moments and signs are unchanged.
For any uniform integer length L on any original dependency supergraph, L>=j is necessary at a hub. At R'>=4/3, for a hub any lawful lambda has u>= (99/1600)*(4/3)^(j+2)>1 for j>=8 (base j=8, monotone). Any R834 witness with any analytic cover and bundle partition forces u<=w_H<=d_AH<1 since T/(2-T)>=1 and Q_A<2. Contradiction. Hence nonuniform prefix lengths strictly enlarge the certifiable class even allowing arbitrary analytic covering/bundling and optimized moment envelopes under uniform lengths. Scope: uniform-length R834/R835 certificate at R'>=4/3, not an impossibility at smaller radii or for unrelated algorithms. This family has unbounded degree, not unbounded treewidth (K_{2,Delta} has treewidth 2). The hubs' interpolation costs are 3 instead of j+2; the change does not remove any physical edge. This is a scoped auxiliary model, native Port realization still open.

## 5. Exact auxiliary verification and next frontier

Actual JavaScript BigInt/integer checks: 256 family inequalities for j=1..64; 57 uniform obstructions j=8..64; 16928 rounding inequalities for ell=m/q, q=1..32, m=0..32q; 75 labeled simple graphs on n=1..4, 5421 cap vectors in {0,1,2}^n, 84750 allocations within caps enumerated, zero disagreements with the cap elimination criterion. These finite checks support the exact stated scopes; general arguments are above. No numerical convex optimization, native BRC, or runtime speedup was executed. Next: derive a certified slack-aware search that returns rational witnesses or a scoped infeasibility certificate, improve integer radius recovery by exploiting actual neighborhood cap slack, and test native Port realization/oracle availability. Do not repeat R835 encoding or these proofs.

## Replay (JavaScript)
```javascript
function replay(){
 let stats={family:0,uniform_obstruction:0,rounding:0,graphs:0,cap_vectors:0,enumerated_allocations:0,disagreements:0};
 const ok=b=>{if(!b)throw Error("assertion failed")};
 for(let j=1;j<=64;j++){let D=1n<<BigInt(j);
 ok(5n*(8n*D+1n)<64n*D);stats.family++;
 ok(14n*D<=2n*(8n*D-1n));stats.family++;
 ok(4n*7n*4n<=27n*5n);stats.family++;
 ok(5n*8n<=3n*16n);stats.family++;
 if(j>=8){let k=BigInt(j+2);ok(99n*4n**k>=1600n*3n**k);stats.uniform_obstruction++}
 }
 for(let q=1;q<=32;q++)for(let m=0;m<=32*q;m++){let l=Math.ceil(m/q);ok(2*q*(l+2)<=3*(m+2*q));stats.rounding++}
 for(let n=1;n<=4;n++){let es=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)es.push([i,j]);
 for(let mask=0;mask<2**es.length;mask++){stats.graphs++;let adj=Array.from({length:n},()=>[]);es.forEach(([i,j],k)=>{if(mask&(1<<k)){adj[i].push(j);adj[j].push(i)}});
 let legal=L=>adj.every(ns=>ns.reduce((s,v)=>s+(1<<(2-L[v])),0)<=4);
 function caps(C){if(C.length<n){for(let c=0;c<=2;c++)caps([...C,c]);return}
 stats.cap_vectors++;let direct=legal(C),any=false;
 function enumerate(L){if(L.length<n){for(let l=0;l<=C[L.length];l++)enumerate([...L,l]);return}stats.enumerated_allocations++;if(legal(L))any=true}
 enumerate([]);if(direct!==any)stats.disagreements++;ok(direct===any)}
 caps([]);
 }}
 return stats;
}
console.log(replay());
```
