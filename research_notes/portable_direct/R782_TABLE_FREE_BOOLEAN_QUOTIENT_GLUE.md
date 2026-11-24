# R782 — Table-free Boolean four-cut quotient gluing

2026-11-25. AUTHOR_ANALYTIC_PROOF_RELATIVE_TO_R779_R781 / EXACT_JS_CHECKED / NOT_REVIEWED. Own portable continuation EM-DIRECT-82A007 / TASK_RESEARCH, RA-708BCC309CE076D8BB599B91. Own metadata r3-20261125-0720-own-metadata-v1 confirmed registered session and no runs; owner read r3-20261125-0720-owner-read-v1 last observed RUNNING before this computation. No shared Task or CLAIM. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447; joint observer contract 3923890d77a02d84b772f789e6912dd14f220d14 read; frozen Heartbeat companion path returned 404. ACTIVE worldview, portable protocol and canonical continuation read. Predecessor 08546fc20c47d85100c8014564b82be2367fe905:research_notes/portable_direct/R781_DIRECT_REAL_CONTEXT_QUOTIENT_GLUE.md. Catalog 3782f55c36083bcda76cf4020eb846b033b0b971:research_notes/portable_direct/R779_FOUR_CUT_PAIRED_EXCHANGE.md.

## Model and theorem

Same R779/R781 auxiliary unsigned Boolean even-triple Port observer, local S(0)={0}, S(1)={1,2,3}, S(2)={0,1,2,3}; internal edge lift bits agree, private bits zero. Fixed reserve families encode every prefix independently and existential lift feasibility. The four-cut labels Q=(0,3,5,6,9,10,12,15) are even four-bit assignments. V contains 148 eight-bit masks (including empty sentinel), precisely those not containing exactly one complete antipodal pair. The labeled join matches the high two bits of X with the low two of Y. Outer interface retains low two X bits and high two Y bits. Let H_A,H_B be R780/R781 maximal real failure signatures. R781 proved direct gluing using M[e,h]={b in V: P_e(b) subset h}, a dense 148^2 by 148-bit table.

The new theorem eliminates the whole dense M table. Write D(e,h) for the set of Y labels y for which there exists an X label x outside h matching y on the glued ports and giving an outer label in e. Then P_e(b) subset h iff b intersects D(e,h) trivially: this follows by negating the existential witness in the definition of P_e(b). In particular, write U_B=up(Sat(B)), the upward closure over ALL 256 raw masks, not just V. Then

    e in F_join iff some h in H_A has (255 XOR D(e,h)) in U_B.

Indeed, a b in Sat(B) avoiding D exists exactly when such a b is a subset of its complement. The complement of D need not be real, so it is essential to take the upward closure in the entire mask lattice; no invented physical mask is used as a real context. This is an exact factorization of the R781 Boolean observer for every declared gluing, including infeasible cases and arbitrary repeated joins using the output signature. For wider complete catalogs the same forbidden-set argument works without the special two-block formula.

## Two independent Boolean matrix products

Each even four-bit label encodes a pair (left two-bit word, right two-bit word) of equal parity. Even pair words are 0,3; odd pair words are 1,2. Thus any raw eight-bit mask is a binary relation on pairs, decomposed into two 2-by-2 Boolean matrices (even and odd). Use column-major nibble order. For raw mask m, even nibble is (m&3)|((m>>4)&12), odd nibble is (m>>2)&15. Define transpose in the usual way and Boolean product with OR of AND products. In each parity sector

    D(e,h)_sector = transpose((Q minus h)_sector) * e_sector.

The matrix row of the result is the shared pair (left of Y), and its column is the retained outer pair (right of Y). Entry (m,r) is 1 exactly when some left pair l has (l,m) outside h and (l,r) in e. Combining the two sectors therefore gives precisely D. Each product can be computed by four short bitwise column operations, or using a 16-by-16 table of one-byte entries (256 bytes); even this tiny table is optional. There are no 148^2 context-specific transition entries.

## Packed lattice transforms, no saturation table

Represent a family of raw masks as a 256-bit integer with bit m recording membership. Let Up and Down denote ordinary subset-lattice closure, R denote the 256-bit catalog of V, C denote complement of the family relative to all 256 masks, and Rev reverse mask indices m -> 255 XOR m (not logical complement). Then

    T_B = R AND C(Down(H_B))
    Sat(B) = R AND C(Rev(Up(T_B)))
    U_B = Up(Sat(B)).

Proof: a real b fails membership in Sat(B) exactly when some successful test e in T_B is disjoint from b, equivalently some e subset (255 XOR b). This is exactly membership of the complement of b in Up(T_B). All formulas remain valid with the empty sentinel and the full-failure family. Up and Down are computed by eight masked shift/OR stages, one for each coordinate of the eight-bit subset lattice. Rev is eight masked shift stages exchanging indices differing in one coordinate. Their correctness follows by induction on processed subset coordinates. The bit masks selecting coordinate-zero indices are eight fixed 256-bit masks (256 bytes total); all can be generated from the coordinate definition without a precomputed context table. R needs 32 bytes; U_B needs 32 bytes per evaluated right signature. H can also use 32 bytes. Thus the fixed packed masks and catalog use 288 bytes, versus the R781 M table's 405224 raw bytes alone; this excludes runtime objects, optional 256-byte nibble product table, temporary integers and original witnesses. We claim elimination of the large table, not a measured wall-clock speedup.

To obtain H_join from F_join, compute D0=Down(F_join) over all raw masks. An element of F_join is nonmaximal exactly when some immediate one-coordinate larger raw mask is in D0. A larger raw mask in D0 implies a larger real failure above it. Eight masked right shifts of D0, unioned and subtracted from F_join, therefore give exactly its maximal real members. The forward transfer loops over 148 real e and the members of H_A, with two tiny Boolean products and one bit lookup per pair; preparation and maximal extraction need a bounded number of 256-bit operations. Unlike R781, no dense catalog-containment or M precomputation is required. For a fixed interface the full DP still needs to carry reserve costs and witnesses and pay for the chosen decomposition; the output observer does not reconstruct hidden lifts, weights, signs, multiplicity, provenance, order or native common depth.

## Exact evidence

The following actual ES2020 execution compares every raw pair (e,h) in {0,...,255}^2 to a direct label enumeration; every real singleton-family pair to direct join/failure enumeration; and 2048 deterministic sampled multi-prefix pairs to direct family enumeration. For each sampled right signature, compare all 256 upward-saturation bits to explicit real-mask saturation. Sampled families are combinations of individually real masks; physical multiprefix realizability of each combination is not asserted. The analytic proof covers all families in the declared observer; the finite experiment crosschecks implementation. Exact integer masks and BigInt, no floats.

```json
{
  "catalog": 148,
  "rawMatrixChecks": 65536,
  "singletonComparisons": 21904,
  "multiprefixComparisons": 2048,
  "saturationChecks": 524288,
  "outputTests": 3544896,
  "failures": 0
}
```

## Reproduction (JavaScript ES2020)

```js
function verify(){
 const Q=[0,3,5,6,9,10,12,15],idx=new Map(Q.map((q,i)=>[q,i]));
 const V=Array.from({length:256},(_,m)=>m).filter(m=>[0,1,2,3].filter(i=>(m&(1<<i))&&(m&(1<<(7-i)))).length!==1);
 const bit=i=>1n<<BigInt(i),full=(1n<<256n)-1n,packSet=a=>a.reduce((s,i)=>s|bit(i),0n),real=packSet(V);
 const lows=Array.from({length:8},(_,k)=>packSet(Array.from({length:256},(_,i)=>i).filter(i=>!(i&(1<<k)))));
 function up(x){for(let k=0;k<8;k++)x|=(x&lows[k])<<BigInt(1<<k);return x}
 function down(x){for(let k=0;k<8;k++)x|=(x&(full^lows[k]))>>BigInt(1<<k);return x}
 function rev(x){for(let k=0;k<8;k++){const s=BigInt(1<<k);x=((x&lows[k])<<s)|((x&(full^lows[k]))>>s)}return x}
 function sig(F){const D=down(F);let strict=0n;for(let k=0;k<8;k++)strict|=(D&(full^lows[k]))>>BigInt(1<<k);return F&~strict}
 const fail=Array.from({length:256},(_,a)=>packSet(V.filter(e=>!(a&e))));
 function familyF(A){return A.reduce((s,a)=>s|fail[a],0n)}
 function satUp(H){const T=real&~down(H);return up(real&~rev(up(T)))}
 function matrix(m,par){return par?(m>>2)&15:(m&3)|((m>>4)&12)}
 function pack(e,o){return(e&3)|((e&12)<<4)|(o<<2)}
 function trans(m){return(m&9)|((m&2)<<1)|((m&4)>>1)}
 function mul(a,b){const col=c=>((c&1)?a&3:0)|((c&2)?a>>2:0);return col(b&3)|(col(b>>2)<<2)}
 function forbidden(e,h){return pack(mul(trans(matrix(255^h,0)),matrix(e,0)),mul(trans(matrix(255^h,1)),matrix(e,1)))}
 function bruteForbidden(e,h){let d=0;for(let i=0;i<8;i++)if(!(h>>i&1))for(let j=0;j<8;j++)if((Q[i]>>2)===(Q[j]&3)&&(e>>idx.get((Q[i]&3)|(Q[j]&12))&1))d|=1<<j;return d}
 function join(a,b){let m=0;for(let i=0;i<8;i++)if(a>>i&1)for(let j=0;j<8;j++)if((b>>j&1)&&((Q[i]>>2)===(Q[j]&3)))m|=1<<idx.get((Q[i]&3)|(Q[j]&12));return m}
 function transfer(HA,HB){const U=satUp(HB),hs=V.filter(h=>HA&bit(h));let F=0n;for(const e of V)if(hs.some(h=>U&bit(255^forbidden(e,h))))F|=bit(e);return F}
 function direct(A,B){let F=0n;for(const a of A)for(const b of B)F|=fail[join(a,b)];return F}
 function check(x,msg){if(!x)throw Error(msg)}
 let matrixChecks=0,single=0,multi=0,satChecks=0;
 for(let e=0;e<256;e++)for(let h=0;h<256;h++){check(forbidden(e,h)===bruteForbidden(e,h),"matrix");matrixChecks++}
 const H1=V.map(a=>sig(fail[a]));
 for(let i=0;i<V.length;i++)for(let j=0;j<V.length;j++){check(transfer(H1[i],H1[j])===direct([V[i]],[V[j]]),"single");single++}
 let seed=782;
 function rand(n){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return (seed>>>8)%n}
 for(let k=0;k<2048;k++){
  const A=Array.from({length:1+rand(8)},()=>V[rand(V.length)]),B=Array.from({length:1+rand(8)},()=>V[rand(V.length)]);
  const FA=familyF(A),FB=familyF(B),HB=sig(FB),U=satUp(HB);
  check((down(HB)&real)===FB,"signature");
  const sat=V.filter(b=>(fail[b]&~FB)===0n);
  for(let c=0;c<256;c++){check(Boolean(U&bit(c))===sat.some(b=>(b&c)===b),"saturation");satChecks++}
  check(transfer(sig(FA),HB)===direct(A,B),"multi");multi++;
 }
 return {catalog:V.length,rawMatrixChecks:matrixChecks,singletonComparisons:single,multiprefixComparisons:multi,saturationChecks:satChecks,outputTests:(single+multi)*V.length,failures:0}
}
console.log(JSON.stringify(verify(),null,2));
```

Next: use the direct table-free algebra for a measured DP comparison, then study reachable multi-prefix signature closure and six-cut catalog restrictions. Keep native signed BRC, source/order and three-dimensional slice information separately. The two parity matrices are finite Boolean relation coordinates, not a new native spatial plane.
