# R800 — Exact Boolean common-prefix counting hardness via connector stretching

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation of R799. Own researcher EM-DIRECT-82A007, Activity RA-708BCC309CE076D8BB599B91; own session metadata recovered, no RUN, execution_authorized=false. Owner read r3-20261126-0117-owner-read was RUNNING at last observation before this proof; not evidence of an empty owner list. No shared Task/CLAIM/Result/Review change. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389, P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer blob 3923890d77a02d84b772f789e6912dd14f220d14. ACTIVE worldview and canonical account entries at main@2ee52e0c0ac2200c6850f22403dac8d49ee945b1, current portable and method policies consulted. Scope: unsigned Boolean/integer auxiliary Port observer, preserving the original common-prefix carrier, signed native BRC, time order and common depth separately.

Exact predecessor sources:
- 1a2471a8b10ac6f0a8d7eadeb05f27def385aff3:research_notes/portable_direct/R795_INTRINSIC_FIXED_RANK_PORT_SELECTOR.md
- 2e9d7f8540edc05f8b2569278333d467cdcb2855:research_notes/portable_direct/R798_COMMON_PREFIX_JOINT_LIFT_SPECTRUM.md
- 9b0c500f0972f718ee7a2ba3e674448f53f40188:research_notes/portable_direct/R799_UNIVERSAL_CYCLE_OVERLAP_AND_MIXED_MOMENT_HARDNESS.md

## 1. New exact Boolean counting result

Let B=(L,R,F) be any finite simple bipartite graph, n=|L|+|R|, q=|F|. For n=0 the spin partition is 1, so assume n>=1. Reuse the R799 subcubic realization: one cycle C_v per vertex, common marked slot per edge in F, all positive directions agree on common slots. A connector is a slot used publicly in exactly one observation, privately in the other. Every nonisolated C_v has 2 deg(v) connectors; every isolated triangle has 3. Independently subdivide one connector of each cycle by k fresh edges (replace it by a path of k+1 edges). Update the corresponding fixed boundary S_i by adding the new public vertices to its own side, and choosing every inactive slot privately in the opposite side, as in R799. The source remains simple and subcubic. Both boundaries remain fixed rank m=|E(G)| in the common A-twist: active edges and selected public vertices have equal counts, and other edges are selected privately. The R795 local prefix F allows either endpoint, U and V force one; private selection is always feasible. There are 3^m independent prefixes with unit weights. No extra boundary-layer filter is needed.

Let c_v be the number of connectors on C_v after padding, C=sum_v c_v=m-q, D=2^C. Define H=H_12(1,1)=#{x:L_1(x)>0 and L_2(x)>0}. For each cycle-direction vector sigma in {+,-}^n define A_sigma as the set of actual prefixes satisfying all its indicated public endpoint demands. Private slots impose no feasibility restriction. Thus H=|union_sigma A_sigma|. Each connector has two admissible prefixes for a fixed orientation, and each common slot has two if directions agree, one if they disagree. Consequently
  |A_sigma|=D*2^(number of agreeing F edges);
  T=sum_sigma |A_sigma|=D*Z_B(2),
where Z_B(2)=sum_sigma 2^(number of agreeing edges), the same partition function as R799.

This T counts (prefix, cycle-direction vector), NOT private internal multiplicities. For x in the union write M(x)=#{sigma:x in A_sigma}; the exact excess is T-H=sum_x(M(x)-1). A cycle is ambiguous when both of its direction constraints hold at x. If M(x)>1 at least one cycle is ambiguous. For a fixed sigma, x uniformly in A_sigma is independent over slots, and each connector is flexible with probability 1/2. An ambiguous cycle requires all its c_v connectors flexible (shared slots can only add restrictions). Hence
  0 <= T-H <= sum_sigma sum_v #{x in A_sigma : C_v ambiguous}
             <= T sum_v 2^(-c_v).
The first inequality is a union bound on marked (prefix, direction) pairs; each nonzero excess fiber is covered, with possible overcount. In particular this is a certified relative-error bound for replacing the Boolean count by the orientation mass, in the declared observation only. No individual ambiguous prefix is identified with a unique one.

## 2. Exact integer recovery from one Boolean query

Choose k=2n+q, so every c_v>=k and Z<=2^(n+q). Then
  0 <= Z_B(2)-H/D <= 2^(n+q) n 2^(-k)=n/2^n <= 1/2.
Therefore exactly
  Z_B(2)=ceil(H_12(1,1)/2^(m-q)).
The ceiling is integer division (H+D-1)//D, no floating-point arithmetic. Padding needs nk new vertices and edges, hence |V(G)|=4q+3i+nk, |E(G)|=5q+3i+nk, maximum degree 3; i is the number of isolated vertices. The entire transformation, division and exact bit lengths are polynomial in |B|. This is one Boolean-oracle call per R799 spin-partition query, and the unpadded R799 mixed moment can also be recovered by multiplying this integer by 3^(m_original-q).

R799 section 3 proves #P-hardness of Z_B(2) on simple bipartite graphs under polynomial-time Turing reductions by interpolation of a cut polynomial from exact independent-set counts. Use that exact reduction, followed by the new one-query transformation. For the Boolean problem, membership in #P is not proved by guessing lifts (which would overcount); guess only a prefix and deterministically test the two fixed boundaries using bipartite matching via R795, or the cycle component test. A three-state choice can use two bits and reject the fourth code. Each feasible prefix then has exactly one accepting witness. Thus H_12(1,1) is #P-complete under polynomial-time Turing reductions, even for the subcubic R795 realization, uniform weights and exactly two boundaries. Literature for the source #IS hardness: S. Vadhan, The Complexity of Counting in Sparse, Regular, and Planar Graphs, SIAM J. Comput. 31 (2001), 398-427, doi:10.1137/S0097539797321602. The #P result is for exact counting, not a lower bound for approximation.

## 3. Independent exact contraction and error coordinate

For this realization each connector is public only to one observation. At z_1=z_2=1 the R798 inclusion-exclusion formula reduces to a ternary spin system. A cycle variable +/- has unary factor 2^c_v; star has unary factor -1. A shared edge contributes 2 only for equal nonstar directions, and 1 otherwise. This retains the complete Boolean union count, with star representing the intersection of both orientation events, not native signed amplitude.

There is an independent nonnegative expression: enumerate prefixes only on the q shared slots. At each v let mask_v be the set of directions allowed by those shared prefixes. For local connectors the number of prefixes allowing some permitted direction is 0 for an empty mask, 2^c_v for a singleton, and 2^(c_v+1)-1 for both directions (exactly one connector tuple allows both). Multiply over v and sum over shared prefixes. This yields H with no negative weights and gives an independent O(3^q(n+q)) arithmetic algorithm, useful when q is small even if connectors are long. All integer bit lengths must be included in implementation costs.

The error bound also gives an explicit observer lease: when sum_v 2^-c_v <= epsilon < 1, H lies between (1-epsilon)T and T. It does not remove cycle ambiguity from per-prefix provenance, or apply to arbitrary dependent prefix weights without a separate bound. For nonuniform independent weights, the analogous proof replaces 2^-c_v by the product over connectors of the conditional flexible weight divided by the total admitted weight under the chosen direction, and takes a bound valid uniformly over directions with nonzero mass.

## 4. Exact replay

Executed the following dependency-free JavaScript with BigInt. It compares the nonnegative shared-prefix expression, the signed ternary contraction, the binary spin sum and the certified error interval. For small unpadded cases it independently enumerates all slot-prefix assignments and tests all cycle masks. It uses R795 and R799's proved realization and local table, not a new expanded XOR/label-tree simulation; no independent proof review or actual end-to-end #IS interpolation is claimed. Labeled bipartite graphs on part sizes (1,1),(1,2),(2,1),(2,2),(2,3),(3,3), including empty graphs; three connector lengths per graph (unpadded, +1, +k). Actual output:
```json
{
  "graphs": 602,
  "cases": 1806,
  "roundingChecks": 602,
  "sharedPrefixCases": 799596,
  "fullPrefixes": 66582,
  "examples": [
    {
      "a": 1,
      "b": 1,
      "q": 1,
      "pad": 5,
      "m": 15,
      "H": "97793",
      "D": "16384",
      "Z": "6",
      "deficit": "511"
    },
    {
      "a": 2,
      "b": 2,
      "q": 4,
      "pad": 12,
      "m": 68,
      "H": "1512612747983298494465",
      "D": "18446744073709551616",
      "Z": "82",
      "deficit": "20266060884738047"
    },
    {
      "a": 3,
      "b": 3,
      "q": 9,
      "pad": 21,
      "m": 171,
      "H": "16099901938051894644954375583110699619544651215667201",
      "D": "5846006549323611672814739330865132078623730171904",
      "Z": "2754",
      "deficit": "98785331901977416534091874124985101677756415"
    }
  ],
  "mismatches": 0
}
```
```javascript
function verify(){
  const pow2=k=>1n<<BigInt(k);
  function check(n,F,c,brute=false){
    const q=F.length, m=q+c.reduce((a,b)=>a+b,0), D=pow2(m-q);
    let Z=0n;
    for(let s=0;s<2**n;s++){let agree=F.filter(([u,v])=>(s>>u&1)===(s>>v&1)).length; Z+=pow2(agree)}
    let H=0n;
    // Direct shared-prefix enumeration; connector prefix classes counted independently.
    for(let s=0;s<3**q;s++){
      let t=s, allowed=Array(n).fill(3);
      for(const [u,v] of F){let p=t%3;t=Math.floor(t/3);let mask=[3,1,2][p];allowed[u]&=mask;allowed[v]&=mask}
      let prod=1n;
      for(let v=0;v<n;v++)prod*=allowed[v]===3?2n*pow2(c[v])-1n:allowed[v]===0?0n:pow2(c[v]);
      H+=prod;
    }
    let signed=0n;
    for(let s=0;s<3**n;s++){
      let t=s, a=[], prod=1n;
      for(let v=0;v<n;v++){let p=t%3;t=Math.floor(t/3);a.push(p);prod*=p===2?-1n:pow2(c[v])}
      for(const [u,v] of F)if(a[u]!==2&&a[u]===a[v])prod*=2n;
      signed+=prod;
    }
    if(signed!==H)throw Error("signed contraction");
    let deficit=D*Z-H;
    if(deficit<0n||deficit> Z*c.reduce((a,b)=>a+D/pow2(b),0n))throw Error("deficit bound");
    let rounds=(H+D-1n)/D;
    let direct=0n;
    if(brute){
      let slots=F.slice();for(let v=0;v<n;v++)for(let j=0;j<c[v];j++)slots.push([v]);
      for(let s=0;s<3**m;s++){let t=s,a=Array(n).fill(3);for(let vs of slots){let p=t%3;t=Math.floor(t/3);for(let v of vs)a[v]&=[3,1,2][p]}if(a.every(v=>v))direct++}
      if(direct!==H)throw Error("literal slot enumeration")
    }
    return {H,Z,D,deficit,rounds,m,brute:brute?3**m:0};
  }
  let graphs=0,cases=0,roundingChecks=0,sharedPrefixCases=0,fullPrefixes=0,examples=[];
  for(let [a,b] of [[1,1],[1,2],[2,1],[2,2],[2,3],[3,3]]){
    let n=a+b,P=[];for(let u=0;u<a;u++)for(let v=0;v<b;v++)P.push([u,a+v]);
    for(let mask=0;mask<2**P.length;mask++){
      let F=P.filter((_,i)=>mask>>i&1),q=F.length,d=Array(n).fill(0);
      for(let [u,v] of F){d[u]++;d[v]++}
      let base=d.map(v=>v?2*v:3),k=2*n+q;
      for(let pad of [0,1,k]){
        let c=base.map(v=>v+pad),r=check(n,F,c,pad===0&&q+c.reduce((x,y)=>x+y,0)<=9);
        cases++;sharedPrefixCases+=3**q;fullPrefixes+=r.brute;
        if(pad===k){roundingChecks++;if(r.rounds!==r.Z)throw Error("exact recovery")}
        if(a===b&&mask===2**P.length-1&&pad===k)examples.push({a,b,q,pad,m:r.m,H:String(r.H),D:String(r.D),Z:String(r.Z),deficit:String(r.deficit)});
      }
      graphs++;
    }
  }
  return {graphs,cases,roundingChecks,sharedPrefixCases,fullPrefixes,examples,mismatches:0};
}
console.log(JSON.stringify(verify(),null,2));
```

## 5. Next scientific question

The exact Boolean hardness gap left by R799 is closed. Investigate approximation and sampler quality on unpadded or short-connector overlap graphs: can the ambiguity factors be retained while exploiting ferromagnetic partition algorithms, and which mixed-sign overlap geometries admit comparable relative-error certificates? The compact nonnegative shared-slot expression and the explicit ambiguity deficit are the verified frontier. Keep all native signed, source, event-order and common-depth observers separate. This is an author proof, not accepted formal Result.
