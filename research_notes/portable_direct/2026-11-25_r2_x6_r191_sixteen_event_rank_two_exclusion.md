# X6 R191 — Sixteen-event rank-two exclusion

2026-11-25. Independent informed static auxiliary weight BRC research; exact finite necessary-relaxation replay, NOT_REVIEWED. Historical provenance EM-DIRECT-AE5AD5; live execution binding unconfirmed. X6 read r2-20261125-1311-x6-read SUCCEEDED at 2026-11-25T05:12:11.002462Z, Source 4c06b309b04dc03a0ac466297225fe2eb043525e, NO_CANONICAL_PUBLICATION_DIRECTORY, native_operational_view_evaluated=false, execution_authorized=false. No CLAIM or shared owner change. P000 V5 and ACTIVE worldview retained.

## Input and coverage

R190@5b1679368f07d744eef051a45cfcd39d1a7c597b (blob dc61a58820a620340029e69aec604b0715dc3720), R182 census@6945e591116377f9386c7419b6ce31a2b9e8a146 (blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82), R182 single-child sufficiency theorem@502d7abb2fe8470ed2cdabf242c2cc59a0c302ac; inherited frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f. Same Port 10, 1935 unoriented directions, six BRC pair denominators, positive weights (17t,B,22t,D), exact optimizer and strict 3/2 near set. No new direction scoring. Select every census row with smaller side event count 16. Exact ratio sorting covers open intervals and event singleton points, with original root masks and clipped support count checked. Actual disconnected components clipped before retaining outer endpoints. R182 proves constancy of the necessary endpoint-capacity decision on each child's own strata. A wholly failing child excludes the root. This is not a sufficiency test for a six-query tree and does not describe native spatial/time dynamics.

## Actual calculation

[
  {
    "id": 1716,
    "side": -1,
    "supports": 26,
    "events": 16,
    "strata": 33,
    "passing": 33
  },
  {
    "id": 1716,
    "side": 1,
    "supports": 28,
    "events": 35,
    "strata": 71,
    "passing": 0
  },
  {
    "id": 3487,
    "side": 1,
    "supports": 29,
    "events": 15,
    "strata": 31,
    "passing": 0
  },
  {
    "id": 3503,
    "side": -1,
    "supports": 31,
    "events": 16,
    "strata": 33,
    "passing": 0
  },
  {
    "id": 3539,
    "side": -1,
    "supports": 30,
    "events": 16,
    "strata": 33,
    "passing": 0
  },
  {
    "id": 3588,
    "side": 1,
    "supports": 28,
    "events": 16,
    "strata": 33,
    "passing": 0
  }
]

Total strata 234; sum of distinct observation sign-pattern counts 406178; excluded IDs 1716, 3487, 3503, 3539, 3588. Conditional on inherited R190 exclusion bank, remaining 202 = 114 rank two + 88 rank three. Global 6<=D_linear<=7 unchanged. No independent review or Activity association yet. Next min-17 rows: [{"id":850,"events":[[1,17],[-1,21]]},{"id":1267,"events":[[1,17],[-1,41]]},{"id":1305,"events":[[1,56],[-1,17]]},{"id":1436,"events":[[1,17],[-1,22]]},{"id":3471,"events":[[1,18],[-1,17]]},{"id":3555,"events":[[1,17],[-1,20]]},{"id":3819,"events":[[1,17],[-1,24]]}]. If any row was not wholly excluded, intersect both child passing strata exactly before claiming exclusion.

## Standalone reproduction

The inherited R190 replay was transcribed and executed on the selected frozen census rows, using BigInt. Full inputs and outputs below.

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
const rows=[{"i":1716,"a":"898317677494040","b":"1353482119413991","r":["1281","18","-23"],"local":50,"vertices":[["1003","10","-17"],["1559","26","-29"]],"sides":[{"side":1,"supports":28,"events":["1,39,87","1,43,87","1,82,126","1,92,126","11,1071,1386","113,10540,14238","122,25655,24095","14,1369,1764","14,2326,2765","14,2344,2765","15,481,1175","190,17933,23940","2,327,395","2,371,395","2,395,395","201,6017,15745","21,629,1645","21,656,1645","22,965,1914","23,2601,2898","24,771,1880","249,7990,19505","28,1191,2436","3,283,378","36,1105,2820","37,3333,4662","38,7900,7505","46,10064,9085","697,61704,87822","7,288,609","7,600,882","72,6125,9072","8,1501,1580","81,2261,6345","9,775,1134"]},{"side":-1,"supports":26,"events":["1,108,126","108,3227,8460","11,421,957","14,1551,1764","1407,44069,110215","265,11109,23055","3,90,235","37,1617,3219","4,159,348","4,185,348","4,341,504","61,594,3894","7,288,609","795,25709,62275","8,1397,1580","89,3723,7743"]}]},{"i":3487,"a":"909987338649592","b":"1341812470841351","r":["592","-34","-3"],"local":33,"vertices":[["196","-11","-1"],["396","-23","-2"]],"sides":[{"side":1,"supports":29,"events":["1,9,95","158,2709,395","173,1560,16432","2,27,90","2,31,47","215,1952,20408","231,3842,2926","278,4843,695","31,384,1748","33,544,440","442,7520,1105","50,671,2254","6,80,271","618,5653,58619","76,935,4411","85,193,14549"]},{"side":-1,"supports":30,"events":["1,9,95","108,1873,270","18,293,240","2,27,90","2,31,47","22,377,55","27,445,342","27,446,360","33,533,418","33,535,440","34,591,85","378,6647,945","454,7757,1135","54,931,135","592,7919,26713","594,10319,1485","706,12041,1765","72,1237,180","8,123,189","9,146,114"]}]},{"i":3503,"a":"1049624782700536","b":"1202174494113799","r":["226","-16","-1"],"local":61,"vertices":[["2964","-209","-14"],["1782","-127","-7"]],"sides":[{"side":1,"supports":28,"events":["1,1,206","1,5,151","103,357,18615","11,60,1656","115,1431,3054","118,307,20510","120,391,21488","135,137,27826","15,73,2345","162,1315,15533","171,736,25940","18,187,1067","19,28,3986","21,176,2008","23,118,3626","23,183,2209","237,1000,36284","26,259,1794","27,212,2596","270,769,47462","29,164,4360","3,17,451","3,26,286","33,158,4990","35,176,5284","397,2056,62684","4,3,816","401,2072,63292","41,109,7145","41,34,8390","451,2272,68084","5,21,765","5,26,754","50,567,2358","58,567,4002","59,41,12010","6,11,1276","62,701,2926","7,40,1052","7,72,420","7,76,392","705,6047,67273","717,6115,68453","73,409,10979","79,756,5451","8,21,1392"]},{"side":-1,"supports":31,"events":["1,8,96","103,1122,5742","11,34,1955","15,151,923","151,1606,8690","16,181,755","19,93,2871","2,28,5","29,157,4367","3,13,455","3,26,286","32,363,1509","4,45,189","5,22,770","56,621,2655","7,71,427"]}]},{"i":3539,"a":"1049625319571448","b":"1201074982486023","r":["231","-16","-1"],"local":71,"vertices":[["1452","-97","-7"],["1782","-127","-7"]],"sides":[{"side":1,"supports":29,"events":["1,1,206","1,5,151","103,357,18615","107,274,18563","107,64,21698","11,60,1656","115,1548,1442","118,307,20510","120,391,21488","135,137,27826","14,199,35","15,73,2345","162,1315,15533","171,736,25940","186,2493,2480","19,28,3986","2,5,346","21,176,2008","21,285,266","224,3249,560","23,118,3626","237,1000,36284","248,3519,620","26,367,65","262,3778,655","270,769,47462","278,3910,695","29,164,4360","3,17,451","3,26,286","3,38,79","3,40,40","33,158,4990","35,176,5284","358,5180,895","368,5171,920","397,2056,62684","4,3,816","401,2072,63292","41,109,7145","41,34,8390","418,5858,1045","420,5639,5320","451,2272,68084","5,21,765","5,26,754","59,41,12010","6,11,1276","7,40,1052","705,6047,67273","717,6115,68453","73,409,10979","8,21,1392","842,12040,2105","87,1172,1102","93,1251,1178"]},{"side":-1,"supports":30,"events":["11,34,1955","12,157,311","16,233,40","172,1989,8073","18,241,227","19,263,231","19,93,2871","2,28,5","29,157,4367","3,13,455","3,26,286","48,643,608","48,647,640","5,22,770","54,749,684","54,751,720"]}]},{"i":3588,"a":"410960920583","b":"2250289341136888","r":["-946","91","-1"],"local":82,"vertices":[["-11","1","0"],["-935","90","-1"]],"sides":[{"side":1,"supports":28,"events":["115,1513,60911","135,1787,71689","16,183,8007","19,234,4212","197,3281,116059","2,21,5","21,227,319","22,241,55","296,3199,8345","3,34,434","3,38,1564","3,38,664","3,40,1598","54,655,27659","55,872,31654","81,935,40681"]},{"side":-1,"supports":30,"events":["1,12,222","1,17,1127","1,17,1153","1,17,1738","1,17,1907","1,17,1972","1,17,646","1,17,711","1,17,763","1,17,815","1,17,867","1,17,945","1,17,984","10,121,2219","11,122,1594","11,124,1592","11,187,9992","13,148,2894","13,163,6749","151,1644,2282","16,272,13651","17,205,8687","2,23,289","2,34,1383","2,34,1955","223,2403,6294","23,317,12427","248,2747,46471","25,308,4840","263,3132,58410","28,355,6197","289,3622,150008","29,324,5448","293,3638,151504","3,32,46","3,34,434","3,34,668","3,38,664","3,51,1951","3,51,2081","3,51,2516","3,51,3797","3,51,4343","3,51,6059","3,51,6605","37,436,18734","38,433,3519","38,563,21199","4,68,3247","418,4403,1045","5,85,3077","53,628,7640","53,867,30957","6,102,5423","7,102,3876","7,80,1558","7,87,1359","73,826,6766","8,136,10355","8,136,6533","83,936,7696","9,101,835","9,153,11170","9,153,11222","9,153,17956","9,153,18008","9,153,6646","9,153,6698"]}]}];
console.log(JSON.stringify(replay(data,rows),null,2));
```

## Actual output

```json
{
  "output": [
    {
      "i": 1716,
      "side": -1,
      "supports": 26,
      "events": 16,
      "distinct": 16,
      "results": [
        {
          "kind": "open",
          "r": [
            "39017",
            "404",
            "-665"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "77031",
            "798",
            "-1313"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "16015",
            "166",
            "-273"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "51089",
            "530",
            "-871"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "25925",
            "269",
            "-442"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "761",
            "8",
            "-13"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "467",
            "5",
            "-8"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "5310",
            "57",
            "-91"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "588863",
            "6623",
            "-10166"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "583553",
            "6566",
            "-10075"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "611978",
            "6899",
            "-10569"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "28425",
            "333",
            "-494"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "53637",
            "648",
            "-937"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "25212",
            "315",
            "-443"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "27427",
            "343",
            "-482"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "2215",
            "28",
            "-39"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "189508",
            "2413",
            "-3341"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "187293",
            "2385",
            "-3302"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "20472",
            "261",
            "-361"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "78843",
            "1008",
            "-1391"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "47157",
            "603",
            "-832"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "62628",
            "801",
            "-1105"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "72147",
            "927",
            "-1274"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "9519",
            "126",
            "-169"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "7287",
            "99",
            "-130"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "5055",
            "72",
            "-91"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "18647",
            "275",
            "-338"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "69533",
            "1028",
            "-1261"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "9315",
            "138",
            "-169"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "4987",
            "76",
            "-91"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "5697",
            "87",
            "-104"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "710",
            "11",
            "-13"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "2269",
            "37",
            "-42"
          ],
          "feasible": true
        }
      ],
      "excluded": false
    },
    {
      "i": 1716,
      "side": 1,
      "supports": 28,
      "events": 35,
      "distinct": 35,
      "results": [
        {
          "kind": "open",
          "r": [
            "131206",
            "1321",
            "-2227"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "130203",
            "1311",
            "-2210"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "151442",
            "1535",
            "-2573"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "21239",
            "224",
            "-363"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "60241",
            "637",
            "-1030"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "219725",
            "2324",
            "-3757"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "12574",
            "133",
            "-215"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6607",
            "70",
            "-113"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "546578",
            "5981",
            "-9395"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "539971",
            "5911",
            "-9282"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "557270",
            "6107",
            "-9581"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "17299",
            "196",
            "-299"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "459293",
            "5291",
            "-7960"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1360580",
            "15677",
            "-23581"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1371929",
            "15809",
            "-23778"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11349",
            "132",
            "-197"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "428864",
            "5015",
            "-7451"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "417515",
            "4883",
            "-7254"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "445820",
            "5219",
            "-7747"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "28305",
            "336",
            "-493"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1263",
            "15",
            "-22"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "744",
            "9",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "41511",
            "513",
            "-728"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "40767",
            "504",
            "-715"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4447",
            "55",
            "-78"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "21491",
            "266",
            "-377"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "71828",
            "893",
            "-1261"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "50337",
            "627",
            "-884"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "70877",
            "884",
            "-1245"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "20540",
            "257",
            "-361"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8133",
            "102",
            "-143"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3859",
            "49",
            "-68"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "20368",
            "259",
            "-359"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "36877",
            "469",
            "-650"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "313676",
            "4079",
            "-5551"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "276799",
            "3610",
            "-4901"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "289900",
            "3781",
            "-5133"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "13101",
            "171",
            "-232"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "22620",
            "297",
            "-401"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "9519",
            "126",
            "-169"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "171257",
            "2273",
            "-3042"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "161738",
            "2147",
            "-2873"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "238447",
            "3175",
            "-4238"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "76709",
            "1028",
            "-1365"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "78111",
            "1047",
            "-1390"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1402",
            "19",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "10143",
            "138",
            "-181"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "18884",
            "257",
            "-337"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "169607",
            "2366",
            "-3041"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "150723",
            "2109",
            "-2704"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2915325",
            "41838",
            "-52559"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2764602",
            "39729",
            "-49855"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "460868",
            "6623",
            "-8311"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "606",
            "9",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "11601",
            "174",
            "-211"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "34197",
            "513",
            "-622"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "60603",
            "912",
            "-1103"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "26406",
            "399",
            "-481"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "98269",
            "1501",
            "-1794"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "268401",
            "4104",
            "-4901"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "383132",
            "5903",
            "-7007"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "114731",
            "1799",
            "-2106"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "126767",
            "1988",
            "-2327"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "12036",
            "189",
            "-221"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "125525",
            "1988",
            "-2309"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "113489",
            "1799",
            "-2088"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "117005",
            "1856",
            "-2153"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3516",
            "57",
            "-65"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9682",
            "157",
            "-179"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "15848",
            "257",
            "-293"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "17407",
            "283",
            "-322"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 3487,
      "side": 1,
      "supports": 29,
      "events": 16,
      "distinct": 15,
      "results": [
        {
          "kind": "open",
          "r": [
            "71584",
            "-4026",
            "-365"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "286140",
            "-16093",
            "-1459"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "73940",
            "-4159",
            "-377"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "9620",
            "-543",
            "-49"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "63440",
            "-3586",
            "-323"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "624780",
            "-35317",
            "-3181"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "645012",
            "-36461",
            "-3284"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "20232",
            "-1144",
            "-103"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "25548",
            "-1447",
            "-130"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "56412",
            "-3197",
            "-287"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "30468",
            "-1727",
            "-155"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4524",
            "-257",
            "-23"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8660",
            "-493",
            "-44"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4136",
            "-236",
            "-21"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "788",
            "-45",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3744",
            "-214",
            "-19"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "25644",
            "-1471",
            "-130"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "124476",
            "-7141",
            "-631"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "155468",
            "-8923",
            "-788"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "30992",
            "-1782",
            "-157"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "36920",
            "-2124",
            "-187"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "42848",
            "-2466",
            "-217"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "453036",
            "-26087",
            "-2294"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "410188",
            "-23621",
            "-2077"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "205588",
            "-11839",
            "-1041"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "988",
            "-57",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "12064",
            "-698",
            "-61"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11076",
            "-641",
            "-56"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "23952",
            "-1390",
            "-121"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1138620",
            "-66079",
            "-5752"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "189836",
            "-11017",
            "-959"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 3503,
      "side": -1,
      "supports": 31,
      "events": 16,
      "distinct": 16,
      "results": [
        {
          "kind": "open",
          "r": [
            "13358",
            "-942",
            "-63"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "10394",
            "-733",
            "-49"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6194",
            "-437",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "14382",
            "-1015",
            "-67"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "15246",
            "-1076",
            "-71"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "864",
            "-61",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6766",
            "-478",
            "-31"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5902",
            "-417",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6128",
            "-433",
            "-28"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6354",
            "-449",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8122",
            "-574",
            "-37"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1768",
            "-125",
            "-8"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3350",
            "-237",
            "-15"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "14982",
            "-1060",
            "-67"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6966",
            "-493",
            "-31"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5916",
            "-419",
            "-26"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4826",
            "-342",
            "-21"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8562",
            "-607",
            "-37"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1622",
            "-115",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1170",
            "-83",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "12192",
            "-865",
            "-52"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11022",
            "-782",
            "-47"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3816",
            "-271",
            "-16"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "23322",
            "-1657",
            "-97"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2912",
            "-207",
            "-12"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "46566",
            "-3311",
            "-191"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "29772",
            "-2117",
            "-122"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "12978",
            "-923",
            "-53"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "492",
            "-35",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7194",
            "-512",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2234",
            "-159",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1742",
            "-124",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3524",
            "-251",
            "-14"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 3539,
      "side": -1,
      "supports": 30,
      "events": 16,
      "distinct": 16,
      "results": [
        {
          "kind": "open",
          "r": [
            "3333",
            "-223",
            "-16"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5214",
            "-349",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "12903",
            "-868",
            "-61"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "20592",
            "-1387",
            "-97"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "53977",
            "-3637",
            "-254"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "33385",
            "-2250",
            "-157"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "638",
            "-43",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "429",
            "-29",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1518",
            "-103",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4125",
            "-280",
            "-19"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "18898",
            "-1283",
            "-87"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "33671",
            "-2286",
            "-155"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "869",
            "-59",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "220",
            "-15",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3091",
            "-211",
            "-14"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5962",
            "-407",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "12507",
            "-857",
            "-56"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6545",
            "-450",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "682",
            "-47",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "13233",
            "-913",
            "-58"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "13926",
            "-971",
            "-59"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "28545",
            "-2000",
            "-119"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "15367",
            "-1077",
            "-64"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2189",
            "-154",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3905",
            "-275",
            "-16"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1716",
            "-121",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "737",
            "-52",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "495",
            "-35",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "748",
            "-53",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "28677",
            "-2032",
            "-115"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "39435",
            "-2795",
            "-158"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "10758",
            "-763",
            "-43"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1254",
            "-89",
            "-5"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 3588,
      "side": 1,
      "supports": 28,
      "events": 16,
      "distinct": 16,
      "results": [
        {
          "kind": "open",
          "r": [
            "-12661",
            "1156",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-12650",
            "1155",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-45331",
            "4141",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-78012",
            "7127",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-276045",
            "25240",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-198033",
            "18113",
            "-22"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-466257",
            "42802",
            "-83"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-268224",
            "24689",
            "-61"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-47223",
            "4348",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-15114",
            "1399",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-3003",
            "278",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-2904",
            "269",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-296307",
            "27562",
            "-125"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-293403",
            "27293",
            "-124"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-25542",
            "2377",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-345147",
            "32132",
            "-151"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-347391",
            "32341",
            "-152"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-2244",
            "209",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-8811",
            "821",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-15378",
            "1433",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-21714",
            "2039",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-28050",
            "2645",
            "-19"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-15378",
            "1453",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-33462",
            "3167",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-66770",
            "6355",
            "-57"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-100078",
            "9543",
            "-89"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-5621",
            "536",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1100",
            "105",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-3157",
            "302",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-5214",
            "499",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-553311",
            "53111",
            "-562"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-548097",
            "52612",
            "-557"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-274516",
            "26351",
            "-279"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    }
  ],
  "totalPatterns": 406178,
  "excluded": [
    1716,
    3487,
    3503,
    3539,
    3588
  ],
  "strata": 234
}
```
