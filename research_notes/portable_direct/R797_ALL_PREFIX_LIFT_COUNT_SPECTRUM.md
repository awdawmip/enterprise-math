# R797 — Exact all-prefix lift-count spectrum and weighted factorization

2026-11-25. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation of R796, same research lane EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91. Own SID recovery succeeded, no own RUN, execution_authorized=false. Current owner read r3-20261125-2220-owner-read last observed RUNNING (read job, not an owner). No shared Task/CLAIM/Result/Review changes. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389 P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer contract 3923890d77a02d84b772f789e6912dd14f220d14 retrieved by exact Git blob; ACTIVE worldview and current global/project entry and policies consulted, common immutable global-main snapshot not established. This is an unsigned integer Port branch-count observer, not native signed/amplitude BRC or physical dynamics.

Sources:
- 3e7108d2ba1a0d36a83957d6c01f9e493029eedb:research_notes/portable_direct/R796_EXACT_LIFT_FIBER_AND_MINIMAL_SELECTOR.md
- 1a2471a8b10ac6f0a8d7eadeb05f27def385aff3:research_notes/portable_direct/R795_INTRINSIC_FIXED_RANK_PORT_SELECTOR.md

## 1. Problem and exact spectrum

For R795 source graph G=(V,E), m=|E|, each edge independently has prefix F=3, V=5 or U=6 (both public endpoints allowed, only second, only first respectively). Private selection has 2 lifts at F and 1 at either forced prefix; public selection has 1 lift whenever admitted. Label capacity trees have unique lifts given selected incidences. Fix boundary S=A xor D of size m, P={e:a_e in S}, U=S intersect V. Let L(x,S) count full binary lift assignments for prefix x. Define H_S(z)=sum over x with L>0 of z^(log2 L). Zero count recorded separately as 3^m-H_S(1). Population includes all 3^m actual prefixes once each, not random physical assumptions.

Build the R796 graph H at the all-flexible prefix: on all selected public vertices U, each nonprivate slot with two endpoints in U is an ordinary edge, exactly one endpoint is a stub, no endpoints is impossible. For each component require e+h=v. If S is not size m or these tests fail, H_S=0 since every prefix is a restriction of the all-flexible public choices. Otherwise H consists of rooted trees with exactly one stub, and unicyclic components without stubs, by R796. Write p=|P|; let t be the number of slots (ordinary and stub) in the tree components; for cycle components let ell_i be the cycle length and a_i the number of attached tree edges. Then

H_S(z) = (2+z)^p 2^(t+sum_i a_i) product_i (2^(ell_i+1)-2+z).

Proof: The private slots independently give two prefix values with one lift and one with two. In a tree component there is one orientation, each slot (including its stub) admits that endpoint in exactly two prefix values. Every attached tree edge in a unicyclic component has the same fixed orientation in both possible cycle lifts, and thus also two prefix values. Each cycle orientation permits 2^ell independent prefix vectors on its cycle, and the two vectors sets intersect only in the all-flexible cycle vector. Thus precisely 2^(ell+1)-2 cycle vectors have one orientation and one vector has two. Prefix choices are on distinct slots between components. Multiplication of these polynomials adds the logarithmic lift exponents, as independent lifts multiply. This proves every coefficient exactly. Zero prefixes are all remaining prefixes. No assumptions about the size of G.

Consequences for feasible S:
- Positive-prefix number = 3^p 2^(t+sum a_i) product_i (2^(ell_i+1)-1).
- Max L = 2^(p+c) for c cycles; min positive L=1. Each exponent from 0 to p+c occurs. The minimum over *all* prefixes is zero unless S=A: any public slot uses a fixed set of at most two endpoints; if all forced orientations were valid, varying one selected public endpoint while fixing every other forced orientation would give two different selected public sets of the same size, contradicting fixed S. S=A has no public slots and all forced choices give L=1.
- Sum_x L(x,S)^k = H_S(2^k) for integer k>=1. In particular sum_x L=4^p 2^(m-p+c). Proof: t+sum(a_i+ell_i)=m-p and each cycle factor evaluated at 2 gives 2^(ell_i+1).
- Exact uniform-prefix probabilities follow by division by 3^m; this is an explicitly chosen finite counting measure, not native randomness.

Example triangle with S=V: H=14+z, hence 12 of 27 prefixes fail, 14 admit one lift, 1 admits two. For S=A: H=(2+z)^3=8+12z+6z^2+z^3. This distinguishes support, branch count and prefix-frequency observers.

## 2. Weighted independent prefix law

Allow arbitrary nonnegative integer or rational weights f_e,u_e,v_e on F,U,V for each edge; no normalization necessary. The exact weighted spectrum sums the product of the selected weights for each positive prefix. Replace the private factor by u_e+v_e+f_e z. For each tree or stub slot forced toward endpoint b use q_e(b)=f_e+weight of the prefix forcing b. For each cycle, let Q_+,Q_- be products of q_e(b) over the respective orientations of cycle edges; let R=product of f_e on the cycle. Replace its cycle factor by Q_+ + Q_- - 2R + R z. Attached tree factors remain separate. The same two-event inclusion-exclusion proof applies: intersection requires every cycle edge flexible. Subtraction merely computes the disjoint count of one-orientation prefix events; it is not physical cancellation. Zero-prefix total weight is product_e(f_e+u_e+v_e) minus the spectrum evaluated at 1. Independent nonuniform prefix law and exact moments are immediate.

## 3. Computation and observer boundary

Find components and cycles using linear graph operations and leaf peeling. Factored uniform representation has O(m+n) combinatorial cost; O(m) bits for the source-size exponents under indexed input accounting (retained source and labels are not free or erased); the integer factors themselves have total O(m) bits. Expanded polynomial degree <=m, coefficients each <=3^m, so O(m^2) bits suffice and naive multiplication by linear factors takes O(m^2) integer arithmetic operations; bit complexity also depends on integer multiplication. For weighted factors count arithmetic operations plus weight bit lengths and the exact output size; no uniform bit-time speedup is claimed. Evaluating at z=1 or 2^k needs only product of factors, not expanding prefixes. The formula computes all prefix counts for one fixed S. It does not compute an adversarial minimum over external-selected S. Marginal histograms alone are not generally sufficient for future operations sharing a prefix: one slot's public u and v feasibility each occurs at 2/3 of prefixes but joint feasibility occurs at 1/3, not 4/9. Retain the common prefix labels, source and component incidence for such composition; the exact weighted product factorization is for the stated independent measure and single boundary. Signed BRC weights, event order, provenance and X6 common-depth semantics remain separately retained.

## 4. Exact finite verification

Independent literal XOR local enumeration yields the R795 local table; exhaustive prefix and incidence assignment DP counts full lifts across all cardinality-m S for every nonempty labeled simple graph on 2--4 vertices. Compare both uniform and nonuniform exact histogram coefficients against component factors, and zero prefix weight; weighted cycle factors checked using direct enumeration of the at most two component orientations. This validates the finite scope, not runtime benchmarks or original expanded capacity tree vertices (their uniqueness is used analytically). Integer arithmetic is exact for these inputs, max weights <= 8 per slot, all counts within safe JS integer range.

Actual result:
```json
{
  "graphs": 71,
  "prefixes": 4161,
  "boundaries": 3036,
  "positiveBoundaries": 1872,
  "cycleBoundaries": 93,
  "fullHistComparisons": 3036,
  "coefficientComparisons": 14991,
  "zeroPrefixCount": 321618,
  "positivePrefixCount": 122100,
  "branchPairs": 295252,
  "weightedComparisons": 3036,
  "local": {
    "3": [
      1,
      1,
      2
    ],
    "5": [
      0,
      1,
      1
    ],
    "6": [
      1,
      0,
      1
    ]
  }
}
```

Executable dependency-free JavaScript:
```javascript
function verify(){
 const pc=x=>{let c=0;while(x){x&=x-1;c++}return c}, local={};
 for(const x of [3,5,6]){
  const a=[0,0,0];
  for(let b=0;b<128;b++){
   const [s,t,j,k,u,v,p]=Array.from({length:7},(_,i)=>b>>i&1);
   const z=[s+2*t,s+2*u+4*j,t+2*v+4*k,j+2*k+4*p];
   if(z.every(q=>[0,3,5,6].includes(q))&&z[0]!=(x^5)&&z[1]!=3&&z[2]!=6&&z[3]!=6){
    const S=u+2*v+4*(p^1);if(![1,2,4].includes(S))throw Error("rank");a[[1,2,4].indexOf(S)]++;
   }
  }
  local[x]=a;
 }
 const mult=(a,b)=>{let c=Array(a.length+b.length-1).fill(0);a.forEach((x,i)=>b.forEach((y,j)=>c[i+j]+=x*y));return c};
 const result={graphs:0,prefixes:0,boundaries:0,positiveBoundaries:0,cycleBoundaries:0,fullHistComparisons:0,coefficientComparisons:0,zeroPrefixCount:0,positivePrefixCount:0,branchPairs:0,weightedComparisons:0,local};
 for(let n=2;n<=4;n++){
  const pairs=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)pairs.push([i,j]);
  for(let g=1;g<1<<pairs.length;g++){
   const E=pairs.filter((_,i)=>g>>i&1),m=E.length,T=3**m;
   result.graphs++;const hist=new Map();
   for(let S=0;S<1<<(n+m);S++)if(pc(S)===m)hist.set(S,{h:Array(m+1).fill(0),w:Array(m+1).fill(0),z:0,wz:0});
   let totalWeight=0;
   const weights=E.map((_,i)=>[1+i%3,2+i%2,3]);
   for(let p=0;p<T;p++){
    result.prefixes++;let z=p,dp=new Map([[0,1]]),weight=1;
    for(let i=0;i<m;i++){
     const a=z%3,x=[3,5,6][a];z=Math.floor(z/3);weight*=weights[i][a];
     const next=new Map();for(const [S,c] of dp)for(const [j,k] of [...E[i],n+i].entries()){
      const w=local[x][j];if(w&&!(S>>k&1)){const M=S|1<<k;next.set(M,(next.get(M)||0)+w*c)}
     }dp=next;
    }
    totalWeight+=weight;
    for(const [S,c] of dp){const h=hist.get(S),d=Math.log2(c);if(!Number.isInteger(d))throw Error("not power");h.h[d]++;h.w[d]+=weight;result.positivePrefixCount++;result.branchPairs+=c;}
   }
   for(const [S,actual] of hist){
    result.boundaries++;const U=S&((1<<n)-1),P=E.map((_,i)=>!!(S>>(n+i)&1));
    let p=[1],w=[1],bad=false,cyc=0;
    const adj=Array.from({length:n},()=>[]),stub=Array.from({length:n},()=>[]);
    const admit=(i,v)=>weights[i][0]+weights[i][E[i][0]===v?2:1];
    for(let i=0;i<m;i++){
     if(P[i]){p=mult(p,[2,1]);w=mult(w,[weights[i][1]+weights[i][2],weights[i][0]]);continue}
     const [a,b]=E[i],l=!!(U>>a&1),r=!!(U>>b&1);
     if(!l&&!r){bad=true;break}if(l&&r){adj[a].push([b,i]);adj[b].push([a,i])}else stub[l?a:b].push(i);
    }
    let seen=new Set();
    for(let v=0;v<n&&!bad;v++)if((U>>v&1)&&!seen.has(v)){
     const C=[v];seen.add(v);for(let j=0;j<C.length;j++)for(const [u] of adj[C[j]])if(!seen.has(u)){seen.add(u);C.push(u)}
     const edges=C.flatMap(a=>adj[a].filter(([b])=>a<b).map(([,i])=>i)),stubs=C.flatMap(a=>stub[a].map(i=>[a,i]));
     if(edges.length+stubs.length!==C.length){bad=true;break}
     // Enumerate only orientations of this component to get weighted products and cycle overlap.
     // Uniform formula independently uses component size/cycle length, found by leaf peeling.
     const solutions=[];
     for(let t=0;t<1<<edges.length;t++){
      const used=new Set(stubs.map(([a])=>a));if(used.size!==stubs.length)continue;let ok=true,fac=1;const dest=new Map(stubs.map(([a,i])=>[i,a]));
      for(const [j,i] of edges.entries()){const a=E[i][t>>j&1];if(used.has(a)){ok=false;break}used.add(a);dest.set(i,a)}
      if(ok&&used.size===C.length){for(const [i,a] of dest)fac*=admit(i,a);solutions.push({dest,fac})}
     }
     if(stubs.length===1){if(solutions.length!==1)throw Error("tree");p=mult(p,[2**C.length]);w=mult(w,[solutions[0].fac]);}
     else{
      if(solutions.length!==2)throw Error("cycle");cyc++;
      const [a,b]=solutions;let overlap=1,ell=0;
      for(const [i,v] of a.dest){if(v===b.dest.get(i))overlap*=admit(i,v);else{overlap*=weights[i][0];ell++}}
      p=mult(p,[2**(C.length-ell)*(2**(ell+1)-2),2**(C.length-ell)]);
      w=mult(w,[a.fac+b.fac-2*overlap,overlap]);
     }
    }
    if(bad){p=[];w=[]}else{result.positiveBoundaries++;if(cyc)result.cycleBoundaries++}
    for(let d=0;d<=m;d++){if((p[d]||0)!==actual.h[d]||(w[d]||0)!==actual.w[d])throw Error(JSON.stringify({n,E,S,p,w,actual}));result.coefficientComparisons++;}
    const pos=actual.h.reduce((a,b)=>a+b,0),wpos=actual.w.reduce((a,b)=>a+b,0);
    if(T-pos!==T-p.reduce((a,b)=>a+b,0)||totalWeight-wpos!==totalWeight-w.reduce((a,b)=>a+b,0))throw Error("zero");
    result.zeroPrefixCount+=T-pos;result.fullHistComparisons++;result.weightedComparisons++;
   }
  }
 }
 return result;
}
console.log(JSON.stringify(verify(),null,2));
```

## 5. Next

Study joint spectra for two or more boundaries sharing prefixes, using the intersections of forced orientations and private multiplicity; test if bounded combined separator width enables exact joint-count robust compatibility with a fixed exterior. The larger unique-lift selector remains open; do not infer an impossibility from R796's size-four certificate. No mathematical admission or formal task completion.
