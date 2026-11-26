# X6 R246 — conic incidence flats and exact boundary-capacity exclusions

2026-11-27 (Asia/Shanghai). Author proof and exact BigInt computation; NOT_REVIEWED. Independent informed TASK_RESEARCH, non-overwriting preservation. Native task lookup r2-20261127-0008-x6-read SUCCEEDED, Source a033cb726cdd1db950a3660a49a9ed24ec5e7ba2, observed 2026-11-26T16:08:15.826699Z, NO_CANONICAL_PUBLICATION_DIRECTORY. This is directory absence only; active owner and own researcher binding not established. No CLAIM, formal Result, review or shared state mutation.

Frozen predecessor: 2e43e8f1623d9c114f31e7c6ea120f1923d6660f:research_notes/portable_direct/2026-11-26_r2_x6_r245_rank_four_primary_face_pruning.md (blob 29ccfec9892403268d1df9b95344444099a62856). Use its exact 47 labeled necessary supports, 49 components, 51 projective endpoint rays, 98 directed germs, 2225 exact linear suffix partitions, Port 10, 1935 directions, six-pair BRC, positive weights (17t,B,22t,D), strict 3/2 near set and legal optimizer. All capacity exclusions inherit the necessary-wall theorem and pure-linear suffix arrangement/capacity correctness of the pinned predecessor. Coefficients and projective conic geometry here are auxiliary weight readouts, not native spatial geometry, no P000/worldview change. No joint relation erased: full signed germ masks and tags are retained for the finite obstruction.

## 1. Structural lemma: conic-incidence boundary reduction

Let P be a finite set of distinct projective rays in three-dimensional auxiliary coefficient coordinates. A nonzero real homogeneous quadratic Q vanishing on three distinct collinear rays vanishes identically on their projective line, hence has its linear equation as a factor (restrict to the two-dimensional linear subspace; a nonzero binary quadratic has at most two distinct projective roots). Such Q is excluded as a unique quadratic root by R242's real factor family closure, subject to inherited hypotheses. A nonsingular conic therefore has no three collinear zero rays.

Five distinct projective points with no three collinear determine exactly one projective quadratic. Proof: choose the first three as coordinate axes, rescale so the fourth is (1,1,1); all coordinates of the fifth (u,v,w) are nonzero, and pairwise unequal because otherwise it is collinear with the fourth and one coordinate axis. The first three point conditions leave only the three mixed monomials. The next two rows (1,1,1) and (uv,uw,vw) are independent, leaving a one-dimensional kernel. The resulting nonzero quadratic must be nonsingular: a real singular quadratic either splits into at most two real projective lines, or has real zero locus a single point (rank-two semidefinite), or a line (rank one). None can contain five distinct points without a collinear triple. Thus every such five-point set gives a nonsingular indefinite quadratic, uniquely up to nonzero scale. Conversely every nonsingular quadratic with five specified zero rays occurs in this enumeration. Additional zero rays cause duplicate sets but not new quadratics. This gives exact rank-five primary-flat coverage without enumerating arbitrary coefficient directions.

For Q(x)=x^T A x with signature (2,1) and isotropic nonzero p, its germ derivative at p is 2p^T A v. The tangent restriction to p^perp_A has radical span(p) and is positive on all vectors not proportional to p. Proof by congruence to diag(1,1,-1) and orthogonal rotation in the first two coordinates followed by rescaling p to (1,0,1); p^perp_A consists of (a,b,a), with Q=b^2. Thus for any nondegenerate directed germ at p whose first derivative vanishes, its second coefficient is positive. For signature (1,2) the signs reverse. In a given nonsingular conic all tangent germs have this same second-order sign; no zero germ is possible. Also for two distinct isotropic projective points p,b, p^T A b is nonzero by the same tangent argument; both directed germs on their segment have the same eventual sign, since Q((1-e)p+e b)=2e(1-e)p^T A b. For three distinct zero rays p,b,c, they are independent (no collinear triple), and the determinant of their Gram matrix is 2(p^TAb)(b^TAc)(c^TAp)=det(A)det([p b c])^2. Hence for signature (2,1) the product is negative. These are exact constraints for future six-coefficient enumeration; this run did not yet use them to classify all coefficient cells.

## 2. Fixed two-ray incidence: complete five-zero subset

In R245's zero-based endpoint ordering, fix p18=(0,1,0), p0=(0,1,12). These impose b=0 and f=-12c in monomial ordering (t^2,B^2,D^2,tB,tD,BD). Enumerate all three additional endpoints from the remaining 49, i.e. 18424 sets. Reject those with any collinear triple by the structural lemma; 3795 such sets. For each of the 14629 other sets compute the exact 1D coefficient kernel, canonicalize by gcd and overall sign, and deduplicate. This is full coverage of nonsingular quadratics through these two fixed rays and at least three other distinct endpoint rays. The rank-five boundary subset is finite; this is not full coverage of their four-dimensional coefficient space.

Actual exact results:
```json
{"total":18424,"collinear":3795,"admissible":14629,"direct":9925,"recursive":2229,"survivors":[],"unknown":0,"checks":5214049,"unique":14599,"masks":12154,"mult":{"direct":11871,"recursive":2728,"survive":0,"unknown":0}}
```
All 14599 distinct nonsingular conics in this set excluded by 12154 distinct full germ masks. Direct and recursive counts in the first level are masks; mult counts distinct canonical conics, not five-point sets. 30 duplicate five-point sets removed. Scope of masks: complete signed jets evaluated with BigInt and symmetric branch swap only. The initial optimistic primary-mask pilot reached its 4,000,000 check budget with 3143 unknown conics (10213 primary direct,1168 primary recursive,5 full direct,70 full recursive; no observed survivor). It is superseded for this subset by the full-jet-first deduplicated run above, which completed without unknowns. The pilot is not additional coverage.

## 3. Four continuous incidence subspaces

For each specified triple of distinct endpoints, take the kernel of their three quadratic evaluation rows in the full six-coefficient space. In each tested case the kernel is rank 3. Pull all 98 germ jet rows back by an exact integer basis, then use R245's inherited R244 rank-three primary/first-active and independent full-row arrangement enumerators; compare complete mask sets exactly. The rank-three full arrangement is complete under the inherited proof (all nonzero row normals span the dual, extreme rays and tangent flags cover every sign face). Primary rows that vanish identically are handled by the first-active-row method. On each full mask test both five-depth linear suffixes. This exhausts arbitrary nonzero real coefficient vectors in each listed kernel, including degeneracy; no sampling claim.

Actual results (B lists basis vectors in monomial order t^2,B^2,D^2,tB,tD,BD):
```json
[{"z":[18,0,6],"B":[["-9","0","0","1","0","0"],["-69","0","0","0","1","0"],["-2691","0","-1","0","0","12"]],"masks":3086,"direct":2130,"recursive":956,"survivors":[],"unknown":0,"checks":1828693},{"z":[18,0,21],"B":[["-4","0","0","1","0","0"],["-74","0","0","0","1","0"],["1924","0","-1","0","0","12"]],"masks":2957,"direct":2458,"recursive":499,"survivors":[],"unknown":0,"checks":779115},{"z":[18,6,21],"B":[["-6048","0","1","143","0","0"],["-5106","0","-1","0","143","0"],["-30636","0","5","0","0","11"]],"masks":3200,"direct":2802,"recursive":398,"survivors":[],"unknown":0,"checks":939635},{"z":[18,0,1],"B":[["-17","0","0","1","0","0"],["-391","0","0","0","1","0"],["73117","0","-1","0","0","12"]],"masks":2971,"direct":2453,"recursive":518,"survivors":[],"unknown":0,"checks":1217603}]
```
The four subspaces have 12214 masks counted with multiplicity between families, 9843 direct and 2371 recursive exclusions, zero unknown; 4765046 capacity checks in the shared memo run. Total final checks with section 2 = 9979095 (not counting superseded pilot). No disjointness from section 2 claimed. All four entire continuous families are excluded under inherited capacity premises.

## 4. Reproduction code (two separate replacements for final return of pinned R245 experiment)

Retrieve the exact JavaScript block from the frozen predecessor. Keep all preceding definitions, input data, linear bank and capacity kernel unchanged. Replace the final return of experiment(data), which invokes rank4, with either of the blocks below; run each independently. In the tool execution the replacement was performed programmatically and the result emitted using new Function with final 'return experiment(data)'. Each block uses only the pinned input and integer operations. No external solver.

### A. Five-point conics through p18 and p0
```javascript
 const anchor=18, mon=[[0,0],[2,2],[0,1],[0,2],[1,2]], H=P.map(p=>mon.map(([i,j])=>p[i]*p[j])), dotN=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n);
 const col=(i,j,k)=>dot(cross(P[i],P[j]),P[k])===0n;
 function nullvec(ids){let B=Array.from({length:5},(_,i)=>Array.from({length:5},(_,j)=>i===j?1n:0n));for(let id of ids){let v=B.map(x=>dotN(H[id],x)),p=v.findIndex(Boolean);if(p<0)throw Error("unexpected rank loss");B=B.flatMap((x,i)=>i===p?[]:[norm(x.map((y,j)=>v[p]*y-v[i]*B[p][j]))])}return norm(B[0],true)}
 let ids=P.map((p,i)=>i).filter(i=>i!==anchor),stats={total:0,collinear:0,admissible:0,direct:0,recursive:0,survivors:[],unknown:0,checks:0},seen=new Set(),bank=new Map(),start=checks;
 const jets=G.map(([u,v])=>{let a=P[u],b=sub(P[v],a);return [0,1,2].map(t=>mon.map(([i,j])=>t===0?a[i]*a[j]:t===1?a[i]*b[j]+a[j]*b[i]:b[i]*b[j]))});
 for(let a=0;a<1;a++)for(let b=a+1;b<ids.length;b++)for(let c=b+1;c<ids.length;c++)for(let d=c+1;d<ids.length;d++){let z=[ids[a],ids[b],ids[c],ids[d]],w=[anchor,...z],ok=true;stats.total++;for(let i=0;i<5;i++)for(let j=i+1;j<5;j++)for(let k=j+1;k<5;k++)if(col(w[i],w[j],w[k]))ok=false;if(!ok){stats.collinear++;continue}stats.admissible++;let q=nullvec(z);let key=q.join();if(seen.has(key))continue;seen.add(key);let m=0n,n=0n;for(let i=0;i<G.length;i++){let s=0;for(let h of jets[i]){s=sg(dotN(h,q));if(s)break}if(s>0)m|=G[i][2];if(s<0)n|=G[i][2]}[m,n]=canon(m,n);let mk=m+","+n;if(!bank.has(mk))bank.set(mk,{m,n,z,q:q.map(String),mult:0});bank.get(mk).mult++}
 ceiling=checks+15000000;let mult={direct:0,recursive:0,survive:0,unknown:0};
 for(let {m,n,z,q,mult:k} of bank.values()){if(count(m)>31||count(n)>31){stats.direct++;mult.direct+=k;continue}try{if(!can(m,5)||!can(n,5)){stats.recursive++;mult.recursive+=k}else{stats.survivors.push({z,q,m:m.toString(16),n:n.toString(16),k});mult.survive+=k}}catch(err){if(err!==CUT)throw err;stats.unknown++;mult.unknown+=k}}
 stats.unique=seen.size;stats.masks=bank.size;stats.checks=checks-start;stats.mult=mult;return stats;
```

### B. Continuous triple incidence spaces
```javascript
 const mon=[[0,0],[1,1],[2,2],[0,1],[0,2],[1,2]], H=P.map(p=>mon.map(([i,j])=>p[i]*p[j])), dotN=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n);
 const J=G.map(([u,v])=>{let a=P[u],b=sub(P[v],a);return [0,1,2].map(t=>mon.map(([i,j])=>t===0?a[i]*a[j]:t===1?a[i]*b[j]+a[j]*b[i]:b[i]*b[j]))});
 function triple(z){let B=Array.from({length:6},(_,i)=>Array.from({length:6},(_,j)=>i===j?1n:0n));for(let id of z){let v=B.map(x=>dotN(H[id],x)),p=v.findIndex(Boolean);if(p<0)throw Error("rank loss");B=B.flatMap((x,i)=>i===p?[]:[norm(x.map((y,j)=>v[p]*y-v[i]*B[p][j]))])}
 let rows=J.map(rs=>rs.map(h=>B.map(x=>dotN(h,x)))),p=partitions(rows),full=fullPartitions(rows),keys=new Set(p.bank.map(({a,b})=>a+","+b));if(full.keys.size!==keys.size||[...full.keys].some(k=>!keys.has(k)))throw Error("coverage mismatch");
 let direct=0,recursive=0,survivors=[],unknown=0,start=checks;ceiling=checks+6000000;
 for(let {a,b,vs} of p.bank){if(count(a)>31||count(b)>31){direct++;continue}try{if(!can(a,5)||!can(b,5)){recursive++;continue}let q=actual(rows,vs);survivors.push({q:q.map(String),a:a.toString(16),b:b.toString(16)})}catch(e){if(e!==CUT)throw e;unknown++}}
 return {z,B:B.map(x=>x.map(String)),masks:keys.size,direct,recursive,survivors,unknown,checks:checks-start}}
 return [[18,0,6],[18,0,21],[18,6,21],[18,0,1]].map(triple);
```

## Next
Use the tangent sign and no-three-collinear constraints in the six-coefficient primary-flat enumeration, prioritizing high incidence endpoint p18 and shared flats. The four tested three-zero subspaces and fixed two-ray five-zero subset are closed conditional on the inherited proof; do not repeat them. A natural next exact step is other rank-five boundary rays, or a full four-dimensional kernel through p18,p0 with its identically zero primary rows handled by full jets. Generic nonsingular conic root and sole quadratic at internal nodes remain open; unrestricted K6 remains 1–2. Independent mathematical review and Activity association pending.
