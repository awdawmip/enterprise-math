# R861 candidate -- Counterexample-guided character discovery and sharp shared-rank obstruction
2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.
Continuation of R860 at 6643ea611a582beca6847525e0085f8278662bf7:research_notes/portable_direct/R860_MIXED_CHARACTER_ROUNDED_SUPPORT_OBSERVER.md (read at immutable ref). Frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389 retained; P000 V5 and JOINT_RELATION_OBSERVER_PRESERVATION V2 read at that pin. Generated startup and residual companion absent (404); no repin. Global P000 V4 and ACTIVE worldview plus current entries at 0eaa532f037e690cace3e16e2229fb99776e6355; current control protocol at 62a7c454e35b35518527f8a6b05b48dc3ed693b9. Own EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91 recovery metadata verified, execution_authorized=false. R860 owner read SUCCEEDED (empty RUNNING snapshot, 05:17:48 UTC); fresh r3-20261128-r861-running-read admitted, last observed RUNNING/NATIVE_RUNNER. No shared claim or protected state mutation. Auxiliary finite integer resource model, not native BRC arithmetic; original option identities and relation data retained.

## 1. Counterexample-guided exact finite-window membership
Use R859/R860 independent nonempty finite option lists E_i of nonnegative integer r-vectors, with original option identities retained and all local feasibility filtering already done. A suffix word has sum F in S. Fix a prime p, and a finite explicit batch Y in {0,...,p-1}^r (possibly different suffixes or instances with same dimension). All statements are for the declared batch and horizon. Let A be a matrix over F_p, initially empty; chi(F)=AF mod p. Use the R860 additive character DP with normal -1 (all minus ones) to compute m_A(v)=min sum_j F_j among words with chi(F)=v, retaining an exact minimizing original word (empty class = +infinity). For target y:
* If class empty or m_A(Ay)>sum y, certify y absent.
* If the minimizing word has F=y, certify y present.
* Otherwise retain the witness delta=(F-y) mod p. It is nonzero: if F congruent y coordinatewise, F=y+p b with b>=0 since F nonnegative and y_j<p. sum F<=sum y then implies b=0, contradiction. Also A delta=0.
Choose a row b with b.delta !=0 for at least one unresolved witness and append it. Such a row exists (e_j at any nonzero coordinate). Every old row and its span annihilate delta, so the new row raises rank by one. Certified decisions are permanent: an actual word remains an actual word; an absence certificate remains valid under refinement of its class. Rebuild the character table only for unresolved suffixes/instances. After at most r additions, full rank separates all nonzero deltas, so all targets are certified. No enumeration of p^r candidate rows, no enumeration of all suffix words in the support DP. Worst-case character table still p^r; not a general polynomial solver. An arbitrary tied minimum suffices, even for a reachable target. For any h with 0<=h_j<p whose whole integer box is included in Y, collect the certified present targets <=h and take coordinatewise maxima (or DEAD): exactly the R857 minimal suffix observer. A finite list of such exact caps preserves suffix languages and left quotients under every original next option when the next queries are also covered. For arbitrary h outside the declared box, retain the sound R860 cap or refine with an enlarged certified window; no claim of equality to the minimal observer there.

## 2. Deterministic row discovery and a fixed-witness rank bound
For a finite explicit multiset D of nonzero kernel conflicts in F_p^r, uniform random b separates each delta with probability 1-1/p (a nonzero linear form is uniform). Set b's entries successively by maximizing conditional expected separated count over p candidate values. For each delta, if a nonzero coefficient remains unfixed its contribution is 1-1/p; otherwise contribution is its fixed separation indicator. This is an exact rational calculation, O(p r |D|) field operations with incremental partial dot products and last-nonzero positions. Final row separates at least (1-1/p)|D| conflicts. Any nonempty D therefore raises rank when selected from the current kernel. For a FIXED explicit D, discard separated conflicts and repeat: after s rows at most |D|/p^s remain, hence at most min(r, floor(log_p |D|)+1) rows suffice for nonempty D (zero for empty). This log bound does not apply to changing oracle counterexamples, which retain the r bound. Exact minimum for fixed D is r minus the maximum dimension of a subspace K with K intersect D empty; proof by rank-nullity and choosing a quotient map with kernel K. In particular, for binary graph edge differences D={e_u+e_v: uv an edge}, a matrix separates D iff its columns give a proper coloring by at most 2^s labels. Thus minimal number of rows is ceil(log2 chi(G)) for nonempty vertex set (chi=1 yields rank zero). This is a characterization of the explicit witness separation problem, not a reduction of every R860 cap optimization to graph coloring.

## 3. Sharp rank barrier, even with ALL conditional linear supports
Let d>=1, r=2d, p=2, c=(1,...,1). For nonzero x in F_2^d, use its 0/1 representative and define
F_+(x)=c+(x,-x), F_-(x)=c-(x,-x).
Every such vector is nonnegative, has mass 2d, and violates the box F<=c. For any A with fewer than d rows, the restriction x -> A(x,x) has nonzero kernel x. Both F_+(x) and F_-(x) have character Ac. Their midpoint is c, so even the complete continuous convex hull conditioned on this class contains c. The budget intersection is nonempty and c has the correct character as an integer point. No method that reasons ONLY from these class convex hulls, the box and the same character congruences can certify this infeasibility (the relaxation contains c). This applies to the single explicit option group of these 2(2^d-1) vectors. Conversely the d rows reading the first d coordinates mod 2 remove class Ac; all other integer points in the box have mass <2d, excluded by the conditional mass bound. So rank d is necessary and sufficient for exact infeasibility by that relaxation. Distinct integer points and continuous interpolation are not identified with native spatial states.

A polynomial-size family gives the same tight lower bound for one SHARED character matrix (not a separate optimal matrix per instance). For i=1,...,d, use d independent local groups on coordinate pairs (j,d+j). For group j choose (1+a,1-a) with a in {-1,0,1}; at j=i exclude a=0. Other coordinates zero. Total explicit option count per instance 3d-1; vector storage O(d^3) per family if sparse, O(d^3) scalar entries across family if full vectors counted as O(d) times O(d^2) options. No word fits c since pair i is mandatory nonzero. Any rank<d map has nonzero kernel x in the paired subspace; take i with x_i=1, choose all a_j=+x_j or -x_j. Both words occur in instance i, same character as c, midpoint c. Rank d suffices simultaneously as above. Thus no single fixed low-rank shared observer can eliminate all d holes, even when each individual instance admits rank 1 (read pair i's first coordinate mod2, and use mass bound). Adaptive per-instance rank 1 vs shared rank d is a concrete reason to choose suffix-local feature banks rather than force one global bank. For shared rank d the dense mixed table is 2^d versus full coordinate residue table 2^(2d); this is a table capacity comparison, not a reachable-class lower bound or a runtime ratio.

## 4. Cost and verification
For a rank s matrix, one minimum-support DP over N explicit options costs O(N p^s) additions/comparisons after character and mass preprocessing O(N r s); retaining words by direct copying costs up to O(n+r) more per transition, or use backpointers and reconstruct when a witness is needed. The batch queries cost O(|Y| r s) for characters and at most O(|Y| (n+r)) to check reconstructed words per round (naive dense vector addition O(nr) if used). Row discovery O(p r |D|); at most r rebuilds plus initial table. Bit lengths polynomial in explicit entries, n, p, and row lengths. Enumerating all targets in a box may itself be p^r, so the finite-window result is not a general complexity breakthrough. The polynomial-size family requires d different instances and is not a rank lower bound for one polynomial-size instance.
Exact executed author check below uses small bounded integers (all values, counts, bit masks below 2^53, bit width <=16; ordinary JS Number is exact in this range), exhaustive original-word sums for 240 random finite instances, all binary target points, all restricted character maps for d<=3, midpoint witness checks, and a shared family d=1..8 with actual support DP and row refinement. No large-instance brute force or independent review. Fixed seeds and implementation below.
```json
{
  "random_instances": 240,
  "candidate_queries": 6044,
  "brute_words": 18408,
  "table_transitions": 18143,
  "refinements": 156,
  "greedy_checks": 156,
  "max_random_rank": 4,
  "rank_maps": 609,
  "midpoint_witnesses": 434,
  "shared_family": [
    {
      "d": 1,
      "rank": 1,
      "full_classes": 4,
      "mixed_classes": 2
    },
    {
      "d": 2,
      "rank": 2,
      "full_classes": 16,
      "mixed_classes": 4
    },
    {
      "d": 3,
      "rank": 3,
      "full_classes": 64,
      "mixed_classes": 8
    },
    {
      "d": 4,
      "rank": 4,
      "full_classes": 256,
      "mixed_classes": 16
    },
    {
      "d": 5,
      "rank": 5,
      "full_classes": 1024,
      "mixed_classes": 32
    },
    {
      "d": 6,
      "rank": 6,
      "full_classes": 4096,
      "mixed_classes": 64
    },
    {
      "d": 7,
      "rank": 7,
      "full_classes": 16384,
      "mixed_classes": 128
    },
    {
      "d": 8,
      "rank": 8,
      "full_classes": 65536,
      "mixed_classes": 256
    }
  ]
}
```
```javascript
function verify(){
  const ok=(b,m)=>{if(!b)throw Error(m)};
  let seed=861,rand=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return (seed>>>8)%n};
  const sum=v=>v.reduce((a,b)=>a+b,0),eq=(a,b)=>a.every((x,j)=>x===b[j]),add=(a,b)=>a.map((x,j)=>x+b[j]);
  const bits=v=>v.reduce((a,x,j)=>a|((x&1)<<j),0);
  const parity=x=>{let a=0;while(x){a^=1;x&=x-1}return a};
  const chr=(v,rows)=>rows.reduce((a,b,j)=>a|(parity(bits(v)&b)<<j),0);
  let stats={random_instances:0,candidate_queries:0,brute_words:0,table_transitions:0,refinements:0,greedy_checks:0,max_random_rank:0,rank_maps:0,midpoint_witnesses:0,shared_family:[]};
  function table(groups,r,rows){
    let T=new Map([[0,{v:Array(r).fill(0),mass:0,word:[]}]]);
    for(const g of groups){let U=new Map();for(const [k,w] of T)for(let j=0;j<g.length;j++){
      let z=g[j],key=k^chr(z,rows),mass=w.mass+sum(z);stats.table_transitions++;
      if(!U.has(key)||U.get(key).mass>mass)U.set(key,{v:add(w.v,z),mass,word:[...w.word,j]});
    }T=U}return T;
  }
  function greedy(D,r){
    let b=0,rem=(1<<r)-1;
    const score=(b,rem)=>D.reduce((s,d)=>s+((d&rem)?1:2*parity(d&b)),0);
    for(let j=0;j<r;j++){let bit=1<<j;rem^=bit;if(score(b|bit,rem)>score(b,rem))b|=bit}
    ok(D.filter(d=>parity(d&b)).length*2>=D.length,"greedy half");stats.greedy_checks++;return b;
  }
  function refine(problems,r){
    let rows=[],answers=problems.map(p=>p.ys.map(()=>null));
    while(true){
      let D=[];
      for(let i=0;i<problems.length;i++){let {groups,ys}=problems[i],T=table(groups,r,rows);
        for(let j=0;j<ys.length;j++){if(answers[i][j]!==null)continue;let y=ys[j],w=T.get(chr(y,rows));
          if(!w||w.mass>sum(y)){answers[i][j]=false;continue}
          let actual=w.word.reduce((v,k,l)=>add(v,groups[l][k]),Array(r).fill(0));ok(eq(actual,w.v)&&sum(actual)===w.mass,"word");
          if(eq(w.v,y)){answers[i][j]=true;continue}
          let d=bits(w.v)^bits(y);ok(d!==0&&rows.every(b=>!parity(d&b)),"nonzero kernel conflict");D.push(d);
        }
      }
      if(!D.length)return {rows,answers};
      rows.push(greedy(D,r));stats.refinements++;ok(rows.length<=r,"rank bound");
    }
  }
  function brute(groups,r){let S=[Array(r).fill(0)];for(let g of groups)S=S.flatMap(x=>g.map(z=>add(x,z)));stats.brute_words+=S.length;return S}
  for(let k=0;k<240;k++){
    let r=2+rand(5),n=1+rand(5),groups=Array.from({length:n},()=>Array.from({length:2+rand(3)},()=>Array.from({length:r},()=>rand(3))));
    let S=brute(groups,r),ys=Array.from({length:1<<r},(_,b)=>Array.from({length:r},(_,j)=>(b>>j)&1));
    let result=refine([{groups,ys}],r);stats.random_instances++;stats.candidate_queries+=ys.length;stats.max_random_rank=Math.max(stats.max_random_rank,result.rows.length);
    ys.forEach((y,j)=>ok(result.answers[0][j]===S.some(z=>eq(z,y)),"exact membership"));
  }
  function rank(rows,d){let basis=Array(d).fill(0),k=0;for(let x of rows){for(let j=d-1;j>=0;j--)if(x>>j&1){if(basis[j])x^=basis[j];else{basis[j]=x;k++;break}}}return k}
  for(let d=1;d<=3;d++)for(let s=0;s<=d;s++)for(let x=0;x<2**(s*d);x++){
    let rows=Array.from({length:s},(_,j)=>(x>>(d*j))&((1<<d)-1));
    let ker=Array.from({length:(1<<d)-1},(_,j)=>j+1).find(v=>rows.every(b=>!parity(v&b)));
    ok((ker===undefined)===(rank(rows,d)===d),"kernel rank");stats.rank_maps++;
    if(ker!==undefined){
      let c=Array(2*d).fill(1),u=Array.from({length:d},(_,j)=>ker>>j&1);
      let plus=c.map((v,j)=>v+(j<d?u[j]:-u[j-d])),minus=c.map((v,j)=>v-(j<d?u[j]:-u[j-d]));
      ok(plus.every((v,j)=>v+minus[j]===2*c[j])&&plus.some(v=>v>1)&&minus.some(v=>v>1),"midpoint hole");
      ok(rows.every(b=>parity(b&ker)===0),"same class");stats.midpoint_witnesses++;
    }
  }
  for(let d=1;d<=8;d++){
    let r=2*d,c=Array(r).fill(1),problems=Array.from({length:d},(_,i)=>({ys:[c],groups:Array.from({length:d},(_,j)=>{
      let out=[];for(let a of (i===j?[-1,1]:[-1,0,1])){let v=Array(r).fill(0);v[j]=1+a;v[d+j]=1-a;out.push(v)}return out;
    })}));
    let res=refine(problems,r);ok(res.answers.every(x=>x[0]===false),"family infeasible");
    let restricted=res.rows.map(b=>(b&((1<<d)-1))^(b>>d));
    ok(rank(restricted,d)===d&&res.rows.length===d,"tight family rank");
    stats.shared_family.push({d,rank:res.rows.length,full_classes:2**r,mixed_classes:2**d});
  }
  return stats;
}
console.log(JSON.stringify(verify(),null,2));
```

## 5. Next
Develop suffix-local feature replacement with a cost-aware certificate that retains old suffix-language decisions without requiring one shared matrix. Explore whether a polynomial-size single independent-choice instance forces high rank for this exact class-convex relaxation; current lower bound for one instance uses exponential explicit options, and the compact family concerns shared rank only. Recover actual native Port/BRC transfer separately; no native theorem, formal Result or review is claimed.
