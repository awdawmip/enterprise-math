# R865 — Budget-conditioned support certificates and zero-slack observation descent
2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.
Predecessor: 4e3b6fa0665dc1da833ab716ffee612a1cf6e2fb:research_notes/portable_direct/R864_REACHABLE_FIBER_BRIDGES_SPARSE_OPTIMALITY.md. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 and joint relation observer read; residual companion at this pin returned 404; no repinning. Global P000 V4 and ACTIVE worldview read, canonical entry snapshot c396321727a82d912b38def92c41d6239ce39c15. Activity RA-708BCC309CE076D8BB599B91 / EM-DIRECT-82A007 own recovery metadata verified; execution_authorized=false. R864 owner query succeeded, empty RUNNING snapshot as of 2026-11-28T09:25:33.675891Z; new original r3-20261128-r865-running-read initially QUEUED. Independent portable research, no shared Task/claim mutation. Auxiliary independent integer capacity certificate model only.

## 1. Conditional support bound and exact observation deletion
Let E_i be nonempty finite indexed option lists of nonnegative integer vectors in dimension r. F(w)=sum_i z_i is the original suffix sum and h an integer upper budget. A is a linear feature over F_p for prime p. For each reachable A-label v define the exact unrestricted conditional support S_v(a)=max_{w:AF(w)=v} a·F(w) for signed integer a. Compute this by the R860 additive max recurrence. Let b be an integer observation row, d positive integer, and lplus,lminus nonnegative integer multiplier vectors. For every feasible word in v,

L_v=ceil((-S_v(-d b-lminus)-lminus·h)/d) <= b·F(w) <= floor((S_v(d b-lplus)+lplus·h)/d)=U_v.

Proof: d b·F=(d b-lplus)·F+lplus·F <= S_v(d b-lplus)+lplus·h; apply the same argument to -b and use integer rounding. Empty unreachable classes do not need bounds. For multiple certified multiplier choices intersect the intervals. If L_v>U_v, discard the class; if L_v=U_v, the omitted integer readout is certified constant, and b·F mod p is recovered from v. More generally a certified set of admissible integer readouts whose residues all agree suffices; a non-singleton contiguous integer interval alone does not certify a residue. Unresolved classes retain the observation or undergo further refinement. This is a sufficient certificate, not necessary; conditional support separation can still have integer holes (R859). Rational multipliers can be used by clearing denominators; no optimizer or completeness is assumed.
For K prescribed rows and one multiplier pair per row, support preprocessing uses at most 2K N p^s candidate shifts, N=sum_i |E_i|, s=number of A rows. Input projection O(Nr(s+K)); each shift includes O(s) field operations plus dictionary cost and integer score operations. Evaluating bounds for h costs O(Kr) arithmetic per v. Bit complexity depends on input and multiplier lengths. This is a certificate cost, not a bound on arbitrary budget optimization.

## 2. Exact budget-conditioned bridge
For fixed suffix i and h denote feasible indexed words by W_i(h). Suppose decoder g_{i,h} satisfies B F(w)=g_{i,h}(A F(w)) mod p on W_i(h). Singleton bounds supply such a decoder on certified classes (empty classes arbitrary; remaining classes must retain B or be certified separately). Define genuinely budget-conditioned support T_{i,h}(v,a)=max_{w in W_i(h), AF(w)=v} a·F(w), or any additive integer objective. Exact B-conditioned support equals max_{v:g_{i,h}(v)=u} T_{i,h}(v,a), with original maximizing witness, by equality of unions of word fibers. Backward recursion selecting z in group i changes h to h-z; child supports and decoders must be certified at that actual residual budget. Then B(z+F)=Bz+g_{i+1,h-z}(AF). Maximizing over original z and reachable child labels yields exact parent budget-conditioned support; empty child domains contribute nothing. Different budgets are not merged. Unrestricted support maximizers cannot be used as feasible witnesses: Section 1 tables supply bounds only. Exact conditioned support may still be hard.

## 3. Zero-slack face certificate and propagation
Choose lambda>=0 integer. Let m_i=min_{z in E_i} lambda·z and M=sum_i m_i. If lambda·h<M, no feasible word exists. For any feasible word,
sum_i(lambda·z_i-m_i)+sum_j lambda_j(h_j-F_j)=lambda·h-M=Delta.
All terms nonnegative. If Delta=0, every feasible word chooses only local minimizers and saturates every resource j with lambda_j>0. Replacing E_i by these indexed minimizers while retaining original budgets preserves exactly the original feasible words. Saturated resource readouts are constants h_j; any row supported on them needs no extra residue label, and other rows may drop their saturated contribution by an affine translation. For Delta>=0, any option with local excess>Delta can be removed, and positive-weight coordinate deficit is at most floor(Delta/lambda_j). This gives an exact interval certificate before constructing residue tables. Cost O(Nr) per weight vector, plus bit costs.
For any viable prefix P on the zero-slack face every chosen option is a minimizer; residual h'=h-F(P) satisfies lambda·h'=sum of remaining minima. Thus the same certificate holds at every remaining stage with constants given by actual residual budget. This proves descent for the finite horizon of indexed option selection. Invalid prefixes have no feasible extensions. All original indexed feasible words remain in the relation; only certified observations are omitted. No identification of different budgets or native cell identities is implied.

## 4. Strict separation without unary pruning; exact cost solver
For prime p and d>=1 take 2d independent groups, two per block j. Each group chooses x or y in {0,...,p-1}, contributing respectively (x,p-1-x) or (y,p-1-y) to its block's two resources, zero elsewhere. Each block budget is (p-1,p-1). The two constraints imply x+y=p-1. All individual choices have a feasible extension (choose complement and arbitrary complements in other blocks), so no sound unary deletion including R863 local minimum propagation removes any option. Unconditioned B reading each block's first coordinate mod p has exactly p^d labels: set y=0 and vary x independently. Every feasible word has B=(p-1,...,p-1), a single conditioned label. Zero-slack lambda=(1,...,1) holds at every viable prefix. There are p^d feasible indexed words, not one. This changes the observation domain and is consistent with R864 unchanged-domain optimality.
For arbitrary additive costs c_{j,1}(x),c_{j,2}(y), exact optimum is sum_j min_{0<=x<p}[c_{j,1}(x)+c_{j,2}(p-1-x)]. Recover original minimizer by each local argmin; check all budgets and cost directly. O(dp) candidate pairs plus input reading (O(d^2 p) dense scalar entries, O(dp) sparse entries) and integer bit costs. Actual solver for disjoint-block family, not general runtime lower bound. Unconditioned table has p^d explicit states; conditioned readout constant. Original budget constraints still carry x/y coupling and are not erased.

## 5. Scope and next question
Closes the first concrete R864 budget-conditioned observation demand question with sufficient certificates that require neither full feasible-language enumeration nor higher feature rank. Reuses R860 conditional support and R864 exact fibers. Next: automatic discovery of nonnegative weights and multipliers, including zero-slack face certificates on overlapping resource incidence graphs; characterize when local face/interval propagation and bounded separator tables certify complete conditioned readouts without solving full integer program. No novelty claim against classical Lagrangian relaxation or constraint propagation; no native BRC/Port attribution or independent review.

## Exact bounded author computation
Fixed seed, JS safe integer arithmetic (rounding divisions bounded, exact integer quotient floors), BigInt exact large counts. Full word enumeration checks signed rational-multiplier bounds, singleton and empty certificates, feasible support aggregation, weighted face filtering and original witnesses. Structured family exhaustively tested p=2,3,5,7 and d=1..3; p=7,d=100 uses analytic factorization, not enumeration. Costs c_i(x)=(i+1)x^2-3x (zero-based i). First execution of draft test failed before completion due to const reassignment in structured test; corrected let declaration and reran entire test. Only successful rerun results below.

```javascript
function verify(){
let seed=8652026;const rng=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return(seed>>>8)%n},ck=x=>{if(!x)throw Error("assertion")},dot=(x,y)=>x.reduce((s,v,j)=>s+v*y[j],0),add=(x,y)=>x.map((v,j)=>v+y[j]),mod=(x,p)=>(x%p+p)%p,key=x=>x.join(","),le=(x,h)=>x.every((v,j)=>v<=h[j]);
const out={random_networks:0,enumerated_words:0,conditional_bounds:0,feasible_word_bound_checks:0,certified_labels:0,bridge_support_checks:0,face_cases:0,face_word_checks:0,structured_cases:0,structured_local_options_checked:0,structured_feasible_words_checked:0};
function words(E,r){let T=[{f:Array(r).fill(0),c:0,w:[]}];for(const G of E)T=T.flatMap(t=>G.map((z,j)=>({f:add(t.f,z.f),c:t.c+z.c,w:[...t.w,j]})));return T}
function support(E,A,p,a){let T=new Map([[key(A.map(()=>0)),0]]);for(const G of E){const U=new Map();for(const [k,c]of T)for(const z of G){const v=A.length?k.split(",").map(Number):[],q=key(v.map((x,j)=>mod(x+dot(A[j],z.f),p))),s=c+dot(a,z.f);if(!U.has(q)||s>U.get(q))U.set(q,s)}T=U}return T}
function bound(E,A,p,b,h,d,lp,lm){const up=support(E,A,p,b.map((v,j)=>d*v-lp[j])),dn=support(E,A,p,b.map((v,j)=>-d*v-lm[j])),R=new Map();for(const [k,s]of up)R.set(k,[Math.ceil((-dn.get(k)-dot(lm,h))/d),Math.floor((s+dot(lp,h))/d)]);return R}
for(let t=0;t<300;t++){
const r=1+rng(4),n=1+rng(5),p=[2,3,5][t%3],E=Array.from({length:n},()=>Array.from({length:1+rng(4)},()=>({f:Array.from({length:r},()=>rng(5)),c:rng(9)-4}))),h=Array.from({length:r},()=>rng(16)),A=Array.from({length:rng(3)},()=>Array.from({length:r},()=>rng(p))),b=Array.from({length:r},()=>rng(5)-2),d=1+rng(4),lp=Array.from({length:r},()=>rng(5)),lm=Array.from({length:r},()=>rng(5)),W=words(E,r),R=bound(E,A,p,b,h,d,lp,lm),lab=f=>key(A.map(a=>mod(dot(a,f),p))),direct=new Map(),best=new Map();
for(const w of W){out.enumerated_words++;if(!le(w.f,h))continue;const k=lab(w.f),[l,u]=R.get(k),v=dot(b,w.f);ck(l<=v&&v<=u);out.feasible_word_bound_checks++;if(!direct.has(k))direct.set(k,new Set());direct.get(k).add(mod(v,p));const q=mod(v,p);best.set(q,Math.max(best.get(q)??-Infinity,w.c))}
const certified=new Map();for(const [k,[l,u]]of R){out.conditional_bounds++;if(l>u)ck(!direct.has(k));if(l===u){certified.set(k,mod(l,p));out.certified_labels++;if(direct.has(k))ck(direct.get(k).size===1&&direct.get(k).has(mod(l,p)))}}
if([...direct.keys()].every(k=>certified.has(k))){const C=new Map(),D=new Map();for(const w of W)if(le(w.f,h)){const k=lab(w.f);C.set(k,Math.max(C.get(k)??-Infinity,w.c))}for(const[k,v]of C){const q=certified.get(k);D.set(q,Math.max(D.get(q)??-Infinity,v))}ck(D.size===best.size);for(const[k,v]of best){ck(D.get(k)===v);out.bridge_support_checks++}}
const lam=Array.from({length:r},()=>rng(3));if(lam.every(x=>x===0))lam[0]=1;const minima=E.map(G=>Math.min(...G.map(z=>dot(lam,z.f)))),face=E.map((G,i)=>G.filter(z=>dot(lam,z.f)===minima[i])),H=face.reduce((s,G)=>add(s,G[0].f),Array(r).fill(0));ck(dot(lam,H)===minima.reduce((a,b)=>a+b,0));const F=words(face,r).filter(w=>le(w.f,H)),original=W.filter(w=>le(w.f,H));ck(F.length===original.length);for(const w of original){ck(w.f.every((x,j)=>!lam[j]||x===H[j]));ck(w.w.every((j,i)=>dot(lam,E[i][j].f)===minima[i]));out.face_word_checks++}out.face_cases++;out.random_networks++;
}
for(const p of [2,3,5,7])for(let d=1;d<=3;d++){
const n=2*d,r=2*d,H=Array(r).fill(p-1),E=Array.from({length:n},(_,i)=>Array.from({length:p},(_,x)=>({f:Array.from({length:r},(_,j)=>j===2*Math.floor(i/2)?x:j===2*Math.floor(i/2)+1?p-1-x:0),c:(i+1)*x*x-3*x}))),W=words(E,r),A=Array.from({length:d},(_,i)=>Array.from({length:r},(_,j)=>+(j===2*i))),T=new Set(),S=new Set(),covered=Array.from({length:n},()=>new Set());let best=Infinity;
for(const w of W){T.add(key(A.map(a=>mod(dot(a,w.f),p))));if(le(w.f,H)){S.add(key(A.map(a=>mod(dot(a,w.f),p))));w.w.forEach((x,i)=>covered[i].add(x));best=Math.min(best,w.c);out.structured_feasible_words_checked++}}
ck(T.size===p**d&&S.size===1);ck(covered.every(s=>s.size===p));out.structured_local_options_checked+=n*p;
let fact=0;for(let j=0;j<d;j++)fact+=Math.min(...Array.from({length:p},(_,x)=>E[2*j][x].c+E[2*j+1][p-1-x].c));ck(fact===best);out.structured_cases++;}
const p=7,d=100;let opt=0,vis=0,w=[];for(let j=0;j<d;j++){let best=Infinity,bx=0;for(let x=0;x<p;x++){let y=p-1-x,c=(2*j+1)*x*x-3*x+(2*j+2)*y*y-3*y;vis++;if(c<best){best=c;bx=x}}opt+=best;w.push(bx,p-1-bx)}ck(w.every((x,i)=>i%2||x+w[i+1]===p-1));ck(w.reduce((s,x,i)=>s+(i+1)*x*x-3*x,0)===opt);out.large_factorized_optimum={p,d,visited_pairs:vis,optimum:opt,feasible_word_count:(BigInt(p)**BigInt(d)).toString(),unconditioned_label_count:(BigInt(p)**BigInt(d)).toString(),conditioned_label_count:1};return out}
console.log(JSON.stringify(verify()));
```

```json
{
  "random_networks": 300,
  "enumerated_words": 9772,
  "conditional_bounds": 983,
  "feasible_word_bound_checks": 2453,
  "certified_labels": 25,
  "bridge_support_checks": 6,
  "face_cases": 300,
  "face_word_checks": 452,
  "structured_cases": 12,
  "structured_local_options_checked": 204,
  "structured_feasible_words_checked": 607,
  "large_factorized_optimum": {
    "p": 7,
    "d": 100,
    "visited_pairs": 700,
    "optimum": 179097,
    "feasible_word_count": "3234476509624757991344647769100216810857203198904625400933895331391691459636928060001",
    "unconditioned_label_count": "3234476509624757991344647769100216810857203198904625400933895331391691459636928060001",
    "conditioned_label_count": 1
  }
}
```
All assertions passed.
