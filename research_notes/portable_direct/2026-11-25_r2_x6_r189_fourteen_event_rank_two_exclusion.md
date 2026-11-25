# X6 R189 — fourteen-event rank-two replay

2026-11-25. Independent informed static six-pair BRC auxiliary weight study, author calculation, NOT_REVIEWED. Historical lane provenance EM-DIRECT-AE5AD5, live execution binding unconfirmed. Exact X6 read r2-20261125-1112-x6-read SUCCEEDED at 2026-11-25T03:12:58.331762Z, Source db5103b44e0e7b13afdf1ff2cd142466714dbd5f, NO_CANONICAL_PUBLICATION_DIRECTORY; native owner projection not evaluated and execution_authorized=false. No CLAIM or owner mutation. P000 V5, ACTIVE worldview and joint relation observer preservation retained. Auxiliary weight coefficient space is not a native spatial or dynamical model.

Frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f inherited via R188@0fb828189e6bf385c867c5faccead1f5882fb181 (blob 37623dab2c58cef74a94c6f50574466aab685b1e). Port 10, 1935 unoriented directions, six pair BRC observers, weights (17t,B,22t,D), exact optimum and strict 3/2 near set. Embedded support bank read from R188 and R182 side census pinned at 6945e591116377f9386c7419b6ce31a2b9e8a146:research_notes/portable_direct/x6_r182_rank_two_side_census.json (blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82). All census rows with min side event count 14 selected; no rescoring. Reuse R182 single-child sufficient event theorem and R178/R188 endpoint capacity necessary relaxation. Every varying event x in a rank-two cone with generators u,v occurs at ratio |x.u|/|x.v|; exact event rays and intervening positive sums represent every relative stratum including equality. Clip disconnected support components before extracting outer endpoints, check class masks and support counts, enumerate endpoint sign patterns and test depth-five necessary capacity recursion. A side with no passing strata excludes its entire root class. Passing is necessary relaxation feasibility only. BigInt exact arithmetic; bounded 31-bit support masks. No new general theorem or independent review.

## Actual execution

- 51: side 1, supports 29, events 14, strata 29, passing 0, excluded true
- 764: side 1, supports 31, events 14, strata 29, passing 0, excluded true
- 1499: side 1, supports 29, events 14, strata 29, passing 0, excluded true
- 3651: side 1, supports 28, events 14, strata 29, passing 0, excluded true

Executed JavaScript replay below. Total strata 116; summed unique sign-pattern counts 167646; newly excluded 51, 764, 1499, 3651. Based on R188's 213 remaining, now 209 = 121 rank two + 88 rank three. Global depth remains 6<=D_linear<=7 under inherited proof bank. Activity association pending. Any classes with neither side wholly excluded need exact intersection. Next min-15-event census rows: [{"i":1261,"events":[15,39]},{"i":3578,"events":[15,93]}]. Rank-three strata remain open.

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
const rows=[{"i":51,"a":"1132515426404","b":"2250667298258827","r":["-80","35","-3"],"local":33,"vertices":[["-55","24","-2"],["-25","11","-1"]],"sides":[{"side":1,"supports":29,"events":["1,15,141","10,53,337","111,919,7934","13,112,962","15,127,1082","167,1448,12358","21,179,1519","22,188,1593","23,196,1702","33,287,2407","4,27,207","411,3589,30029","56,459,3774","67,581,4881"]},{"side":-1,"supports":29,"events":["1,15,141","1,1699,18893","10,53,337","10,81,672","101,534,3405","103,1460,14608","11,4624,53108","13,270,2772","173,3510,36972","19,193,1783","19,284,2680","21,11747,133501","33,11815,136697","43,640,6068","49,1000,10466","5,44,370","5,71,709","53,425,3553","54,785,7639","6,61,563","95,809,7030"]}]},{"i":764,"a":"1132515555920","b":"2250667298129319","r":["91","22","-4"],"local":44,"vertices":[["24","5","-1"],["340","83","-15"]],"sides":[{"side":1,"supports":31,"events":["16,89,847","18,383,2425","27,347,2461","3,27,211","3,38,274","41,1624,9500","5,43,341","61,2099,12175","79,3060,17544","8,45,423","83,1098,7534","83,1800,11148","83,2853,16569","9,185,1219"]},{"side":-1,"supports":25,"events":["1,39,225","10,81,672","101,901,6953","11,421,2387","11,434,2530","127,1103,8683","16,139,1094","17,153,1188","179,2367,16249","19,401,2563","19,661,3785","2,17,136","21,263,1921","21,799,4505","22,289,1999","28,1139,6817","3,100,602","3,119,697","3,38,274","301,2669,20689","4,35,274","47,1904,11356","49,1600,9866","56,459,3774","6,34,317","7,90,638","7,93,635","81,1052,7372","87,1901,11671","9,113,823","9,76,611"]}]},{"i":1499,"a":"1132515469840","b":"2250667298149871","r":["10608","3346","-671"],"local":83,"vertices":[["156","67","-11"],["21060","6625","-1331"]],"sides":[{"side":1,"supports":29,"events":["127,1299,8763","18,383,2425","18,397,2411","2,45,267","23,211,1587","25,261,1725","3,40,272","3,41,271","4,15,141","41,1624,9500","5,48,324","61,2099,12175","75,2783,15313","99,3568,19598"]},{"side":-1,"supports":30,"events":["1,22,134","1,35,199","1,36,198","1,38,214","1,39,225","10,25,287","10,63,522","10,66,519","105,3859,21029","11,402,2178","11,421,2387","11,434,2530","121,1114,8174","124,1161,8556","128,833,6655","143,6120,38148","156,1429,10764","166,1053,8658","169,1566,11346","179,2367,16249","181,5706,36648","19,401,2563","19,661,3785","21,799,4505","22,289,1999","22,315,1973","232,2133,16008","24,167,1237","26,185,1336","26,259,1794","27,347,2461","27,628,3584","28,1139,6817","3,100,602","3,119,697","3,40,272","3,41,271","3,61,407","3,67,401","369,1307,13084","4,27,207","41,1700,10336","43,412,2792","47,1904,11356","49,1000,6644","49,1098,6546","49,1585,9881","49,1600,9866","58,567,4002","66,1543,8753","67,981,5987","68,2939,18457","7,102,626","7,157,935","7,295,1817","7,66,462","7,90,638","7,93,635","78,727,5382","79,3060,17544","79,756,5451","81,1052,7372","83,1098,7534","83,1800,11148","83,2853,16569","83,306,2931","87,1901,11671","87,3149,17209","88,2755,17837","9,185,1219","9,289,1817"]}]},{"i":3651,"a":"581658395803160","b":"1670141401104871","r":["746","17","-15"],"local":57,"vertices":[["1301","29","-26"],["1683","39","-34"]],"sides":[{"side":1,"supports":28,"events":["12,4,599","173,11781,21798","29,66,1518","3335,518,165730","346,45584,68335","38,56,1951","4,4,203","45,154,2420","47,182,2554","51,22,2552","51,62,2602","561,322,28172","8,20,421","89,330,4818"]},{"side":-1,"supports":27,"events":["1,2,52","104,60,5223","11,26,577","127,274,6629","133,194,6826","15,22,770","15,38,790","157,290,8134","16,12,807","17,42,894","176,236,9007","18,56,961","1915,5294,101410","193,642,10356","2,135,252","211,550,11132","23,66,1221","25,22,1265","251,614,13192","26,56,1357","281,770,14872","29,66,1518","337,802,17684","401,1266,21432","41,138,2202","43,110,2266","43,146,2311","43,94,2246","463,1114,24311","47,110,2464","49,66,2508","5,6,255","569,586,28898","67,154,3509","67,190,3554","67,198,3564","67,86,3424","673,2354,36256","7,22,374","773,2962,41966","79,22,3938","8,20,421","845,1982,44305","89,230,4693","95,198,4950"]}]}];
console.log(JSON.stringify(replay(data,rows),null,2));
```

## Actual output

```json
{
  "output": [
    {
      "i": 51,
      "side": 1,
      "supports": 29,
      "events": 14,
      "distinct": 14,
      "results": [
        {
          "kind": "open",
          "r": [
            "-35130",
            "15337",
            "-1285"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-35075",
            "15313",
            "-1283"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-42605",
            "18602",
            "-1560"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-7530",
            "3289",
            "-277"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-2945",
            "1287",
            "-109"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-4250",
            "1859",
            "-159"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-9025",
            "3948",
            "-338"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-4775",
            "2089",
            "-179"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-425",
            "186",
            "-16"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-6700",
            "2933",
            "-253"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-715",
            "313",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-450",
            "197",
            "-17"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-27500",
            "12039",
            "-1039"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-54550",
            "23881",
            "-2061"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-61575",
            "26957",
            "-2327"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-7025",
            "3076",
            "-266"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-28525",
            "12503",
            "-1093"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-21500",
            "9427",
            "-827"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-7615",
            "3339",
            "-293"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-16575",
            "7268",
            "-638"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-27175",
            "11917",
            "-1047"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-10600",
            "4649",
            "-409"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-11900",
            "5221",
            "-461"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-132200",
            "58003",
            "-5123"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-132555",
            "58159",
            "-5137"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-355",
            "156",
            "-14"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-985",
            "433",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-630",
            "277",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-655",
            "288",
            "-26"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 764,
      "side": 1,
      "supports": 31,
      "events": 14,
      "distinct": 14,
      "results": [
        {
          "kind": "open",
          "r": [
            "1646",
            "349",
            "-69"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3268",
            "693",
            "-137"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4544",
            "971",
            "-191"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5820",
            "1249",
            "-245"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "49086",
            "10573",
            "-2069"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "92352",
            "19897",
            "-3893"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5100",
            "1099",
            "-215"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "9648",
            "2083",
            "-407"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "12109",
            "2617",
            "-511"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "135660",
            "29321",
            "-5725"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "68547",
            "14819",
            "-2893"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1434",
            "317",
            "-61"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "235",
            "52",
            "-10"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "916",
            "203",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1525",
            "339",
            "-65"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "609",
            "136",
            "-26"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "398",
            "89",
            "-17"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "585",
            "131",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "71637",
            "16138",
            "-3068"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "71052",
            "16007",
            "-3043"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "36027",
            "8117",
            "-1543"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1002",
            "227",
            "-43"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2133",
            "490",
            "-92"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1131",
            "263",
            "-49"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2535",
            "592",
            "-110"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1404",
            "329",
            "-61"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "987",
            "233",
            "-43"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "570",
            "137",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "91",
            "22",
            "-4"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 1499,
      "side": 1,
      "supports": 29,
      "events": 14,
      "distinct": 14,
      "results": [
        {
          "kind": "open",
          "r": [
            "12140",
            "5025",
            "-844"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "48404",
            "20033",
            "-3365"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "48596",
            "20107",
            "-3378"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "192",
            "74",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2644",
            "1003",
            "-178"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7740",
            "2935",
            "-521"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4548",
            "1691",
            "-304"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "10452",
            "3829",
            "-695"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "61296",
            "22222",
            "-4061"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "112140",
            "40615",
            "-7427"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "36552",
            "13084",
            "-2411"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "107172",
            "37889",
            "-7039"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "344916",
            "121187",
            "-22606"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "582660",
            "204485",
            "-38173"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "97552",
            "34234",
            "-6391"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2652",
            "919",
            "-173"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "416",
            "142",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "12324",
            "4193",
            "-799"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6236",
            "2117",
            "-404"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "25092",
            "8509",
            "-1625"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4684",
            "1583",
            "-303"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3012",
            "989",
            "-193"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "828",
            "271",
            "-53"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "66540",
            "21775",
            "-4259"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "431148",
            "139861",
            "-27518"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "795756",
            "257947",
            "-50777"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1306344",
            "422348",
            "-83287"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "510588",
            "164401",
            "-32510"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "531648",
            "171026",
            "-33841"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 3651,
      "side": 1,
      "supports": 28,
      "events": 14,
      "distinct": 14,
      "results": [
        {
          "kind": "open",
          "r": [
            "221812",
            "4945",
            "-4433"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "442323",
            "9861",
            "-8840"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "473183",
            "10550",
            "-9457"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "30860",
            "689",
            "-617"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "19654",
            "439",
            "-393"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8448",
            "189",
            "-169"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1992049",
            "44650",
            "-39871"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1983601",
            "44461",
            "-39702"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2014115",
            "45146",
            "-40313"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "30514",
            "685",
            "-611"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "36291",
            "816",
            "-727"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5777",
            "131",
            "-116"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8813",
            "200",
            "-177"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3036",
            "69",
            "-61"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "32339",
            "740",
            "-651"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "29303",
            "671",
            "-590"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "35011",
            "802",
            "-705"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5708",
            "131",
            "-115"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8883",
            "204",
            "-179"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3175",
            "73",
            "-64"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "459881",
            "10610",
            "-9279"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "456706",
            "10537",
            "-9215"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "124643",
            "2876",
            "-2515"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "41866",
            "967",
            "-845"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "51773",
            "1196",
            "-1045"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "9907",
            "229",
            "-200"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2791575",
            "64614",
            "-56377"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2781668",
            "64385",
            "-56177"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2783351",
            "64424",
            "-56211"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    }
  ],
  "totalPatterns": 167646,
  "excluded": [
    51,
    764,
    1499,
    3651
  ],
  "strata": 116
}
```
