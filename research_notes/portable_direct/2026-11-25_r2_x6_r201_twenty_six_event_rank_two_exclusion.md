# X6 R201 — Twenty-six-event rank-two exclusion replay

2026-11-25. AUTHOR EXACT FINITE NECESSARY-RELAXATION REPLAY / NOT_REVIEWED. Independent informed static BRC auxiliary weight research. Current live research identity unconfirmed; historical predecessor EM-DIRECT-AE5AD5. Native read request r2-20261125-2311-x6-read SUCCEEDED at 2026-11-25T15:11:32.752274Z, Source e9a2c363dccf1eab6755e467d2f87bb18e598300, NO_CANONICAL_PUBLICATION_DIRECTORY, execution_authorized=false, native_operational_view_evaluated=false. This establishes no owner absence. No CLAIM, owner change, formal Result or review.

## Scope and proof

Reuse R200@3c0645a4c449ed77fb4af4210456c792b517be4b:research_notes/portable_direct/2026-11-25_r2_x6_r200_twenty_five_event_rank_two_exclusion.md (blob 980aa53e7ad6066e7b5c2f427838021d62be0fd5), R182 theorem@502d7abb2fe8470ed2cdabf242c2cc59a0c302ac and census@6945e591116377f9386c7419b6ce31a2b9e8a146 (blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82). Frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f: Port 10, 1935 unoriented integer directions, four positive weights w=(17t,B,22t,D), six joint BRC pair denominators, strict 3/2 near-direction set. P000 V5 and joint relation observer preservation. Auxiliary coefficient chart, not native spatial geometry/dynamics; no fresh physical or classical reference computation. Reuse the R182 one-child refinement: fixed labeled ternary determinant strata preserve the depth-five necessary relaxation; in rank two r=alpha*u+beta*v with alpha,beta>0, event locations are beta/alpha=|x dot u|/|x dot v|. Exact equality strata and open intervals are represented separately. Equal geometric cuts coalesced without erasing original event identities. If all strata of either child fail the necessary relaxation, the root class is impossible. Passing does not prove a tree. Source equality check of executed replay function vs pinned R200 modulo whitespace passed. Embedded frozen support bank and entire min-26 census tranche; exact BigInt geometry and finite bit masks, no claim of independent review.

## Executed result

```json
[
  {
    "id": 1137,
    "side": 1,
    "supports": 31,
    "events": 26,
    "distinct": 26,
    "strata": 53,
    "passing": 0
  }
]
```

Total 53 strata; sum of distinct observation pattern counts 80917; newly excluded [1137]. Conditional on inherited R200, remaining 168 = 80 rank two + 88 rank three. Bound 6<=D_linear<=7 unchanged. Next min-27 rows: [{"id":1208,"events":[[1,27],[-1,74]]},{"id":1481,"events":[[1,27],[-1,61]]}]. Activity association and independent review outstanding.

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
const rows=[{"i":1137,"a":"1407393333349","b":"2250392420351882","r":["-35","15","-1"],"local":88,"vertices":[["-85","36","-2"],["-1000","429","-29"]],"sides":[{"side":1,"supports":31,"events":["1,11,145","1,12,144","1,15,219","1,8,96","11,74,814","123,1961,26041","13,569,9259","16,89,847","2,21,291","2,73,1211","2,9,69","23,149,1499","24,371,5023","3,26,286","3,34,434","45,691,9839","47,2191,35081","5,201,3231","5,389,5603","51,2539,38333","55,2327,36817","7,106,1454","73,1007,14671","8,45,423","9,143,1963","91,4891,75709"]},{"side":-1,"supports":29,"events":["1,15,219","1,16,212","1,16,218","11,122,1594","11,124,1592","11,391,6545","11,476,7480","11,476,7769","11,68,697","11,74,814","124,765,7854","128,765,8058","13,935,13651","132,881,9768","134,884,8789","147,530,3292","162,1315,15533","165,712,5723","166,909,8802","168,1054,10829","17,101,1069","176,1029,9267","18,116,1171","18,98,955","196,1075,10391","2,153,2210","2,23,289","20,107,1063","203,1275,13090","21,176,2008","211,1275,13430","23,183,2209","23,352,4796","233,1542,17242","26,1309,20570","27,100,602","27,170,1717","27,212,2596","3,170,2482","3,20,222","3,26,286","3,32,436","3,34,434","31,220,2294","319,2206,23606","32,175,1697","332,1913,17509","4,26,261","4,29,296","4,55,803","43,634,9428","47,656,9484","53,628,7640","59,416,4366","6,34,317","648,4337,47952","7,106,1454","7,115,1523","7,47,462","7,76,1016","705,6047,67273","71,2652,43656","717,6115,68453","77,555,5698","79,555,5846","8,45,423","83,1268,18154","93,424,3203"]}]}];
console.log(JSON.stringify(replay(data,rows),null,2));
```

## Actual full output

```json
{
  "output": [
    {
      "i": 1137,
      "side": 1,
      "supports": 31,
      "events": 26,
      "distinct": 26,
      "results": [
        {
          "kind": "open",
          "r": [
            "-380",
            "161",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-675",
            "286",
            "-16"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-880",
            "373",
            "-21"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-2845",
            "1206",
            "-68"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-71165",
            "30183",
            "-1717"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-68320",
            "28977",
            "-1649"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-34670",
            "14705",
            "-837"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1020",
            "433",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-22235",
            "9443",
            "-549"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-43450",
            "18453",
            "-1073"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-5860",
            "2489",
            "-145"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-15150",
            "6437",
            "-377"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1085",
            "461",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-40",
            "17",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1870",
            "795",
            "-47"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-3700",
            "1573",
            "-93"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-2425",
            "1031",
            "-61"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1150",
            "489",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-23445",
            "9971",
            "-593"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-45740",
            "19453",
            "-1157"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-23205",
            "9869",
            "-587"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-670",
            "285",
            "-17"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-43280",
            "18411",
            "-1099"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-172450",
            "73359",
            "-4379"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-58115",
            "24722",
            "-1476"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1895",
            "807",
            "-49"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-8635",
            "3680",
            "-226"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-6740",
            "2873",
            "-177"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-62385",
            "26597",
            "-1643"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-118030",
            "50321",
            "-3109"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-118975",
            "50724",
            "-3134"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-945",
            "403",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1435",
            "612",
            "-38"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-9100",
            "3881",
            "-241"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1850",
            "789",
            "-49"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-2000",
            "853",
            "-53"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-415",
            "177",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-75",
            "32",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-11705",
            "4995",
            "-313"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-11630",
            "4963",
            "-311"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-95300",
            "40687",
            "-2567"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-178970",
            "76411",
            "-4823"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-45305",
            "19343",
            "-1221"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-2250",
            "961",
            "-61"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-61325",
            "26214",
            "-1684"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-120400",
            "51467",
            "-3307"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-30425",
            "13006",
            "-836"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1300",
            "557",
            "-37"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-35",
            "15",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-660",
            "283",
            "-19"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-935",
            "401",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-8690",
            "3727",
            "-251"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-4845",
            "2078",
            "-140"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    }
  ],
  "totalPatterns": 80917,
  "excluded": [
    1137
  ],
  "strata": 53
}
```
