# R856 candidate — Affine suffix-lattice capacity observer, exact saturation and exponential separation

2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.

Continuation of R855 at 7d2f3e8afdeeb5d5ef04de8e4817c20485607982:research_notes/portable_direct/R855_CANONICAL_DEBT_SYNCHRONOUS_DYADIC_CARRY.md (blob 564d21473bd73e7b5748802133cd9969a2b1753c). Frozen science remains a72226e2430ffa4786321ac86e7f0c599d5f0389, P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447, joint observer blob 3923890d77a02d84b772f789e6912dd14f220d14; both read. Frozen generated startup and residual companion paths returned 404; no repin. Global normative snapshot cab704bb872c05566c688520c31f4f9adf84d59b, both entry blobs matched, ACTIVE worldview, TASK and informed routes, current continuation, portable and method read. Own lane record EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91 metadata verified, no private execution authority established. Prior owner query r3-20261128-r855-running-read SUCCEEDED, empty as of 2026-11-28T00:25:20.370172Z, complete event pages revalidated, Source changed during collection. New owner query r3-20261128-r856-running-read admitted QUEUED. No shared-task state mutation. Auxiliary positive certificate model only; no native BRC dynamics calculation. Preserve original joint option identities, local analytic ceiling tests, branch signs, road matrix, common depth and original provenance; the theorem concerns only the named finite-horizon capacity observer.

## 1. Model and normalization

n independent items with nonempty explicit tables O_i. Option z has r nonnegative integer increments d_ij(z) and nonnegative rational additive cost c_i(z). Exactly one option per item, each sum <= A_j. R855 dyadic increments 2^a-2^b are included. Choose any fixed item order. Set b_ij=min_z d_ij(z), e_ij(z)=d_ij(z)-b_ij and A'_j=A_j-sum_i b_ij. These per-coordinate minima need not be simultaneously attained by one option; this is a translation of the entire joint table, not permission to choose independent coordinates. If A'_j<0 or a table is empty, infeasible. Otherwise all e>=0, and feasibility and costs are unchanged. Local analytic tests must already be included in allowed options, at the same radius.

At suffix beginning at i define g_ij=gcd of all e_kj(z) with k>=i (gcd empty/all zero =0), and M_ij=sum_{k>=i} max_z e_kj(z). Compute backward by gcd and addition. All future sums lie in [0,M_ij] intersect g_ij Z; if g=0 only zero is possible. M is an attained marginal maximum because item tables are independent, but the vector M need not be jointly attainable. The original suffix sums in coordinate j belong to sum_{k>=i} b_kj+g_ij Z. Moreover g is the greatest positive modulus of a containing affine integer lattice when the marginal suffix has more than one value: every difference is divisible by g, and each within-item difference occurs as a difference of two suffix sums by holding all other items fixed. The gcd of all within-item differences is exactly gcd of normalized entries. This is a statement about the enclosing lattice, not absence of holes.

## 2. Exact clipped suffix observer

For a prefix with normalized committed total S_j, let h=A'_j-S_j. Reject h<0 (all remaining increments nonnegative). Otherwise define
    H_ij(h)=0 if g_ij=0,
    H_ij(h)=min(M_ij, g_ij floor(h/g_ij)) if g_ij>0.
For any fixed legal future option sequence with normalized sum F_j, F_j<=h iff F_j<=H_ij(h). Proof: F_j is an integer multiple of g and lies between 0 and M; for g=0 F_j=0. Conjoin these exact equivalences over the r coordinates, with the SAME future sequence, so coupling within every joint option is preserved. This is a finite-horizon observer factorization.

Transition: for option z in O_i, set h'_j=H_ij-e_ij(z). Reject if any h'_j<0; otherwise key at the next stage is H_(i+1)j(h'_j). Proof: the remaining suffix total F'_j added to the selected e is a legal i-suffix sum, hence the equivalence above applies to e+F'. For canonical transition equality, if H_i was rounded (not clipped), h-H_i is in [0,g_i), and g_i divides every e and every next-suffix entry, hence divides g_(i+1) when positive; H_(i+1)(h-e)=H_(i+1)(H_i-e). If H_i was clipped, H_i=M_i and H_i-e>=M_(i+1), so both next keys saturate. If g_i=0, all current and future normalized increments are zero. Negative rejection is equivalent for original and canonical budget because e is an attainable current marginal increment and is <=M_i. Thus the key is a true deterministic congruence for declared future decisions, not merely a terminal feasibility filter. All final nonnegative keys collapse to zero; empty items handled as above. Store minimum exact cumulative cost per vector H, with selected original option identities. Equal key prefixes have identical feasible continuations; cheaper prefix remains cheaper under every same suffix. Induction proves exact minimum and original witness reconstruction. Arbitrary rational costs may be scaled by product of input denominators (polynomial bit length), no rounding. All prefix translation, modulus and saturation arithmetic exact.

## 3. State and complexity bounds

For g>0, marginal state count <=1+M_ij/g_ij; for g=0 it is 1. Thus S_i <= product_j (1+M_ij/g_ij), interpreting zero-g factor as one, or the actual number of reachable prefix keys if smaller. With maximum option table D, transitions <= D sum_i S_i. Arithmetic, preprocessing, backpointers and exact rational costs use polynomial bit length in materialized inputs. This is not an unrestricted polynomial-time claim; M/g can be large. It is polynomial if the product bound is polynomial, independently of dyadic endpoint width.

Comparison with R855: at the same fixed sorted order and shared t at a stage where all future original increments are divisible by 2^t, each b and e is divisible by 2^t, and so is positive g. The R855 Q determines floor((A-S_original)/2^t). Subtract the exact suffix baseline divided by 2^t and then divide by g/2^t and floor, or saturate. Thus every equal R855 key maps to equal H, including zero-g; new prefix rejection can be earlier. The two-coordinate observer does not become a native 2D plane or a complete native slice. It is coarser than the shared-layer key at these stages, possibly strictly. No claim about arbitrary differing item orders. The finest affine lattice can also be non-dyadic: if nonzero normalized increments are 2^b(2^k-1), fixed k>=2 and zero options available, g=2^min b(2^k-1). The odd factor gives an exact additional refinement of the arithmetic unit, not an approximation.

## 4. Exponential separation theorem

For integer m>=2, take m+1 items indexed i=0..m, with options (1,0) and (1,2^i), the latter cost 0, the former cost 1 for i<m and cost 2 for i=m. Budgets (m+1,2^m). All increments are zero or single dyadic differences; both options have the same first increment 1=2^1-2^0. Therefore all R855 common decision levels are zero; choose tie order i increasing. Immediately before the last item the 2^m distinct binary subset sums 0..2^m-1 are all feasible prefixes, and all must have distinct R855 Q keys in its unaugmented table. At final stage its raw table can have 2^m+1 keys. By contrast translate first coordinate to zero. At stage i<=m the second suffix gcd is 2^i, marginal max=2^(m+1)-2^i. Since prefix sum lies between 0 and 2^i-1, the remaining raw budget is 2^m minus that prefix. Its canonical H is exactly 2^m for prefix zero or 2^m-2^i for positive prefix. Hence at most two states at EVERY stage, final one. Exact optimum =2: choosing final zero and all low bits costs 2, choosing final high forces all low bits zero and costs m>=2. The separation is against R855's unaugmented common-level implementation in this particular order, not against any possible adaptive implementation or information-theoretic lower bound. This shows fixed irrelevant capacity coordinates can obstruct a common precision layer exponentially while suffix-affine coordinates remove the obstruction.

## 5. Executed evidence and next

Executed deterministic BigInt calculation (code below). 420 small instances (30 high-exponent cases) with 1..3 scopes, up to seven items, 1..4 explicit options, dyadic increments, integer costs and exact budgets compared to full exhaustive option choices. Four edge cases (empty population, empty table, fixed infeasible baseline, affine nonzero baseline). Two strict-separation instances m=16 and 100; m=16 also evaluates the raw residual key, equivalent in this construction to common t=0 R855 up to constant baseline shift. Initial assertion expected peak 65536 but raw final stage admits one extra sum 2^16; corrected to 65537, matching the analytic count. No change to solver or mathematical model. 228 fixed-gap gcd identities checked. Each returned original witness rechecked for exact cost and capacity. General rational costs and local analytic prefiltering proved conditionally, not experimentally tested. No native BRC execution.

Results: {"instances":426,"feasible":256,"infeasible":170,"bruteLeaves":66521,"transitions":19035,"merges":7466,"witnessChecks":256,"maxStates":338,"commonMaxStates":65537,"wideMaxStates":2,"wideOptimum":"2","oddGcdChecks":228,"highExponent":231,"failures":0}

Next: use actual joint reachable suffix threshold sets (not just marginal affine lattice) to characterize the minimal finite-horizon observer; find computable structural certificates for large gaps/holes without enumerating the joint suffix, and study adaptive item orders. General shared-bundle propagation and native Port correspondence remain open.

```js
function experiment(){
const st={instances:0,feasible:0,infeasible:0,bruteLeaves:0,transitions:0,merges:0,witnessChecks:0,maxStates:0,commonMaxStates:0,wideMaxStates:0,wideOptimum:null,oddGcdChecks:0,highExponent:0,failures:0};
const ck=(x,m)=>{if(!x)throw Error(m)}, pow=t=>1n<<BigInt(t), gcd=(a,b)=>{while(b)[a,b]=[b,a%b];return a}, min=(a,b)=>a<b?a:b,max=(a,b)=>a>b?a:b;
let seed=856;const rnd=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return (seed>>>8)%n};
function solve(items,A,common=false){
 if(items.some(x=>!x.length)||A.some(x=>x<0n))return null;
 const n=items.length,r=A.length,zero=()=>A.map(()=>0n);
 const mins=items.map(opts=>A.map((_,j)=>opts.reduce((x,o)=>min(x,o.d[j]),opts[0].d[j])));
 const norm=items.map((opts,i)=>opts.map(o=>({d:o.d.map((x,j)=>x-mins[i][j]),c:o.c})));
 const G=Array.from({length:n+1},zero),M=Array.from({length:n+1},zero);
 for(let i=n-1;i>=0;i--)for(let j=0;j<r;j++){
  G[i][j]=norm[i].reduce((x,o)=>gcd(x,o.d[j]),G[i+1][j]);
  M[i][j]=M[i+1][j]+norm[i].reduce((x,o)=>max(x,o.d[j]),0n);
 }
 const canon=(h,i,j)=>{if(h<0n)return null;if(common)return h;let g=G[i][j];return g===0n?0n:min(M[i][j],h/g*g)};
 const start=A.map((a,j)=>canon(mins.reduce((x,v)=>x-v[j],a),0,j));
 if(start.includes(null))return null;
 let dp=new Map([[start.join(","),{h:start,c:0n,w:[]}]]), peak=1;
 for(let i=0;i<n;i++){
  const next=new Map();
  for(const s of dp.values())for(let z=0;z<norm[i].length;z++){
   if(!common)st.transitions++;
   let o=norm[i][z],h=s.h.map((v,j)=>canon(v-o.d[j],i+1,j));if(h.includes(null))continue;
   let k=h.join(","),c=s.c+o.c,old=next.get(k);
   if(old){if(!common)st.merges++;if(old.c<=c)continue}
   next.set(k,{h,c,w:[...s.w,z]})
  }dp=next;peak=Math.max(peak,dp.size);
 }
 let best=null;for(const s of dp.values())if(!best||s.c<best.c)best=s;
 if(common)st.commonMaxStates=Math.max(st.commonMaxStates,peak);else st.maxStates=Math.max(st.maxStates,peak);
 return best?{...best,peak}:null;
}
function brute(items,A){let best=null;function rec(i,s,c){if(i===items.length){st.bruteLeaves++;if(s.every((v,j)=>v<=A[j])&&(best===null||c<best))best=c;return}for(const o of items[i])rec(i+1,s.map((v,j)=>v+o.d[j]),c+o.c)}rec(0,A.map(()=>0n),0n);return best}
function check(items,A,opt){st.instances++;let s=solve(items,A);ck((s===null)===(opt===null),"feasibility");if(s){st.feasible++;ck(s.c===opt,"optimum");let sums=A.map(()=>0n),cost=0n;ck(s.w.length===items.length,"identity");for(let i=0;i<s.w.length;i++){let o=items[i][s.w[i]];cost+=o.c;sums=sums.map((v,j)=>v+o.d[j])}ck(cost===s.c&&sums.every((v,j)=>v<=A[j]),"witness");st.witnessChecks++}else st.infeasible++;return s}
for(let k=0;k<420;k++){let r=1+k%3,n=1+rnd(7),large=k>=390;let items=Array.from({length:n},()=>Array.from({length:1+rnd(4)},()=>({d:Array.from({length:r},()=>{let b=rnd(large?220:8),a=b+rnd(large?14:7);st.highExponent=Math.max(st.highExponent,a);return pow(a)-pow(b)}),c:BigInt(rnd(21))})));let A=Array.from({length:r},(_,j)=>{let m=items.reduce((s,o)=>s+o.reduce((x,z)=>max(x,z.d[j]),0n),0n);return m*BigInt(rnd(101))/100n});check(items,A,brute(items,A))}
for(let k=2;k<=20;k++){let g=pow(k)-1n;for(let b=0;b<12;b++){ck(gcd(pow(b+k)-pow(b),pow(b+1+k)-pow(b+1))===pow(b)*g,"odd lattice");st.oddGcdChecks++}}
const wide=m=>Array.from({length:m+1},(_,i)=>[{d:[1n,0n],c:i===m?2n:1n},{d:[1n,pow(i)],c:0n}]);
let sm=wide(16),sa=[17n,pow(16)],old=solve(sm,sa,true),nw=check(sm,sa,2n);ck(old.c===nw.c&&old.peak===65537&&nw.peak===2,"strict width");
let big=check(wide(100),[101n,pow(100)],2n);st.wideMaxStates=big.peak;st.wideOptimum=big.c.toString();ck(big.peak===2,"wide");
check([], [0n,0n],0n);check([[]],[10n],null);check([[{d:[1n],c:0n}]],[0n],null);
check([[{d:[2n],c:0n},{d:[5n],c:1n}],[{d:[7n],c:2n}]],[9n],2n);
return st;
}
console.log(JSON.stringify(experiment()));
```
