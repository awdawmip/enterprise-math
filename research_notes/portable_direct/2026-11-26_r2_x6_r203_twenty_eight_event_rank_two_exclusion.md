# X6 R203 — Twenty-eight-event rank-two exclusion replay

2026-11-26 Asia/Shanghai. AUTHOR EXACT FINITE NECESSARY-RELAXATION REPLAY / NOT_REVIEWED. Independent informed static BRC auxiliary weight research. Researcher identity unconfirmed; historical predecessor EM-DIRECT-AE5AD5. Native task lookup r2-20261126-0110-x6-read SUCCEEDED at 2026-11-25T17:10:59.945859Z, Source bcf3cc5f2338301fca81835ccaf7a549b76357cb, NO_CANONICAL_PUBLICATION_DIRECTORY (not a native owner projection). No CLAIM, shared state mutation or formal Result.

## Scope and proof

Reuse R202@2f0151260312a128a3a61fe2b5b489e1233689ca:research_notes/portable_direct/2026-11-26_r2_x6_r202_twenty_seven_event_rank_two_exclusion.md; R182@502d7abb2fe8470ed2cdabf242c2cc59a0c302ac:research_notes/portable_direct/2026-11-25_r2_x6_r182_one_child_event_refinement.md and census@6945e591116377f9386c7419b6ce31a2b9e8a146:research_notes/portable_direct/x6_r182_rank_two_side_census.json (blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82). Frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f: Port 10, 1,935 unoriented integer directions, four positive weights w=(17t,B,22t,D), six joint BRC pair denominators, strict 3/2 near-direction set. P000 V5 and joint relation observer preservation. Auxiliary coefficient chart, not native spatial geometry/dynamics; no new physical reference computation. R182: fixed-endpoint necessary relaxation constant within each labeled ternary determinant stratum of a child. For r=alpha*u+beta*v, alpha,beta>0, varying events occur at beta/alpha=|x dot u|/|x dot v|; distinct cuts split open intervals and singleton equality strata. Both children must pass; if one child fails throughout its class the whole class is excluded. Passing alone proves no actual tree. All representatives checked against original masks and support counts. Executed function matched pinned R202 ignoring whitespace; full min-28 tranche selected from frozen census. BigInt exact geometry, 31-bit support masks. No event identities dropped; only duplicate cuts merged.

## Actual executed result

```json
[
  {
    "id": 1508,
    "side": -1,
    "supports": 26,
    "events": 28,
    "distinct": 28,
    "strata": 57,
    "passing": 57
  },
  {
    "id": 1508,
    "side": 1,
    "supports": 31,
    "events": 52,
    "distinct": 52,
    "strata": 105,
    "passing": 0
  },
  {
    "id": 1945,
    "side": -1,
    "supports": 28,
    "events": 28,
    "distinct": 28,
    "strata": 57,
    "passing": 0
  },
  {
    "id": 2752,
    "side": 1,
    "supports": 28,
    "events": 28,
    "distinct": 28,
    "strata": 57,
    "passing": 0
  },
  {
    "id": 3246,
    "side": 1,
    "supports": 26,
    "events": 28,
    "distinct": 27,
    "strata": 55,
    "passing": 55
  },
  {
    "id": 3246,
    "side": -1,
    "supports": 29,
    "events": 45,
    "distinct": 42,
    "strata": 85,
    "passing": 0
  }
]
```

Total 416 strata; sum of distinct observation-pattern counts 804122; newly excluded [1508,1945,2752,3246]. Conditional on R202, remaining 162 = 74 rank two + 88 rank three. Bound 6<=D_linear<=7 unchanged. Next min-29 rows: [{"id":1474,"events":[[1,29],[-1,79]]}]. Activity association and independent review outstanding. No formal Task closure.

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
const rows=[{"i":1508,"a":"898455116447640","b":"1353344680460391","r":["397","1","-6"],"local":79,"vertices":[["69","0","-1"],["1122","3","-17"]],"sides":[{"side":1,"supports":31,"events":["1,1,68","1,1005,126","1,191,87","1,193,87","1,255,87","1,459,126","1,459,87","10,49,677","11,5,736","12,893,940","121,120,8226","147,55,9812","15,1802,1305","15,2491,1175","17,4839,1479","17,8739,2142","18,136,1241","18,85,1241","183,15245,14335","19,11,1276","19,28,1310","2,1666,395","2,4012,395","20,2979,1740","207,1036,13862","25,4611,2175","27,3995,2115","3,1,200","3,1013,235","3,221,235","3,235,235","3,493,261","3,501,235","3,515,235","3,599,235","3,629,235","3,701,235","34,31778,6715","45,4522,3525","464,2207,31879","472,2239,32471","5,1111,435","5,43,341","55,272,3706","57,4700,4465","59,425,3995","6,451,470","60,7429,4700","63,5,4168","69,65,4684","9,10,614","9,11,616"]},{"side":-1,"supports":26,"events":["1,147,87","1,225,87","1,264,87","1,5256,126","1,8103,87","101,901,6953","127,1103,8683","147,1073,10003","16,139,1094","16,3,1062","2,17,136","25,37,1724","27,2240,2115","3,233,235","3,26207,235","3,467,235","3,493,235","3,805,235","3,896,235","301,2669,20689","37,44,2530","4,35,274","5,7,344","651,49859,50995","69,341,4651","7,2,466","9,10,614","9,76,611"]}]},{"i":1945,"a":"863133305404952","b":"1388666508280039","r":["51","1","-1"],"local":61,"vertices":[["867","18","-17"],["408","7","-8"]],"sides":[{"side":1,"supports":27,"events":["1,37,87","1,39,87","1,82,126","11,187,731","125,2059,8471","137,2047,8795","1394,207778,275315","14,2326,2765","147,4007,11515","17,289,1157","190,30374,37525","2,295,395","2,307,395","2,327,395","201,5291,15745","201,6017,15745","21,551,1645","21,629,1645","226,35666,44635","28,109,1529","30,777,2350","36,1105,2820","36,5245,7110","4,15,219","44,6715,8690","6,856,1185","61,1031,4195","67,2439,5829","7,255,609","7,71,427","72,6125,9072","74,11242,14615","81,2261,6345","83,2958,7221"]},{"side":-1,"supports":28,"events":["1,17,66","105,1584,6776","108,3227,8460","11,421,957","13,194,834","13,482,1131","134,10065,16884","15,151,923","16,2367,3160","2,73,174","26,2095,3276","268,40007,52930","29,439,1875","3,90,235","36,937,2820","39,1069,3055","4,15,219","4,159,348","4,341,504","47,745,3117","52,8337,10270","54,1477,4230","54,203,2956","664,2591,36253","67,2322,5829","7,110,462","7,249,609","72,1913,5640"]}]},{"i":2752,"a":"1115201452560","b":"2250684612216303","r":["340","56","-15"],"local":63,"vertices":[["204","31","-9"],["1156","193","-51"]],"sides":[{"side":1,"supports":28,"events":["1,28,128","10,181,859","114,5279,22515","1204,59715,237790","13,45,462","138,6715,27255","142,6977,28045","15,199,1035","167,3073,14529","169,3071,14703","1954,97373,385915","2,5,64","2,99,395","206,10327,40685","3,38,207","3,40,207","3,52,260","3,53,259","3,53,261","394,18931,77815","42,1975,8295","42,2077,8295","5,87,435","7,71,427","81,2392,10244","82,4033,16195","92,4575,18170","93,2828,12136"]},{"side":-1,"supports":30,"events":["1,18,87","1,29,127","107,3290,14362","109,3361,14735","11,336,1452","12,355,1517","13,225,1131","14,108,711","149,4563,19797","18,187,1067","19,237,1311","19,327,1649","2,15,102","2,16,101","202,9843,39895","27,823,3545","28,845,3583","3,53,259","302,2326,15341","32,945,4047","34,85,1085","35,1037,4423","369,1307,13084","38,293,1930","38,295,1928","38,303,1920","39,134,1387","395,5037,27255","49,1390,6254","5,143,637","67,1917,8535","67,2023,8585","7,72,420","76,2295,9741","82,3822,16195","9,31,320"]}]},{"i":3246,"a":"18708374748696","b":"2233091438412263","r":["1727","24","-35"],"local":72,"vertices":[["44","1","-1"],["1683","23","-34"]],"sides":[{"side":1,"supports":26,"events":["1,53,87","1,92,126","11,1071,1386","113,10540,14238","122,25655,24095","14,1369,1764","14,2326,2765","18,965,1566","190,17933,23940","190,30374,37525","196,1075,10391","2,327,395","2,371,395","2,395,395","2,99,174","22,965,1914","226,35666,44635","3,283,378","37,3333,4662","38,7900,7505","66,2505,5170","697,61704,87822","72,3863,6264","72,6125,9072","8,1501,1580","8,45,423","84,3287,6580","9,775,1134"]},{"side":-1,"supports":29,"events":["1,108,126","10,63,522","10,66,519","103,1122,5742","113,1372,6516","12,503,940","128,833,6655","129,6145,11223","14,1551,1764","14,2344,2765","159,6733,12455","16,179,887","16,89,847","166,1053,8658","166,909,8802","176,1029,9267","18,683,1410","18,98,955","21,773,1645","216,1319,11317","237,2772,13420","24,167,1237","26,185,1336","260,1581,13629","28,165,1473","3,111,235","300,3339,16591","32,175,1697","332,1913,17509","37,1617,3219","4,185,348","4,27,207","4,341,504","5,238,435","5,58,282","52,8337,10270","6,219,470","6,34,317","7,600,882","7,76,392","7,80,392","8,1397,1580","8,45,423","9,361,705","94,558,4941"]}]}];
console.log(JSON.stringify(replay(data,rows),null,2));
```

## Full actual output

```json
{
  "output": [
    {
      "i": 1508,
      "side": -1,
      "supports": 26,
      "events": 28,
      "distinct": 28,
      "results": [
        {
          "kind": "open",
          "r": [
            "451141",
            "7",
            "-6540"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "451072",
            "7",
            "-6539"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "364943",
            "8",
            "-5291"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "278814",
            "9",
            "-4043"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "305569",
            "10",
            "-4431"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "26755",
            "1",
            "-388"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "387277",
            "58",
            "-5627"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "360522",
            "57",
            "-5239"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "365887",
            "58",
            "-5317"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "5365",
            "1",
            "-78"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "8867",
            "2",
            "-129"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "3502",
            "1",
            "-51"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "2329",
            "1",
            "-34"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "10472",
            "5",
            "-153"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "68301",
            "33",
            "-998"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "57829",
            "28",
            "-845"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "41802",
            "21",
            "-611"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "25775",
            "14",
            "-377"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "1777",
            "1",
            "-26"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "39974",
            "23",
            "-585"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "24861",
            "15",
            "-364"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "9748",
            "7",
            "-143"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "11991",
            "9",
            "-176"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "2243",
            "2",
            "-33"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "8627",
            "8",
            "-127"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "15011",
            "14",
            "-221"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "22068",
            "21",
            "-325"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "7057",
            "7",
            "-104"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "23794",
            "25",
            "-351"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "16737",
            "18",
            "-247"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "6436",
            "7",
            "-95"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "9007",
            "10",
            "-133"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "13476",
            "15",
            "-199"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "4469",
            "5",
            "-66"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "5746",
            "7",
            "-85"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "7023",
            "9",
            "-104"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "55030",
            "79",
            "-817"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "48007",
            "70",
            "-713"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "24573",
            "36",
            "-365"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "1139",
            "2",
            "-17"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "3141",
            "6",
            "-47"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "5143",
            "10",
            "-77"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "32912",
            "65",
            "-493"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "27769",
            "55",
            "-416"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "32101",
            "64",
            "-481"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "4332",
            "9",
            "-65"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "122937",
            "261",
            "-1846"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "118605",
            "252",
            "-1781"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "126389",
            "269",
            "-1898"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "7784",
            "17",
            "-117"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "8647",
            "19",
            "-130"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "863",
            "2",
            "-13"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "9355",
            "22",
            "-141"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "17847",
            "42",
            "-269"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "661186",
            "1561",
            "-9967"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "643339",
            "1519",
            "-9698"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "644461",
            "1522",
            "-9715"
          ],
          "feasible": true
        }
      ],
      "excluded": false
    },
    {
      "i": 1508,
      "side": 1,
      "supports": 31,
      "events": 52,
      "distinct": 52,
      "results": [
        {
          "kind": "open",
          "r": [
            "20407",
            "1",
            "-296"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "20338",
            "1",
            "-295"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "17785",
            "1",
            "-258"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "15232",
            "1",
            "-221"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "26945",
            "2",
            "-391"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11713",
            "1",
            "-170"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "409229",
            "98",
            "-5955"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "397516",
            "97",
            "-5785"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3364",
            "1",
            "-49"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "389660",
            "137",
            "-5681"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "422611",
            "151",
            "-6162"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "32951",
            "14",
            "-481"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "42664",
            "19",
            "-623"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "9713",
            "5",
            "-142"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "24809",
            "14",
            "-363"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "15096",
            "9",
            "-221"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "37283",
            "23",
            "-546"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "22187",
            "14",
            "-325"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "20945",
            "14",
            "-307"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "19703",
            "14",
            "-289"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9817",
            "7",
            "-144"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "9748",
            "7",
            "-143"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1363",
            "1",
            "-20"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "9334",
            "7",
            "-137"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "12871",
            "10",
            "-189"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3537",
            "3",
            "-52"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5711",
            "5",
            "-84"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7885",
            "7",
            "-116"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "23172",
            "21",
            "-341"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "15287",
            "14",
            "-225"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "16374",
            "15",
            "-241"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1087",
            "1",
            "-16"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "39063",
            "36",
            "-575"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "37976",
            "35",
            "-559"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "84769",
            "79",
            "-1248"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "131562",
            "123",
            "-1937"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "80335",
            "76",
            "-1183"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "270113",
            "257",
            "-3978"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "424487",
            "410",
            "-6253"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "154374",
            "153",
            "-2275"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "229517",
            "230",
            "-3383"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "75143",
            "77",
            "-1108"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "33767",
            "35",
            "-498"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "59925",
            "63",
            "-884"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "67983",
            "72",
            "-1003"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8058",
            "9",
            "-119"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "440759",
            "569",
            "-6528"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "432701",
            "560",
            "-6409"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "436549",
            "565",
            "-6466"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3848",
            "5",
            "-57"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5263",
            "7",
            "-78"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1415",
            "2",
            "-21"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7334",
            "11",
            "-109"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5919",
            "9",
            "-88"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2623",
            "4",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1950",
            "3",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5039",
            "8",
            "-75"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8128",
            "13",
            "-121"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "74360",
            "119",
            "-1107"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "140592",
            "225",
            "-2093"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "26179",
            "43",
            "-390"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "252093",
            "420",
            "-3757"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "21002",
            "35",
            "-313"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "20933",
            "35",
            "-312"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "293755",
            "502",
            "-4381"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "566577",
            "969",
            "-8450"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "581367",
            "996",
            "-8671"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "14790",
            "27",
            "-221"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "26957",
            "50",
            "-403"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "12167",
            "23",
            "-182"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2606",
            "5",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "29529",
            "57",
            "-442"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "48824",
            "95",
            "-731"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "19295",
            "38",
            "-289"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "63529",
            "127",
            "-952"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "44234",
            "89",
            "-663"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "207243",
            "420",
            "-3107"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "163009",
            "331",
            "-2444"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "338980",
            "691",
            "-5083"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "175971",
            "360",
            "-2639"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "179302",
            "367",
            "-2689"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3331",
            "7",
            "-50"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1040929",
            "2188",
            "-15625"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2078527",
            "4369",
            "-31200"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2482632",
            "5223",
            "-37267"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "404105",
            "854",
            "-6067"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "14653",
            "31",
            "-220"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "35485",
            "76",
            "-533"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "38540",
            "83",
            "-579"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3055",
            "7",
            "-46"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "55647",
            "132",
            "-839"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "108239",
            "257",
            "-1632"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "131368",
            "313",
            "-1981"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "23129",
            "56",
            "-349"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "11461",
            "28",
            "-173"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "45637",
            "112",
            "-689"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2848",
            "7",
            "-43"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5627",
            "14",
            "-85"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "76138",
            "193",
            "-1151"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "70511",
            "179",
            "-1066"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "78227",
            "200",
            "-1183"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "164170",
            "421",
            "-2483"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "266323",
            "691",
            "-4030"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "102153",
            "270",
            "-1547"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "103275",
            "273",
            "-1564"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 1945,
      "side": -1,
      "supports": 28,
      "events": 28,
      "distinct": 28,
      "results": [
        {
          "kind": "open",
          "r": [
            "8109",
            "167",
            "-159"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "47787",
            "984",
            "-937"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "27744",
            "571",
            "-544"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7701",
            "158",
            "-151"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3570",
            "73",
            "-70"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6579",
            "134",
            "-129"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "52071",
            "1051",
            "-1021"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "97563",
            "1968",
            "-1913"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "25449",
            "513",
            "-499"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4233",
            "84",
            "-83"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4284",
            "85",
            "-84"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "51",
            "1",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "75378",
            "1477",
            "-1478"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "75327",
            "1476",
            "-1477"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "54774",
            "1073",
            "-1074"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "34221",
            "670",
            "-671"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "22185",
            "434",
            "-435"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "54519",
            "1066",
            "-1069"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "16218",
            "317",
            "-318"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "10353",
            "202",
            "-203"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "65535",
            "1273",
            "-1285"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "120717",
            "2344",
            "-2367"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "15555",
            "302",
            "-305"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3723",
            "72",
            "-73"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1022040",
            "19667",
            "-20040"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2040357",
            "39262",
            "-40007"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "256581",
            "4937",
            "-5031"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "12291",
            "234",
            "-241"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3315",
            "63",
            "-65"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7599",
            "144",
            "-149"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2907",
            "55",
            "-57"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1122",
            "21",
            "-22"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "22593",
            "417",
            "-443"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "21471",
            "396",
            "-421"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7140",
            "131",
            "-140"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "21369",
            "390",
            "-419"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "21930",
            "397",
            "-430"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "132141",
            "2389",
            "-2591"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "296718",
            "5341",
            "-5818"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "164577",
            "2952",
            "-3227"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "42126",
            "755",
            "-826"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "425187",
            "7618",
            "-8337"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "142494",
            "2553",
            "-2794"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2295",
            "41",
            "-45"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4998",
            "89",
            "-98"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2703",
            "48",
            "-53"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2091",
            "37",
            "-41"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "22389",
            "396",
            "-439"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "103173",
            "1817",
            "-2023"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "80784",
            "1421",
            "-1584"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "81651",
            "1436",
            "-1601"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "867",
            "15",
            "-17"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "10761",
            "186",
            "-211"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "9894",
            "171",
            "-194"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "27285",
            "471",
            "-535"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "17391",
            "300",
            "-341"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "17799",
            "307",
            "-349"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 2752,
      "side": 1,
      "supports": 28,
      "events": 28,
      "distinct": 28,
      "results": [
        {
          "kind": "open",
          "r": [
            "2924",
            "448",
            "-129"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2720",
            "417",
            "-120"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "704956",
            "108464",
            "-31101"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "702236",
            "108047",
            "-30981"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "357884",
            "55066",
            "-15789"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "13532",
            "2085",
            "-597"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "12920",
            "1991",
            "-570"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "12308",
            "1897",
            "-543"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "110636",
            "17064",
            "-4881"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "208964",
            "32231",
            "-9219"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1138388",
            "176184",
            "-50223"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6621364",
            "1024873",
            "-292119"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3320848",
            "514013",
            "-146508"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "20332",
            "3153",
            "-897"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "331432",
            "51407",
            "-14622"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "311100",
            "48254",
            "-13725"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "728620",
            "113292",
            "-32145"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4060620",
            "631498",
            "-179145"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "451928",
            "70283",
            "-19938"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6732",
            "1049",
            "-297"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "73984",
            "11539",
            "-3264"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "141236",
            "22029",
            "-6231"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "175032",
            "27323",
            "-7722"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "208828",
            "32617",
            "-9213"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "128452",
            "20069",
            "-5667"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "48076",
            "7521",
            "-2121"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "32232",
            "5053",
            "-1422"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "274244",
            "43009",
            "-12099"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "374340",
            "58744",
            "-16515"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "474436",
            "74479",
            "-20931"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "33252",
            "5245",
            "-1467"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "456620",
            "72381",
            "-20145"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "25568",
            "4053",
            "-1128"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3604",
            "573",
            "-159"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "645456",
            "103613",
            "-28476"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1287308",
            "206653",
            "-56793"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "161364",
            "25904",
            "-7119"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3604",
            "579",
            "-159"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6188",
            "996",
            "-273"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2584",
            "417",
            "-114"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "68",
            "11",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "884",
            "144",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6800",
            "1109",
            "-300"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5916",
            "965",
            "-261"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "70108",
            "11497",
            "-3093"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "134300",
            "22029",
            "-5925"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "137360",
            "22531",
            "-6060"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3060",
            "502",
            "-135"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1700",
            "279",
            "-75"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "340",
            "56",
            "-15"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "272",
            "45",
            "-12"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "476",
            "79",
            "-21"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "179724",
            "29936",
            "-7929"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "358972",
            "59793",
            "-15837"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "181900",
            "30299",
            "-8025"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4828",
            "805",
            "-213"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2992",
            "499",
            "-132"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 3246,
      "side": 1,
      "supports": 26,
      "events": 28,
      "distinct": 27,
      "results": [
        {
          "kind": "open",
          "r": [
            "36373",
            "792",
            "-817"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "36329",
            "791",
            "-816"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "62656",
            "1363",
            "-1407"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "26327",
            "572",
            "-591"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "57478",
            "1237",
            "-1287"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "31151",
            "665",
            "-696"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "48028",
            "1025",
            "-1073"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "16877",
            "360",
            "-377"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "1662",
            "35",
            "-37"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "27997",
            "585",
            "-622"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "13743",
            "286",
            "-305"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "13232",
            "273",
            "-293"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "44859",
            "910",
            "-989"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "31627",
            "637",
            "-696"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "66565",
            "1334",
            "-1463"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "34938",
            "697",
            "-767"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "14827",
            "294",
            "-325"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "9543",
            "185",
            "-208"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "10237",
            "198",
            "-223"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "694",
            "13",
            "-15"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "15766",
            "289",
            "-339"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "30838",
            "565",
            "-663"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "8335",
            "152",
            "-179"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "10837",
            "195",
            "-232"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "63678",
            "1145",
            "-1363"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "52841",
            "950",
            "-1131"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "19626",
            "349",
            "-419"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "64915",
            "1144",
            "-1383"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "80831",
            "1417",
            "-1720"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "15916",
            "273",
            "-337"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "19129",
            "328",
            "-405"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "3213",
            "55",
            "-68"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "1466",
            "25",
            "-31"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "4117",
            "70",
            "-87"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "2177",
            "37",
            "-46"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "237",
            "4",
            "-5"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "1764",
            "29",
            "-37"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "6819",
            "112",
            "-143"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "3457",
            "55",
            "-72"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "17380",
            "273",
            "-361"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "18257",
            "286",
            "-379"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "877",
            "13",
            "-18"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "4981",
            "73",
            "-102"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "9085",
            "133",
            "-186"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "9427",
            "138",
            "-193"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "342",
            "5",
            "-7"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "32585",
            "473",
            "-666"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "32243",
            "468",
            "-659"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "21089",
            "306",
            "-431"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "9935",
            "144",
            "-203"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "388425",
            "5599",
            "-7928"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "1155340",
            "16653",
            "-23581"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "633206",
            "9109",
            "-12919"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "111072",
            "1565",
            "-2257"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "112755",
            "1588",
            "-2291"
          ],
          "feasible": true
        }
      ],
      "excluded": false
    },
    {
      "i": 3246,
      "side": -1,
      "supports": 29,
      "events": 45,
      "distinct": 42,
      "results": [
        {
          "kind": "open",
          "r": [
            "1733",
            "38",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1689",
            "37",
            "-38"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "13116",
            "287",
            "-295"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11427",
            "250",
            "-257"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "89795",
            "1959",
            "-2018"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "78368",
            "1709",
            "-1761"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "41264",
            "899",
            "-927"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4160",
            "89",
            "-93"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5101",
            "109",
            "-114"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "941",
            "20",
            "-21"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "167454",
            "3559",
            "-3737"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "333967",
            "7098",
            "-7453"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "47947",
            "1019",
            "-1070"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1662",
            "35",
            "-37"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6252",
            "131",
            "-139"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "10842",
            "227",
            "-241"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "13303",
            "276",
            "-295"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2461",
            "49",
            "-54"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4333",
            "86",
            "-95"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1872",
            "37",
            "-41"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "457",
            "9",
            "-10"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1784",
            "35",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2197",
            "43",
            "-48"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "413",
            "8",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "782",
            "15",
            "-17"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "369",
            "7",
            "-8"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1063",
            "20",
            "-23"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "694",
            "13",
            "-15"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5183",
            "97",
            "-112"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4489",
            "84",
            "-97"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "33661",
            "625",
            "-726"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "29172",
            "541",
            "-629"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "45747",
            "847",
            "-986"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "62322",
            "1153",
            "-1343"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "31789",
            "588",
            "-685"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1256",
            "23",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "931",
            "17",
            "-20"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7123",
            "130",
            "-153"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "14202",
            "259",
            "-305"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7079",
            "129",
            "-152"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "90032",
            "1597",
            "-1921"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "82953",
            "1468",
            "-1769"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "42157",
            "746",
            "-899"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1361",
            "24",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "60409",
            "1061",
            "-1286"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "59048",
            "1037",
            "-1257"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "64079",
            "1125",
            "-1364"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5031",
            "88",
            "-107"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2353",
            "41",
            "-50"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2028",
            "35",
            "-43"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5319",
            "89",
            "-112"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8610",
            "143",
            "-181"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "71931",
            "1187",
            "-1510"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "135252",
            "2231",
            "-2839"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "46365",
            "764",
            "-973"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3843",
            "61",
            "-80"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "18819",
            "296",
            "-391"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "14976",
            "235",
            "-311"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2167",
            "34",
            "-45"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "193",
            "3",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7483",
            "116",
            "-155"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7290",
            "113",
            "-151"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3535",
            "54",
            "-73"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "13920",
            "211",
            "-287"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3447",
            "52",
            "-71"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3315",
            "49",
            "-68"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1219",
            "18",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "342",
            "5",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "833",
            "12",
            "-17"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2990",
            "43",
            "-61"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4121",
            "59",
            "-84"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1131",
            "16",
            "-23"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3051",
            "43",
            "-62"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4971",
            "70",
            "-101"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "49578",
            "697",
            "-1007"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "94185",
            "1324",
            "-1913"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "100243",
            "1409",
            "-2036"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6058",
            "85",
            "-123"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6847",
            "96",
            "-139"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "789",
            "11",
            "-16"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "27869",
            "388",
            "-565"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "27080",
            "377",
            "-549"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "34733",
            "483",
            "-704"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7653",
            "106",
            "-155"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3112",
            "43",
            "-63"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    }
  ],
  "totalPatterns": 804122,
  "excluded": [
    1508,
    1945,
    2752,
    3246
  ],
  "strata": 416
}
```
