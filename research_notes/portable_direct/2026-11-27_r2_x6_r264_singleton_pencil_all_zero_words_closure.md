# X6 R264 — arbitrary singleton-pencil zero words excluded under the common zero

2026-11-27. Independent informed TASK_RESEARCH, author proof and exact BigInt computation, NOT_REVIEWED. P000 V5 and ACTIVE residual-fidelity and joint-relation constraints retained. Coordinates (t,B,D) are auxiliary BRC weight coordinates, not native spatial addresses. Native request r2-20261127-1308-x6-read SUCCEEDED at 2026-11-27T05:08:20.116941Z, Source ed90fe9e5400d61cd1e2ab0e8b46a52bac13fc66, NO_CANONICAL_PUBLICATION_DIRECTORY (directory observation, not owner projection). Own researcher identity unconfirmed; no CLAIM, Result/Review or shared state mutation. Activity association pending.

## Frozen scientific inputs

R247@7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md (51 rays, 98 directed germs, 47 necessary support labels, 2225 linear suffix partitions). Port 10, 1935 directions, weights (17t,B,22t,D), six-pair joint BRC strict 3/2. Inherit the necessary-wall and monotone linear-suffix capacity premises. R261@b091d79f5b7b493918b181750b2494c3688799a2:research_notes/portable_direct/2026-11-27_r2_x6_r261_all_pencil_circuit_helly.md (17 directions, 12 slope sectors, intercept circuit criterion). R262@cdd1ec936c0b5c10261a9c61e25620c15f43f999 and R263@ad7b401b318356baa1c1597663cedff871e80dae exclude exactly one finite zero on each multipoint pencil. R258@b0960b0e767177f2b6bb7437275bf19aa662f7f0 excludes internal sole quadratic observations at author-proof scope.

## Theorem and proof

Let Q=a t^2+b B^2+c D^2+d tB+e tD+f BD be full rank with Q(p24)=c=0. If all 39 finite anchors on the six multipoint pencils through p24 have Q(p)!=0, Q cannot be the sole quadratic root of a correct depth-six tree, regardless of the zero/sign status of every remaining singleton-pencil anchor. In fact the first seven singleton pencils after the six multipoint pencils suffice.

Proof: for direction (T,U), finite p=(rT,rU,D), r>0, y=D/r, the sign is that of K+(eT+fU)y, K=aT^2+dTU+bU^2. The six multipoint pencils with strict signs use exactly the R261 slope sectors and open interval intercept constraints. Each singleton pencil independently admits two strict words or a zero word. The zero word imposes a singleton intercept K=-(eT+fU)y. Allowing a zero word even when the representative slope is zero is a relaxation: true full-rank Q cannot vanish identically on a pencil. For strict words on a singleton pencil the intercept bounds do not depend on the chosen representative's slope sign. The germ at p24 is recovered exactly as in R261: sign(e+17f), or sign(K17) if this slope is zero. The latter is nonzero because the B=17t pencil is strict. Normalize f>0 or f=0,e>0 by global branch exchange; (e,f)=(0,0) implies rank deficiency.

For four distinct directions let w be the signed cofactor vector of their rows (T^2,TU,U^2); all w_j are nonzero. The interval sum of w_j J_j must contain zero. Each J_j is either a nonempty open interval (possibly unbounded) or a singleton. If any J_j is open then the Minkowski sum is open and both finite endpoint comparisons are strict. If all four are singletons, the sum is a singleton and zero membership is an exact equality, not a strict inequality. After normalization f>0, each comparison is a linear constraint in x=e/f: A x+B>0 or A x+B=0. The latter fixes x=-B/A when A!=0, or requires B=0 otherwise. Intersect fixed x with all prior strict bounds and all prior equalities; for f=0 the test is A>0 or A=0. This covers all true coefficient vectors, including zero anchors and sector-boundary values. We use the conditions only as necessary filters; R261 gives sufficiency when the full intercept constraints are applied, but no sufficiency is needed here.

At each prefix retain the outgoing germ signs at all nonzero anchors, and leave the outgoing germs of finite zero anchors unassigned, never assumed absent from the eventual tree. Each partial mask is a subset of its eventual strict branch. count<=31 and can(mask,5) must hold by inherited monotone suffix capacity. Therefore failure excludes all residual completions. The exact computation below exhausts the 12 slope sectors, the strict words on the six multipoint pencils, and all three words on each subsequent singleton pencil. No partial mask survives prefix 13, so no tangent-residual completion is needed. Unprocessed four singleton pencils are unconstrained. This proves the theorem.

Corollary: combine R262/R263 and the theorem: any successful full-rank sole quadratic root with c=0 must have at least two finite zeros on distinct pencils, with at least one of those zeros in the 39-anchor multipoint set. There are thus at least three projective zero anchors including p24; three distinct zero anchors of a full-rank ternary quadratic cannot be collinear (otherwise a linear factor), and their evaluations are linearly independent. The remaining coefficient space is a union of 3-dimensional kernels for triples including p24 and at least one multipoint anchor. K6 remains 1..2. c!=0 remains open.

## Exact executed evidence

Three runs were completed. Common prefix costs are repeated; not additive as independent work. Run A: exactly one zero among singleton anchors {7,13,17,22,27,30,31}, remaining finite anchors strict, 19,499,850 checks; unique by prefix [4,80,1278,2789,1997,233,212,232,268,67,10,7,0,0,0,0,0]; 12 sectors, final 0. Run B: exactly two singleton zeros, all multipoint anchors strict, 19,502,075 checks; prefix [4,80,1278,2789,1997,233,212,232,277,69,10,7,0,0,0,0,0]; 12 sectors, final 0. Run C (strongest, subsumes A and B): arbitrary singleton zeros, 19,502,075 checks, same unique counts as B, 12 sectors, final 0. No CUT or incomplete sector. Run C exact aggregate by prefix:
columns: k (one-based), visits, direct, algebraic, recursive, surviving sector states, capacity checks, unique masks up to branch exchange.
1 57 0 0 0 57 197 4
2 530 0 0 0 530 24220 80
3 6340 540 0 830 4970 599759 1278
4 27752 6285 11472 2701 7294 3137075 2789
5 48063 17307 20233 6674 3849 8442941 1997
6 14790 5968 4402 4080 340 5535642 233
7 1020 74 530 129 287 541429 212
8 861 41 467 51 302 297473 232
9 906 41 495 23 347 279328 277
10 1041 41 612 313 75 462631 69
11 225 0 148 67 10 153763 10
12 30 0 20 3 7 6986 7
13 21 0 14 7 0 20631 0
14–17 all zero.
Frozen groups: [[18,2,0,36],[26,19,34,20,25,28,39,1,37],[10,15,11,45,49,9,38,42,40,44,47,50],[48,21,29,23,46],[4,14,16,12,3,8],[6,5,43],[7],[13],[17],[22],[27],[30],[31],[32],[33],[35],[41]].

## Reproduction: strongest Run C

Extract the first JavaScript fenced block in the pinned R247 as src, and first JavaScript block in pinned R261 as patch. Apply the following exact edits, then execute. All coefficient arithmetic uses BigInt; counters are ordinary integers within exact range. The source code remains part of the frozen BRC auxiliary observer computation, not a native dynamics experiment.

```javascript
let edits=[
["ceiling=50000000;","ceiling=100000000;"],
["function patterns(k,s)","function eq(I,x,y){if(!x)return !y;let q=x>0n?[-y,x]:[y,-x];if(I[2]&&cmp(I[2],q))return false;if(I[0]&&cmp(I[0],q)>=0||I[1]&&cmp(q,I[1])>=0)return false;I[2]=q;return true}\nfunction patterns(k,s)"],
["if(v[i]>0)a|=E[ids[i]];else b|=E[ids[i]]","if(v[i]>0)a|=E[ids[i]];else if(v[i]<0)b|=E[ids[i]]"],
["out.push({a,b,l:pos.length?row(pos[s<0?pos.length-1:0]):null,u:neg.length?row(neg[s<0?0:neg.length-1]):null})","let z=v.indexOf(0);out.push({a,b,l:z>=0?row(ids[z]):pos.length?row(pos[s<0?pos.length-1:0]):null,u:z>=0?row(ids[z]):neg.length?row(neg[s<0?0:neg.length-1]):null,zero:z>=0?ids[z]:null})"],
["if(!s){emit(Array(n).fill(1));","if(k>=6)emit([0]);if(!s){emit(Array(n).fill(1));"],
["let states=[{a:0n,b:0n,ps:[],I}]","let states=[{a:0n,b:0n,ps:[],I,zs:[]}]"],
["for(let st of states)for(let p of pats){visits++;","for(let st of states)for(let p of pats){let zs=p.zero===null?st.zs:st.zs.concat(p.zero);visits++;"],
["if(!inf&&!(f?cut(J,sum[0],sum[1]):sum[0]>0n))","let closed=ix.every(z=>ps[z].zero!==null);if(!inf&&!(f?(closed?eq(J,sum[0],sum[1]):cut(J,sum[0],sum[1])):(closed?sum[0]===0n:sum[0]>0n)))"],
["out.push({a,b,ps,I:J});","out.push({a,b,ps,I:J,zs});"],
["for(let {a,b,I} of states){if((a|b)!==ALL||(a&b))throw Error(\"full mask\");","for(let {a,b,I,zs} of states){if((a|b)!==(ALL^zs.reduce((v,z)=>v|E[z],0n))||(a&b))throw Error(\"partial mask\");"],
["f:String(f),positive:","zs,f:String(f),positive:"]
];for(let [a,b] of edits){if(!patch.includes(a))throw Error(a);patch=patch.replace(a,b)}
patch=patch.replace(/return \{groups,points:[\s\S]*?\};\s*$/,"return {groups,checks,completed,unique:unique.map(s=>s.size),totals,final};");
src=src.replace('return {points:P.length,germs:G.length,linearPartitions:Q.length,result:rank4("two_anchor_kernel",[])};',patch).replace(/experiment\(data\)\s*$/,"return experiment(data);");
let result=new Function(src)();
```

Next: allow zero words on multipoint pencils, where each may have at most one finite zero. At a target multipoint pencil of nonzero slope s, emit v_i=-s before z, v_z=0, v_i=s after z, with exact intercept singleton at z. If B=17t is the target, exclude s=0 for full rank. Keep the same mixed open/singleton circuit tests and partial capacity cuts; if candidates remain, use three-polar coordinates and the full lexicographic local residual. Do not repeat completed singleton-only work. Independent review pending.
