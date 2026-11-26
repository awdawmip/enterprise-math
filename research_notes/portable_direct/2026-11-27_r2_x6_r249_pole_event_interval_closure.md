# X6 R249 — exact pole-event stratification and a full-dimensional single-anchor interval exclusion

2026-11-27. Independent informed TASK_RESEARCH, author proof and exact BigInt computations, NOT_REVIEWED. Native task read r2-20261127-0312-x6-read SUCCEEDED at 2026-11-26T19:12:40.376273Z, Source dfd4a083615dc982bc6c66368187bcf4665b2c68, NO_CANONICAL_PUBLICATION_DIRECTORY (directory absence only, no native owner projection or execution authorization). No CLAIM, task, Result or Review mutation; own researcher/Activity binding unconfirmed. P000 V5 unchanged.

## Frozen inputs and inherited premises
- R248 at 98f303d0e1b1b1c496c00dbc895d8c7d01f005b0:research_notes/portable_direct/2026-11-27_r2_x6_r248_anchor_tangent_coordinate_closure.md, blob f0c6fcd5fdfc4f343ff6b19ba5567ccb5d779b44.
- R247 at 7e54892a45579bdc497c27e061399339d1fb3512:research_notes/portable_direct/2026-11-27_r2_x6_r247_two_anchor_signed_primary_faces.md, blob fdbef2ee6e6c32573f3a1ccd171cb5337de520fa. Its complete exact integer input and signed rank-four arrangement/suffix code were read and reused.
- R238 at a64888948bdacb5ba4e691d3eb2b783ed43f56ea:research_notes/portable_direct/2026-11-26_r2_x6_r238_one_support_factor_root_family_closure.md, blob 9b05af42eef4b4351130e2a6f8a53f8995b749e9. Zero-germ support-factor recovery and previously closed one-support-factor family.
- Same frozen Port 10, 1935 integer directions, six-pair BRC, positive weights (17t,B,22t,D), strict 3/2 near-set problem, 47 necessary supports, 49 components, 51 endpoint rays, 98 directed interval germs and 2225 linear suffix partitions. All root exclusions inherit the necessary-wall theorem and completeness of the pure-linear suffix capacity method. This is auxiliary weight coefficient arithmetic, not a new native spatial plane, physical dynamics or an extra native dimension.

## Theorem 1: exact pole-event stratification, including every higher jet

At p18=(0,1,0) impose Q(p18)=0, so Q=a t²+c D²+e tD+d tB+f BD. For f!=0 define the pole s=-d/f. The fixed-pole homogeneous family is Q=a t²+c D²+e tD+f B(D-s t); the f=0 part is also contained in this family and has already been treated by R248.

Write the three germ rows in coefficient order (a,c,e,d,f). For each nonzero row r let r(s)=(r_a,r_c,r_e,r_f-s r_d). Add the chart row (0,0,0,0,1) before restriction. Retain original row orientations and germ labels; primitive row deduplication is only for enumerating determinant events. For any four rows the determinant of the restricted matrix is F-s E, where F is the determinant on columns (a,c,e,f) and E is the determinant on columns (a,c,e,d). Thus the only possible isolated finite arrangement events are exact rational s=F/E with E!=0. Identically zero determinants are retained as zero, not treated as events. A nonzero constant minor certifies rank four for all s.

Claim: on any open interval containing none of these events, the entire bank of oriented sign patterns of all restricted rows, including the chart row, is invariant. Consequently the full lexicographic germ-mask bank is invariant there, not just the endpoint signs or the optimistic first-active masks.

Proof: every ordered maximal minor has constant sign. This determines ranks of all subsets (an independent subset extends to a basis of the row family), and the signs of every minimal linear dependence by extending its independent part to a row basis and applying Cramer's rule. For clarity, a desired sign pattern is feasible exactly when the signed strict rows, after projection modulo the span of its zero rows, admit a linear functional strictly positive on each. Equivalently zero is absent from their convex hull: if absent the closest point of this finite convex hull supplies a strict separating functional, and if present the convex combination obstructs it. An inclusion-minimal positive dependence in this quotient is unique up to scale and has all its strict coefficients positive (otherwise a second independent dependence allows a positive combination to reduce its support). Choose an independent basis of the zero rows; adjoining this strict subset gives a unique dependence in the original row family, whose strict coefficient signs are determined by maximal minors after extending to a row basis. The existence of such an obstruction is therefore invariant under constant maximal-minor signs. This proves exact sign-pattern invariance, including zero equalities. Restore fixed orientation multipliers of normalized rows, then apply the germ lexicographic rule to each sign pattern. The chart row permits restricting to f>0 or f<0 without losing the same invariance. Branch-swap canonicalization is only done after full sign evaluation. This proof covers the whole open interval; isolated event poles require separate exact computations.

## Exact determinant event experiment

Using the immutable R247 input, construct 98 directed germs exactly as there, including its two split supports. The full single-anchor jet arrangement has 188 distinct nonzero primitive rows INCLUDING the chart row; the first-active subset has 63 including chart. All arithmetic was BigInt; determinant counts are row-quadruple counts, not counts of conics. Row orientation was ignored only in event enumeration because multiplying rows by fixed nonzero constants leaves their determinant zero locations unchanged.

Primary only: all 595665 quadruples, 116637 identically zero, 26599 nonzero constant, 452429 moving, yielding 197869 distinct rational events (173263 positive, 24605 negative, one zero). Nearest strictly below/above 22: 1043909/47451, 563117/25596. This demonstrates that a naive global pole sweep is already very large even before full jets.

Full jets: all 50404915 quadruples, 2587726 identically zero, 2091284 nonzero constant, 45725905 moving, of which 908259 vanish at s=22. Nearest strictly below/above 22:
l=22207240/1009421 = 22-22/1009421;
u=1392445341/63292963 = 22+155/63292963.
Zero-based quadruple witnesses in the insertion-order normalized full bank: l=[52,53,56,94], u=[65,112,136,146]. There are no full-row determinant events in (l,22) or (22,u). The number of distinct FULL events was not computed. Nonzero constant minor count proves the rank premise. The first-active event boundaries alone would not justify transfer of full high-order jets.

## Exact rank-four slice closure and transfer

Reuse R247 signed first-active rank-four arrangement plus pure-linear suffix capacity. Only the jet rows and result label were changed. For s=n/m (m>0), use the integral basis (t²,D²,B(mD-n t),tD); its real span is the entire fixed-s family. The two interior representatives are mediants 22207262/1009422 and 1392445363/63292964, strictly between l and 22 and between 22 and u respectively, checked by exact cross products. The other three slices are l,22,u. Each run used the complete original bank, including all higher residuals, with original 45M capacity-check ceiling; all unknown lists empty.

| pole | open masks (direct / recursive) | boundary optimistic (direct / recursive / relaxed) | refined full (excluded / relaxed) | exact capacity checks |
|---|---|---|---|---:|
| l | 20148 (18299 / 1849) | 139326 (120294 / 18961 / 71) | 38 (35 / 3) | 9571719 |
| left mediant | 20148 (18299 / 1849) | 139326 (120294 / 18961 / 71) | 38 (35 / 3) | 9571719 |
| 22 | 20009 (17885 / 2124) | 138049 (117151 / 20826 / 72) | 39 (36 / 3) | 10875536 |
| right mediant | 20148 (18240 / 1908) | 139326 (120459 / 18796 / 71) | 38 (35 / 3) | 10127945 |
| u | 20148 (18240 / 1908) | 139326 (120459 / 18796 / 71) | 38 (35 / 3) | 10127945 |

Total 50274864 exact capacity checks over five actually executed slices; identical results at certain different slices are not deduplicated in this work count. Counts are not disjoint coverage counts across families. Each slice has exactly the same three relaxed full mask pairs as R248:
```json
[["33cf3303c4c003300cff3fd0","3cc30ccfc3b3ffccfc000c02f","33000000"],
 ["33cf3303c4c003300fff3fd0","3cc30ccfc3b3ffccfc000c02f","30000000"],
 ["33cf3303c4c003300fff3fd0","3cc30ccfc383ffccfc000c02f","300000030000000"]]
```
Independent exact decoding checked disjoint strict masks and zero indices [24,25,28,29], [28,29], [28,29,56,57] respectively. In all three, germs 28,29 are support 13, normal (74,0,-1), endpoints (1,9,74),(1,4,74), a nondegenerate projective interval. R238 forces factor 74t-D. In fact there is a stronger elementary tangent check: if Q=(u t+v D)M with v!=0, then at p18 the B coefficient of M, say beta, gives d=u beta and f=v beta. Hence if f!=0 the pole is -u/v. For support 13 the pole must be 74, which is outside [l,u]. Thus no such relaxed mask can be attained by a member of these slices with f!=0; the f=0 family is already closed by R248, and R238 also excludes the factor family directly. This uses zero germs, not isolated zero points. No need to assert that the relaxed capacity recursion itself has no feasible masks.

**Conclusion:** Under inherited necessary-wall and linear-suffix completeness premises, all nonzero Q with Q(p18)=0, f!=0 and
22207240/1009421 <= -d/f <= 1392445341/63292963
are excluded as the sole quadratic root of a depth-six correct decision tree. This is a full-dimensional open cone portion (with its two pole boundaries) in the five-dimensional single-anchor coefficient kernel, not merely a finite union of four-dimensional subspaces. It is a narrow interval, not global single-anchor closure. The three fixed event poles were checked separately and Theorem 1 transfers both open cells in full. General single-anchor kernel and unrestricted quadratic roots and internal unique quadratic remain open. K6 remains 1–2.

## Further author lemma: project individual candidate masks onto the pole axis
For an oriented full germ mask (positive, negative and zero germs), the coefficients attaining it form a convex cone with the zero vector excluded if any sign is strict. Indeed a lexicographically positive vector stays lex-positive under sums and positive rescaling: at the earliest of the two leading nonzero indices, the sum is positive. The same is true for lex-negative and the all-zero class is linear. Intersect the corresponding inverse images under the jet row maps. After normalizing f=1 the coefficient domain remains convex; its image s=-d is an interval (possibly empty, singleton, unbounded, or with nonincluded endpoints). This is not a claim that the union of relaxed-capacity feasible masks is convex. It suggests a more economical route than the 197869+ event sweep: use monotone suffix conflict subsets to enumerate only relevant masks, then compute their exact pole projections, with lexicographic boundary cases preserved. Exact projection algorithm and global closure not yet executed. For a fixed mask all first-nonzero choices are finite disjoint linear equalities/strict inequalities; feasible intervals may be computed by linear elimination and union. The oriented sign data, zero cases and original germ labels must remain intact.

## Reproduction of actual experiment

Read the full R247 note at the immutable pin above. Extract its first JavaScript block as string src. The following is the determinant experiment (the primary call was executed with event-set collection, the full call without storing all distinct events). No remote computation service or native spatial simulation required.
```javascript
const data=JSON.parse(src.match(/const data=(\[.*\]);/)[1]);
const abs=x=>x<0n?-x:x,gcd=(a,b)=>b?gcd(b,a%b):abs(a),
norm=v=>{let g=v.reduce(gcd,0n);return g?v.map(x=>x/(v.find(Boolean)<0n?-g:g)):v};
const parts=data.map(e=>e.normal.join()==="51,2,-1"?[[["1","9","69"],["3","17","187"]],[["2","5","112"],["1","0","51"]]]:e.normal.join()==="17,-1,0"?[[["0","0","1"],["1","17","391"]],[["1","17","69"],["1","17","22"]]]:[e.endpoints]).map(s=>s.map(pair=>pair.map(p=>norm(p.map(BigInt)))));
const full=new Map(),prim=new Map(),chart=[0n,0n,0n,0n,1n];
for(let m of [full,prim])m.set(chart.join(),chart);
for(let seg of parts)for(let [a,b] of seg)for(let [p,q] of [[a,b],[b,a]]){
 let [t,B,D]=p,[x,y,z]=q.map((v,j)=>v-p[j]);
 let rows=[[t*t,D*D,t*D,t*B,B*D],[2n*t*x,2n*D*z,t*z+D*x,t*y+B*x,B*z+D*y],[x*x,z*z,x*z,x*y,y*z]].filter(v=>v.some(Boolean));
 for(let v of rows){let w=norm(v);full.set(w.join(),w)}
 let w=norm(rows[0]);prim.set(w.join(),w)
}
const det3=(u,v,w,i,j,k)=>u[i]*(v[j]*w[k]-v[k]*w[j])-u[j]*(v[i]*w[k]-v[k]*w[i])+u[k]*(v[i]*w[j]-v[j]*w[i]);
function events(A,collect=false){
 let map=new Map(),lo=null,hi=null,equal=0,moving=0,constant=0,zero=0,visits=0;
 for(let i=0;i<A.length;i++)for(let j=i+1;j<A.length;j++)for(let k=j+1;k<A.length;k++){
  let u=A[i],v=A[j],w=A[k],b=det3(u,v,w,0,1,2);
  let cd=[-det3(u,v,w,1,2,3),det3(u,v,w,0,2,3),-det3(u,v,w,0,1,3),b],
      cf=[-det3(u,v,w,1,2,4),det3(u,v,w,0,2,4),-det3(u,v,w,0,1,4),b];
  for(let l=k+1;l<A.length;l++){
   let t=A[l],d=cd[0]*t[0]+cd[1]*t[1]+cd[2]*t[2]+cd[3]*t[3],
       f=cf[0]*t[0]+cf[1]*t[1]+cf[2]*t[2]+cf[3]*t[4];
   visits++;if(!d){if(!f)zero++;else constant++;continue}
   moving++;if(d<0n){d=-d;f=-f}
   if(collect){let g=gcd(f,d);map.set((f/g)+"/"+(d/g),[f/g,d/g])}
   let delta=f-22n*d;if(!delta){equal++;continue}
   if(delta<0n){if(!lo||f*lo[1]>lo[0]*d)lo=[f,d,i,j,k,l]}
   else if(!hi||f*hi[1]<hi[0]*d)hi=[f,d,i,j,k,l]
  }
 }
 const fmt=v=>{let g=gcd(v[0],v[1]);return {ratio:[String(v[0]/g),String(v[1]/g)],witness:v.slice(2)}};
 return {rows:A.length,visits,zero,constant,moving,equal,lower:fmt(lo),upper:fmt(hi),
 distinct:collect?map.size:null,positive:collect?[...map.values()].filter(([x])=>x>0n).length:null,
 negative:collect?[...map.values()].filter(([x])=>x<0n).length:null};
}
const primaryOut=events([...prim.values()],true),fullOut=events([...full.values()]);
```
Then execute five exact rank-four runs, using the original src each time:
```javascript
const old="[t*t,D*(D-12n*B),t*B,t*D],[2n*t*x,2n*D*z-12n*(B*z+D*y),t*y+B*x,t*z+D*x],[x*x,z*(z-12n*y),x*y,x*z]";
if(!src.includes(old))throw Error("patch mismatch");
for(let [num,den] of [[22n,1n],[22207262n,1009422n],[1392445363n,63292964n],[22207240n,1009421n],[1392445341n,63292963n]]){
 let neu=`[t*t,D*D,B*(${den}n*D-${num}n*t),t*D],[2n*t*x,2n*D*z,B*(${den}n*z-${num}n*x)+y*(${den}n*D-${num}n*t),t*z+D*x],[x*x,z*z,y*(${den}n*z-${num}n*x),x*z]`;
 let v=src.replace(old,neu).replace('rank4("two_anchor_kernel",[])','rank4("pole_'+num+'_'+den+'",[])').replace(/experiment\(data\)\s*$/,"return experiment(data)");
 const o=Function(v)();
 if(o.points!==51||o.germs!==98||o.linearPartitions!==2225)throw Error("frozen dimensions");
 const a=o.result;for(let stage of [a.open,a.boundaryOptimistic,a.refined])if(stage.unknown.length)throw Error("unresolved cutoff");
 if(a.open.survivors.length||a.refined.survivors.length!==3)throw Error("unexpected frontier");
 for(let [x,y] of a.refined.survivors){
  let A=BigInt("0x"+x),B=BigInt("0x"+y),Z=((1n<<98n)-1n)^(A|B);
  if(A&B||(Z&(3n<<28n))!==(3n<<28n))throw Error("support-13 zero certificate");
 }
 // a includes full coverage counts, all refined survivor masks and intermediate provenance.
}
```
The determinant code above is a consolidated reproduction of the two actually executed loops; the exact values and counts recorded above are their actual outputs. Rank-four patches were executed for all five rational poles, and zero masks independently decoded. No independent review or Lean validation claimed. Next: avoid repeating the interval and fixed slices; prioritize exact conflict-mask projection or global rank-five primary face recursion with monotone capacity certificates instead of enumerating hundreds of thousands of full slices.
