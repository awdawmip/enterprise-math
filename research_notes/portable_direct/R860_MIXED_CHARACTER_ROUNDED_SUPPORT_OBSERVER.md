# R860 candidate — Mixed-character rounded support observer
2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.
Continuation of R859 90dfdbe0c2b095aaa1aa3fa1de16c7a229107c42:research_notes/portable_direct/R859_RESIDUE_CONDITIONED_SUPPORT_OBSERVER.md; R857 minimal suffix observer and R858 rational support retained through R859. Frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389 unchanged; P000 V5 and joint observer read directly there, generated foundation startup returned 404. Global P000 V4 and ACTIVE worldview, global entries at d0e5607d5afe1da43b5016de19e8325338a9e191 read; current continuation, portable, research method and activity protocols read. Existing lane EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91 own recovery metadata verified, execution_authorized=false; R859 owner read SUCCEEDED, empty RUNNING projection as of 2026-11-28T04:20:16.593401Z (Source changed during collection); current r3-20261128-r860-running-read admitted QUEUED. No shared claim or protected mutation. Auxiliary integer-capacity model only, not native BRC execution.

## 1. General projected-character theorem
Reuse independent finite nonempty sets E_i of original option identities with nonnegative integral r-vectors z and additive costs (rational allowed); local analytic feasibility already filtered. F(w) is the sum of the exact suffix word. For integer rows b_l, moduli q_l>=2, define chi(F)=(b_l.F mod q_l)_l in G=product Z/q_l. Choose any finite signed normal bank N. Let B_i(v,a)=max a.F over original suffix words with chi(F)=v; omit unreachable classes. Terminal only zero with support 0. Backward recurrence B_i(v,a)=max_z[a.z+B_(i+1)(v-chi(z),a)] is exact by partition by first option. Full vector and option identity retained in input, not reconstructed from the character. Supports for distinct directions need not share a witness.

For h>=0, the box 0<=F<=h bounds each b_l.F between lo_l=sum min(b_lj,0)h_j and hi_l=sum max(b_lj,0)h_j. Include +/- b_l in N and tighten by conditional supports: lo=max(lo,-B(v,-b_l)), hi=min(hi,B(v,b_l)). Round lo UP and hi DOWN to v_l mod q_l, obtaining L_l,U_l. If L_l>U_l for any l, class impossible. The intervals are necessary jointly, not asserted sufficient. Include unit normals e_j. For each selected positive integer d and signed integer coefficients beta_l, include normal a=d e_j-sum beta_l b_l. Then any feasible word in v obeys
 d F_j <= B_i(v,a)+sum beta_l (U_l if beta_l>=0 else L_l).
Cap coordinate j by the floor of RHS/d, its unit support and h_j. Discard a class if any cap is negative. Take componentwise maximum of caps over surviving classes, or DEAD if none. Every old feasible word survives every operation and lies below its own cap; all caps <=h. Thus F(w)<=h iff F(w)<=K_i(h), with DEAD meaning no feasible word. False surviving classes are allowed. No necessity of recovering all full residues or assuming marginal independence. Negative original budgets DEAD. A single pass is sound. Same suffix language implies equal left quotients under every original next option; retain minimum additive-cost prefix for equal K key, subtract full selected vector then recanonicalize. Exact feasibility, original witness and optimum follow as in R857. Scope is declared finite-horizon budget language; no claim of full state equality or native transfer.

With s rows and G size Q=product q_l, dense preprocessing O((r+s)|N| Q sum |E_i|) integer operations (precompute dot products and characters to improve constants); storage O((n+1)Q(|N|+s)); canonicalization O(Q(r+s r+s |cuts|)) arithmetic. Sparse classes may replace Q. Integer bit lengths polynomial in explicit inputs, coefficient bit lengths, log n and log q_l; output recovery polynomial per transition with direct word copying or backpointers. Outer DP state count not generally polynomial. For one row fixed q, table has at most q classes regardless of r; full residue table can have q^r. Claim concerns exact language-preserving CAP, not equality to R859 cap for arbitrary inputs.

## 2. Mixed-character separation family
For m>=3 put T=2^m, L=T-1, P=T/4-1. There are r=3+d resource coordinates, d>=0 dummy dimensions. Process m-2 prefix bit groups (0 or 2^i on first coordinate, i=0..m-3), then special group (first three coordinates) {(0,0,0),(0,1,0),(0,0,1),(0,1,1),(T,2,1),(T,1,2)}, then m ordinary bit groups i=0..m-1, then d independent dummy groups with 0,1,2 on their own coordinate. Unmentioned entries zero. Budget (L+P,1,1,2,...,2). Bit zero costs 1 and nonzero costs 0; special costs in listed order 2,1,1,0,0,0; dummy k costs 2-k. Optimum 0: choose all bits, special (0,1,1), all dummy 2. High special choices infeasible due to a side coordinate >1. All costs nonnegative.

At each prefix stage remaining prefix sum R, let M=L+R. Every raw residual first budget h lies in [M,L+P]. Suffix low-bit sums cover every integer [0,M] (binary ordinary plus remaining prefix). High options add T; since M>=T-1, the first marginal contains [0,M+T]. Side marginals contain 1 and dummy marginals contain 2. Difference lattice full Z^r because bit 1, special low unit differences and dummy unit differences. Exact marginal clipping cannot remove any such budget.

Even the strongest cap observer conditioning on any ONE ORIGINAL coordinate modulo 3, separately, cannot tighten the budget at these prefix stages, when it uses the continuous convex hull in each conditioned class, enforces the selected coordinate residue on its box, and takes coordinate maxima across classes. For side coordinate 2 use class 1: low (0,1,0) and high (T,1,2), all M bits and dummy 2; interpolate with lambda=(h-M)/T<=1/4 to attain first coordinate h while side 3<=1. Symmetric for side 3. For a dummy coordinate choose residue 2 and interpolate low zero special with either high; lambda<=1/4. For first coordinate choose v=h mod3. Let a=M-((M-v) mod3), c=M-((M+T-v) mod3); both attainable low-bit sums in [M-2,M]. The points with first coordinates a (zero special) and c+T (high special) are in the same class. Their midpoint first coordinate >=M+T/2-2 >=M+P for m>=3. Interpolate from the low point to midpoint to reach h; side 2,3 stay <=1. The attained first coordinate h has the selected residue; any other continuous coordinates need not be integers for this specified relaxation. In every coordinate-conditioned observer the actual feasible word (M,1,1,2,...,2) attains all other original budgets. Thus all these individual conditional convex-cap observers, exact marginal caps and global affine lattice leave the budget unchanged, even under arbitrary repeated composition. This is a lower bound for these specified representations, not all algorithms nor their joint multi-character conditioning. At the cut before special, at least 2^(m-2) distinct keys. Unconditional continuous caps also fail.

In contrast choose the genuinely mixed character chi=F2+F3 mod3. Only 3 table classes. Include unit supports and +/-b, b=e2+e3, and normal a=3e1-T b (d=3,beta=T). At each prefix stage b.h=2; class 0 has rounded U=0. The max of a.F in class 0 is 3M, attained by low zero or high special and all bits. Thus F1<=M in this class. Classes 1,2 have only low special choices, and unit support gives F1<=M. Actual word (M,1,1,2,...,2) attains all caps. Hence K=(M,1,1,2,...,2) for every prefix residual; a single key. After special all remaining side contributions zero, unit supports saturate all other coordinates; each low bit and dummy choice similarly leaves identical canonical key (remaining maxima). All high options rejected by direct negative budget. Exact optimum 0 and exactly one key throughout. Full R859 q=3 residue table has at least 3^d reachable classes at initial suffix from independent dummy options, even with sparse storage. Mixed rank-one table has exactly 3 initial classes and at most 3 throughout. This establishes simultaneous exponential savings in the specified outer keys and full residue preprocessing, with q fixed and coefficient bit length O(m). Independent coordinate tests are not joint tests; the mixed direction retains the cross-coordinate interaction needed for this language.

## 3. Exact executed author verification
Deterministic JavaScript BigInt arithmetic, no native dynamics. The code below is executable as a standalone JS expression with console.log replacing text. Random finite comparisons against full original-word enumeration, including signed character rows and signed dual coefficients; exact support table comparisons at every suffix, language checks, optimal witness reconstruction. The family uses actual DP, not brute force at large dimensions. Small-family interpolation inequality checked exhaustively for all integer R in [0,P], h in [M,L+P], m=3..10 (a,c chosen as proof). General family and language guarantee by proof, not extrapolation from tests.
Results:
```json
{
  "stats": {
    "instances": 240,
    "words": 8415,
    "language": 66965,
    "supports": 1714,
    "feasible": 64,
    "transitions": 3248,
    "witnesses": 69,
    "failures": 0
  },
  "families": [
    {
      "m": 3,
      "d": 0,
      "groups": 5,
      "peak": 1,
      "tablePeak": 3,
      "fullResidueLower": "1",
      "coordinateKeyLower": "2",
      "opt": "0"
    },
    {
      "m": 4,
      "d": 2,
      "groups": 9,
      "peak": 1,
      "tablePeak": 3,
      "fullResidueLower": "9",
      "coordinateKeyLower": "4",
      "opt": "0"
    },
    {
      "m": 8,
      "d": 0,
      "groups": 15,
      "peak": 1,
      "tablePeak": 3,
      "fullResidueLower": "1",
      "coordinateKeyLower": "64",
      "opt": "0"
    },
    {
      "m": 15,
      "d": 5,
      "groups": 34,
      "peak": 1,
      "tablePeak": 3,
      "fullResidueLower": "243",
      "coordinateKeyLower": "8192",
      "opt": "0"
    },
    {
      "m": 100,
      "d": 40,
      "groups": 239,
      "peak": 1,
      "tablePeak": 3,
      "fullResidueLower": "12157665459056928801",
      "coordinateKeyLower": "316912650057057350374175801344",
      "opt": "0"
    }
  ],
  "interpolationChecks": 43945,
  "seed": 860
}
```
```javascript
const verify = function(){
 const mod=(a,q)=>((a%q)+q)%q, dot=(a,b)=>a.reduce((s,x,j)=>s+x*b[j],0n), min=(a,b)=>a<b?a:b,max=(a,b)=>a>b?a:b, floor=(a,b)=>(a-mod(a,b))/b, add=(a,b)=>a.map((x,j)=>x+b[j]),sub=(a,b)=>a.map((x,j)=>x-b[j]),le=(a,b)=>a.every((x,j)=>x<=b[j]),key=a=>a.join(",");
 const stats={instances:0,words:0,language:0,supports:0,feasible:0,transitions:0,witnesses:0,failures:0};const ck=(x,msg)=>{if(!x){stats.failures++;throw Error(msg)}};
 let seed=860;const rnd=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%n};
 const unit=(r,j)=>Array.from({length:r},(_,k)=>BigInt(j===k)), neg=a=>a.map(x=>-x);
 function obs(items,b,q,cuts){
  let r=b.length, N=[...Array.from({length:r},(_,j)=>unit(r,j)),b,neg(b),...cuts.map(({j,d,beta})=>b.map((x,k)=>(k===j?d:0n)-beta*x))];
  let tab=Array(items.length+1);tab[items.length]=new Map([[0n,N.map(()=>0n)]]);
  for(let i=items.length-1;i>=0;i--){let t=new Map();for(let o of items[i])for(let [v,B] of tab[i+1]){let w=mod(v+dot(b,o.d),q),V=N.map((a,k)=>dot(a,o.d)+B[k]),old=t.get(w);t.set(w,old?old.map((x,k)=>max(x,V[k])):V)}tab[i]=t}
  function canon(h,i){if(h.some(x=>x<0n))return null;let lo=dot(b.map(x=>min(x,0n)),h),hi=dot(b.map(x=>max(x,0n)),h),out=null;
   for(let [v,B] of tab[i]){
    let L=max(lo,-B[r+1]),U=min(hi,B[r]);L+=mod(v-L,q);U-=mod(U-v,q);if(L>U)continue;
    let cap=h.map((x,j)=>min(x,B[j]));for(let k=0;k<cuts.length;k++){let {j,d,beta}=cuts[k];cap[j]=min(cap[j],floor(B[r+2+k]+beta*(beta>=0n?U:L),d))}
    if(cap.some(x=>x<0n))continue;out=out?out.map((x,j)=>max(x,cap[j])):cap;
   }return out
  }return {canon,tab,N}
 }
 function solve(items,A,b,q,cuts){let o=obs(items,b,q,cuts),h=o.canon(A,0),D=new Map(),peak=0;
  if(h)D.set(key(h),{h,c:0n,w:[]});peak=D.size;
  for(let i=0;i<items.length;i++){let next=new Map();for(let s of D.values())for(let k=0;k<items[i].length;k++){stats.transitions++;let x=items[i][k],h=o.canon(sub(s.h,x.d),i+1);if(!h)continue;let c=s.c+x.c,z=key(h),old=next.get(z);if(!old||c<old.c)next.set(z,{h,c,w:[...s.w,k]})}D=next;peak=Math.max(peak,D.size)}
  let best=null;for(let s of D.values())if(!best||s.c<best.c)best=s;return {best,peak,tablePeak:Math.max(...o.tab.map(t=>t.size))}
 }
 function words(items,r){let f=[{d:Array(r).fill(0n),c:0n}];for(let t of items)f=f.flatMap(s=>t.map(o=>({d:add(s.d,o.d),c:s.c+o.c})));return f}
 function checkWitness(items,A,s,opt){ck((s===null)===(opt===null),"feasibility");if(s){let d=A.map(()=>0n),c=0n;ck(s.w.length===items.length,"length");s.w.forEach((k,i)=>{d=add(d,items[i][k].d);c+=items[i][k].c});ck(c===opt&&s.c===opt&&le(d,A),"witness");stats.witnesses++}}
 for(let trial=0;trial<240;trial++){let r=2+trial%3,n=1+rnd(5),q=BigInt(2+trial%4),b=Array.from({length:r},()=>BigInt(rnd(7)-3)),cuts=Array.from({length:r*2},(_,k)=>({j:k%r,d:BigInt(1+rnd(4)),beta:BigInt(rnd(9)-4)}));
  let items=Array.from({length:n},()=>Array.from({length:1+rnd(4)},()=>({d:Array.from({length:r},()=>BigInt(rnd(8))),c:BigInt(rnd(9))})));
  let f=words(items,r),A=Array.from({length:r},()=>BigInt(rnd(7*n+1))),opt=null;stats.instances++;stats.words+=f.length;
  for(let w of f)if(le(w.d,A)&&(opt===null||w.c<opt))opt=w.c;if(opt!==null)stats.feasible++;checkWitness(items,A,solve(items,A,b,q,cuts).best,opt);
  let o=obs(items,b,q,cuts);
  for(let i=0;i<=n;i++){let F=words(items.slice(i),r),br=new Map();for(let w of F){let v=mod(dot(b,w.d),q),B=o.N.map(a=>dot(a,w.d)),old=br.get(v);br.set(v,old?old.map((x,j)=>max(x,B[j])):B)}ck(br.size===o.tab[i].size,"residue count");for(let [v,B] of br){ck(key(B)===key(o.tab[i].get(v)),"support");stats.supports++}
   for(let t=0;t<5;t++){let h=Array.from({length:r},()=>BigInt(rnd(7*n+1))),cap=o.canon(h,i);for(let w of F){ck(le(w.d,h)===(cap!==null&&le(w.d,cap)),"language");stats.language++}}
  }
 }
 function family(m,dummy){let r=3+dummy,T=1n<<BigInt(m),L=T-1n,P=T/4n-1n,items=[],vec=(x,y,z)=>[x,y,z,...Array(dummy).fill(0n)],bit=i=>[{d:vec(0n,0n,0n),c:1n},{d:vec(1n<<BigInt(i),0n,0n),c:0n}];
  for(let i=0;i<m-2;i++)items.push(bit(i));items.push([[0n,0n,0n,2n],[0n,1n,0n,1n],[0n,0n,1n,1n],[0n,1n,1n,0n],[T,2n,1n,0n],[T,1n,2n,0n]].map(([x,y,z,c])=>({d:vec(x,y,z),c})));for(let i=0;i<m;i++)items.push(bit(i));for(let j=3;j<r;j++)items.push([0n,1n,2n].map(x=>({d:unit(r,j).map(y=>y*x),c:2n-x})));
  return {items,A:vec(L+P,1n,1n).map((x,j)=>j>=3?2n:x),b:vec(0n,1n,1n),cuts:[{j:0,d:3n,beta:T}]}
 }
 let families=[];for(let [m,d] of [[3,0],[4,2],[8,0],[15,5],[100,40]]){let {items,A,b,cuts}=family(m,d),s=solve(items,A,b,3n,cuts);checkWitness(items,A,s.best,0n);ck(s.peak===1&&s.tablePeak===3,"family peak");families.push({m,d,groups:items.length,peak:s.peak,tablePeak:s.tablePeak,fullResidueLower:(3n**BigInt(d)).toString(),coordinateKeyLower:(1n<<BigInt(m-2)).toString(),opt:s.best.c.toString()})}
 // Exhaust the claimed first-coordinate class convex interpolation inequalities for small m,
 // using rational numerator with denominator 2, without floating point.
 let interpolationChecks=0;
 for(let m=3;m<=10;m++){let T=1n<<BigInt(m),L=T-1n,P=T/4n-1n;
  for(let R=0n;R<=P;R++){let M=L+R;for(let h=M;h<=L+P;h++){let v=mod(h,3n),a=M-mod(M-v,3n),c=M-mod(M+T-v,3n);ck(a>=0n&&c>=0n&&a<=h&&a+c+T>=2n*h&&mod(a,3n)===mod(c+T,3n),"coordinate interpolation");interpolationChecks++}}
 }
 return {stats,families,interpolationChecks,seed:860}
};
console.log(JSON.stringify(verify(),null,2));
```

## 4. Continuation
Next: automatic discovery of a sparse set of mixed characters from actual obstructions, especially how to obtain certified useful rows without testing q^r candidate normals. Investigate lower bound on necessary character rank for families with several independent mixed defects; compare against jointly conditioned support rather than only marginal character caps. General minimum observer remains NP-hard (R857); native BRC correspondence, signed roads/phase/shared bundle propagation and general Port realization open. No raw native branch, phase, path or original option identity deleted. This is an auxiliary finite-budget observer result, not a Foundation/Working Truth admission.
