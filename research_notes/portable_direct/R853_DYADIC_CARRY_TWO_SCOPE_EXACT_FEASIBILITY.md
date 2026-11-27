# R853 — Dyadic carry coordinates for two exact scopes: same-radius feasibility and objective FPTAS

2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.
Independent informed portable continuation of R852, no shared Task claim or mutation. Existing lane metadata EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91, own session recovery returned metadata_only=true, no runs, execution_authorized=false. R852 owner read SUCCEEDED with empty RUNNING list at its as-of snapshot and Source drift; current request r3-20261128-r853-running-read last observed RUNNING / NATIVE_RUNNER before science publication. Global core blobs matched immutable 68c861f899de7fb3b56616813cd7dab614e76e50; ACTIVE worldview, global P000 V4, current normative and portable routes read. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 and joint observer read; generated startup and residual companion absent at that pin (404), no repinning. Positive auxiliary certificate model; no native BRC dynamics or signed/joint observer quotient. Original labels, provenance, branch identities and complete selected witness retained.

## 1. Question and result

R852 at 32dbcd8b18040cd685d79334f4e18f340c484cdc:research_notes/portable_direct/R852_TWO_LIVE_CAPACITY_GAP_HARDNESS.md proves weak NP-hardness for two interleaved exact Kraft capacities using two grouped witnesses with arbitrary integer increments. Can actual independent binary labels remove that obstacle? Yes on the following degree-two paired family, even at the SAME radius: arbitrary number of anchors, two fixed Kraft scopes, every anchor incident to one edge in each scope, each edge one independently selectable label with two adjacent allowed lengths (or more generally the option data below). No shared-bundle propagation. Anchor-local constraints and costs depend only on its pair.

For anchor i let x_i,y_i in {0,1} denote selection of the shorter length at scopes 1 and 2. Subtract the fixed base and all long-label capacities. Residual budgets A,B are exact nonnegative integers; a negative budget is infeasible. The increments on scope 1 are w_i=2^t_i, t_i>=0; those on scope 2 are v_i>=0 arbitrary integers (in the actual adjacent-label model also powers of two). For an adjacent pair of lengths l-1,l at common scale M, the long contribution is 2^(M-l) and the additional short contribution is exactly 2^(M-l), hence t_i=M-l. For each i compute the exact allowed local subset O_i of the four binary pairs, and assign each allowed pair a nonnegative rational local cost c_i(x,y). E.g. p=(1+b1 R^(L1+2))(1+b2 R^(L2+2)) times nondecreasing anchor base, keep p<=U<=2-eta, and c_i=(p-1)/(2-p). Positive weights allowed; no simultaneous switches across different labels are imposed. The problem is sum w_i x_i<=A, sum v_i y_i<=B, minimize sum c_i, with one actual pair per i.

Theorem A: exact same-radius feasibility and witness recovery are polynomial in n and the bit length of explicit option data. The number of scalar carry states is <=n+1, independent of the NUMERICAL budget A or B. Theorem B: for rational 0<eps<=1, exact-feasibility FPTAS for the sum of local nonnegative costs at this same radius: either correctly report infeasible or return actual feasible choices of cost <=(1+eps)OPT, including OPT=0. Neither resource bound nor analytic ceiling is relaxed. This extends R852's one-pivot idea via a binary carry sufficient statistic instead of a numerical capacity index. It does not assert a theorem for all independent labels, nonadjacent length choices, or arbitrary interleaved scopes.

## 2. Exact carry coordinate and observer proof

Let V=sum v_i, saving s=sum v_i(1-y_i). The second budget is exactly s>=V-B. Process items in nondecreasing t_i, grouping by exponent t. Let A_t=A mod 2^t, W_t the total selected scope-1 increments from exponents <t. At the start of level t, define q_t=ceil((W_t-A_t)/2^t). Because 0<=A_t<2^t and W_t>=0, q_t>=0; also q_t<=number of selected earlier items (including t=0, q_0=0). After selecting x for an item of exponent t, add x to the in-level carry q. After all items of this level, with X_t their total x and a_t the t-th binary digit of A, apply
    q_(t+1)=ceil((q_t+X_t-a_t)/2)=floor((q_t+X_t+1-a_t)/2).
Proof: W_(t+1)=W_t+2^t X_t and A_(t+1)=A_t+2^t a_t. The identity ceil((ceil(z)+k)/2)=ceil((z+k)/2) for integer k follows by comparing to each integer bound. Consequently this recurrence is EXACT, not a rounding of a capacity constraint. During a level q<=n. Choose m=max(1,bit_length(A),1+max t_i), interpreting empty max as 0. Then all increments and A have been processed, and q_m=0 iff W_m<=A (the negative difference cannot be <=-2^m). This is a finite-horizon observer descent certificate: equal q at the same level and item index implies identical final acceptance on scope 1 under any same suffix choices, despite different discarded lower-bit totals. Preserve original input and backpointer to recover actual capacity totals and identities; this is a sufficient statistic for this constraint observer only.

For feasibility keep the largest exact saving s per q at each item and each fold. Every future saving update is additive, and all future q transitions depend only on current q and the same suffix choices. Thus largest saving dominates any other prefix with equal q for the declared feasibility observer. At the final cut accept iff a q=0 representative has s>=V-B. Empty local option set is immediately infeasible; negative budget similarly; zero items with nonnegative budgets are feasible. Exact verification by reconstructing and checking both original sums and local choices.

Theorem A complexity: O(n(n+m)) candidate operations with <=4 options per item, including empty-level folds; arithmetic uses integers of bit length polynomial in the input (save sums of v_i). m is bounded by explicit capacity/label representation length; actual dyadic M is not treated as a binary-encoded exponentially large exponent without charging its materialization. Storage O(n) rolling states and O(n(n+m)) backpointer records. This is not a pseudo-polynomial dependence on the numerical capacity.

## 3. Same-radius objective approximation, exact capacities

To preserve cost as well as feasibility, keep for each (q,bin(c)) the prefix with maximum exact saving. Here c is total local cost accumulated. Use R850 exact dyadic bins with K=ceil(2(n+m)/eps), rho=1+1/K; zero separate. For positive c, e=floor(log2 c), bin=(e,floor(K(c/2^e-1))). Same-bin costs differ by at most factor rho. Can multiply all rational costs by a common positive integer denominator (product of all denominators suffices); its bit length is sum of denominator bit lengths, so costs become exact nonnegative integers and ratios are unchanged. Do not approximate the carry or savings.

Induction at each of at most n+m trims: for any original reference prefix there is a representative with IDENTICAL q, no smaller saving, and cost <=rho^j reference cost. Initially zero. Append reference option: q equal, savings dominance persists, and adding a nonnegative cost preserves multiplicative domination. At a fold use the same exact carry map, no change to cost/saving. Trimming inside the same key preserves q, increases saving or retains it, and increases cost by at most rho (zero remains zero). Thus reference feasibility implies the representative with q_m=0 and adequate saving. The minimum cost among accepted representatives is <=rho^(n+m)OPT<=exp(eps/2)OPT<= (1+eps)OPT. All returned witnesses are actual choices, so if reference infeasible none can be accepted. Cost-zero case is preserved exactly. No radius payment is required for this restricted topology.

Let J=1+O(K times the number of occupied binary octaves between the smallest positive scaled cost and n times maximal scaled cost). Bit length of these bounds is polynomial in explicit input, including denominators; if all costs zero use J=1. At most (n+1)J states, O(n(n+m)J) candidate operations, with polynomial exact arithmetic, bin lookup, witness backpointer storage and original constraint re-verification. The proof covers arbitrary local option tables, even if not monotone, and arbitrary v_i. Deriving four local options and exact cost values from the actual rational products is polynomial in represented label/weight bit length and exponents. Fixed additive cost from isolated anchors can be restored without worsening the relative bound.

## 4. What changes compared with R852

R852 arbitrary grouped increment a_i may have many set bits. Its all-or-nothing switch couples these bits, so it cannot be replaced by independent bit items: e.g. choosing a=3 as a single switch permits only {0,3}; replacing by weights 1 and 2 permits {0,1,2,3}, changing feasibility and provenance. Here each decision affects a single bit on one scope, which permits processing by bit order; the second capacity is handled by monotone exact savings dominance. The result establishes an exact tractable subfamily on the same two-scope topology. It is not a general solution to binary coupled multi-bit increments, arbitrary graph topology, all independent multilevel label choices, shared propagation, or native Port realization.

## 5. Reproducible exact finite evidence

Executed the following JS in the available V8 runtime using BigInt for both capacities and scaled exact rational costs. Small integer carry, exponent, and array indices are within exact Number range. Input generator deterministic seed 853, exhaustive pair-option combinations per small instance, plus exponents up to 229 to exercise binary not numeric budget dependence. Abstract options include arbitrary allowed subsets and nonnegative integer costs. Analytic instances use strictly positive single-label weights b=a/(64*2^(L+2)), R=2, adjacent lengths, exact local products and rational phi costs; residual budgets fit the 2^M scale when nonnegative. Negative residual budgets represent baseline overflow. Tested feasibility-only and eps=1,1/2,1/10 against exhaustive optimum, including witness identity and both exact capacities. Finite evidence is not a proof for unbounded instances; the preceding derivation supplies the theorem. Results:
{"abstractCases":362,"analyticCases":180,"largeExponentCases":36,"feasible":333,"infeasible":245,"bruteLeaves":71217,"solverCalls":2312,"transitions":153292,"folds":310769,"merges":51031,"maxStates":591,"witnessChecks":1332,"failures":0}

```js
function experiment(){
 const stats={abstractCases:0,analyticCases:0,largeExponentCases:0,feasible:0,infeasible:0,bruteLeaves:0,solverCalls:0,transitions:0,folds:0,merges:0,maxStates:0,witnessChecks:0,failures:0};
 const ck=(x,m)=>{if(!x)throw Error(m)};
 const sum=(a)=>a.reduce((s,x)=>s+x,0n);
 const pow=t=>1n<<BigInt(t);
 const bits=x=>x===0n?0:x.toString(2).length;
 let seed=853;
 const rnd=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%n};
 function solve(items,A,B,eps){
  stats.solverCalls++;
  if(A<0n||B<0n||items.some(i=>!i.opts.length))return null;
  const m=Math.max(bits(A),1,...items.map(i=>i.t+1)),K=eps?BigInt(Math.ceil(2*(items.length+m)*eps[1]/eps[0])):1n;
  const groups=Array.from({length:m},()=>[]);
  items.forEach((i,j)=>groups[i.t].push(j));
  const total=sum(items.map(i=>i.v)),need=total-B;
  function bin(c){if(!eps||c===0n)return "0";let e=bits(c)-1,b=pow(e);return e+":"+((c-b)*K/b)}
  function put(map,s){let key=s.q+":"+bin(s.c),old=map.get(key);if(old){stats.merges++;if(old.s>s.s||(old.s===s.s&&old.c<=s.c))return}map.set(key,s)}
  let states=new Map([["0:0",{q:0,s:0n,c:0n,w:[]}]]);
  for(let t=0;t<m;t++){
   for(const j of groups[t]){
    let next=new Map(),i=items[j];
    for(const st of states.values())for(let z=0;z<i.opts.length;z++){
     const o=i.opts[z];stats.transitions++;
     put(next,{q:st.q+o.x,s:st.s+(o.y?0n:i.v),c:st.c+o.c,w:st.w.concat([[j,z]])});
    }
    states=next;stats.maxStates=Math.max(stats.maxStates,states.size);
   }
   const bit=Number((A>>BigInt(t))&1n),next=new Map();
   for(const st of states.values()){stats.folds++;put(next,{...st,q:Math.floor((st.q+1-bit)/2)})}
   states=next;stats.maxStates=Math.max(stats.maxStates,states.size);
  }
  let best=null;
  for(const st of states.values())if(st.q===0&&st.s>=need&&(!best||st.c<best.c))best=st;
  return best;
 }
 function brute(items,A,B){
  let best=null;
  function rec(j,a,b,c){if(j===items.length){stats.bruteLeaves++;if(a<=A&&b<=B&&(best===null||c<best))best=c;return}let i=items[j];for(const o of i.opts)rec(j+1,a+BigInt(o.x)*pow(i.t),b+BigInt(o.y)*i.v,c+o.c)}
  if(A>=0n&&B>=0n)rec(0,0n,0n,0n);return best;
 }
 function check(items,A,B,kind){
  stats[kind]++;
  const ref=brute(items,A,B);stats[ref===null?"infeasible":"feasible"]++;
  for(const eps of [null,[1,1],[1,2],[1,10]]){
   const s=solve(items,A,B,eps);
   ck((s===null)===(ref===null),"feasibility");
   if(!s)continue;
   let a=0n,b=0n,c=0n;const seen=new Set();
   for(const [j,z] of s.w){ck(!seen.has(j),"identity");seen.add(j);let i=items[j],o=i.opts[z];a+=BigInt(o.x)*pow(i.t);b+=BigInt(o.y)*i.v;c+=o.c}
   ck(seen.size===items.length&&a<=A&&b<=B&&c===s.c,"witness");stats.witnessChecks++;
   if(eps)ck(c*BigInt(eps[1])<=ref*BigInt(eps[0]+eps[1]),"objective");
  }
 }
 function budgets(items){return [sum(items.map(i=>pow(i.t))),sum(items.map(i=>i.v))]}
 for(let z=0;z<360;z++){
  const n=1+z%7,items=[];
  for(let i=0;i<n;i++){let t=rnd(7),v=BigInt(1+rnd(127)),mask=1+rnd(15),opts=[];for(let q=0;q<4;q++)if(mask&(1<<q))opts.push({x:q&1,y:q>>1,c:BigInt(rnd(53))});items.push({t,v,opts})}
  let [a,b]=budgets(items);check(items,BigInt(rnd(Number(a)+1)),BigInt(rnd(Number(b)+1)),"abstractCases");
 }
 // Genuine positive single-label witnesses, R=2, U varies, b=a/(64*2^(L+2)).
 for(let z=0;z<180;z++){
  const n=1+z%6,M=8,items=[],baseA=[],baseB=[];
  for(let i=0;i<n;i++){
   let l=1+rnd(M),r=1+rnd(M),a=BigInt(1+rnd(12)),b=BigInt(1+rnd(12)),U=[9n,10n,11n,12n][rnd(4)],opts=[];
   for(let x=0;x<2;x++)for(let y=0;y<2;y++){
    // p_short=1+a/128; p_long=1+a/64. Product denominator 128^2.
    let N=(128n+a*BigInt(2-x))*(128n+b*BigInt(2-y)),D=16384n;
    if(8n*N<=U*D)opts.push({x,y,num:N-D,den:2n*D-N});
   }
   baseA.push(pow(M-l));baseB.push(pow(M-r));
   items.push({t:M-l,v:pow(M-r),opts});
  }
  let scale=1n;for(const i of items)for(const o of i.opts)scale*=o.den;
  for(const i of items)for(const o of i.opts)o.c=o.num*(scale/o.den);
  let [a,b]=budgets(items);
  // Residual budgets after subtracting fixed long-label and boundary capacities.
  // Ensure actual scope totals fit 2^M.
  let A=a>256n-sum(baseA)?256n-sum(baseA):a,B=b>256n-sum(baseB)?256n-sum(baseB):b;
  if(A>=0n)A=BigInt(rnd(Number(A)+1));if(B>=0n)B=BigInt(rnd(Number(B)+1));
  check(items,A,B,"analyticCases");
 }
 for(let z=0;z<36;z++){
  let items=Array.from({length:6},(_,j)=>({t:40+((j*73+z*19)%190),v:pow(30+((j*37+z*11)%180)),opts:[{x:0,y:1,c:pow(j*11)},{x:1,y:0,c:pow(7+j*13)},{x:1,y:1,c:0n}]}));
  let [a,b]=budgets(items);check(items,a/BigInt(1+z%4),b/BigInt(1+(z+1)%4),"largeExponentCases");
 }
 // Explicit zero/empty edge cases.
 check([],0n,0n,"abstractCases");check([{t:0,v:1n,opts:[]}],0n,0n,"abstractCases");
 return stats;
}
console.log(JSON.stringify(experiment()));
```

## Next

Investigate independent multilevel labels or nonadjacent two-length choices: a switch with increment 2^a-2^b creates a contiguous interval of binary ones. Determine whether bounded overlap of those intervals admits an augmented carry state, or whether exact same-radius or radius-gap hardness persists. Also examine extensions to more scopes where two or more exact savings must be tracked simultaneously. The full Port, native joint moment observer, and general shared-bundle optimization remain open.
