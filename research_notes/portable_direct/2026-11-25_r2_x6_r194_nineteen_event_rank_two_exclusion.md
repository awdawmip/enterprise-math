# X6 R194 — Nineteen-event rank-two exclusion replay

2026-11-25. Independent informed static auxiliary BRC weight research. AUTHOR EXACT FINITE NECESSARY-RELAXATION REPLAY, NOT_REVIEWED. Historical predecessor EM-DIRECT-AE5AD5; live identity binding unconfirmed. X6 read r2-20261125-1607-x6-read SUCCEEDED at 2026-11-25T08:07:20.312072Z, Source 9b2abeb9b8c83e67b7426d93082ac6c254c07f12, NO_CANONICAL_PUBLICATION_DIRECTORY; native_operational_view_evaluated=false; execution_authorized=false. No CLAIM or shared task state mutation.

## Frozen source and scope

R193@ca97bb057c0559f8e7b88c7b32d962d9a2f62d14 blob daf29b2801375c93d4741723113a588f461f9ad2; R182 census@6945e591116377f9386c7419b6ce31a2b9e8a146 blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82; R182 one-child theorem@502d7abb2fe8470ed2cdabf242c2cc59a0c302ac. Preserve R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd, R122@1e4ab68c4f9c91bc60c07017acc57be20829832f, Port 10, 1935 unoriented integer directions, six BRC pair denominators, w=(17t,B,22t,D), exact optimum and strict 3/2 near set. P000 V5, ACTIVE worldview and joint-relation observer preservation. Auxiliary coefficient chart, not native spatial geometry or time dynamics. No re-scoring.

R182 establishes that each child's fixed-endpoint depth-five necessary capacity relaxation is constant on its own exact event strata. Coalesce coincident event rays, retain every equality point and adjacent open interval; check root signs and support counts. Clip disconnected components individually before retaining extreme endpoints per support. Entirely failing one child suffices for exclusion. Both passing somewhere requires exact intersection, not automatically a tree witness. This replay inherits the earlier proof and arithmetic; no independent mathematical review.

## Executed summary

```json
[
  {
    "id": 1283,
    "side": 1,
    "supports": 31,
    "events": 19,
    "distinct": 19,
    "strata": 39,
    "passing": 0
  },
  {
    "id": 1475,
    "side": 1,
    "supports": 29,
    "events": 19,
    "distinct": 18,
    "strata": 37,
    "passing": 0
  },
  {
    "id": 1485,
    "side": 1,
    "supports": 29,
    "events": 19,
    "distinct": 19,
    "strata": 39,
    "passing": 0
  },
  {
    "id": 1666,
    "side": 1,
    "supports": 26,
    "events": 19,
    "distinct": 19,
    "strata": 39,
    "passing": 39
  },
  {
    "id": 1666,
    "side": -1,
    "supports": 27,
    "events": 19,
    "distinct": 19,
    "strata": 39,
    "passing": 0
  },
  {
    "id": 1921,
    "side": 1,
    "supports": 28,
    "events": 19,
    "distinct": 19,
    "strata": 39,
    "passing": 0
  },
  {
    "id": 3035,
    "side": -1,
    "supports": 27,
    "events": 19,
    "distinct": 19,
    "strata": 39,
    "passing": 0
  },
  {
    "id": 3700,
    "side": -1,
    "supports": 31,
    "events": 19,
    "distinct": 19,
    "strata": 39,
    "passing": 0
  }
]
```

Total 310 strata; sum of distinct pattern counts 514808; newly excluded [1283,1475,1485,1666,1921,3035,3700]. Conditional on inherited R193 bank: remaining 186 = 98 rank two + 88 rank three. Global 6<=D_linear<=7 unchanged. Any nonexcluded rows remain open. Next min-20 rows: [{"id":44,"events":[[1,20],[-1,34]]},{"id":323,"events":[[1,20],[-1,66]]},{"id":1562,"events":[[1,20],[-1,60]]},{"id":1920,"events":[[1,20],[-1,33]]},{"id":2513,"events":[[1,20],[-1,37]]},{"id":2542,"events":[[1,20],[-1,35]]},{"id":3912,"events":[[1,50],[-1,20]]}]. No Activity association or independent review claimed.

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
const rows=[{"i":1283,"a":"1132515469904","b":"2250667298149807","r":["2044","1033","-154"],"local":60,"vertices":[["1888","966","-143"],["156","67","-11"]],"sides":[{"side":1,"supports":31,"events":["1,12,92","1,30,204","13,45,462","13,639,4377","173,585,6162","173,8343,56481","2,57,411","23,285,2107","23,441,3147","23,675,4707","295,3669,27011","295,5697,40323","295,8739,60291","3,27,211","4,49,367","4,75,549","5,43,341","9,175,1229","9,179,1225"]},{"side":-1,"supports":28,"events":["1,9,73","10,81,672","10,90,729","101,901,6953","11,510,3366","127,1103,8683","15,135,1087","16,139,1094","17,153,1188","176,1029,9267","181,2196,16628","181,3600,24636","2,17,136","2,5,60","21,263,1921","216,1319,11317","260,1581,13629","28,165,1473","301,2669,20689","37,1765,11867","39,134,1387","4,201,1395","4,35,274","4,75,549","41,2023,13889","49,610,4486","49,976,6668","53,425,3553","557,935,13651","56,459,3774","57,683,5245","59,1115,8089","59,1739,12067","59,699,5437","7,340,2312","87,1069,7979","88,1065,8087","88,1741,11987","9,113,823","9,31,320","9,76,611","94,558,4941"]}]},{"i":1475,"a":"1115335687704","b":"2250684477997479","r":["381","42","-11"],"local":35,"vertices":[["306","35","-9"],["75","7","-2"]],"sides":[{"side":1,"supports":29,"events":["1,1,38","1,26,130","10,443,1975","19,11,730","19,479,2485","2,51,261","2,88,395","24,785,3739","2426,106437,479135","254,10727,50165","266,11975,52535","3,77,391","4,3,153","56,2431,11060","589,19061,89515","593,19129,89447","736,31739,145360","746,539,28555","8,357,1580"]},{"side":-1,"supports":25,"events":["1,1,38","11,356,1672","11,357,1683","14,620,2765","15,493,2363","151,149,5740","152,101,5827","18,7,695","19,11,730","202,990,10827","3,2,115","4,3,153","67,981,5987","7,102,626","78,385,4178","8,39,429","8,7,305","9,227,1177","9,8,343"]}]},{"i":1485,"a":"1132515535376","b":"2250667298149807","r":["15","6","-1"],"local":55,"vertices":[["69","23","-4"],["156","67","-11"]],"sides":[{"side":1,"supports":29,"events":["13,45,462","173,585,6162","19,28,457","2005,2383,46955","2391,2433,55007","2427,3357,56131","2615,3749,62665","29,47,707","380,407,8800","40,49,940","50,77,1210","537,603,12373","549,807,12713","607,778,14341","6098,6611,141394","681,963,15757","727,862,17021","8321,9887,194863","8900,10547,208360"]},{"side":-1,"supports":28,"events":["107,134,2521","109,136,2516","142,169,3326","142,187,3366","143,6120,38148","158,185,3694","176,257,4228","181,5706,36648","185,293,4495","1981,2125,45611","2,5,60","233,763,8324","244,343,5832","2669,4019,64387","2725,2941,63155","293,374,6919","3,61,407","32,41,739","331,340,7616","39,134,1387","4,13,143","4561,7531,111503","49,1000,6644","527,752,12196","53,62,1222","53,68,1224","557,935,13651","64,73,1475","68,2939,18457","70,97,1619","77,95,1777","79,106,1877","87,120,2012","88,2755,17837","9,31,320","908,935,20944"]}]},{"i":1666,"a":"898317677363096","b":"1353482136191079","r":["253","0","-4"],"local":38,"vertices":[["187","0","-3"],["66","0","-1"]],"sides":[{"side":1,"supports":26,"events":["11,68,697","124,765,7854","128,765,8058","137,2047,8795","16,272,1027","17,101,1069","17,115,1097","18,116,1171","2,11,127","203,1275,13090","211,1275,13430","22,374,1411","23,149,1499","32,175,2039","359,1904,23290","37,255,2397","7,104,448","8,136,527","97,544,6086"]},{"side":-1,"supports":27,"events":["105,1584,6776","11,74,709","13,194,834","134,884,8789","137,958,8903","168,1054,10829","19,102,1224","199,1056,12906","27,170,1717","29,439,1875","35,192,2226","4,26,261","43,412,2792","5,48,324","5,73,317","56,289,3689","61,408,3927","61,594,3894","71,391,4505"]}]},{"i":1921,"a":"581658328170264","b":"1670141484990695","r":["972","11","-19"],"local":56,"vertices":[["867","10","-17"],["105","1","-2"]],"sides":[{"side":1,"supports":28,"events":["111,5423,8695","123,5926,9635","138,85,7208","19,2520,2394","20,89,1081","216,10081,16920","22,1479,1914","29,66,1518","3,1,155","3,196,261","339,17034,26555","38,17,1972","45,154,2420","47,182,2554","570,28917,44650","61,8180,7686","8,20,421","863,71,44155","89,330,4818"]},{"side":-1,"supports":29,"events":["1,63,87","11,26,577","15,38,790","151,1606,8690","17,42,894","18,56,961","1915,5294,101410","193,642,10356","2,9,108","20,93,1077","211,550,11132","23,66,1221","25,17,1309","251,614,13192","281,770,14872","29,66,1518","337,802,17684","36,1795,2820","37,34,1955","38,165,2058","387,18773,30315","4,17,217","401,1266,21432","41,138,2202","43,110,2266","43,146,2311","463,1114,24311","47,110,2464","604,2741,32593","67,154,3509","67,190,3554","67,198,3564","673,2354,36256","7,22,374","74,20251,14615","773,2962,41966","8,20,421","845,1982,44305","89,230,4693"]}]},{"i":3035,"a":"898317677494168","b":"1353344697237607","r":["396","1","-6"],"local":58,"vertices":[["66","0","-1"],["1122","3","-17"]],"sides":[{"side":1,"supports":30,"events":["1,1005,126","1,191,87","1,193,87","1,255,87","1,459,126","1,459,87","11,187,731","12,893,940","125,2059,8471","15,1802,1305","15,2491,1175","17,289,1157","17,4839,1479","17,8739,2142","183,15245,14335","2,1666,395","2,4012,395","20,2979,1740","25,4611,2175","27,3995,2115","3,1013,235","3,221,235","3,235,235","3,493,261","3,501,235","3,515,235","3,599,235","3,629,235","3,701,235","34,31778,6715","35,179,2317","38,191,2539","45,4522,3525","5,1111,435","53,425,3553","57,4700,4465","6,451,470","60,7429,4700","61,1031,4195"]},{"side":-1,"supports":27,"events":["1,147,87","1,225,87","1,264,87","1,5256,126","1,8103,87","10,81,672","121,1114,8174","169,1566,11346","27,2240,2115","3,233,235","3,26207,235","3,467,235","3,493,235","3,805,235","3,896,235","47,745,3117","56,459,3774","63,317,4207","651,49859,50995"]}]},{"i":3700,"a":"901191279181816","b":"1341812441481223","r":["5355","-289","-35"],"local":43,"vertices":[["2601","-144","-17"],["8109","-434","-53"]],"sides":[{"side":1,"supports":29,"events":["10,178,25","10,183,25","127,1299,8763","14,251,35","152,2727,380","159,1052,15484","19,301,440","2,31,47","21,356,280","21,358,266","22,395,55","23,402,207","231,3842,2926","237,2772,13420","246,4403,615","26,259,1794","3,20,292","3,51,38","3,51,40","30,527,253","30,536,75","4,51,183","46,821,115","46,836,115","6,76,275","67,792,3740","7,123,63","77,1343,693"]},{"side":-1,"supports":31,"events":["10,179,25","1138,20723,2845","15,263,127","1786,32171,4465","2,31,47","203,3555,1827","27,446,360","3,51,38","3,51,40","32,583,80","38,685,95","398,7078,995","4,51,183","406,7214,1015","5,58,282","568,10319,1420","8,123,189","82,1472,205","862,15707,2155"]}]}];
console.log(JSON.stringify(replay(data,rows),null,2));
```

## Actual output

```json
{
  "output": [
    {
      "i": 1283,
      "side": 1,
      "supports": 31,
      "events": 19,
      "distinct": 19,
      "results": [
        {
          "kind": "open",
          "r": [
            "2932",
            "1499",
            "-222"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1044",
            "533",
            "-79"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "40",
            "20",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1356",
            "667",
            "-101"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "79980",
            "39055",
            "-5939"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "158604",
            "77443",
            "-11777"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "159280",
            "77770",
            "-11827"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "676",
            "327",
            "-50"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "85540",
            "41285",
            "-6321"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "84864",
            "40958",
            "-6271"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "97572",
            "47059",
            "-7208"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "12708",
            "6101",
            "-937"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "210216",
            "100312",
            "-15461"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2089452",
            "997019",
            "-153673"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "375896",
            "179192",
            "-27635"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "165924",
            "78133",
            "-12137"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "29012",
            "13659",
            "-2122"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8148",
            "3821",
            "-595"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4508",
            "2111",
            "-329"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "868",
            "401",
            "-63"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "53420",
            "24675",
            "-3877"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "105972",
            "48949",
            "-7691"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "36572",
            "16889",
            "-2654"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3744",
            "1718",
            "-271"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4372",
            "1999",
            "-316"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "9372",
            "4279",
            "-677"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1732",
            "789",
            "-125"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "42588",
            "19391",
            "-3073"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "11924",
            "5423",
            "-860"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5108",
            "2301",
            "-367"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5540",
            "2495",
            "-398"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5972",
            "2689",
            "-429"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4124",
            "1853",
            "-296"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2276",
            "1017",
            "-163"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9140",
            "4075",
            "-654"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6864",
            "3058",
            "-491"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3948",
            "1721",
            "-280"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "44460",
            "19315",
            "-3149"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "22308",
            "9691",
            "-1580"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 1475,
      "side": 1,
      "supports": 29,
      "events": 19,
      "distinct": 18,
      "results": [
        {
          "kind": "open",
          "r": [
            "579",
            "66",
            "-17"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "273",
            "31",
            "-8"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "288951",
            "32670",
            "-8449"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "288678",
            "32639",
            "-8441"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "294021",
            "33226",
            "-8595"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5343",
            "587",
            "-154"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "295698",
            "31721",
            "-8423"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "881751",
            "94576",
            "-25115"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "158325",
            "16962",
            "-4507"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "68199",
            "7196",
            "-1927"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "68589",
            "7237",
            "-1938"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "390",
            "41",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8649",
            "902",
            "-243"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "16908",
            "1763",
            "-475"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1524423",
            "156752",
            "-42539"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3031938",
            "311741",
            "-84603"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3032835",
            "311833",
            "-84628"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "897",
            "92",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3414",
            "349",
            "-95"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2517",
            "257",
            "-70"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2559",
            "260",
            "-71"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "20514",
            "2083",
            "-569"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "16653",
            "1684",
            "-461"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "12792",
            "1285",
            "-353"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6201",
            "622",
            "-171"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5811",
            "581",
            "-160"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "16224",
            "1609",
            "-445"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "10413",
            "1028",
            "-285"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "11037",
            "1089",
            "-302"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "624",
            "61",
            "-17"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "177042",
            "17121",
            "-4799"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "353460",
            "34181",
            "-9581"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "608247",
            "58618",
            "-16461"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "254787",
            "24437",
            "-6880"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "85371",
            "8117",
            "-2296"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "257439",
            "24265",
            "-6896"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "128757",
            "12136",
            "-3449"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 1485,
      "side": 1,
      "supports": 29,
      "events": 19,
      "distinct": 19,
      "results": [
        {
          "kind": "open",
          "r": [
            "163662",
            "55009",
            "-9547"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "163593",
            "54986",
            "-9543"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "107355",
            "36203",
            "-6278"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "51117",
            "17420",
            "-3013"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "216876",
            "74197",
            "-12821"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "816387",
            "279368",
            "-48271"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "490971",
            "171277",
            "-29456"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1147497",
            "405740",
            "-69553"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "206868",
            "73147",
            "-12539"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "93711",
            "33142",
            "-5681"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "50343",
            "17805",
            "-3052"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6975",
            "2468",
            "-423"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "542757",
            "192111",
            "-32924"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "535782",
            "189643",
            "-32501"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "110811",
            "39223",
            "-6722"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "129084",
            "45695",
            "-7831"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "134163",
            "47515",
            "-8142"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5079",
            "1820",
            "-311"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "40233",
            "14681",
            "-2498"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "75387",
            "27542",
            "-4685"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "80418",
            "29467",
            "-5009"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5031",
            "1925",
            "-324"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "157683",
            "60810",
            "-10217"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "152652",
            "58885",
            "-9893"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "154833",
            "59739",
            "-10036"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2181",
            "854",
            "-143"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3879",
            "1547",
            "-258"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5577",
            "2240",
            "-373"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8049",
            "3261",
            "-542"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "10521",
            "4282",
            "-711"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "10872",
            "4427",
            "-735"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "351",
            "145",
            "-24"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "38034",
            "15761",
            "-2607"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "37683",
            "15616",
            "-2583"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "39243",
            "16263",
            "-2690"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1560",
            "647",
            "-107"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "201",
            "85",
            "-14"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2259",
            "968",
            "-159"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "483",
            "207",
            "-34"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 1666,
      "side": 1,
      "supports": 26,
      "events": 19,
      "distinct": 19,
      "results": [
        {
          "kind": "open",
          "r": [
            "6273",
            "0",
            "-100"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "6086",
            "0",
            "-97"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "2385",
            "0",
            "-38"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "1069",
            "0",
            "-17"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "5098",
            "0",
            "-81"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "4029",
            "0",
            "-64"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "442",
            "0",
            "-7"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "3927",
            "0",
            "-62"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "4624",
            "0",
            "-73"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "697",
            "0",
            "-11"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "824",
            "0",
            "-13"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "127",
            "0",
            "-2"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "4519",
            "0",
            "-71"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "13430",
            "0",
            "-211"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "15469",
            "0",
            "-243"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "2039",
            "0",
            "-32"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "701",
            "0",
            "-11"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "64",
            "0",
            "-1"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "1475",
            "0",
            "-23"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "1411",
            "0",
            "-22"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "1219",
            "0",
            "-19"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "1027",
            "0",
            "-16"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "3274",
            "0",
            "-51"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "8795",
            "0",
            "-137"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "10665",
            "0",
            "-166"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "1870",
            "0",
            "-29"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "129",
            "0",
            "-2"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "1097",
            "0",
            "-17"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "1747",
            "0",
            "-27"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "2397",
            "0",
            "-37"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "25687",
            "0",
            "-396"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "23290",
            "0",
            "-359"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "24461",
            "0",
            "-377"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "1171",
            "0",
            "-18"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "2670",
            "0",
            "-41"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "1499",
            "0",
            "-23"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "2026",
            "0",
            "-31"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "527",
            "0",
            "-8"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "593",
            "0",
            "-9"
          ],
          "feasible": true
        }
      ],
      "excluded": false
    },
    {
      "i": 1666,
      "side": -1,
      "supports": 27,
      "events": 19,
      "distinct": 19,
      "results": [
        {
          "kind": "open",
          "r": [
            "63",
            "0",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "317",
            "0",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2411",
            "0",
            "-38"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4505",
            "0",
            "-71"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3111",
            "0",
            "-49"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1717",
            "0",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2035",
            "0",
            "-32"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "318",
            "0",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "702",
            "0",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3894",
            "0",
            "-61"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2364",
            "0",
            "-37"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "834",
            "0",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4761",
            "0",
            "-74"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3927",
            "0",
            "-61"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5151",
            "0",
            "-80"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1224",
            "0",
            "-19"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1933",
            "0",
            "-30"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "709",
            "0",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2256",
            "0",
            "-35"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1547",
            "0",
            "-24"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2515",
            "0",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "968",
            "0",
            "-15"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2843",
            "0",
            "-44"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1875",
            "0",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2199",
            "0",
            "-34"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "324",
            "0",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2205",
            "0",
            "-34"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "12906",
            "0",
            "-199"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7849",
            "0",
            "-121"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2792",
            "0",
            "-43"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2339",
            "0",
            "-36"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8903",
            "0",
            "-137"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9164",
            "0",
            "-141"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "261",
            "0",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4525",
            "0",
            "-69"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8789",
            "0",
            "-134"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4658",
            "0",
            "-71"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "527",
            "0",
            "-8"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "593",
            "0",
            "-9"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 1921,
      "side": 1,
      "supports": 28,
      "events": 19,
      "distinct": 19,
      "results": [
        {
          "kind": "open",
          "r": [
            "7549",
            "87",
            "-148"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "21780",
            "251",
            "-427"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "46957",
            "539",
            "-920"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "25177",
            "288",
            "-493"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6235",
            "71",
            "-122"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "93288",
            "1061",
            "-1825"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "33075",
            "376",
            "-647"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5937",
            "67",
            "-116"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4877",
            "54",
            "-95"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8694",
            "95",
            "-169"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9981",
            "109",
            "-194"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1287",
            "14",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8247",
            "89",
            "-160"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "15207",
            "164",
            "-295"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "383525",
            "4129",
            "-7438"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "368318",
            "3965",
            "-7143"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "190633",
            "2052",
            "-3697"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "12948",
            "139",
            "-251"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9087",
            "97",
            "-176"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "32487",
            "346",
            "-629"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "36006",
            "383",
            "-697"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3519",
            "37",
            "-68"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "11038",
            "115",
            "-213"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7519",
            "78",
            "-145"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "62435",
            "644",
            "-1203"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "117351",
            "1210",
            "-2261"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "119793",
            "1235",
            "-2308"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2442",
            "25",
            "-47"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "47645",
            "477",
            "-914"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "45203",
            "452",
            "-867"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6205",
            "62",
            "-119"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4437",
            "44",
            "-85"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9189",
            "91",
            "-176"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4752",
            "47",
            "-91"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "82051",
            "807",
            "-1570"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "77299",
            "760",
            "-1479"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "109615",
            "1073",
            "-2096"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "32316",
            "313",
            "-617"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "32421",
            "314",
            "-619"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 3035,
      "side": -1,
      "supports": 27,
      "events": 19,
      "distinct": 19,
      "results": [
        {
          "kind": "open",
          "r": [
            "1729728",
            "37",
            "-26208"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1729662",
            "37",
            "-26207"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "43362",
            "1",
            "-657"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "178266",
            "7",
            "-2701"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "207174",
            "12",
            "-3139"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "28908",
            "5",
            "-438"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "38742",
            "8",
            "-587"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "9834",
            "3",
            "-149"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "13794",
            "8",
            "-209"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "59136",
            "37",
            "-896"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "112266",
            "74",
            "-1701"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "53130",
            "37",
            "-805"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "42834",
            "37",
            "-649"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "32538",
            "37",
            "-493"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "31680",
            "37",
            "-480"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "30822",
            "37",
            "-467"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "36630",
            "44",
            "-555"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5808",
            "7",
            "-88"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "10758",
            "14",
            "-163"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4950",
            "7",
            "-75"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7392",
            "13",
            "-112"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "17226",
            "32",
            "-261"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "17688",
            "33",
            "-268"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "462",
            "1",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2244",
            "5",
            "-34"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1782",
            "4",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "149622",
            "337",
            "-2267"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "147840",
            "333",
            "-2240"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "168762",
            "382",
            "-2557"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "20922",
            "49",
            "-317"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "18150",
            "43",
            "-275"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "15378",
            "37",
            "-233"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1653036",
            "4033",
            "-25046"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3290694",
            "8029",
            "-49859"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3327456",
            "8123",
            "-50416"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "36762",
            "94",
            "-557"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4686",
            "12",
            "-71"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "10098",
            "26",
            "-153"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "11220",
            "29",
            "-170"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 3700,
      "side": -1,
      "supports": 31,
      "events": 19,
      "distinct": 19,
      "results": [
        {
          "kind": "open",
          "r": [
            "1106343",
            "-61247",
            "-7231"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1103742",
            "-61103",
            "-7214"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "364446",
            "-20167",
            "-2382"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1082934",
            "-59899",
            "-7078"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "575586",
            "-31835",
            "-3762"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "68238",
            "-3771",
            "-446"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "74511",
            "-4116",
            "-487"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6273",
            "-345",
            "-41"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4437",
            "-244",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2601",
            "-143",
            "-17"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7497",
            "-412",
            "-49"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "27387",
            "-1505",
            "-179"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "252603",
            "-13846",
            "-1651"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "225216",
            "-12341",
            "-1472"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5147379",
            "-281134",
            "-33643"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4922163",
            "-268793",
            "-32171"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "821151",
            "-44842",
            "-5367"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4743",
            "-259",
            "-31"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "54774",
            "-2989",
            "-358"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "104805",
            "-5719",
            "-685"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "113679",
            "-6202",
            "-743"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8874",
            "-483",
            "-58"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1587681",
            "-85967",
            "-10377"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1578807",
            "-85484",
            "-10319"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4749426",
            "-256753",
            "-31042"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3170619",
            "-171269",
            "-20723"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1086606",
            "-58695",
            "-7102"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "89199",
            "-4816",
            "-583"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "830790",
            "-44849",
            "-5430"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2403171",
            "-129731",
            "-15707"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1205487",
            "-65076",
            "-7879"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7803",
            "-421",
            "-51"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "48042",
            "-2589",
            "-314"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "40239",
            "-2168",
            "-263"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "50337",
            "-2708",
            "-329"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "60435",
            "-3248",
            "-395"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "68238",
            "-3667",
            "-446"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7803",
            "-419",
            "-51"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "15912",
            "-853",
            "-104"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    }
  ],
  "totalPatterns": 514808,
  "excluded": [
    1283,
    1475,
    1485,
    1666,
    1921,
    3035,
    3700
  ],
  "strata": 310
}
```
