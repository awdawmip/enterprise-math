# X6 R244 — exact two-projective-parameter quadratic coefficient families by first-active-row stratification

2026-11-26. Author proof + exact BigInt computation; NOT_REVIEWED. Independent informed TASK_RESEARCH. Researcher binding unconfirmed. Original native lookup r2-20261126-2208-x6-read SUCCEEDED at 2026-11-26T14:08:38.128751Z, Source e1f8febe2b6e1c6dc8c9d2fef32a453bc6a8fc24, NO_CANONICAL_PUBLICATION_DIRECTORY. No native owner projection or execution authority; no CLAIM/shared task mutation.

Frozen Port 10, 1935 integer directions, six-pair BRC, positive (17t,B,22t,D), strict 3/2 near set and legal optimizer. R243 pin b0910438dd620222c7c1c75b7ec9dbed0db6f7a8:research_notes/portable_direct/2026-11-26_r2_x6_r243_quadratic_pencil_event_capacity.md, blob e4ef139ff3ad772d43b4fddc9c3b12813b6735e4; its frozen 47 labeled supports, 49 components, 51 endpoint rays, 98 directed germs and R240 linear suffix recursion reused. P000 V5 and residual/joint-observer preservation unchanged. All vectors below are auxiliary weight or observation coefficient vectors, not native spatial geometry. No new scoring or native dynamics computation. Inherited necessary-wall and suffix-completeness premises are retained; author computation is not independent review.

## Theorem: recursive first-active-row event arrangement

Let V be a finite-dimensional real linear coefficient space of homogeneous polynomial observations of fixed degree. For each tagged directed germ g let r_g,0,...,r_g,m be its jet coefficient linear functionals on V in increasing germ order. The germ sign of q is the sign of its first nonzero evaluation, or zero if all vanish. For a linear subspace W of V, define h_g(W) to be the first row not identically zero on W, if one exists. Away from the union of kernels of these active rows restricted to W, every germ sign is constant on each arrangement chamber and equal to the sign of h_g(W)(q); germs without any active row are identically zero there. On any event hyperplane H = W intersect ker h_g(W), repeat the same construction on H, using the original full ordered jets. Every nonzero q either is off all events or belongs to at least one such H. Induction on dim W proves that the resulting finite strata cover the full coefficient space excluding zero, and each stratum has constant complete tagged germ sign data. Overlap can be deduplicated by full masks (not by label counts); no zero or higher-order residual is discarded. R243 is the affine one-parameter case; this theorem covers multiple parameters and all degeneracies.

## Exact rank-three realization used here

For a three-dimensional coefficient family with primary rows spanning R^3, the central primary arrangement is pointed (its common lineality is zero). Each full-dimensional chamber closure is a polyhedral cone with an extreme ray v, intersection of two independent primary hyperplanes. At v the incident hyperplanes induce a rank-two central arrangement on the auxiliary tangent space v-perp. Every sector in that arrangement is incident to a ray w = v cross r for an incident primary normal r. A representative sign tuple is obtained by lexicographic evaluation along (v, ±w, ±r), because a row vanishing on both v and w is parallel to r. These perturbations realize actual vectors v+epsilon w+epsilon^2 r for sufficiently small positive epsilon; the coefficient-space perturbation is evaluated BEFORE selecting the first nonzero germ jet row. Antipodal vectors swap branches and hence can be identified only for the symmetric suffix capacity question. Enumerate all extreme rays up to sign, all incident primary rows and both perturbation signs. This covers all primary open chambers. For each primary hyperplane r-perp, restrict each jet and choose its first nonzero restriction. Each distinct event line has direction v=r cross s where s is an active restricted row. Evaluate the full jets on v and (v, ±(r cross v)); these cover the event lines and adjacent open sectors in that hyperplane, up to global sign. If all restrictions are zero, the entire hyperplane has the all-zero mask. This covers all boundary strata. If a jet primary is absent globally, its zero is retained. All arithmetic can be integral for rational rows. A finite lex coefficient perturbation can be materialized as integer q via Horner base M=2 max absolute row-direction evaluation +2; the earliest nonzero contribution dominates the sum of later terms.

Independent enumeration check: construct the full arrangement of ALL nonzero jet rows instead of the first-active rows, using (v), (v, ±w), (v, ±w, ±r) for each intersection ray and incident normal. Same rank-three arrangement argument yields all faces. Check equality of full masks from the two methods. Also regenerate inherited 2225 pure-linear masks. This proves coverage of the three tested continuous coefficient families, not the entire six-dimensional quadratic coefficient space.

## Application to X6

For each root mask, count distinct support labels on each strict branch. Depth five allows at most 31, so either child above 31 is impossible. Otherwise apply the pinned R240 pure-linear finite germ relaxation: at most d distinct labels is feasible (one support query per label); more than 2^d-1 is impossible; saturated capacity requires a support query to eliminate a whole label, so use the support bank there; otherwise enumerate the complete linear mask bank. A false child excludes every actual tree with that mask; a true relaxation does not construct a correct tree. Positive and negative masks retain all directed germs and zero is their complement. Exact BigInt counts, cached only on identical full masks. Per-family cutoff 2,500,000 recursive mask checks; unknowns are never counted as exclusions. Each family includes all nonzero real coefficient triples, up to overall nonzero scaling/branch swap. The diagonal family includes all arbitrary diagonal forms (not merely one-parameter pencils); the off-diagonal family includes all forms alpha tB+beta tD+gamma BD, with full rank if alpha beta gamma !=0; the third family consists of alpha t^2+beta tB+gamma BD. No classification by measure on coefficient space is claimed.

## Actual exact output

```json
{"points":51,"germs":98,"linearPartitions":2225,"linearPrimary":51,"families":[{"name":"diagonal","monos":[[0,0],[1,1],[2,2]],"primaryRows":51,"primaryRays":1096,"openMasks":1135,"openVisits":8920,"boundaryVisits":6819,"fullRows":156,"fullRays":11001,"partitions":2279,"zeroMasks":19,"direct":1918,"excluded":361,"survivors":[],"unknown":[],"checks":1267547},{"name":"off_diagonal","monos":[[0,1],[0,2],[1,2]],"primaryRows":50,"primaryRays":1043,"openMasks":1089,"openVisits":8524,"boundaryVisits":6561,"fullRows":158,"fullRays":11782,"partitions":2148,"zeroMasks":19,"direct":1779,"excluded":369,"survivors":[],"unknown":[],"checks":874416},{"name":"t_squared_two_crosses","monos":[[0,0],[0,1],[1,2]],"primaryRows":48,"primaryRays":936,"openMasks":983,"openVisits":7672,"boundaryVisits":5916,"fullRows":153,"fullRays":10259,"partitions":1995,"zeroMasks":18,"direct":1741,"excluded":254,"survivors":[],"unknown":[],"checks":378551}],"totalChecks":2520514}
```

For any family with no survivors or unknowns the entire specified real coefficient family is excluded as the unique quadratic root followed by arbitrary linear queries, conditional on the inherited necessary-wall premises. Otherwise retain listed masks and representative coefficients for refinement. The two arrangement methods are algorithmic crosschecks on the same data, not independent mathematical review. Next: use first-active-row stratification in higher coefficient dimension or reduce full-rank search by exact capacity conflicts; refine any listed survivors. Internal placement of the nonlinear query and unrestricted K6 remain open (1–2).

## Reproducible exact source (JavaScript, BigInt)
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
 const families=[family("diagonal",[[0,0],[1,1],[2,2]]),family("off_diagonal",[[0,1],[0,2],[1,2]]),family("t_squared_two_crosses",[[0,0],[0,1],[1,2]])];
 return {points:P.length,germs:G.length,linearPartitions:Q.length,linearPrimary:linear.primary,families,totalChecks:checks};
}
const data=[{"normal":["187","12","-1"],"segments":9,"endpoints":[["0","1","12"],["1","17","391"]]},{"normal":["204","11","-1"],"segments":9,"endpoints":[["0","1","11"],["1","17","391"]]},{"normal":["5","-2","0"],"segments":51,"endpoints":[["2","5","73"],["2","5","5"]]},{"normal":["9","-1","0"],"segments":4,"endpoints":[["1","9","74"],["1","9","69"]]},{"normal":["85","7","-2"],"segments":10,"endpoints":[["1","9","74"],["3","17","187"]]},{"normal":["51","2","-1"],"segments":9,"endpoints":[["1","9","69"],["1","0","51"]]},{"normal":["0","1","-1"],"segments":2,"endpoints":[["2","5","5"],["1","0","0"]]},{"normal":["34","1","-1"],"segments":7,"endpoints":[["2","5","73"],["1","0","34"]]},{"normal":["187","20","-9"],"segments":5,"endpoints":[["6","15","158"],["1","1","23"]]},{"normal":["68","1","-3"],"segments":8,"endpoints":[["2","5","47"],["3","0","68"]]},{"normal":["176","22","-9"],"segments":4,"endpoints":[["6","15","154"],["19","28","440"]]},{"normal":["22","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","22"]]},{"normal":["61","0","-1"],"segments":78,"endpoints":[["0","1","0"],["1","17","61"]]},{"normal":["74","0","-1"],"segments":14,"endpoints":[["1","9","74"],["1","4","74"]]},{"normal":["126","0","-1"],"segments":103,"endpoints":[["0","1","0"],["1","30","126"]]},{"normal":["4","-1","0"],"segments":35,"endpoints":[["1","4","152"],["1","4","74"]]},{"normal":["17","-1","0"],"segments":44,"endpoints":[["0","0","1"],["1","17","22"]]},{"normal":["156","-1","-1"],"segments":46,"endpoints":[["1","4","152"],["1","30","126"]]},{"normal":["69","0","-1"],"segments":16,"endpoints":[["1","17","69"],["1","9","69"]]},{"normal":["9","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","9"]]},{"normal":["235","0","-3"],"segments":84,"endpoints":[["0","1","0"],["3","77","235"]]},{"normal":["87","0","-1"],"segments":107,"endpoints":[["0","1","0"],["1","17","87"]]},{"normal":["104","-1","-1"],"segments":60,"endpoints":[["1","4","100"],["3","77","235"]]},{"normal":["38","0","-3"],"segments":57,"endpoints":[["0","1","0"],["3","40","38"]]},{"normal":["5","0","-2"],"segments":72,"endpoints":[["0","1","0"],["2","5","5"]]},{"normal":["39","-1","-1"],"segments":50,"endpoints":[["3","1","116"],["1","17","22"]]},{"normal":["40","0","-3"],"segments":63,"endpoints":[["0","1","0"],["3","38","40"]]},{"normal":["26","-1","-1"],"segments":39,"endpoints":[["2","5","47"],["3","53","25"]]},{"normal":["25","0","-3"],"segments":52,"endpoints":[["0","1","0"],["3","53","25"]]},{"normal":["83","0","-2"],"segments":69,"endpoints":[["0","1","0"],["2","34","83"]]},{"normal":["102","-7","-1"],"segments":14,"endpoints":[["1","4","74"],["3","17","187"]]},{"normal":["204","-11","1"],"segments":51,"endpoints":[["0","1","11"],["1","30","126"]]},{"normal":["395","0","-2"],"segments":119,"endpoints":[["0","1","0"],["2","73","395"]]},{"normal":["289","18","-1"],"segments":10,"endpoints":[["0","1","18"],["1","17","595"]]},{"normal":["66","2","-1"],"segments":11,"endpoints":[["1","4","74"],["1","0","66"]]},{"normal":["132","5","-1"],"segments":16,"endpoints":[["1","17","217"],["1","0","132"]]},{"normal":["44","1","-1"],"segments":9,"endpoints":[["1","17","61"],["1","11","55"]]},{"normal":["88","3","-1"],"segments":7,"endpoints":[["1","4","100"],["1","0","88"]]},{"normal":["88","7","-3"],"segments":5,"endpoints":[["1","17","69"],["1","11","55"]]},{"normal":["132","-7","-1"],"segments":14,"endpoints":[["1","9","69"],["1","11","55"]]},{"normal":["153","8","-1"],"segments":7,"endpoints":[["1","9","225"],["1","0","153"]]},{"normal":["153","5","-4"],"segments":1,"endpoints":[["3","1","116"],["4","0","153"]]},{"normal":["117","-2","-2"],"segments":42,"endpoints":[["2","5","112"],["2","34","83"]]},{"normal":["198","8","-1"],"segments":5,"endpoints":[["1","4","230"],["1","0","198"]]},{"normal":["198","5","-4"],"segments":11,"endpoints":[["2","8","109"],["2","0","99"]]},{"normal":["306","17","-1"],"segments":8,"endpoints":[["1","17","595"],["1","0","306"]]},{"normal":["234","-1","-1"],"segments":43,"endpoints":[["1","4","230"],["2","73","395"]]}];
console.log(JSON.stringify(experiment(data)));
```
