# X6 R199 — Twenty-four-event rank-two exclusion replay

2026-11-25. AUTHOR EXACT FINITE NECESSARY-RELAXATION REPLAY / NOT_REVIEWED. Independent informed static BRC auxiliary weight research. Live research identity unconfirmed; historical predecessor EM-DIRECT-AE5AD5. Control request r2-20261125-2114-x6-read SUCCEEDED at 2026-11-25T13:14:46.330644Z; Source 0a9461102589067ad8b3bf4b982f0f8b1e5b0f5f; NO_CANONICAL_PUBLICATION_DIRECTORY, execution_authorized=false, native_operational_view_evaluated=false. No native CLAIM, owner change or Result/review.

## Frozen scope and proof

R198@f0b77c11c06a3f1b65cd30c7f88bdae506d0c06b:research_notes/portable_direct/2026-11-25_r2_x6_r198_twenty_three_event_rank_two_exclusion.md (blob b2f0990420fe3b2a500a23aa3f85d5a4b2b3a12a); R182 census@6945e591116377f9386c7419b6ce31a2b9e8a146:research_notes/portable_direct/x6_r182_rank_two_side_census.json (blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82); R182 one-child theorem@502d7abb2fe8470ed2cdabf242c2cc59a0c302ac:research_notes/portable_direct/2026-11-25_r2_x6_r182_one_child_event_refinement.md. R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f remain frozen: Port 10, 1935 unoriented integer directions, w=(17t,B,22t,D), six BRC pair denominators, exact minimizer and strict 3/2 near set. P000 V5, ACTIVE worldview and joint-relation preservation. Auxiliary coefficient chart only. Child-specific ternary determinant events partition the original relative-open rank-two class by the R182 theorem. Keep exact event points, open intervals, component clipping and all support incidence labels. Coalesce identical event rays only; a uniformly impossible child excludes the class, whereas passing a necessary capacity test is not sufficient. The actual replay function was checked against R198 source modulo whitespace before execution. The selected row is the complete min-24 tranche of the frozen R182 census. Exact BigInt geometry and finite bit masks.

## Executed result

```json
[
  {
    "id": 3265,
    "side": 1,
    "supports": 28,
    "events": 24,
    "distinct": 23,
    "strata": 47,
    "passing": 0
  }
]
```

Total 47 strata; sum of distinct pattern counts 79809; newly excluded [3265]. Conditional on inherited R198, remaining 171 = 83 rank two + 88 rank three. The bound 6<=D_linear<=7 is unchanged. Any nonexcluded row remains unresolved. Next min-25 rows from the frozen census: [{"id":1961,"events":[[1,25],[-1,25]]},{"id":2201,"events":[[1,25],[-1,27]]}]. Activity association and independent review remain outstanding.

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
const rows=[{"i":3265,"a":"863133304880920","b":"1388666508280039","r":["1704","11","-31"],"local":47,"vertices":[["1599","10","-29"],["105","1","-2"]],"sides":[{"side":1,"supports":28,"events":["1,153,126","1,2,55","1,75,87","1,87,87","10,3706,1975","12,17,646","18,6715,3555","19,1740,1653","19,28,1025","2,592,395","2,7,110","20,1653,1740","28,109,1529","3,173,235","3,5,163","4,15,219","4,7,218","42,2193,3290","5,409,435","66,3995,5170","7,17,391","8,3223,1580","9,114,530","9,530,705"]},{"side":-1,"supports":28,"events":["1,180,126","1016,2881,56555","108,289,6029","11,17,595","12,17,646","139,153,7395","16,23,862","176,535,9761","18,64,989","2,6,111","2,7,110","2,789,395","217,15987,18879","220,711,12159","23,51,1275","265,527,14569","3,220,261","3,7,167","32,415,1907","356,1255,19571","38,113,2110","38,117,2106","4,15,219","54,203,2956","664,2591,36253","7,17,391","8,27,441"]}]}];
console.log(JSON.stringify(replay(data,rows),null,2));
```

## Actual complete output

```json
{
  "output": [
    {
      "i": 3265,
      "side": 1,
      "supports": 28,
      "events": 24,
      "distinct": 23,
      "results": [
        {
          "kind": "open",
          "r": [
            "1267",
            "8",
            "-23"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6003",
            "38",
            "-109"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3469",
            "22",
            "-63"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "935",
            "6",
            "-17"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4509",
            "29",
            "-82"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8083",
            "52",
            "-147"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "769",
            "5",
            "-14"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1914",
            "13",
            "-35"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "14387",
            "101",
            "-264"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "26860",
            "189",
            "-493"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "13889",
            "98",
            "-255"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "14807",
            "105",
            "-272"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "20288",
            "145",
            "-373"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5481",
            "40",
            "-101"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8733",
            "64",
            "-161"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11985",
            "88",
            "-221"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6128",
            "45",
            "-113"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "271",
            "2",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9048",
            "67",
            "-167"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8777",
            "65",
            "-162"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "10342",
            "77",
            "-191"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1565",
            "12",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2422",
            "19",
            "-45"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3279",
            "26",
            "-61"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "376",
            "3",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1233",
            "10",
            "-23"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "857",
            "7",
            "-16"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "481",
            "4",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2029",
            "17",
            "-38"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1548",
            "13",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5755",
            "49",
            "-108"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "15717",
            "134",
            "-295"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "12831",
            "110",
            "-241"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "9945",
            "86",
            "-187"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4251",
            "37",
            "-80"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2808",
            "25",
            "-53"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1111",
            "10",
            "-21"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7191",
            "65",
            "-136"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1321",
            "12",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2056",
            "19",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "10700",
            "99",
            "-203"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "19344",
            "179",
            "-367"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "29143",
            "270",
            "-553"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "9799",
            "91",
            "-186"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9738",
            "91",
            "-185"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "77843",
            "728",
            "-1479"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "77948",
            "729",
            "-1481"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    }
  ],
  "totalPatterns": 79809,
  "excluded": [
    3265
  ],
  "strata": 47
}
```
