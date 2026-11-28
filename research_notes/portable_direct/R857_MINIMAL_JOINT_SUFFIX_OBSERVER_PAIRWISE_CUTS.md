# R857 candidate — Minimal joint suffix observer and certified pairwise resource cuts

2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.

Continues immutable R856 at 50f0046f27867901c9fd77bd9c5712ed1a66145e:research_notes/portable_direct/R856_AFFINE_SUFFIX_LATTICE_CAPACITY_OBSERVER.md (blob d480134b78834c3b043ce1adbbe55674461cddb8). Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389 unchanged: P000 V5 and joint relation observer read at pin. Global entries verified at e46721e8c879b817f4ee29bb1abc9ffa96c3aeda, ACTIVE worldview, role router, informed and TASK routes, current continuation/portable/residual/method rules read. Existing lane EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91 public metadata verified; private execution authority not established. R856 original owner query SUCCEEDED (RUNNING filter empty as of 2026-11-28T01:17:13.849384Z; Source changed during collection); R857 original request r3-20261128-r857-running-read admitted QUEUED. Independent informed auxiliary research, no shared task mutation.

## 1. Exact minimal observer

Reuse R856 independent explicit option tables, normalized nonnegative integer resource vectors e_i(z), nonnegative rational additive costs, same-radius local analytic prefilter, residual vector h. Let W_i be the set of all ordered legal suffix option words and F(w) their joint sum. Define L_i(h)={w in W_i:F(w)<=h componentwise}. Define C_i(h)=DEAD if L_i(h) is empty, otherwise the vector whose jth component is max_{w in L_i(h)} F_j(w). The maxima need not be attained simultaneously. Nevertheless C_i(h)<=h, and for every w, F(w)<=h iff F(w)<=C_i(h): forward by the maxima, backward by the inequality. Hence two h have identical feasible suffix words iff their C_i keys coincide (including DEAD). Necessity follows by taking the same maxima; sufficiency by the equivalence. This characterizes the coarsest exact equivalence for the stated Boolean observation of every suffix word, not a claim about other observers or cost-only minimality.

For fixed first option z, left quotient of L_i(h) by z equals L_(i+1)(h-e_i(z)). Equal keys imply equal left quotients and therefore equal next minimal keys, including DEAD. Exact additive cost minimization can retain the cheapest prefix per key and recover a genuine original word using backpointers. This preserves all same-suffix feasibility decisions; it does not preserve arbitrary future changes to budgets, costs, option tables or physical observation. Original joint tables, label identities, road matrix, signs, branch multiplicities, common depth and provenance remain separate.

Computing this key can be hard even in one coordinate: binary item choices {0,a_i}, h=T, yield C_i(T)=largest subset sum <=T; C_i(T)=T iff SUBSET SUM is yes. Thus no general polynomial-time explicit exact closure oracle is proved. The next construction obtains safe cheap compression without computing the minimal key.

## 2. Pairwise joint residual cuts

For j,l define
 B_i(j,l)=sum_{k>=i} max_{z in O_k}(e_kj(z)-e_kl(z)).
It is nonnegative after R856 normalization (each l-coordinate has a zero option, all j increments nonnegative), B_i(j,j)=0. By summing itemwise inequalities, for every same suffix word
 F_j(w)-F_l(w)<=B_i(j,l).
The bound is an attained maximum for that pair because items are independent; maximizing choices may differ across pairs. Also B_i(j,l)<=B_i(j,k)+B_i(k,l) by adding differences and taking maxima, then summing.

Define P_i(h)_j=min_l(h_l+B_i(j,l)), including l=j. It is nonnegative when h>=0 and <=h. Every feasible suffix word satisfies F_j<=F_l+B<=h_l+B for each l, hence F<=P_i(h). The converse is immediate. In fact P_i is idempotent: triangle inequality gives min_{k,l}(h_l+B_i(k,l)+B_i(j,k))>=min_l(h_l+B_i(j,l)), and choosing k=j gives equality. This is a joint difference-constraint closure of the budgets, with no resource rounding.

Compose with the R856 lattice/saturation map H_i:
 K_i(h)=H_i(P_i(H_i(h))).
Each factor preserves exactly the same feasible suffix words; thus K_i does too. Reject negative budgets before the map. Deterministic transition for DP: subtract a selected joint vector from the stored K_i and apply K_(i+1); rejecting a negative coordinate is safe. Proof by induction on remaining suffix words: feasibility after a chosen first option is the left quotient of the original language, and replacing its residual by K preserves that language. The resulting key need not equal K_(i+1) applied to the original uncompressed budget; only language equivalence is needed. Equal stored keys have equal continuations, so keeping the lowest cost prefix is exact. Final nonnegative keys collapse to zero. No assertion that one pass gives the minimal observer or that peak table size decreases on every instance; K is a safe representative, not a demonstrated canonical quotient of the full minimal language. Optional iteration of alternating H/P preserves feasibility but no polynomial bound on iteration count is asserted.

Compute B backward in O(r^2 sum |O_i|) integer operations, with polynomial bit lengths in explicit inputs. Per-state cut O(r^2); H uses integer gcd/division as in R856. With actual reachable key counts S_i, candidate transitions <= sum S_i|O_i|; per transition polynomial bit arithmetic and witness storage. R856 product bound on lattice key count still holds, so no unrestricted polynomial-time claim. Exact optimum uses rational cost arithmetic or a common denominator of polynomial bit length.

## 3. Exponential separation even against exact marginal reachability

For m>=2, use m-1 prefix binary items (0,0) or (2^i,0), i=0..m-2; then m tail binary items (0,0) or (2^i,2^i), i=0..m-1. Cost 1 for zero, 0 for nonzero. Set A=(2^m-1,2^(m-1)) and B=2^(m-1). All choices are dyadic increments; each nonzero tail option is individually within both original budgets. Prefix sums p span every integer 0..B-1. At cut just before tail, h=(2B-1-p,B), hence first residual takes B distinct values B..2B-1. Both marginal tail sets contain EVERY integer 0..2B-1, so R856 H and even exact marginal-predecessor observers retain B different states. All prefixes are feasible. However tail F_1=F_2 and the first bound is redundant: all prefixes admit exactly the same suffix words F<=B. The minimal joint key is (B,B), and the pair cut obtains it directly.

At any prefix stage, let R be sum of unprocessed prefix weights. B_i(1,2)=R, B_i(2,1)=0. The raw first residual is >=B+R; both H coordinates are unchanged before pair cut (tail spans all marginal integer values and h within maxima). Thus the cut gives (B+R,B) at every prefix stage independently of previous choices. Each next prefix stage has exactly one stored key: subtract chosen increment (0 or weight), then cap to B+R_new. In tail, both residuals equal, and R856 gcd=2^i at tail stage i. With tail sum so far in [0,2^i-1], at most two canonical values (B or B-2^i) before final item, final one. Hence peak joint table <=2 for all m, compared to >=2^(m-1) at the cut for marginal-only observer in this fixed order. Exact optimum=1: all prefix items nonzero, all low tail bits nonzero, high tail bit zero is feasible and costs 1; cost zero violates second budget. No enumeration needed for large m. This separates the joint cut from even the ideal marginal predecessor, not from algorithms that already exploit the diagonal coupling or choose a different order.

## 4. Executed evidence

Deterministic JS BigInt tests: 320 small explicit instances (20 high-exponent cases), r=1..3, n=1..7, 1..4 options, nonnegative integer costs, exact budgets, checked joint and marginal-only solvers against full enumeration and reconstructed original witnesses. 24 additional small suffix-language families exhaust integer budget grid 0..12 squared at every suffix; compare closure keys to complete word signatures in both directions and check one-option descent. Two separation instances m=15 (marginal and joint) and m=100 (joint only), analytic optimum 1. Large instance not exhaustively enumerated. No native BRC experiment; finite-horizon auxiliary certificate observer only. Tests are author checks, not independent review.

Results: {"instances":320,"feasible":115,"infeasible":205,"bruteLeaves":44737,"transitions":4074,"merges":1468,"witnessChecks":233,"closureQueries":13013,"closurePairs":24584,"closureTransitions":15691,"strictCuts":307,"failures":0,"smallLatticePeak":16385,"smallJointPeak":2,"wideJointPeak":2,"wideOptimum":"1","widePrefixStates":1}

Next: extend B_i(j,l) to nonnegative rational linear support cuts, choose useful normals without enumerating suffix words, compare against exact closure on small cases; determine when finitely many such cuts plus arithmetic lattice holes suffice. General Port/native BRC correspondence and shared-bundle propagation remain open.

```js
function run(){
const st={instances:0,feasible:0,infeasible:0,bruteLeaves:0,transitions:0,merges:0,witnessChecks:0,closureQueries:0,closurePairs:0,closureTransitions:0,strictCuts:0,failures:0};
const ck=(b,m)=>{if(!b)throw Error(m)}, min=(a,b)=>a<b?a:b,max=(a,b)=>a>b?a:b,gcd=(a,b)=>{while(b)[a,b]=[b,a%b];return a};
let seed=857;const rnd=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return (seed>>>8)%n};
function solve(items,A,joint=true,track=true){
 const n=items.length,r=A.length,zero=()=>A.map(()=>0n);
 if(items.some(t=>!t.length))return null;
 const b=items.map(t=>A.map((_,j)=>t.reduce((s,o)=>min(s,o.d[j]),t[0].d[j])));
 const E=items.map((t,i)=>t.map(o=>({d:o.d.map((x,j)=>x-b[i][j]),c:o.c})));
 const G=Array.from({length:n+1},zero),M=Array.from({length:n+1},zero),B=Array.from({length:n+1},()=>A.map(()=>zero()));
 for(let i=n-1;i>=0;i--)for(let j=0;j<r;j++){
 G[i][j]=E[i].reduce((s,o)=>gcd(s,o.d[j]),G[i+1][j]);M[i][j]=M[i+1][j]+E[i].reduce((s,o)=>max(s,o.d[j]),0n);
 for(let l=0;l<r;l++)B[i][j][l]=B[i+1][j][l]+E[i].reduce((s,o)=>max(s,o.d[j]-o.d[l]),0n);
 }
 const clip=(h,i)=>h.map((x,j)=>G[i][j]===0n?0n:min(M[i][j],x/G[i][j]*G[i][j]));
 function canon(h,i){if(h.some(x=>x<0n))return null;let v=clip(h,i);if(!joint)return v;let u=v.map((x,j)=>v.reduce((s,y,l)=>min(s,y+B[i][j][l]),x));if(track&&u.some((x,j)=>x<v[j]))st.strictCuts++;return clip(u,i)}
 const start=canon(A.map((a,j)=>b.reduce((s,v)=>s-v[j],a)),0);
 if(!start)return null;
 let dp=new Map([[start.join(","),{h:start,c:0n,w:[]}]]),peak=1,peaks=[1];
 for(let i=0;i<n;i++){const next=new Map();for(const s of dp.values())for(let z=0;z<E[i].length;z++){if(track)st.transitions++;const o=E[i][z],h=canon(s.h.map((x,j)=>x-o.d[j]),i+1);if(!h)continue;const k=h.join(","),c=s.c+o.c,old=next.get(k);if(old){if(track)st.merges++;if(old.c<=c)continue}next.set(k,{h,c,w:[...s.w,z]})}dp=next;peak=Math.max(peak,dp.size);peaks.push(dp.size)}
 let best=null;for(const s of dp.values())if(!best||s.c<best.c)best=s;
 return best?{...best,peak,peaks}:null;
}
function brute(items,A){let best=null;function rec(i,s,c){if(i===items.length){st.bruteLeaves++;if(s.every((x,j)=>x<=A[j])&&(best===null||c<best))best=c;return}for(const o of items[i])rec(i+1,s.map((x,j)=>x+o.d[j]),c+o.c)}rec(0,A.map(()=>0n),0n);return best}
function verify(items,A,s,opt){ck((s===null)===(opt===null),"feasibility");if(s){ck(s.c===opt,"optimum");let v=A.map(()=>0n),c=0n;ck(s.w.length===items.length,"witness length");s.w.forEach((z,i)=>{let o=items[i][z];v=v.map((x,j)=>x+o.d[j]);c+=o.c});ck(c===s.c&&v.every((x,j)=>x<=A[j]),"witness");st.witnessChecks++}}
for(let k=0;k<320;k++){let r=1+k%3,n=1+rnd(7),high=k>=300;let items=Array.from({length:n},()=>Array.from({length:1+rnd(4)},()=>({d:Array.from({length:r},()=>{let t=BigInt(rnd(high?200:5));return high?(BigInt(rnd(6))<<t):BigInt(rnd(17))}),c:BigInt(rnd(23))})));let A=Array.from({length:r},()=>high?(BigInt(rnd(8))<<BigInt(rnd(201))):BigInt(rnd(n*12+1)));let opt=brute(items,A),s=solve(items,A);st.instances++;if(s)st.feasible++;else st.infeasible++;verify(items,A,s,opt);verify(items,A,solve(items,A,false,false),opt)}
// Minimal joint closure: enumerate suffix words, including repeated resource vectors.
for(let k=0;k<24;k++){
 let items=Array.from({length:1+rnd(4)},()=>Array.from({length:2+rnd(2)},()=>[rnd(5),rnd(5)]));
 const sums=Array.from({length:items.length+1},()=>[]);sums[items.length]=[[0,0]];
 for(let i=items.length-1;i>=0;i--)for(const e of items[i])for(const f of sums[i+1])sums[i].push([e[0]+f[0],e[1]+f[1]]);
 const closure=(i,h)=>{let sig=[],m=[-1,-1];sums[i].forEach((v,k)=>{if(v.every((x,j)=>x<=h[j])){sig.push(k);m=m.map((x,j)=>Math.max(x,v[j]))}});return {sig:sig.join(","),key:sig.length?m.join(","):"dead",m,some:sig.length>0}};
 for(let i=0;i<=items.length;i++){let bySig=new Map(),byKey=new Map();for(let a=0;a<=12;a++)for(let b=0;b<=12;b++){
 let h=[a,b],z=closure(i,h);st.closureQueries++;
 if(bySig.has(z.sig)){ck(bySig.get(z.sig)===z.key,"minimal necessity");st.closurePairs++}else bySig.set(z.sig,z.key);
 if(byKey.has(z.key)){ck(byKey.get(z.key)===z.sig,"minimal sufficiency");st.closurePairs++}else byKey.set(z.key,z.sig);
 if(i<items.length&&z.some)for(const e of items[i]){const sub=v=>v.map((x,j)=>x-e[j]);ck(closure(i+1,sub(h)).key===closure(i+1,sub(z.m)).key,"descent");st.closureTransitions++}
 }}
}
function family(m){let p=t=>1n<<BigInt(t),items=[];for(let i=0;i<m-1;i++)items.push([{d:[0n,0n],c:1n},{d:[p(i),0n],c:0n}]);for(let i=0;i<m;i++)items.push([{d:[0n,0n],c:1n},{d:[p(i),p(i)],c:0n}]);return [items,[p(m)-1n,p(m-1)]]}
let [i15,a15]=family(15),j15=solve(i15,a15),l15=solve(i15,a15,false,false);verify(i15,a15,j15,1n);verify(i15,a15,l15,1n);
let [i100,a100]=family(100),j100=solve(i100,a100);verify(i100,a100,j100,1n);
ck(l15.peaks[14]===16384,"lattice lower bound");ck(j15.peaks[14]===1&&j100.peaks[99]===1,"joint prefix collapse");ck(j100.peak<=2&&j15.peak<=2,"joint peak");
return {...st,smallLatticePeak:l15.peak,smallJointPeak:j15.peak,wideJointPeak:j100.peak,wideOptimum:String(j100.c),widePrefixStates:j100.peaks[99]};
}
console.log(run());
```
