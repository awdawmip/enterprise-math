# R864 — Reachable-fiber bridges and sparse-state optimality of cumulative demands
2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.
Predecessor: 1adf38377fde835e6d0c1d865f3c0b6b3313da78:research_notes/portable_direct/R863_SUFFIX_LOCAL_CHARACTER_BRIDGES.md. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: p000_reality_foundation.json V5 and definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json read. Global canonical entries read at bc666567c9d0e1251c87bdb655716034fcbfe8df, global P000 V4 projection canonical blob matched, ACTIVE worldview read. Own activity RA-708BCC309CE076D8BB599B91 / EM-DIRECT-82A007, recovery metadata verified; execution_authorized=false. Current running owner read r3-20261128-r864-running-read last observed RUNNING / NATIVE_RUNNER. Independent portable research only, no shared claim change. Auxiliary independent integer option model, not native BRC/Port realization.

## 1. Reachable-fiber criterion and a bounded exact test
Let p be prime, E_k nonempty finite indexed integer vector option lists in dimension r, fixed order. S_i denotes the integer sums of suffix words, including all original indexed choices for witnesses. Reduce modulo p only for feature labels. For a fixed child feature A:F_p^r -> F_p^s and parent feature B:F_p^r -> F_p^t, the (possibly nonlinear) decoder f with Bx=f(Ax) on S_i mod p exists iff no two reachable points have the same A label and different B labels. Affine centering is equivalent by fixed translations. The criterion is exact for this suffix and these observations, not arbitrary future added options.

Compute the joint image of partial sums from zero, storing a dictionary keyed by A label, with B label and one original indexed word witness. For each next local option, add its A and B labels to each entry. If two candidate entries collide on A but not B, return both partial words, extending both by the same arbitrary remaining word. Their A equality and B inequality persist by translation, so this is a full suffix counterexample. If no collision, retaining one witness per A label preserves the exact joint image: equal A and B labels undergo identical shifts for every option. Induction proves exactness. At completion the dictionary is the decoder on reachable labels; unreachable labels are irrelevant. In successful or pre-failure steps the table has at most p^s entries, not p^(s+t). Let R_k be the number of reachable A labels after k local groups, and N=sum_k |E_k|. At most sum_k |E_k| R_{k-1} <= N p^s candidate shifts are needed; on an unsuccessful test only a prefix of the final failing layer is needed. Precompute feature labels with O(N r(s+t)) field operations; shifts and comparisons cost O(s+t) each, plus dictionary overhead (or deterministic balanced-tree logarithmic factor). Store persistent witness pointers, O(sum_k R_k) records before the failure, with word recovery O(n); working label space O(p^s(s+t)). This is a bounded-by-child-alphabet test and not a polynomial-time guarantee for unbounded s. It requires no enumeration of original words or parent-alphabet table.

A collision supplies delta=x-y mod p !=0, A delta=0, B delta !=0. Appending any row b with b delta !=0 strictly increases rank and removes this collision. A coordinate row with nonzero delta suffices. Restart the bounded test with refined A; at most r-rank(A_initial) refinements until success. This is a constructive upper bound, not a minimum rank algorithm; costs sum over the actual successive ranks. Each failure returns two original indexed words.

## 2. Exact nonlinear support bridge
For suffix i+1 choose child A and parent B=A_i. With centered labels and baselines t_i from R863, if the decoder f is certified on uncentered child labels, shift its input/output by the known baseline labels to obtain a centered decoder g. Then chi_i(z+F)=B(z-b_i)+g(chi_{i+1}(F)) mod p for every z and actual child F. For each fixed signed integer support direction a, maximize a dot z + B_{i+1}(u,a) over reachable u and indexed z giving the parent label. Because the bridge is constant on the whole actual child fiber and the score is additive, this gives exact conditional support values and original maximizing words by induction, even though g is nonlinear. Different directions may have different witnesses; never combine witnesses into a fabricated joint state. The unchanged R859/R860 sound budget cuts may consume these exact values. If needed for DP feasibility/cost, equality of feasible-suffix languages from R857 still justifies merging equal capacity states and retaining least cost; the bridge does not by itself reduce their number.

## 3. Obstruction: nonlinear compression cannot reduce the minimal sparse class count under unchanged demands
Let D_k be the fixed linear feature matrix demanded at suffix k, with centered or uncentered labels. A general schedule has arbitrary finite-valued observation maps phi_i on actual suffix sums, exact demand readout at each stage, and deterministic backward transitions phi_k(z+F)=T_k(z,phi_{k+1}(F)) for every indexed z and actual F. Fix baselines for groups. For any i and k<=i, if phi_i(F)=phi_i(F'), apply the same baseline prefix from i back to k and read D_k there. Linearity and cancellation of the prefix imply D_k(F-F')=0 mod p. Thus every phi_i fiber is contained in a fiber of the cumulative map L_i(F)=(D_0 F,...,D_i F) mod p. Conversely L_i is a valid schedule: child L_{i+1} determines parent L_i by truncation and translation by D_k z; it exposes D_i. On actual S_i its fibers are exactly those of R863's minimal compatible row space W_i=sum_{k<=i} res_{V_i} D_k, since differences of reachable suffix sums belong to V_i and the restricted row spans are equal. Consequently the minimum number of reachable labels among ALL deterministic schedules with these demands equals |L_i(S_i)|, and R863 already attains it pointwise. This is stronger than its linear rank optimum: no nonlinear decoder can improve the sparse reachable class count with those exact readouts and operation horizon. A nonlinear representation may use fewer field coordinates or a smaller dense ambient table, but may require a lookup and extra discovery. To obtain further sparse-state reduction one must change the observation demand (e.g. use budget-conditioned or objective-conditioned equivalence), alter operation horizon, or use implicit non-enumerative support formulas. No claim for arbitrary original-state identity, multiplicity, or native geometry. The fixed indexed words remain the evidence population.

## 4. Exponential dense gap with zero sparse gain
Over p=3 take d disjoint two-coordinate groups E_j={(0,0),(1,1),(2,1)} on coordinates (x_j,y_j). Let child demand read x, parent demand read y. The actual relation is y_j=1_{x_j!=0}. All 3^d distinct x vectors occur; a rank-d child suffices for exact nonlinear decoding. At least d field coordinates are necessary for any F_3-valued feature recovering x. But differences (1,1),(2,1) have nonzero determinant mod 3, so the affine hull has dimension 2d, and linear bridges retaining both demands require rank 2d. Dense table capacities are 3^d versus 3^(2d), while both schemes have exactly 3^d reachable classes. For each parent y pattern exact support is the maximum over matching child x classes, so parent table has 2^d entries. This family has 3d indexed options, O(d^2) dense scalar entries. The example is an exact bridge/readout separation, not a full optimization runtime lower bound. A coordinatewise indicator decoder uses O(d) operations without a dictionary in this specific family. No general cheap implicit decoder is asserted.

## 5. Next question
The genuine next step is to weaken demand semantically while retaining the full feasible-suffix language, rather than merely replacing linear by nonlinear labels. Investigate budget-conditioned support tables with deletion certificates, and whether their conditional observation demand can be inferred without enumerating the exact feasible language (NP-hard in general per R857). A second concrete question: certify separable decoder formulas from local option structure at less cost than the generic dictionary test. No independent review, literature novelty claim, formal acceptance, or native attribution.

## Executed bounded verification
Exact JS integer arithmetic in safe range. Seed fixed, finite small random networks; direct full suffix word enumeration independently checks decoder outcomes and returned collision witnesses; baseline-prefix readout partition check; p=3 disjoint nonlinear example support maxima readout. Proof above establishes general quantifiers; bounded computation is author cross-check, not a universal exhaustive proof.

```javascript
()=>{
 const out={instances:0,bridge_success:0,bridge_collision:0,collision_word_checks:0,bridge_transitions:0,reachable_pairs:0,refinement_steps:0,schedule_stage_checks:0,support_classes:0,gap_instances:0};
 let seed=8642026; const rand=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return (seed>>>8)%n};
 const mod=(x,p)=>(x%p+p)%p, add=(a,b,p)=>a.map((x,j)=>mod(x+b[j],p)), dot=(a,b)=>a.reduce((s,x,j)=>s+x*b[j],0), map=(A,x,p)=>A.map(a=>mod(dot(a,x),p)), key=x=>x.join(","), ck=x=>{if(!x)throw Error("assertion")};
 function sums(E,r,p){let T=[{v:Array(r).fill(0),w:[]}];for(const G of E)T=T.flatMap(o=>G.map((z,j)=>({v:add(o.v,z,p),w:[...o.w,j]})));return T}
 function bridge(E,A,B,r,p){let T=new Map([ [key(A.map(()=>0)),{v:B.map(()=>0),x:Array(r).fill(0),w:[]}] ]);
 for(let i=0;i<E.length;i++){const U=new Map();for(const [k,o] of T)for(let j=0;j<E[i].length;j++){const z=E[i][j], x=add(o.x,z,p),u=key(map(A,x,p)),v=map(B,x,p),w=[...o.w,j];out.bridge_transitions++;const old=U.get(u);if(old&&key(old.v)!==key(v)){const tail=E.slice(i+1).map(()=>0);return {ok:false,w:[old.w.concat(tail),w.concat(tail)]}}if(!old)U.set(u,{v,x,w})}T=U;ck(T.size<=p**A.length)}
 return {ok:true,T}}
 function direct(E,A,B,r,p){const T=new Map();let ok=true;for(const {v} of sums(E,r,p)){const u=key(map(A,v,p)),b=key(map(B,v,p));if(T.has(u)&&T.get(u)!==b)ok=false;T.set(u,b);out.reachable_pairs++}return {ok,T}}
 for(let t=0;t<320;t++){const p=[2,3,5][t%3],r=1+rand(5),n=1+rand(5),E=Array.from({length:n},()=>Array.from({length:1+rand(4)},()=>Array.from({length:r},()=>rand(p)))),A=Array.from({length:rand(3)},()=>Array.from({length:r},()=>rand(p))),B=Array.from({length:1+rand(3)},()=>Array.from({length:r},()=>rand(p)));let C=A.slice();
 for(;;){const a=bridge(E,C,B,r,p),b=direct(E,C,B,r,p);ck(a.ok===b.ok);
 if(a.ok){out.bridge_success++;ck(a.T.size===b.T.size);for(const [k,o]of a.T)ck(key(o.v)===b.T.get(k));break}
 out.bridge_collision++;const x=a.w.map(w=>w.reduce((s,j,i)=>add(s,E[i][j],p),Array(r).fill(0)));ck(key(map(C,x[0],p))===key(map(C,x[1],p)));ck(key(map(B,x[0],p))!==key(map(B,x[1],p)));out.collision_word_checks+=2;const j=x[0].findIndex((v,k)=>v!==x[1][k]);C.push(Array.from({length:r},(_,k)=>+(k===j)));out.refinement_steps++;ck(C.length<=A.length+r)}
 // Compare cumulative centered demand readouts with exact baseline-prefix observations.
 const D=Array.from({length:n},()=>Array.from({length:1+rand(2)},()=>Array.from({length:r},()=>rand(p))));
 for(let i=0;i<=n;i++){const X=sums(E.slice(i),r,p),P=new Map(),R=new Map();for(const {v} of X){const tuple=key(map(D.slice(0,i+1).flat(),v,p));let baseline=Array(r).fill(0),obs=[];for(let k=i;k>=0;k--){if(k<n)obs.push(key(map(D[k],add(v,baseline,p),p)));if(k>0)baseline=add(baseline,E[k-1][0],p)}const q=obs.join("|");if(P.has(tuple))ck(P.get(tuple)===q);if(R.has(q))ck(R.get(q)===tuple);P.set(tuple,q);R.set(q,tuple)}ck(P.size===R.size);out.schedule_stage_checks++}
 out.instances++}
 // Nonlinear bridge example, exact conditional support DP for arbitrary signed direction.
 for(let d=1;d<=6;d++){const r=2*d,p=3,eye=j=>Array.from({length:r},(_,k)=>+(j===k)),E=Array.from({length:d},(_,j)=>[Array(r).fill(0),add(eye(j),eye(d+j),p),add(eye(j).map(x=>2*x),eye(d+j),p)]),A=Array.from({length:d},(_,j)=>eye(j)),B=Array.from({length:d},(_,j)=>eye(d+j));const a=bridge(E,A,B,r,p);ck(a.ok&&a.T.size===3**d);const dirs=[Array.from({length:r},(_,j)=>j%5-2),Array(r).fill(1)];
 // Here coordinates have disjoint supports, so integer sums equal residues.
 const L=sums(E,r,p),T=new Map();for(const {v}of L){const k=key(map(A,v,p)),z=dirs.map(b=>dot(b,v)),old=T.get(k);T.set(k,old?old.map((x,j)=>Math.max(x,z[j])):z)}
 const U=new Map();for(const [k,z]of T){const q=key(a.T.get(k).v),old=U.get(q);U.set(q,old?old.map((x,j)=>Math.max(x,z[j])):z)}
 const V=new Map();for(const {v}of L){const q=key(map(B,v,p)),z=dirs.map(b=>dot(b,v)),old=V.get(q);V.set(q,old?old.map((x,j)=>Math.max(x,z[j])):z)}
 ck(U.size===2**d&&V.size===U.size);for(const [k,z]of V){ck(key(z)===key(U.get(k)));out.support_classes++}
 ck(L.length===3**d);out.gap_instances++}
 return out
}
console.log(JSON.stringify(verify()));
```

Actual result:
```json
{
  "instances": 320,
  "bridge_success": 320,
  "bridge_collision": 352,
  "collision_word_checks": 704,
  "bridge_transitions": 13171,
  "reachable_pairs": 24434,
  "refinement_steps": 352,
  "schedule_stage_checks": 1265,
  "support_classes": 126,
  "gap_instances": 6
}
```
All assertions passed.
