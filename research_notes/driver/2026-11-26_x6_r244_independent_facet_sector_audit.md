# X6 R244 — independent full-row facet-sector audit
2026-11-26; RESEARCH_DRIVER lane. Original author R2, 0d22bde873e96277d20f5b6c46ac83b3acd6a8d5:research_notes/portable_direct/2026-11-26_r2_x6_r244_first_active_row_quadratic_families.md, blob f94419a5604912d6bf442f72df336043b955a2b3. Shared frozen input and prior proof exposure, independent mathematical argument and independently implemented exact enumeration, not blind discovery or an assertion of native reviewer independence. Port 10, 1935 integer directions, six-pair BRC, positive (17t,B,22t,D), strict 3/2 near set, legal optimizer, 47 support labels, 49 components, 51 endpoint rays, 98 directed germs unchanged. Inherited necessary-wall and suffix-relaxation lemmas are premises; this audit does not redo their derivation.

## Argument
For a coefficient subspace W, ordered jet rows restricted to W are linear forms. Away from the kernels of their first nonzero restrictions, each germ sign is constant on chambers. On a kernel recurse with the full ordered jets restricted to that kernel. Dimension strictly decreases, and identically zero germs stay zero. This proves the first-active-row coverage theorem, in arbitrary finite dimension, independently of the enumeration.

Alternative rank-three enumeration: take every nonzero jet row as a plane normal, quotient proportional normals only for geometric enumeration. Their span is R^3 in each tested family. For each plane h-perp, intersect all distinct other planes to get lines, represent each by two opposite primitive integer rays, sort around the plane using a reference ray u, v=h cross u, the half-plane determined by dot(v,p), dot(u,p), and the sign of h dot (a cross b). Essential rank implies at least two distinct lines on each plane. Adjacent rays enclose an angle strictly between 0 and pi. Their sum q=a+b lies strictly inside that sector. Evaluate the full ordered jets at each ray, q, q+epsilon*h, q-epsilon*h (positive infinitesimal). For q all distinct other planes are off their kernels; hence their sign is preserved by sufficiently small epsilon, and the selected plane sign is resolved. Every full-dimensional chamber has a 2D facet, each contains an open sector of this arrangement. Every nonzero 1D and 2D face is visited. Thus full rank-three coefficient space is covered. At each jet row, evaluate dot(row,q) then dot(row,perturbation) if zero, before proceeding to the next jet row. Exact integer signs; no floating-point tests. Branch reversal identification valid because both suffix branches have identical feasibility requirements.

Use independent full-row enumeration for the linear bank too. Recurrence on tagged germ subset s and remaining depth d: c(s) counts distinct support labels. Fail if c(s)>2^d-1, pass if c(s)<=d (sequential support tests in relaxation), else examine all linear masks or only support masks at equality c(s)=2^d-1. Saturation forces elimination of a whole support label; this is inherited necessary-wall lemma. For a candidate query intersect both strict masks with s, require each child count <=2^(d-1)-1, recurse. Memoize full s and d. A false child proves actual root impossible; a true child only passes the relaxation. Zero germs are relaxed away, not treated as proof of output. No cutoff.

## Actual computation
Independent exact BigInt implementation executed in Code Mode; no budget cutoff. Output:
```json
{"points":51,"germs":98,"linearPartitions":2225,"linearRows":92,"totalChecks":2469916,"totalCalls":3667,"families":[{"name":"diagonal","rows":156,"edgeVisits":44332,"sectorVisits":44332,"partitions":2279,"zero":19,"direct":1918,"excluded":361,"survivors":[],"checks":1202628,"calls":1898},{"name":"off_diagonal","rows":158,"edgeVisits":47504,"sectorVisits":47504,"partitions":2148,"zero":19,"direct":1779,"excluded":369,"survivors":[],"checks":892890,"calls":1365},{"name":"t_squared_two_crosses","rows":153,"edgeVisits":41450,"sectorVisits":41450,"partitions":1995,"zero":18,"direct":1741,"excluded":254,"survivors":[],"checks":374398,"calls":404}]}
```
All per-family partition, zero, direct, recursive and survivor counts match the author's pinned result. All 6422 family-local masks excluded (5438 immediate, 984 recursive); no claim of distinctness across families. Source order and cache implementation differ; scan counts need not match. The three entire real coefficient families are excluded as sole quadratic root followed by arbitrary linear suffix, conditional on inherited premises. General K6 in [1,2], general six-coefficient quadratic and internal placement remain open.

## Exact reproduction recipe
Use the pinned source's literal data array and component splits for normals (51,2,-1) and (17,-1,0); generate oriented endpoint germs, tags, and linear/monomial jet rows as in the source. For geometric bank replace its partitions/fullPartitions routines with:
```javascript
// vectors and dot/cross use BigInt; unique canonicalizes nonzero vectors up to sign and gcd.
function bank(rows){
 const H=unique(rows.flat()),out=new Map();
 function put(q,w=null){
  let a=0n,b=0n;
  for(let i=0;i<rows.length;i++){
   let z=0;for(let r of rows[i]){z=sg(dot(r,q));if(!z&&w)z=sg(dot(r,w));if(z)break}
   if(z>0)a|=germs[i].bit;else if(z<0)b|=germs[i].bit
  }
  if(a>b)[a,b]=[b,a];out.set(a+","+b,[a,b]);
 }
 for(let h of H){
  const rays=unique(H.map(k=>cross(h,k)));if(rays.length<2)throw Error("rank2 plane");
  const u=rays[0],v=cross(h,u);
  const half=p=>{let y=dot(v,p),x=dot(u,p);return y>0n||(y===0n&&x>=0n)?0:1};
  const circle=rays.flatMap(p=>[p,p.map(x=>-x)]);
  circle.sort((a,b)=>half(a)-half(b)||-sg(dot(h,cross(a,b))));
  for(let i=0;i<circle.length;i++){
   const a=circle[i],b=circle[(i+1)%circle.length],q=a.map((x,j)=>x+b[j]);
   if(dot(h,cross(a,b))<=0n||!q.some(Boolean))throw Error("invalid sector");
   put(a);put(q);put(q,h);put(q,h.map(x=>-x));
  }
 }
 return [...out.values()];
}
```
Input germ construction: primitive positive rays p and q; two germs with (u,v)=(p,q-p),(q,p-q), each with its own bit and shared support tag. Linear jet rows [u,v]; for monomial x_i*x_j use rows u_i*u_j, u_i*v_j+u_j*v_i, v_i*v_j. For each coefficient family build bank independently. For recurrence order support masks first, then deduplicated full linear masks, cache count and can(s,d); examine root masks in bank insertion order, first reject if either count >31; otherwise apply can(a,5)&&can(b,5). Full proof, original data and reproduction recipe retained. Next: other rank-three coefficient supports and capacity conflicts for dimension six.
