# R838 — Exact joint integer grading/payment feasibility is NP-complete even for one anchor

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_RATIONAL_CHECKED / NOT_REVIEWED.
Independent portable TASK_RESEARCH, EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91. Own session metadata verified, execution_authorized=false, no run. The new RUNNING inventory request r3-20261127-r838-running-read was queued with EVENT_READ_CONTROL_BUSY at the derivation boundary; no shared ownership is inferred or changed. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 and joint-observer contract read directly (generated foundation package 404). Global canonical entry snapshot 206f1c3d2a4a684127fe8743f64ebc6054d8f3c5; ACTIVE worldview and current portable rules read. This is the auxiliary combinatorial observer/algorithm-certificate problem, not a native BRC time evolution or classical physical reference calculation. Preserve original signed joint moments, roads, branch identity, provenance, temporal order and common depth.

Direct source: R837 9d062156808e49e28ff18098f507ddd7c409bc1a:research_notes/portable_direct/R837_RATIONAL_GRID_PAYMENT_SEARCH_AND_SHARP_ROUNDING.md (fixed-grading payment algorithm, radius gap, sharp fixed-payment rounding); R836 2bcc65992adb4ae3b77cb1125554a25399c5752e:research_notes/portable_direct/R836_JOINT_NEIGHBOR_KRAFT_CONVEX_CERTIFICATE.md (fixed-payment singleton cap elimination and continuous relaxation); R835 5bbb0f700911cefec0c28aa434b0d73be0a4d6cf:research_notes/portable_direct/R835_NEIGHBOR_PREFIX_REGRADING_HIGH_GIRTH_OBSTRUCTION.md (neighborhood Kraft). Standard external complexity input: Alimonti and Kann, Some APX-completeness results for cubic graphs, Theoretical Computer Science 237 (2000), 123–134, DOI 10.1016/S0304-3975(98)00158-3, establishes hardness of minimum vertex cover for cubic graphs. The following reduction is new to this continuation.

## 1. Exact scope and decision problem

Fix R=2, eta=1/2, singleton bundles, one artificial analytic anchor containing every original label (permitted R834 cover, including extra edges), positive rational activities b_f=|alpha_f|lambda_f with lambda_f=1 fixed. The actual label dependency graph G for the R835 neighborhood Kraft constraint is unchanged, and may be bipartite of maximum degree 3. Choose nonnegative finite integer L_f and payments d_f satisfying

sum_{h in N_G(f)} 2^{-L_h} <= 1,  d_f >= b_f 2^{L_f+2},  prod_f(1+d_f) <= 3/2.

Because there is only one analytic anchor, all propagation products are empty. For any grading, the least payments are exactly d_f=b_f 2^{L_f+2}. Thus decision reduces to a purely discrete product constraint, with no floating point or continuous payment search.

Theorem: this fixed-cover exact joint feasibility decision is NP-complete, even with bipartite G of max degree 3, fixed R=2 and fixed eta=1/2. This is a restriction of R836/R837 certificate search, not a hardness claim about partition-function approximation, optimized arbitrary covers, optimized joint-moment envelopes, or native Port realizability.

## 2. Reduction from vertex cover

Given a nonisolated simple graph X=(V,E) of max degree 3, n=|V|>=2, m=|E|>=1 and integer 0<=K<=n, construct bipartite G on n+2m+1 labels. Keep an original label v for each vertex; for each edge e=uv add center a_e and private dummy z_e, with edges (a_e,u),(a_e,v),(a_e,z_e). Add an isolated padding label t. The maximum degree is 3. Use the same G for the original-label Kraft constraints, independent of the single analytic anchor.

Every endpoint in any feasible grading must have L>=1: L=0 would already consume all Kraft mass in a center neighborhood, which has two additional finite-length labels. Likewise two endpoints of one edge cannot both have L=1, since their total Kraft mass is 1 and the dummy has strictly positive mass. Consequently S={v in V:L_v>=2} is a vertex cover. This argument holds for arbitrary auxiliary lengths, even very large ones.

Conversely, any vertex cover S gives a feasible grading: L_v=2 on S, L_v=1 off S; L_{a_e}=L_{z_e}=2; L_t=0. Each center sees at most one length-1 endpoint and hence its Kraft sum <=1. Each original vertex sees at most three length-2 centers; each dummy sees one center; the isolated label has empty neighborhood.

## 3. Exact product budget isolates the cover size

Let b_v=1/(64n) for all original labels, b_{a_e}=b_{z_e}=1/(4096nm). Define p=1+1/(8n), q=1+1/(4n), r=q/p=1+1/(8n+1), s=1+1/(16n+2), T=p^{n-K}q^K s. Set padding factor P=(3/2)/T and b_t=(P-1)/4.

All weights are positive rational. Indeed p<=q, q^n<=1/(1-1/4)=4/3 by bounding each binomial coefficient by n^j and summing the geometric series. Also s<=19/18, so T<=38/27<3/2. Their total representation length is polynomial in input size (T's numerator/denominator have O(n log n) bits).

With the constructive grading from section 2 the auxiliary product is A=(1+1/(256nm))^{2m}<=1/(1-1/(128n))<s<r. The same binomial-to-geometric bound justifies the first inequality, and 128n-1>16n+2 justifies the strict second. Padding at length zero contributes exactly P.

If |S|<=K, the constructed full product p^{n-|S|}q^{|S|} A P <= p^{n-K}q^K A P < T P=3/2. Set payments to their minimal activities; the required margin holds.

If any feasible grading exists, extract its vertex cover S as above. Original label product is at least p^{n-|S|}q^{|S|}; auxiliary factors are >=1 and padding is >=P. If |S|>=K+1, the full product is >=p^{n-K}q^K r P > T P=3/2, contradiction. Hence X has a vertex cover of size <=K iff this fixed-anchor certificate is feasible. This proves NP-hardness using cubic vertex cover. The construction has O(n+m) labels/edges plus one explicitly listed anchor; exact rational construction is polynomial.

NP membership: positive rational b_f and product cap 3/2 imply every feasible activity b_f 2^{L_f+2}<=1/2. Hence L_f is O(bitlength(b_f)) and has a polynomial representation; exact dyadic Kraft sums and exact rational products can be verified in polynomial bit time. Minimal payments can be reconstructed rather than guessed. NP-completeness follows.

The reduction can use an actual auxiliary joint-moment model: independent Bernoulli(1/2) variables on G edges, each I_f the product over incident edges, and the isolated padding label with its own independent Bernoulli. Shared edge variables induce true dependencies, disjoint edge sets are independent, lambda_f=1 bounds all joint moments, alpha_f=b_f. Every joint moment is exactly 2^{-number of distinct selected edge/private variables}; all original observations remain recoverable. This realizes the stated auxiliary observer, not a native Port construction.

## 4. Consequences for automatic optimization

R836's fixed-payment integer-cap test and R837's fixed-grading grid algorithm are both polynomial in their respective declared scopes. Exact joint search cannot generally be replaced by an unconditional polynomial-time algorithm unless P=NP, even when the analytic problem has no propagation denominators. Alternating optimization may find certificates but does not become a complete polynomial solver merely by combining those two subroutines.

There is no contradiction with the earlier FPTAS: finding the *optimal/exact-feasible* grading at a specified radius/margin is different from approximating the partition function once a legal positive-radius witness is given or a promised gap is available. The reduction fixes lambda and cover; an algorithm allowed to redesign them is a different decision problem. A tractable follow-up is bounded-treewidth dynamic programming on the neighborhood-constraint hypergraph with the integer domains truncated by the above bit bound; another is a promise-gap constructive theorem using the R836 relaxation plus R837 grid and controlled slack, rather than exact global feasibility.

## 5. Exact finite replay

Enumerate all labeled simple graphs on 2..5 vertices, discard any with degree zero or >3. For every remaining graph and every K=0..n, enumerate all subsets S. Check the constructive grading's complete Kraft constraints iff S is a cover; check exact products for each cover against the fixed cap iff |S|<=K; for all |S|>K independently check the lower-bound obstruction ignoring auxiliary products. The symbolic proof handles arbitrary finite lengths and general sizes; the finite replay does not enumerate all length vectors and does not establish complexity hardness by experiment.

Executed JavaScript BigInt reduced rational arithmetic:
{
  "graphs": 558,
  "graphK": 3296,
  "endpointMasks": 101724,
  "kraftChecks": 101724,
  "exactProductChecks": 79946,
  "noncoverMasks": 64102,
  "coverMasks": 37622,
  "paddingChecks": 3296,
  "disagreements": 0
}

Reproduction (self-contained):
```javascript
function replay(){
 const gcd=(a,b)=>{while(b)[a,b]=[b,a%b];return a<0n?-a:a};
 const F=(a,b=1)=>{a=BigInt(a);b=BigInt(b);let g=gcd(a,b);return [a/g,b/g]};
 const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),sub=(a,b)=>F(a[0]*b[1]-b[0]*a[1],a[1]*b[1]),mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]),div=(a,b)=>F(a[0]*b[1],a[1]*b[0]),pow=(a,k)=>F(a[0]**BigInt(k),a[1]**BigInt(k)),le=(a,b)=>a[0]*b[1]<=b[0]*a[1],lt=(a,b)=>!le(b,a);
 const one=F(1),half=F(1,2),cap=F(3,2),ok=x=>{if(!x)throw Error("assertion")};
 let stats={graphs:0,graphK:0,endpointMasks:0,kraftChecks:0,exactProductChecks:0,noncoverMasks:0,coverMasks:0,paddingChecks:0,disagreements:0};
 for(let n=2;n<=5;n++){
  let es=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)es.push([i,j]);
  for(let mask=0;mask<2**es.length;mask++){
   let E=es.filter((_,i)=>mask&(1<<i)),m=E.length,deg=Array(n).fill(0);for(let [i,j] of E){deg[i]++;deg[j]++}
   if(deg.some(x=>x===0||x>3))continue;
   stats.graphs++;
   let A=Array.from({length:n+2*m+1},()=>[]);
   for(let e=0;e<m;e++){let [i,j]=E[e],a=n+2*e,b=a+1;for(let v of [i,j,b]){A[a].push(v);A[v].push(a)}}
   let p=F(8*n+1,8*n),q=F(4*n+1,4*n),aux=pow(add(one,F(1,256*n*m)),2*m),r=div(q,p),slack=F(16*n+3,16*n+2);
   ok(lt(aux,slack)&&lt(slack,r));
   for(let K=0;K<=n;K++){
    stats.graphK++;
    let T=mul(mul(pow(p,n-K),pow(q,K)),slack);
    ok(lt(T,cap));
    let pad=div(cap,T),bpad=div(sub(pad,one),F(4));
    ok(lt(F(0),bpad));stats.paddingChecks++;
    for(let S=0;S<2**n;S++){
     let k=0;for(let i=0;i<n;i++)if(S&(1<<i))k++;
     let cover=E.every(([i,j])=>(S&(1<<i))||(S&(1<<j)));
     let L=Array.from({length:A.length},(_,i)=>i<n?(S&(1<<i)?2:1):i===A.length-1?0:2);
     let kraft=A.every(N=>le(N.reduce((sum,v)=>add(sum,F(1,2**L[v])),F(0)),one));
     ok(kraft===cover);stats.kraftChecks++;stats.endpointMasks++;stats[cover?"coverMasks":"noncoverMasks"]++;
     let base=mul(pow(p,n-k),pow(q,k)),actual=mul(mul(base,aux),pad);
     if(cover){ok(le(actual,cap)===(k<=K));stats.exactProductChecks++}
     if(k>K){ok(lt(cap,mul(base,pad)));stats.exactProductChecks++}
    }
   }
  }
 }
 return stats;
}
console.log(replay());
```

Next: explicit tree-decomposition solver and promise-gap joint optimizer, with exact certificate output; retain the unresolved complete Port observer and native realization. No native BRC dynamical experiment or independent scientific review executed.
