# X6 R190 — Fifteen-event rank-two exclusion

2026-11-25. Independent informed static six-pair BRC auxiliary weight research; exact finite necessary-relaxation replay, NOT_REVIEWED. Historical provenance EM-DIRECT-AE5AD5; live execution binding unconfirmed. Current exact read r2-20261125-1211-x6-read SUCCEEDED at 2026-11-25T04:11:55.523994Z, Source 25353998409f4982b9916287820aa91e301e0664, NO_CANONICAL_PUBLICATION_DIRECTORY, native_operational_view_evaluated=false, execution_authorized=false. Gateway identity-only response grants no research authority. No CLAIM or shared owner mutation. P000 V5, ACTIVE worldview and joint relation observer preservation retained. This is an auxiliary weight coefficient study, not native spatial/time dynamics.

## Frozen inputs and argument

R189@634ae9241c6989b85e16f9bb123777a954af8d9a (blob 63ca77a94ca7aec2ffdb18fd76370a24ec925d8c), inherited frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f; R182 side census @6945e591116377f9386c7419b6ce31a2b9e8a146 (blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82), R182 single-child theorem @502d7abb2fe8470ed2cdabf242c2cc59a0c302ac. Same Port 10, 1935 unoriented integer directions, six BRC pair denominators, positive weights (17t,B,22t,D), exact optimizer and strict 3/2 near sets. No new direction scoring. Select every census row with min side event count 15 (1261,3578). The inherited theorem makes a child's depth-five necessary endpoint-capacity recursion constant on its own event strata. In the relative interior of a rank-two cone, events are exact ratios |x.u|/|x.v|; distinct event rays and positive sums of adjacent rays cover all 2m+1 strata, including zeros. Actual disconnected support components are clipped before retaining outer endpoints per support. Each representative is checked against original ternary masks, and clipped support counts checked against census. Enumerate endpoint sign patterns and apply the inherited recurrence using BigInt and exact bounded 31-bit support masks. A child with no passing strata excludes its full original root class; this is not a sufficiency claim for six-query trees.

## Actual execution

1261: positive child, 30 supports, 15 distinct events, 31 strata, zero passing. 3578: positive child, 28 supports, 15 distinct events, 31 strata, zero passing. Sum of unique sign-pattern counts across evaluations 85962. Both classes excluded; 62 evaluations total. From R189's reported 209 remaining, now 207 = 119 rank two + 88 rank three (conditional on inherited exclusion bank). Global 6<=D_linear<=7 unchanged. Avoided testing the opposite 39- and 93-event child lists. No new universal theorem or independent review. Activity association pending.

Next min-16 rows: 1716 [35,16], 3487 [16,20], 3503 [46,16], 3539 [56,16], 3588 [16,68]. Select child by actual event count, including negative child. Rank-three exact stratification remains open.

## Standalone reproduction

The following is the pinned R189 replay with only census row selection changed. The equivalent transcribed function was actually run with these rows using exact BigInt; output below is the observed result.

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
const rows=[{"i":1261,"a":"1132515467856","b":"2250667298215343","r":["411","278","-42"],"local":53,"vertices":[["24","22","-3"],["387","256","-39"]],"sides":[{"side":1,"supports":30,"events":["1,12,92","1,18,138","1,28,206","13,639,4377","2,105,747","2,57,411","23,285,2107","23,441,3147","23,675,4707","3,27,211","4,15,141","4,49,367","4,75,549","45,1246,9284","5,43,341"]},{"side":-1,"supports":29,"events":["1,52,368","1,56,412","1,9,73","10,63,522","10,81,672","10,90,729","101,901,6953","11,595,4301","1109,12984,102352","1109,20420,152584","1109,31574,227932","127,1103,8683","15,135,1087","16,139,1094","166,1053,8658","17,153,1188","181,2196,16628","2,17,136","216,1319,11317","260,1581,13629","3,170,1258","3,35,277","301,2669,20689","4,201,1395","4,35,274","4,75,549","41,2023,13889","43,88,1004","56,459,3774","57,683,5245","59,1115,8089","59,1739,12067","59,699,5437","607,31060,217832","671,1580,16984","7,340,2312","87,1069,7979","88,1065,8087","9,76,611"]}]},{"i":3578,"a":"408821825543","b":"2251388844376056","r":["-748","58","1"],"local":105,"vertices":[["-38","3","0"],["-8190","635","11"]],"sides":[{"side":1,"supports":28,"events":["1,11,145","1,12,144","108,1379,270","13,132,2376","16,183,8007","175,1649,81583","19,234,4212","2,21,291","3,34,434","338,4283,845","4,39,897","446,5723,1115","54,655,27659","81,935,40681","89,775,40409"]},{"side":-1,"supports":31,"events":["1,10,224","1,10,476","1,11,145","1,11,187","1,11,223","1,11,493","1,12,222","1,12,56","1,12,92","1,9,459","10,121,2219","10,77,4369","103,745,44183","11,122,1594","11,124,1592","1109,12984,102352","113,1372,6516","115,1431,3054","124,829,52037","13,148,2894","13,163,6749","13,88,5474","14,171,966","17,114,7140","17,179,8245","17,205,8687","173,1076,71230","181,2196,16628","19,237,1311","2,17,901","2,21,369","2,23,289","20,243,927","209,1700,92854","21,263,1921","23,233,5149","23,285,2107","23,287,3301","24,233,11305","245,2972,13752","248,2747,46471","25,228,11526","25,288,2312","25,308,1408","25,308,4840","256,2779,47687","263,3132,58410","289,3622,150008","29,324,5448","293,3638,151504","295,3669,27011","3,32,436","3,34,434","3,34,668","3,35,277","31,384,1748","37,340,17102","37,436,18734","38,433,3519","4,39,897","4,49,185","4,49,367","43,348,19074","47,410,21352","47,540,4348","49,610,4486","49,610,7034","53,628,7640","55,476,24922","57,683,5245","59,699,5437","601,4402,258740","605,4418,260236","61,634,13640","61,660,11352","63,775,9053","7,76,1016","7,80,1558","7,80,648","7,87,1359","717,9079,102773","73,826,6766","76,935,4411","76,941,3505","83,1012,4796","87,1069,7979","88,1065,8087","9,113,823","9,68,3910","9,88,1628","9,98,1678","93,850,42908","94,961,17213"]}]}];
console.log(JSON.stringify(replay(data,rows),null,2));
```

## Actual output

```json
{
  "output": [
    {
      "i": 1261,
      "side": 1,
      "supports": 30,
      "events": 15,
      "distinct": 15,
      "results": [
        {
          "kind": "open",
          "r": [
            "399",
            "346",
            "-48"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "774",
            "670",
            "-93"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "29191",
            "24632",
            "-3447"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "57608",
            "48594",
            "-6801"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "57863",
            "48808",
            "-6831"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "255",
            "214",
            "-30"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1589",
            "1292",
            "-183"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1334",
            "1078",
            "-153"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6719",
            "5244",
            "-753"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5385",
            "4166",
            "-600"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1967",
            "1520",
            "-219"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "516",
            "394",
            "-57"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1119",
            "848",
            "-123"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2841",
            "2150",
            "-312"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4520",
            "3406",
            "-495"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1679",
            "1256",
            "-183"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5294",
            "3918",
            "-573"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3615",
            "2662",
            "-390"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "362",
            "266",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "367",
            "264",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "372",
            "262",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2237",
            "1570",
            "-234"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "37544",
            "25778",
            "-3873"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "35307",
            "24208",
            "-3639"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "991",
            "678",
            "-102"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "36045",
            "24608",
            "-3705"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "29259",
            "19928",
            "-3003"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "22473",
            "15248",
            "-2301"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "17949",
            "12128",
            "-1833"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "13425",
            "9008",
            "-1365"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1151",
            "772",
            "-117"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 3578,
      "side": 1,
      "supports": 28,
      "events": 15,
      "distinct": 15,
      "results": [
        {
          "kind": "open",
          "r": [
            "-27880",
            "2200",
            "1"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-27842",
            "2197",
            "1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-61576",
            "4856",
            "5"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-341614",
            "26939",
            "29"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-189644",
            "14954",
            "17"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-37674",
            "2969",
            "5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-270250",
            "21285",
            "48"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-502826",
            "39601",
            "91"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-399886",
            "31491",
            "75"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-296946",
            "23381",
            "59"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-99814",
            "7859",
            "20"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-2496",
            "196",
            "1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1012230",
            "79315",
            "568"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-3034194",
            "237749",
            "1703"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-189114",
            "14809",
            "115"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1504542",
            "117667",
            "1057"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1549442",
            "121177",
            "1090"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-44900",
            "3510",
            "33"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-47422",
            "3707",
            "35"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-2522",
            "197",
            "2"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-3536",
            "276",
            "3"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1014",
            "79",
            "1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-5590",
            "435",
            "6"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-32526",
            "2531",
            "35"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1838",
            "143",
            "2"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-6072",
            "472",
            "7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-20422",
            "1587",
            "24"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-14350",
            "1115",
            "17"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-7568",
            "588",
            "9"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-786",
            "61",
            "1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-748",
            "58",
            "1"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    }
  ],
  "totalPatterns": 85962,
  "excluded": [
    1261,
    3578
  ],
  "strata": 62
}
```
