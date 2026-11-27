# T6 p17 fixed-basis order optimum and elementary shear audit

2026-11-27 | EM-DVR-DEBB5E | directed, nonblind independent implementation of the other author's new optimum certificate. Original lattice author EM-T6SM-B134BD, original 4891 witness EM-DVR-DEBB5E, optimum and two-shear improvement author EM-DIRECT-8327F7 (RA-184AE178188022AA92EFE075). This Driver's previous 4891 witness is shared context, not independent authorship of that witness. This note is scoped mathematical evidence, not a native review record.

## Exact sources

- Author result c441385b56231b836401dd402826641b054dae3b:research_notes/portable_direct/2026-11-27_t6_p17_basis_order_optimum/README.md (read commit diff).
- Fixed input 996ddf75043e981b87ff8b34ca9f6d4e456dbc3b:research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/p17_q0_certificate.json, verified Git blob d9ac014355a6a1058cc8a0cf2141a01082628881.
- Previous Driver proof b4992484cd931e25ab1215ef2c40b55cd055d998:research_notes/driver/2026-11-27_t6_p17_full_budget_interval_uniqueness.md.

## Review

Work in the same weighted coordinates v_j=(17j-1)u_j, with six congruences modulo 17^k and signed budgets A,B. For each remaining row set S and distinguished i, recompute the orthogonal residual of b_i from scratch against all other rows of S, using primitive integer Gram-Schmidt. The resulting g_i, with d_i=<g_i,b_i>>0, satisfies <g_i,b_j>=0 for every other row in S. Thus g_i/d_i is the unique dual vector in span(S); this is independent of the other author's inverse-dual deletion recurrence. The width is (max(0,g_i)-min(0,g_i))/d_i. For a fixed ordering, signed mass A+B bounds the width of each possible coefficient interval by (A+B)s. For strict width below 1 the safe integer cap is floor((D-1)/N) for s=N/D.

For a threshold s, the feasible deletion search is complete: all strictly better orders must delete a row whose width is <s at the current remaining row set; checking every such row recursively until empty either constructs a better order or excludes all. No floating point or original author's program called.

Original 16-row basis, order [8,5,2,0,1,3,4,9,6,7,13,15,10,11,12,14]:
s=4499962405859179975681503620802131657556552414450801884451136759621202/22009362241807629126111895087560945050967640226441506149068904810154599921, bottleneck row 10, cap 4891.
Exact strict search: reachable remaining sizes 16,15,14,13,12; eligible deletion sets {14},{12},{11},{15},empty. 70 exact width comparisons. Therefore 4891 is optimal for this fixed basis and width certificate, not merely an observed heuristic order.

Apply b13 <- b13-b10 and b9 <- b9-b7 (zero-based). Each is unimodular, preserving the weighted lattice and its underlying congruence kernel. Same witness ordering now yields
s=1030548826800040964456984983424111409196510927609310897149/5133042287601705018579921655423908833108236306427651347343484, bottleneck row 12, cap 4980. Strict search: sizes 16,15, eligible {14},empty; 31 comparisons. Thus 4980 is the best fixed-basis cap for the modified rows.

For any single shear b_i <- b_i+k b_j, i != j, k nonzero integer, while both rows remain the span is unchanged and only normalized dual d_j changes to d_j-k d_i. If i is deleted before j, all earlier widths are unchanged and the remaining rows after deleting i equal the old rows: a strict improvement would contradict fixed-basis optimum. Otherwise, before deleting j the original strictly reachable states must be followed with both rows present. Check all 240+210 ordered pairs on those two states, extending each dual vector with zero. All pairwise coordinate differences must have absolute value strictly less than s. Integer interval intersection is exact, using floor(lower)+1 and ceil(upper)-1. Across 450 ordered pairs, exactly 15 integer-feasible intervals exist, all [0,0], all in the full 16-row state with j=14 and i !=14. No nonzero integer coefficient survives. This independently verifies the author's local optimality for one shear and arbitrary row reordering, with no coefficient truncation.

These results do not establish global optimality over arbitrary unimodular basis changes, or the T6 global lower bound. The previous Driver user-facing summary said 16->1 paths, whereas the underlying previous note recorded 8 at full budget for its immediately preceding order; do not reuse 16 as that order's bound. The 4891 and 4980 cap results are unaffected.

## Reproducer

The following BigInt core was actually executed on the verified JSON input within the tool runtime; the standalone Node file-read wrapper below is supplied for portable reproduction, not separately executed. No original author's implementation imported.

```js
const C=JSON.parse(require("fs").readFileSync(process.argv[2],"utf8")), B=C.weighted_basis.map(r=>r.map(BigInt)),P=[8,5,2,0,1,3,4,9,6,7,13,15,10,11,12,14], all=Array.from({length:16},(_,i)=>i);
const abs=x=>x<0n?-x:x, gcd=(x,y)=>{x=abs(x);y=abs(y);while(y)[x,y]=[y,x%y];return x}, dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n), prim=a=>{let h=a.reduce(gcd,0n);if(!h)throw Error("zero residual");return a.map(x=>x/h)}, proj=(v,g)=>{let d=dot(g,g),t=dot(v,g);return prim(v.map((x,i)=>d*x-t*g[i]))};
function dual(B,S,i){let G=[];for(let j of S)if(j!==i){let v=B[j].slice();for(let g of G)v=proj(v,g);G.push(v)}let v=B[i].slice();for(let g of G)v=proj(v,g);let d=dot(v,B[i]);if(d<0n){v=v.map(x=>-x);d=-d}if(d<=0n||S.some(j=>dot(v,B[j])!==(j===i?d:0n)))throw Error("invalid dual");let lo=v.reduce((a,b)=>a<b?a:b,0n),hi=v.reduce((a,b)=>a>b?a:b,0n);return {v:[...v,0n],d,n:hi-lo}}
const lt=(a,b)=>a.n*b.d<b.n*a.d;
function width(B){let s={n:0n,d:1n},i0=-1;for(let t=0;t<P.length;t++){let w=dual(B,P.slice(0,t+1),P[t]);if(lt(s,w)){s=w;i0=P[t]}}return {n:s.n/gcd(s.n,s.d),d:s.d/gcd(s.n,s.d),bottleneck:i0}}
function strictSearch(B,s){let todo=[all],seen=new Set(),states=[],checks=0;while(todo.length){let S=todo.pop(),key=S.join();if(seen.has(key))continue;seen.add(key);if(!S.length)throw Error("strictly improved order exists");let W=S.map(i=>dual(B,S,i));checks+=S.length;let allowed=S.filter((i,t)=>lt(W[t],s));states.push({S,allowed,W});for(let i of allowed)todo.push(S.filter(j=>j!==i))}return {states,checks}}
function floor(a,b){if(b<=0n)throw Error("bad denom");return a/b-(a<0n&&a%b!==0n?1n:0n)}const ceil=(a,b)=>-floor(-a,b);
function integers(i,j,s){let lo=null,hi=null;for(let a=0;a<17;a++)for(let b=a+1;b<17;b++){let x=(j.v[a]-j.v[b])*i.d*s.d, y=(i.v[a]-i.v[b])*j.d*s.d, z=s.n*i.d*j.d;if(!y){if(abs(x)>=z)return null;continue}if(y<0n){x=-x;y=-y}let l=floor(x-z,y)+1n,h=ceil(x+z,y)-1n;lo=lo===null||l>lo?l:lo;hi=hi===null||h<hi?h:hi;if(lo>hi)return null;}return {lo,hi}}
const M=B.map(r=>r.slice());for(let [i,j] of [[13,10],[9,7]])M[i]=M[i].map((x,k)=>x-M[j][k]);const s0=width(B),s1=width(M),t0=strictSearch(B,s0),t1=strictSearch(M,s1);let pairChecks=0, feasible=[];for(let {S,W} of t1.states)for(let i=0;i<S.length;i++)for(let j=0;j<S.length;j++)if(i!==j){pairChecks++;let a=integers(W[i],W[j],s1);if(a){feasible.push({size:S.length,i:S[i],j:S[j],lo:String(a.lo),hi:String(a.hi)});if(a.lo!==0n||a.hi!==0n)throw Error("nonzero coefficient feasible")}}
const result={old:s0,new:s1,oldStrict:{checks:t0.checks,states:t0.states.map(x=>({size:x.S.length,allowed:x.allowed}))},newStrict:{checks:t1.checks,states:t1.states.map(x=>({size:x.S.length,allowed:x.allowed}))},pairChecks,feasible,oldCap:(s0.d-1n)/s0.n,newCap:(s1.d-1n)/s1.n};console.log(JSON.stringify(result,(_,x)=>typeof x==="bigint"?x.toString():x));
```

## Control boundary

Prior reference request dvr-20261127-1503-t6-rr-c428-reference-p1-v1 remains terminal FAILED SOURCE_MAIN_CAS_RETRY_LIMIT. Original continuation query dvr-20261127-1605-t6-cas-failure-continuation-v1 returned SUCCEEDED, its Source snapshot 78188ca5d47fdcff8b054b4f14f98a87b2aae65f and NO_LIVE_CLAIM / typed frontier are control observations, not permission to interrupt separate active scientific work. Existing RR-C428294CF760BD8D99AA current GitHub blob 62e50de0541fcb25492cffd9354afa8d3a3cda52 and DR-0D8591E64A4073A61E6A blob 7fcaede9f4afb515826746045bc5c0656b321979 preserve the nonterminal RETURN_TO_OWNER. The new same-SID read-only current-flow request dvr-20261127-1700-t6-cas-reconcile-flow-v1 was RUNNING at last read. Do not replay the failed reference request or act on an old flow as current. No new protected mutation, CLAIM, accepted Result, or Task/mother closure.
