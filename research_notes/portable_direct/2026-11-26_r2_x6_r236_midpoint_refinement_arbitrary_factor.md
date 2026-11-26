# X6 R236 — exact midpoint refinement of all seven residual arbitrary-second-factor root classes

2026-11-26. AUTHOR EXACT FINITE RELAXATION COMPUTATION / NOT_REVIEWED. Same frozen Port 10 / 1935 directions / six-pair BRC / (17t,B,22t,D)>0 / strict 3/2 near mask plus legal optimum. 47 necessary supports, 49 connected components; static auxiliary weight chart, not native spatial geometry. P000 V5 unchanged. Informed unclaimed research. Inputs R233 c963f003a50e4b329f437e8a96a04d22677a1cde:research_notes/portable_direct/2026-11-26_r2_x6_r233_arbitrary_second_factor_germ_lift.md; R235 486fa2049d9e5134a3943234031ff066bbed95e7:research_notes/portable_direct/2026-11-26_r2_x6_r235_arbitrary_second_factor_coverage.md. No new whole-direction scoring, independent review, or control mutation.

For each original active component with closure rays a,b insert the projective interior ray a+b. Retain four directed germs (a,a+b),(a+b,a),(a+b,b),(b,a+b). Old endpoint germs are exactly the first and fourth fine germs in the sense of eventual signs of every linear form and every product, since the fine segment is a nonempty initial part of the old segment. Thus projection from fine strict masks to coarse masks commutes with the product partition and all linear-query signs; no old excluded root needs testing. Enumerate all linear sign patterns on the fine endpoint bank by the exact R229 arrangement. Test only those support-index × linear-factor partitions whose coarse product root is among the seven surviving R235 masks, and verify the projected support-index × coarse linear-partition count equals the original multiplicity nine. This covers every actual polynomial L_i M in those seven classes, regardless of M's coefficient magnitude. Count distinct support labels, not subcomponents. Apply exact finite pure-linear germ elimination for both root sides, with saturated-node restriction as in R234. False is a rigorous exclusion conditional on the inherited necessary-wall premise; true is only relaxation feasibility. A cutoff yields unknown.

Actual computation:
```json
{"coarseIds":[4497,723,1046,1059,1114,1045,1120],"coarsePairs":9,"supportIndices":[11,13,26,39],"points":99,"germs":196,"rays":4296,"signPatterns":17731,"linearPartitions":13064,"fineRoots":15,"counts":{"excluded":11,"relaxedFeasible":4,"unknown":0},"checks":1682987,"calls":654,"memo":[0,0,48,171,415,20],"limit":12000000,"perCoarse":[{"id":4497,"fine":1,"excluded":1,"feasible":0,"unknown":0},{"id":723,"fine":1,"excluded":1,"feasible":0,"unknown":0},{"id":1046,"fine":3,"excluded":3,"feasible":0,"unknown":0},{"id":1059,"fine":1,"excluded":1,"feasible":0,"unknown":0},{"id":1114,"fine":5,"excluded":2,"feasible":3,"unknown":0},{"id":1045,"fine":3,"excluded":3,"feasible":0,"unknown":0},{"id":1120,"fine":1,"excluded":0,"feasible":1,"unknown":0}]}
```

Every distinct fine root mask (hexadecimal, four consecutive germ bits per original component) and its status:
```json
[{"a":"f09f00fff0f010fff01911fff770f08feff00000ffe0000","b":"ff0f60f0000f0fef000fe6ee00088f0f70100fffff001ffff","id":4497,"m":1,"state":"excluded","labels":[28,30]},{"a":"f0ff0ff0f0f000ff010f000000f0f0000ffffff0ffff300","b":"ff0f00f00f0f0fff00fef0ffffff0f0fff0000000f0000cff","id":1114,"m":1,"state":"excluded","labels":[23,26]},{"a":"f0ff0ff0f0f000ff010f000000f0f0000ffffff0ffff700","b":"ff0f00f00f0f0fff00fef0ffffff0f0fff0000000f00008ff","id":1114,"m":1,"state":"relaxedFeasible","labels":[23,26]},{"a":"f0ff0ff0f0f000ff010f000000f0f0000ffffff0ffff100","b":"ff0f00f00f0f0fff00fef0ffffff0f0fff0000000f0000eff","id":1114,"m":1,"state":"excluded","labels":[23,26]},{"a":"f0ff0ff0f0f000ff010f000000f0f0000f0ffff0ffff100","b":"ff0f00f00f0f0fff00fef0ffffff0f0fff0000000f0000eff","id":723,"m":2,"state":"excluded","labels":[22,26]},{"a":"f0ff0ff0f0f000fffeff1f000ff0f0000ff00070ffff100","b":"ff0f00f00f0f0fff000100e0fff00f0fff000fff8f0000eff","id":1046,"m":1,"state":"excluded","labels":[25,26]},{"a":"f0ff0ff0f0f000fff87f1f000ff0f0000ff000f0ffff100","b":"ff0f00f00f0f0fff000780e0fff00f0fff000fff0f0000eff","id":1059,"m":1,"state":"excluded","labels":[25,26]},{"a":"f0ff0ff0f0f000fff8ff1f000ff0f0000ff00070ffff100","b":"ff0f00f00f0f0fff000700e0fff00f0fff000fff8f0000eff","id":1046,"m":1,"state":"excluded","labels":[25,26]},{"a":"f0ff0ff0f0f000fffcff1f000ff0f0000ff00070ffff100","b":"ff0f00f00f0f0fff000300e0fff00f0fff000fff8f0000eff","id":1046,"m":1,"state":"excluded","labels":[25,26]},{"a":"f0ff0ff0f0f000ff070f000000f0f0000ffffff0ffff700","b":"ff0f00f00f0f0fff00f8f0ffffff0f0fff0000000f00008ff","id":1114,"m":1,"state":"relaxedFeasible","labels":[23,26]},{"a":"f0ff0ff0f0f000ff030f000000f0f0000ffffff0ffff700","b":"ff0f00f00f0f0fff00fcf0ffffff0f0fff0000000f00008ff","id":1114,"m":1,"state":"relaxedFeasible","labels":[23,26]},{"a":"f0ff0ff0f0f000ff070f000000f0f0000ffffff0ffff700","b":"ff0f00f00f0f0fff00f800ffffff0f0fff0000000f00008ff","id":1120,"m":2,"state":"relaxedFeasible","labels":[23,25]},{"a":"f0ff0ff0f0f000fffeff1f000ff0f0000ff000f0ffff100","b":"ff0f00f00f0f0fff000100e0fff00f0fff000fff0f0000eff","id":1045,"m":1,"state":"excluded","labels":[25,25]},{"a":"f0ff0ff0f0f000fff8ff1f000ff0f0000ff000f0ffff100","b":"ff0f00f00f0f0fff000700e0fff00f0fff000fff0f0000eff","id":1045,"m":1,"state":"excluded","labels":[25,25]},{"a":"f0ff0ff0f0f000fffcff1f000ff0f0000ff000f0ffff100","b":"ff0f00f00f0f0fff000300e0fff00f0fff000fff0f0000eff","id":1045,"m":1,"state":"excluded","labels":[25,25]}]
```

Only classes whose all fine masks were excluded are closed; the remaining feasible/unknown fine masks are not output-tree constructions. This is not the unrestricted K6 result; neither arbitrary quadratic roots with no necessary support factor nor later first joint queries are covered.

Reproduction: obtain data and old arrays from R233 (old is second JSON block), ids from R235's third JSON block relaxedFeasible; run the following function in Node.js and compare.
```javascript
function refine(data,old,ids,limit=12000000){
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],abs=x=>x<0n?-x:x,gcd=(a,b)=>b?gcd(b,a%b):abs(a),norm=(a,un=false)=>{let g=a.reduce(gcd,0n);return g?a.map(x=>x/(un&&a.find(Boolean)<0n?-g:g)):a},sg=x=>x>0n?1:x<0n?-1:0;
const N=data.map(e=>e.normal.map(BigInt)),parts=data.map(e=>e.normal.join()==="51,2,-1"?[[["1","9","69"],["3","17","187"]],[["2","5","112"],["1","0","51"]]]:e.normal.join()==="17,-1,0"?[[["0","0","1"],["1","17","391"]],[["1","17","69"],["1","17","22"]]]:[e.endpoints]).map(s=>s.map(pair=>pair.map(p=>p.map(BigInt))));
let P=[],idx=new Map(),G=[],tag=Array(47).fill(0n),even=0n,coarse=[];
function id(p){p=norm(p);let k=p.join();if(!idx.has(k)){idx.set(k,P.length);P.push(p)}return idx.get(k)}
for(let k=0;k<parts.length;k++)for(let [a,b] of parts[k]){if(dot(N[k],a)||dot(N[k],b))throw Error("endpoint");let u=id(a),v=id(b),m=id(a.map((t,i)=>t+b[i]));if(u===v||u===m||v===m)throw Error("degenerate");even|=1n<<BigInt(G.length);coarse.push(G.length,G.length+3);for(let [i,j] of [[u,m],[m,u],[m,v],[v,m]]){let bit=1n<<BigInt(G.length);G.push([i,j,bit]);tag[k]|=bit;}}
if(G.length!==196||coarse.length!==98||N.length!==47)throw Error("dimensions");
let rays=new Map();for(let i=0;i<P.length;i++)for(let j=i+1;j<P.length;j++){let v=norm(cross(P[i],P[j]),true);if(v.some(Boolean))rays.set(v.join(),v)}
const canonical=(a,b)=>a<b?[a,b]:[b,a],mask=s=>{let a=0n,b=0n;for(let [u,v,bit] of G){let z=s[u]||s[v];if(z>0)a|=bit;else if(z<0)b|=bit}return canonical(a,b)};
function project(s){let r=0n;for(let j=0;j<coarse.length;j++)if(s&(1n<<BigInt(coarse[j])))r|=1n<<BigInt(j);return r}
let qs=new Map(),signs=new Set();function add(s){let key=s.join();if(signs.has(key))return;signs.add(key);let [a,b]=mask(s);qs.set(a+","+b,[a,b])}
for(let v of rays.values()){let sv=P.map(p=>sg(dot(v,p)));add(sv);for(let i=0;i<P.length;i++)if(!sv[i]){let w=cross(v,P[i]),sw=P.map((p,j)=>sv[j]?0:sg(dot(w,p))),su=P.map((p,j)=>sv[j]||sw[j]?0:sg(dot(P[i],p)));for(let e of [-1,1]){add(sv.map((z,j)=>z||e*sw[j]));for(let f of [-1,1])add(sv.map((z,j)=>z||e*sw[j]||f*su[j]))}}}
let Q=[...qs.values()],S=N.map(n=>mask(P.map(p=>sg(dot(n,p))))),dup=tag.filter((_,k)=>parts[k].length===2).map(t=>t&even);
function pc32(x){x=x-((x>>>1)&0x55555555);x=(x&0x33333333)+((x>>>2)&0x33333333);return (((x+(x>>>4))&0x0f0f0f0f)*0x01010101)>>>24}
function count(s){let a=(s|(s>>1n)|(s>>2n)|(s>>3n))&even;let n=0;for(let j=0;j<7;j++)n+=pc32(Number((a>>BigInt(32*j))&0xffffffffn));for(let d of dup)if((a&d)===d)n--;return n}
function slow(s){return tag.reduce((n,t)=>n+(t&s?1:0),0)}
for(let [a,b] of Q.concat(S))for(let t of [a,b,a|b])if(count(t)!==slow(t))throw Error("count");
let targets=new Map(ids.map(i=>[old[i].slice(0,2).map(h=>BigInt("0x"+h)).join(","),i])),coarsePairs=new Map(),rootMap=new Map(),targetFine=new Map(ids.map(i=>[i,new Set()]));
let sc=S.map(([a,b])=>[project(a),project(b)]);
for(let [a,b] of Q){let ca=project(a),cb=project(b);for(let i=0;i<S.length;i++){let [cc,cd]=sc[i],k=canonical((ca&cc)|(cb&cd),(ca&cd)|(cb&cc)).join(","),id=targets.get(k);if(id===undefined)continue;let ckey=i+":"+canonical(ca,cb).join(",");coarsePairs.set(ckey,id);let [c,d]=S[i],[u,v]=canonical((a&c)|(b&d),(a&d)|(b&c)),rk=u+","+v;if(canonical(project(u),project(v)).join(",")!==k)throw Error("project");if(!rootMap.has(rk))rootMap.set(rk,[u,v,id,0]);rootMap.get(rk)[3]++;targetFine.get(id).add(rk)}}
let oldMultiplicity=ids.reduce((s,i)=>s+old[i][2],0);if(coarsePairs.size!==oldMultiplicity||[...targetFine.values()].some(s=>!s.size))throw Error("coarse coverage");
const ordered=[...new Map([...S,...Q].map(([a,b])=>[a+","+b,[a,b]])).values()];
let rows=[...rootMap.values()].sort((a,b)=>Math.max(count(b[0]),count(b[1]))-Math.max(count(a[0]),count(a[1])));
let memo=Array.from({length:6},()=>new Map()),checks=0,calls=0;
const CAP={};
function solve(s,d){
let c=count(s);if(c<=d)return true;if(c>(1<<d)-1)return false;let prior=memo[d].get(s);if(prior!==undefined)return prior;calls++;
let cap=(1<<(d-1))-1,bank=c===(1<<d)-1?S:ordered,seen=new Set(),opts=[];
for(let [a,b] of bank){if(checks>=limit)throw CAP;checks++;let [x,y]=canonical(a&s,b&s);let cx=count(x),cy=count(y);if(cx>cap||cy>cap)continue;if(cx<=d-1&&cy<=d-1){memo[d].set(s,true);return true}let key=x+","+y;if(seen.has(key))continue;seen.add(key);opts.push([x,y,cx,cy]);}
opts.sort((a,b)=>Math.max(a[2],a[3])-Math.max(b[2],b[3])||(a[2]+a[3])-(b[2]+b[3]));
for(let [x,y,cx,cy] of opts){if(cx<cy)[x,y]=[y,x];if(solve(x,d-1)&&solve(y,d-1)){memo[d].set(s,true);return true}}
memo[d].set(s,false);return false;
}
let results=[],stopped=false;
for(let [a,b,id,m] of rows){let state="unknown";if(!stopped)try{let x=a,y=b;if(count(x)<count(y))[x,y]=[y,x];state=solve(x,5)&&solve(y,5)?"relaxedFeasible":"excluded"}catch(err){if(err!==CAP)throw err;stopped=true}results.push({a:a.toString(16),b:b.toString(16),id,m,state,labels:[count(a),count(b)]})}
let counts={excluded:0,relaxedFeasible:0,unknown:0};for(let r of results)counts[r.state]++;
return {summary:{coarseIds:ids,coarsePairs:coarsePairs.size,supportIndices:[...new Set([...coarsePairs.keys()].map(x=>Number(x.split(":")[0])))].sort((a,b)=>a-b),points:P.length,germs:G.length,rays:rays.size,signPatterns:signs.size,linearPartitions:Q.length,fineRoots:rows.length,counts,checks,calls,memo:memo.map(x=>x.size),limit,perCoarse:ids.map(i=>({id:i,fine:targetFine.get(i).size,excluded:results.filter(r=>r.id===i&&r.state==="excluded").length,feasible:results.filter(r=>r.id===i&&r.state==="relaxedFeasible").length,unknown:results.filter(r=>r.id===i&&r.state==="unknown").length}))},results};
}
```

Next: refine the residual fine masks using more interior rays or exact local clipping; retain any feasible cases as unresolved.
