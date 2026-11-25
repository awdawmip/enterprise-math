# X6 R197 — Twenty-two-event rank-two exclusion replay

2026-11-25. AUTHOR EXACT FINITE NECESSARY-RELAXATION REPLAY / NOT_REVIEWED. Independent informed static BRC auxiliary weight research. Historical predecessor EM-DIRECT-AE5AD5; live execution binding unconfirmed. Request r2-20261125-1908-x6-read SUCCEEDED, observed 2026-11-25T11:08:51.776491Z, Source 2d4c2259b39e7d9a6975d4754add02ae63fe786a, NO_CANONICAL_PUBLICATION_DIRECTORY; execution_authorized=false, native_operational_view_evaluated=false. No CLAIM, owner mutation, formal result or review.

## Frozen scope and method

R196@8059794887d4c419c719f3630d66079b380ee499, blob ad012230ea7ffdc28081d86e6b2f2e14af17dbd9; R182 side census@6945e591116377f9386c7419b6ce31a2b9e8a146, blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82; R182 one-child theorem@502d7abb2fe8470ed2cdabf242c2cc59a0c302ac. Retain R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f: Port 10, 1935 unoriented integer directions, six BRC denominators, w=(17t,B,22t,D), exact optimum and strict 3/2 near set. P000 V5, ACTIVE worldview, joint-relation preservation. Auxiliary coefficient chart only, no native dynamics or new scoring. R182 proves the fixed-endpoint depth-five necessary capacity relaxation constant on each child's event strata. The exact replay retains equality points, open intervals, endpoint incidence and root signs, clips actual components before compressing to extreme endpoints per support, coalesces equal event rays without erasing relation labels. Uniform failure in a child excludes the whole class; passing is only necessary feasibility, not an actual tree witness. Executed replay function matches pinned R196 source modulo whitespace; input is the complete min-22 census tranche. BigInt geometry and exact finite support masks.

## Executed result

```json
[
  {
    "id": 1714,
    "side": -1,
    "supports": 26,
    "events": 22,
    "distinct": 22,
    "strata": 45,
    "passing": 45
  },
  {
    "id": 1714,
    "side": 1,
    "supports": 29,
    "events": 49,
    "distinct": 49,
    "strata": 99,
    "passing": 0
  }
]
```

Total 144 strata; sum of distinct pattern counts 242170; newly excluded [1714]. Conditional on inherited R196: remaining 176 = 88 rank two + 88 rank three. Global 6<=D_linear<=7 unchanged. Nonexcluded rows remain unresolved. Next min-23 census rows: [{"id":893,"events":[[1,23],[-1,81]]},{"id":1213,"events":[[1,23],[-1,74]]},{"id":2967,"events":[[1,49],[-1,23]]},{"id":3117,"events":[[1,39],[-1,23]]}]. Activity association and independent review not claimed.

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
const rows=[{"i":1714,"a":"898317694271256","b":"1353482119413863","r":["646","7","-11"],"local":70,"vertices":[["1003","10","-17"],["289","4","-5"]],"sides":[{"side":1,"supports":29,"events":["1,37,87","1,39,87","1,43,87","1,92,126","11,1071,1386","113,10540,14238","122,25655,24095","13,482,1131","14,1369,1764","147,4007,11515","15,481,1175","190,17933,23940","199,3273,13731","2,371,395","2,395,395","201,5291,15745","201,6017,15745","21,551,1645","21,629,1645","21,656,1645","22,965,1914","23,2601,2898","24,771,1880","249,7990,19505","27,697,2115","28,1191,2436","3,283,378","30,777,2350","36,1105,2820","362,5897,24978","37,3333,4662","38,7900,7505","39,1069,3055","41,603,2829","46,10064,9085","5,78,345","605,9189,41745","697,61704,87822","7,288,609","7,600,882","79,1335,5451","8,123,552","8,1501,1580","81,2261,6345","86,1303,5934","88,1325,6072","9,133,621","9,775,1134","97,1529,6693"]},{"side":-1,"supports":26,"events":["1,108,126","1,16,69","108,3227,8460","11,169,759","11,421,957","14,1551,1764","1407,44069,110215","2,31,138","265,11109,23055","3,90,235","36,937,2820","37,1617,3219","4,159,348","4,185,348","43,412,2792","5,48,324","54,1477,4230","7,115,483","7,288,609","72,1913,5640","795,25709,62275","89,3723,7743"]}]}];
console.log(JSON.stringify(replay(data,rows),null,2));
```

## Complete actual output

```json
{
  "output": [
    {
      "i": 1714,
      "side": -1,
      "supports": 26,
      "events": 22,
      "distinct": 22,
      "results": [
        {
          "kind": "open",
          "r": [
            "156706",
            "1595",
            "-2659"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "312409",
            "3180",
            "-5301"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "286229",
            "2927",
            "-4858"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "260049",
            "2674",
            "-4415"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "144364",
            "1485",
            "-2451"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "28679",
            "296",
            "-487"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "17663",
            "183",
            "-300"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "6647",
            "70",
            "-113"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "24701",
            "261",
            "-420"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "18054",
            "191",
            "-307"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "20757",
            "220",
            "-353"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "44217",
            "469",
            "-752"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "47685",
            "506",
            "-811"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "3468",
            "37",
            "-59"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "5287",
            "57",
            "-90"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "1819",
            "20",
            "-31"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "125647",
            "1389",
            "-2142"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "123828",
            "1369",
            "-2111"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "136663",
            "1513",
            "-2330"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "12835",
            "144",
            "-219"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "3281",
            "37",
            "-56"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "459629",
            "5184",
            "-7845"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "465545",
            "5251",
            "-7946"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "5916",
            "67",
            "-101"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "9367",
            "107",
            "-160"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "3451",
            "40",
            "-59"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "169235",
            "1969",
            "-2894"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "842724",
            "9805",
            "-14411"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "375003",
            "4366",
            "-6413"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "282285",
            "3293",
            "-4828"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "10115",
            "118",
            "-173"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "935",
            "11",
            "-16"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "44438",
            "529",
            "-761"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "43503",
            "518",
            "-745"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "33660",
            "407",
            "-577"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "23817",
            "296",
            "-409"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "114053",
            "1444",
            "-1961"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "204289",
            "2592",
            "-3513"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "235518",
            "2999",
            "-4051"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "31229",
            "407",
            "-538"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "293080",
            "3863",
            "-5053"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "261851",
            "3456",
            "-4515"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "64855",
            "864",
            "-1119"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "127279",
            "1728",
            "-2199"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "31892",
            "433",
            "-551"
          ],
          "feasible": true
        }
      ],
      "excluded": false
    },
    {
      "i": 1714,
      "side": 1,
      "supports": 29,
      "events": 49,
      "distinct": 49,
      "results": [
        {
          "kind": "open",
          "r": [
            "25772",
            "259",
            "-437"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "437121",
            "4393",
            "-7412"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "515610",
            "5183",
            "-8743"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "78489",
            "790",
            "-1331"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "95353",
            "971",
            "-1618"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "112217",
            "1152",
            "-1905"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "124933",
            "1284",
            "-2121"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "387515",
            "3984",
            "-6579"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "196673",
            "2022",
            "-3339"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5831",
            "60",
            "-99"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "100487",
            "1055",
            "-1708"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "94656",
            "995",
            "-1609"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "105179",
            "1107",
            "-1788"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "10523",
            "112",
            "-179"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "172159",
            "1838",
            "-2929"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "678113",
            "7240",
            "-11537"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2405636",
            "25893",
            "-40947"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1727523",
            "18653",
            "-29410"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1886218",
            "20381",
            "-32113"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "158695",
            "1728",
            "-2703"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "76653",
            "839",
            "-1306"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "147917",
            "1628",
            "-2521"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "76449",
            "842",
            "-1303"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4981",
            "56",
            "-85"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "36975",
            "416",
            "-631"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "142919",
            "1608",
            "-2439"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "114495",
            "1289",
            "-1954"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "86071",
            "970",
            "-1469"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4473941",
            "50441",
            "-76360"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4387870",
            "49471",
            "-74891"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4391151",
            "49508",
            "-74947"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3281",
            "37",
            "-56"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "676498",
            "7723",
            "-11555"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1349715",
            "15409",
            "-23054"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "510340",
            "5827",
            "-8717"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "181305",
            "2072",
            "-3097"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "31671",
            "362",
            "-541"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8721",
            "100",
            "-149"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "11169",
            "130",
            "-191"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "13617",
            "160",
            "-233"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "119816",
            "1417",
            "-2051"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "226015",
            "2674",
            "-3869"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "80546",
            "955",
            "-1379"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "176715",
            "2101",
            "-3026"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "73406",
            "873",
            "-1257"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "43503",
            "518",
            "-745"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "273921",
            "3284",
            "-4693"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "504339",
            "6050",
            "-8641"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "46223",
            "555",
            "-792"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "142783",
            "1720",
            "-2447"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "209933",
            "2531",
            "-3598"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "67150",
            "811",
            "-1151"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "70567",
            "857",
            "-1210"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "144551",
            "1760",
            "-2479"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1545521",
            "19025",
            "-26524"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2946491",
            "36290",
            "-50569"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2992986",
            "36863",
            "-51367"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "46495",
            "573",
            "-798"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "203966",
            "2517",
            "-3501"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "157471",
            "1944",
            "-2703"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1886405",
            "23527",
            "-32402"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1728934",
            "21583",
            "-29699"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1736091",
            "21673",
            "-29822"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7157",
            "90",
            "-123"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "16405",
            "207",
            "-282"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "9248",
            "117",
            "-159"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1105",
            "14",
            "-19"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "16167",
            "205",
            "-278"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "31229",
            "396",
            "-537"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "15062",
            "191",
            "-259"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "17969",
            "228",
            "-309"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2907",
            "37",
            "-50"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "11220",
            "143",
            "-193"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "30753",
            "392",
            "-529"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7905",
            "101",
            "-136"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "253827",
            "3244",
            "-4367"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "316489",
            "4055",
            "-5446"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "62662",
            "811",
            "-1079"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "606679",
            "7878",
            "-10449"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "544017",
            "7067",
            "-9370"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "10589691",
            "140194",
            "-182633"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "10045674",
            "133127",
            "-173263"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "10075747",
            "133529",
            "-173782"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "30073",
            "402",
            "-519"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "31637",
            "423",
            "-546"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1564",
            "21",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "72471",
            "983",
            "-1252"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "70907",
            "962",
            "-1225"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "73627",
            "999",
            "-1272"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2720",
            "37",
            "-47"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "108069",
            "1477",
            "-1868"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "105349",
            "1440",
            "-1821"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "230996",
            "3159",
            "-3993"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "125647",
            "1719",
            "-2172"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "65773",
            "900",
            "-1137"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5899",
            "81",
            "-102"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "103105",
            "1418",
            "-1783"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "97206",
            "1337",
            "-1681"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "97495",
            "1341",
            "-1686"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    }
  ],
  "totalPatterns": 242170,
  "excluded": [
    1714
  ],
  "strata": 144
}
```
