# X6 R192 — Seventeen-event rank-two exclusion replay

2026-11-25. Independent informed static auxiliary weight BRC research, exact finite necessary-relaxation replay, NOT_REVIEWED. Historical predecessor provenance EM-DIRECT-AE5AD5, current live research identity binding unconfirmed. Current X6 lookup r2-20261125-1410-x6-read SUCCEEDED at 2026-11-25T06:10:43.174265Z, Source 4e697e7f251c5609589eca00ff07d2ee61709e09, NO_CANONICAL_PUBLICATION_DIRECTORY; native_operational_view_evaluated=false, execution_authorized=false. No CLAIM or shared-state mutation.

## Inputs and scope

R191@92312bc554ede26c70eed35cb0ddb60bd22ee762 blob ea5b14e3532aff86a6fa2ef1249998e25b8cc10c; R182 census@6945e591116377f9386c7419b6ce31a2b9e8a146 blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82; R182 theorem@502d7abb2fe8470ed2cdabf242c2cc59a0c302ac. Preserve frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f, Port 10, 1935 unoriented integer directions, six BRC pair denominators, weights (17t,B,22t,D), exact optimizer and strict 3/2 near set. No new scoring. P000 V5 and ACTIVE worldview retained. This is an auxiliary coefficient representation, not native spatial/time dynamics.

Reuse R182 single-child sufficient event refinement for the fixed-endpoint depth-five necessary capacity relaxation. For each selected original rank-two sign class C, all event rays lie in its relative interior, sorted by exact rational ratio; coalesced event points and all open intervals are tested. Original root masks and support counts checked at each representative. Actual disconnected components clipped before their outer endpoints are retained. Entirely failing child suffices to exclude root. If both children have passing strata, further exact intersection required; no exclusion asserted from that case here. Passing the relaxation is not a six-query tree witness.

## Executed result

```json
[
  {
    "id": 850,
    "side": 1,
    "supports": 28,
    "events": 17,
    "distinct": 17,
    "strata": 35,
    "passing": 0
  },
  {
    "id": 1267,
    "side": 1,
    "supports": 31,
    "events": 17,
    "distinct": 15,
    "strata": 31,
    "passing": 0
  },
  {
    "id": 1305,
    "side": -1,
    "supports": 29,
    "events": 17,
    "distinct": 16,
    "strata": 33,
    "passing": 0
  },
  {
    "id": 1436,
    "side": 1,
    "supports": 31,
    "events": 17,
    "distinct": 17,
    "strata": 35,
    "passing": 0
  },
  {
    "id": 3471,
    "side": -1,
    "supports": 26,
    "events": 17,
    "distinct": 17,
    "strata": 35,
    "passing": 35
  },
  {
    "id": 3471,
    "side": 1,
    "supports": 28,
    "events": 18,
    "distinct": 18,
    "strata": 37,
    "passing": 0
  },
  {
    "id": 3555,
    "side": 1,
    "supports": 30,
    "events": 17,
    "distinct": 17,
    "strata": 35,
    "passing": 0
  },
  {
    "id": 3819,
    "side": 1,
    "supports": 28,
    "events": 17,
    "distinct": 17,
    "strata": 35,
    "passing": 0
  }
]
```

Total strata 276, sum of distinct sign pattern counts 480168, excluded IDs 850, 1267, 1305, 1436, 3471, 3555, 3819. Conditional on inherited R191 bank: remaining 195 = 107 rank two + 88 rank three. Global 6<=D_linear<=7 unchanged. Next min-18 census rows: [{"id":1337,"events":[[1,26],[-1,18]]},{"id":3501,"events":[[1,29],[-1,18]]}]. Any nonexcluded rows require both-child passing-set intersection. No independent review or Activity association yet.

## Standalone reproduction

Executed the transcribed R191 recurrence with the selected exact census inputs using BigInt; no floating-point geometric predicate. The following self-contained JavaScript reproduces the full results.

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
const rows=[{"i":850,"a":"1115201468944","b":"2250684612216295","r":["169","20","-6"],"local":37,"vertices":[["1560","179","-55"],["806","101","-29"]],"sides":[{"side":1,"supports":28,"events":["1204,59715,237790","142,6977,28045","15,151,923","1954,97373,385915","2,99,395","206,10327,40685","3,52,260","3,53,259","3,53,261","42,2077,8295","5,87,435","6,305,1185","62,3147,12245","81,2392,10244","82,4033,16195","92,4575,18170","93,2828,12136"]},{"side":-1,"supports":29,"events":["1,10,62","1,18,87","1,29,127","107,3290,14362","11,336,1452","12,355,1517","13,225,1131","14,171,966","149,4563,19797","19,237,1311","19,327,1649","21,209,1309","24,167,1237","27,823,3545","28,845,3583","3,53,259","32,945,4047","35,1037,4423","67,1917,8535","67,2023,8585","76,2295,9741"]}]},{"i":1267,"a":"1132515535440","b":"2250667298145711","r":["101","37","-6"],"local":57,"vertices":[["133","51","-8"],["69","23","-4"]],"sides":[{"side":1,"supports":31,"events":["1,12,92","1,20,136","1,30,204","1,31,203","2,5,64","23,285,2107","23,441,3147","295,3669,27011","295,5697,40323","295,8739,60291","3,27,211","3,38,274","4,49,367","5,43,341","9,175,1229","9,179,1225","9,400,2564"]},{"side":-1,"supports":27,"events":["1,9,73","10,81,672","10,90,729","101,901,6953","11,510,3366","127,1103,8683","143,6120,38148","15,135,1087","16,139,1094","17,153,1188","176,1029,9267","178,543,6399","181,2196,16628","181,3600,24636","181,5706,36648","2,17,136","21,263,1921","216,1319,11317","260,1581,13629","28,165,1473","3,38,274","3,61,407","301,2669,20689","332,1913,17509","34,85,1085","4,35,274","49,1000,6644","49,155,1756","49,610,4486","49,976,6668","53,425,3553","56,459,3774","57,683,5245","68,2939,18457","87,1069,7979","88,1065,8087","88,1741,11987","88,2755,17837","9,113,823","9,76,611","94,558,4941"]}]},{"i":1305,"a":"901195574149112","b":"1350604239273991","r":["2866","-144","-19"],"local":71,"vertices":[["265","-13","-2"],["2601","-131","-17"]],"sides":[{"side":1,"supports":30,"events":["1,1,137","1,12,56","1,6,98","10,53,987","10,61,979","105,121,14465","11,70,1074","113,1372,6516","127,1299,8763","13,68,1284","15,8,2020","159,1052,15484","16,315,40","162,3196,405","17,111,1657","19,11,2563","19,115,1861","19,28,2648","2,27,90","2,8,243","201,76,26912","214,1129,21127","237,2772,13420","245,2972,13752","25,261,1725","25,9,3345","26,104,2909","26,259,1794","3,1,401","3,12,326","3,16,296","3,17,295","3,20,292","31,384,1748","327,265,44489","356,2243,34781","37,44,5104","4,25,391","43,244,4228","57,331,5597","58,567,4002","6,41,583","6,43,581","62,1223,155","67,792,3740","69,1264,920","7,50,678","76,935,4411","8,32,917","83,488,8144","84,1649,210","9,49,887","9,56,880","9,58,878","9,64,872","93,1747,775"]},{"side":-1,"supports":29,"events":["1,1,137","1,7,97","1101,20069,14680","1101,20101,13946","189,1181,18475","19,104,1872","2,27,90","24,473,60","25,308,1408","4,16,485","4,55,179","50,31,6755","58,1142,145","6,37,587","75,404,7396","82,1628,205","83,1012,4796"]}]},{"i":1436,"a":"76277271625735","b":"2175522542059480","r":["-2264","194","7"],"local":37,"vertices":[["-1774","156","5"],["-2754","232","9"]],"sides":[{"side":1,"supports":31,"events":["1,11,15","19,200,541","2,13,299","2,21,57","21,125,3397","22,257,55","224,2209,10895","23,211,1587","24,275,60","34,395,85","38,373,1850","394,4501,985","47,20,14722","7,4,2210","72,847,180","8,27,1800","91,974,2575"]},{"side":-1,"supports":28,"events":["1,1,323","10,51,1938","106,1204,265","158,1821,395","19,210,284","2,13,299","2,21,57","23,146,3442","295,1882,44138","3,1,935","3,17,481","305,1844,49480","35,173,6739","4,25,599","43,205,8219","56,257,10624","59,51,18921","61,400,9116","64,373,10313","73,448,11876","76,801,2163","9,52,1448"]}]},{"i":3471,"a":"18708593376792","b":"1951616243597799","r":["263","16","-6"],"local":35,"vertices":[["174","11","-4"],["89","5","-2"]],"sides":[{"side":1,"supports":28,"events":["172,5513,21672","1742,105429,344045","176,5557,22176","182,10547,35945","194,11539,38315","23,714,2898","29,883,3654","3,50,262","35,1089,4410","5,153,630","5,84,436","512,31063,101120","520,31199,102700","605,19506,76230","61,994,5350","63,1900,7938","724,41863,142990","8,253,1008"]},{"side":-1,"supports":26,"events":["10,586,1975","102,5920,20145","111,1853,9691","121,1114,8174","124,1161,8556","24,733,3024","26,1480,5135","36,1171,4536","38,2141,7505","382,21899,75445","46,2637,9085","56,3253,11060","58,567,4002","78,727,5382","79,756,5451","8,471,1580","9,146,790"]}]},{"i":3555,"a":"909987342843896","b":"1201074982486023","r":["3762","-212","-19"],"local":34,"vertices":[["396","-23","-2"],["3366","-189","-17"]],"sides":[{"side":1,"supports":30,"events":["1,9,95","13,120,1232","158,2709,395","173,1560,16432","2,27,90","2,31,47","215,1952,20408","231,3842,2926","278,4843,695","3,38,170","31,384,1748","33,544,440","442,7520,1105","50,671,2254","6,80,271","618,5653,58619","76,935,4411"]},{"side":-1,"supports":30,"events":["1,9,95","108,1873,270","18,293,240","2,27,90","2,31,47","22,377,55","27,445,342","27,446,360","33,533,418","33,535,440","34,591,85","4,55,179","454,7757,1135","54,931,135","592,7919,26713","594,10319,1485","706,12041,1765","72,1237,180","8,123,189","9,146,114"]}]},{"i":3819,"a":"18708459159064","b":"2233091220308455","r":["269","20","-7"],"local":41,"vertices":[["2601","195","-68"],["89","5","-2"]],"sides":[{"side":1,"supports":28,"events":["127,1299,8763","172,5513,21672","1742,105429,344045","176,5557,22176","182,10547,35945","194,11539,38315","20,89,1081","23,714,2898","25,261,1725","26,135,1386","346,1755,18486","35,1089,4410","512,31063,101120","520,31199,102700","605,19506,76230","724,41863,142990","8,253,1008"]},{"side":-1,"supports":26,"events":["10,586,1975","102,5920,20145","166,833,8878","169,1566,11346","2,112,395","2,9,108","20,93,1077","202,990,10827","26,1480,5135","26,259,1794","36,1171,4536","38,165,2058","38,2141,7505","382,21899,75445","4,17,217","46,2637,9085","50,252,2673","56,3253,11060","6,31,320","604,2741,32593","7,66,462","78,385,4178","8,39,429","8,471,1580"]}]}];
console.log(JSON.stringify(replay(data,rows),null,2));
```

## Full actual output

```json
{
  "output": [
    {
      "i": 850,
      "side": 1,
      "supports": 28,
      "events": 17,
      "distinct": 17,
      "results": [
        {
          "kind": "open",
          "r": [
            "879",
            "101",
            "-31"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "198",
            "23",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "367",
            "43",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6408",
            "751",
            "-227"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "64902",
            "7663",
            "-2303"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "123396",
            "14575",
            "-4379"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "62980",
            "7439",
            "-2235"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2564",
            "303",
            "-91"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6649",
            "786",
            "-236"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4085",
            "483",
            "-145"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "88338",
            "10465",
            "-3137"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "84253",
            "9982",
            "-2992"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "230017",
            "27465",
            "-8183"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "145764",
            "17483",
            "-5191"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "140329",
            "16883",
            "-5001"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "275223",
            "33166",
            "-9812"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "277719",
            "33467",
            "-9901"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2496",
            "301",
            "-89"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3336",
            "403",
            "-119"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4176",
            "505",
            "-149"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "288167",
            "35011",
            "-10293"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2589327",
            "314594",
            "-92488"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "202318",
            "24587",
            "-7227"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "243125",
            "29624",
            "-8690"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "568895",
            "69552",
            "-20350"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3170245",
            "387688",
            "-113410"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1057186",
            "129283",
            "-37819"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1313",
            "161",
            "-47"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "56386",
            "6923",
            "-2019"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "55073",
            "6762",
            "-1972"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "80895",
            "9982",
            "-2900"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "106717",
            "13202",
            "-3828"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5213",
            "645",
            "-187"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "13182",
            "1633",
            "-473"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6994",
            "867",
            "-251"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 1267,
      "side": 1,
      "supports": 31,
      "events": 17,
      "distinct": 15,
      "results": [
        {
          "kind": "open",
          "r": [
            "35243",
            "13402",
            "-2115"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "70353",
            "26753",
            "-4222"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "70537",
            "26822",
            "-4233"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "184",
            "69",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "251",
            "94",
            "-15"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "318",
            "119",
            "-19"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "67",
            "25",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "486",
            "181",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1528",
            "565",
            "-91"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "45354",
            "16769",
            "-2701"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "487",
            "180",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1398",
            "511",
            "-83"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "775",
            "283",
            "-46"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "152",
            "55",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1697",
            "603",
            "-100"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6636",
            "2357",
            "-391"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4430",
            "1573",
            "-261"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2224",
            "789",
            "-131"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "747",
            "265",
            "-44"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "17",
            "6",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "28705",
            "10119",
            "-1688"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "28688",
            "10113",
            "-1687"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "15067",
            "5311",
            "-886"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1446",
            "509",
            "-85"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "885",
            "311",
            "-52"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "324",
            "113",
            "-19"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "529",
            "184",
            "-31"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "205",
            "71",
            "-12"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "325",
            "112",
            "-19"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "120",
            "41",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "189",
            "64",
            "-11"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 1305,
      "side": -1,
      "supports": 29,
      "events": 17,
      "distinct": 16,
      "results": [
        {
          "kind": "open",
          "r": [
            "1201",
            "-59",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "936",
            "-46",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4962",
            "-244",
            "-37"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8988",
            "-442",
            "-67"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "19262",
            "-948",
            "-143"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "29536",
            "-1454",
            "-219"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6073",
            "-299",
            "-45"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "829",
            "-41",
            "-6"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1252",
            "-62",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2927",
            "-145",
            "-21"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1534",
            "-76",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "141",
            "-7",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "288234",
            "-14324",
            "-2033"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "288093",
            "-14317",
            "-2032"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "73869",
            "-3671",
            "-521"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7383",
            "-367",
            "-52"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4845",
            "-241",
            "-34"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2307",
            "-115",
            "-16"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3029",
            "-151",
            "-21"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "722",
            "-36",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1303",
            "-65",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "581",
            "-29",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1021",
            "-51",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "440",
            "-22",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "51725",
            "-2591",
            "-349"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "51285",
            "-2569",
            "-346"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "71041",
            "-3559",
            "-479"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "19756",
            "-990",
            "-133"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1337",
            "-67",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "299",
            "-15",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4096",
            "-206",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7893",
            "-397",
            "-52"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3498",
            "-176",
            "-23"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 1436,
      "side": 1,
      "supports": 31,
      "events": 17,
      "distinct": 17,
      "results": [
        {
          "kind": "open",
          "r": [
            "-6363",
            "559",
            "18"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-10952",
            "962",
            "31"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-11993",
            "1053",
            "34"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1041",
            "91",
            "3"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1385",
            "121",
            "4"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1729",
            "151",
            "5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-5830",
            "508",
            "17"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-9931",
            "865",
            "29"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-10610",
            "924",
            "31"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-679",
            "59",
            "2"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-108296",
            "9410",
            "319"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-324209",
            "28171",
            "955"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-13915",
            "1209",
            "41"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-65411",
            "5681",
            "193"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-85221",
            "7397",
            "252"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-19810",
            "1716",
            "59"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-41133",
            "3559",
            "123"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-21323",
            "1843",
            "64"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-11327",
            "979",
            "34"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1331",
            "115",
            "4"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-20925",
            "1807",
            "63"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-19594",
            "1692",
            "59"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-326",
            "28",
            "1"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-131018",
            "11244",
            "403"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-159483",
            "13675",
            "492"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-28465",
            "2431",
            "89"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-42667",
            "3639",
            "134"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-14202",
            "1208",
            "45"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-63103",
            "5367",
            "200"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-48901",
            "4159",
            "155"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-33712",
            "2866",
            "107"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-18523",
            "1573",
            "59"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-79581",
            "6721",
            "258"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-61058",
            "5148",
            "199"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-15953",
            "1345",
            "52"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 3471,
      "side": -1,
      "supports": 26,
      "events": 17,
      "distinct": 17,
      "results": [
        {
          "kind": "open",
          "r": [
            "13507",
            "847",
            "-310"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "13333",
            "836",
            "-306"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "24760",
            "1549",
            "-568"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "36187",
            "2262",
            "-830"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "45781",
            "2861",
            "-1050"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "9594",
            "599",
            "-220"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "13539",
            "839",
            "-310"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "58101",
            "3596",
            "-1330"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "88161",
            "5455",
            "-2018"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "30060",
            "1859",
            "-688"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "34345",
            "2123",
            "-786"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "4285",
            "264",
            "-98"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "5952",
            "365",
            "-136"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "19523",
            "1196",
            "-446"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "15671",
            "960",
            "-358"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "137187",
            "8404",
            "-3134"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "146497",
            "8965",
            "-3346"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "9310",
            "561",
            "-212"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "29779",
            "1793",
            "-678"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "20469",
            "1232",
            "-466"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "11159",
            "671",
            "-254"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "1849",
            "110",
            "-42"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "20274",
            "1199",
            "-460"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "38699",
            "2288",
            "-878"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "77495",
            "4579",
            "-1758"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "38796",
            "2291",
            "-880"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "163245",
            "9574",
            "-3698"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "124449",
            "7283",
            "-2818"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "154236",
            "8965",
            "-3488"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "29787",
            "1682",
            "-670"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "36013",
            "2033",
            "-810"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "6226",
            "351",
            "-140"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "13253",
            "747",
            "-298"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "7027",
            "396",
            "-158"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "7116",
            "401",
            "-160"
          ],
          "feasible": true
        }
      ],
      "excluded": false
    },
    {
      "i": 3471,
      "side": 1,
      "supports": 28,
      "events": 18,
      "distinct": 18,
      "results": [
        {
          "kind": "open",
          "r": [
            "1307",
            "82",
            "-30"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "143596",
            "9009",
            "-3296"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "148751",
            "9328",
            "-3414"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5155",
            "319",
            "-118"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "70701",
            "4370",
            "-1618"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "65546",
            "4051",
            "-1500"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "77183",
            "4766",
            "-1766"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11637",
            "715",
            "-266"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3430784",
            "207779",
            "-78200"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3419147",
            "207064",
            "-77934"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "713535",
            "43186",
            "-16262"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "862063",
            "52052",
            "-19638"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "916705",
            "55341",
            "-20882"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "54642",
            "3289",
            "-1244"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "61059",
            "3674",
            "-1390"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6417",
            "385",
            "-146"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "434722",
            "25553",
            "-9852"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "428305",
            "25168",
            "-9706"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "431659",
            "25365",
            "-9782"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3354",
            "197",
            "-76"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "971",
            "57",
            "-22"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1501",
            "88",
            "-34"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "21653",
            "1263",
            "-490"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "951231",
            "55484",
            "-21526"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "956899",
            "55811",
            "-21654"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5668",
            "327",
            "-128"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2584759",
            "149047",
            "-58366"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2579091",
            "148720",
            "-58238"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "751658",
            "43329",
            "-16972"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "427541",
            "24596",
            "-9650"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1943855",
            "111111",
            "-43822"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1516314",
            "86515",
            "-34172"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2310805",
            "131807",
            "-52074"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "794491",
            "45292",
            "-17902"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1685699",
            "95862",
            "-37966"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2576907",
            "146432",
            "-58030"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2576996",
            "146437",
            "-58032"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 3555,
      "side": 1,
      "supports": 30,
      "events": 17,
      "distinct": 17,
      "results": [
        {
          "kind": "open",
          "r": [
            "744678",
            "-43217",
            "-3761"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1488960",
            "-86411",
            "-7520"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "94050",
            "-5458",
            "-475"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "15840",
            "-917",
            "-80"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "17622",
            "-1020",
            "-89"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1782",
            "-103",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "13266",
            "-766",
            "-67"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "38016",
            "-2195",
            "-192"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "10692",
            "-617",
            "-54"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "154440",
            "-8911",
            "-780"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "690822",
            "-39800",
            "-3489"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "536382",
            "-30889",
            "-2709"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "133848",
            "-7707",
            "-676"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "132858",
            "-7646",
            "-671"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5544",
            "-319",
            "-28"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "16830",
            "-967",
            "-85"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "210078",
            "-12048",
            "-1061"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "193248",
            "-11081",
            "-976"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "193842",
            "-11115",
            "-979"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "594",
            "-34",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1119888",
            "-63779",
            "-5656"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1119294",
            "-63745",
            "-5653"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "562716",
            "-32047",
            "-2842"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6138",
            "-349",
            "-31"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "482526",
            "-27349",
            "-2437"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "958914",
            "-54349",
            "-4843"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "337590",
            "-19132",
            "-1705"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "53856",
            "-3047",
            "-272"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "32868",
            "-1859",
            "-166"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11880",
            "-671",
            "-60"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "15642",
            "-883",
            "-79"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3762",
            "-212",
            "-19"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "192060",
            "-10809",
            "-970"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "380358",
            "-21406",
            "-1921"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "383724",
            "-21595",
            "-1938"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 3819,
      "side": 1,
      "supports": 28,
      "events": 17,
      "distinct": 17,
      "results": [
        {
          "kind": "open",
          "r": [
            "4806",
            "357",
            "-125"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11817",
            "876",
            "-307"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "28899",
            "2082",
            "-739"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "161577",
            "11616",
            "-4127"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "174429",
            "12513",
            "-4450"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "12852",
            "897",
            "-323"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "14373",
            "1002",
            "-361"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1521",
            "105",
            "-38"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "161",
            "11",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3309",
            "225",
            "-82"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1214560",
            "80227",
            "-29637"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1211251",
            "80002",
            "-29555"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "505925",
            "33371",
            "-12336"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "306524",
            "20111",
            "-7453"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "342013",
            "22399",
            "-8308"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "35489",
            "2288",
            "-855"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "17807",
            "1148",
            "-429"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "125",
            "8",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "18104",
            "1151",
            "-433"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "17979",
            "1143",
            "-430"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "28613",
            "1802",
            "-681"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "10634",
            "659",
            "-251"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "90793",
            "5524",
            "-2123"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "352538",
            "21437",
            "-8241"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "389607",
            "23673",
            "-9104"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "37069",
            "2236",
            "-863"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "502741",
            "29848",
            "-11611"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "968413",
            "57460",
            "-22359"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "273905",
            "16211",
            "-6316"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "401112",
            "23595",
            "-9221"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1862335",
            "108043",
            "-42518"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3323558",
            "192491",
            "-75815"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4306999",
            "249067",
            "-98174"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "983441",
            "56576",
            "-22359"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "16670",
            "959",
            "-379"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    }
  ],
  "totalPatterns": 480168,
  "excluded": [
    850,
    1267,
    1305,
    1436,
    3471,
    3555,
    3819
  ],
  "strata": 276
}
```
