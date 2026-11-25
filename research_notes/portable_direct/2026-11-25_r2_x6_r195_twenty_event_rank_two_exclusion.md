# X6 R195 — Twenty-event rank-two exclusion replay

2026-11-25. Independent informed static auxiliary BRC weight research. AUTHOR EXACT FINITE NECESSARY-RELAXATION REPLAY, NOT_REVIEWED. Historical predecessor EM-DIRECT-AE5AD5; live identity binding unconfirmed. Current X6 read r2-20261125-1707-x6-read SUCCEEDED at 2026-11-25T09:07:42.388313Z, Source e9ec4c51cb05a52e0a97d9cfe47a699b6b31d0f5, NO_CANONICAL_PUBLICATION_DIRECTORY, execution_authorized=false, native_operational_view_evaluated=false. No CLAIM or shared task mutation.

## Frozen scope and method

R194@9a5ce5dba0b4777e6517919685b847218e7765d0 blob 4e7f633ab1586872ed9c28d09ebc85dfc73d4330; R182 side census@6945e591116377f9386c7419b6ce31a2b9e8a146 blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82; R182 one-child theorem@502d7abb2fe8470ed2cdabf242c2cc59a0c302ac. Retain R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f: Port 10, 1935 unoriented integer directions, six BRC denominators, w=(17t,B,22t,D), exact optimum and strict 3/2 near set. P000 V5, ACTIVE worldview, joint-relation preservation. Auxiliary coefficient chart only. No re-scoring. R182 proves each child's fixed-endpoint depth-five necessary capacity relaxation constant on its own exact event strata. Replay retains equality points, open intervals, endpoint incidence and root signs, clips each actual component before compressing to extreme endpoints per support. Coincident event rays coalesced, original labels retained in frozen rows. A uniformly failing child excludes the class; both passing somewhere would require intersection and further evidence, not a tree witness.

## Executed result

```json
[
  {
    "id": 44,
    "side": 1,
    "supports": 29,
    "events": 20,
    "distinct": 18,
    "strata": 37,
    "passing": 0
  },
  {
    "id": 323,
    "side": 1,
    "supports": 30,
    "events": 20,
    "distinct": 20,
    "strata": 41,
    "passing": 0
  },
  {
    "id": 1562,
    "side": 1,
    "supports": 29,
    "events": 20,
    "distinct": 20,
    "strata": 41,
    "passing": 0
  },
  {
    "id": 1920,
    "side": 1,
    "supports": 27,
    "events": 20,
    "distinct": 20,
    "strata": 41,
    "passing": 0
  },
  {
    "id": 2513,
    "side": 1,
    "supports": 28,
    "events": 20,
    "distinct": 20,
    "strata": 41,
    "passing": 0
  },
  {
    "id": 2542,
    "side": 1,
    "supports": 28,
    "events": 20,
    "distinct": 20,
    "strata": 41,
    "passing": 0
  },
  {
    "id": 3912,
    "side": -1,
    "supports": 30,
    "events": 20,
    "distinct": 18,
    "strata": 37,
    "passing": 0
  }
]
```

Total 279 strata; sum of distinct pattern counts 404795; newly excluded [44,323,1562,1920,2513,2542,3912]. Conditional on inherited R194: remaining 179 = 91 rank two + 88 rank three. Global 6<=D_linear<=7 unchanged. Any nonexcluded rows remain unresolved. Next min-21 census rows: [{"id":1506,"events":[[1,27],[-1,21]]},{"id":3484,"events":[[1,23],[-1,21]]}]. No Activity association or independent review claimed.

## Standalone reproduction

```javascript
function replay(data,rows){
const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],sg=x=>x>0n?1:x<0n?-1:0,abs=x=>x<0n?-x:x,gcd=(a,b)=>b?gcd(b,a%b):abs(a),norm=p=>{let d=p.reduce(gcd,0n);return d?p.map(x=>x/d):p},uniq=a=>[...new Map(a.map(p=>[p.join(),p])).values()],add=(a,b)=>norm(a.map((x,j)=>x+b[j]));
const P=uniq(data.flatMap(e=>e.endpoints.map(p=>p.map(BigInt))));
const comps=data.map(e=>({parts:e.normal.join()==="51,2,-1"?[[["1","9","69"],["3","17","187"]],[["2","5","112"],["1","0","51"]]]:e.normal.join()==="17,-1,0"?[[["0","0","1"],["1","17","391"]],[["1","17","69"],["1","17","22"]]]:[e.endpoints]})).map(e=>e.parts.map(pair=>pair.map(p=>p.map(BigInt))));
function clip(r,side){let ret=[];for(let e of comps){let parts=[];for(let [u,v] of e){let a=BigInt(side)*dot(r,u),b=BigInt(side)*dot(r,v);if(a<=0n&&b<=0n)continue;let d=(a<0n||b<0n)?norm(a<0n?u.map((x,j)=>b*x-a*v[j]):v.map((x,j)=>a*x-b*u[j])):null;parts.push([a<0n?d:u,b<0n?d:v])}if(parts.length)ret.push([parts[0][0],parts.at(-1)[1]])}return ret}
const pc=x=>{x=x-((x>>>1)&0x55555555);x=(x&0x33333333)+((x>>>2)&0x33333333);return (((x+(x>>>4))&0x0F0F0F0F)*0x01010101)>>>24};
let totalPatterns=0;
function feasible(pairs){const N=pairs.length;if(N>31)return false;if(N<=5)return true;const pp=uniq(pairs.flat()),idx=new Map(pp.map((p,i)=>[p.join(),i])),Q=new Map();
function rec(r,t=null,p=null,s=1,u=1){let a=0n,b=0n;for(let i=0;i<pp.length;i++){let x=sg(dot(r,pp[i]));if(!x&&t)x=s*sg(dot(t,pp[i]));if(!x&&p)x=u*sg(dot(p,pp[i]));if(x>0)a|=1n<<BigInt(i);if(x<0)b|=1n<<BigInt(i)}if(a>b)[a,b]=[b,a];let key=`${a},${b}`;if(Q.has(key))return;let au=0,av=0,bu=0,bv=0;pairs.forEach(([p,q],i)=>{let x=1n<<BigInt(idx.get(p.join())),y=1n<<BigInt(idx.get(q.join())),z=1<<i;if(a&x)au|=z;if(a&y)av|=z;if(b&x)bu|=z;if(b&y)bv|=z});Q.set(key,[au,av,bu,bv])}
for(let i=0;i<pp.length;i++)for(let j=i+1;j<pp.length;j++){let r=cross(pp[i],pp[j]);if(!r.some(Boolean))continue;rec(r);for(let k=0;k<pp.length;k++)if(!dot(r,pp[k])){let t=cross(r,pp[k]);for(let s of [-1,1]){rec(r,t,null,s);for(let u of [-1,1])rec(r,t,pp[k],s,u)}}}
if(!Q.size)throw Error("unexpected rank-one carrier");totalPatterns+=Q.size;const all=2**N-1,qs=[...Q.values()],cache=new Map();
function solve(u,v,d){let n=pc(u|v);if(n>2**d-1)return false;if(n<=d)return true;let key=`${u},${v},${d}`;if(cache.has(key))return cache.get(key);let ans=false,limit=2**(d-1)-1;for(let [au,av,bu,bv] of qs){let pa=(u&au)|(v&av),pb=(u&bu)|(v&bv),a=u&~bu&pa,b=v&~bv&pa,c=u&~au&pb,e=v&~av&pb;if(pc(a|b)>limit||pc(c|e)>limit)continue;if(solve(a,b,d-1)&&solve(c,e,d-1)){ans=true;break}}cache.set(key,ans);return ans}
return solve(all,all,5)}
function side(c,s){let a=BigInt(c.a),b=BigInt(c.b);function valid(r,strict=false){return P.every((p,i)=>{let x=sg(dot(r,p)),bit=1n<<BigInt(i);return (a&bit)?(strict?x===1:x>=0):(b&bit)?(strict?x===-1:x<=0):x===0})}
let [u,v]=c.vertices.map(p=>p.map(BigInt));if(!valid(u)||!valid(v))throw Error("bad vertex");let events=new Map();for(let z of s.events){let x=z.split(",").map(BigInt),A=dot(x,u),B=dot(x,v);if(A*B>=0n)throw Error("not varying");let alpha=abs(B),beta=abs(A),r=norm(u.map((x,j)=>alpha*x+beta*v[j]));events.set(r.join(),{r,alpha,beta})}
let list=[{r:u,alpha:1n,beta:0n},...[...events.values()].sort((a,b)=>sg(a.beta*b.alpha-b.beta*a.alpha)),{r:v,alpha:0n,beta:1n}],reps=[];for(let i=0;i+1<list.length;i++){reps.push({kind:"open",r:add(list[i].r,list[i+1].r)});if(i+1<list.length-1)reps.push({kind:"event",r:list[i+1].r})}
let results=[];for(let q of reps){if(!valid(q.r,true))throw Error("representative outside class");let pairs=clip(q.r,s.side);if(pairs.length!==s.supports)throw Error("support count mismatch");results.push({kind:q.kind,r:q.r.map(String),feasible:feasible(pairs)})}return {i:c.i,side:s.side,supports:s.supports,events:s.events.length,distinct:events.size,results,excluded:results.every(x=>!x.feasible)}}
let output=[];for(let c of rows){let s=[...c.sides].sort((a,b)=>a.events.length-b.events.length);let q=side(c,s[0]);output.push(q);if(!q.excluded)output.push(side(c,s[1]))}
return {output,totalPatterns,excluded:[...new Set(output.filter(x=>x.excluded).map(x=>x.i))],strata:output.reduce((n,x)=>n+x.results.length,0)}
}
const data=[{"normal":["187","12","-1"],"segments":9,"endpoints":[["0","1","12"],["1","17","391"]]},{"normal":["204","11","-1"],"segments":9,"endpoints":[["0","1","11"],["1","17","391"]]},{"normal":["5","-2","0"],"segments":51,"endpoints":[["2","5","73"],["2","5","5"]]},{"normal":["9","-1","0"],"segments":4,"endpoints":[["1","9","74"],["1","9","69"]]},{"normal":["85","7","-2"],"segments":10,"endpoints":[["1","9","74"],["3","17","187"]]},{"normal":["51","2","-1"],"segments":9,"endpoints":[["1","9","69"],["1","0","51"]]},{"normal":["0","1","-1"],"segments":2,"endpoints":[["2","5","5"],["1","0","0"]]},{"normal":["34","1","-1"],"segments":7,"endpoints":[["2","5","73"],["1","0","34"]]},{"normal":["187","20","-9"],"segments":5,"endpoints":[["6","15","158"],["1","1","23"]]},{"normal":["68","1","-3"],"segments":8,"endpoints":[["2","5","47"],["3","0","68"]]},{"normal":["176","22","-9"],"segments":4,"endpoints":[["6","15","154"],["19","28","440"]]},{"normal":["22","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","22"]]},{"normal":["61","0","-1"],"segments":78,"endpoints":[["0","1","0"],["1","17","61"]]},{"normal":["74","0","-1"],"segments":14,"endpoints":[["1","9","74"],["1","4","74"]]},{"normal":["126","0","-1"],"segments":103,"endpoints":[["0","1","0"],["1","30","126"]]},{"normal":["4","-1","0"],"segments":35,"endpoints":[["1","4","152"],["1","4","74"]]},{"normal":["17","-1","0"],"segments":44,"endpoints":[["0","0","1"],["1","17","22"]]},{"normal":["156","-1","-1"],"segments":46,"endpoints":[["1","4","152"],["1","30","126"]]},{"normal":["69","0","-1"],"segments":16,"endpoints":[["1","17","69"],["1","9","69"]]},{"normal":["9","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","9"]]},{"normal":["235","0","-3"],"segments":84,"endpoints":[["0","1","0"],["3","77","235"]]},{"normal":["87","0","-1"],"segments":107,"endpoints":[["0","1","0"],["1","17","87"]]},{"normal":["104","-1","-1"],"segments":60,"endpoints":[["1","4","100"],["3","77","235"]]},{"normal":["38","0","-3"],"segments":57,"endpoints":[["0","1","0"],["3","40","38"]]},{"normal":["5","0","-2"],"segments":72,"endpoints":[["0","1","0"],["2","5","5"]]},{"normal":["39","-1","-1"],"segments":50,"endpoints":[["3","1","116"],["1","17","22"]]},{"normal":["40","0","-3"],"segments":63,"endpoints":[["0","1","0"],["3","38","40"]]},{"normal":["26","-1","-1"],"segments":39,"endpoints":[["2","5","47"],["3","53","25"]]},{"normal":["25","0","-3"],"segments":52,"endpoints":[["0","1","0"],["3","53","25"]]},{"normal":["83","0","-2"],"segments":69,"endpoints":[["0","1","0"],["2","34","83"]]},{"normal":["102","-7","-1"],"segments":14,"endpoints":[["1","4","74"],["3","17","187"]]},{"normal":["204","-11","1"],"segments":51,"endpoints":[["0","1","11"],["1","30","126"]]},{"normal":["395","0","-2"],"segments":119,"endpoints":[["0","1","0"],["2","73","395"]]},{"normal":["289","18","-1"],"segments":10,"endpoints":[["0","1","18"],["1","17","595"]]},{"normal":["66","2","-1"],"segments":11,"endpoints":[["1","4","74"],["1","0","66"]]},{"normal":["132","5","-1"],"segments":16,"endpoints":[["1","17","217"],["1","0","132"]]},{"normal":["44","1","-1"],"segments":9,"endpoints":[["1","17","61"],["1","11","55"]]},{"normal":["88","3","-1"],"segments":7,"endpoints":[["1","4","100"],["1","0","88"]]},{"normal":["88","7","-3"],"segments":5,"endpoints":[["1","17","69"],["1","11","55"]]},{"normal":["132","-7","-1"],"segments":14,"endpoints":[["1","9","69"],["1","11","55"]]},{"normal":["153","8","-1"],"segments":7,"endpoints":[["1","9","225"],["1","0","153"]]},{"normal":["153","5","-4"],"segments":1,"endpoints":[["3","1","116"],["4","0","153"]]},{"normal":["117","-2","-2"],"segments":42,"endpoints":[["2","5","112"],["2","34","83"]]},{"normal":["198","8","-1"],"segments":5,"endpoints":[["1","4","230"],["1","0","198"]]},{"normal":["198","5","-4"],"segments":11,"endpoints":[["2","8","109"],["2","0","99"]]},{"normal":["306","17","-1"],"segments":8,"endpoints":[["1","17","595"],["1","0","306"]]},{"normal":["234","-1","-1"],"segments":43,"endpoints":[["1","4","230"],["2","73","395"]]}];
const rows=[{"i":44,"a":"1132515426404","b":"2250667298258842","r":["-89","36","-3"],"local":53,"vertices":[["-55","24","-2"],["-34","12","-1"]],"sides":[{"side":1,"supports":29,"events":["10,53,337","111,919,7934","13,112,962","15,127,1082","167,1448,12358","21,179,1519","22,188,1593","22,65,55","23,196,1702","24,167,1237","3,13,65","3,16,101","33,287,2407","38,100,95","4,17,87","4,27,207","411,3589,30029","56,459,3774","67,581,4881","9,76,611"]},{"side":-1,"supports":30,"events":["10,53,337","10,81,672","101,534,3405","103,1460,14608","1058,2716,2645","1078,3035,2695","136,407,340","15,64,326","1528,4515,3820","173,3510,36972","189,869,4045","19,193,1783","200,607,500","2068,5865,5170","2162,5944,5405","22,63,55","226,607,565","286,752,715","304,903,760","3356,9105,8390","3364,9105,8410","38,115,95","412,1173,1030","49,1000,10466","5,44,370","5,71,709","53,425,3553","54,785,7639","6,61,563","62,185,155","698,1955,1745","74,215,185","95,809,7030","99,448,2126"]}]},{"i":323,"a":"1441753071687","b":"2250358060613528","r":["-3179","419","-8"],"local":85,"vertices":[["-2261","317","-8"],["-4097","521","-8"]],"sides":[{"side":1,"supports":30,"events":["1,11,187","110,938,5497","12,113,1135","13,103,235","165,1277,3013","19,234,4212","19,425,13141","2,21,291","3,23,55","3,38,664","3,53,1821","3,77,2253","34,266,85","4,29,10","46,338,115","55,443,1702","70,579,2151","89,2329,67643","899,17935,582641","937,18173,597907"]},{"side":-1,"supports":28,"events":["1,12,222","1,17,397","1,17,399","1,17,425","1,17,427","1,17,433","1,17,457","1,17,473","1,17,520","10,121,2219","100,2239,69202","11,187,4835","11,187,6092","12,204,5945","124,3079,91258","128,3095,92702","13,148,2894","13,221,6485","13,314,9409","13,343,9931","14,313,9680","142,2867,92644","149,3728,110165","154,1214,385","158,1204,395","16,272,8347","161,3709,113291","167,4012,120479","18,137,331","2,15,5","2,34,1071","2,34,1097","2,34,863","211,4837,148045","23,510,15827","248,2747,46471","256,2779,47687","263,3132,58410","27,212,490","27,459,10931","28,355,6197","29,324,5448","3,32,436","3,34,668","3,38,664","3,51,1301","3,51,1411","3,51,1444","3,51,1535","3,51,1717","33,313,3119","39,663,18311","4,68,1921","43,799,26809","47,1049,32465","5,85,2333","5,85,2489","6,102,3031","61,660,11352","64,527,1969","7,80,1558","8,136,3881","9,153,3553","9,153,4384","9,153,4436","9,98,1678"]}]},{"i":1562,"a":"300183435869720","b":"1951616243597799","r":["142","7","-3"],"local":76,"vertices":[["195","9","-4"],["89","5","-2"]],"sides":[{"side":1,"supports":29,"events":["1,33,126","14,869,2765","16,531,2016","2,7,110","23,211,1587","278,17833,54905","28,109,1529","29,66,1518","38,56,1951","4,15,219","4,4,203","45,154,2420","46,2838,9085","47,182,2554","51,62,2602","54,203,2956","8,20,421","89,330,4818","9,298,1134","94,6083,18565"]},{"side":-1,"supports":26,"events":["1,2,52","11,26,577","121,1114,8174","124,1161,8556","127,274,6629","133,194,6826","15,22,770","15,38,790","154,10064,30415","156,1429,10764","157,290,8134","17,42,894","176,236,9007","176,535,9761","18,56,961","18,64,989","1915,5294,101410","193,642,10356","2,7,110","211,550,11132","220,711,12159","23,66,1221","232,2133,16008","25,22,1265","251,614,13192","26,56,1357","281,770,14872","29,66,1518","337,802,17684","356,1255,19571","38,117,2106","4,15,219","4,263,790","401,1266,21432","41,138,2202","43,110,2266","43,146,2311","43,94,2246","463,1114,24311","47,110,2464","49,66,2508","5,6,255","569,586,28898","58,567,4002","664,2591,36253","67,154,3509","67,190,3554","67,198,3564","67,86,3424","673,2354,36256","7,22,374","77,2601,9702","773,2962,41966","78,727,5382","79,756,5451","8,20,421","8,27,441","845,1982,44305","89,230,4693","95,198,4950"]}]},{"i":1920,"a":"581658328170008","b":"1670141484990951","r":["850","11","-17"],"local":53,"vertices":[["867","10","-17"],["1683","23","-34"]],"sides":[{"side":1,"supports":27,"events":["1,126,126","10,1197,1260","113,6562,9831","12,4,599","18,835,1410","190,11147,16530","2,121,174","26,135,1386","3,133,235","3335,518,165730","346,1755,18486","37,2085,3219","38,56,1951","4,4,203","5,592,630","51,22,2552","51,62,2602","561,322,28172","6,271,470","697,38694,60639"]},{"side":-1,"supports":29,"events":["1,2,52","1,59,87","10,1139,1260","104,60,5223","127,274,6629","133,194,6826","14,74,745","15,22,770","157,290,8134","16,12,807","166,833,8878","176,236,9007","20,107,1063","20,4709,3950","202,990,10827","25,22,1265","26,56,1357","267,11611,20915","28,6677,5530","37,4620,4662","43,94,2246","49,66,2508","5,6,255","50,252,2673","569,586,28898","6,31,320","67,86,3424","76,935,4411","78,385,4178","79,22,3938","8,39,429","83,1012,4796","95,198,4950"]}]},{"i":2513,"a":"1115201448464","b":"2250684478019055","r":["5063","1217","-296"],"local":57,"vertices":[["19","4","-1"],["5044","1213","-295"]],"sides":[{"side":1,"supports":28,"events":["10,443,1975","1770,3381,44290","19,28,457","2,88,395","2005,2383,46955","2391,2433,55007","2427,3357,56131","2615,3749,62665","29,47,707","380,407,8800","40,49,940","50,77,1210","537,603,12373","549,807,12713","607,778,14341","6098,6611,141394","681,963,15757","727,862,17021","8321,9887,194863","8900,10547,208360"]},{"side":-1,"supports":31,"events":["10,25,287","107,134,2521","109,136,2516","14,620,2765","142,169,3326","142,187,3366","158,185,3694","176,257,4228","185,293,4495","1981,2125,45611","2,16,101","2,5,55","244,343,5832","2669,4019,64387","2725,2941,63155","284,527,7072","293,374,6919","32,41,739","331,340,7616","38,303,1920","4561,7531,111503","527,752,12196","53,62,1222","53,68,1224","557,935,13651","57,236,1987","59,245,2056","64,73,1475","7,72,420","70,97,1619","77,95,1777","79,106,1877","821,1496,20383","83,351,2886","87,120,2012","908,935,20944","91,2907,13413"]}]},{"i":2542,"a":"1115335666192","b":"2250667298149871","r":["11172","3487","-701"],"local":55,"vertices":[["1284","349","-71"],["21060","6625","-1331"]],"sides":[{"side":1,"supports":28,"events":["19,28,457","2005,2383,46955","2391,2433,55007","2427,3357,56131","25,261,1725","2615,3749,62665","29,47,707","380,407,8800","4,15,141","40,49,940","5,48,324","50,77,1210","537,603,12373","549,807,12713","607,778,14341","6098,6611,141394","681,963,15757","727,862,17021","8321,9887,194863","8900,10547,208360"]},{"side":-1,"supports":30,"events":["10,25,287","107,134,2521","109,136,2516","142,169,3326","142,187,3366","158,185,3694","176,257,4228","185,293,4495","1981,2125,45611","2,5,60","24,167,1237","244,343,5832","26,185,1336","2669,4019,64387","2725,2941,63155","293,374,6919","32,41,739","331,340,7616","369,1307,13084","43,412,2792","4561,7531,111503","527,752,12196","53,62,1222","53,68,1224","557,935,13651","64,73,1475","66,1543,8753","67,981,5987","7,102,626","70,97,1619","77,95,1777","79,106,1877","83,306,2931","87,120,2012","908,935,20944"]}]},{"i":3912,"a":"1049624782700536","b":"1201075519356935","r":["286","-21","-1"],"local":64,"vertices":[["1782","-127","-7"],["3366","-251","-11"]],"sides":[{"side":1,"supports":28,"events":["1,13,13","1,4,185","1,6,150","1,9,95","10,129,131","103,282,22650","115,1431,3054","12,163,30","129,1662,1720","13,120,1232","173,1560,16432","2,13,299","2,5,436","20,119,3001","21,188,1996","214,1441,31943","215,1952,20408","23,103,4343","23,146,3442","23,155,3433","233,1031,43897","25,109,4697","28,151,4451","28,373,70","295,1882,44138","3,17,481","3,20,448","305,1844,49480","32,427,80","334,4469,835","35,173,6739","356,4921,890","4,25,599","4,49,107","4,55,10","43,205,8219","554,7429,1385","56,257,10624","6,79,80","61,400,9116","618,5653,58619","62,275,11686","64,373,10313","686,3041,129286","73,448,11876","73,942,956","838,11438,2095","86,1173,215","9,116,120","9,52,1448"]},{"side":-1,"supports":30,"events":["1,13,13","1,4,185","1,6,150","1,9,95","13,69,2061","19,245,249","2,13,299","21,125,3397","22,296,55","326,4489,815","36,469,480","36,479,90","4,11,880","4,55,10","44,607,110","54,697,720","6,80,15","8,19,1736","8,27,1800","98,1327,245"]}]}];
console.log(JSON.stringify(replay(data,rows),null,2));
```

## Actual output

```json
{
  "output": [
    {
      "i": 44,
      "side": 1,
      "supports": 29,
      "events": 20,
      "distinct": 18,
      "results": [
        {
          "kind": "open",
          "r": [
            "-3149",
            "1356",
            "-113"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-3094",
            "1332",
            "-111"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1872",
            "804",
            "-67"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-650",
            "276",
            "-23"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1755",
            "732",
            "-61"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1105",
            "456",
            "-38"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-611",
            "252",
            "-21"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-117",
            "48",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-499",
            "204",
            "-17"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-382",
            "156",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-206",
            "84",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-442",
            "180",
            "-15"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-741",
            "300",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-299",
            "120",
            "-10"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-928",
            "372",
            "-31"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-629",
            "252",
            "-21"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-5647",
            "2256",
            "-188"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-5018",
            "2004",
            "-167"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-5681",
            "2268",
            "-189"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-663",
            "264",
            "-22"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-754",
            "300",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-91",
            "36",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-958",
            "372",
            "-31"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-867",
            "336",
            "-28"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-2958",
            "1140",
            "-95"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-2091",
            "804",
            "-67"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-782",
            "300",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1037",
            "396",
            "-33"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1173",
            "444",
            "-37"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-13039",
            "4932",
            "-411"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-4602",
            "1740",
            "-145"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-767",
            "288",
            "-24"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-746",
            "276",
            "-23"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-725",
            "264",
            "-22"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1026",
            "372",
            "-31"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-301",
            "108",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-67",
            "24",
            "-2"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 323,
      "side": 1,
      "supports": 30,
      "events": 20,
      "distinct": 20,
      "results": [
        {
          "kind": "open",
          "r": [
            "-73117",
            "10229",
            "-256"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-436441",
            "61057",
            "-1528"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-439605",
            "61499",
            "-1539"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-3164",
            "442",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-17743",
            "2473",
            "-61"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-14579",
            "2031",
            "-50"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-16635",
            "2317",
            "-57"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-2056",
            "286",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-3263",
            "453",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1207",
            "167",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1574",
            "216",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-23977",
            "3289",
            "-76"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-45679",
            "6243",
            "-142"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-67381",
            "9197",
            "-208"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-87973",
            "12003",
            "-271"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-20592",
            "2806",
            "-63"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-12479",
            "1699",
            "-38"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-4366",
            "592",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-30395",
            "4109",
            "-89"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-86819",
            "11735",
            "-254"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-87884",
            "11878",
            "-257"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1065",
            "143",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1459",
            "195",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1853",
            "247",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-21792",
            "2890",
            "-57"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-19939",
            "2643",
            "-52"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-12723",
            "1685",
            "-33"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-5507",
            "727",
            "-14"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1961043",
            "258421",
            "-4929"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-3916579",
            "516115",
            "-9844"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-12995",
            "1707",
            "-32"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-4036361",
            "528569",
            "-9740"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-2018615",
            "264341",
            "-4871"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-869",
            "113",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-24356",
            "3142",
            "-53"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-23487",
            "3029",
            "-51"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-466",
            "60",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-18919",
            "2431",
            "-40"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-9939",
            "1277",
            "-21"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-959",
            "123",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-2528",
            "322",
            "-5"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 1562,
      "side": 1,
      "supports": 29,
      "events": 20,
      "distinct": 20,
      "results": [
        {
          "kind": "open",
          "r": [
            "1649",
            "77",
            "-34"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3103",
            "145",
            "-64"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "10871",
            "512",
            "-225"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7768",
            "367",
            "-161"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "13427",
            "638",
            "-279"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5659",
            "271",
            "-118"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3069",
            "147",
            "-64"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "479",
            "23",
            "-10"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "16911",
            "822",
            "-355"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "16432",
            "799",
            "-345"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "26395",
            "1303",
            "-558"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "36358",
            "1807",
            "-771"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "28211",
            "1406",
            "-599"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "20064",
            "1005",
            "-427"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "21325",
            "1069",
            "-454"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1261",
            "64",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6678",
            "339",
            "-143"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5417",
            "275",
            "-116"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "17342",
            "899",
            "-375"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11925",
            "624",
            "-259"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "18573",
            "975",
            "-404"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6648",
            "351",
            "-145"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1511",
            "80",
            "-33"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2418",
            "129",
            "-53"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4925",
            "263",
            "-108"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2507",
            "134",
            "-55"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3236",
            "173",
            "-71"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "729",
            "39",
            "-16"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "409",
            "22",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2134",
            "115",
            "-47"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5122",
            "277",
            "-113"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "28598",
            "1547",
            "-631"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "22554",
            "1227",
            "-499"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "16510",
            "907",
            "-367"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "108971",
            "5990",
            "-2423"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "92461",
            "5083",
            "-2056"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "96553",
            "5308",
            "-2147"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4092",
            "225",
            "-91"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7919",
            "440",
            "-177"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "27584",
            "1535",
            "-617"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "27673",
            "1540",
            "-619"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 1920,
      "side": 1,
      "supports": 27,
      "events": 20,
      "distinct": 20,
      "results": [
        {
          "kind": "open",
          "r": [
            "1988",
            "23",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "26965",
            "312",
            "-529"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1121",
            "13",
            "-22"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5544",
            "65",
            "-109"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9967",
            "117",
            "-196"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4423",
            "52",
            "-87"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "254",
            "3",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "657",
            "8",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "10136",
            "125",
            "-201"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "29751",
            "367",
            "-590"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "60440",
            "747",
            "-1199"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "30689",
            "380",
            "-609"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "10163",
            "127",
            "-202"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "40452",
            "509",
            "-805"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3417",
            "43",
            "-68"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3969",
            "50",
            "-79"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5476",
            "69",
            "-109"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "17935",
            "226",
            "-357"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9997",
            "126",
            "-199"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2059",
            "26",
            "-41"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "104633",
            "1323",
            "-2084"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "207207",
            "2620",
            "-4127"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "70138",
            "887",
            "-1397"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3207",
            "41",
            "-64"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5161",
            "66",
            "-103"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1954",
            "25",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "17281",
            "225",
            "-346"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "15327",
            "200",
            "-307"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "158203",
            "2083",
            "-3174"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "459282",
            "6049",
            "-9215"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "462069",
            "6086",
            "-9271"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2787",
            "37",
            "-56"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6021",
            "80",
            "-121"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3234",
            "43",
            "-65"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "13173",
            "176",
            "-265"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "9939",
            "133",
            "-200"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2795751",
            "37838",
            "-56377"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2785812",
            "37705",
            "-56177"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "962693",
            "13033",
            "-19414"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "102267",
            "1394",
            "-2065"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "103950",
            "1417",
            "-2099"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 2513,
      "side": 1,
      "supports": 28,
      "events": 20,
      "distinct": 20,
      "results": [
        {
          "kind": "open",
          "r": [
            "32903",
            "6959",
            "-1738"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "32884",
            "6955",
            "-1737"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "29415",
            "6243",
            "-1558"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "114191",
            "24260",
            "-6053"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "485683",
            "103348",
            "-25777"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1828541",
            "389132",
            "-97055"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "278317",
            "59692",
            "-14863"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2624531",
            "565940",
            "-140753"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "473149",
            "102028",
            "-25375"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "214363",
            "46228",
            "-11497"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "42371",
            "9140",
            "-2273"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1226251",
            "264532",
            "-65785"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "126809",
            "27356",
            "-6803"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "295457",
            "63740",
            "-15851"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "153587",
            "33140",
            "-8241"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11717",
            "2540",
            "-631"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "90657",
            "19713",
            "-4894"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "78940",
            "17173",
            "-4263"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "15003",
            "3273",
            "-812"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "176111",
            "38468",
            "-9541"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "176493",
            "38553",
            "-9562"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "382",
            "85",
            "-21"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "369953",
            "82505",
            "-20374"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "369571",
            "82420",
            "-20353"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "46863",
            "10452",
            "-2581"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5333",
            "1196",
            "-295"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4801",
            "1084",
            "-267"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "13871",
            "3140",
            "-773"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4459",
            "1012",
            "-249"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3965",
            "908",
            "-223"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "335049",
            "78417",
            "-19174"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "331084",
            "77509",
            "-18951"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "22135",
            "5182",
            "-1267"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "941",
            "221",
            "-54"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "30995",
            "7322",
            "-1787"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "92044",
            "21745",
            "-5307"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7983",
            "1905",
            "-464"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "458783",
            "109700",
            "-26709"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "531739",
            "127225",
            "-30972"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "72956",
            "17525",
            "-4263"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "39000",
            "9369",
            "-2279"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 2542,
      "side": 1,
      "supports": 28,
      "events": 20,
      "distinct": 20,
      "results": [
        {
          "kind": "open",
          "r": [
            "763940",
            "208695",
            "-42437"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3054476",
            "834431",
            "-169677"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3536111",
            "966931",
            "-196603"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "481635",
            "132500",
            "-26926"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4096026",
            "1129211",
            "-229429"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7710417",
            "2125922",
            "-431932"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9377316",
            "2612351",
            "-530269"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11044215",
            "3098780",
            "-628606"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3982086",
            "1117301",
            "-226651"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "902043",
            "253123",
            "-51347"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3740559",
            "1050064",
            "-213002"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "10319634",
            "2897069",
            "-587659"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2134344",
            "599189",
            "-121543"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2486430",
            "698065",
            "-141599"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "418210",
            "117415",
            "-23817"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "22830",
            "6425",
            "-1303"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "343937",
            "96897",
            "-19649"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "665044",
            "187369",
            "-37995"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "714309",
            "201289",
            "-40817"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "49265",
            "13920",
            "-2822"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "53957",
            "15247",
            "-3091"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4692",
            "1327",
            "-269"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "744275",
            "212410",
            "-43024"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "739583",
            "211083",
            "-42755"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3833273",
            "1118678",
            "-226152"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3093690",
            "907595",
            "-183397"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3115991",
            "914186",
            "-184728"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "22301",
            "6591",
            "-1331"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "24485",
            "7240",
            "-1462"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2184",
            "649",
            "-131"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1541",
            "461",
            "-93"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "57915",
            "17330",
            "-3496"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "90961",
            "27371",
            "-5519"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "33046",
            "10041",
            "-2023"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1402297",
            "428222",
            "-86240"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2771548",
            "846403",
            "-170457"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "885356",
            "270971",
            "-54561"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "769876",
            "237481",
            "-47787"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "45972",
            "14297",
            "-2875"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "609284",
            "191429",
            "-38463"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "315172",
            "99027",
            "-19897"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 3912,
      "side": -1,
      "supports": 30,
      "events": 20,
      "distinct": 18,
      "results": [
        {
          "kind": "open",
          "r": [
            "2805",
            "-200",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "9438",
            "-673",
            "-37"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1023",
            "-73",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1815",
            "-130",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1045",
            "-75",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "10725",
            "-770",
            "-41"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8371",
            "-601",
            "-32"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6017",
            "-432",
            "-23"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "17347",
            "-1247",
            "-66"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11330",
            "-815",
            "-43"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5797",
            "-417",
            "-22"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "264",
            "-19",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3179",
            "-229",
            "-12"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2915",
            "-210",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1595",
            "-115",
            "-6"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "275",
            "-20",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "10395",
            "-760",
            "-37"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "20515",
            "-1500",
            "-73"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "43945",
            "-3215",
            "-156"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "23430",
            "-1715",
            "-83"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "847",
            "-62",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "286",
            "-21",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7766",
            "-571",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "15246",
            "-1121",
            "-53"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "20471",
            "-1506",
            "-71"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5225",
            "-385",
            "-18"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "35640",
            "-2635",
            "-121"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "30415",
            "-2250",
            "-103"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "33099",
            "-2449",
            "-112"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2684",
            "-199",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "20999",
            "-1559",
            "-70"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "18315",
            "-1360",
            "-61"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "18920",
            "-1405",
            "-63"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "605",
            "-45",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5192",
            "-387",
            "-17"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "25355",
            "-1890",
            "-83"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "28721",
            "-2141",
            "-94"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    }
  ],
  "totalPatterns": 404795,
  "excluded": [
    44,
    323,
    1562,
    1920,
    2513,
    2542,
    3912
  ],
  "strata": 279
}
```
