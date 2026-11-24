# R762KW — Structural classification of the eleven-event reserve

2026-11-24. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable continuation of R762KV, 88954b5da3cb001d937f873698a6894ac21d6a15:research_notes/portable_direct/R762KV_SHARP_SINGLETON_SUFFIX_RESERVE.md (blob fb5deac046000d7187e362fd32e0209a1b78d383). Frozen P000 a72226e2430ffa4786321ac86e7f0c599d5f0389 and joint-relation companion read. Original registration r3-20261124-0124-own-research-registration-v1 confirmed SUCCEEDED, EM-DIRECT-82A007, RA-708BCC309CE076D8BB599B91; recovery r3-20261124-0820-recovery-read-v1 returned no runs and execution_authorized=false. Current inventory r3-20261124-0820-owner-read-v1 queued at research start. No shared task adopted or protected writes attempted.

## KW.1 — Cycle-coordinate avoidance theorem

In KV's unsigned auxiliary branch model, identify the twelve Ports with edges of Q3 (the support cube): A_ij is the k-edge, B_ik the j-edge, C_jk the i-edge. At an occupied vertex v a local XOR contribution is an even triple of half-edge bits. A singleton allows the three nonzero triples; a double allows all four triples. At an empty vertex all bits vanish. Let G be the induced subgraph on occupied vertices A. A global boundary b is the XOR of the two half-edge bits on each cube edge.

For unconstrained occupied triples (temporarily allow zero at singletons), the image is the full even-total boundary space E iff A is a connected vertex cover, by KU.2 (union of local triangles connected on all twelve Ports). Equivalently, no cube edge has both endpoints empty and G is connected. For a given b in E, choose any solution x0. Differences of solutions vanish on edges touching empty vertices; on internal edges both half-edge differences agree. Even local parity means their nonzero edges form an element z of the binary cycle space Z(G). Conversely every such z yields a solution x0+z. Let p_v be restriction of z to the three edges incident at v, with missing edges zero. At each singleton v the only forbidden condition is p_v(z)=x0_v. Since the unconstrained x0 can independently take any even triple at each occupied vertex (producing some b in E), universal raw E-saturation is equivalent to:
for every assignment of even triples q_v at singletons, there exists z in Z(G) with p_v(z) != q_v for all singleton v.
Thus unsaturation is precisely existence of a cover of Z(G) by one affine forbidden fiber per singleton. This is a structural criterion for any clipped inventory; no counts or native source histories are discarded. At total 11 at least one double exists. Any monochromatic realization can be made mixed by changing the two identical colors at a double to two of another color, preserving XOR; nine other events remain. Hence raw and mixed E-saturation agree for the following classification.

## KW.2 — All 384 optimal clipped stocks, analytic classification

KV established the sharp minimum 11 by exact exhaustive proof (including equivalence to F-saturation); we replace its classification of the 11-event winners by a structural proof, without requiring its 6561-stock census to count them. At total 11 the occupied count a can only be 6,7,8; singleton count is 2a-11.

Case a=6: two empty vertices must be nonadjacent. If opposite (distance 3), G is a six-cycle; if distance 2, G is a four-cycle with two pendant leaves (check by deleting 000 and 110). In both cases cycle rank is one, so the unique singleton must lie on the cycle: there are two distinct local values iff it does, otherwise q=0 forbids every cycle. Count = 4 opposite pairs * 6 + 12 distance-two pairs * 4 = 72.

Case a=7: by cube symmetry delete 000. The three distance-one neighbors have degree two; suppress them to obtain K4, with outer vertices at distance two and center at distance three. The three edges of the outer triangle are subdivided by the three degree-two vertices. Choose their bits a,b,c independently; the three center-edge bits are fixed as pairwise XORs by even parity. Cycle space has dimension 3. A degree-two vertex's projection has rank one, its bit is one of a,b,c; each outer vertex projection has rank two, spanned by its two incident outer-edge bits; the center projection has rank two with row space spanned by a+b,a+c. Forbidden fibers have size at most 4 (rank one) or 2 (rank two) out of 8.

With three singleton vertices:
* Three rank-two constraints cannot cover 8 (at most 6).
* Three rank-one constraints cannot cover: independent coordinates can all avoid their respective forbidden bits.
* Two rank-one and one rank-two: avoiding the first two fixes two independent bits and leaves a two-point line along the third. The last constraint can cover that line iff its projection is insensitive to the free bit. This happens exactly at the outer vertex incident with both selected subdivided outer edges, i.e. the common distance-two corner of the two selected neighbors of the empty vertex. Outside-image forbidden values only weaken constraints.
* One rank-one and two rank-two: after the rank-one constraint there are four candidates. A rank-two forbidden fiber could cover two of them only if its defining row space contains the selected rank-one linear form. Both must contain it for a cover. Only the two outer endpoints of the corresponding subdivided edge have this property. On the remaining four-point square, their constraints each specify a different independent bit, hence the two forbidden pairs intersect and cover at most three points. No cover.

So exactly three of the 35 singleton triples fail per missing vertex, each consists of two neighbors of the missing vertex and their common other neighbor. Count = 8*(35-3)=256.

Case a=8: five singleton vertices, any choice succeeds. The full cube's cycle space is generated by the six square face boundaries with the one relation that their sum is zero (dimension 5: independence modulo constants follows from connected face adjacency). Assign binary face bits X_i,Y_j,Z_k (opposite faces indexed 0,1). At vertex (i,j,k), the local edge bits are X_i+Y_j, X_i+Z_k, Y_j+Z_k. Each forbidden even triple is equivalent to two complementary forbidden assignments of these three face bits. After assigning X,Y, a clause either places no restriction on Z_k or requires exactly one of its values; the trigger has form X_i+Y_j=constant, and the forced value of Z_k is X_i+constant.

There is an axis splitting the five singleton vertices as 2 and 3: otherwise every axis splits 1 and 4, so their sum of Hamming distances to the majority corner would be 3, whereas the five distinct cube vertices have total distance at least 0+1+1+1+2=5. Rename this axis k. Choose the four X,Y bits independently uniformly. Within one k-slice, a pair of clauses conflicts only if both triggers hold and they force opposite Z_k. The two distinct trigger equations are independent, so conflict probability <=1/4. For a diagonal pair (different i AND j), the opposition equation X_i+X_i'=constant is independent of both triggers, so the probability is exactly 1/8. The slice with three clauses necessarily contains a diagonal pair. Across the two slices there are four pairs total, at least one diagonal. By the union bound probability of any conflict <=3/4+1/8=7/8. Some face assignment has no conflict, and each Z bit can then be chosen consistently. This proves every singleton constraint can be avoided for every q. Count = choose(8,5)=56.

Total = 72+256+56=384. This proof classifies all 504 clipped stocks of total 11 (including invalid active sets). It proves the winners without enumerating 4096 boundaries or all ternary stocks. Sharp global minimum 11 and equivalence to F-saturation still use KV's finite proof. No claim about native signed dynamics.

## KW.3 — Exact executed independent cycle-coordinate verification

The following JS program enumerates binary cycle elements and forbidden local assignments (not the KV boundary DP); it tests each of the 504 stock patterns against the structural criterion. The recursion stops at the first full forbidden cover if one exists, so the number of leaf checks is not a count of all possible forbidden assignments.

```javascript
const edges=[];for(let v=0;v<8;v++)for(let d=0;d<3;d++){let w=v^(1<<d);if(v<w)edges.push([v,w,d])}
const count=x=>{let n=0;while(x){x&=x-1;n++}return n};
const cycles=A=>{const es=edges.filter(([v,w])=>(A>>v&1)&&(A>>w&1));let out=[];for(let k=0;k<1<<es.length;k++){let p=0,l=Array(8).fill(0);for(let i=0;i<es.length;i++)if(k>>i&1){let [v,w,d]=es[i];p^=(1<<v)|(1<<w);l[v]^=1<<d;l[w]^=1<<d}if(!p)out.push(l)}return out};
const values=[0,3,5,6];let stats={},checks=0,failures=0;
for(let A=0;A<256;A++){let a=count(A),s=2*a-11;if(s<0||s>a)continue;let C=cycles(A);let cov=edges.every(([v,w])=>(A>>v&1)||(A>>w&1));let connected=cov&&C.length===(1<<(edges.filter(([v,w])=>(A>>v&1)&&(A>>w&1)).length-a+1));for(let S=A;;S=(S-1)&A){if(count(S)==s){let vs=Array.from({length:8},(_,i)=>i).filter(i=>S>>i&1);let actual=false;if(connected){let f=vs.map(v=>values.map(q=>C.reduce((b,c,i)=>c[v]===q?b|(1n<<BigInt(i)):b,0n)));let all=(1n<<BigInt(C.length))-1n;function cover(i,b){if(i===f.length){checks++;return b===all}return f[i].some(x=>cover(i+1,b|x))}actual=!cover(0,0n)}
let missing=Array.from({length:8},(_,i)=>i).filter(i=>!(A>>i&1));let pred=connected;if(pred&&a===6)pred=C.some(c=>c[vs[0]]!==0);if(pred&&a===7){let o=missing[0],ns=vs.filter(v=>count(v^o)===1);pred=!(ns.length===2&&vs.some(v=>v===(o^(ns[0]^o)^(ns[1]^o))))}if(actual!==pred)failures++;let key=`${8-a},${s},${a-s}`;stats[key]??=[0,0];stats[key][0]++;stats[key][1]+=Number(actual)}if(!S)break}}
console.log({stats,checks,failures})
```

Observed: {"stats":{"2,1,5":[168,72],"1,3,4":[280,256],"0,5,3":[56,56]},"checks":74200,"failures":0}.

## Next

Find analytic certificates for the sharp impossibility at ten events (especially the full cube with six singletons, i.e. signed NAE cover obstruction) and the F-only target restriction. Then classify reserves for prescribed prefix support rather than all E. KW's cycle-coordinate avoidance is a scoped auxiliary observer representation; retain native signs, time and common depth until an actual typed BRC mapping and preservation proof exist.
