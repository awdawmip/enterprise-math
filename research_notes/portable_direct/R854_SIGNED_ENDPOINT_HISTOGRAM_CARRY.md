# R854 — Signed-endpoint carry and endpoint-histogram compression for nonadjacent dyadic options

2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.
Informed portable continuation of R853 (73941ec123d4edd2e20a932f26a7b14d1db4641c:research_notes/portable_direct/R853_DYADIC_CARRY_TWO_SCOPE_EXACT_FEASIBILITY.md, blob bbd505b1c0339398d7619d365002e757d7aa607c, read at immutable ref). Existing own lane metadata EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91 recovered, metadata_only=true, no runs, execution_authorized=false. Prior owner request r3-20261128-r853-running-read SUCCEEDED, empty RUNNING as-of list at 2026-11-27T22:20:32.797761Z with Source drift. New request r3-20261128-r854-running-read last observed RUNNING/NATIVE_RUNNER before publication; no shared claim or task mutation. Global core entries matched immutable 1c00562cd2c09cb112cd2f20993112dc238c0f1b; ACTIVE worldview, global P000 V4, current normative/method/portable contracts read. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: p000_reality_foundation.json V5 (blob dc84bdae6595b5e237a2ad50d8b21916adb2e447), joint observer (blob 3923890d77a02d84b772f789e6912dd14f220d14) read; generated foundation package absent at pin (404); no repinning. Auxiliary positive certificate model only: no native BRC dynamics, native observer quotient, P000 change, claim or admission. Reuse R853's exact ceiling carry and cost-bin dominance, keeping witness identity, original option tables and provenance.

## 1. Problem and new theorem

There are n independent items (degree-two local anchor pairs in R853); each item i has base exponent b_i >=0 and a nonempty explicit option table. Option z has exponent a_iz >= b_i, first capacity increment 2^a_iz - 2^b_i, arbitrary nonnegative integer second increment v_iz, and nonnegative rational local cost c_iz. Choose one option per item, with total first and second increments at most A and B, respectively, both exact nonnegative integers; minimize total cost. Empty table or negative residual budget is infeasible. This includes independent nonadjacent two-length and multilevel single-label choices on side 1, paired with arbitrary finite local options on side 2. For actual labels of lengths M-a and M-b, subtract long baseline 2^b from the first Kraft capacity; the difference is exactly the stated increment. Derive each option's local allowed status and exact rational cost from its original anchor ceiling before DP; no shared propagation between anchors. If local choices have nontrivial native joint/signed relations, those are outside this sufficient statistic's scope and must remain in their original source.

Theorem: Let h be the maximum number of DISTINCT pending upper exponents possible at any step in the increasing-lower-exponent schedule described below (not number of simultaneously open intervals). With fixed h, exact same-radius feasibility and an FPTAS for total local cost exist in polynomial time in explicit input bit length and 1/eps. No capacity or analytic ceiling is relaxed. All options and original sums can be restored. This is stronger than bounded interval-overlap alone: n arbitrarily overlapping intervals may all have one common upper endpoint, giving h=1 even as n grows. Adjacent choices are processed as one immediate positive bit (R853).

## 2. Signed endpoint construction and exact observer

Represent a=b as zero; a=b+1 as +1 at bit b; a>b+1 as -1 at bit b plus +1 at bit a. This is exact: the latter sum is 2^a-2^b. It is NOT legal to choose these endpoint signs independently; one local option fixes both. Process levels t=0,...,m-1, where m=max(1,bit_length(A),1+max_i,z a_iz,1+max_i b_i), with empty maxima omitted. At start of t, let W_t be the signed weighted sum of already processed endpoint events at exponents <t; A_t=A mod 2^t. Define q_t=ceil((W_t-A_t)/2^t), which may now be negative. Store a histogram H(a) of scheduled positive endpoints at future levels, counts only (no zero entries). Release H(t) at the start of level t: q += H(t), delete that bucket. Process all items whose b_i=t in fixed order; choose their full option, add v and c immediately, then update q and H according to the endpoint representation. At end of level t with budget bit alpha_t, fold

    q <- floor((q+1-alpha_t)/2).

Proof: adding signed integer X at level t adds 2^t X to W, hence q+X exactly; ceil((ceil(z)+k)/2)=ceil((z+k)/2) for every integer k, including negative. The identity follows by testing each integer upper bound. Thus the fold is exact even for negative carry. At any intermediate event at level t each chosen item's partial contribution to W is between -2^t and 2^t; it is either zero, an unmatched negative start, a completed nonnegative difference, or an adjacent bit. Therefore -n <= q <= n: the budget low part is in [0,2^t), and ceil of its subtracted normalized sum lies in that range. All H counts are between 0 and n. At terminal level m all scheduled endpoints have been released, W is the actual nonnegative increment total, and 0<=A<2^m. Hence q_m>=0 and q_m=0 iff W<=A.

Define the potential future endpoint set after an event as the union of possible unreleased upper endpoints a>b+1 from already processed items. Its size is at most h; this set depends on the input/schedule, not on the chosen state. Actual histogram keys are a subset. Equal (q,H) at the same event has identical future carry and histogram transitions for any identical remaining option suffix; therefore identical terminal first-capacity acceptance. This is an exact finite-horizon constraint observer, not equivalence of entire chosen branch histories. Preserve a real witness and original tables. In particular equal counts at an upper endpoint can be combined without knowing which item emitted them because all original local cost and second-resource contributions were already charged at their respective decision events and no future item depends on their identities. Shared constraints with such a dependency would need more state.

For feasibility retain minimal exact second capacity V per (q,H); V dominance persists under identical suffixes, so exact feasibility and witness recovery follow. Pruning V>B is safe since all second increments are nonnegative. Terminal acceptance requires H empty, q=0 and V<=B. Return original options via backpointers.

State bound (2n+1)(n+1)^h; sharper per event (2n+1) product_a (d_a+1), where d_a is number of already processed items having an option scheduling a still-pending upper endpoint a. If binary long intervals have overlap w (counting simultaneously possible open items), an alternative representation retaining each pending binary choice yields 2^w in place of (n+1)^h; a direct histogram representation also has at most 2^w possible histograms since they are images of those w choices. Thus use min(2^w,(n+1)^h) for binary intervals. For at most D options per item a similar upper bound D^w applies when w counts items with possible unreleased endpoints and choices are considered already charged. For h fixed, arbitrary overlap is allowed. With D the maximum local option count, at most O((n+m)D(2n+1)(n+1)^h) candidate state operations; histogram updates/key comparison have polynomial overhead. Counts, budgets, exact costs and witness backpointers have polynomial bit size. Explicitly charge m (binary materialization width), local option enumeration and their actual integer/rational arithmetic; do not claim polynomial in a binary-encoded exponent without charging its expanded representation. This is polynomial in explicit dyadic input bit length for fixed h; not a general FPT algorithm in h alone.

## 3. Same-radius FPTAS

Scale nonnegative rational costs by product of their positive denominators (polynomial total bit length). For eps in (0,1], T=max(1,n+2m), K=ceil(2T/eps), rho=1+1/K. Zero gets its own bin; for positive scaled cost C, e=floor(log2 C), use key (e,floor(K(C/2^e-1))). Same-bin costs differ by at most rho. Keep minimum exact V per (q,H,bin(C)), tie-break by lower C. At most T trims: release, each option event, and fold. Induction for any feasible reference prefix after j trims: a stored representative has identical q,H, no larger V, and cost <=rho^j reference cost. Extending by the same option preserves exact coordinates and dominance; adding nonnegative cost preserves multiplicative domination. A trim retains the key, weakly decreases V, and raises cost by at most rho. Zero remains zero. Therefore at termination a feasible reference yields a feasible representative of cost <=rho^T OPT<=exp(eps/2)OPT<= (1+eps)OPT. Conversely all returned witnesses are real. Final minimum cost among accepted states has the stated bound, including OPT=0. With J=1+O(K times binary octave count of positive scaled cost range) the previous state and transition bounds are multiplied by J. The range is from the smallest positive option cost to n times the largest (all zero gives J=1). Both octave count and arithmetic bit lengths are polynomial. Same radius and exact local analytic ceilings hold because options were prefiltered at that radius; no residual payment or radius shrink is required here.

## 4. Distinguishing example and scope

A single item b=0 with options a=3 and a=4, same second increment, has identical signed carry immediately after choice (-1), but different pending endpoints. With A=10 the increments 7 and 15 straddle the constraint; a carry-only collapse can erase feasibility (give cost 7 to a=3, zero to a=4). The pending histogram is the explicit repair coordinate. Conversely 40 intervals with b=0,...,39 and a=80 have one common pending endpoint: require at least 20 selected by second budget B=20, each unselected consumes 1 second unit, selected consumes 0, first budget 20*2^80, selected cost 1, unselected cost 0. Every 20-selection is first-feasible and 21 or more is impossible since sum_i 2^b_i<2^40<2^80. Exact optimum 20, established analytically without brute force. This family illustrates arbitrarily large overlap with one histogram coordinate, not a new universal complexity bound. R852's grouped arbitrary multi-bit switches are not all single differences and can have unbounded endpoint width; no contradiction with hardness. General independent-label cases with unbounded endpoint diversity or more exact scopes, shared bundle propagation, native Port realization and joint observer remain open.

## 5. Exact executed evidence

The following V8 JavaScript uses BigInt for original capacity sums and scaled costs, and exact small integer carry/index/count operations. Deterministic seed 854. Exhaustively enumerate all explicit option combinations per small instance. Analytic cases construct strictly positive R=2 factors with local rational ceilings and costs, baseline capacities at M=9, two independent label choices (multiple on first, adjacent on second). For the wide 40-item common-endpoint case use the preceding proved optimum, not exhaustive enumeration. Large exponents to 231 exercise the materialized binary scale. Check feasibility-only and eps=1,1/2,1/10; recover original selected option identities and recheck capacities, local analytic ceilings, scaled costs, and relative cost bound. No native BRC computation is claimed. Results:
{"abstract":320,"analytic":120,"largeExponent":24,"wideSharedEndpoint":1,"edgeCases":4,"feasible":272,"infeasible":197,"bruteLeaves":250568,"solverCalls":1876,"transitions":447249,"releaseSteps":857348,"foldSteps":992390,"merges":196346,"maxStates":4048,"maxPendingKeys":5,"maxPotentialEndpointWidth":6,"witnessChecks":1088,"failures":0}

```js
function experiment(){
 const st={abstract:0,analytic:0,largeExponent:0,wideSharedEndpoint:0,edgeCases:0,feasible:0,infeasible:0,bruteLeaves:0,solverCalls:0,transitions:0,releaseSteps:0,foldSteps:0,merges:0,maxStates:0,maxPendingKeys:0,maxPotentialEndpointWidth:0,witnessChecks:0,failures:0};
 const ck=(p,m)=>{if(!p)throw Error(m)};
 const pow=t=>1n<<BigInt(t),bits=x=>x===0n?0:x.toString(2).length;
 const sum=a=>a.reduce((s,x)=>s+x,0n);
 let seed=854;function rnd(n){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return (seed>>>8)%n}
 function solve(items,A,B,eps){
  st.solverCalls++;
  if(A<0n||B<0n||items.some(i=>i.opts.length===0))return null;
  const n=items.length,m=Math.max(1,bits(A),...items.flatMap(i=>[i.b+1,...i.opts.map(o=>o.a+1)]));
  const K=eps?BigInt(Math.ceil(2*Math.max(1,n+2*m)*eps[1]/eps[0])):1n;
  const groups=Array.from({length:m},()=>[]);items.forEach((i,j)=>groups[i.b].push(j));
  function bin(c){if(!eps||c===0n)return "z";const e=bits(c)-1,p=pow(e);return e+":"+((c-p)*K/p)}
  function put(map,s){ck(Math.abs(s.q)<=n,"carry bound");st.maxPendingKeys=Math.max(st.maxPendingKeys,s.h.size);
   const key=s.q+"|"+[...s.h].sort((a,b)=>a[0]-b[0]).map(([a,k])=>a+":"+k).join(",")+"|"+bin(s.c);
   let old=map.get(key);if(old){st.merges++;if(old.v<s.v||(old.v===s.v&&old.c<=s.c))return}map.set(key,s)}
  let states=new Map();put(states,{q:0,h:new Map(),v:0n,c:0n,w:[]});
  function size(){st.maxStates=Math.max(st.maxStates,states.size)}
  const potential=new Set();
  for(let t=0;t<m;t++){
   potential.delete(t);
   let next=new Map();
   for(const s of states.values()){st.releaseSteps++;let h=new Map(s.h),d=h.get(t)||0;h.delete(t);put(next,{...s,q:s.q+d,h})}
   states=next;size();
   for(const j of groups[t]){
    const i=items[j];for(const o of i.opts)if(o.a>t+1)potential.add(o.a);
    st.maxPotentialEndpointWidth=Math.max(st.maxPotentialEndpointWidth,potential.size);
    next=new Map();
    for(const s of states.values())for(let z=0;z<i.opts.length;z++){
     const o=i.opts[z];st.transitions++;
     const v=s.v+o.v;if(v>B)continue;
     let q=s.q,h=new Map(s.h);
     if(o.a===t+1)q++;else if(o.a>t+1){q--;h.set(o.a,(h.get(o.a)||0)+1)}
     else ck(o.a===t,"bad exponent");
     put(next,{q,h,v,c:s.c+o.c,w:s.w.concat([[j,z]])})
    }
    states=next;size();
   }
   next=new Map();const bit=Number((A>>BigInt(t))&1n);
   for(const s of states.values()){st.foldSteps++;put(next,{...s,q:Math.floor((s.q+1-bit)/2)})}
   states=next;size();
  }
  let best=null;
  for(const s of states.values()){ck(s.h.size===0&&s.q>=0,"terminal");if(s.q===0&&s.v<=B&&(!best||s.c<best.c))best=s}
  return best;
 }
 function brute(items,A,B){
  let best=null;
  function go(j,a,b,c){if(j===items.length){st.bruteLeaves++;if(a<=A&&b<=B&&(best===null||c<best))best=c;return}
   const i=items[j];for(const o of i.opts)go(j+1,a+pow(o.a)-pow(i.b),b+o.v,c+o.c)}
  if(A>=0n&&B>=0n)go(0,0n,0n,0n);return best;
 }
 function check(items,A,B,kind,expected){
  st[kind]++;const ref=expected===undefined?brute(items,A,B):expected;
  st[ref===null?"infeasible":"feasible"]++;
  for(const eps of [null,[1,1],[1,2],[1,10]]){
   const s=solve(items,A,B,eps);ck((s===null)===(ref===null),"feasibility");if(!s)continue;
   let a=0n,b=0n,c=0n;const seen=new Set();
   for(const [j,z] of s.w){ck(!seen.has(j),"duplicate");seen.add(j);let i=items[j],o=i.opts[z];a+=pow(o.a)-pow(i.b);b+=o.v;c+=o.c;
    if(o.N!==undefined){ck(8n*o.N<=o.U*o.denP,"analytic ceiling");ck(o.c*o.denC===o.numC*o.scale,"analytic cost")}}
   ck(seen.size===items.length&&a<=A&&b<=B&&c===s.c&&b===s.v,"witness");
   if(eps)ck(c*BigInt(eps[1])<=ref*BigInt(eps[0]+eps[1]),"cost");
   st.witnessChecks++;
  }
 }
 function maxes(items){return [sum(items.map(i=>i.opts.reduce((a,o)=>{let b=pow(o.a)-pow(i.b);return a>b?a:b},0n))),sum(items.map(i=>i.opts.reduce((a,o)=>a>o.v?a:o.v,0n)))]}
 for(let z=0;z<320;z++){
  const n=1+z%6,items=[];
  for(let j=0;j<n;j++){const b=rnd(7),opts=Array.from({length:1+rnd(5)},()=>({a:b+rnd(7),v:BigInt(rnd(100)),c:BigInt(rnd(51))}));items.push({b,opts})}
  let [a,b]=maxes(items);check(items,BigInt(rnd(Number(a)+1)),BigInt(rnd(Number(b)+1)),"abstract")
 }
 for(let z=0;z<120;z++){
  const n=1+z%5,M=9,items=[],baseA=[],baseB=[];
  for(let j=0;j<n;j++){
   let b=rnd(7),d=rnd(8),ends=[b,b+1,Math.min(M-1,b+2+rnd(5))],u=BigInt(1+rnd(32)),v=BigInt(1+rnd(32)),U=[9n,10n,11n,12n][rnd(4)],opts=[];
   // R=2; long activities u/256 and v/256; shorter activities divided by 2^(exponent gain).
   for(const a of [...new Set(ends)])for(let y=0;y<2;y++){
    let p=256n*pow(a-b),q=256n*pow(y),N=(p+u)*(q+v),D=p*q;
    if(8n*N<=U*D)opts.push({a,v:BigInt(y)*pow(d),N,U,denP:D,numC:N-D,denC:2n*D-N})
   }
   baseA.push(pow(b));baseB.push(pow(d));items.push({b,opts})
  }
  let scale=1n;for(const i of items)for(const o of i.opts)scale*=o.denC;
  for(const i of items)for(const o of i.opts){o.scale=scale;o.c=o.numC*(scale/o.denC)}
  let [a,b]=maxes(items),A=pow(M)-sum(baseA),B=pow(M)-sum(baseB);
  if(a<A)A=a;if(b<B)B=b;if(A>=0n)A=BigInt(rnd(Number(A)+1));if(B>=0n)B=BigInt(rnd(Number(B)+1));
  check(items,A,B,"analytic")
 }
 for(let z=0;z<24;z++){
  const items=Array.from({length:5},(_,j)=>{let b=10+(j*37+z*13)%140;return {b,opts:[{a:b,v:pow(5+j*23),c:0n},{a:b+1,v:0n,c:pow(j*9)},{a:230+(z%2),v:pow(j*7),c:pow(100+j)}]}});
  let [a,b]=maxes(items);check(items,a/BigInt(1+z%4),b/BigInt(1+z%3),"largeExponent")
 }
 // 40 simultaneous long intervals, one common end. Zero option has second cost 1, chosen interval has second cost 0.
 // Require at least 20 switches; cheapest 20 cost 20; first cap admits any 20, no 21.
 const wide=Array.from({length:40},(_,j)=>({b:j,opts:[{a:j,v:1n,c:0n},{a:80,v:0n,c:1n}]}));
 check(wide,20n*pow(80),20n,"wideSharedEndpoint",20n);
 check([],0n,0n,"edgeCases");
 check([{b:0,opts:[]}],0n,0n,"edgeCases");
 check([{b:0,opts:[{a:0,v:0n,c:0n}]}],-1n,0n,"edgeCases");
 check([{b:0,opts:[{a:3,v:0n,c:7n},{a:4,v:0n,c:0n}]}],10n,0n,"edgeCases");
 return st;
}
console.log(JSON.stringify(experiment()));
```

## Next

Investigate whether the endpoint histogram itself has a smaller exact quotient using normalization/merging of pending counts at related exponents, and whether unbounded endpoint diversity with actual independent labels is weakly NP-hard or tractable. Explore a second dyadic capacity observer if both sides have sparse paired endpoints, with synchronized ordering/width rather than an independent reordering. Keep original selected witnesses and frozen scientific pins. No new formal Task or Result requested or claimed.
