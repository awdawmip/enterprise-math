# X6 R228: local extreme-ray bank, five unknown quarter-witness sides

2026-11-26, informed RESEARCH_DRIVER. Same Port10, w=(17t,B,22t,D)>0, six BRC relations, 47 necessary supports and 49 components, strict tagged-wall capacity relaxation. Input original author R227 578fb612d9c52fa677c966740a99565d58fc98d7:research_notes/portable_direct/2026-11-26_r2_x6_r227_quadratic_root_wall_capacity.md, and quarter-witness artifact b898d514819b08dd5cc3844d9f9ad36176536163:research_notes/driver/2026-11-26_x6_r228_quarter_witness_refinement.json. Only the five unknown sides are recomputed; previously passing side states are reused without asserting actual tree feasibility. No earlier excluded roots are repeated.

## Exact local-bank improvement

The same R228 monotonicity theorem applies at each reached witness subset S: after checking distinct-label capacity, if rank(S)<=2, a nonzero normal kills all S in one query (or S empty); if rank(S)=3, any feasible first query has a pointed closed sign cone with an extreme ray formed by two independent points of S, and both strict children of that extreme query are subsets of the original ones. Therefore we can replace scanning the global pair bank at every state by scanning only pairs of actual surviving witness points. Precompute or cache their sign masks in the global bank and deduplicate by ray and resulting unordered child pair. Rank 2 shortcut is exact since normalized positive distinct rays are independent in pairs; rank 1 has at most one distinct witness. Discard zero points only in the finite capacity relaxation. Memoize true/false outcomes only; caps return unknown. This improves the finite relaxation algorithm without changing its proposition or input. Exact BigInt signs, all tags at coincident rays retained, rank and branch capacities checked. No claim for general quadratics or earlier linear ancestors.

## Actual exact result

```json
{"n":4,"budget":6000000,"total":{"checks":2121461,"calls":3767,"pairVisits":2454425,"queryBanks":23148,"rankShortcut":1,"cappedSides":0},"excluded":[{"i":11,"j":20,"counts":[25,24],"sides":[{"pass":true,"reused":true,"pointCount":104},{"pass":false,"calls":827,"checks":445227,"pairVisits":512885,"memoHits":294,"pointCount":102,"queries":4666,"rankShortcut":0,"cap":false}]},{"i":12,"j":33,"counts":[24,25],"sides":[{"pass":false,"calls":550,"checks":369710,"pairVisits":428382,"memoHits":72,"pointCount":103,"queries":4769,"rankShortcut":0,"cap":false},{"pass":true,"reused":true,"pointCount":104}]},{"i":12,"j":45,"counts":[24,25],"sides":[{"pass":false,"calls":759,"checks":370217,"pairVisits":429877,"memoHits":152,"pointCount":103,"queries":4762,"rankShortcut":1,"cap":false},{"pass":true,"reused":true,"pointCount":104}]},{"i":13,"j":23,"counts":[24,24],"sides":[{"pass":true,"reused":true,"pointCount":99},{"pass":false,"calls":578,"checks":428317,"pairVisits":494391,"memoHits":105,"pointCount":102,"queries":4660,"rankShortcut":0,"cap":false}]}],"remaining":[{"i":13,"j":26,"counts":[25,23],"sides":[{"pass":true,"reused":true,"pointCount":103},{"pass":true,"calls":1053,"checks":507990,"pairVisits":588890,"memoHits":329,"pointCount":98,"queries":4291,"rankShortcut":0,"cap":false}]}],"unknown":[],"results":[{"i":11,"j":20,"counts":[25,24],"sides":[{"pass":true,"reused":true,"pointCount":104},{"pass":false,"calls":827,"checks":445227,"pairVisits":512885,"memoHits":294,"pointCount":102,"queries":4666,"rankShortcut":0,"cap":false}]},{"i":12,"j":33,"counts":[24,25],"sides":[{"pass":false,"calls":550,"checks":369710,"pairVisits":428382,"memoHits":72,"pointCount":103,"queries":4769,"rankShortcut":0,"cap":false},{"pass":true,"reused":true,"pointCount":104}]},{"i":12,"j":45,"counts":[24,25],"sides":[{"pass":false,"calls":759,"checks":370217,"pairVisits":429877,"memoHits":152,"pointCount":103,"queries":4762,"rankShortcut":1,"cap":false},{"pass":true,"reused":true,"pointCount":104}]},{"i":13,"j":23,"counts":[24,24],"sides":[{"pass":true,"reused":true,"pointCount":99},{"pass":false,"calls":578,"checks":428317,"pairVisits":494391,"memoHits":105,"pointCount":102,"queries":4660,"rankShortcut":0,"cap":false}]},{"i":13,"j":26,"counts":[25,23],"sides":[{"pass":true,"reused":true,"pointCount":103},{"pass":true,"calls":1053,"checks":507990,"pairVisits":588890,"memoHits":329,"pointCount":98,"queries":4291,"rankShortcut":0,"cap":false}]}]}
```

## Replay

```js
function run(data,old,n=4,budget=6000000){
 const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],abs=x=>x<0n?-x:x,gcd=(a,b)=>b?gcd(b,a%b):abs(a),norm=(a,ray=false)=>{let g=a.reduce(gcd,0n);if(!g)return a;if(ray&&a.find(Boolean)<0n)g=-g;return a.map(x=>x/g)},sg=x=>x>0n?1:x<0n?-1:0;
 const N=data.map(e=>e.normal.map(BigInt)),parts=data.map((e,k)=>(k===5?[[[1,9,69],[3,17,187]],[[2,5,112],[1,0,51]]]:k===16?[[[0,0,1],[1,17,391]],[[1,17,69],[1,17,22]]]:[e.endpoints]).map(pair=>pair.map(p=>norm(p.map(BigInt)))));
 if(N.length!==47||parts.flat().length!==49||parts.some((ss,k)=>ss.flat().some(p=>dot(N[k],p)!==0n)))throw Error("input");
 function split(segs,q){let out=[[],[]];for(let [a,b] of segs){let A=dot(q,a),B=dot(q,b),sa=sg(A),sb=sg(B);if(sa*sb<0){let p=norm(a.map((x,k)=>abs(B)*x+abs(A)*b[k]));out[sa>0?0:1].push([a,p]);out[sb>0?0:1].push([p,b]);}else if(sa||sb)out[(sa||sb)>0?0:1].push([a,b]);}return out}
 function root(i,j){let ss=[[],[]];for(let k=0;k<N.length;k++){if(k===i||k===j)continue;let [p,n]=split(parts[k],N[i]),[pp,pn]=split(p,N[j]),[np,nn]=split(n,N[j]);let s0=[...pp,...nn],s1=[...pn,...np];if(s0.length)ss[0].push({k,segs:s0});if(s1.length)ss[1].push({k,segs:s1})}return ss}
 function solve(side){
  let map=new Map();for(let {k,segs} of side)for(let [a,b] of segs)for(let j=0;j<=n;j++){let p=norm(a.map((x,i)=>BigInt(n-j)*x+BigInt(j)*b[i])),id=p.join();if(!map.has(id))map.set(id,{p,tags:new Set()});map.get(id).tags.add(k)}
  let P=[...map.values()],bits=P.map((_,i)=>1n<<BigInt(i)),all=(1n<<BigInt(P.length))-1n,L=new Map();for(let i=0;i<P.length;i++)for(let k of P[i].tags)L.set(k,(L.get(k)??0n)|bits[i]);
  if(L.size!==side.length)throw Error("tag loss");let labelMasks=[...L.values()],countCache=new Map(),memo=new Map(), stats={calls:0,checks:0,pairVisits:0,memoHits:0,pointCount:P.length,queries:0,rankShortcut:0,cap:false},pairCache=new Map(),rayCache=new Map();
  function count(S){let v=countCache.get(S);if(v!==undefined)return v;let c=0;for(let x of labelMasks)if(S&x)c++;countCache.set(S,c);return c}
  function indices(S){let a=[];for(let i=0;i<bits.length;i++)if(S&bits[i])a.push(i);return a}
  function query(i,j){let k=i*P.length+j,v=pairCache.get(k);if(v!==undefined)return v;let q=norm(cross(P[i].p,P[j].p),true);if(!q.some(Boolean)){pairCache.set(k,null);return null}let r=q.join(),x=rayCache.get(r);if(!x){let A=0n,B=0n;for(let z=0;z<P.length;z++){let y=dot(q,P[z].p);if(y>0n)A|=bits[z];else if(y<0n)B|=bits[z]}if(A>B)[A,B]=[B,A];x={id:rayCache.size,A,B};rayCache.set(r,x)}pairCache.set(k,x);return x}
  function possible(S,d){stats.calls++;let c=count(S);if(c>2**d-1)return false;if(c<=d)return true;let key=d+"/"+S.toString(16);if(memo.has(key)){stats.memoHits++;return memo.get(key)}if(stats.checks>=budget){stats.cap=true;return null}let ids=indices(S),cap=2**(d-1)-1;
    if(ids.length<=1){stats.rankShortcut++;memo.set(key,true);return true}
    let q=query(ids[0],ids[1]);if(!q)throw Error("distinct normalized positive rays expected");
    if(!(S&(q.A|q.B))){stats.rankShortcut++;memo.set(key,true);return true}
    let seen=new Set(),partitions=new Set(),unknown=false;
    for(let i=0;i<ids.length;i++)for(let j=i+1;j<ids.length;j++){
      stats.pairVisits++;let q=query(ids[i],ids[j]);if(!q||seen.has(q.id))continue;seen.add(q.id);if(stats.checks>=budget){stats.cap=true;return null}stats.checks++;
      let A=S&q.A,B=S&q.B,ca=count(A),cb=count(B);if(ca>cap||cb>cap)continue;if(A>B){[A,B]=[B,A];[ca,cb]=[cb,ca]}let k=A.toString(16)+"/"+B.toString(16);if(partitions.has(k))continue;partitions.add(k);if(ca<cb)[A,B]=[B,A];let x=possible(A,d-1);if(x===false)continue;let y=possible(B,d-1);if(y===false)continue;if(x===true&&y===true){memo.set(key,true);return true}unknown=true;
    }
    if(unknown)return null;memo.set(key,false);return false
  }
  let pass=possible(all,5);stats.queries=rayCache.size;return {pass,...stats}
 }
 let results=[],excluded=[],remaining=[],unknown=[];for(let row of old){if(row.sides.some(x=>x?.pass===false))continue;let ss=root(row.i,row.j);if(ss.map(x=>x.length).join()!==row.counts.join())throw Error("count mismatch");let out=row.sides.map((x,i)=>x?.pass===null?solve(ss[i]):{pass:x?.pass,reused:true,pointCount:x?.pointCount});let x={i:row.i,j:row.j,counts:row.counts,sides:out};results.push(x);if(out.some(x=>x.pass===false))excluded.push(x);else {remaining.push(x);if(out.some(x=>x.pass===null))unknown.push(x)}}
 let total={checks:0,calls:0,pairVisits:0,queryBanks:0,rankShortcut:0,cappedSides:0};for(let x of results)for(let s of x.sides)if(!s.reused){total.checks+=s.checks;total.calls+=s.calls;total.pairVisits+=s.pairVisits;total.queryBanks+=s.queries;total.rankShortcut+=s.rankShortcut;total.cappedSides+=Number(s.cap)}
 return {n,budget,total,excluded,remaining,unknown,results}
}
```
Inputs original R227 `const data=[...];` and quarter artifact `result.results`. Run run(data,old,4,6000000). The input quarter state was unknown on five sides; earlier finite passes preserved.
