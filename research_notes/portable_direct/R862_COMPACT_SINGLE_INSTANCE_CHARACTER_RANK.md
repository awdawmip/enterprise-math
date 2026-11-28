# R862 candidate — Compact single-instance sharp character-rank obstruction
2026-11-28. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.
Continuation: R861 at 1b0bb2f48e30f6e3464744ef7aa73ea5b4abc47b:research_notes/portable_direct/R861_COUNTEREXAMPLE_GUIDED_CHARACTER_RANK.md, section 3 and its remaining compact single-instance question. Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 and definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json read; generated foundation startup 404, no repin. Global canonical 5bf095933826006b57095f00d53358158d735446, P000 V4 projection matched canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview. Current control snapshot fdadd70ce8ace1c26a1e578b553e1a85ceea9346. Own EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91 session metadata recovery succeeded, execution_authorized=false; fresh owner query r3-20261128-r862-running-read admitted, last seen RUNNING / SOURCE_MATERIALIZATION at 1795850330 UTC epoch seconds. No shared claim, Result or review. This is an auxiliary nonnegative integer independent-option capacity model, not a native BRC/Port implementation; all original choices retained.

## 1. Sharp lower bound in a single compact instance, for every prime p
Fix prime p and integer d>=1. Set c=1 for p=2, c=(p-1)/2 for odd p. There are r=2d+1 resource coordinates, d independent groups. Group j chooses a_j in {-c,...,c}; its contribution on coordinate pair (j,d+j) is (c+a_j,c-a_j); on final coordinate it contributes 1[a_j=0]; on other coordinates zero. All contributions are nonnegative integers. Thus a word a has F(a)=(c1+a,c1-a,Z(a)), Z(a)=#zeros. Budget h=(c1,c1,d-1). There are d(2c+1) explicit options, at most 3d for p=2 and pd for odd p, and O(pd^2) dense scalar entries. The input bit length is polynomial in d for every fixed p. No word is feasible: both pair caps force a_j=0 for all j, yielding Z=d.

For a linear character A over F_p, define the precise relaxation R(A) as the union over reachable characters v of conv{F(a): AF(a)=v mod p} intersected with the box 0<=y<=h, with y integer and Ay=v mod p. This is the relaxation using all real linear support directions in each character class and the class congruence. No restriction to a finite direction library is needed.

Let V={(x,-x,0): x in F_p^d}. If rank(A|V)<d, take nonzero kernel x. Represent x by a in [-c,c]^d (for binary choose 0 or 1). Both a and -a are legal words. Set y=(c1,c1,Z(a)). Then F(a)+F(-a)=2y over the integers, both F words have character Ay because their differences from y are +/- (x,-x,0) modulo p, and 0<=y<=h since x nonzero. Hence y belongs to R(A), although the true feasible set is empty. This holds for every A of rank <d and even for higher rank A whose restriction is noninjective. The additional zero-count coordinate is the new ingredient: it enforces nonzero deviation for the midpoint without encoding all nonzero words in a single exponential list or using d different instances.

Conversely take A reading the first d coordinates modulo p. Every convex combination of words has pair sums exactly 2c. A point inside the box therefore has both coordinates of each pair equal to c. Its class must have first d residues c. Any word of that class has a_j=0: no other element of [-c,c] is congruent to zero mod p (binary endpoints +/-1 are congruent to each other, not zero). Thus all words in that class have Z=d; their convex hull cannot meet the last budget d-1. Consequently R(A) is empty and the minimum rank required by the exact conditional-hull relaxation is exactly d. This is a single independent-option network with polynomial explicit size, closing the stated compact-instance gap of R861 within this auxiliary model.

## 2. Sparse as well as dense table obstruction
Every successful A is injective on V. For each x in F_p^d choose one representative a as above. Partition these p^d choices by Z(a) modulo p. One part has >=p^(d-1) elements. Within that part, distinct x,x' give distinct characters: their final-coordinate difference is 0 mod p and the paired difference is a nonzero vector of V. Therefore even an exact sparse table of reachable classes for any successful A has >=p^(d-1) entries. The coordinate-reading successful A has exactly p^d reachable classes (including binary duplicate +/-1), giving the factor-p sandwich. Dense tables require at least p^d entries. This counts explicit classes only; it is not a lower bound for arbitrary compressed representations or all algorithms. For fixed p, input size is O(d^2 log p) dense, or O(d p log(d p)) with indexed nonzero entries.

## 3. A cheap alternative and the scope of the obstruction
For this same instance the direct local budget filtering is linear in the explicit options (nonnegative later contributions cannot undo a violation). Each option with a_j nonzero already violates one paired capacity. Only a_j=0 remains, so the last capacity d is forced and exceeds d-1. Hence preprocessing can solve this instance without building a global residue table. The rank lower bound is specifically for the unfiltered full original-word conditional-hull representation, not a hardness result for feasibility itself. This distinction gives a concrete design principle: do not increase the rank of a global observation if a local, provenance-preserving budget restriction can eliminate the same defect. No independent arithmetic BRC execution or native correspondence is claimed. Keep pair identities and zero-count relations in the witness; the two-coordinate pairs are auxiliary resource coordinates, not native spatial planes.

## 4. Cost, evidence, next
Full explicit option lists O(dp) and dense storage O(d^2 p) integers; no hidden enumeration in the construction. The general lower bound is an analytic rank-nullity and midpoint proof for all primes and d. Exact bounded author check below exhausts ambient matrices with d-1 rows for listed small sizes (lower row counts can be zero padded), restricted matrices for additional sizes, all words for p in {2,3,5,7}, d=1..5, and all extra-marker columns of coordinate-reading maps for d<=3. All integer operations are within JS safe integer range. Counts are executed results; no independent review or formal admission. Next: derive a certified suffix-local feature switch on affine reachable difference subspaces, and combine budget-filtering provenance with suffix-dependent support tables; separate the cost of repeated table construction from rank savings. Retain raw choices for any horizon outside the declared budget.

## Exact reproducible check
```javascript
function verify(){
 const out={ambient_maps:0,restricted_maps:0,midpoint_checks:0,words:0,instances:0,sparse_bound_checks:0};
 function ck(x){if(!x)throw Error("assertion");}
 function digits(v,p,n){return Array.from({length:n},()=>{let a=v%p;v=Math.floor(v/p);return a;});}
 function mod(x,p){return ((x%p)+p)%p;}
 function dot(a,b,p){return mod(a.reduce((s,x,i)=>s+x*b[i],0),p);}
 function rep(x,p){return p===2?x:(x<=Math.floor(p/2)?x:x-p);}
 function pair(x){return [...x,...x.map(a=>-a),0];}
 function word(a,c){return [...a.map(x=>c+x),...a.map(x=>c-x),a.filter(x=>x===0).length];}
 function verifyWitness(p,d,x,A){
  const c=p===2?1:(p-1)/2, a=x.map(y=>rep(y,p)),u=word(a,c),v=word(a.map(y=>-y),c);
  const y=Array(2*d).fill(c).concat([u[2*d]]);
  ck(u[2*d]<=d-1 && v[2*d]===u[2*d]);
  ck(u.every((z,i)=>z>=0&&v[i]>=0&&z+v[i]===2*y[i]));
  ck(A.every(row=>dot(row,u,p)===dot(row,y,p)&&dot(row,v,p)===dot(row,y,p)));
  ck(u.some((z,i)=>i<2*d&&z>c)&&v.some((z,i)=>i<2*d&&z>c));
  out.midpoint_checks++;
 }
 for(const [p,d] of [[2,1],[2,2],[2,3],[3,2],[5,2],[7,2]]){
  const n=2*d+1,k=d-1;
  for(let id=0;id<p**(n*k);id++){
   const a=digits(id,p,n*k), A=Array.from({length:k},(_,j)=>a.slice(j*n,(j+1)*n));
   let x=null;for(let z=1;z<p**d;z++){const t=digits(z,p,d);if(A.every(row=>dot(row,pair(t),p)===0)){x=t;break;}}
   ck(x!==null);verifyWitness(p,d,x,A);out.ambient_maps++;
  }
 }
 for(const [p,d] of [[2,4],[3,3],[5,3]]){
  const k=d-1;
  for(let id=0;id<p**(d*k);id++){
   const a=digits(id,p,d*k), A=Array.from({length:k},(_,j)=>[...a.slice(j*d,(j+1)*d),...Array(d+1).fill(0)]);
   let x=null;for(let z=1;z<p**d;z++){const t=digits(z,p,d);if(A.every(row=>dot(row,pair(t),p)===0)){x=t;break;}}
   ck(x!==null);verifyWitness(p,d,x,A);out.restricted_maps++;
  }
 }
 for(const p of [2,3,5,7])for(let d=1;d<=5;d++){
  const c=p===2?1:(p-1)/2,n=2*d+1,choices=2*c+1, classes=new Map();
  for(let id=0;id<choices**d;id++){
   const a=digits(id,choices,d).map(x=>x-c),v=word(a,c),key=v.slice(0,d).map(x=>mod(x,p)).join(",");
   ck(!v.every((x,j)=>x<=(j<2*d?c:d-1)));
   const target=Array(d).fill(c%p).join(",");
   if(key===target)ck(v[2*d]===d);
   classes.set(key,1);out.words++;
  }
  ck(classes.size===p**d);out.instances++;
  // Injective restriction with an arbitrary extra marker column, and a concrete
  // reachable-class lower-bound check for all p^d choices of that column for d<=3.
  if(d<=3)for(let id=0;id<p**d;id++){
   const col=digits(id,p,d),keys=new Set();
   for(let z=0;z<p**d;z++){
    const x=digits(z,p,d),v=word(x.map(y=>rep(y,p)),c);
    keys.add(x.map((y,j)=>mod(c+y+col[j]*v[n-1],p)).join(","));
   }
   ck(keys.size>=p**(d-1));out.sparse_bound_checks++;
  }
 }
 return out;
}
console.log(JSON.stringify(verify()));
```
Executed output:
```json
{
  "ambient_maps": 36592,
  "restricted_maps": 20450,
  "midpoint_checks": 57042,
  "words": 24238,
  "instances": 20,
  "sparse_bound_checks": 607
}
```
