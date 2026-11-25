# X6 R193 — Eighteen-event rank-two exclusion replay

2026-11-25. Independent informed static auxiliary weight BRC research. Author exact finite necessary-relaxation replay, NOT_REVIEWED. Historical predecessor EM-DIRECT-AE5AD5; current live research identity binding unconfirmed. Current X6 lookup r2-20261125-r193-read SUCCEEDED at 2026-11-25T07:06:30.837081Z, Source 8951962a0ccdd09b9a8f8d83aea518149140443e, NO_CANONICAL_PUBLICATION_DIRECTORY; native_operational_view_evaluated=false, execution_authorized=false. No CLAIM or shared-state mutation.

## Inputs and scope

R192@0fbfd7b353d3efa8fbdab8982ab2d28088eb82bf, blob d66d5363f564eb4740295e917739e65be96be9ce; R182 census@6945e591116377f9386c7419b6ce31a2b9e8a146, blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82; R182 theorem@502d7abb2fe8470ed2cdabf242c2cc59a0c302ac. Preserve frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd, R122@1e4ab68c4f9c91bc60c07017acc57be20829832f, Port 10, 1935 unoriented integer directions, six BRC pair denominators, weights (17t,B,22t,D), exact optimizer and strict 3/2 near set. P000 V5, ACTIVE worldview, joint relation observer preservation retained. Auxiliary coefficient chart, not native spatial geometry/time dynamics. No re-scoring.

Use R182 one-child sufficiency for the fixed-endpoint depth-five necessary capacity relaxation, and the R192 recurrence transcribed below. Exact event rays coalesced, all open intervals and event points retained, root masks and support counts checked. Clip actual disconnected components before retaining outer endpoints. An entirely failing child excludes the class; if both children have passing strata their exact intersection is still required. A passing relaxation is not a six-query tree witness.

## Executed result

```json
[
  {
    "id": 1337,
    "side": -1,
    "supports": 31,
    "events": 18,
    "distinct": 18,
    "strata": 37,
    "passing": 0
  },
  {
    "id": 3501,
    "side": -1,
    "supports": 31,
    "events": 18,
    "distinct": 18,
    "strata": 37,
    "passing": 0
  }
]
```

Total strata 74, sum of distinct sign-pattern counts 138508; excluded IDs 1337, 3501. Conditional on inherited R192 bank: remaining 193 = 105 rank two + 88 rank three. Global 6<=D_linear<=7 unchanged. Next min-19 census rows: [{"id":1283,"events":[[1,19],[-1,42]]},{"id":1475,"events":[[1,19],[-1,19]]},{"id":1485,"events":[[1,19],[-1,36]]},{"id":1666,"events":[[1,19],[-1,19]]},{"id":1921,"events":[[1,19],[-1,39]]},{"id":3035,"events":[[1,39],[-1,19]]},{"id":3700,"events":[[1,28],[-1,19]]}]. Any unexcluded min-18 rows must be retained for exact intersection. No independent review or Activity association yet.

## Standalone reproduction

The following self-contained JavaScript was executed with exact census inputs, BigInt geometry and the inherited <=31-support bitmask recurrence.

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
const rows=[{"i":1337,"a":"901191279181784","b":"1350608534503431","r":["2437","-131","-17"],"local":40,"vertices":[["1177","-65","-8"],["3697","-197","-26"]],"sides":[{"side":1,"supports":29,"events":["1,1,137","1,6,98","10,183,25","12,221,30","14,251,35","152,2727,380","158,2907,395","160,2941,400","2,31,47","21,356,280","21,358,266","22,395,55","23,402,207","231,3842,2926","246,4403,615","3,51,38","3,51,40","30,527,253","30,536,75","33,544,440","46,821,115","46,836,115","6,76,275","7,123,63","77,1343,693","83,488,8144"]},{"side":-1,"supports":31,"events":["1,1,137","10,179,25","1138,20723,2845","124,2279,310","15,263,127","1786,32171,4465","2,31,47","203,3555,1827","27,446,360","3,51,38","3,51,40","32,583,80","38,685,95","568,10319,1420","7,80,388","8,123,189","82,1472,205","862,15707,2155"]}]},{"i":3501,"a":"1049625315377144","b":"1202174494113799","r":["1472","-102","-7"],"local":47,"vertices":[["2964","-209","-14"],["1452","-97","-7"]],"sides":[{"side":1,"supports":28,"events":["115,1431,3054","115,1548,1442","14,199,35","18,187,1067","186,2493,2480","2,5,346","21,285,266","224,3249,560","23,183,2209","248,3519,620","26,259,1794","26,367,65","262,3778,655","27,212,2596","278,3910,695","3,38,79","3,40,40","358,5180,895","368,5171,920","420,5639,5320","50,567,2358","58,567,4002","62,701,2926","7,72,420","7,76,392","79,756,5451","842,12040,2105","87,1172,1102","93,1251,1178"]},{"side":-1,"supports":31,"events":["1,8,96","103,1122,5742","12,157,311","15,151,923","151,1606,8690","16,181,755","16,233,40","172,1989,8073","18,241,227","19,263,231","32,363,1509","4,45,189","48,643,608","48,647,640","54,749,684","54,751,720","56,621,2655","7,71,427"]}]}];
console.log(JSON.stringify(replay(data,rows),null,2));
```

## Actual output

```json
{
  "output": [
    {
      "i": 1337,
      "side": -1,
      "supports": 31,
      "events": 18,
      "distinct": 18,
      "results": [
        {
          "kind": "open",
          "r": [
            "5429",
            "-299",
            "-37"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4252",
            "-234",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "17273",
            "-949",
            "-118"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "13021",
            "-715",
            "-89"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "120104",
            "-6578",
            "-823"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "107083",
            "-5863",
            "-734"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2447552",
            "-133562",
            "-16831"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2340469",
            "-127699",
            "-16097"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "99596",
            "-5434",
            "-685"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "49835",
            "-2717",
            "-343"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "28618",
            "-1560",
            "-197"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7401",
            "-403",
            "-51"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8560",
            "-466",
            "-59"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1159",
            "-63",
            "-8"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "150397",
            "-8135",
            "-1043"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "750826",
            "-40612",
            "-5207"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "250899",
            "-13571",
            "-1740"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1871",
            "-101",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "83876",
            "-4526",
            "-583"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1507897",
            "-81367",
            "-10481"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "516773",
            "-27885",
            "-3592"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "42422",
            "-2288",
            "-295"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "395115",
            "-21307",
            "-2748"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1142923",
            "-61633",
            "-7949"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1161242",
            "-62616",
            "-8077"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "18319",
            "-983",
            "-128"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "18748",
            "-1006",
            "-131"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "429",
            "-23",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2857",
            "-153",
            "-20"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2428",
            "-130",
            "-17"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "49811",
            "-2665",
            "-349"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "246627",
            "-13195",
            "-1728"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "412483",
            "-22061",
            "-2891"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "165856",
            "-8866",
            "-1163"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "167563",
            "-8957",
            "-1175"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1707",
            "-91",
            "-12"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2702",
            "-144",
            "-19"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 3501,
      "side": -1,
      "supports": 31,
      "events": 18,
      "distinct": 18,
      "results": [
        {
          "kind": "open",
          "r": [
            "7408",
            "-522",
            "-35"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "19260",
            "-1357",
            "-91"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "11004",
            "-775",
            "-52"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2748",
            "-193",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1268",
            "-89",
            "-6"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8664",
            "-608",
            "-41"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5916",
            "-415",
            "-28"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "9084",
            "-637",
            "-43"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "46428",
            "-3247",
            "-220"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "83772",
            "-5857",
            "-397"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "30380",
            "-2123",
            "-144"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7368",
            "-512",
            "-35"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "13452",
            "-931",
            "-64"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6084",
            "-419",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3356",
            "-231",
            "-16"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "628",
            "-43",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5228",
            "-357",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "9828",
            "-671",
            "-47"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "22360",
            "-1524",
            "-107"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "34892",
            "-2377",
            "-167"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "12324",
            "-839",
            "-59"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "39052",
            "-2657",
            "-187"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "41764",
            "-2841",
            "-200"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2712",
            "-184",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "56912",
            "-3854",
            "-273"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "111112",
            "-7524",
            "-533"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "55660",
            "-3769",
            "-267"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "208",
            "-14",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "55740",
            "-3751",
            "-268"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "111272",
            "-7488",
            "-535"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "37012",
            "-2489",
            "-178"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "73788",
            "-4957",
            "-355"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "28652",
            "-1919",
            "-138"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "270036",
            "-18071",
            "-1301"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "48776",
            "-3264",
            "-235"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "22620",
            "-1513",
            "-109"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "12036",
            "-805",
            "-58"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    }
  ],
  "totalPatterns": 138508,
  "excluded": [
    1337,
    3501
  ],
  "strata": 74
}
```
