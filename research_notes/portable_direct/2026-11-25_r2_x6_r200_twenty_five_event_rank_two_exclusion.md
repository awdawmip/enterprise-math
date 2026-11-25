# X6 R200 — Twenty-five-event rank-two exclusion replay

2026-11-25. AUTHOR EXACT FINITE NECESSARY-RELAXATION REPLAY / NOT_REVIEWED. Independent informed static BRC auxiliary weight research. Live execution identity unconfirmed; historical predecessor EM-DIRECT-AE5AD5. Control request r2-20261125-2206-x6-read SUCCEEDED at 2026-11-25T14:06:55.128175Z, Source c9608394c68f0ac8c9af7d1c5f294c3900a69229, NO_CANONICAL_PUBLICATION_DIRECTORY, execution_authorized=false, native_operational_view_evaluated=false. No native CLAIM, owner change or formal Result/review.

## Frozen scope and proof

R199@02e04e9c00933f25a2101f8916504a21d74eabd3:research_notes/portable_direct/2026-11-25_r2_x6_r199_twenty_four_event_rank_two_exclusion.md (blob ae21fea2c590db6899c6478c1ee19dbf505bc6d8); R182 census@6945e591116377f9386c7419b6ce31a2b9e8a146:research_notes/portable_direct/x6_r182_rank_two_side_census.json (blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82); R182 theorem@502d7abb2fe8470ed2cdabf242c2cc59a0c302ac:research_notes/portable_direct/2026-11-25_r2_x6_r182_one_child_event_refinement.md. R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f remain frozen: Port 10, 1935 unoriented integer directions, w=(17t,B,22t,D), six BRC pair denominators, exact minimizer and strict 3/2 near set. P000 V5 and joint relation preservation; auxiliary coefficient chart only. R182 one-child sufficiency: the labeled child ternary determinant arrangement fixes the depth-five necessary relaxation within each exact stratum. For r=alpha*u+beta*v with both coefficients positive, event ratios beta/alpha=|x dot u|/|x dot v| determine the exact open intervals and singleton equality strata. Coalesce only identical geometric rays, preserve underlying event and support labels. If all strata of either child fail, the whole root class is excluded. Passing necessary relaxation is not sufficient. Actual replay function equals R199 frozen source modulo whitespace. Selected rows are the entire min-25 tranche of the frozen R182 census. BigInt geometry and exact finite bit masks.

## Executed result

```json
[
  {
    "id": 1961,
    "side": 1,
    "supports": 29,
    "events": 25,
    "distinct": 24,
    "strata": 49,
    "passing": 0
  },
  {
    "id": 2201,
    "side": 1,
    "supports": 26,
    "events": 25,
    "distinct": 25,
    "strata": 51,
    "passing": 51
  },
  {
    "id": 2201,
    "side": -1,
    "supports": 29,
    "events": 27,
    "distinct": 27,
    "strata": 55,
    "passing": 0
  }
]
```

Total 155 strata; sum of distinct pattern counts 284139; newly excluded [1961,2201]. Conditional on inherited R199, remaining 169 = 81 rank two + 88 rank three. Bound 6<=D_linear<=7 unchanged. Nonexcluded rows remain unresolved. Next min-26 rows from frozen census: [{"id":1137,"events":[[1,26],[-1,68]]}]. Activity association and independent review outstanding.

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
const rows=[{"i":1961,"a":"863133322182424","b":"1388666424393959","r":["158","3","-3"],"local":47,"vertices":[["3927","82","-77"],["7449","134","-139"]],"sides":[{"side":1,"supports":29,"events":["1,1,53","1,10,62","1,2,55","1,34,87","11,775,1386","12,17,646","12,407,1044","138,85,7208","1394,207778,275315","19,28,1025","199,3273,13731","2,295,395","2,7,110","3,1,155","3,5,163","36,4981,7110","36,5245,7110","362,5897,24978","38,17,1972","4,7,218","6,425,756","6,856,1185","7,17,391","79,1335,5451","863,71,44155"]},{"side":-1,"supports":26,"events":["1,16,69","1016,2881,56555","108,289,6029","11,17,595","12,17,646","139,153,7395","16,23,862","16,2367,3160","176,535,9761","18,64,989","2,6,111","2,7,110","21,209,1309","220,711,12159","23,51,1275","25,17,1309","265,527,14569","3,7,167","356,1255,19571","37,34,1955","38,113,2110","38,117,2106","7,115,483","7,17,391","8,27,441"]}]},{"i":2201,"a":"1115182595608","b":"2250684614312423","r":["2481","126","-67"],"local":46,"vertices":[["578","35","-17"],["1903","91","-50"]],"sides":[{"side":1,"supports":26,"events":["1,1,38","1002,80773,197895","14,1199,2765","15,346,1214","166,13430,32785","19,11,730","19,28,713","20,947,2520","21,1012,2646","23,1054,2898","27,620,2188","3145,146454,396270","329,15070,41454","35,933,3045","4,107,348","4,29,205","4,341,790","40,3181,7900","501,23870,63126","56,4813,11060","72,3377,9072","746,539,28555","8,13,299","83,3894,10458","948,44209,119448"]},{"side":-1,"supports":29,"events":["1,1,38","11,291,957","12,13,455","14,108,711","151,149,5740","152,101,5827","18,7,695","19,11,730","19,28,713","2,15,102","2,16,101","2,170,395","2,3,75","3,2,115","302,2326,15341","304,371,11485","38,293,1930","38,295,1928","38,303,1920","38,3285,7505","4,107,348","4,29,205","4,3,153","8,13,299","8,59,409","8,7,305","9,8,343"]}]}];
console.log(JSON.stringify(replay(data,rows),null,2));
```

## Actual output

```json
{
  "output": [
    {
      "i": 1961,
      "side": 1,
      "supports": 29,
      "events": 25,
      "distinct": 24,
      "results": [
        {
          "kind": "open",
          "r": [
            "4744",
            "99",
            "-93"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "53001",
            "1106",
            "-1039"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "128404",
            "2679",
            "-2517"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "75403",
            "1573",
            "-1478"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "60932",
            "1267",
            "-1193"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1691625",
            "35170",
            "-33119"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "231469",
            "4804",
            "-4529"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "623065",
            "12870",
            "-12171"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "27697",
            "572",
            "-541"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "41663",
            "858",
            "-813"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "21319",
            "439",
            "-416"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "975",
            "20",
            "-19"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4058",
            "83",
            "-79"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "15257",
            "312",
            "-297"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "81553",
            "1663",
            "-1586"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "147849",
            "3014",
            "-2875"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "50091",
            "1021",
            "-974"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2424",
            "49",
            "-47"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "60257",
            "1217",
            "-1168"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "178347",
            "3602",
            "-3457"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "89819",
            "1814",
            "-1741"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1291",
            "26",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1607",
            "32",
            "-31"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1923",
            "38",
            "-37"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "10378",
            "203",
            "-199"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8455",
            "165",
            "-162"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "40244",
            "779",
            "-769"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "72033",
            "1393",
            "-1376"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "77116",
            "1491",
            "-1473"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5083",
            "98",
            "-97"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "19357",
            "372",
            "-369"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "72345",
            "1390",
            "-1379"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "72503",
            "1393",
            "-1382"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "158",
            "3",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "15299",
            "289",
            "-290"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "15141",
            "286",
            "-287"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "276326",
            "5211",
            "-5235"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "537511",
            "10136",
            "-10183"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "611308",
            "11503",
            "-11573"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "685105",
            "12870",
            "-12963"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "344435",
            "6470",
            "-6517"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3765",
            "70",
            "-71"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "42675",
            "785",
            "-802"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "38910",
            "715",
            "-731"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2343",
            "43",
            "-44"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3264",
            "59",
            "-61"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "709513",
            "12798",
            "-13251"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2125275",
            "38335",
            "-39692"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "710908",
            "12823",
            "-13277"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 2201,
      "side": 1,
      "supports": 26,
      "events": 25,
      "distinct": 25,
      "results": [
        {
          "kind": "open",
          "r": [
            "1191",
            "72",
            "-35"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "4186",
            "253",
            "-123"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "89375",
            "5393",
            "-2624"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "85189",
            "5140",
            "-2501"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "47689",
            "2869",
            "-1398"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "10189",
            "598",
            "-295"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "2219311",
            "129355",
            "-64034"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "2209122",
            "128757",
            "-63739"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "1107353",
            "64541",
            "-31950"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "5584",
            "325",
            "-161"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "374909",
            "21656",
            "-10769"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "369325",
            "21331",
            "-10608"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "160343",
            "9194",
            "-4589"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "111704",
            "6251",
            "-3159"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "29881",
            "1672",
            "-845"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "7820",
            "437",
            "-221"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "1382",
            "77",
            "-39"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "3236",
            "179",
            "-91"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "3813",
            "210",
            "-107"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "577",
            "31",
            "-16"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "3369313",
            "179296",
            "-93005"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "3368736",
            "179265",
            "-92989"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "4388541",
            "233301",
            "-121082"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "1019805",
            "54036",
            "-28093"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "183099",
            "9690",
            "-5041"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "78789",
            "4104",
            "-2153"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "8931",
            "465",
            "-244"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "90900",
            "4731",
            "-2483"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "269572",
            "13825",
            "-7313"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "448244",
            "22919",
            "-12143"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "458343",
            "23433",
            "-12416"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "10099",
            "514",
            "-273"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "16301",
            "827",
            "-440"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "22503",
            "1140",
            "-607"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "58229",
            "2939",
            "-1568"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "35726",
            "1799",
            "-961"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "21016",
            "1057",
            "-565"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "6306",
            "315",
            "-169"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "150383",
            "7511",
            "-4030"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "144077",
            "7196",
            "-3861"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "155728",
            "7777",
            "-4173"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "11651",
            "581",
            "-312"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "585539",
            "29138",
            "-15665"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "573888",
            "28557",
            "-15353"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "191459",
            "9527",
            "-5122"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "489",
            "24",
            "-13"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "25335",
            "1221",
            "-668"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "24846",
            "1197",
            "-655"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "13165",
            "634",
            "-347"
          ],
          "feasible": true
        },
        {
          "kind": "event",
          "r": [
            "1484",
            "71",
            "-39"
          ],
          "feasible": true
        },
        {
          "kind": "open",
          "r": [
            "3387",
            "162",
            "-89"
          ],
          "feasible": true
        }
      ],
      "excluded": false
    },
    {
      "i": 2201,
      "side": -1,
      "supports": 29,
      "events": 27,
      "distinct": 27,
      "results": [
        {
          "kind": "open",
          "r": [
            "1191",
            "72",
            "-35"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4186",
            "253",
            "-123"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4799",
            "290",
            "-141"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "613",
            "37",
            "-18"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "12346",
            "739",
            "-361"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11733",
            "702",
            "-343"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "753",
            "45",
            "-22"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1068",
            "63",
            "-31"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "11257",
            "661",
            "-326"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "10189",
            "598",
            "-295"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9465",
            "531",
            "-268"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "169646",
            "9491",
            "-4797"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "60689",
            "3395",
            "-1716"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "12421",
            "694",
            "-351"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "13348",
            "745",
            "-377"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "927",
            "51",
            "-26"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "13520",
            "743",
            "-379"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "12593",
            "692",
            "-353"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "112896",
            "6189",
            "-3161"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "100303",
            "5497",
            "-2808"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "107141",
            "5870",
            "-2999"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6838",
            "373",
            "-191"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7415",
            "404",
            "-207"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "577",
            "31",
            "-16"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "43938",
            "2355",
            "-1217"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "87299",
            "4679",
            "-2418"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "92578",
            "4957",
            "-2563"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5279",
            "278",
            "-145"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9981",
            "525",
            "-274"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4702",
            "247",
            "-129"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6607",
            "346",
            "-181"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1905",
            "99",
            "-52"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2604",
            "135",
            "-71"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "699",
            "36",
            "-19"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1031",
            "53",
            "-28"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2394",
            "123",
            "-65"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7409",
            "380",
            "-201"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5015",
            "257",
            "-136"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6832",
            "349",
            "-185"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1817",
            "92",
            "-49"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "93907",
            "4753",
            "-2532"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "92090",
            "4661",
            "-2483"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "103741",
            "5242",
            "-2795"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11651",
            "581",
            "-312"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1083",
            "54",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "262",
            "13",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5519",
            "272",
            "-147"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "99080",
            "4883",
            "-2639"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "99569",
            "4907",
            "-2652"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "489",
            "24",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "11821",
            "571",
            "-312"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11332",
            "547",
            "-299"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6408",
            "309",
            "-169"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1484",
            "71",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3387",
            "162",
            "-89"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    }
  ],
  "totalPatterns": 284139,
  "excluded": [
    1961,
    2201
  ],
  "strata": 155
}
```
