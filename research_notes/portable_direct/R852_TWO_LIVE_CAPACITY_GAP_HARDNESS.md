# R852 — Two live exact capacities: radius-gap hardness and a one-pivot pseudo-polynomial frontier

2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.
Independent informed portable continuation of R851 (062575b1b0e97069440940cdf4b7a64d5cac378b:research_notes/portable_direct/R851_SCOPE_STREAMING_LIVE_ANCHOR_FRONTIER.md). Existing lane metadata EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91 read; no private execution authority established. R851 owner read succeeded with empty RUNNING list at its as-of snapshot and Source drift; R852 read r3-20261128-r852-running-read was RUNNING / NATIVE_RUNNER at last observation. No shared task mutation. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389 P000 V5 and joint observer read; generated startup 404; global P000 V4 and ACTIVE worldview read. Global entry blobs matched immutable c92bdf20ff18ecbf99b2f62fc9ad78d03cc1940e. Current normative/portable routes read. This is a positive auxiliary certificate model, not native BRC dynamics, not a physical slice or a quotient of joint/signed observations. All original witness identities and relations retained.

## 1. Two exact capacities obstruct even radius-gap feasibility

Use R851's finite explicit edge witness model, except permit scopes to interleave. Each edge belongs to exactly one Kraft scope and one anchor; its list may contain grouped labels with lengths L in [0,M] and weights b>=0. Capacity k=sum 2^(M-L); payment p(R)=prod(1+b R^(L+2)); scope base and bound exact nonnegative integers; anchor B=1 and ceiling U=9/8 (eta=1/2 is valid since U<=3/2). Live width counts vertices incident to both processed and unprocessed edges.

Theorem. The promise distinction YES (feasible at R2) versus NO (infeasible even at R1) is NP-hard under polynomial-time many-one reduction, already with at most two live Kraft scopes, one live anchor, two explicit witnesses per edge, and degree two at every anchor. R1=2 and R2/R1=1+1/[100(M+2)], where M is polynomial in input bit length. In particular a fully polynomial radius-gap algorithm with exact capacities, even when allowed to return arbitrary valid witnesses at R1 for YES, would imply P=NP. The exact feasibility decision on this constructed family is NP-complete. This is a weak-hardness reduction from PARTITION, not a strong-hardness result or a claim at a fixed constant radius ratio.

Proof. Input positive integers a_i with even total W=2T; odd totals can be rejected in advance or doubled. Set M=bit_length(2W+1); thus 2^M>2W and all bits used below fit. Create two scopes S1,S2, each incident to one edge of every anchor A_i; order edges (S1,A1),(S2,A1),(S1,A2),(S2,A2),... . The live anchors number at most one and the live scopes at most two. Each scope has bound 2^M and fixed base 2^M-(W+T), leaving W+T. This base is itself a sum of binary dyadic capacities of fixed boundary labels.

For each i and each scope, construct exactly two allowed explicit grouped witnesses, long and short. The distinguished label has positive weight b=1/(16*2^(M+2)), long length M, short length M-1. For every set bit 2^t in a_i-1 include one additional zero-weight label with long length M-t and short length M-t-1. Each individual length is nonnegative. These actual label lists have total capacities k_long=a_i and k_short=2a_i; zero-weight labels contribute factor 1. This construction uses O(log(a_i+1)) labels per edge and preserves their distinct identities. No restriction to all independent label combinations is claimed: the edge list contains the two specified grouped witnesses, as permitted by R851's explicit-list model.

At R1 the payments are p_long=17/16 and p_short=33/32. Thus two longs violate U=9/8 since (17/16)^2=289/256>288/256. At R2 set d=100(M+2), R2=2(1+1/d). For 0<=j<=M+2, (1+1/d)^j<=1/(1-j/d)<=100/99 by binomial expansion bounded by a geometric series. Therefore even the mixed product at R2 is at most (1+100/(99*16))(1+100/(99*32))<9/8. Two shorts cost no more. By monotonicity these same allowed/disallowed pair patterns hold for every radius in [R1,R2].

In any feasible assignment at least one short per anchor is required. Baseline capacity W in each scope comes from long options; each short adds a_i. The total additional budget of the two scopes is 2T=W, while at least W is required. All a_i>0 forces exactly one short per anchor, and each scope's additional load equals T. Thus feasible assignments correspond exactly to partitions. A partition gives a feasible witness at R2; no partition rules out every witness even at R1. Rational powers are polynomial-bit because M=O(log W) and the rational base and weight have polynomial bit length. The reduction, label lists, recovery and exact verification are polynomial. Taking eps=1/[100(M+2)] gives (R2/R1)^2>=1+eps with 1/eps polynomial, so the gap guarantee of R851 cannot extend merely by bounding the number of live capacity coordinates at two unless P=NP. Membership in NP for the exact finite-list problem follows by checking the selected rational witness products and integer capacities. This construction uses zero weights and explicit grouped witness lists, not unconstrained independent label sets nor a strictly positive-weight native Port claim.

## 2. One-pivot pseudo-polynomial generalization of R851

For any supplied interleaved edge order, let A_j and S_j denote live anchors and scopes after cut j. Set w=max |A_j|, residual scope budget H_s=B_s-b_s>=0. Use R851's bins of live residuals and closed incremental cost, same rho and radius-gap assumption. For each cut choose a pivot scope t_j in S_j (none if empty). In each key retain EXACT capacity counts of every live nonpivot scope, together with the residual/cost bins. Among candidates with that key retain one with minimum exact pivot capacity (ties arbitrary). All capacity counts are checked against H_s on every extension; when a scope closes it can be dropped from the future state. New scopes start at zero. Anchor closure is identical to R851: check ceiling before adding incremental cost and removing the residual.

Theorem. Under the hypotheses and radius gap of R851 except for scope contiguity, this algorithm returns a feasible witness at R1 of cost <= any reference feasible at R2. Per-cut state count is at most
  J^(|A_j|+1) * prod_{s in S_j minus {t_j}} (H_s+1).
Candidate transitions bounded by E D times the maximum such table size, with polynomial overhead in explicit input and witness bit length; J as in R851. If S_j is empty, take product=1. One may choose the largest H_s as the pivot separately at each cut, minimizing the displayed factor. In particular, bounded active widths and polynomially bounded budgets except the largest active scope suffice for a polynomial algorithm at inverse-polynomial accuracy. In general this is pseudo-polynomial, not fully polynomial in binary capacities.

Proof. Strengthen the R851 induction to componentwise capacity dominance for EVERY live scope. Extension by the reference's next option preserves each component and therefore cannot violate a scope budget. Closure of scope removes only a coordinate with no future incident edge. Before trimming, the residual and closed cost estimates hold by exactly the R851 monotone affine residual propagation and convex increment f_B(v). Within a cell all nonpivot capacities are identical to the candidate and the selected pivot capacity is no larger. Hence the entire capacity vector is no larger, even if the next pivot differs. All residual and closed-cost coordinates increase at most rho in the trim, and the original R851 alpha*rho^E<=1 invariant and final baseline argument apply. Every selected prefix is a real witness; backpointers recover identities and all exact constraints can be rechecked. Exact integer capacity arithmetic has polynomial bit length; table cardinality incurs the stated numerical-budget dependence. This is a proof of the general algorithm, not an executed general interleaved solver.

## 3. Why a capacity frontier can be exponentially large

In the same paired construction take a_i=2^i for i=0,...,m-1. Before adding final constraints, exactly-one-short assignments have capacity vectors (W+s,2W-s) for all s=0,...,W=2^m-1. They are distinct and pairwise incomparable. For example use H_s=2W at the observer cut, so none is excluded. Both longs violate the anchor ceiling and both shorts consume more total capacity, so no feasible pair assignment dominates any of these vectors. Thus even with no active residual coordinates after a paired prefix, an explicit componentwise-minimal capacity frontier may require 2^m states. This is an output-size lower bound, not a lower bound against implicit representation. The partition gap theorem above is the separate algorithmic obstruction. The positive model does not permit erasure of original joint observations.

## 4. Exact finite evidence

The following JS was executed with BigInt exact integer products for threshold comparisons, exact small safe integer capacities, complete enumeration of every binary edge pair assignment, and independent integer subset-sum bitset. Coverage: all ordered positive integer lists of lengths 1..5 with entries 1..5 and even total. It checks both radii, actual dyadic capacity construction, exact network feasibility equivalence, and subset DP for this reduction family (not the general one-pivot solver). Results:
{"instances":1952,"partitionYes":1625,"partitionNo":327,"assignments":1683800,"capacityValid":514385,"gapChecks":11712,"dyadicOptions":18552,"subsetDPChecks":1952,"failures":0}

```js
function experiment(){
 const stats={instances:0,partitionYes:0,partitionNo:0,assignments:0,capacityValid:0,gapChecks:0,dyadicOptions:0,subsetDPChecks:0,failures:0};
 const check=(x,m)=>{if(!x)throw Error(m)};
 function one(a){
  const W=a.reduce((x,y)=>x+y,0),T=W/2;if(W%2)return;
  const M=(2*W+1).toString(2).length, B=2**M,base=B-W-T;
  const d=100n*BigInt(M+2),n=2n*(d+1n), b=16n*(2n**BigInt(M+2));
  function p(l,r){let num=r[0]**BigInt(l+2),den=b*r[1]**BigInt(l+2);return [den+num,den]}
  const rs=[[2n,1n],[n,d]], ok=rs.map(r=>[0,1,2].map(q=>{let x=p(M-1,r),y=p(M,r);let u=q===0?x:q===1?x:y,v=q===0?x:y;return 8n*u[0]*v[0]<=9n*u[1]*v[1]}));
  check(ok.every(x=>x[0]&&x[1]&&!x[2]),"threshold");stats.gapChecks+=6;
  for(const ai of a){let ls=[M];for(let t=0;t<M;t++)if((ai-1)&(1<<t))ls.push(M-t);let k=ls.reduce((s,l)=>s+2**(M-l),0);check(k===ai&&ls.reduce((s,l)=>s+2**(M-l+1),0)===2*ai,"dyadic");stats.dyadicOptions+=2}
  let sub=1n;for(const ai of a)sub|=sub<<BigInt(ai);let yes=((sub>>BigInt(T))&1n)===1n;
  let feasible=false;
  for(let m=0;m<4**a.length;m++){stats.assignments++;let k1=base,k2=base,good=true;for(let i=0;i<a.length;i++){let z=(m>>(2*i))&3, x=z&1,y=z>>1;k1+=(x?1:2)*a[i];k2+=(y?1:2)*a[i];if(x+y===2)good=false}if(k1>B||k2>B)continue;stats.capacityValid++;if(good)feasible=true}
  check(yes===feasible,"partition");stats.instances++;stats.subsetDPChecks++;stats[yes?"partitionYes":"partitionNo"]++;
 }
 function rec(a,n){if(a.length===n){one(a);return}for(let i=1;i<=5;i++)rec(a.concat(i),n)}
 for(let n=1;n<=5;n++)rec([],n);return stats;
}
console.log(JSON.stringify(experiment()));
```

## Next
Seek a structural certificate for exact capacity dominance (e.g. independent label choices, bounded number of dyadic layers or bounded numeric nonpivot budgets), implement and verify the general one-pivot solver, and investigate whether positive-only weights and independently generated witness lists retain the gap hardness. Constant-radius-gap hardness remains open here. No native Port realization or complete joint moment observer is established.
