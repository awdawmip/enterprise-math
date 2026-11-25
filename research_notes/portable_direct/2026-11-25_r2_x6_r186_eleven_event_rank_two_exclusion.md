# X6 R186 — eleven-event rank-two replay

2026-11-25. Independent informed static BRC auxiliary weight study; author computation, NOT_REVIEWED. Historical lane provenance EM-DIRECT-AE5AD5, live identity unconfirmed. No formal CLAIM. X6 read r2-20261125-0810-x6-read SUCCEEDED, observed 2026-11-25T00:10:31.992515+00:00, Source 8fb933dfaae16de5f8d4fd6d712545a8b1fc83e9, NO_CANONICAL_PUBLICATION_DIRECTORY, native_operational_view_evaluated=false, execution_authorized=false. No owner mutation.

Frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f inherited through R185@78ab5daae47e66b347b07d7bde08707a43f9b019. Port 10, 1935 unoriented directions, six BRC pair observers, positive weights (17t,B,22t,D), exact optimum and full strict 3/2 near set. P000 V5 and ACTIVE residual fidelity; auxiliary coefficient chart only. Inputs: R182 side census 6945e591116377f9386c7419b6ce31a2b9e8a146:research_notes/portable_direct/x6_r182_rank_two_side_census.json; bank from 5f3315d51bdfd61afcd63cad89aa5f63d76592ea:research_notes/portable_direct/x6_r185_ten_event_first_child.cjs. Both fetched at pins. No new direction scoring. Select all two rows with minimum side events 11, not in R182–R185 completed tranches. Sort sides explicitly. Preserve R182 one-child sufficient signs, coalesce exact event ratios, evaluate event equalities and all open intervals, check original sign masks and clipped support count, use inherited R178/R185 depth-five endpoint necessary relaxation. Passing is not actual tree construction.

Executed exact BigInt replay in JavaScript tool runtime; no separate Node execution. Each row is evaluated on smaller side first; opposite if needed. A child failing every stratum excludes root class. For any surviving class, both-child intersection remains open unless already determined.

- 1389, side 1, supports 30, events 11, distinct 11, strata 23, passing 0, excluded true
- 3938, side 1, supports 30, events 11, distinct 11, strata 23, passing 0, excluded true

Total strata 46; summed unique sign-pattern counts 101718; newly excluded 1389, 3938. Remaining 220 = 132 rank two + 88 rank three, conditional on inherited proof bank; 6<=D_linear<=7. Next: exclude completed IDs and process min-12 tranche or surviving opposite intersections; rank-three exact relative strata still open. Activity binding pending.

## Reproducible source

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
const rows=[{"i":1389,"a":"900645550161912","b":"1351145673588743","r":["2005","-74","-18"],"local":23,"vertices":[["1769","-65","-16"],["236","-9","-2"]],"sides":[{"side":1,"supports":30,"events":["14,187,803","17,55,1661","25,261,1725","27,646,342","29,112,2888","29,714,261","3,40,172","58,1493,145","71,271,7061","8,32,787","87,2176,725"]},{"side":-1,"supports":29,"events":["21,500,280","21,502,266","21,515,175","258,6647,645","27,640,342","27,641,360","32,415,1907","33,782,440","33,784,418","387,9673,3225","43,1071,387","7,171,63"]}]},{"i":3938,"a":"75175612514311","b":"1050724294328312","r":["-1224","91","4"],"local":40,"vertices":[["-306","22","1"],["-3366","251","11"]],"sides":[{"side":1,"supports":30,"events":["1,13,13","172,1989,8073","19,245,249","22,296,55","326,4489,815","36,469,480","36,479,90","4,55,10","54,697,720","6,80,15","98,1327,245"]},{"side":-1,"supports":30,"events":["1,13,13","1,7,149","10,129,131","115,1431,3054","12,113,1135","12,139,563","12,163,30","129,1662,1720","15,104,2236","16,179,887","25,261,1725","28,373,70","3,38,79","300,3339,16591","32,427,80","33,313,3119","334,4469,835","35,244,5216","4,49,107","4,55,10","554,7429,1385","58,679,2714","6,79,80","73,942,956","8,93,375","838,11438,2095","86,1173,215","87,835,8213","88,981,4853","9,101,497","9,116,120"]}]}];
console.log(JSON.stringify(replay(data,rows),null,2));
```

## Actual output

```json
{
  "output": [
    {
      "i": 1389,
      "side": 1,
      "supports": 30,
      "events": 11,
      "distinct": 11,
      "results": [
        {
          "kind": "open",
          "r": [
            "1550",
            "-57",
            "-14"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1331",
            "-49",
            "-12"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "157289",
            "-5820",
            "-1406"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "155958",
            "-5771",
            "-1394"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "49487",
            "-1832",
            "-442"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "41990",
            "-1557",
            "-374"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "78977",
            "-2932",
            "-702"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "36987",
            "-1375",
            "-328"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "40863",
            "-1520",
            "-362"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3876",
            "-145",
            "-34"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1601",
            "-60",
            "-14"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2528",
            "-95",
            "-22"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6455",
            "-243",
            "-56"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3927",
            "-148",
            "-34"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1618",
            "-61",
            "-14"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "927",
            "-35",
            "-8"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3253",
            "-123",
            "-28"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5579",
            "-211",
            "-48"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "35211",
            "-1334",
            "-302"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "29632",
            "-1123",
            "-254"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4669",
            "-177",
            "-40"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3051",
            "-116",
            "-26"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3287",
            "-125",
            "-28"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 3938,
      "side": 1,
      "supports": 30,
      "events": 11,
      "distinct": 11,
      "results": [
        {
          "kind": "open",
          "r": [
            "-1373940",
            "98963",
            "4490"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1373634",
            "98941",
            "4489"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1390464",
            "100155",
            "4544"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-16830",
            "1214",
            "55"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-28152",
            "2055",
            "92"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-67626",
            "4951",
            "221"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-236844",
            "17347",
            "774"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-406062",
            "29743",
            "1327"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-549576",
            "40279",
            "1796"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-143514",
            "10536",
            "469"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-147492",
            "10829",
            "482"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-3978",
            "293",
            "13"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-94554",
            "6970",
            "309"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-90576",
            "6677",
            "296"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-303858",
            "22481",
            "993"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-213282",
            "15804",
            "697"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-215424",
            "15963",
            "704"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-2142",
            "159",
            "7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-8874",
            "660",
            "29"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-24480",
            "1821",
            "80"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-171054",
            "12747",
            "559"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-146574",
            "10926",
            "479"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-149940",
            "11177",
            "490"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    }
  ],
  "totalPatterns": 101718,
  "excluded": [
    1389,
    3938
  ],
  "strata": 46
}
```
