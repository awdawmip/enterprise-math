# R855 candidate — Canonical committed debt and synchronous exact dyadic capacity observers

2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.
Informed portable continuation of immutable R854: 8c3cd66609d2e6b47e83084251455aeba86da959:research_notes/portable_direct/R854_SIGNED_ENDPOINT_HISTOGRAM_CARRY.md (blob 7ba93151d3455d5e7fdf4cf0dc9f953df3847437). R853/R854 supplied exact ceiling carry and independent local option tables. Current control Source at status 83291ecba974f8976a92a63411797cbface14ea3; global entries matched immutable e32830d5f836c0df952c743cf5ed293f8b84b46e. Frozen science unchanged a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer blob 3923890d77a02d84b772f789e6912dd14f220d14. ACTIVE worldview and current portable/method/continuation rules read. Own lane metadata EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91; metadata_only=true, execution_authorized=false, no own runs. Prior RUNNING read r3-20261128-r854-running-read SUCCEEDED, empty as of 2026-11-27T23:21:54.926738Z, event pages revalidated; new read r3-20261128-r855-running-read queued at admission. No shared task mutation. This is a positive auxiliary certificate optimization model, not native BRC dynamics or a native observer quotient.

## 1. Model and theorem
There are n independent items with nonempty explicit local option tables. Each option z has a vector of r nonnegative dyadic capacity increments d_ij(z)=2^a_ij(z)-2^b_ij(z), integers a>=b>=0, and an exact nonnegative rational cost c_i(z). Choose exactly one option per item; each total S_j must be <= integer budget A_j>=0; minimize the additive cost. Zero increments allowed. In actual Kraft constraints subtract fixed long-label baselines before forming the increments; the theorem requires those baselines to be option-independent, with each nonzero difference corresponding to an allowed single label length change (or the general explicit auxiliary table). All local analytic ceiling tests and costs are determined from the original local options at a fixed radius, before this algorithm. No cross-item propagation or identity-dependent future choice is assumed. An empty option table or negative residual budget is infeasible.

For item i, let t_i be the minimum lower exponent of any nonzero increment across all its options and all coordinates; for an all-zero item set t_i=0. Sort items by t_i and a fixed tie order. At a stage with current exponent t, every unprocessed option is coordinatewise divisible by 2^t. Let H_j be the union of exponents >t in the signed endpoint representations of all options of processed items (ignore zero increments). Let h_j=|H_j|. If r and max over stages sum_j h_j are fixed, exact feasibility AND exact additive-cost minimization at the same radius are polynomial in explicit input bit length (charge materialized integer/exponent width). In particular, both sides can be compressed with no arbitrary-capacity dominance or FPTAS needed. The new canonical key is more compact than the histogram representation, even with one scope.

## 2. Canonical committed-debt coordinate and exact observer proof
For each coordinate and a processed prefix, let S be its FULL committed increment including future endpoints of selected options. Put A_t=A mod 2^t. Define
    Q_t = ceil((S-A_t)/2^t).
Unlike R854's signed partial carry, Q includes all pending endpoint debt; Q>=0 because S>=0 and 0<=A_t<2^t. It may be numerically large; the theorem bounds the number of reachable distinct values, not its numeric range.

For any fixed future suffix with total increment F divisible by 2^t,
    S+F <= A iff Q_t + F/2^t <= floor(A/2^t).
Proof: subtract A_t, divide by 2^t, and use the fact the right-hand budget and F/2^t are integers. Thus equal Q at the same stage yields the same terminal feasibility for EVERY identical suffix; equality of vector Q preserves simultaneous feasibility for all scopes. This is a finite-horizon factorization of the specified capacity observer, not an assertion of full native history equivalence.

Decision at layer t: Q_j <- Q_j+d_ij(z)/2^t, and charge exact cost. For a jump from t to u>t, let D=2^(u-t), a=(A>>t) mod D. Then
    Q_u = ceil((Q_t-a)/D).
Indeed A_u=A_t+2^t*a and for any real x and integer a,D>0, ceil((ceil(x)-a)/D)=ceil((x-a)/D); both sides have the same integer upper bounds. This also handles negative intermediate numerators. Therefore jumps between distinct t_i suffice. Initially t=0 and Q=0; after the last item accept precisely Q_j<=floor(A_j/2^t) for every j. Prefix rejection Q_j>floor(A_j/2^t) is safe since future increments are nonnegative.

Store the minimum exact cost per full vector Q with real backpointers. Equal keys have the same future transitions and suffix acceptance, and a cheaper prefix remains cheaper under any identical future additive cost. Induction yields exact optimality and feasibility, including zero cost, all-zero items and no items. Store original option tables and selected identities for witness recovery. Rational costs can be scaled by product of input denominators, with polynomial total bit length. No rounding of actual capacities, costs or local ceiling constraints is needed.

Strict quotient example: at t=2 with A mod 4=0, two chosen increments 2^3-1 each yield S=14 and one 2^4-1 yields S=15. Both have Q=4; R854's pending histograms differ (two at 3 versus one at 4). All remaining increments divisible by 4 give the same first-capacity answer. The exact key subsumes safe carry normalization without falsely separating endpoints of a single choice. A different observer reading individual endpoints would require the original history.

## 3. Cardinality bound and further refinement
Write each chosen difference as two signed events (-1 at b, +1 at a); adjacent differences may equivalently use a single +1 at b. Separate the already chosen options' events into <=t and >t. Let W be the low signed sum. Each item's low partial contribution lies in [-2^t,2^t] (either an unmatched negative start, a completed difference, a single adjacent bit or zero). Hence q=ceil((W-A_t)/2^t) lies in [-n,n]. At each pending exponent e>t the signed count H(e) is an integer in [-n,n]. Consequently
    Q = q + sum_(e>t) H(e)*2^(e-t).
The number of possible Q keys in scope j is <=(2n+1)^(1+h_j). For r scopes the state count <=(2n+1)^(r+sum h_j). This bound uses potential endpoints over all processed options, not only those chosen by one witness, and handles pending negative starts on a scope whose own lower endpoint is above the shared decision layer. At a jump just before processing the next item, the map from the previous states is deterministic and cannot increase their number. Thus use the maximum over post-decision stages and the initial state.

More refined bound: partition the pending exponent set arbitrarily into nonempty clusters C. For a cluster with min exponent l and span d=max(C)-l, its normalized signed sum Z=sum H(e)2^(e-l) has at most
    min((2n+1)^|C|, 2n*(2^(d+1)-1)+1)
distinct values, because |Z|<=n*(2^(d+1)-1). Multiplying these bounds and (2n+1) bounds Q cardinality, without requiring the cluster sums to be independent. Consecutive dense exponent blocks can therefore be cheaper than independent endpoint counters. For actual DP one stores only Q, not a chosen cluster decomposition. No general polynomial bound for unbounded endpoint diversity is claimed.

With maximum table size Dopt and state bound Smax, O(n(Dopt+1)Smax) candidate transitions and jump operations; integer keys have O(M+log(n+1)) bits for materialized max exponent/budget width M, plus r-coordinate overhead. Exact costs and backpointers have polynomial bit lengths; preprocessing scans all table entries and sorts n decision levels. Hash or ordered-map overhead and original witness checks are polynomial in these parameters. This is polynomial for fixed r+max sum h_j, not an FPT assertion in this parameter. Compact exponent encoding without charging expanded width is outside the complexity claim.

Wide example: n=40 items with b=0..39, each selects one of (2^80-2^b,0) at cost 1 or (0,2^80-2^b) at cost 0; both budgets 20*2^80. Any 21 selections in either scope exceed its budget since sum 2^b<2^40; exactly 20 in each is feasible. Both scopes have one pending upper endpoint throughout; exact optimum 20 without brute force.

## 4. Executed evidence and next question
Deterministic V8 BigInt experiment below compares exact optimum and feasibility against exhaustive option combinations for 420 small instances, including 30 high-exponent cases, 1 to 3 scopes, up to 7 items, nonadjacent and multilevel explicit options, arbitrary independent per-scope bases (including zero increments), zero costs and budgets. Wide 40-item optimum uses the preceding proof; three edge cases include empty item population, empty option table, zero capacity. Original selected identities, exact capacities and costs rechecked for each feasible returned witness. These are auxiliary integer-scaled-cost cases; general rational costs and local analytic prefiltering are proved, not separately empirically exercised. No native BRC experiment.
Results: {"instances":424,"feasible":252,"infeasible":172,"bruteLeaves":72635,"transitions":49330,"folds":15750,"merges":5074,"witnessChecks":252,"maxStates":1506,"wideMaxStates":40,"highExponent":231,"failures":0}

Next: exploit suffix divisibility beyond the common decision level (per-scope next-active exponent) and test whether independent local schedules can reduce joint pending width; characterize exact quotient cardinality when pending exponent diversity is unbounded and investigate native/shared-bundle transfer separately. R852's arbitrary multibit grouped switches are outside the bounded-width tractable claim. Keep original joint moments, road matrix, branch signs, common depth and provenance.

```js
function experiment(){
 const st={instances:0,feasible:0,infeasible:0,bruteLeaves:0,transitions:0,folds:0,merges:0,witnessChecks:0,maxStates:0,wideMaxStates:0,highExponent:0,failures:0};
 const pow=t=>1n<<BigInt(t), delta=([a,b])=>pow(a)-pow(b);
 const ck=(p,msg)=>{if(!p)throw Error(msg)};
 const cd=(x,d)=>x>=0n?(x+d-1n)/d:x/d;
 let seed=855; const rnd=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return (seed>>>8)%n};
 const prepare=items=>items.map((opts,i)=>({i,opts:opts.map(o=>({...o,d:o.ab.map(delta)})),t:Math.min(...opts.flatMap(o=>o.ab.filter(([a,b])=>a>b).map(([a,b])=>b)),Infinity)})).map(o=>({...o,t:o.t===Infinity?0:o.t})).sort((a,b)=>a.t-b.t||a.i-b.i);
 function solve(items,A){
  if(A.some(a=>a<0n)||items.some(x=>!x.length))return null;
  const r=A.length, order=prepare(items);let t=0, dp=new Map([["0".repeat(0),{q:A.map(()=>0n),c:0n,w:[]}]]);
  function insert(map,s){let k=s.q.join(",");let old=map.get(k);if(old){st.merges++;if(old.c<=s.c)return}map.set(k,s)}
  for(const it of order){
   if(it.t!==t){let d=pow(it.t-t), nxt=new Map();for(const s of dp.values()){st.folds++;insert(nxt,{...s,q:s.q.map((q,j)=>cd(q-((A[j]>>BigInt(t))%d),d))})}dp=nxt;t=it.t}
   let nxt=new Map();for(const s of dp.values())for(let z=0;z<it.opts.length;z++){st.transitions++;let o=it.opts[z],q=s.q.map((x,j)=>{ck(o.d[j]%pow(t)===0n,"divisibility");return x+o.d[j]/pow(t)});if(q.some((x,j)=>x>(A[j]>>BigInt(t))))continue;insert(nxt,{q,c:s.c+o.c,w:[...s.w,[it.i,z]]})}
   dp=nxt;st.maxStates=Math.max(st.maxStates,dp.size);
  }
  let best=null;for(const s of dp.values())if(s.q.every((q,j)=>q<=A[j]>>BigInt(t))&&(!best||s.c<best.c))best=s;return best;
 }
 function brute(items,A){let best=null;function rec(i,s,c){if(i===items.length){st.bruteLeaves++;if(s.every((x,j)=>x<=A[j])&&(best===null||c<best))best=c;return}for(const o of items[i])rec(i+1,s.map((x,j)=>x+delta(o.ab[j])),c+o.c)}rec(0,A.map(()=>0n),0n);return best}
 function check(items,A,opt,wide=false){st.instances++;let s=solve(items,A);ck((s===null)===(opt===null),"feasibility");if(s){st.feasible++;ck(s.c===opt,"exact optimum");let sums=A.map(()=>0n),cost=0n;ck(s.w.length===items.length&&new Set(s.w.map(x=>x[0])).size===items.length,"witness identities");for(const [i,z] of s.w){let o=items[i][z];cost+=o.c;sums=sums.map((x,j)=>x+delta(o.ab[j]))}ck(cost===s.c&&sums.every((x,j)=>x<=A[j]),"recovery");st.witnessChecks++}else st.infeasible++;if(wide)st.wideMaxStates=st.maxStates}
 // All options in each item are independent of other items; integer scaled costs.
 for(let k=0;k<420;k++){let r=1+k%3,n=1+rnd(7),large=k>=390;let items=Array.from({length:n},()=>Array.from({length:1+rnd(4)},()=>({ab:Array.from({length:r},()=>{let b=rnd(large?220:7),a=b+rnd(large?15:6);st.highExponent=Math.max(st.highExponent,a);return [a,b]}),c:BigInt(rnd(21))})));let A=Array.from({length:r},(_,j)=>{let max=items.reduce((s,o)=>s+o.reduce((m,z)=>delta(z.ab[j])>m?delta(z.ab[j]):m,0n),0n);return max*BigInt(rnd(101))/100n});check(items,A,brute(items,A))}
 const wide=Array.from({length:40},(_,b)=>[{ab:[[80,b],[b,b]],c:1n},{ab:[[b,b],[80,b]],c:0n}]);let old=st.maxStates;st.maxStates=0;check(wide,[20n*pow(80),20n*pow(80)],20n,true);st.maxStates=Math.max(old,st.maxStates);
 check([], [0n,0n],0n);check([[]],[10n,10n],null);check([[{ab:[[1,0],[1,0]],c:0n}]],[0n,1n],null);
 ck(cd(14n,4n)===cd(15n,4n),"strict quotient example");
 return st;
}
console.log(JSON.stringify(experiment()));
```
