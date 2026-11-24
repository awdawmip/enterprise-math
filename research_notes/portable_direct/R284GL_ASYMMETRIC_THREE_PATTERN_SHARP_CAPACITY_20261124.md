# R284GL — Sharp capacity for the entire asymmetric three-pattern carrier; arbitrary omissions

2026-11-24. Informed portable research, frozen auxiliary four-phase binary fixed-tag model. Author proof, NOT_REVIEWED; no shared CLAIM. P000 / ACTIVE worldview unchanged. This is a discrete source-incidence model, not a new native X6/BRC computation or physical attribution. Own registered session MCP-8cd6c4fa26b9459d923ff73ba0082220, Researcher EM-DIRECT-0C386E, Activity RA-B82240E8488EF5A1DA5186C4, original registration receipt r1-20261124-0256-r284gd-session-v1 SUCCEEDED; owner inventory r1-20261124-0900-owner pending at derivation, no formal task authority asserted.

Frozen sources:
- R284GK @9c56aa402a9f36352c11ea721fe5b1bba580fdf1:research_notes/portable_direct/R284GK_LOW_OMISSION_THREE_PATTERN_CONSTRUCTION_20261124.md (construction, symmetric-only optimality).
- R284GE @a112519ea319ef0e0bdf10ee01d817e10fd3dcd5:research_notes/portable_direct/R284GE_EXACT_ADJACENT_ROLLBACK_CAPACITY_20261124.md (GE1, exact last-source cut and full-cycle criterion).
- R284GK checker @501e7fce66cecd84af712be7dc79cf249c265590:research_notes/portable_direct/R284GK_finite_capacity.cpp (bit and last-change indexing).

## Theorem

For all integer q>=0,u>=1, the minimum width among *all* nonconstant histograms supported on {3,5,6}, allowing unequal, zero, and sub-2q multiplicities, is exactly

F(q,u) = min(4q+8u+2, max(5q+5u+2,6q+4u+2)).

Thus asymmetric three-pattern codes do not improve the prior symmetric upper construction. The global seven-pattern problem for q>0 remains open outside previously established regions; no unsupported erasure of patterns 1,2,4,7. In addition, at q=0 the full seven-pattern problem has exact capacity 5u+2 for every integer u>=1.

## Exact third-phase distances without heavy or symmetry hypotheses

Let x3=A,x5=B,x6=C, all nonnegative. At edge 0->1 let a,b be attempts on 3,5 and s,t their successes; 0<=s<=a,0<=t<=b,(a-s)+(b-t)<=q. Use positive part [z]+. The exact minimum over histories and comparison stable words at fixed s,t is

d2(s,t) = [A-s-2q]+ + max(0,t-q,C+t-2q),
d3(s,t) = max(0,C-2q,s-q,B-t+s-2q,B-t+C+s-3q).

Reason: for phase 2, the A-s unwritten mismatches of type 3 have a disjoint pair of capacity-q vertices; the C type-6 mismatches have endpoints S3,T1, and the t type-5 mismatches have only T1. The latter two demands have maximal deficit max(0,t-q,C+t-2q) (the singleton C-2q cut is dominated). For phase 3, B-t unwritten type-5 mismatches have endpoints S3,T2; C type-6 mismatches have endpoints S3,T1; s successful type-3 mismatches have only T2. The contained-demand deficits of the possible subsets of these three vertices are precisely the displayed maximum after dominated terms are removed. GE/FM gives equality with the physical minimum, not just a bound. In particular no use of residual total as a substitute for source incidence.

Put M=[C-q]+. d2 decreases in s and increases in t; d3 increases in s and decreases in t. To minimize d2 use s=a,t=[b-q]+; to minimize d3 use s=[a-q]+,t=b. Each allocates all useful omissions to only one type, and is attainable. Therefore the exact attempted-prefix tests are

D2(a,b) = [A-a-2q]+ + [[b-q]+ + M-q]+,
D3(a,b) = max(0,C-2q,[a-q]+-q,B-b+[a-q]+-2q+M).

They extend GK to the entire asymmetric carrier including small and zero counts. A safe path requires D2,D3>=2u+1 at every prefix. Cycle rotation with phase-0 XOR normalization interchanges 3 and 6, keeping 5 fixed; thus apply the same formulas on the rotated edge with A,C exchanged.

## Lower bound

Write the smaller of x3,x6 as m and the larger as L=2q+e. By phase rotation we can test the edge updating the larger type L and alternating type B, leaving m unchanged. Opposite stable distance is exactly [m-2q]+ + [L-2q]+ because the two differing types have disjoint source/comparison endpoint pairs. Necessity >=2u+1 implies L>2q and e>=u+1 (integer).

The adjacent GE1 condition for the edge updating m and B is [m-q]+ + [B-q]+ >= q+4u+1: the two active types have distinct old source groups. The analogous inequality also holds for L. The following cases cover every histogram.

1. B<q. GE1 forces m>=2q+4u+1; L>=m, hence n>=4q+8u+2>=F.

2. B>=q and m>=q. Put d=m-2q, so -q<=d<=e. GE1 gives m+B>=3q+4u+1, hence n=m+L+B>=5q+4u+1+e>=5q+5u+2. If d>=2u+1, this bound is >=5q+6u+2, which is >=F: for q<=u compare 5q+5u+2; for u<q<2u compare 6q+4u+2; for q>=2u compare 4q+8u+2. If e>q+1, the same GE bound gives n>=6q+4u+3, so together with the first bound n>=max(5q+5u+2,6q+4u+2)>=F.

It remains d<=2u and e<=q+1. Every monotone attempted path must first move the count a of the larger changing type from e-1 to e, at some b held fixed. At a=e, D2=[[b-q]+ + d]+. Safety forces b>=q+2u+1-d since d<=2u. At the preceding a=e-1<=q, D3=max(0,d,B-b+d-q), so safety forces B>=b+q+2u+1-d. Adding yields B>=2q+4u+2-2d and n>=6q+4u+2+e-d>=6q+4u+2. Combine with the first bound.

3. m<q and B>=q. Opposite stable separation now implies e>=2u+1, and GE1 gives B>=2q+4u+1. Thus n>=4q+6u+2+m>=5q+5u+2 when q<=u; this already suffices for that region. For q>=u, it suffices to prove n>=6q+4u+2 (which is >=F).

If e>=2q+2u+2, the preceding GE bound with L=2q+e yields n>=6q+6u+3+m. Otherwise take again the unit crossing a=e-1 to e at b. Now M=[m-q]+=0 in the exact prefix tests. At a=e, D2=[b-2q]+ so b>=2q+2u+1. At a=e-1, let s=[e-1-q]+. Since e<=2q+2u+1, s-q<=2u; also m-2q<0. Therefore D3 safety forces B>=b+2q+2u+1-s>=4q+4u+2-s. If e<=q+1 then s=0 and n>=6q+4u+2+m+e. Otherwise s=e-1-q and n>=7q+4u+3+m. Both prove the required bound.

These cases establish n>=F without assuming x3=x6, x3,x6>=2q, x5>=q, or any bound on q,u. GK gives equality for q<2u with its symmetric construction; for q>=2u the repeated Gray code x3=x6=2q+4u+1,x5=0 attains F. Rotation and the all-cycle criteria are the same as the fixed source. No finite test is used to infer the unbounded lower bound.

## Global no-omission endpoint and elementary general lower bound

For any seven-mode histogram, each normalized binary column contributes at most four to the sum of all six nominal pairwise Hamming distances (a column with k ones contributes k(4-k)<=4). Each adjacent nominal distance is >=2q+4u+1 by GE1: the changing count D>q and sum min(q,N_e)>=q. Each opposite nominal distance is >=2q+2u+1: for a pair with D differing coordinates, one can remove min(D,2q) mismatches by disjoint corrections of at most q on each side, which satisfy every last-change source capacity and are reachable by GE section 1. Stable separation demands remaining distance >=2u+1. Hence

4n >= 4(2q+4u+1)+2(2q+2u+1) = 12q+20u+6,
n>=3q+5u+2.

At q=0 this lower bound equals the GK construction (A=C=u+1,B=3u) for every u>=1. This is a global theorem, including all four other types. For q>0 the bound alone is not sharp in general. No claim that the other modes are redundant.

## Exact executed regression

The following independent JS checker recomputes the eight-source cut incidence from pattern bits and last nominal changing edges, merges duplicate cut masks by minimum capacity coefficient, and minimizes over *all* current omission allocations. It compares both new formulas at each prefix for q=0..3, A,B,C=0..7, a=0..A,b=0..B. Actual run: {"checked":41472,"cutCounts":[6,7],"status":"PASS"} (41472 prefix pairs, 82944 distance comparisons; 6 and 7 distinct compressed cuts). This corroborates the derivation even for zero and non-heavy types. The proof, not the finite check, establishes the all-parameter result.

```javascript
function verify(){
const pp=[3,5,6],bit=(p,i)=>i?((p>>(i-1))&1):0,last=(p,i)=>{for(let d=1;d<=4;d++){let e=(i-d+4)%4;if(bit(p,e)!=bit(p,(e+1)%4))return e;}};
const cuts=j=>{let out=[];for(let U=0;U<256;U++){let w=pp.map(p=>{let E=(1<<last(p,0))|(1<<(4+last(p,j)));return +(bit(p,0)!=bit(p,j)&&(U&E)==E)}),v=pp.map(p=>+(bit(p,1)!=bit(p,j)&&!!(U&(1<<(4+last(p,j))))));let c=U.toString(2).replace(/0/g,"").length;let key=w.join("")+v.join("");if(!out.some(z=>z.key===key&&z.c<=c)){out=out.filter(z=>z.key!==key);out.push({w,v,c,key})}}return out};
const c2=cuts(2),c3=cuts(3),pos=x=>Math.max(0,x),dist=(cuts,A,B,C,s,t,q)=>Math.max(...cuts.map(({w,v,c})=>w[0]*(A-s)+w[1]*(B-t)+w[2]*C+v[0]*s+v[1]*t-c*q));
let checked=0;
for(let q=0;q<=3;q++)for(let A=0;A<=7;A++)for(let B=0;B<=7;B++)for(let C=0;C<=7;C++)for(let a=0;a<=A;a++)for(let b=0;b<=B;b++){let x=Infinity,y=Infinity;for(let o=0;o<=Math.min(q,a);o++)for(let p=0;p<=Math.min(q-o,b);p++){x=Math.min(x,dist(c2,A,B,C,a-o,b-p,q));y=Math.min(y,dist(c3,A,B,C,a-o,b-p,q))}let m=pos(C-q),s=pos(a-q),D2=pos(A-a-2*q)+pos(pos(b-q)+m-q),D3=Math.max(0,C-2*q,s-q,B-b+s-2*q+m);if(x!==D2||y!==D3)throw Error(JSON.stringify({q,A,B,C,a,b,x,y,D2,D3}));checked++}
return {checked,cutCounts:[c2.length,c3.length],status:"PASS"}
}
console.log(verify());
```

## Next

Any improvement on GK's global upper bound must use at least one of the singleton/triple types {1,2,4,7}. Keep those source incidences explicitly. Attempt to derive a width-preserving comparison or a direct lower-bound charge from GE1 and competing prefix cuts, or find an actual mixed-mode counterexample. The global q=0 case needs no further scan. This is author-checked, NOT_REVIEWED, with no formal Task/Result or Foundation promotion.
