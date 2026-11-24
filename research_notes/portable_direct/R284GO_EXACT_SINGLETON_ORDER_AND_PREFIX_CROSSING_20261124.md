# R284GO — Exact singleton ordering and one-dimensional crossing criterion for all seven modes

2026-11-24. Informed portable research, author proof and exact finite regression, NOT_REVIEWED. Auxiliary four-phase fixed binary tag model, no native physical interpretation. P000 and ACTIVE worldview unchanged. Original registration r1-20261124-0256-r284gd-session-v1 independently returned SUCCEEDED, EM-DIRECT-0C386E / RA-B82240E8488EF5A1DA5186C4. Owner inventory request r1-20261124-1200-owner last observed RUNNING, error=null; no shared CLAIM or formal task mutation.

Frozen inputs:
- R284GN @afae60df3e811e985f53284b629e5c468649ee34:research_notes/portable_direct/R284GN_FULL_SEVEN_MODE_PREFIX_DISTANCE_AND_U4_SHARP_20261124.md (GN2/GN3, exact full-carrier prefix distances, GE full-cycle criterion).
- Its frozen dependency R284GM @a06ff527a1494a6a61b6964f9a753bcb35ab7433:research_notes/portable_direct/R284GM_GLOBAL_LOW_OMISSION_SHARP_CAPACITY_AND_RIGIDITY_20261124.md (adjacent and opposite stable conditions).

## GO1: Exact normal form for write schedules

For an arbitrary nonnegative integer seven-mode histogram x, omission q>=0 and integer distance threshold r=2u+1 (indeed any integer r>=1), consider edge 0->1 in GN normalization. Write a_p for attempted coordinates in p=1,3,5,7. A path is admissible for the third-phase avoidance condition iff D2,D3>=r at every attempted prefix.

Every admissible path can be rearranged into one with all type 1 attempts first, all type 7 attempts last, and only types 3,5 interleaved in the middle. Existence of a path in this normal form is equivalent to existence of an arbitrary path. This retains the entire histogram and independent omission source budgets; no singleton is removed from the code.

Proof: directly from GN2, D2 is nondecreasing in a1,a5 and nonincreasing in a3,a7. From GN3 write s=[a1+a3-q]+, l=[a1-q]+ (equivalently [s-a3]+), s-h=[a3-q]+. Its maximum terms show D3 is nondecreasing in a1,a3, nonincreasing in a5,a7. Thus increasing a1 or decreasing a7 in a prefix weakly improves both distances. Bubble each type 1 attempt to the front by adjacent swaps: at the only changed intermediate vertex the new prefix equals the previous vertex plus a type 1 attempt, hence remains safe. Bubble each type 7 attempt to the back: the changed intermediate vertex equals the later original vertex minus a type 7 attempt and remains safe. All attempts are preserved. The initial and final vertices are unchanged. Conversely the normal form is a valid original path. The other three edges follow by cyclic renormalization, not by assuming the same histogram indices on all four edges.

## GO2: Closed crossing test

Set A=x3, B=x5, P=x1, V=x7, and let a,b denote attempted counts of types 3,5 in the middle portion (a1=P,a7=0). Use [z]+=max(0,z). For 0<=a<=A set U=A-a and

  k(a)=max(0,[U-q]+ + [V-q]+ -q),
  c(a)=max([x2-q]+ + [x6-q]+ -q,
           [U+x2-q]+ + [V+x6-q]+ -2q).

GN2 becomes D2(a,b)=max(k(a), [P+b-q]+ + c(a)). Define the lower bound
  L(a)=0 if k(a)>=r or c(a)>=r;
       max(0,q-P+r-c(a)) otherwise.

For GN3 put s=[P+a-q]+, l=[s-a]+, h=min(s,P), p=[V-q]+-q and
  J(a)=max(0,s-2q,l-q,s-h-q,p+max(0,l-q+x6)),
  C(a)=p+max(s-2q+x6+x4+B, s-h-q+x4+B).

Expanding GN3's M gives D3(a,b)=max(J(a),C(a)-b), so its upper bound is
  H(a)=B if J(a)>=r;
       min(B,C(a)-r) otherwise.

In the integer middle rectangle 0<=a<=A, 0<=b<=B, D2>=r iff b>=L(a); D3>=r iff b<=H(a). In particular L>B or H<0 must not be clamped to a feasible range. Both L and H are nondecreasing in a: this follows from the original monotonicity (or the displayed formulas including their threshold cases).

The exact edge criterion is:
  (i) both original endpoints (0,0,0,0) and (x1,x3,x5,x7) satisfy GN2/GN3;
  (ii) L(a+1)<=H(a) for every integer 0<=a<A.                    (GO)

Necessity: after normalizing, a step from a to a+1 at fixed b has to be safe at both ends; hence b>=L(a+1), b<=H(a). Sufficiency: the initial all-type-1 segment is safe by monotonicity from the original initial endpoint. The final all-type-7 segment is safe by monotonicity backwards from the final endpoint. Thus the middle endpoints (0,0),(A,B) are safe. Start at a=0,b=0=L(0). At each a, increase b to L(a+1) and then increase a by one. Monotonicity of L ensures no backwards b step, and GO implies the upper bound at the entire horizontal segment; H is nondecreasing so the next vertex is safe. After a=A, increase b to B, safe because H(A)=B and D2 is nondecreasing in b. A=0 uses just that horizontal segment. This constructs a schedule explicitly. Integer a,b count attempts, not successful writes; GN formulas already minimize all allowed histories and omissions.

Together with frozen GE adjacent rollback and GM opposite stable checks on the same histogram, apply GO to each rotated edge to decide full-cycle safety. GO replaces four-dimensional path reachability by an exact one-variable crossing criterion. A direct implementation uses O(A+1) integer arithmetic operations and O(1) working memory for the edge decision. Explicit per-coordinate output still takes time proportional to its length.

## GO3: Width-independent finite affine decision

There is also a width-independent number of exact integer arithmetic/comparison operations to decide GO (operand bit length is still accounted for). This is an analytic algorithmic corollary, not a benchmark claim.

For fixed x,q,r, all expressions defining L(a+1) and H(a) are built from a fixed number of integer affine expressions in a using addition, subtraction, min, max, and comparisons with fixed threshold r. Enumerate the branch choices in these fixed expression trees (including both branches of the L and H conditionals), retaining the affine inequalities that justify each branch. Each leaf gives an affine formula for L(a+1)-H(a), valid on the intersection of finitely many linear inequalities in a. Intersect with the integer interval [0,A-1]. Each constraint m*a+c>=0 gives a lower or upper integer bound by exact ceiling/floor division, or a constant true/false condition when m=0; strict comparisons convert to >=1 since the operands are integers. Empty intervals are discarded. For every nonempty interval, test the affine difference at the two integer endpoints, where its maximum is attained. GO holds precisely when every maximum is <=0. Equalities on branches can be assigned to either matching min/max branch, while the L/H comparisons use the exact stated tie convention. All branch counts depend only on the fixed expression, not on A,B,q,r or other multiplicities. This makes a small one-variable piecewise-affine feasibility problem available for uniform symbolic capacity proofs; explicit branch pruning/benchmarking is a next implementation option. No need to enumerate all physical prefix states or all write orders.

## Exact finite regression (executed in JavaScript)

The following reproduces the executed integer test. All x1..x7 in 0..3, q=0..2, thresholds r=1..5 (including non-model even thresholds as stronger implementation regression). The independent reachability comparison uses original four attempted coordinates with GN2/GN3, not the normal-form path. Bounds are checked at every middle prefix. Arithmetic exact within JS safe integer range for this domain.

```javascript
function pos(t){return Math.max(t,0)}
function distances(x,q,a1,a3,a5,a7){
 const U=x[3]-a3,V=x[7]-a7,W=pos(a1+a5-q);
 const d2=Math.max(0,pos(U-q)+pos(V-q)-q,W+pos(x[2]-q)+pos(x[6]-q)-q,W+pos(U+x[2]-q)+pos(V+x[6]-q)-2*q);
 const s=pos(a1+a3-q),l=pos(s-a3),h=Math.min(s,a1);
 const M=(t1,t2)=>Math.max(0,s-t1-t2,l-t1,s-h-t2);
 const d3=Math.max(M(q,q),pos(x[7]-a7-q)+M(q-x[6],q-x[4]-x[5]+a5)-q);
 return [d2,d3];
}
function bounds(x,q,r,a){
 const U=x[3]-a,V=x[7],P=x[1],B=x[5];
 const k=Math.max(0,pos(U-q)+pos(V-q)-q);
 const c=Math.max(pos(x[2]-q)+pos(x[6]-q)-q,pos(U+x[2]-q)+pos(V+x[6]-q)-2*q);
 const L=k>=r||c>=r?0:Math.max(0,q-P+r-c);
 const s=pos(P+a-q),l=pos(s-a),h=Math.min(s,P),p=pos(V-q)-q;
 const J=Math.max(0,s-2*q,l-q,s-h-q,p+Math.max(0,l-q+x[6]));
 const C=p+Math.max(s-2*q+x[6]+x[4]+B,s-h-q+x[4]+B);
 return [L,J>=r?B:Math.min(B,C-r)];
}
function crossing(x,q,r){
 const ok=(a,b,c,d)=>distances(x,q,a,b,c,d).every(v=>v>=r);
 if(!ok(0,0,0,0)||!ok(x[1],x[3],x[5],x[7]))return false;
 for(let a=0;a<x[3];a++)if(bounds(x,q,r,a+1)[0]>bounds(x,q,r,a)[1])return false;
 return true;
}
function full(x,q,r){
 const ps=[1,3,5,7],m=new Map();
 function visit(a){const k=a.join(",");if(m.has(k))return m.get(k);
 if(distances(x,q,...a).some(d=>d<r)){m.set(k,false);return false}
 if(a.every((v,i)=>v===x[ps[i]]))return true;
 for(let i=0;i<4;i++)if(a[i]<x[ps[i]]){let b=a.slice();b[i]++;if(visit(b)){m.set(k,true);return true}}
 m.set(k,false);return false}
 return visit([0,0,0,0]);
}
let hist=0,paths=0,yes=0,btests=0;const x=Array(8).fill(0);
function test(){hist++;for(let q=0;q<=2;q++)for(let r=1;r<=5;r++){
 for(let a=0;a<=x[3];a++){let [L,H]=bounds(x,q,r,a);for(let b=0;b<=x[5];b++){const [d2,d3]=distances(x,q,x[1],a,b,0);if((d2>=r)!==(b>=L)||(d3>=r)!==(b<=H))throw Error(JSON.stringify({x,q,r,a,b,L,H,d2,d3}));btests++}}
 const v=crossing(x,q,r),w=full(x,q,r);if(v!==w)throw Error(JSON.stringify({x,q,r,v,w}));paths++;yes+=v;
}}
function rec(i){if(i===8){test();return}for(let n=0;n<=3;n++){x[i]=n;rec(i+1)}}
rec(1);
console.log({hist,paths,yes,btests,failures:0});
```

Actual output: hist=16384, paths=245760, yes=82874, btests=1536000, failures=0. Both safe and unsafe edge instances were included; these counts are not a global capacity scan and do not independently revalidate GN's physical incidence assumptions.

## Next

Apply the affine crossing obstruction to the single-cell opposite-cut family and the two-full-cut family identified in GN4. In particular use all four rotations and the singleton cost bound to exclude sub-F histograms for u>=5 in u<q<4u-3. The new exact normal form and crossing criterion remove the path-search quantifier without erasing source groups. The general sharp capacity lower bound in that region remains open. No new capacity region or independent Review is claimed.
