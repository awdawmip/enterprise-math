# X6 R196 — Twenty-one-event rank-two exclusion replay

2026-11-25. AUTHOR EXACT FINITE NECESSARY-RELAXATION REPLAY / NOT_REVIEWED. Independent informed static BRC auxiliary weight research. Historical predecessor EM-DIRECT-AE5AD5; live execution binding unconfirmed. Original request r2-20261125-1813-x6-read SUCCEEDED, observed 2026-11-25T10:13:26.937957Z, Source f95a357f39459396d06972facdc1e34cba5dc41b, NO_CANONICAL_PUBLICATION_DIRECTORY; execution_authorized=false, native_operational_view_evaluated=false. No CLAIM, owner mutation, formal result or review.

## Frozen scope and method

R195@5906a4e763dca22078236b0ade6fd24b7d00589d blob e26021f141ba7a9904291436ab45898f500a4715; R182 side census@6945e591116377f9386c7419b6ce31a2b9e8a146 blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82; R182 one-child theorem@502d7abb2fe8470ed2cdabf242c2cc59a0c302ac. Retain R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f: Port 10, 1935 unoriented integer directions, six BRC denominators, w=(17t,B,22t,D), exact optimum and strict 3/2 near set. P000 V5, ACTIVE worldview and joint-relation preservation. Auxiliary coefficient chart only. No re-scoring. R182 proves the fixed-endpoint depth-five necessary capacity relaxation of each child constant on its own exact event strata. Replay retains equality points, open intervals, endpoint incidence and root signs, clips actual components before compressing to extreme endpoints per support. Coincident event rays coalesced; original labels retained. A uniformly failing child excludes the class; passing is only necessary-relaxation feasibility, not a tree witness. The executed function was compared to R195 source modulo whitespace before running; inputs are the exact two min-21 rows of pinned census. BigInt geometry and exact finite support masks.

## Executed result

```json
[
  {
    "id": 1506,
    "side": -1,
    "supports": 27,
    "events": 21,
    "distinct": 21,
    "strata": 43,
    "passing": 0
  },
  {
    "id": 3484,
    "side": -1,
    "supports": 30,
    "events": 21,
    "distinct": 21,
    "strata": 43,
    "passing": 0
  }
]
```

Total 86 strata; sum of distinct pattern counts 144270; newly excluded [1506,3484]. Conditional on inherited R195: remaining 177 = 89 rank two + 88 rank three. Global 6<=D_linear<=7 unchanged. Any nonexcluded rows remain unresolved. Next min-22 census rows: [{"id":1714,"events":[[1,49],[-1,22]]}]. Activity association and independent review not claimed.

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
const rows=[{"i":1506,"a":"898455116316568","b":"1353344697237607","r":["135","0","-2"],"local":47,"vertices":[["69","0","-1"],["66","0","-1"]],"sides":[{"side":1,"supports":27,"events":["1,1,68","10,49,677","11,187,731","11,5,736","121,120,8226","125,2059,8471","147,55,9812","17,289,1157","18,136,1241","18,85,1241","19,11,1276","19,28,1310","207,1036,13862","3,1,200","35,179,2317","38,191,2539","464,2207,31879","472,2239,32471","5,43,341","53,425,3553","55,272,3706","59,425,3995","61,1031,4195","63,5,4168","69,65,4684","9,10,614","9,11,616"]},{"side":-1,"supports":27,"events":["10,81,672","101,901,6953","121,1114,8174","127,1103,8683","147,1073,10003","16,139,1094","16,3,1062","169,1566,11346","2,17,136","25,37,1724","301,2669,20689","37,44,2530","4,35,274","47,745,3117","5,7,344","56,459,3774","63,317,4207","69,341,4651","7,2,466","9,10,614","9,76,611"]}]},{"i":3484,"a":"909987372204024","b":"1341812437286919","r":["4076","-221","-21"],"local":41,"vertices":[["196","-11","-1"],["7956","-431","-41"]],"sides":[{"side":1,"supports":30,"events":["1,16,23","10,178,25","12,113,1135","13,120,1232","14,251,35","152,2727,380","19,301,440","21,356,280","21,358,266","22,395,55","23,402,207","246,4403,615","288,5117,720","3,51,38","3,51,40","30,527,253","30,536,75","38,607,875","46,821,115","46,836,115","7,123,63","77,1343,693","9,114,530"]},{"side":-1,"supports":30,"events":["10,179,25","1138,20723,2845","15,263,127","158,2803,395","164,2899,410","1786,32171,4465","203,3555,1827","236,4181,590","26,461,65","3,51,38","3,51,40","32,583,80","352,6221,880","38,607,875","38,685,95","398,7078,995","406,7214,1015","568,10319,1420","6,106,15","626,11071,1565","82,1472,205"]}]}];
console.log(JSON.stringify(replay(data,rows),null,2));
```

## Full executed output

```json
{
  "output": [
    {
      "i": 1506,
      "side": -1,
      "supports": 27,
      "events": 21,
      "distinct": 21,
      "results": [
        {
          "kind": "open",
          "r": [
            "1793",
            "0",
            "-26"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1724",
            "0",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8677",
            "0",
            "-126"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6953",
            "0",
            "-101"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7297",
            "0",
            "-106"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "344",
            "0",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2337",
            "0",
            "-34"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "20689",
            "0",
            "-301"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6942",
            "0",
            "-101"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "137",
            "0",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "889",
            "0",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2530",
            "0",
            "-37"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3077",
            "0",
            "-45"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "547",
            "0",
            "-8"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1846",
            "0",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8683",
            "0",
            "-127"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9297",
            "0",
            "-136"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "614",
            "0",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "681",
            "0",
            "-10"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1429",
            "0",
            "-21"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1497",
            "0",
            "-22"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "68",
            "0",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "679",
            "0",
            "-10"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "611",
            "0",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1757",
            "0",
            "-26"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8174",
            "0",
            "-121"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "135",
            "0",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4651",
            "0",
            "-69"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6538",
            "0",
            "-97"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1887",
            "0",
            "-28"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "741",
            "0",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "336",
            "0",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1947",
            "0",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11346",
            "0",
            "-169"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "11947",
            "0",
            "-178"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "601",
            "0",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1067",
            "0",
            "-16"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "466",
            "0",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "997",
            "0",
            "-15"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "531",
            "0",
            "-8"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3648",
            "0",
            "-55"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3117",
            "0",
            "-47"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1061",
            "0",
            "-16"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 3484,
      "side": -1,
      "supports": 30,
      "events": 21,
      "distinct": 21,
      "results": [
        {
          "kind": "open",
          "r": [
            "16248",
            "-908",
            "-83"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "16052",
            "-897",
            "-82"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "958124",
            "-53521",
            "-4895"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "942072",
            "-52624",
            "-4813"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "230180",
            "-12857",
            "-1176"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "439008",
            "-24518",
            "-2243"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "567972",
            "-31717",
            "-2902"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "128964",
            "-7199",
            "-659"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "177668",
            "-9913",
            "-908"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "48704",
            "-2714",
            "-249"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "118516",
            "-6601",
            "-606"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "69812",
            "-3887",
            "-357"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "25616",
            "-1426",
            "-131"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "32652",
            "-1817",
            "-167"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "38896",
            "-2162",
            "-199"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "84036",
            "-4669",
            "-430"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "27748",
            "-1541",
            "-142"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "82452",
            "-4577",
            "-422"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "89280",
            "-4954",
            "-457"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6828",
            "-377",
            "-35"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5656",
            "-312",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "27108",
            "-1495",
            "-139"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "34708",
            "-1913",
            "-178"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7600",
            "-418",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "24748",
            "-1361",
            "-127"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "17148",
            "-943",
            "-88"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "977856",
            "-53590",
            "-5023"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4872132",
            "-267007",
            "-25027"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4872716",
            "-267039",
            "-25030"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "584",
            "-32",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8564",
            "-469",
            "-44"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7980",
            "-437",
            "-41"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "23724",
            "-1295",
            "-122"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "39468",
            "-2153",
            "-203"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "13412",
            "-731",
            "-69"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "41004",
            "-2233",
            "-211"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "32244",
            "-1753",
            "-166"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "120216",
            "-6532",
            "-619"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "141684",
            "-7681",
            "-730"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3138516",
            "-170131",
            "-16171"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1048436",
            "-56833",
            "-5402"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6792",
            "-368",
            "-35"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "14748",
            "-799",
            "-76"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    }
  ],
  "totalPatterns": 144270,
  "excluded": [
    1506,
    3484
  ],
  "strata": 86
}
```
