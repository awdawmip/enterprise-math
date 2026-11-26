# X6 R247 — two-anchor incidence kernel, signed first-active primary faces

2026-11-27. Independent informed TASK_RESEARCH; author proof and exact computation, NOT_REVIEWED. Native original read r2-20261127-0111-x6-read SUCCEEDED at 2026-11-26T17:12:04.028685Z, Source 02bc716f354658f56e4af1d4eaa383e1c0d469ce, NO_CANONICAL_PUBLICATION_DIRECTORY. No live owner projection or own researcher binding established; no CLAIM, Result, review or shared state mutation.

Frozen predecessor 2e43e8f1623d9c114f31e7c6ea120f1923d6660f:research_notes/portable_direct/2026-11-26_r2_x6_r245_rank_four_primary_face_pruning.md (blob 29ccfec9892403268d1df9b95344444099a62856). R246: 685a53de549d4d0affe7ace42a26e1fc68af6f30:research_notes/portable_direct/2026-11-27_r2_x6_r246_conic_incidence_boundary_capacity.md. Same Port 10, 1935 integer directions, six-pair BRC, weights (17t,B,22t,D), strict 3/2 near set, 47 necessary labeled supports, 49 components, 51 endpoint rays, 98 directed germs, 2225 linear suffix masks. This is the auxiliary weight coefficient space, not a native spatial plane or new X6 geometry. All exclusions inherit the necessary-wall theorem and the complete pure-linear suffix bank and capacity recursion of the pinned sources.

## Algebra and signed first-active arrangement

The two fixed zero conditions Q(p18)=Q(p0)=0 for p18=(0,1,0) and p0=(0,1,12) force b=0 and f=-12c in the six-monomial basis (t²,B²,D²,tB,tD,BD). Thus the entire four-dimensional kernel is Q=a t²+c D(D-12B)+d tB+e tD. The symmetric matrix has determinant -c(144ac+d²+12de)/4 (direct expansion). In particular c=0 yields a real product t(at+dB+eD); no assumption of nonsingularity is needed in the actual enumeration.

For each directed germ with start (t,B,D) and increment (x,y,z), the three exact jet rows on (a,c,d,e) are (t²,D(D-12B),tB,tD), (2tx,2Dz-12(Bz+Dy),ty+Bx,tz+Dx), (x²,z(z-12y),xy,xz). Delete only identically zero leading rows in this kernel. For a nonzero first-active row r, write r=k h where h is primitive with positive first nonzero entry, k nonzero. Store two disjoint bit sets P_h and N_h for k>0 and k<0; evaluation at sign(h·q)=+ assigns P_h to positive, N_h to negative, and swaps them for -. Zero leaves both sets unassigned until refinement. When restricting to h0·q=0, in coordinates excluding the pivot p, the induced row is h0[p]h[i]-h0[i]h[p]; since pivot positive, its sign is preserved before normalization. If the induced row is negative relative to its canonical primitive representative, exchange its two bit sets. This proves preservation of first-active sign even with mixed orientations. It is essential here, because normalizing a row up to sign without retaining orientation would lose branch relations.

In rank four, every nonzero primary sign face of the essential central arrangement is either in an event hyperplane or a chamber adjacent to a facet. For each event hyperplane, the restricted rank-three arrangement is exhaustively enumerated by the inherited extreme-ray and infinitesimal tangent flag construction; lift its facets to the two incident open chambers with the signed groups restored. Canonicalize by simultaneous branch exchange only. The first-active strict masks are subsets of the corresponding full masks. Capacity is downward closed on each branch, so an infeasible partial mask excludes its entire refinement. For each surviving face, restrict the full jets to the kernel of all its zero primary rows and enumerate the remaining rank at most three, accepting only the original primary mask pair up to common swap. This preserves the actual germ labels and all high-order sign residuals. The frozen R245 method is extended to mixed orientation and identically zero leading rows; it is not a new native geometry model.

## Exact run

An initial run hit its 12,000,000 capacity-check ceiling: 30,433 open masks fully excluded, 209,603 boundary masks of which 174,636 direct and 32,744 recursive exclusions, five relaxed survivors, 2,218 unknown; four refined masks unknown. The final run below replaces that pilot, with 45,000,000 check ceiling; do not add pilot counts. Output includes all remaining masks and refinement provenance. Unknown is never a rejection. Counts are masks, not individual conics; no disjointness from R246's subsets claimed.

```json
{"points":51,"germs":98,"linearPartitions":2225,"result":{"name":"two_anchor_kernel","monos":[],"primary":60,"rayVisits":89257,"edgeVisits":359330,"facetVisits":718660,"open":{"total":30433,"direct":26801,"excluded":3632,"survivors":[],"unknown":[],"checks":7049593},"boundaryOptimistic":{"total":209603,"direct":174636,"excluded":34962,"survivors":[["33ca3202aee808200afffa30","3cc30cda90003a0cbb000014b",27,23,[2,"ray"]],["1ce3a38c0ffbc0c2c0fdcc02b","231c5c73f0043e392f0223fc4",28,28,[3,"ray"]],["1ce3b34c0fb9efd7d0f00000b","231c0c33f04410082f0ffbb54",29,26,[4,"ray"]],["1ce3b34c0fb9efd7d0f00000b","231c0c33f04610082f0fffb74",29,27,[6,"edge"]],["1ce3b34c0fb9efd7d0f00000b","231c0c33f04610082b0fffb74",29,27,[6,"ray"]]],"unknown":[],"checks":6138898},"refined":{"total":4,"direct":0,"excluded":4,"survivors":[],"unknown":[],"checks":9264},"dimHist":{"1":4,"2":1},"details":[["33ca3202aee808200afffa30","3cc30cda90003a0cbb000014b",1,1],["1ce3a38c0ffbc0c2c0fdcc02b","231c5c73f0043e392f0223fc4",1,1],["1ce3b34c0fb9efd7d0f00000b","231c0c33f04410082f0ffbb54",1,1],["1ce3b34c0fb9efd7d0f00000b","231c0c33f04610082f0fffb74",2,1],["1ce3b34c0fb9efd7d0f00000b","231c0c33f04610082b0fffb74",1,1]],"totalChecks":13197755}}
```

Conclusion: The full four-dimensional kernel through p18 and p0 is excluded as the unique quadratic root of a depth-six tree with arbitrary linear suffix, under the inherited capacity premises.

## Reproduction
Complete exact BigInt source, inherited input and kernel included. Executed as a local JavaScript function with final expression returned.

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
 const jetRows=G.map(([u,v])=>{let p=P[u],w=sub(P[v],p);let [t,B,D]=p,[x,y,z]=w;return [[t*t,D*(D-12n*B),t*B,t*D],[2n*t*x,2n*D*z-12n*(B*z+D*y),t*y+B*x,t*z+D*x],[x*x,z*(z-12n*y),x*y,x*z]]});
 if(P[18].join()!=="0,1,0"||P[0].join()!=="0,1,12")throw Error("anchor mismatch");
 for(let i=0;i<G.length;i++){let bit=G[i][2],raw=jetRows[i].find(nz);if(!raw)throw Error("all rows zero");let h=norm(raw,true),k=h.join();if(!groups.has(k))groups.set(k,{h,bits:0n,pos:0n,neg:0n});let g=groups.get(k);g.bits|=bit;g[raw.find(Boolean)>0n?"pos":"neg"]|=bit}
 const H=[...groups.values()],open=new Map(),faces=new Map();
 function add(map,a,b,info){[a,b]=canon(a,b);let k=a+","+b;if(!map.has(k))map.set(k,{a,b,info})}
 let rayVisits=0,edgeVisits=0,facetVisits=0;
 for(let z=0;z<H.length;z++){
  let {h,bits:zero}=H[z],p=h.findIndex(Boolean),ix=[0,1,2,3].filter(i=>i!==p);
  let rs=new Map();
  for(let {h:s,pos,neg} of H){let x=ix.map(i=>h[p]*s[i]-h[i]*s[p]);if(!nz(x))continue;let y=norm(x,true),k=y.join();if(!rs.has(k))rs.set(k,{r:y,pos:0n,neg:0n});let g=rs.get(k);if(x.find(Boolean)>0n){g.pos|=pos;g.neg|=neg}else{g.pos|=neg;g.neg|=pos}}
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
      add(open,x|H[z].pos,y|H[z].neg,[z]);add(open,x|H[z].neg,y|H[z].pos,[z]);
     }
    }
   }
  }
 }
 let start=checks;ceiling=checks+45000000;
 function classify(map){let direct=0,excluded=0,survivors=[],unknown=[];let before=checks;
  for(let {a,b,info} of map.values()){
   if(count(a)>31||count(b)>31){direct++;continue}
   try{if(can(a,5)&&can(b,5))survivors.push([a.toString(16),b.toString(16),count(a),count(b),info]);else excluded++}catch(err){if(err!==CUT)throw err;unknown.push([a.toString(16),b.toString(16),info])}
  }
  return {total:map.size,direct,excluded,survivors,unknown,checks:checks-before}
 }
 const o=classify(open),f=classify(faces);
 const jets=jetRows;const primRows=jets.map(rs=>rs.find(nz));
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
  const rows=jets.map(rs=>rs.map(h=>B.map(x=>dotN(h,x))));const pr=primRows.map(h=>B.map(x=>dotN(h,x)));
  const dimDot=dotN;
  function addV(vs){
   let p=0n,q=0n,x=0n,y=0n;
   for(let i=0;i<rows.length;i++){
    let sign=0;for(let v of vs){sign=sg(dimDot(pr[i],v));if(sign)break}
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

 return {points:P.length,germs:G.length,linearPartitions:Q.length,result:rank4("two_anchor_kernel",[])};
}
const data=[{"normal":["187","12","-1"],"segments":9,"endpoints":[["0","1","12"],["1","17","391"]]},{"normal":["204","11","-1"],"segments":9,"endpoints":[["0","1","11"],["1","17","391"]]},{"normal":["5","-2","0"],"segments":51,"endpoints":[["2","5","73"],["2","5","5"]]},{"normal":["9","-1","0"],"segments":4,"endpoints":[["1","9","74"],["1","9","69"]]},{"normal":["85","7","-2"],"segments":10,"endpoints":[["1","9","74"],["3","17","187"]]},{"normal":["51","2","-1"],"segments":9,"endpoints":[["1","9","69"],["1","0","51"]]},{"normal":["0","1","-1"],"segments":2,"endpoints":[["2","5","5"],["1","0","0"]]},{"normal":["34","1","-1"],"segments":7,"endpoints":[["2","5","73"],["1","0","34"]]},{"normal":["187","20","-9"],"segments":5,"endpoints":[["6","15","158"],["1","1","23"]]},{"normal":["68","1","-3"],"segments":8,"endpoints":[["2","5","47"],["3","0","68"]]},{"normal":["176","22","-9"],"segments":4,"endpoints":[["6","15","154"],["19","28","440"]]},{"normal":["22","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","22"]]},{"normal":["61","0","-1"],"segments":78,"endpoints":[["0","1","0"],["1","17","61"]]},{"normal":["74","0","-1"],"segments":14,"endpoints":[["1","9","74"],["1","4","74"]]},{"normal":["126","0","-1"],"segments":103,"endpoints":[["0","1","0"],["1","30","126"]]},{"normal":["4","-1","0"],"segments":35,"endpoints":[["1","4","152"],["1","4","74"]]},{"normal":["17","-1","0"],"segments":44,"endpoints":[["0","0","1"],["1","17","22"]]},{"normal":["156","-1","-1"],"segments":46,"endpoints":[["1","4","152"],["1","30","126"]]},{"normal":["69","0","-1"],"segments":16,"endpoints":[["1","17","69"],["1","9","69"]]},{"normal":["9","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","9"]]},{"normal":["235","0","-3"],"segments":84,"endpoints":[["0","1","0"],["3","77","235"]]},{"normal":["87","0","-1"],"segments":107,"endpoints":[["0","1","0"],["1","17","87"]]},{"normal":["104","-1","-1"],"segments":60,"endpoints":[["1","4","100"],["3","77","235"]]},{"normal":["38","0","-3"],"segments":57,"endpoints":[["0","1","0"],["3","40","38"]]},{"normal":["5","0","-2"],"segments":72,"endpoints":[["0","1","0"],["2","5","5"]]},{"normal":["39","-1","-1"],"segments":50,"endpoints":[["3","1","116"],["1","17","22"]]},{"normal":["40","0","-3"],"segments":63,"endpoints":[["0","1","0"],["3","38","40"]]},{"normal":["26","-1","-1"],"segments":39,"endpoints":[["2","5","47"],["3","53","25"]]},{"normal":["25","0","-3"],"segments":52,"endpoints":[["0","1","0"],["3","53","25"]]},{"normal":["83","0","-2"],"segments":69,"endpoints":[["0","1","0"],["2","34","83"]]},{"normal":["102","-7","-1"],"segments":14,"endpoints":[["1","4","74"],["3","17","187"]]},{"normal":["204","-11","1"],"segments":51,"endpoints":[["0","1","11"],["1","30","126"]]},{"normal":["395","0","-2"],"segments":119,"endpoints":[["0","1","0"],["2","73","395"]]},{"normal":["289","18","-1"],"segments":10,"endpoints":[["0","1","18"],["1","17","595"]]},{"normal":["66","2","-1"],"segments":11,"endpoints":[["1","4","74"],["1","0","66"]]},{"normal":["132","5","-1"],"segments":16,"endpoints":[["1","17","217"],["1","0","132"]]},{"normal":["44","1","-1"],"segments":9,"endpoints":[["1","17","61"],["1","11","55"]]},{"normal":["88","3","-1"],"segments":7,"endpoints":[["1","4","100"],["1","0","88"]]},{"normal":["88","7","-3"],"segments":5,"endpoints":[["1","17","69"],["1","11","55"]]},{"normal":["132","-7","-1"],"segments":14,"endpoints":[["1","9","69"],["1","11","55"]]},{"normal":["153","8","-1"],"segments":7,"endpoints":[["1","9","225"],["1","0","153"]]},{"normal":["153","5","-4"],"segments":1,"endpoints":[["3","1","116"],["4","0","153"]]},{"normal":["117","-2","-2"],"segments":42,"endpoints":[["2","5","112"],["2","34","83"]]},{"normal":["198","8","-1"],"segments":5,"endpoints":[["1","4","230"],["1","0","198"]]},{"normal":["198","5","-4"],"segments":11,"endpoints":[["2","8","109"],["2","0","99"]]},{"normal":["306","17","-1"],"segments":8,"endpoints":[["1","17","595"],["1","0","306"]]},{"normal":["234","-1","-1"],"segments":43,"endpoints":[["1","4","230"],["2","73","395"]]}];
experiment(data)

```

## Next
Do not repeat the p18,p0 incidence kernel or its rank-five/three-dimensional subsets. Extend the signed first-active method to the single-anchor five-dimensional kernel, using shared lower-rank flats and cached infeasible suffix subsets. Generic nonsingular root and unique quadratic at an internal node remain open. Unrestricted K6 remains 1–2. Independent mathematical review and Activity association pending.
