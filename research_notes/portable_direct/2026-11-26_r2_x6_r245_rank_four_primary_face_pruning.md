# X6 R245 — four-coefficient quadratic root exclusion via primary-face optimistic pruning

2026-11-26. Author mathematical proof and exact BigInt computation, NOT_REVIEWED. Independent informed TASK_RESEARCH. Native X6 lookup r2-20261126-2314-x6-read returned BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false; current owner and researcher binding unconfirmed. No CLAIM, shared state mutation or formal Result. Independent non-overwriting science only under docs/RESEARCH_CONSOLE_FALLBACK.md.

Frozen source: R244 0d22bde873e96277d20f5b6c46ac83b3acd6a8d5:research_notes/portable_direct/2026-11-26_r2_x6_r244_first_active_row_quadratic_families.md. Reuse its 47 tagged supports, 49 components, 51 endpoint rays, 98 germs, exact 2225 linear suffix masks, Port 10, 1935 directions, six-pair BRC, positive (17t,B,22t,D), strict 3/2 near set and legal optimizer. Inherited necessary-wall and linear suffix completeness premises retained. All coefficient coordinates are auxiliary, not native X6 spatial coordinates. No change to P000 V5, joint-relation observer preservation, or native dynamics.

## Theorems and proof

Let a finite homogeneous coefficient space have nonzero primary evaluation rows at all germ starts, and let these rows span the coefficient space. For any coefficient vector, the primary sign mask fixes the strict sign of every germ whose primary row is nonzero there. Drop only germs with zero primary evaluation in an optimistic relaxation; this is NOT a claim of their redundancy. Any complete germ sign mask refines the partial strict masks by adding germs. The pure-linear suffix feasibility predicate is hereditary under deleting tagged germs: restrict a witness tree, preserving signs and labels; no capacity can increase. Therefore if either optimistic strict branch is infeasible, every full jet completion of that primary face is infeasible. If both pass, resolve the full jets on the flat defined by all zero primary rows and retain only masks whose primary signs coincide with that face (up to branch swap). This is an exact finite elimination of primary faces for purposes of the germ relaxation; a surviving full mask is not a correct output tree.

For rank four, use the pointed central primary arrangement. Every full-dimensional chamber has a facet in some primary hyperplane: its closure is full-dimensional polyhedral, pointed since rows span, and has facets. A point in the relative interior of that facet lies off all nonproportional primary hyperplanes. Perturbing it to either side of the hyperplane preserves all other strict signs, hence both adjacent chambers are recovered. Every boundary coefficient lies in at least one primary hyperplane. Within each hyperplane the restricted rows span rank three, since restriction maps the full row span surjectively onto the dual of the hyperplane. Enumerate all restricted faces up to sign using the R244 rank-three extreme ray/incident tangent flag method. Explicitly for each intersection ray v, each incident normal r, take v, (v,+/- v cross r), (v,+/- v cross r,+/- r). This covers all faces: pointed chamber closures have an extreme ray, local tangent arrangement is rank two, and each sector has a bounding ray; its remaining vanishing rows are parallel to r. Use the projection basis h[p] e_i - h[i] e_p (i != p) for hyperplane h=0. Canonical sign normalization of restricted rows must preserve positive/negative group membership. All original primary rows here are nonnegative and nonzero, so the group of rows proportional to h has uniform sign when perturbing off h. Antipodal masks swap the two branches, harmless only for this symmetric capacity test.

For a surviving boundary face, intersect zero primary kernels by successive exact basis elimination B_i <- v_p B_i - v_i B_p where v_i=h(B_i), deleting pivot p. This spans exactly the desired intersection. On the resulting flat enumerate ALL nonzero jet rows (not just primary rows), using the complete arrangement of rank d=1,2,3. Rank one needs one representative modulo global sign. Rank two has event rays perpendicular to each nonzero row and adjacent sectors obtained by perturbing along that row. Rank three uses the same extreme-ray flags. Full restricted rows span since primary rows already span the dual of the flat. Evaluate each original jet in germ-order, taking the first nonzero lex direction evaluation within a row; evaluate primary masks separately and filter exactly to the original face. The full jet mask retains all zero/high-order residuals. The finite mask bank is complete for the specified four-dimensional coefficient family. Enumeration of masks does not itself establish correctness of output decisions; exclusion uses inherited necessary-wall relaxation.

## Actual exact output

```json
{"points":51,"germs":98,"linearPartitions":2225,"result":{"name":"diagonal_plus_tB","monos":[[0,0],[1,1],[2,2],[0,1]],"primary":51,"rayVisits":42097,"edgeVisits":171228,"facetVisits":342456,"open":{"total":14878,"direct":14211,"excluded":667,"survivors":[],"unknown":[],"checks":1800672},"boundaryOptimistic":{"total":99964,"direct":92554,"excluded":7361,"survivors":[["12cb3000aeea29300affc030","3ed30cfed000180cfb000314f",26,25,[6,"ray"]],["12cb3000aeea29300affc030","3ed30cfef000180cfb0003b4f",26,25,[6,"edge"]],["31caa3032e68080220fffa30","3ce315cec8003a1dd9800014f",26,27,[6,"ray"]],["31caa3032ee8082222fffa30","3ce315cec8003a1dd9800014f",28,27,[6,"edge"]],["33ca2202aee8082002fffa30","3cc31cded0003a1dfb000014f",26,25,[6,"ray"]],["33ca3202aee808200afffa30","3cc31cded0003a1dfb000014f",27,25,[6,"edge"]],["33ca2202aee8082002fffa30","3cc31dcec0003a1dd9800014f",26,25,[6,"ray"]],["33ca3202aee808200afffa30","3cc30cded0003a0cfb000014f",27,23,[6,"ray"]],["12cb3000aeea29300affc030","3ed30cfef000100cfb0003b4f",26,24,[6,"ray"]],["12cb3000aeeaa9300affc030","3ed30cfef000100cfb0003b4f",27,24,[6,"edge"]],["20b3000aeaaa9300affc030","3fdb0cfef000100cfb0003b4f",25,25,[6,"ray"]],["24b3000aeeaa9300affc030","3fdb0cfef000100cfb0003b4f",26,25,[6,"edge"]],["31caa3032ee8082222fffa30","3cc315cec0003a1dd9800014f",28,25,[6,"ray"]],["24b3000aeeaa9300affc030","3fd30cfef000100cfb0003b4f",26,24,[6,"ray"]],["2cb3000aeeaa9300affc030","3fd30cfef000100cfb0003b4f",26,24,[6,"edge"]],["2cb3000aeeaa9300affc030","3ed30cfef000100cfb0003b4f",26,24,[6,"ray"]],["32cb3000aeea29300affc030","3cc34cfed000182cfb00025cf",26,25,[7,"ray"]],["32cb3000aeea29300affc030","3cd34cfed000182cfb00035cf",26,26,[7,"edge"]],["33ca3000aee808200afff030","3cc34cfed0003a2cfb00005cf",24,26,[7,"ray"]],["33cb3000aee809300afff030","3cc34cfed0003a2cfb00005cf",25,26,[7,"edge"]],["33cb3000aee809300afff030","3cc34cfed000182cfb00005cf",25,25,[7,"ray"]],["12cb3000aeea29300affc030","3cd34cfed000182cfb00035cf",26,26,[7,"ray"]],["32cb3000aeea29300affc030","3cc34cfef000182cfb0002fcf",26,25,[8,"edge"]],["32cb3000aeea29300affc030","3cc34cfef000182cfb0000fcf",26,25,[8,"ray"]],["32cb3000aee809300affe030","3cc34cfef000182cfb0000fcf",25,25,[8,"ray"]],["32cb3000aeea29300affc030","3cd34cfef000182cfb0001fcf",26,26,[9,"edge"]],["32cb3000aee809300affc030","3cd34cfef000182cfb0001fcf",24,26,[9,"ray"]],["33ca2202aee8082002fffa30","3cc35dcec0003a3dd980005cf",26,27,[18,"edge"]],["33ca3202aee808200afffa30","3cc34cded0003a2cfb00005cf",27,26,[18,"edge"]],["12cb3000aeeaa9300affc030","3ed34cfef000102cfb0003fcf",27,26,[18,"facet"]],["12cb3000aeea29300affc030","3ed34cfef000102cfb0003fcf",26,26,[18,"edge"]],["31caa3032ee8082222fffa30","3cc355cec0003a3dd980005cf",28,27,[18,"edge"]],["2cb3000aeeaa9300affc030","3fd34cfef000102cfb0003fcf",26,26,[18,"facet"]],["24b3000aeeaa9300affc030","3fd34cfef000102cfb0003fcf",26,26,[18,"edge"]],["2cb3000aeeaa9300affc030","3ed34cfef000102cfb0003fcf",26,26,[18,"edge"]],["32cb3000aeea29300affc030","3cd34cfef000182cfb0003fcf",26,26,[18,"facet"]],["33ca3002aee808200afffa30","3cc34cfed0003a2cfb00005cf",26,26,[18,"edge"]],["33cb3000aee809300afff030","3cc34cfef000182cfb0000fcf",25,25,[18,"edge"]],["12cb3000aeea29300affc030","3cd34cfef000182cfb0003fcf",26,26,[18,"edge"]],["32cb3000aee809300affe030","3cd34cfef000182cfb0001fcf",25,26,[18,"edge"]],["32cb3000aee809300affc030","3cd34cfef000182cfb0003fcf",24,26,[18,"edge"]],["31ca22022ee8082002fffa30","3cc35dcec0003a3dd980005cf",25,27,[18,"ray"]],["31ca23032ee8082222fffa30","3cc35dcec0003a3dd980005cf",27,27,[18,"edge"]],["33ca3002aee808200afffa30","3cc34cded0003a2cfb00005cf",26,26,[18,"ray"]],["12cb3000aee809300affc030","3cd34cfef000182cfb0003fcf",24,26,[18,"ray"]],["24b3000aeea29300affc030","3fd34cfef000102cfb0003fcf",25,26,[18,"ray"]],["2cb3000aeea29300affc030","3fd34cfef000102cfb0003fcf",25,26,[18,"edge"]],["2cb3000aeea29300affc030","3ed34cfef000102cfb0003fcf",25,26,[18,"ray"]],["31ca23032ee8082222fffa30","3cc355cec0003a3dd980005cf",27,27,[18,"ray"]]],"unknown":[],"checks":3071920},"refined":{"total":33,"direct":10,"excluded":23,"survivors":[],"unknown":[],"checks":33516},"dimHist":{"1":23,"2":23,"3":3},"details":[["12cb3000aeea29300affc030","3ed30cfed000180cfb000314f",1,1],["12cb3000aeea29300affc030","3ed30cfef000180cfb0003b4f",2,2],["31caa3032e68080220fffa30","3ce315cec8003a1dd9800014f",1,1],["31caa3032ee8082222fffa30","3ce315cec8003a1dd9800014f",2,1],["33ca2202aee8082002fffa30","3cc31cded0003a1dfb000014f",1,1],["33ca3202aee808200afffa30","3cc31cded0003a1dfb000014f",2,1],["33ca2202aee8082002fffa30","3cc31dcec0003a1dd9800014f",1,1],["33ca3202aee808200afffa30","3cc30cded0003a0cfb000014f",1,1],["12cb3000aeea29300affc030","3ed30cfef000100cfb0003b4f",1,1],["12cb3000aeeaa9300affc030","3ed30cfef000100cfb0003b4f",2,1],["20b3000aeaaa9300affc030","3fdb0cfef000100cfb0003b4f",1,1],["24b3000aeeaa9300affc030","3fdb0cfef000100cfb0003b4f",2,1],["31caa3032ee8082222fffa30","3cc315cec0003a1dd9800014f",1,1],["24b3000aeeaa9300affc030","3fd30cfef000100cfb0003b4f",1,1],["2cb3000aeeaa9300affc030","3fd30cfef000100cfb0003b4f",2,1],["2cb3000aeeaa9300affc030","3ed30cfef000100cfb0003b4f",1,1],["32cb3000aeea29300affc030","3cc34cfed000182cfb00025cf",1,1],["32cb3000aeea29300affc030","3cd34cfed000182cfb00035cf",2,2],["33ca3000aee808200afff030","3cc34cfed0003a2cfb00005cf",1,1],["33cb3000aee809300afff030","3cc34cfed0003a2cfb00005cf",2,1],["33cb3000aee809300afff030","3cc34cfed000182cfb00005cf",1,1],["12cb3000aeea29300affc030","3cd34cfed000182cfb00035cf",1,1],["32cb3000aeea29300affc030","3cc34cfef000182cfb0002fcf",2,2],["32cb3000aeea29300affc030","3cc34cfef000182cfb0000fcf",1,1],["32cb3000aee809300affe030","3cc34cfef000182cfb0000fcf",1,1],["32cb3000aeea29300affc030","3cd34cfef000182cfb0001fcf",2,2],["32cb3000aee809300affc030","3cd34cfef000182cfb0001fcf",1,1],["33ca2202aee8082002fffa30","3cc35dcec0003a3dd980005cf",2,1],["33ca3202aee808200afffa30","3cc34cded0003a2cfb00005cf",2,1],["12cb3000aeeaa9300affc030","3ed34cfef000102cfb0003fcf",3,1],["12cb3000aeea29300affc030","3ed34cfef000102cfb0003fcf",2,1],["31caa3032ee8082222fffa30","3cc355cec0003a3dd980005cf",2,1],["2cb3000aeeaa9300affc030","3fd34cfef000102cfb0003fcf",3,1],["24b3000aeeaa9300affc030","3fd34cfef000102cfb0003fcf",2,1],["2cb3000aeeaa9300affc030","3ed34cfef000102cfb0003fcf",2,1],["32cb3000aeea29300affc030","3cd34cfef000182cfb0003fcf",3,1],["33ca3002aee808200afffa30","3cc34cfed0003a2cfb00005cf",2,1],["33cb3000aee809300afff030","3cc34cfef000182cfb0000fcf",2,1],["12cb3000aeea29300affc030","3cd34cfef000182cfb0003fcf",2,1],["32cb3000aee809300affe030","3cd34cfef000182cfb0001fcf",2,1],["32cb3000aee809300affc030","3cd34cfef000182cfb0003fcf",2,1],["31ca22022ee8082002fffa30","3cc35dcec0003a3dd980005cf",1,1],["31ca23032ee8082222fffa30","3cc35dcec0003a3dd980005cf",2,1],["33ca3002aee808200afffa30","3cc34cded0003a2cfb00005cf",1,1],["12cb3000aee809300affc030","3cd34cfef000182cfb0003fcf",1,1],["24b3000aeea29300affc030","3fd34cfef000102cfb0003fcf",1,1],["2cb3000aeea29300affc030","3fd34cfef000102cfb0003fcf",2,1],["2cb3000aeea29300affc030","3ed34cfef000102cfb0003fcf",1,1],["31ca23032ee8082222fffa30","3cc355cec0003a3dd980005cf",1,1]],"totalChecks":4906108}}
```

The tested family is Q=a t²+b B²+c D²+d tB with arbitrary real a,b,c,d not all zero. Nonzero coefficient vectors are classified up to global sign only. Generic primary chambers are all excluded. Boundary refinement result above determines whether the entire family is excluded. Unknown computation statuses (if any) are never counted as exclusions. The proof does not cover all six coefficients or internal placement. Next: use the primary-face prune on larger coefficient spaces (recursive hyperplane restriction with shared flats and mask conflict caching); alternatively apply to other four-term families. Full unrestricted K6 remains 1–2.

## Complete reproducible source (R244 exact inputs and suffix kernel plus R245 extension)

```javascript
function experiment(data){
 const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],abs=x=>x<0n?-x:x,gcd=(a,b)=>b?gcd(b,a%b):abs(a),nz=a=>a.some(Boolean),sg=x=>x>0n?1:x<0n?-1:0,scale=(a,c)=>a.map(x=>x*c),norm=(a,un=false)=>{let g=a.reduce(gcd,0n);return g?a.map(x=>x/(un&&a.find(Boolean)<0n?-g:g)):a},sub=(a,b)=>a.map((x,i)=>x-b[i]);
 const N=data.map(e=>e.normal.map(BigInt)),parts=data.map(e=>e.normal.join()==="51,2,-1"?[[["1","9","69"],["3","17","187"]],[["2","5","112"],["1","0","51"]]]:e.normal.join()==="17,-1,0"?[[["0","0","1"],["1","17","391"]],[["1","17","69"],["1","17","22"]]]:[e.endpoints]).map(s=>s.map(pair=>pair.map(p=>p.map(BigInt))));
 let P=[],idx=new Map(),G=[],tag=Array(47).fill(0n);
 function id(p){p=norm(p);let k=p.join();if(!idx.has(k)){idx.set(k,P.length);P.push(p)}return idx.get(k)}
 for(let k=0;k<parts.length;k++)for(let [a,b] of parts[k]){if(dot(N[k],a)||dot(N[k],b))throw Error("endpoint");let u=id(a),v=id(b);if(u===v)throw Error("degenerate");for(let [i,j] of [[u,v],[v,u]]){let bit=1n<<BigInt(G.length);G.push([i,j,bit]);tag[k]|=bit;}}
 if(P.length!==51||G.length!==98)throw Error("dimensions");
 const ALL=(1n<<BigInt(G.length))-1n;
 const canon=(a,b)=>a<b?[a,b]:[b,a];
 function signJet(rows,vs){for(let r of rows){for(let v of vs){let z=sg(dot(r,v));if(z)return z}}return 0}
 function mask(rows,vs){let a=0n,b=0n;for(let i=0;i<rows.length;i++){let z=signJet(rows[i],vs);if(z>0)a|=G[i][2];else if(z<0)b|=G[i][2]}return canon(a,b)}
 function uniqueRays(xs){let m=new Map();for(let x of xs)if(nz(x)){let v=norm(x,true);m.set(v.join(),v)}return [...m.values()]}
 // First-active-row arrangement, plus exact recursion inside each event hyperplane.
 function partitions(rows){
  const first=rows.map(rs=>rs.find(nz)||[0n,0n,0n]),prim=uniqueRays(first);
  if(!prim.some(a=>prim.some(b=>prim.some(c=>dot(cross(a,b),c)))))throw Error("primary rank not three");
  let raw=[];for(let i=0;i<prim.length;i++)for(let j=i+1;j<prim.length;j++)raw.push(cross(prim[i],prim[j]));
  const rays=uniqueRays(raw),out=new Map();let openVisits=0,boundaryVisits=0;
  function add(rs,vs,stage){let [a,b]=mask(rs,vs);let key=a+","+b;if(!out.has(key))out.set(key,{a,b,vs});if(stage===0)openVisits++;else boundaryVisits++}
  for(let v of rays)for(let r of prim)if(!dot(v,r)){let w=cross(v,r);for(let e of [-1n,1n])for(let f of [-1n,1n])add(first.map(x=>[x]),[v,scale(w,e),scale(r,f)],0)}
  const openMasks=out.size;
  for(let r of prim){
   let cuts=uniqueRays(rows.map(rs=>{let s=rs.find(x=>nz(cross(r,x)));return s?cross(r,s):[0n,0n,0n]}));
   if(!cuts.length){let v=[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]].map(x=>cross(r,x)).find(nz);add(rows,[v],1);continue}
   for(let v of cuts){let w=cross(r,v);add(rows,[v],1);add(rows,[v,w],1);add(rows,[v,scale(w,-1n)],1)}
  }
  return {bank:[...out.values()],primary:prim.length,rays:rays.length,openMasks,openVisits,boundaryVisits};
 }
 // Independent full-row arrangement (same exact perturbation principle).
 function fullPartitions(rows){
  let prim=uniqueRays(rows.flat()),raw=[];for(let i=0;i<prim.length;i++)for(let j=i+1;j<prim.length;j++)raw.push(cross(prim[i],prim[j]));
  let rays=uniqueRays(raw),out=new Set();
  function add(vs){let [a,b]=mask(rows,vs);out.add(a+","+b)}
  for(let v of rays){add([v]);for(let r of prim)if(!dot(v,r)){let w=cross(v,r);for(let e of [-1n,1n]){let u=scale(w,e);add([v,u]);for(let f of [-1n,1n])add([v,u,scale(r,f)])}}}
  return {keys:out,rows:prim.length,rays:rays.length};
 }
 const linrows=G.map(([u,v])=>[P[u],sub(P[v],P[u])]);
 const linear=partitions(linrows);
 if(linear.bank.length!==2225)throw Error("linear bank "+linear.bank.length);
 const S=N.map(n=>mask(linrows,[n])),Q=linear.bank.map(x=>[x.a,x.b]);
 const ordered=[...new Map([...S,...Q].map(([a,b])=>[a+","+b,[a,b]])).values()];
 const cc=new Map();function count(s){let n=cc.get(s);if(n!==undefined)return n;n=0;for(let t of tag)if(t&s)n++;if(cc.size<350000)cc.set(s,n);return n}
 const memo=Array.from({length:6},()=>new Map());let checks=0,ceiling=0,CUT={};
 function can(s,d){if(!s)return true;let c=count(s);if(c>2**d-1)return false;if(c<=d)return true;if(memo[d].has(s))return memo[d].get(s);let bank=c===2**d-1?S:ordered,cap=2**(d-1)-1;for(let [a,b] of bank){if(checks>=ceiling)throw CUT;checks++;let x=a&s,y=b&s,cx=count(x),cy=count(y);if(cx>cap||cy>cap)continue;if(cx<cy)[x,y]=[y,x];if(can(x,d-1)&&can(y,d-1)){memo[d].set(s,true);return true}}memo[d].set(s,false);return false}
 function actual(rows,vs){let max=0n;for(let r of rows.flat())for(let v of vs){let z=abs(dot(r,v));if(z>max)max=z}let m=2n*max+2n;let q=[0n,0n,0n];for(let v of vs)q=q.map((x,i)=>x*m+v[i]);return norm(q)}
 function family(name,monos){
  let rows=G.map(([u,v])=>{let a=P[u],b=sub(P[v],a);return [0,1,2].map(t=>monos.map(([i,j])=>t===0?a[i]*a[j]:t===1?a[i]*b[j]+a[j]*b[i]:b[i]*b[j]))});
  let p=partitions(rows),full=fullPartitions(rows),keys=new Set(p.bank.map(({a,b})=>a+","+b));
  let missing=[...full.keys].filter(k=>!keys.has(k)).length,extra=[...keys].filter(k=>!full.keys.has(k)).length;
  if(missing||extra)throw Error("arrangement mismatch "+name+" "+missing+" "+extra);
  let direct=0,excluded=0,zero=0,survivors=[],unknown=[],before=checks;
  ceiling=checks+2500000;
  for(let {a,b,vs} of p.bank){
   if((a|b)!==ALL)zero++;
   if(count(a)>31||count(b)>31){direct++;continue}
   let status;
   try{status=can(a,5)&&can(b,5)?"survive":"exclude"}catch(err){if(err!==CUT)throw err;status="unknown"}
   if(status==="exclude"){excluded++;continue}
   let q=actual(rows,vs);let [x,y]=mask(rows,[q]);if(x!==a||y!==b)throw Error("witness mismatch");
   (status==="survive"?survivors:unknown).push({a:a.toString(16),b:b.toString(16),q:q.map(String),counts:[count(a),count(b)]});
  }
  if(direct+excluded+survivors.length+unknown.length!==p.bank.length)throw Error("coverage");
  return {name,monos,primaryRows:p.primary,primaryRays:p.rays,openMasks:p.openMasks,openVisits:p.openVisits,boundaryVisits:p.boundaryVisits,fullRows:full.rows,fullRays:full.rays,partitions:p.bank.length,zeroMasks:zero,direct,excluded,survivors,unknown,checks:checks-before};
 }

function rank4(name,monos){
 const groups=new Map(),dotN=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n);
 for(let [u,v,bit] of G){let p=P[u],h=norm(monos.map(([i,j])=>p[i]*p[j]),true),k=h.join();if(!nz(h))throw Error("missing primary");if(!groups.has(k))groups.set(k,{h,bits:0n});groups.get(k).bits|=bit}
 const H=[...groups.values()],open=new Map(),faces=new Map();
 function add(map,a,b,info){[a,b]=canon(a,b);let k=a+","+b;if(!map.has(k))map.set(k,{a,b,info})}
 let rayVisits=0,edgeVisits=0,facetVisits=0;
 for(let z=0;z<H.length;z++){
  let {h,bits:zero}=H[z],p=h.findIndex(Boolean),ix=[0,1,2,3].filter(i=>i!==p);
  let rs=new Map();
  for(let {h:s,bits} of H){let x=ix.map(i=>h[p]*s[i]-h[i]*s[p]);if(!nz(x))continue;let y=norm(x,true),k=y.join();if(!rs.has(k))rs.set(k,{r:y,pos:0n,neg:0n});rs.get(k)[x.find(Boolean)>0n?"pos":"neg"]|=bits}
  let A=[...rs.values()],raw=[];
  for(let i=0;i<A.length;i++)for(let j=i+1;j<A.length;j++)raw.push(cross(A[i].r,A[j].r));
  let rays=uniqueRays(raw);if(!rays.some(v=>A.some(({r})=>dot(v,r))))throw Error("restriction rank");
  function put(a,b,g,s){return s>0?[a|g.pos,b|g.neg]:s<0?[a|g.neg,b|g.pos]:[a,b]}
  for(let v of rays){
   let a=0n,b=0n,Z=[];
   for(let g of A){let s=sg(dot(v,g.r));if(!s)Z.push(g);else [a,b]=put(a,b,g,s)}
   add(faces,a,b,[z,"ray"]);rayVisits++;
   for(let g of Z){let w=cross(v,g.r);
    for(let e of [-1,1]){
     let c=a,d=b,T=[];
     for(let j of Z){let s=e*sg(dot(w,j.r));if(!s)T.push(j);else [c,d]=put(c,d,j,s)}
     add(faces,c,d,[z,"edge"]);edgeVisits++;
     for(let f of [-1,1]){
      let x=c,y=d;for(let j of T){let s=f*sg(dot(g.r,j.r));if(!s)throw Error("nonopen");[x,y]=put(x,y,j,s)}
      if((x|y)!==(ALL^zero))throw Error("facet incomplete");
      add(faces,x,y,[z,"facet"]);facetVisits++;
      add(open,x|zero,y,[z]);add(open,x,y|zero,[z]);
     }
    }
   }
  }
 }
 let start=checks;ceiling=checks+12000000;
 function classify(map){let direct=0,excluded=0,survivors=[],unknown=[];let before=checks;
  for(let {a,b,info} of map.values()){
   if(count(a)>31||count(b)>31){direct++;continue}
   try{if(can(a,5)&&can(b,5))survivors.push([a.toString(16),b.toString(16),count(a),count(b),info]);else excluded++}catch(err){if(err!==CUT)throw err;unknown.push([a.toString(16),b.toString(16),info])}
  }
  return {total:map.size,direct,excluded,survivors,unknown,checks:checks-before}
 }
 const o=classify(open),f=classify(faces);
 const jets=G.map(([u,v])=>{let a=P[u],b=sub(P[v],a);return [0,1,2].map(t=>monos.map(([i,j])=>t===0?a[i]*a[j]:t===1?a[i]*b[j]+a[j]*b[i]:b[i]*b[j]))});
 let refined=new Map(),dimHist={},details=[];
 for(let [aa,bb] of f.survivors){
  let a=BigInt("0x"+aa),b=BigInt("0x"+bb),z=ALL^(a|b);
  let B=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>i===j?1n:0n));
  for(let {h,bits} of H)if(bits&z){
   if((bits&z)!==bits)throw Error("partial group");
   let v=B.map(x=>dotN(h,x)),p=v.findIndex(Boolean);
   if(p>=0)B=B.flatMap((x,i)=>i===p?[]:[norm(x.map((y,j)=>v[p]*y-v[i]*B[p][j]))]);
  }
  const d=B.length;dimHist[d]=(dimHist[d]||0)+1;if(d<1||d>3)throw Error("bad flat rank");
  const rows=jets.map(rs=>rs.map(h=>B.map(x=>dotN(h,x))));
  const dimDot=dotN;
  function addV(vs){
   let p=0n,q=0n,x=0n,y=0n;
   for(let i=0;i<rows.length;i++){
    let sign=0;for(let v of vs){sign=sg(dimDot(rows[i][0],v));if(sign)break}
    if(sign>0)p|=G[i][2];else if(sign<0)q|=G[i][2];
    let s=0;for(let h of rows[i]){for(let v of vs){s=sg(dimDot(h,v));if(s)break}if(s)break}
    if(s>0)x|=G[i][2];else if(s<0)y|=G[i][2];
   }
   let [i,j]=canon(p,q);if(i!==a||j!==b)return;
   [x,y]=canon(x,y);local.add(x+","+y);add(refined,x,y,[aa,bb]);
  }
  let local=new Set();
  if(d===1)addV([[1n]]);
  else if(d===2){
   let rs=uniqueRays(rows.flat());for(let h of rs){let v=[-h[1],h[0]];addV([v]);addV([v,h]);addV([v,scale(h,-1n)])}
  }else{
   let rs=uniqueRays(rows.flat()),raw=[];
   for(let i=0;i<rs.length;i++)for(let j=i+1;j<rs.length;j++)raw.push(cross(rs[i],rs[j]));
   for(let v of uniqueRays(raw)){addV([v]);for(let h of rs)if(!dot(v,h)){let w=cross(v,h);for(let e of [-1n,1n]){let u=scale(w,e);addV([v,u]);for(let f of [-1n,1n])addV([v,u,scale(h,f)])}}}
  }
  if(!local.size)throw Error("missing primary face");
  details.push([aa,bb,d,local.size]);
 }
 let rr=classify(refined);
 return {name,monos,primary:H.length,rayVisits,edgeVisits,facetVisits,open:o,boundaryOptimistic:f,refined:rr,dimHist,details,totalChecks:checks-start}
}

 return {points:P.length,germs:G.length,linearPartitions:Q.length,result:rank4("diagonal_plus_tB",[[0,0],[1,1],[2,2],[0,1]])};
}
const data=[{"normal":["187","12","-1"],"segments":9,"endpoints":[["0","1","12"],["1","17","391"]]},{"normal":["204","11","-1"],"segments":9,"endpoints":[["0","1","11"],["1","17","391"]]},{"normal":["5","-2","0"],"segments":51,"endpoints":[["2","5","73"],["2","5","5"]]},{"normal":["9","-1","0"],"segments":4,"endpoints":[["1","9","74"],["1","9","69"]]},{"normal":["85","7","-2"],"segments":10,"endpoints":[["1","9","74"],["3","17","187"]]},{"normal":["51","2","-1"],"segments":9,"endpoints":[["1","9","69"],["1","0","51"]]},{"normal":["0","1","-1"],"segments":2,"endpoints":[["2","5","5"],["1","0","0"]]},{"normal":["34","1","-1"],"segments":7,"endpoints":[["2","5","73"],["1","0","34"]]},{"normal":["187","20","-9"],"segments":5,"endpoints":[["6","15","158"],["1","1","23"]]},{"normal":["68","1","-3"],"segments":8,"endpoints":[["2","5","47"],["3","0","68"]]},{"normal":["176","22","-9"],"segments":4,"endpoints":[["6","15","154"],["19","28","440"]]},{"normal":["22","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","22"]]},{"normal":["61","0","-1"],"segments":78,"endpoints":[["0","1","0"],["1","17","61"]]},{"normal":["74","0","-1"],"segments":14,"endpoints":[["1","9","74"],["1","4","74"]]},{"normal":["126","0","-1"],"segments":103,"endpoints":[["0","1","0"],["1","30","126"]]},{"normal":["4","-1","0"],"segments":35,"endpoints":[["1","4","152"],["1","4","74"]]},{"normal":["17","-1","0"],"segments":44,"endpoints":[["0","0","1"],["1","17","22"]]},{"normal":["156","-1","-1"],"segments":46,"endpoints":[["1","4","152"],["1","30","126"]]},{"normal":["69","0","-1"],"segments":16,"endpoints":[["1","17","69"],["1","9","69"]]},{"normal":["9","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","9"]]},{"normal":["235","0","-3"],"segments":84,"endpoints":[["0","1","0"],["3","77","235"]]},{"normal":["87","0","-1"],"segments":107,"endpoints":[["0","1","0"],["1","17","87"]]},{"normal":["104","-1","-1"],"segments":60,"endpoints":[["1","4","100"],["3","77","235"]]},{"normal":["38","0","-3"],"segments":57,"endpoints":[["0","1","0"],["3","40","38"]]},{"normal":["5","0","-2"],"segments":72,"endpoints":[["0","1","0"],["2","5","5"]]},{"normal":["39","-1","-1"],"segments":50,"endpoints":[["3","1","116"],["1","17","22"]]},{"normal":["40","0","-3"],"segments":63,"endpoints":[["0","1","0"],["3","38","40"]]},{"normal":["26","-1","-1"],"segments":39,"endpoints":[["2","5","47"],["3","53","25"]]},{"normal":["25","0","-3"],"segments":52,"endpoints":[["0","1","0"],["3","53","25"]]},{"normal":["83","0","-2"],"segments":69,"endpoints":[["0","1","0"],["2","34","83"]]},{"normal":["102","-7","-1"],"segments":14,"endpoints":[["1","4","74"],["3","17","187"]]},{"normal":["204","-11","1"],"segments":51,"endpoints":[["0","1","11"],["1","30","126"]]},{"normal":["395","0","-2"],"segments":119,"endpoints":[["0","1","0"],["2","73","395"]]},{"normal":["289","18","-1"],"segments":10,"endpoints":[["0","1","18"],["1","17","595"]]},{"normal":["66","2","-1"],"segments":11,"endpoints":[["1","4","74"],["1","0","66"]]},{"normal":["132","5","-1"],"segments":16,"endpoints":[["1","17","217"],["1","0","132"]]},{"normal":["44","1","-1"],"segments":9,"endpoints":[["1","17","61"],["1","11","55"]]},{"normal":["88","3","-1"],"segments":7,"endpoints":[["1","4","100"],["1","0","88"]]},{"normal":["88","7","-3"],"segments":5,"endpoints":[["1","17","69"],["1","11","55"]]},{"normal":["132","-7","-1"],"segments":14,"endpoints":[["1","9","69"],["1","11","55"]]},{"normal":["153","8","-1"],"segments":7,"endpoints":[["1","9","225"],["1","0","153"]]},{"normal":["153","5","-4"],"segments":1,"endpoints":[["3","1","116"],["4","0","153"]]},{"normal":["117","-2","-2"],"segments":42,"endpoints":[["2","5","112"],["2","34","83"]]},{"normal":["198","8","-1"],"segments":5,"endpoints":[["1","4","230"],["1","0","198"]]},{"normal":["198","5","-4"],"segments":11,"endpoints":[["2","8","109"],["2","0","99"]]},{"normal":["306","17","-1"],"segments":8,"endpoints":[["1","17","595"],["1","0","306"]]},{"normal":["234","-1","-1"],"segments":43,"endpoints":[["1","4","230"],["2","73","395"]]}];
experiment(data)
```
