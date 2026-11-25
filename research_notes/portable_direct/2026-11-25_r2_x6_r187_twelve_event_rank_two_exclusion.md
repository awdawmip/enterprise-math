# X6 R187 — twelve-event rank-two replay

2026-11-25. Independent informed static six-pair BRC auxiliary weight study, author calculation, NOT_REVIEWED. Historical lane provenance EM-DIRECT-AE5AD5; live identity unconfirmed. No formal CLAIM. Current task receipt r2-20261125-0910-x6-read SUCCEEDED at 2026-11-25T01:10:33.171983+00:00, Source 3d75222684d0e92cda6dbdf5200384e3e1e75b91, NO_CANONICAL_PUBLICATION_DIRECTORY, native_operational_view_evaluated=false, execution_authorized=false. No owner mutation. P000 V5 and ACTIVE residual fidelity preserved; coefficient chart is an auxiliary observation model, not native space or dynamics.

Frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f inherited through R186@e6365a1de6dfc49fadca0ecc961f283d9249991b. Port 10, 1935 unoriented directions, six BRC pair observers, positive weights (17t,B,22t,D), exact optimum and strict 3/2 near set. Actual input reads: R186 exact embedded support bank, blob 10b5c6b7e7aac009d029d8866fa0b0696c7195c0; R182 side census at 6945e591116377f9386c7419b6ce31a2b9e8a146:research_notes/portable_direct/x6_r182_rank_two_side_census.json, blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82. All rows with min side event count 12: 1280,1421. No new direction scoring. Inherited R182 single-child sufficient event theorem and R178/R186 depth-five endpoint capacity relaxation. For each side the event ratio |x.u|/|x.v| sorts the entire relative open rank-two cone; positive sums represent open intervals, internal rays represent equality strata. Verify masks and support counts exactly, clip the actual disconnected components before endpoint extraction, then evaluate inherited necessary capacity relaxation. All arithmetic BigInt except bounded 31-bit support masks. A side with no feasible stratum implies the whole root class is excluded; feasibility is only relaxation feasibility. No claim for any untested class. Current bounds remain conditional on inherited proof bank: 6<=D_linear<=7.

## Actual execution

- 1280, side 1, supports 29, events 12, distinct 12, strata 25, passing 0, excluded true
- 1421, side 1, supports 28, events 12, distinct 12, strata 25, passing 0, excluded true

Executed in JavaScript tool runtime, no separate Node execution. Total strata 50; summed unique sign-pattern counts 92008; newly excluded 1280, 1421. Remaining 218 = 130 rank two + 88 rank three. Activity association pending; no independent review. Next: process smallest untested event tranche, or exact intersection for any surviving two-sided classes; rank-three normalized polygon strata remain open.

## Reproduction (standalone JS)

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
const rows=[{"i":1280,"a":"1132515435088","b":"2250667298217391","r":["303","310","-42"],"local":52,"vertices":[["276","290","-39"],["27","20","-3"]],"sides":[{"side":1,"supports":29,"events":["1,12,92","1,18,138","1,27,207","1,28,206","2,105,747","2,57,411","3,27,211","3,53,415","4,49,367","4,75,549","45,1246,9284","5,43,341"]},{"side":-1,"supports":29,"events":["1,52,368","1,56,412","1,9,73","10,63,522","10,81,672","10,90,729","101,901,6953","11,595,4301","11,636,4752","1109,12984,102352","1109,20420,152584","1109,31574,227932","127,1103,8683","15,135,1087","16,139,1094","166,1053,8658","1661,3587,38845","17,153,1188","181,2196,16628","2,17,136","216,1319,11317","25,288,2312","25,444,3456","25,678,5172","3,170,1258","3,35,277","301,2669,20689","4,201,1395","4,35,274","4,75,549","41,2023,13889","56,459,3774","57,683,5245","59,1115,8089","59,699,5437","607,31060,217832","63,138,1474","87,1069,7979","88,1065,8087","9,244,1862","9,76,611"]}]},{"i":1421,"a":"901191245627384","b":"1341812475035655","r":["3978","-223","-26"],"local":40,"vertices":[["1377","-79","-9"],["2601","-144","-17"]],"sides":[{"side":1,"supports":28,"events":["11,70,1074","16,179,887","17,111,1657","278,4843,695","33,544,440","356,2243,34781","4,49,185","58,567,4002","7,80,392","76,941,3505","9,101,497","9,58,878"]},{"side":-1,"supports":31,"events":["108,1873,270","12,191,160","158,2803,395","164,2899,410","18,293,240","19,284,457","21,344,202","22,387,55","236,4181,590","26,461,65","27,433,360","27,445,342","33,533,418","33,535,440","34,591,85","352,6221,880","378,6647,945","54,931,135","594,10319,1485","6,106,15","6,89,145","626,11071,1565","69,1108,920","69,1112,874","7,106,167","7,80,388","72,1237,180","9,146,114"]}]}];
console.log(JSON.stringify(replay(data,rows),null,2));
```

## Actual output

```json
{
  "output": [
    {
      "i": 1280,
      "side": 1,
      "supports": 29,
      "events": 12,
      "distinct": 12,
      "results": [
        {
          "kind": "open",
          "r": [
            "425",
            "446",
            "-60"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "149",
            "156",
            "-21"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "601",
            "622",
            "-84"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1053",
            "1088",
            "-147"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1755",
            "1762",
            "-240"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "702",
            "674",
            "-93"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "26663",
            "24724",
            "-3447"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "52624",
            "48774",
            "-6801"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1417",
            "1312",
            "-183"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1222",
            "1082",
            "-153"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "169",
            "148",
            "-21"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "468",
            "398",
            "-57"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1975",
            "1674",
            "-240"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1507",
            "1276",
            "-183"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6472",
            "5450",
            "-783"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4965",
            "4174",
            "-600"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2583",
            "2170",
            "-312"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "201",
            "166",
            "-24"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "76",
            "62",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "331",
            "268",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "586",
            "474",
            "-69"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "255",
            "206",
            "-30"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "103",
            "82",
            "-12"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "157",
            "122",
            "-18"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "184",
            "142",
            "-21"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 1421,
      "side": 1,
      "supports": 28,
      "events": 12,
      "distinct": 12,
      "results": [
        {
          "kind": "open",
          "r": [
            "172278",
            "-9883",
            "-1126"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "343179",
            "-19687",
            "-2243"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "185283",
            "-10624",
            "-1211"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "27387",
            "-1561",
            "-179"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "14229",
            "-811",
            "-93"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1071",
            "-61",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "16524",
            "-941",
            "-108"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "15453",
            "-880",
            "-101"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "16983",
            "-967",
            "-111"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1530",
            "-87",
            "-10"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "742509",
            "-41926",
            "-4853"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "740979",
            "-41839",
            "-4843"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "147492",
            "-8327",
            "-964"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "143973",
            "-8123",
            "-941"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "16983",
            "-958",
            "-111"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8874",
            "-499",
            "-58"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "765",
            "-43",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4131",
            "-232",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3519",
            "-196",
            "-23"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "16983",
            "-944",
            "-111"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "29223",
            "-1623",
            "-191"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "12240",
            "-679",
            "-80"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "11934",
            "-661",
            "-78"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "83232",
            "-4609",
            "-544"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "85833",
            "-4753",
            "-561"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    }
  ],
  "totalPatterns": 92008,
  "excluded": [
    1280,
    1421
  ],
  "strata": 50
}
```
