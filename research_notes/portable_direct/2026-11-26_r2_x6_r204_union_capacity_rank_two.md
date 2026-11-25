# X6 R204 — Union-pattern necessary capacity certificate and rank-two replay

2026-11-26 Asia/Shanghai. AUTHOR EXACT FINITE NECESSARY-RELAXATION REPLAY / NOT_REVIEWED. Independent informed static BRC auxiliary weight research. Live Researcher identity not confirmed; historical predecessor EM-DIRECT-AE5AD5. Native task lookup r2-20261126-0213-x6-read SUCCEEDED at 2026-11-25T18:13:24.821495Z, Source 077055350d566ed028a6f0d9783594dcdcbbef33, NO_CANONICAL_PUBLICATION_DIRECTORY; this is not an owner projection. No CLAIM or formal Result.

## Scope and reusable lemma

Frozen R203@e89cb0b1bc28f21e4d2aae350bde78450f46d655:research_notes/portable_direct/2026-11-26_r2_x6_r203_twenty_eight_event_rank_two_exclusion.md (blob 48df939382df9436a5e39d1f6a175c7f32778236), R182@502d7abb2fe8470ed2cdabf242c2cc59a0c302ac and census@6945e591116377f9386c7419b6ce31a2b9e8a146:research_notes/portable_direct/x6_r182_rank_two_side_census.json (blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82). R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f: Port 10, 1935 unoriented integer directions, w=(17t,B,22t,D), six joint BRC pair denominators, strict 3/2 near direction set. 47 support lines, 49 components. P000 V5, joint relation observer preservation. This is a static auxiliary coefficient chart, not a new native spatial or physical computation.

Let Q_r be the set of all realizable ternary observation masks on the fixed child endpoint labels in R182, represented by quadruples (au,av,bu,bv). The fixed-endpoint recurrence R203 uses these masks only, with states (u,v,d), constant capacity base cases, and deterministic successor pairs for each mask. Reversing all signs merely exchanges the two successors; hence canonicalizing a quadruple by simultaneously exchanging its two sign pairs preserves feasibility for every state and depth. For pattern banks Q subset Q', F_Q(u,v,d) implies F_Q'(u,v,d): induction on d, since unchanged base cases settle the same states, and any witnessing mask in Q is also in Q', with both children feasible by induction. Thus for any family of relative strata with common ordered support/endpoint labels, the union Q* of their canonical mask banks is a valid further relaxation, and F_Q*(all,all,5)=false proves failure throughout that family. If it passes, the union result alone proves nothing about any individual stratum; use the original per-stratum recurrence. This preserves all original sign possibilities and introduces additional choices only in the necessary relaxation. No cross-stratum actual tree is asserted. The ordered support IDs are checked at every representative; endpoint labels are the original ordered clipped extreme endpoints per support. Equality strata retained separately by R182. No change to original scientific pins.

Implementation: reuse R203 exact geometry, clipping, ternary observation enumeration and fixed-endpoint transitions; split enumeration from recursion, deduplicate by canonical four-mask tuple (exactly the information the recurrence consumes), construct union and fall back to individual checks if needed. BigInt arithmetic for geometry; 31-bit exact support masks. Union proof does not remove any actual observer relation. No assertion of improved total runtime: full per-stratum pattern enumeration still occurs; measure recursive solver calls and patterns separately. All representatives checked against original root masks. No previous exclusions rerun.

## Executed summary

```json
[
  {
    "id": 50,
    "side": 1,
    "supports": 30,
    "events": 30,
    "distinct": 30,
    "strata": 61,
    "passing": 0,
    "unionPatterns": 1543,
    "union": {
      "feasible": false,
      "states": 1,
      "rootLegal": 0
    },
    "individualSolves": 0
  },
  {
    "id": 1474,
    "side": 1,
    "supports": 29,
    "events": 29,
    "distinct": 29,
    "strata": 59,
    "passing": 0,
    "unionPatterns": 1697,
    "union": {
      "feasible": false,
      "states": 2,
      "rootLegal": 3
    },
    "individualSolves": 0
  },
  {
    "id": 1949,
    "side": 1,
    "supports": 28,
    "events": 30,
    "distinct": 29,
    "strata": 59,
    "passing": 0,
    "unionPatterns": 1949,
    "union": {
      "feasible": false,
      "states": 6,
      "rootLegal": 3
    },
    "individualSolves": 0
  },
  {
    "id": 2472,
    "side": 1,
    "supports": 28,
    "events": 30,
    "distinct": 30,
    "strata": 61,
    "passing": 0,
    "unionPatterns": 1515,
    "union": {
      "feasible": false,
      "states": 6,
      "rootLegal": 3
    },
    "individualSolves": 0
  },
  {
    "id": 3110,
    "side": -1,
    "supports": 29,
    "events": 30,
    "distinct": 28,
    "strata": 57,
    "passing": 0,
    "unionPatterns": 1873,
    "union": {
      "feasible": false,
      "states": 9,
      "rootLegal": 1
    },
    "individualSolves": 0
  }
]
```

297 strata, sum of distinct endpoint observation-pattern counts 446587. Newly excluded [50,1474,1949,2472,3110]; conditional on R203, remaining 157 = 69 rank two + 88 rank three. Bound 6<=D_linear<=7 unchanged. Any row not excluded stays open; separate child passes are not full-root feasibility. Next min-31 rows: [{"id":3509,"sides":[[1,59],[-1,31]]}]. Activity association and independent review outstanding.

## Standalone reproduction (Node.js, no dependencies)

```javascript
function replayUnion(data,rows){
const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],sg=x=>x>0n?1:x<0n?-1:0,abs=x=>x<0n?-x:x,gcd=(a,b)=>b?gcd(b,a%b):abs(a),norm=p=>{let d=p.reduce(gcd,0n);return d?p.map(x=>x/d):p},uniq=a=>[...new Map(a.map(p=>[p.join(),p])).values()],add=(a,b)=>norm(a.map((x,j)=>x+b[j]));
const P=uniq(data.flatMap(e=>e.endpoints.map(p=>p.map(BigInt))));
const comps=data.map(e=>({parts:e.normal.join()==="51,2,-1"?[[["1","9","69"],["3","17","187"]],[["2","5","112"],["1","0","51"]]]:e.normal.join()==="17,-1,0"?[[["0","0","1"],["1","17","391"]],[["1","17","69"],["1","17","22"]]]:[e.endpoints]})).map(e=>e.parts.map(pair=>pair.map(p=>p.map(BigInt))));
function clip(r,side){let ret=[],labels=[];for(let i=0;i<comps.length;i++){let e=comps[i],parts=[];for(let [u,v] of e){let a=BigInt(side)*dot(r,u),b=BigInt(side)*dot(r,v);if(a<=0n&&b<=0n)continue;let d=(a<0n||b<0n)?norm(a<0n?u.map((x,j)=>b*x-a*v[j]):v.map((x,j)=>a*x-b*u[j])):null;parts.push([a<0n?d:u,b<0n?d:v])}if(parts.length){ret.push([parts[0][0],parts.at(-1)[1]]);labels.push(i)}}return {pairs:ret,labels}}
const pc=x=>{x=x-((x>>>1)&0x55555555);x=(x&0x33333333)+((x>>>2)&0x33333333);return (((x+(x>>>4))&0x0F0F0F0F)*0x01010101)>>>24};
function patterns(pairs){const N=pairs.length;if(N>31||N<=5)throw Error("unexpected support count");const pp=uniq(pairs.flat()),idx=new Map(pp.map((p,i)=>[p.join(),i])),Q=new Map();
function rec(r,t=null,p=null,s=1,u=1){let a=0n,b=0n;for(let i=0;i<pp.length;i++){let x=sg(dot(r,pp[i]));if(!x&&t)x=s*sg(dot(t,pp[i]));if(!x&&p)x=u*sg(dot(p,pp[i]));if(x>0)a|=1n<<BigInt(i);if(x<0)b|=1n<<BigInt(i)}if(a>b)[a,b]=[b,a];let key=`${a},${b}`;if(Q.has(key))return;let au=0,av=0,bu=0,bv=0;pairs.forEach(([p,q],i)=>{let x=1n<<BigInt(idx.get(p.join())),y=1n<<BigInt(idx.get(q.join())),z=1<<i;if(a&x)au|=z;if(a&y)av|=z;if(b&x)bu|=z;if(b&y)bv|=z});Q.set(key,[au,av,bu,bv])}
for(let i=0;i<pp.length;i++)for(let j=i+1;j<pp.length;j++){let r=cross(pp[i],pp[j]);if(!r.some(Boolean))continue;rec(r);for(let k=0;k<pp.length;k++)if(!dot(r,pp[k])){let t=cross(r,pp[k]);for(let s of [-1,1]){rec(r,t,null,s);for(let u of [-1,1])rec(r,t,pp[k],s,u)}}}
if(!Q.size)throw Error("unexpected rank-one carrier");return [...Q.values()]}
function canonical(q){let [a,b,c,d]=q;return a<c||(a===c&&b<=d)?q:[c,d,a,b]}
function solvePatterns(N,qs){const all=2**N-1,cache=new Map();let states=0,rootLegal=0;
function solve(u,v,d){let n=pc(u|v);if(n>2**d-1)return false;if(n<=d)return true;let key=`${u},${v},${d}`;if(cache.has(key))return cache.get(key);states++;let ans=false,limit=2**(d-1)-1;for(let [au,av,bu,bv] of qs){let pa=(u&au)|(v&av),pb=(u&bu)|(v&bv),a=u&~bu&pa,b=v&~bv&pa,c=u&~au&pb,e=v&~av&pb;if(pc(a|b)>limit||pc(c|e)>limit)continue;if(d===5)rootLegal++;if(solve(a,b,d-1)&&solve(c,e,d-1)){ans=true;break}}cache.set(key,ans);return ans}
return {feasible:solve(all,all,5),states,rootLegal}}
function side(c,s){let a=BigInt(c.a),b=BigInt(c.b);function valid(r,strict=false){return P.every((p,i)=>{let x=sg(dot(r,p)),bit=1n<<BigInt(i);return (a&bit)?(strict?x===1:x>=0):(b&bit)?(strict?x===-1:x<=0):x===0})}
let [u,v]=c.vertices.map(p=>p.map(BigInt));if(!valid(u)||!valid(v))throw Error("bad vertex");let events=new Map();for(let z of s.events){let x=z.split(",").map(BigInt),A=dot(x,u),B=dot(x,v);if(A*B>=0n)throw Error("not varying");let alpha=abs(B),beta=abs(A),r=norm(u.map((x,j)=>alpha*x+beta*v[j]));events.set(r.join(),{r,alpha,beta})}
let list=[{r:u,alpha:1n,beta:0n},...[...events.values()].sort((a,b)=>sg(a.beta*b.alpha-b.beta*a.alpha)),{r:v,alpha:0n,beta:1n}],reps=[];for(let i=0;i+1<list.length;i++){reps.push({kind:"open",r:add(list[i].r,list[i+1].r)});if(i+1<list.length-1)reps.push({kind:"event",r:list[i+1].r})}
let results=[],bank=new Map(),allQ=[],labels=null;
for(let q of reps){if(!valid(q.r,true))throw Error("representative outside class");let clipped=clip(q.r,s.side);if(clipped.pairs.length!==s.supports)throw Error("support count mismatch");if(labels===null)labels=clipped.labels;else if(labels.join()!==clipped.labels.join())throw Error("support labels changed");let Q=patterns(clipped.pairs);let local=new Map();for(let m of Q){let n=canonical(m);local.set(n.join(),n);bank.set(n.join(),n)}allQ.push([...local.values()]);results.push({kind:q.kind,r:q.r.map(String),patterns:Q.length,distinctMaskPatterns:local.size})}
let union=solvePatterns(s.supports,[...bank.values()]);
if(!union.feasible){for(let x of results){x.feasible=false;x.proof="union"}}
else for(let i=0;i<results.length;i++){let y=solvePatterns(s.supports,allQ[i]);Object.assign(results[i],y,{proof:"individual"})}
return {i:c.i,side:s.side,supports:s.supports,labels,events:s.events.length,distinct:events.size,unionPatterns:bank.size,union,results,excluded:results.every(x=>!x.feasible)}}
let output=[];for(let c of rows){let s=[...c.sides].sort((a,b)=>a.events.length-b.events.length);let q=side(c,s[0]);output.push(q);if(!q.excluded)output.push(side(c,s[1]))}
return {output,excluded:[...new Set(output.filter(x=>x.excluded).map(x=>x.i))],strata:output.reduce((n,x)=>n+x.results.length,0),totalPatterns:output.reduce((n,x)=>n+x.results.reduce((m,y)=>m+y.patterns,0),0)}}
const data=[{"normal":["187","12","-1"],"segments":9,"endpoints":[["0","1","12"],["1","17","391"]]},{"normal":["204","11","-1"],"segments":9,"endpoints":[["0","1","11"],["1","17","391"]]},{"normal":["5","-2","0"],"segments":51,"endpoints":[["2","5","73"],["2","5","5"]]},{"normal":["9","-1","0"],"segments":4,"endpoints":[["1","9","74"],["1","9","69"]]},{"normal":["85","7","-2"],"segments":10,"endpoints":[["1","9","74"],["3","17","187"]]},{"normal":["51","2","-1"],"segments":9,"endpoints":[["1","9","69"],["1","0","51"]]},{"normal":["0","1","-1"],"segments":2,"endpoints":[["2","5","5"],["1","0","0"]]},{"normal":["34","1","-1"],"segments":7,"endpoints":[["2","5","73"],["1","0","34"]]},{"normal":["187","20","-9"],"segments":5,"endpoints":[["6","15","158"],["1","1","23"]]},{"normal":["68","1","-3"],"segments":8,"endpoints":[["2","5","47"],["3","0","68"]]},{"normal":["176","22","-9"],"segments":4,"endpoints":[["6","15","154"],["19","28","440"]]},{"normal":["22","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","22"]]},{"normal":["61","0","-1"],"segments":78,"endpoints":[["0","1","0"],["1","17","61"]]},{"normal":["74","0","-1"],"segments":14,"endpoints":[["1","9","74"],["1","4","74"]]},{"normal":["126","0","-1"],"segments":103,"endpoints":[["0","1","0"],["1","30","126"]]},{"normal":["4","-1","0"],"segments":35,"endpoints":[["1","4","152"],["1","4","74"]]},{"normal":["17","-1","0"],"segments":44,"endpoints":[["0","0","1"],["1","17","22"]]},{"normal":["156","-1","-1"],"segments":46,"endpoints":[["1","4","152"],["1","30","126"]]},{"normal":["69","0","-1"],"segments":16,"endpoints":[["1","17","69"],["1","9","69"]]},{"normal":["9","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","9"]]},{"normal":["235","0","-3"],"segments":84,"endpoints":[["0","1","0"],["3","77","235"]]},{"normal":["87","0","-1"],"segments":107,"endpoints":[["0","1","0"],["1","17","87"]]},{"normal":["104","-1","-1"],"segments":60,"endpoints":[["1","4","100"],["3","77","235"]]},{"normal":["38","0","-3"],"segments":57,"endpoints":[["0","1","0"],["3","40","38"]]},{"normal":["5","0","-2"],"segments":72,"endpoints":[["0","1","0"],["2","5","5"]]},{"normal":["39","-1","-1"],"segments":50,"endpoints":[["3","1","116"],["1","17","22"]]},{"normal":["40","0","-3"],"segments":63,"endpoints":[["0","1","0"],["3","38","40"]]},{"normal":["26","-1","-1"],"segments":39,"endpoints":[["2","5","47"],["3","53","25"]]},{"normal":["25","0","-3"],"segments":52,"endpoints":[["0","1","0"],["3","53","25"]]},{"normal":["83","0","-2"],"segments":69,"endpoints":[["0","1","0"],["2","34","83"]]},{"normal":["102","-7","-1"],"segments":14,"endpoints":[["1","4","74"],["3","17","187"]]},{"normal":["204","-11","1"],"segments":51,"endpoints":[["0","1","11"],["1","30","126"]]},{"normal":["395","0","-2"],"segments":119,"endpoints":[["0","1","0"],["2","73","395"]]},{"normal":["289","18","-1"],"segments":10,"endpoints":[["0","1","18"],["1","17","595"]]},{"normal":["66","2","-1"],"segments":11,"endpoints":[["1","4","74"],["1","0","66"]]},{"normal":["132","5","-1"],"segments":16,"endpoints":[["1","17","217"],["1","0","132"]]},{"normal":["44","1","-1"],"segments":9,"endpoints":[["1","17","61"],["1","11","55"]]},{"normal":["88","3","-1"],"segments":7,"endpoints":[["1","4","100"],["1","0","88"]]},{"normal":["88","7","-3"],"segments":5,"endpoints":[["1","17","69"],["1","11","55"]]},{"normal":["132","-7","-1"],"segments":14,"endpoints":[["1","9","69"],["1","11","55"]]},{"normal":["153","8","-1"],"segments":7,"endpoints":[["1","9","225"],["1","0","153"]]},{"normal":["153","5","-4"],"segments":1,"endpoints":[["3","1","116"],["4","0","153"]]},{"normal":["117","-2","-2"],"segments":42,"endpoints":[["2","5","112"],["2","34","83"]]},{"normal":["198","8","-1"],"segments":5,"endpoints":[["1","4","230"],["1","0","198"]]},{"normal":["198","5","-4"],"segments":11,"endpoints":[["2","8","109"],["2","0","99"]]},{"normal":["306","17","-1"],"segments":8,"endpoints":[["1","17","595"],["1","0","306"]]},{"normal":["234","-1","-1"],"segments":43,"endpoints":[["1","4","230"],["2","73","395"]]}];
const rows=[{"i":50,"a":"1132515426405","b":"2250667298258826","r":["-1055","453","-31"],"local":121,"vertices":[["-55","24","-2"],["-1000","429","-29"]],"sides":[{"side":1,"supports":30,"events":["1,13,143","1,18,216","1,204,2448","1,4,22","1,9,95","11,4373,54533","11,83,814","12,113,1135","12,2297,27715","13,3851,48643","137,958,8903","147,1073,10003","166,1053,8658","17,115,1097","18,73,395","2,39,429","24,2179,28865","3,203,2845","3,25,222","3,38,430","3,40,428","3,53,649","37,4171,56971","4,673,8219","47,383,3478","60,527,5713","7,53,483","7,58,518","9,71,631","9,73,638"]},{"side":-1,"supports":29,"events":["1,10,94","1,100,1304","1,13,143","1,133,1667","1,1409,17095","1,178,2162","1,183,2383","1,220,2827","1,365,4567","1,4,22","1,5,34","1,544,6715","1,8,74","1,9,95","10,47,343","10,63,522","10,66,519","11,1088,14212","11,188,2386","11,200,2374","11,74,709","126,2291,27193","128,833,6655","13,120,1232","13,1236,16248","13,1496,20383","13,180,1848","13,1903,25267","13,3179,40579","13,5267,65635","13,5828,72367","14,1717,23222","143,53761,671873","15,1241,16711","16,81,543","17,143,1258","173,1560,16432","173,2340,24648","18,136,1241","18,140,1255","187,18317,239635","19,245,2719","19,336,4110","19,89,652","191,18385,241199","2,15,132","2,35,433","2,39,429","2,395,4753","21,188,1996","215,1952,20408","216,1319,11317","23,179,1604","23,287,3301","23,443,4939","260,1581,13629","28,165,1473","3,40,428","3,515,6277","3,56,646","31,120,686","33,313,3119","34,3101,41047","37,255,2397","4,493,6664","41,320,3034","47,370,3478","47,383,3478","479,2387,16294","49,248,1663","49,610,7034","5,3689,45203","5,578,7378","5,612,7752","5,708,8808","5,986,12767","50,8419,110378","52,8453,111160","53,1044,11358","59,425,3995","6,1003,12257","61,408,3927","618,5653,58619","63,304,2153","63,307,2150","63,775,9053","7,544,7412","7,960,11988","705,13457,151513","705,9011,100969","71,589,5254","717,13525,154253","717,9079,102773","73,9796,122648","83,422,2815","87,835,8213","94,558,4941"]}]},{"i":1474,"a":"1115335686680","b":"2250684477998503","r":["447","73","-16"],"local":103,"vertices":[["306","35","-9"],["1482","257","-55"]],"sides":[{"side":1,"supports":29,"events":["1,1,35","1,34,170","11,17,391","11,2,376","14,550,2765","16,623,3160","16,649,3160","17,601,3143","174,6715,34365","18,683,3555","19,28,674","19,28,713","196,1075,10391","2,47,265","2,79,395","2,82,395","23,820,4328","25,867,4437","26,135,1386","3,41,271","32,1207,6320","346,12746,68335","346,1755,18486","412,367,14375","61,1436,8080","68,2755,13430","706,26471,139435","8,13,299","99,2437,13007"]},{"side":-1,"supports":26,"events":["1,1,35","1,2,37","1,24,132","10,392,1975","1007,119,34357","106,4165,20935","107,170,3808","11,17,391","11,21,395","11,8,382","113,68,3910","115,34,3944","12,13,455","12,17,425","139,153,4879","14,74,745","149,54,5120","1619,323,55369","166,833,8878","166,909,8802","17,23,601","17,32,610","17,6,584","173,10,5892","179,4239,23685","18,98,955","19,28,713","19,37,704","19,39,702","190,7052,37525","192,23,6551","2,3,75","20,107,1063","20,11,691","215,119,7429","22,882,4345","233,394,8693","25,43,893","253,8721,44319","27,628,3584","281,98,9652","293,167,10129","3,1,103","3,41,271","3,5,112","3,73,395","304,371,11485","32,175,1697","329,62,11248","34,1274,6715","344,119,11815","369,734,13657","37,1292,6664","37,34,1292","38,17,1309","41,5,1399","479,164,16450","49,1171,6473","49,1769,9463","5,2,172","50,252,2673","51,4,1738","563,140,19282","59,2142,11526","6,244,1185","6,31,320","641,1037,22831","66,1543,8753","67,31,2309","7,13,260","71,2429,12235","8,13,299","80,2943,15800","803,272,27574","83,32,2854","85,154,3044","9,16,335","9,323,1717","90,3137,16147"]}]},{"i":1949,"a":"863133305405208","b":"1388666491502823","r":["1213","22","-23"],"local":58,"vertices":[["867","18","-17"],["1559","26","-29"]],"sides":[{"side":1,"supports":28,"events":["1,1,53","1,10,62","1,2,55","1,37,87","12,17,646","138,85,7208","1394,207778,275315","147,4007,11515","19,28,1025","190,30374,37525","2,295,395","2,307,395","2,7,110","201,5291,15745","21,551,1645","226,35666,44635","3,1,155","3,5,163","30,777,2350","36,5245,7110","38,17,1972","4,7,218","44,6715,8690","6,856,1185","67,2439,5829","7,17,391","7,255,609","74,11242,14615","83,2958,7221","863,71,44155"]},{"side":-1,"supports":27,"events":["1016,2881,56555","108,289,6029","11,17,595","12,17,646","134,10065,16884","139,153,7395","16,23,862","16,2367,3160","176,535,9761","18,64,989","2,6,111","2,7,110","2,73,174","21,209,1309","220,711,12159","23,51,1275","25,17,1309","265,527,14569","268,40007,52930","3,7,167","356,1255,19571","36,937,2820","37,34,1955","38,113,2110","38,117,2106","54,1477,4230","67,2322,5829","7,17,391","7,249,609","72,1913,5640","8,27,441"]}]},{"i":2472,"a":"1115201448464","b":"2250684612232687","r":["583","107","-30"],"local":70,"vertices":[["564","103","-29"],["19","4","-1"]],"sides":[{"side":1,"supports":28,"events":["1,28,128","10,181,859","10,183,857","114,5279,22515","1204,59715,237790","138,6715,27255","142,6977,28045","145,2751,12615","15,199,1035","167,3073,14529","169,3071,14703","1954,97373,385915","2,99,395","266,11975,52535","3,38,207","3,40,207","3,52,260","3,53,259","3,53,261","38,1745,7505","38,308,1915","394,18931,77815","42,1975,8295","42,2077,8295","5,69,345","5,87,435","81,2392,10244","82,4033,16195","92,4575,18170","93,2828,12136"]},{"side":-1,"supports":31,"events":["1,18,87","1,29,127","10,25,287","107,3290,14362","109,3361,14735","11,336,1452","110,938,5497","12,355,1517","120,1003,6017","13,225,1131","14,640,2765","149,4563,19797","15,476,2176","151,1606,8690","17,235,1173","18,187,1067","19,327,1649","2,16,101","202,9843,39895","27,823,3545","28,845,3583","29,391,2001","3,53,259","32,945,4047","35,1037,4423","38,303,1920","386,17833,76235","395,5037,27255","46,1445,6511","49,1390,6254","5,143,637","57,236,1987","59,245,2056","61,1700,7816","650,5458,32567","67,1917,8535","67,2023,8585","7,72,420","76,2295,9741","82,3822,16195","83,351,2886"]}]},{"i":3110,"a":"909991667171320","b":"1341808146251783","r":["931","-47","-6"],"local":87,"vertices":[["192","-10","-1"],["2601","-131","-17"]],"sides":[{"side":1,"supports":31,"events":["1,1,161","1,11,69","1,3,147","1,4,132","1,4,134","1,9,95","11,44,1594","12,113,1135","12,17,1972","129,328,18668","13,120,1232","13,52,1882","14,171,966","14,187,803","162,1315,15533","173,1560,16432","188,3573,470","19,28,3131","2,15,193","2,5,289","21,157,2027","21,176,2008","215,1952,20408","23,183,2209","249,902,37378","27,212,2596","29,55,4103","3,1,467","3,26,286","3,38,170","3,40,172","31,579,279","33,244,3188","33,313,3119","346,6731,865","35,13,5459","37,135,5559","4,59,175","42,779,378","44,859,110","478,9063,1195","54,1024,135","554,10744,1385","57,422,5506","57,436,5492","6,115,15","60,527,5713","618,5653,58619","62,1197,155","69,146,9838","7,11,1159","705,6047,67273","717,6115,68453","74,1075,3254","87,1627,725","87,835,8213","9,11,1465","9,114,530","9,68,868","93,1672,1240","93,1682,1178","93,1721,775"]},{"side":-1,"supports":29,"events":["1,11,69","1,2,169","1,4,126","1,4,135","1,4,140","1,8,96","1,9,95","10,131,571","1058,20638,2645","1101,20309,9175","13,19,2141","13,47,1951","16,231,705","16,233,703","17,29,2833","19,21,3075","21,188,1996","23,258,1587","24,353,1051","29,51,4845","3,1,467","3,26,286","32,415,1907","35,88,5060","367,6759,3303","38,555,1668","5,9,837","7,15,999","72,1393,180","9,68,868"]}]}];
console.log(JSON.stringify(replayUnion(data,rows),null,2));
```

## Complete actual output

```json
{
  "output": [
    {
      "i": 50,
      "side": 1,
      "supports": 30,
      "labels": [
        0,
        1,
        3,
        4,
        5,
        11,
        12,
        13,
        14,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        31,
        32,
        36,
        38,
        39,
        42,
        46
      ],
      "events": 30,
      "distinct": 30,
      "unionPatterns": 1543,
      "union": {
        "feasible": false,
        "states": 1,
        "rootLegal": 0
      },
      "results": [
        {
          "kind": "open",
          "r": [
            "-2255",
            "983",
            "-81"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-11220",
            "4891",
            "-403"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-14045",
            "6122",
            "-504"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-2825",
            "1231",
            "-101"
          ],
          "patterns": 1353,
          "distinctMaskPatterns": 1353,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-33185",
            "14458",
            "-1184"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-63545",
            "27685",
            "-2267"
          ],
          "patterns": 1353,
          "distinctMaskPatterns": 1353,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-32265",
            "14057",
            "-1151"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-985",
            "429",
            "-35"
          ],
          "patterns": 1353,
          "distinctMaskPatterns": 1353,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-3285",
            "1430",
            "-116"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-2300",
            "1001",
            "-81"
          ],
          "patterns": 1349,
          "distinctMaskPatterns": 1349,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-7055",
            "3070",
            "-248"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-18865",
            "8209",
            "-663"
          ],
          "patterns": 1353,
          "distinctMaskPatterns": 1353,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-19840",
            "8633",
            "-697"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-975",
            "424",
            "-34"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-545",
            "237",
            "-19"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-115",
            "50",
            "-4"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-27905",
            "12129",
            "-967"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-83600",
            "36337",
            "-2897"
          ],
          "patterns": 1353,
          "distinctMaskPatterns": 1353,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-14400",
            "6259",
            "-499"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-2800",
            "1217",
            "-97"
          ],
          "patterns": 1353,
          "distinctMaskPatterns": 1353,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-18275",
            "7938",
            "-628"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-15475",
            "6721",
            "-531"
          ],
          "patterns": 1353,
          "distinctMaskPatterns": 1353,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-239435",
            "103942",
            "-8168"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-223960",
            "97221",
            "-7637"
          ],
          "patterns": 1353,
          "distinctMaskPatterns": 1353,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-261985",
            "113707",
            "-8913"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-38025",
            "16486",
            "-1276"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-39965",
            "17327",
            "-1341"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-1940",
            "841",
            "-65"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-985",
            "427",
            "-33"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-30",
            "13",
            "-1"
          ],
          "patterns": 1353,
          "distinctMaskPatterns": 1353,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-545",
            "236",
            "-18"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-2150",
            "931",
            "-71"
          ],
          "patterns": 1349,
          "distinctMaskPatterns": 1349,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-4705",
            "2036",
            "-154"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-2555",
            "1105",
            "-83"
          ],
          "patterns": 1353,
          "distinctMaskPatterns": 1353,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-3205",
            "1386",
            "-104"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-650",
            "281",
            "-21"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-67365",
            "29086",
            "-2140"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-66715",
            "28805",
            "-2119"
          ],
          "patterns": 1353,
          "distinctMaskPatterns": 1353,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-111365",
            "48076",
            "-3530"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-44650",
            "19271",
            "-1411"
          ],
          "patterns": 1353,
          "distinctMaskPatterns": 1353,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-3260",
            "1407",
            "-103"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-990",
            "427",
            "-31"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-1475",
            "636",
            "-46"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-1960",
            "845",
            "-61"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-41685",
            "17966",
            "-1292"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-39725",
            "17121",
            "-1231"
          ],
          "patterns": 1353,
          "distinctMaskPatterns": 1353,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-25545",
            "11008",
            "-790"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-88000",
            "37919",
            "-2719"
          ],
          "patterns": 1353,
          "distinctMaskPatterns": 1353,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-45490",
            "19601",
            "-1405"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-2980",
            "1283",
            "-91"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-6635",
            "2856",
            "-202"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-3655",
            "1573",
            "-111"
          ],
          "patterns": 1347,
          "distinctMaskPatterns": 1347,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-4085",
            "1758",
            "-124"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-430",
            "185",
            "-13"
          ],
          "patterns": 1353,
          "distinctMaskPatterns": 1353,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-3410",
            "1465",
            "-101"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-13210",
            "5675",
            "-391"
          ],
          "patterns": 1353,
          "distinctMaskPatterns": 1353,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-2265",
            "973",
            "-67"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-4910",
            "2109",
            "-145"
          ],
          "patterns": 1353,
          "distinctMaskPatterns": 1353,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-17875",
            "7672",
            "-522"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-12965",
            "5563",
            "-377"
          ],
          "patterns": 1353,
          "distinctMaskPatterns": 1353,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-1995",
            "856",
            "-58"
          ],
          "patterns": 1359,
          "distinctMaskPatterns": 1359,
          "feasible": false,
          "proof": "union"
        }
      ],
      "excluded": true
    },
    {
      "i": 1474,
      "side": 1,
      "supports": 29,
      "labels": [
        2,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        14,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        31,
        32,
        36,
        38,
        39,
        42
      ],
      "events": 29,
      "distinct": 29,
      "unionPatterns": 1697,
      "union": {
        "feasible": false,
        "states": 2,
        "rootLegal": 3
      },
      "results": [
        {
          "kind": "open",
          "r": [
            "1776",
            "209",
            "-53"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "3246",
            "383",
            "-97"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "18339",
            "2179",
            "-550"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "15093",
            "1796",
            "-453"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "20319",
            "2442",
            "-613"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "25545",
            "3088",
            "-773"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "9216",
            "1115",
            "-279"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "2103",
            "257",
            "-64"
          ],
          "patterns": 1475,
          "distinctMaskPatterns": 1475,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "2919",
            "358",
            "-89"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "816",
            "101",
            "-25"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "17157",
            "2157",
            "-530"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "16341",
            "2056",
            "-505"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "42783",
            "5397",
            "-1324"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "69225",
            "8738",
            "-2143"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "2067",
            "261",
            "-64"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1053",
            "136",
            "-33"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "699",
            "91",
            "-22"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "345",
            "46",
            "-11"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "8349",
            "1127",
            "-268"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "8004",
            "1081",
            "-257"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "1650",
            "223",
            "-53"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1896",
            "257",
            "-61"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "5211",
            "709",
            "-168"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "3315",
            "452",
            "-107"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "16380",
            "2251",
            "-531"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "13065",
            "1799",
            "-424"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "3297",
            "454",
            "-107"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "123",
            "17",
            "-4"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "213",
            "30",
            "-7"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1794",
            "253",
            "-59"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "16341",
            "2309",
            "-538"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "14547",
            "2056",
            "-479"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "168597",
            "24415",
            "-5628"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "154050",
            "22359",
            "-5149"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "90207",
            "13115",
            "-3018"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "26364",
            "3871",
            "-887"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "13611",
            "1999",
            "-458"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "858",
            "127",
            "-29"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "7449",
            "1112",
            "-253"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "6591",
            "985",
            "-224"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "21723",
            "3298",
            "-745"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "15132",
            "2313",
            "-521"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "7725",
            "1181",
            "-266"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "318",
            "49",
            "-11"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "2991",
            "465",
            "-104"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "17628",
            "2741",
            "-613"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "44031",
            "6853",
            "-1532"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "26403",
            "4112",
            "-919"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "1149",
            "179",
            "-40"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1173",
            "184",
            "-41"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "572757",
            "90905",
            "-20158"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "571584",
            "90721",
            "-20117"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "286536",
            "45481",
            "-10085"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1488",
            "241",
            "-53"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "561",
            "91",
            "-20"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "195",
            "32",
            "-7"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "88218",
            "14831",
            "-3213"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "264459",
            "44461",
            "-9632"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "88647",
            "14906",
            "-3229"
          ],
          "patterns": 1485,
          "distinctMaskPatterns": 1485,
          "feasible": false,
          "proof": "union"
        }
      ],
      "excluded": true
    },
    {
      "i": 1949,
      "side": 1,
      "supports": 28,
      "labels": [
        2,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        14,
        16,
        19,
        20,
        21,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        32,
        36,
        38,
        39,
        41,
        42,
        44
      ],
      "events": 30,
      "distinct": 29,
      "unionPatterns": 1949,
      "union": {
        "feasible": false,
        "states": 6,
        "rootLegal": 3
      },
      "results": [
        {
          "kind": "open",
          "r": [
            "47042",
            "971",
            "-921"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "93217",
            "1924",
            "-1825"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "26720",
            "551",
            "-523"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "13663",
            "280",
            "-267"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "7473",
            "153",
            "-146"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1283",
            "26",
            "-25"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "1335",
            "27",
            "-26"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1387",
            "28",
            "-27"
          ],
          "patterns": 1705,
          "distinctMaskPatterns": 1705,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "16869",
            "339",
            "-328"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "32351",
            "650",
            "-629"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "74511",
            "1482",
            "-1445"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "116671",
            "2314",
            "-2261"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "31118",
            "617",
            "-603"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "38919",
            "771",
            "-754"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "43946",
            "869",
            "-851"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "5027",
            "98",
            "-97"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "26867",
            "518",
            "-517"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "48707",
            "938",
            "-937"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "48759",
            "939",
            "-938"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "52",
            "1",
            "-1"
          ],
          "patterns": 1705,
          "distinctMaskPatterns": 1705,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "34441",
            "661",
            "-662"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "241035",
            "4626",
            "-4633"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "254675",
            "4883",
            "-4894"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "13640",
            "257",
            "-261"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "23449",
            "439",
            "-448"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "9809",
            "182",
            "-187"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "9666136",
            "179311",
            "-184267"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "9656327",
            "179129",
            "-184080"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "1934364",
            "35883",
            "-36875"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "15493",
            "286",
            "-295"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "48419",
            "890",
            "-921"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "81345",
            "1494",
            "-1547"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "41279",
            "758",
            "-785"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1213",
            "22",
            "-23"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "528456",
            "9531",
            "-10007"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "527243",
            "9509",
            "-9984"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "530466",
            "9567",
            "-10045"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "3223",
            "58",
            "-61"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "79707",
            "1428",
            "-1507"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "315605",
            "5654",
            "-5967"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "330073",
            "5911",
            "-6240"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "14468",
            "257",
            "-273"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "15265",
            "271",
            "-288"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "797",
            "14",
            "-15"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "35396",
            "617",
            "-665"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "34599",
            "603",
            "-650"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "19110",
            "333",
            "-359"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "3621",
            "63",
            "-68"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "25085",
            "428",
            "-469"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1702159",
            "29041",
            "-31824"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "1722341",
            "29384",
            "-32201"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "20182",
            "343",
            "-377"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "22919",
            "389",
            "-428"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "2737",
            "46",
            "-51"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "3274",
            "55",
            "-61"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "537",
            "9",
            "-10"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "729209",
            "12212",
            "-13577"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1457881",
            "24415",
            "-27144"
          ],
          "patterns": 1711,
          "distinctMaskPatterns": 1711,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "1459440",
            "24441",
            "-27173"
          ],
          "patterns": 1717,
          "distinctMaskPatterns": 1717,
          "feasible": false,
          "proof": "union"
        }
      ],
      "excluded": true
    },
    {
      "i": 2472,
      "side": 1,
      "supports": 28,
      "labels": [
        2,
        6,
        8,
        9,
        10,
        11,
        12,
        14,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        31,
        32,
        36,
        38,
        39,
        42
      ],
      "events": 30,
      "distinct": 30,
      "unionPatterns": 1515,
      "union": {
        "feasible": false,
        "states": 6,
        "rootLegal": 3
      },
      "results": [
        {
          "kind": "open",
          "r": [
            "2877",
            "527",
            "-148"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "25329",
            "4640",
            "-1303"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "1878993",
            "345613",
            "-96722"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1853664",
            "340973",
            "-95419"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "176429",
            "32457",
            "-9082"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "87055",
            "16054",
            "-4483"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "203785",
            "37692",
            "-10499"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1135655",
            "210098",
            "-58511"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "1136276",
            "210213",
            "-58543"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "621",
            "115",
            "-32"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "2503",
            "464",
            "-129"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1882",
            "349",
            "-97"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "20679",
            "3839",
            "-1066"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "39476",
            "7329",
            "-2035"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "58020",
            "10819",
            "-2993"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "76564",
            "14309",
            "-3951"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "19979",
            "3734",
            "-1031"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "3352",
            "627",
            "-173"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "67889",
            "12703",
            "-3504"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "132426",
            "24779",
            "-6835"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "88599",
            "16580",
            "-4573"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "44772",
            "8381",
            "-2311"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "16280",
            "3063",
            "-841"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "52908",
            "9997",
            "-2735"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "90049",
            "17039",
            "-4656"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "127190",
            "24081",
            "-6577"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "2823",
            "535",
            "-146"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "28075",
            "5344",
            "-1453"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "31379",
            "5973",
            "-1624"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "3304",
            "629",
            "-171"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "180451",
            "34691",
            "-9354"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "357598",
            "68753",
            "-18537"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "385563",
            "74161",
            "-19988"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "27965",
            "5408",
            "-1451"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "14339",
            "2773",
            "-744"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "713",
            "138",
            "-37"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "790",
            "153",
            "-41"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "77",
            "15",
            "-4"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "37207",
            "7344",
            "-1937"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "37130",
            "7329",
            "-1933"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "18613",
            "3674",
            "-969"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "96",
            "19",
            "-5"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "115",
            "23",
            "-6"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "479",
            "96",
            "-25"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "33127",
            "6663",
            "-1730"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "98902",
            "19893",
            "-5165"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "20125",
            "4048",
            "-1051"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1723",
            "347",
            "-90"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "11451",
            "2326",
            "-599"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "32630",
            "6631",
            "-1707"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "497",
            "101",
            "-26"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "172",
            "35",
            "-9"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "554",
            "113",
            "-29"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "936",
            "191",
            "-49"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "191",
            "39",
            "-10"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "783",
            "160",
            "-41"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "725",
            "149",
            "-38"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "667",
            "138",
            "-35"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "223557",
            "46555",
            "-11744"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "222890",
            "46417",
            "-11709"
          ],
          "patterns": 1301,
          "distinctMaskPatterns": 1301,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "222909",
            "46421",
            "-11710"
          ],
          "patterns": 1307,
          "distinctMaskPatterns": 1307,
          "feasible": false,
          "proof": "union"
        }
      ],
      "excluded": true
    },
    {
      "i": 3110,
      "side": -1,
      "supports": 29,
      "labels": [
        0,
        1,
        11,
        12,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        26,
        28,
        29,
        31,
        32,
        33,
        35,
        36,
        38,
        40,
        42,
        43,
        45,
        46
      ],
      "events": 30,
      "distinct": 28,
      "unionPatterns": 1873,
      "union": {
        "feasible": false,
        "states": 9,
        "rootLegal": 1
      },
      "results": [
        {
          "kind": "open",
          "r": [
            "1135",
            "-59",
            "-6"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "943",
            "-49",
            "-5"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "11654",
            "-604",
            "-63"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "10711",
            "-555",
            "-58"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "12371",
            "-641",
            "-67"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "14031",
            "-727",
            "-76"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "47637",
            "-2467",
            "-259"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "81243",
            "-4207",
            "-442"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "91344",
            "-4730",
            "-497"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "10101",
            "-523",
            "-55"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "2744",
            "-142",
            "-15"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "47523",
            "-2459",
            "-260"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "169173",
            "-8753",
            "-926"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "290823",
            "-15047",
            "-1592"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "298586",
            "-15448",
            "-1635"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "7763",
            "-401",
            "-43"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "43742",
            "-2256",
            "-245"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "35979",
            "-1855",
            "-202"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "1959",
            "-101",
            "-11"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "7119",
            "-367",
            "-40"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "8361",
            "-431",
            "-47"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1242",
            "-64",
            "-7"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "2659",
            "-137",
            "-15"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1417",
            "-73",
            "-8"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "3709",
            "-191",
            "-21"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "2292",
            "-118",
            "-13"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "2467",
            "-127",
            "-14"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "175",
            "-9",
            "-1"
          ],
          "patterns": 1669,
          "distinctMaskPatterns": 1669,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "1033",
            "-53",
            "-6"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "858",
            "-44",
            "-5"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "52671",
            "-2701",
            "-307"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "51813",
            "-2657",
            "-302"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "10804",
            "-554",
            "-63"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "2207",
            "-113",
            "-13"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "4555",
            "-233",
            "-27"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "6903",
            "-353",
            "-41"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "9059",
            "-463",
            "-54"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "2156",
            "-110",
            "-13"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "2139",
            "-109",
            "-13"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "2122",
            "-108",
            "-13"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "1789",
            "-91",
            "-11"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1456",
            "-74",
            "-9"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "22759",
            "-1155",
            "-142"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "21303",
            "-1081",
            "-133"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "7528",
            "-382",
            "-47"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1281",
            "-65",
            "-8"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "4599",
            "-233",
            "-29"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "7917",
            "-401",
            "-50"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "8075",
            "-409",
            "-51"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "158",
            "-8",
            "-1"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "1405",
            "-71",
            "-9"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "2652",
            "-134",
            "-17"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "3583",
            "-181",
            "-23"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "931",
            "-47",
            "-6"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "5710",
            "-288",
            "-37"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "10489",
            "-529",
            "-68"
          ],
          "patterns": 1675,
          "distinctMaskPatterns": 1675,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "2618",
            "-132",
            "-17"
          ],
          "patterns": 1681,
          "distinctMaskPatterns": 1681,
          "feasible": false,
          "proof": "union"
        }
      ],
      "excluded": true
    }
  ],
  "excluded": [
    50,
    1474,
    1949,
    2472,
    3110
  ],
  "strata": 297,
  "totalPatterns": 446587
}
```
