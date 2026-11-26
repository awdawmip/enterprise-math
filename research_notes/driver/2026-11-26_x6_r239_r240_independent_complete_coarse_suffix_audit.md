# X6 R239/R240 independent full coarse suffix audit

2026-11-26. Independent mathematical reimplementation using packed 32-bit intersections to count exact tagged directed-germ support sets (duplicate components corrected). Frozen input and premises as R239, Port 10, 1935 directions, six BRC, positive weights (17t,B,22t,D), 47 supports/49 components, strict 3/2 near set plus legal optimizer; no re-scoring. Input: 13b49598c381b21e899704d21e8498071c852565:research_notes/portable_direct/2026-11-26_r2_x6_r239_factor_free_reducible_root_xor_capacity.md; compare R240 4bc3061af929f51a8dca388738fe3d3a6dc957d6:research_notes/portable_direct/2026-11-26_r2_x6_r240_factor_free_reducible_suffix_capacity.md. Rebuild complete rank-three linear query bank and factor XOR partitions, direct capacity 31, one-step capacity 15 per child and full exact depth-five recursion. Saturated count requires a support query, count<=depth admits the relaxation by sequential support deletion. Every eligible child query considered unless a true option has already been established. No cutoff. All author direct and one-step counts, full recursive exclusions and exact residual mask multiplicities matched. Combined with independent R241 refinement a776c11796c4586d94f3c3080e7bb095e9e0e4df and earlier independent R238 audit, the full real reducible sole nonlinear root exclusion is independently checked conditional on inherited necessary-wall/rank-three coverage premises. Not a native Review or Result acceptance. Preserve author contribution.

Actual output:
```json
{
  "points": 51,
  "germs": 98,
  "queries": 2225,
  "factors": 2178,
  "total": 2372931,
  "direct": 2296890,
  "afterDirect": 69057,
  "oneExcluded": 50865,
  "onePairs": 55868,
  "afterOne": 18192,
  "checks1": 61641249,
  "excluded": 18189,
  "excludedPairs": 20170,
  "checks2": 36168134,
  "calls": 30285,
  "residual": [
    [
      "33cf330384c0033038fffff0",
      1
    ],
    [
      "33cf330384c003303afffff0",
      1
    ],
    [
      "33cf330384c0233038fffff0",
      1
    ]
  ],
  "memo": [
    0,
    0,
    571,
    1676,
    9783,
    18255
  ]
}
```

Reproduce with the pinned data array:
```js
function coarseAudit(data){
 const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],sg=x=>x>0n?1:x<0n?-1:0,gcd=(a,b)=>b?gcd(b,a%b):a<0n?-a:a,pr=v=>{let g=v.reduce(gcd,0n);return g?v.map(x=>x/g):v},canon=(a,b)=>a<b?a:b;
 let P=[],idmap=new Map(),G=[],tags=[],duplicates=[];function id(v){v=pr(v.map(BigInt));let k=v.join();if(!idmap.has(k)){idmap.set(k,P.length);P.push(v)}return idmap.get(k)}
 for(let d of data){let parts=d.normal.join()==="51,2,-1"?[[["1","9","69"],["3","17","187"]],[["2","5","112"],["1","0","51"]]]:d.normal.join()==="17,-1,0"?[[["0","0","1"],["1","17","391"]],[["1","17","69"],["1","17","22"]]]:[d.endpoints];let t=0n,ds=[];for(let [a,b] of parts){let i=id(a),j=id(b),k=G.length;G.push([i,j],[j,i]);ds.push(k);t|=3n<<BigInt(k)}tags.push(t);if(ds.length===2)duplicates.push(ds)}
 const U=(1n<<BigInt(G.length))-1n,bits=G.map((_,i)=>1n<<BigInt(i)), bank=new Map();
 function masks(z){let a=0n,b=0n;for(let i=0;i<G.length;i++){let [u,v]=G[i],s=z[u]||z[v];if(s>0)a|=bits[i];if(s<0)b|=bits[i]}return a<b?[a,b]:[b,a]}
 function put(z){let [a,b]=masks(z);bank.set(a+","+b,[a,b])}
 let rays=new Map();for(let i=0;i<P.length;i++)for(let j=0;j<i;j++){let v=pr(cross(P[i],P[j]));if(v.every(x=>!x))continue;if(v.find(x=>x)<0n)v=v.map(x=>-x);rays.set(v.join(),v)}
 for(let v of rays.values()){let z=P.map(p=>sg(dot(v,p)));put(z);for(let i=0;i<P.length;i++)if(!z[i]){let w=cross(v,P[i]),y=P.map(p=>sg(dot(w,p))),x=P.map(p=>sg(dot(P[i],p)));for(let a of [-1,1]){put(z.map((v,j)=>v||a*y[j]));for(let b of [-1,1])put(z.map((v,j)=>v||a*y[j]||b*x[j]))}}}
 const words=x=>[0n,32n,64n,96n].map(k=>Number((x>>k)&0xffffffffn)|0),pc=x=>{x=x-((x>>>1)&0x55555555);x=(x&0x33333333)+((x>>>2)&0x33333333);return (((((x+(x>>>4))&0x0f0f0f0f)*0x01010101)>>>24))},occ=x=>(x|(x>>>1))&0x55555555;
 // use packed 32-bit words; duplicate components occupy known even bit positions
 const dd=duplicates.map(p=>p.map(i=>[i>>>5,1<<(i&31)]));
 function count4(a,b,c,d){a=occ(a);b=occ(b);c=occ(c);d=occ(d);let n=pc(a)+pc(b)+pc(c)+pc(d);for(let [[i,x],[j,y]] of dd){let u=i===0?a:i===1?b:i===2?c:d,v=j===0?a:j===1?b:j===2?c:d;if((u&x)&&(v&y))n--}return n}
 function count(s){return count4(...words(s))}
 function pair(q){let [a,b]=q;return {a,b,x:words(a),y:words(b)}}
 const Q=[...bank.values()].map(pair),S=data.map(d=>pair(masks(P.map(p=>sg(dot(p,d.normal.map(BigInt)))))));
 for(let q of [...Q,...S])for(let m of [q.a,q.b,q.a|q.b])if(count(m)!==tags.filter(t=>t&m).length)throw Error("count");
 const F=Q.filter(q=>(q.a|q.b)===U).map(q=>q.a),roots=new Map();let direct=0,total=0;
 for(let i=0;i<F.length;i++)for(let j=0;j<=i;j++){total++;let a=F[i]^F[j],b=U^a;if(count(a)>31||count(b)>31){direct++;continue}a=canon(a,b);roots.set(a,(roots.get(a)||0)+1)}
 let oneMemo=new Map(),checks1=0;function one(s){if(oneMemo.has(s))return oneMemo.get(s);let n=count(s);if(n<=15)return true;let [a,b,c,d]=words(s),ok=false;for(let q of n===31?S:Q){checks1++;let x=q.x,y=q.y;if(count4(a&x[0],b&x[1],c&x[2],d&x[3])<=15&&count4(a&y[0],b&y[1],c&y[2],d&y[3])<=15){ok=true;break}}oneMemo.set(s,ok);return ok}
 let survivors=[],oneExcluded=0,onePairs=0;for(let [a,m] of roots){let b=U^a;let [x,y]=count(a)>=count(b)?[a,b]:[b,a];if(one(x)&&one(y))survivors.push([a,m]);else{oneExcluded++;onePairs+=m}}
 survivors.sort((a,b)=>Math.max(count(b[0]),count(U^b[0]))-Math.max(count(a[0]),count(U^a[0])));
 const memo=Array.from({length:6},()=>new Map());let checks2=0,calls=0;function solve(s,d){let n=count(s);if(n<=d)return true;if(n>2**d-1)return false;let mm=memo[d];if(mm.has(s))return mm.get(s);calls++;let cap=2**(d-1)-1,[a,b,c,f]=words(s),opts=new Map();for(let q of n===2**d-1?S:Q){checks2++;let x=q.x,y=q.y,cx=count4(a&x[0],b&x[1],c&x[2],f&x[3]);if(cx>cap)continue;let cy=count4(a&y[0],b&y[1],c&y[2],f&y[3]);if(cy>cap)continue;if(cx<=d-1&&cy<=d-1){mm.set(s,true);return true}let u=s&q.a,v=s&q.b;if(cx<cy)[u,v,cx,cy]=[v,u,cy,cx];opts.set(u+","+v,[u,v,cx,cy])}let sorted=[...opts.values()].sort((a,b)=>a[2]-b[2]||a[3]-b[3]);for(let [u,v] of sorted)if(solve(u,d-1)&&solve(v,d-1)){mm.set(s,true);return true}mm.set(s,false);return false}
 let residual=[],excluded=0,excludedPairs=0;for(let [a,m] of survivors){let b=U^a;let [x,y]=count(a)>=count(b)?[a,b]:[b,a];if(solve(x,5)&&solve(y,5))residual.push([a.toString(16),m]);else{excluded++;excludedPairs+=m}}
 return {points:P.length,germs:G.length,queries:Q.length,factors:F.length,total,direct,afterDirect:roots.size,oneExcluded,onePairs,afterOne:survivors.length,checks1,excluded,excludedPairs,checks2,calls,residual:residual.sort(),memo:memo.map(x=>x.size)};
}
```
