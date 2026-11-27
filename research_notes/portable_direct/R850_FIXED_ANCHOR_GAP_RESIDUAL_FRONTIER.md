# R850 - Fixed-anchor asymmetric residual frontier and certified gap solver

2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_RATIONAL_CHECKED / NOT_REVIEWED.
Informed portable continuation of R849, not shared Task execution. Own metadata EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91 / MCP-ec17f2f30fb8409f8e664eb29ae6c08c verified; no own runs and execution_authorized=false. Prior R849 RUNNING request succeeded with empty projection at 2026-11-27T18:16:40.692848Z; current original request r3-20261128-r850-running-read observation {"status":"SUCCEEDED","error":null,"as_of":"2026-11-27T19:21:36.492793+00:00","running":0,"next":null,"source":"7403583b0ed8aeffeb5d70744b93660c12c7cc9d","phase":"COMPLETE"}. No ownership or Result mutation.
Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 and joint observer read at pin; global V4, ACTIVE worldview and current normative/portable rules read. Global entry files matched snapshot deed81800d0f284a88dbfa89eba3e23b5e691c30. Source predecessor 4456e16091a8467dc1ac2a5b40494f799c0bc04d:research_notes/portable_direct/R849_FEEDBACK_EDGE_AND_WIDTH_TWO_FEASIBILITY.md; R847 1e96cadf2804d95507f8ab0551b1e67cf15a080b:research_notes/portable_direct/R847_GROUP_SEPARABLE_KRAFT_CAPACITY_RESIDUAL_FRONTIER.md. Auxiliary positive certificate model only; preserve original labels, joint relations, signed observations, roads, branch provenance and common depth; no native BRC calculation or independent review.

## 1. Model and theorem

In the R848/R849 finite explicit-list model, suppose there are g>=1 analytic anchors and n independent Kraft scopes. A simple bipartite incidence graph is allowed to be arbitrary, with any cycle rank. Each edge has a finite list of actual witnesses (k,p) with integer k>=0, rational p>=1. Each scope has a nonnegative fixed integer base and a capacity bound. A missing edge is an empty witness (0,1). No cross-scope shared grade or other coupling is assumed; if multiple groups occur at the same scope-anchor pair, first form its list or use the explicitly supplied scope alternatives. A local option consists of one witness on each incident edge satisfying that scope's exact capacity. At fixed g, enumerate at most D^g local options per scope (D maximum edge list cardinality, assume D>=1). Empty option set implies infeasibility.

For any complete selection define P_h=prod of p on anchor h, v_h=P_h-1, Q_h=B_h P_h with rational fixed base B_h>=1, ceiling B_h<=U_h<=2-eta, eta>0. If B_h>U_h, reject directly. Objective C=sum_h phi(Q_h), phi(Q)=(Q-1)/(2-Q). Theorem: for any rational 0<eps<=1 there is a list of actual complete selections W such that for EVERY capacity-feasible reference selection z there exists z' in W with v_h(z') <= (1+eps)v_h(z) for h<g and v_g(z')<=v_g(z). The last coordinate can be any chosen anchor. Every returned selection satisfies all Kraft capacities exactly. In particular g=1 requires only one exact minimum state; zero residuals remain zero. For fixed g, W and the algorithm have polynomial size and bit complexity in the explicit rational/integer input and 1/eps. Unlike R849's feedback-edge search, the exponent is independent of the number of cycles.

## 2. Proof and exact dyadic bins

Let K=ceil(2 max(1,n)/eps). For positive v, find integer e such that 2^e<=v<2^(e+1); use bin (e,floor(K(v/2^e-1))), and a separate zero bin. Each bin is the half-open interval [2^e(1+j/K),2^e(1+(j+1)/K)), 0<=j<K. The ratio of any two positive numbers in one bin is less than or equal to rho=1+1/K. Determine e using numerator and denominator bit lengths and exact integer comparison, then j using integer division; no floating point or transcendental computation is required.

Initialize one state with all products 1 and an empty witness. Process scopes in any order. For each state and every feasible local option, multiply each product by its option factor. Group the resulting states by the vector of bins of the first g-1 residuals; in each cell keep a state with minimum EXACT last product, with original selection pointers. No rounding of an actual product or capacity is performed.

Proof by induction over scope count i. For every prefix reference, a retained prefix has first g-1 residuals at most rho^i times the reference and last residual no greater. Extend the inductive witness with the SAME next scope option as the reference. This is legal because the scopes have independent Kraft capacities; the earlier selections do not affect its capacity. For p>=1, T_p(v)=pv+p-1 preserves one-sided multiplicative residual dominance, since T_p(lambda v)<=lambda T_p(v) for lambda>=1. It also preserves exact last-coordinate order. Replacing by the cell's minimum last product can increase each other residual by at most rho; zero remains zero. Induction closes. rho^n<=exp(eps/2)<=1+eps by log(1+eps)>=eps/2 for eps<=1. For n=0 the initial state is exact. All states are actual original assignments, not virtual rounded capacities. This proof establishes only a positive-resource future-operation observer, not a quotient of native joint/signed information.

Bit cost: a positive partial residual on anchor h is at least a_h=min over all positive edge residuals (p-1), ignoring anchors with no positive option (always zero). It is at most H_h=prod of maximal factors of its incident edges minus 1. These rational bounds have polynomial bit length in explicit input because each edge contributes at most one factor. Thus the number of possible occupied octave indices is O(1+log_2(H_h/a_h)); the bin count J_h=O(1+K(1+log_2(H_h/a_h))) including zero. For an always-zero anchor take J_h=1. Let S=prod_{h<g} J_h (empty product 1). The candidate transition bound is O(S sum_i D_i^deg(i)) where D_i is the largest list at scope i, at most O(n S D^g). Local enumeration, exact integer Kraft comparison, rational multiplications, bin calculation and comparison are all included up to polynomial bit factors. Backpointers store O(n S) states, or copied witnesses at polynomial additional cost; selected output revalidation reads original lists. For fixed g, all these quantities are polynomial in total input bits and 1/eps. This is not FPT in g alone and is not a general treewidth result. If original grades are implicit, first account for list construction separately (R847 for explicitly bounded grades).

## 3. Three-way exact-certifying gap decision

Use actual ceilings U_h and exact witness revalidation to find the minimum exact C over W satisfying all original analytic ceilings. If found, return YES and the witness. If none, test the relaxed ceilings U_h^+=B_h[1+(1+eps)(U_h/B_h-1)] for h<g, U_g^+=U_g. If no retained witness satisfies these relaxed ceilings, return certified NO: any feasible original reference would have supplied such a retained witness by the theorem. Otherwise return UNKNOWN, never an unsupported exact infeasibility assertion. Relaxed ceilings can exceed 2; only compare products there, never evaluate phi at them.

If there exists an original reference with v_h <= (U_h/B_h-1)/(1+eps) for h<g and v_g <= U_g/B_g-1, a true feasible witness is guaranteed. More strongly, a reference whose residuals satisfy (1+eps)v_h <= target_h for h<g and v_g<=target_g has a witness componentwise within the targets. Last anchor needs no promise slack. This separates exact-capacity protection from approximate residual search. R849's NP-complete exact problem is not solved unconditionally; exponentially narrow gaps may yield UNKNOWN.

## 4. Radius-gap corollary for pendant factors

Assume each edge witness has a radius-independent encoding/capacity identity and product p_e(R)=prod_{f in e}(1+b_f R^(L_f+2)), b_f>=0, integer L_f>=0. Bases B_h(R)>=1 are nondecreasing in R (constant is allowed). No retained shared-bundle propagation constraint is present. Fix rational R2>R1>1 and run the above algorithm on the lists at R1, with original ceiling U_h<=2-eta. Every nonconstant monomial of P_h(R)-1 has degree at least 2, with nonnegative coefficients. Hence v_h(R1)<=(R1/R2)^2 v_h(R2). If (R2/R1)^2>=1+eps, apply the frontier theorem to the R2 reference identity at R1: all first g-1 residuals after trimming are <= v_h(R2), and the last is <= v_g(R2) even without the eps loss. Together with B_h(R1)<=B_h(R2) this gives Q_h'<=Q_h(reference at R2), preserving the reference safety and C'<=C_ref by monotonicity of phi on [1,2). Selecting the least exact feasible cost among the retained witnesses retains this bound. Thus polynomial gap search over arbitrary cycles at fixed g, with NO additional objective error. This is a cross-radius comparison, not a same-radius FPTAS for exact feasibility.

If using R847 lists with local error delta at R1, use an intermediate radius Rmid: if (Rmid/R1)^2>=1+delta, each substituted edge residual is <= its reference at Rmid while its Kraft capacity weakly decreases. Product monotonicity then yields whole-anchor residual at most v_h(Rmid). If (R2/Rmid)^2>=1+eps, the above trimming pays its error from the remaining gap. Sufficient combined condition (R2/R1)^2 >= (1+delta)(1+eps); intermediate real radius only used in proof. Local list error and global trim act on overlapping coordinates, so no max-loss assertion without an additional argument. This corollary keeps all actual encoding witnesses. General retained inter-anchor propagation (R840/R844) is not included.

## 5. Exact finite checks

Self-contained JS BigInt rational arithmetic. R849 regression: every ordered positive weight list of size 1..4 with entries 1..5 and even total; construct exact R849 edge factors and constant base with R2=2, R1=3/2, eps=1/2. Check R2 frontier coverage and three-way soundness by exhaustive capacity-valid selections, compare R2 feasibility with PARTITION, and verify R1 feasible optimum bound and componentwise witness for every R2-feasible instance. Additional 48 deterministic generic cases with 1..4 anchors, three scopes, missing edges, variable capacities and rational options; eps=1/3; all complete capacity-valid assignments checked against frontier. Two extra boundary cases (zero residual and empty feasible local set). Original witness recomputation on all retained states in the audit and best R1 witnesses. Counters: {"partition_cases":390,"partition_yes":260,"partition_no":130,"generic_cases":48,"scope_options":9434,"complete_assignments":36449,"dp_runs":830,"transitions":32613,"replacements":972,"max_states":400,"coverage_checks":36449,"output_checks":6243,"exact_yes":280,"certified_no":20,"unknown":140,"radius_reference_feasible":260,"radius_checks":260,"failures":0}. This tests the finite auxiliary model; general theorem is analytic. No performance or native-dynamics claim.

```js
function experiment(){
 const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a};
 const F=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);let d=gcd(a<0n?-a:a,b);return [a/d,b/d]};
 const one=F(1),zero=F(0),add=(x,y)=>F(x[0]*y[1]+y[0]*x[1],x[1]*y[1]),sub=(x,y)=>F(x[0]*y[1]-y[0]*x[1],x[1]*y[1]),mul=(x,y)=>F(x[0]*y[0],x[1]*y[1]),div=(x,y)=>F(x[0]*y[1],x[1]*y[0]),cmp=(x,y)=>x[0]*y[1]<y[0]*x[1]?-1:x[0]*y[1]>y[0]*x[1]?1:0,le=(x,y)=>cmp(x,y)<=0,prod=a=>a.reduce(mul,one);
 const stats={partition_cases:0,partition_yes:0,partition_no:0,generic_cases:0,scope_options:0,complete_assignments:0,dp_runs:0,transitions:0,replacements:0,max_states:0,coverage_checks:0,output_checks:0,exact_yes:0,certified_no:0,unknown:0,radius_reference_feasible:0,radius_checks:0,failures:0};
 function check(b,msg){if(!b)throw Error(msg)}
 function bin(v,K){
  let [a,b]=v;if(a===0n)return "z";
  let e=a.toString(2).length-b.toString(2).length;
  if(e>=0?a<(b<<BigInt(e)):(a<<BigInt(-e))<b)e--;
  if(e>=0)b<<=BigInt(e);else a<<=BigInt(-e);
  return e+":"+((K*(a-b))/b).toString();
 }
 function local(scope,g){
  let out=[];
  function rec(h,k,p,w){if(h===g){if(k<=scope.cap)out.push({p,w});return}
   for(let i=0;i<scope.lists[h].length;i++){let z=scope.lists[h][i];if(k+z.k<=scope.cap)rec(h+1,k+z.k,p.concat([z.p]),w.concat(i))}
  }
  rec(0,scope.base??0n,[],[]);stats.scope_options+=out.length;return out;
 }
 function all(options,g){let out=[];function rec(i,p,w){if(i===options.length){out.push({p,w});stats.complete_assignments++;return}for(let z of options[i])rec(i+1,p.map((x,h)=>mul(x,z.p[h])),w.concat([z.w]))}
  rec(0,Array(g).fill(one),[]);return out;
 }
 function solve(options,g,eps){stats.dp_runs++;let n=options.length,K=(2n*BigInt(Math.max(n,1))*eps[1]+eps[0]-1n)/eps[0],states=[{p:Array(g).fill(one),w:[]}];
  for(let op of options){let next=new Map();for(let s of states)for(let z of op){stats.transitions++;let p=s.p.map((x,h)=>mul(x,z.p[h]));let key=p.slice(0,g-1).map(x=>bin(sub(x,one),K)).join("|"),old=next.get(key);
    if(!old||cmp(p[g-1],old.p[g-1])<0){if(old)stats.replacements++;next.set(key,{p,w:s.w.concat([z.w])})}
   }states=[...next.values()];stats.max_states=Math.max(stats.max_states,states.length);
  }return states;
 }
 const q=(s,base)=>s.p.map((p,h)=>mul(p,base[h]));
 const feasible=(s,base,cap)=>q(s,base).every((x,h)=>le(x,cap[h]));
 const cost=(s,base)=>q(s,base).reduce((t,x)=>add(t,div(sub(x,one),sub(F(2),x))),zero);
 function best(arr,base,cap){let b=null;for(let s of arr)if(feasible(s,base,cap)){let c=cost(s,base);if(!b||le(c,b.c))b={s,c}}return b}
 function verify(s,scopes,g){let p=Array(g).fill(one);check(s.w.length===scopes.length,"witness length");for(let i=0;i<scopes.length;i++){let a=scopes[i],k=a.base??0n;for(let h=0;h<g;h++){let z=a.lists[h][s.w[i][h]];k+=z.k;p[h]=mul(p[h],z.p)}check(k<=a.cap,"Kraft witness")}check(p.every((x,h)=>cmp(x,s.p[h])===0),"product witness");stats.output_checks++}
 function audit(scopes,g,base,cap,eps){
  let op=scopes.map(s=>local(s,g)),ref=all(op,g),res=solve(op,g,eps),fac=add(one,eps);
  for(let s of ref){check(res.some(t=>t.p.every((x,h)=>h===g-1?le(x,s.p[h]):le(sub(x,one),mul(fac,sub(s.p[h],one))))),"frontier coverage");stats.coverage_checks++}
  for(let s of res)verify(s,scopes,g);
  let trueBest=best(ref,base,cap),got=best(res,base,cap);
  let relaxed=cap.map((u,h)=>h===g-1?u:mul(base[h],add(one,mul(fac,sub(div(u,base[h]),one)))));
  if(got){check(!!trueBest,"false yes");stats.exact_yes++}
  else if(!res.some(s=>feasible(s,base,relaxed))){check(!trueBest,"false no");stats.certified_no++}
  else stats.unknown++;
  return trueBest;
 }
 function part(a){
  let W=a.reduce((s,x)=>s+x,0);if(W%2)return;stats.partition_cases++;
  let M=16n*BigInt(W+1)**2n,T=BigInt(W/2),weights=a.map(BigInt);
  const x=weights.map(v=>F(v,M-v)),P=prod(x.map(v=>add(one,v))),theta=F(2n*M+2n*T+1n,2n*M),base0=div(F(3,2),mul(P,theta)),base=[base0,base0],cap=[F(3,2),F(3,2)];
  check(le(one,base0),"base");
  const scopes=(small)=>x.map(v=>{let short=small?mul(v,F(27,64)):v,long=small?mul(mul(v,F(2)),F(81,256)):mul(v,F(2));let opts=[{k:2n,p:add(one,short)},{k:1n,p:add(one,long)}];return {base:1n,cap:4n,lists:[opts,opts]}});
  let s2=scopes(false),s1=scopes(true),eps=F(1,2),ref=audit(s2,2,base,cap,eps);
  if(ref){stats.partition_yes++;stats.radius_reference_feasible++}else stats.partition_no++;
  let r1=solve(s1.map(s=>local(s,2)),2,eps),b1=best(r1,base,cap);
  if(ref){check(b1&&le(b1.c,ref.c),"radius objective");check(r1.some(t=>q(t,base).every((z,h)=>le(z,q(ref.s,base)[h]))),"radius domination");stats.radius_checks++}
  if(b1)verify(b1.s,s1,2);
  let partition=false;for(let m=0;m<2**a.length;m++)if(a.reduce((s,v,i)=>s+(((m>>i)&1)?v:0),0)===W/2)partition=true;
  check(!!ref===partition,"R849 partition");
 }
 function visit(a,n){if(a.length===n){part(a);return}for(let v=1;v<=5;v++)visit(a.concat(v),n)}
 for(let n=1;n<=4;n++)visit([],n);
 for(let g=1;g<=4;g++)for(let seed=0;seed<12;seed++){
  let scopes=Array.from({length:3},(_,i)=>({base:BigInt(seed%2),cap:BigInt(g+1+((i+seed)%g)),lists:Array.from({length:g},(_,h)=>{
   if((i+h+seed)%7===0)return [{k:0n,p:one}];
   let a=1+((i*5+h*7+seed*3)%11);return [{k:2n,p:F(64+a,64)},{k:1n,p:F(64+2*a,64)}]
  })}));
  let base=Array(g).fill(one),cap=Array.from({length:g},(_,h)=>F(5+(seed+h)%3,4));stats.generic_cases++;audit(scopes,g,base,cap,F(1,3));
 }
 // Exact all-zero, and empty local feasible set.
 audit([{cap:0n,lists:[[{k:0n,p:one}],[{k:0n,p:one}]]}],2,[one,one],[one,one],F(1,2));
 audit([{cap:0n,lists:[[{k:1n,p:one}],[{k:0n,p:one}]]}],2,[one,one],[one,one],F(1,2));
 return stats;
}
console.log(JSON.stringify(experiment()));
```

## 6. Next

Study a separator-local extension to unbounded number of anchors where at most a bounded number of analytic residuals cross the cut but Kraft scopes can be closed exactly. Multiple live capacity coordinates cannot simply be rounded upward or downward without paying a separate feasibility budget; derive a one-sided multi-capacity condition or counterexample. General shared-bundle propagation and native Port/joint moment observer remain open. Do not repeat the fixed-anchor proof or R849 PARTITION enumeration absent a specific verification purpose.
