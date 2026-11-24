# R781 — Direct real-context quotient gluing via polarity and pullback

2026-11-25. AUTHOR_ANALYTIC_PROOF_RELATIVE_TO_R779 / EXACT_JS_CHECKED / NOT_REVIEWED. Own portable continuation EM-DIRECT-82A007 / TASK_RESEARCH, RA-708BCC309CE076D8BB599B91; no shared Task claim. Own recovery r3-20261125-0620-own-metadata-v1 confirms no RUN; owner inventory r3-20261125-0620-owner-read-v1 last observed RUNNING. Predecessor a91ae025bd09fc99a03467582f2ca04235d9bfb9:research_notes/portable_direct/R780_REAL_CONTEXT_QUOTIENT_AND_WITNESSES.md; catalog theorem 3782f55c36083bcda76cf4020eb846b033b0b971:research_notes/portable_direct/R779_FOUR_CUT_PAIRED_EXCHANGE.md. Frozen scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389, P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447, joint observer contract 3923890d77a02d84b772f789e6912dd14f220d14 actually read; ACTIVE worldview and current continuation and portable rules read. Frozen Heartbeat and residual companion paths returned 404; no native dynamics claimed.

## 1. Model and exact theorem

Reuse R777–R780 auxiliary unsigned Boolean feasibility model. At every loop-free subcubic Port vertex the lift is an even triple, matched on internal edges, zero on private ports. Independent prefix x_i in S(p_i), target w_i, reserve t_i give admissibility x_i XOR w_i XOR z_i in S(t_i), with S(0)={0}, S(1)={1,2,3}, S(2)={0,1,2,3}. For a fixed reserve, family A comprises extendible boundary masks for every actual interior prefix. All families are nonempty; an infeasible prefix may have the empty mask. The quantifier is for every prefix there exists a lift. We now include empty mask 0 in the test catalog as an always-failing sentinel; a signature H includes 0 if it has no nonempty maximal failure. The signature (Q) denotes an infeasible reserve; R780's feasible H=() becomes (0).

For any labeled interface, let V be the complete catalog of individually realizable fixed-prefix boundary sets (plus 0), and F_A={e in V: some a in A has a intersect e empty}. H_A=Max F_A. We need only V closed under the specific graph gluings and pullbacks below, with its nonempty members having fixed-prefix realizations, not arbitrary abstract sets.

Define the polar of a family U subset V by U^perp={b in V: every u in U intersects b}. The successful test set is T_A=V minus F_A=A^perp. The saturated family Sat(A)=T_A^perp. It contains A, has exactly the same successful tests as A, and is the largest family of individual real masks with those tests: for any b in Sat(A), all successful e meet b; any failed e still misses an original a. These statements also hold for infeasible reserves and the empty-mask sentinel. No assertion is made that Sat(A) is itself the multiprefix family of a graph.

Let two disjoint regions X,Y be glued along specified matching boundary ports, retaining an outer interface Z. J(a,b) denotes the set of outer assignments extendible through a and b. For e in V_Z and b in V_Y define pullback P_e(b)={x in Q_X: some y in b matches x on glued ports and their remaining bits belong to e}. The pullback is in V_X (or 0): glue a fixed-prefix realizing gadget for b to one for e along the Y outer ports, leaving the X ports dangling; equality of bits implements exactly the pullback. Where necessary include separate equality wires for untouched X outer ports. Such wires are degree-two even vertices with third private port and saturated reserve. Gluing preserves the graph class, parallel edges allowed; gadgets are disjoint copies. Fixed-prefix targets absorb fixed prefix as in R779. Likewise the reverse pullback belongs to V_Y and J(a,b) belongs to V_Z. This proves closure for complete catalogs at arbitrary widths; it does not assume those catalogs are known at all widths.

For a fixed outer test e, the raw glued observer succeeds iff for every a in A and b in B, J(a,b) intersects e. This is equivalent to for every b in B, P_e(b) in T_A. Replacing A by Sat(A) preserves this predicate because all P_e(b) are real; then replacing B by Sat(B) preserves it by the symmetric pullback argument for every individually real a in Sat(A). Hence
  T_join(e)=1 iff for every b in Sat(B), P_e(b) in T_A.
The quotient therefore has a direct binary composition, including infeasible cases, without reconstructing an antichain representative. It also respects arbitrary repeated valid gluing: induction on the expression tree applies the same identity, preserving the universal-prefix/existential-lift order. This is an explicit descent certificate for the stated observer only.

## 2. Direct H-coordinate implementation

For each test h and outer e precompute M[e,h]={b in V_Y: P_e(b) subset h}. Let Down(H) be the union of principal downsets within V. For b in V_Y put D_b={d in V_Y: d intersect b empty}. Then
  Sat(B)={b: D_b subset Down(H_B)},
  e fails join iff some h in H_A satisfies M[e,h] intersect Sat(B) nonempty.
Take inclusion maxima of the failed e to obtain H_join. This is a direct calculation from the two signatures, their static boundary catalogs, and the labeled gluing table. No original multiprefix family or hidden lift is needed. R779's four-cut catalog has 147 nonempty masks and 0, so each D_b, M[e,h] and Sat(B) is representable by 148 bits. In the connected-four-cut 2-edge join studied below, there are 148^2=21904 M entries, each at most 148 bits (raw packed payload 3,241,792 bits = 405224 bytes, excluding indexing and representation overhead). Construction enumerates at most 64 boundary label pairs for each join/pullback; M construction checks 148^3 mask containments. Per transition, saturation tests 148 subset comparisons of bitsets, then at most 148*|H_A| intersections; maximal extraction uses at most 148^2 inclusion tests (or a precomputed inclusion table). General width preprocessing/catalog discovery and witness recovery are separate costs. This is a bounded-width exact algorithm, not a measured speedup over R777 or a claim of optimal memory.

## 3. Exact computation and scope

Q=(0,3,5,6,9,10,12,15), masks indexed in this order. V is every eight-bit mask whose number of full antipodal pairs is not exactly one, including zero. For each two-region join, match high two bits of X with low two of Y; keep low two of X and high two of Y. Exhaust every 148^2 fixed-mask pair, every 148^2 outer-test/neighbor pair for catalog closure, and all singleton-family compositions against direct enumeration. Check 2048 deterministic pseudo-random pairs of families of 1..8 real masks; these families are abstract combinations of individually realizable masks, not claimed all physically reachable as multiprefix families. Check the two genuine R780 collision families in both positions against each sampled B. JS BigInt exact bitsets and integer labels. All assertions passed. Actual output:
{
  "catalog": 148,
  "joinClosure": 21904,
  "pullbackClosure": 21904,
  "singletonComparisons": 21904,
  "multiprefixComparisons": 2048,
  "collisionComparisons": 4096,
  "outputTestComparisons": 4151104,
  "tableEntries": 21904,
  "tableBitWidth": 148,
  "failures": 0
}

This resolves the direct-composition question of R780 at four-cut interfaces with this explicit gluing; the analytic law applies at other interfaces if their complete catalogs are available. Signed BRC, multiplicities, weights inside lifts, order, provenance and native slice common depth remain separate. Reserve costs can be carried as additive DP costs with selected original reserve witnesses; the quotient itself does not reconstruct hidden lifts. Next: derive smaller transition tables exploiting boundary permutations and antipodal structure, characterize reachable signature closure under four-cut joins, and extend real test catalogs to six-cut. Do not assert universal six-cut sufficiency from the R779 necessary pairing property alone.

## Reproduction (JavaScript ES2020)

```js
function verify(){
 const Q=[0,3,5,6,9,10,12,15], idx=new Map(Q.map((q,i)=>[q,i]));
 const V=Array.from({length:256},(_,m)=>m).filter(m=>[0,1,2,3].filter(i=>(m&(1<<i))&&(m&(1<<(7-i)))).length!==1);
 const n=V.length, vi=new Map(V.map((m,i)=>[m,i])), bit=i=>1n<<BigInt(i), full=(1n<<BigInt(n))-1n;
 const fail=V.map(a=>V.reduce((s,e,i)=>s|((a&e)?0n:bit(i)),0n));
 const down=V.map(h=>V.reduce((s,e,i)=>s|((e&h)===e?bit(i):0n),0n));
 const masks=x=>V.filter((_,i)=>x&bit(i));
 const sig=F=>masks(F).filter(h=>!V.some((k,j)=>k!==h&&(h&k)===h&&(F&bit(j))));
 const fromH=H=>H.reduce((s,h)=>s|down[vi.get(h)],0n);
 const familyF=A=>A.reduce((s,a)=>s|fail[vi.get(a)],0n);
 const sat=F=>V.reduce((s,b,i)=>s|((fail[i]&~F)===0n?bit(i):0n),0n);
 function join(a,b){
  let m=0;
  for(let i=0;i<8;i++)if(a>>i&1)
   for(let j=0;j<8;j++)if((b>>j&1)&&((Q[i]>>2)===(Q[j]&3)))
    m|=1<<idx.get((Q[i]&3)|(Q[j]&12));
  return m;
 }
 function pull(e,b){
  let m=0;
  for(let i=0;i<8;i++)for(let j=0;j<8;j++)if((b>>j&1)&&((Q[i]>>2)===(Q[j]&3))&&(e>>idx.get((Q[i]&3)|(Q[j]&12))&1)){m|=1<<i;break;}
  return m;
 }
 const J=V.map(a=>V.map(b=>vi.get(join(a,b))));
 const P=V.map(e=>V.map(b=>vi.get(pull(e,b))));
 const assert=(x,msg)=>{if(!x)throw Error(msg)};
 assert(n===148,"catalog");
 for(let i=0;i<n;i++)for(let j=0;j<n;j++)assert(J[i][j]!==undefined&&P[i][j]!==undefined,"closure");
 const M=P.map(row=>V.map(h=>row.reduce((s,k,j)=>s|((V[k]&h)===V[k]?bit(j):0n),0n)));
 function transfer(HA,HB){
  const B=sat(fromH(HB));
  const hs=HA.map(h=>vi.get(h));
  let F=0n;
  for(let e=0;e<n;e++)if(hs.some(h=>(M[e][h]&B)!==0n))F|=bit(e);
  return F;
 }
 function direct(A,B){let F=0n;for(const a of A)for(const b of B)F|=fail[J[vi.get(a)][vi.get(b)]];return F;}
 const H1=V.map(a=>sig(familyF([a])));
 let singles=0, multi=0, collisions=0;
 for(let i=0;i<n;i++)for(let j=0;j<n;j++){assert(transfer(H1[i],H1[j])===fail[J[i][j]],"singleton");singles++}
 let seed=781;
 function rand(n){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%n;}
 const examples=[[62,142,188],[63,142,252]];
 assert(familyF(examples[0])===familyF(examples[1]),"R780 collision");
 for(let k=0;k<2048;k++){
  const A=Array.from({length:1+rand(8)},()=>V[rand(n)]);
  const B=Array.from({length:1+rand(8)},()=>V[rand(n)]);
  const FA=familyF(A), FB=familyF(B);
  assert(fromH(sig(FA))===FA&&fromH(sig(FB))===FB,"signature");
  assert(transfer(sig(FA),sig(FB))===direct(A,B),"multiprefix");
  multi++;
  assert(direct(examples[0],B)===direct(examples[1],B),"collision left");
  assert(direct(B,examples[0])===direct(B,examples[1]),"collision right");
  collisions+=2;
 }
 return {catalog:n,joinClosure:n*n,pullbackClosure:n*n,singletonComparisons:singles,multiprefixComparisons:multi,collisionComparisons:collisions,outputTestComparisons:(singles+multi+collisions)*n,tableEntries:n*n,tableBitWidth:n,failures:0};
}
console.log(JSON.stringify(verify(),null,2));
```
