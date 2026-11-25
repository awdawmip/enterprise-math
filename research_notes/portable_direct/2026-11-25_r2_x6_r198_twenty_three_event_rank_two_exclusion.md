# X6 R198 — Twenty-three-event rank-two exclusion replay

2026-11-25. AUTHOR EXACT FINITE NECESSARY-RELAXATION REPLAY / NOT_REVIEWED. Independent informed static BRC auxiliary weight research. Current execution binding unconfirmed; historical predecessor EM-DIRECT-AE5AD5. Control request r2-20261125-2008-x6-read SUCCEEDED, observed 2026-11-25T12:08:18.483258Z, Source e945e2a81222c2cf259d26a5cf3e7fbed8a3ac7e, NO_CANONICAL_PUBLICATION_DIRECTORY, execution_authorized=false, native_operational_view_evaluated=false. No CLAIM or formal result/review.

## Frozen scope and method

R197@ff3c930e1322ad37672b8f16d4f8db4a6b3cdb69, blob 9de32b4741bc90ed81bc661854f462407e77b2bf; R182 side census@6945e591116377f9386c7419b6ce31a2b9e8a146, blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82; R182 one-child theorem@502d7abb2fe8470ed2cdabf242c2cc59a0c302ac. R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f remain frozen: Port 10, 1935 unoriented integer directions, six BRC denominators, w=(17t,B,22t,D), exact optimum and strict 3/2 near set. P000 V5, ACTIVE worldview, joint-relation preservation. Auxiliary coefficient chart, not native dynamics. R182 proves child-specific constancy of fixed-endpoint depth-five necessary relaxation on its own event strata. Preserve equality points, open intervals, actual component clipping, labeled support incidence; coalesce identical event rays without discarding relation labels. Uniform failure in one child excludes root; a pass is necessary only. Executed function matched R197 pinned source modulo whitespace, and rows match complete min-23 census tranche. Exact BigInt geometry and finite bit masks.

## Executed result

```json
[
  {
    "id": 893,
    "side": 1,
    "supports": 29,
    "events": 23,
    "distinct": 23,
    "strata": 47,
    "passing": 0
  },
  {
    "id": 1213,
    "side": 1,
    "supports": 29,
    "events": 23,
    "distinct": 20,
    "strata": 41,
    "passing": 0
  },
  {
    "id": 2967,
    "side": -1,
    "supports": 27,
    "events": 23,
    "distinct": 22,
    "strata": 45,
    "passing": 0
  },
  {
    "id": 3117,
    "side": -1,
    "supports": 29,
    "events": 23,
    "distinct": 23,
    "strata": 47,
    "passing": 0
  }
]
```

Total 180 strata; sum of distinct pattern counts 281182; newly excluded [893,1213,2967,3117]. Conditional on inherited R197: remaining 172 = 84 rank two + 88 rank three. 6<=D_linear<=7 unchanged. Nonexcluded rows remain unresolved. Next min-24 census rows: [{"id":3265,"events":[[1,24],[-1,27]]}]. Activity association and independent review not claimed.

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
const rows=[{"i":893,"a":"1115201468952","b":"2250684477998567","r":["692","77","-23"],"local":99,"vertices":[["806","101","-29"],["578","53","-17"]],"sides":[{"side":1,"supports":29,"events":["1,1,35","103,238,3740","11,17,391","11,2,376","1204,59715,237790","142,6977,28045","19,28,674","19,28,713","1954,97373,385915","2,99,395","206,10327,40685","3,7,110","352,18407,69520","358,18605,70705","412,367,14375","42,2077,8295","6,305,1185","62,3147,12245","8,13,299","81,2392,10244","82,4033,16195","92,4575,18170","93,2828,12136"]},{"side":-1,"supports":28,"events":["1,1,35","1,2,36","1,2,37","1,29,127","10,63,522","10,66,519","1007,119,34357","101,194,3628","1049,2057,37723","107,170,3808","107,3290,14362","11,17,391","11,21,395","11,336,1452","11,8,382","110,271,4019","113,68,3910","115,268,4178","115,34,3944","12,17,425","12,355,1517","128,833,6655","139,153,4879","149,4563,19797","149,54,5120","1619,323,55369","166,1053,8658","17,23,601","17,32,610","17,6,584","173,10,5892","19,28,713","19,37,704","19,39,702","192,23,6551","2,3,75","20,11,691","20,47,727","21,46,760","215,119,7429","216,1319,11317","233,394,8693","241,561,8755","25,43,893","260,1581,13629","27,823,3545","281,98,9652","293,167,10129","3,1,103","3,5,112","3,7,110","304,371,11485","32,945,4047","329,62,11248","344,119,11815","35,68,1258","369,734,13657","37,34,1292","38,17,1309","4,27,207","41,5,1399","479,164,16450","5,11,184","5,2,172","508,1187,18625","51,4,1738","563,140,19282","61,594,3894","641,1037,22831","67,1917,8535","67,31,2309","7,13,260","76,187,2771","76,2295,9741","8,13,299","8,17,295","8,19,293","803,272,27574","83,32,2854","85,154,3044","9,16,335"]}]},{"i":1213,"a":"1510472548359","b":"2250289341136824","r":["-525","66","-1"],"local":96,"vertices":[["-9","1","0"],["-2091","263","-4"]],"sides":[{"side":1,"supports":29,"events":["1,11,223","1,11,493","115,1513,60911","12,97,30","13,116,391","13,132,2376","135,1787,71689","14,121,35","16,183,8007","17,159,3039","175,1649,81583","19,169,325","197,3281,116059","2,17,61","3,25,53","3,38,1564","3,40,1598","4,35,121","4,35,199","4,39,897","54,655,27659","55,872,31654","81,935,40681"]},{"side":-1,"supports":28,"events":["1,10,146","1,10,224","1,10,476","1,17,1127","1,17,1153","1,17,1738","1,17,1907","1,17,1972","1,17,646","1,17,711","1,17,763","1,17,815","1,17,867","1,17,945","1,17,984","11,187,9992","121,1108,21512","13,120,1232","13,163,6749","15,127,263","16,272,13651","17,179,8245","17,205,8687","173,1560,16432","189,1907,27577","19,180,2784","2,21,369","2,34,1383","2,34,1955","215,1952,20408","226,1879,565","23,233,5149","23,317,12427","24,233,11305","25,228,11526","289,3622,150008","293,3638,151504","3,28,440","3,34,668","3,51,1951","3,51,2081","3,51,2516","3,51,3797","3,51,4343","3,51,6059","3,51,6605","37,340,17102","37,436,18734","38,563,21199","4,39,897","4,68,3247","43,400,6308","5,85,3077","53,867,30957","58,485,145","58,518,145","59,496,1038","6,102,5423","61,634,13640","618,5653,58619","7,102,3876","8,136,10355","8,136,6533","814,6647,2035","83,800,12148","9,153,11170","9,153,11222","9,153,17956","9,153,18008","9,153,6646","9,153,6698","9,88,1628","93,850,42908","94,961,17213"]}]},{"i":2967,"a":"898317676969752","b":"1353482136191207","r":["166","1","-3"],"local":72,"vertices":[["61","0","-1"],["1599","10","-29"]],"sides":[{"side":1,"supports":28,"events":["1,1005,126","1,191,87","1,193,87","1,238,126","1,255,87","1,278,126","1,310,126","1,459,126","1,459,87","1,99,87","10,4187,1975","10,4694,1975","12,893,940","15,1802,1305","15,2491,1175","15,3128,1890","17,4839,1479","17,8739,2142","183,15245,14335","2,1019,395","2,1049,395","2,1666,395","2,4012,395","2,875,395","20,2979,1740","20,5241,2520","25,4611,2175","25,6678,3150","27,3995,2115","3,1013,235","3,221,235","3,235,235","3,493,261","3,501,235","3,515,235","3,599,235","3,629,235","3,701,235","34,31778,6715","4,825,504","45,4522,3525","5,1111,435","5,1618,630","57,4700,4465","6,451,470","60,7429,4700","61,5645,5307","7,72,420","9,120,544"]},{"side":-1,"supports":27,"events":["1,119,87","1,147,87","1,209,126","1,225,87","1,264,126","1,264,87","1,340,126","1,5256,126","1,8103,87","15,198,902","18,187,1067","2,1243,395","2,968,395","27,2240,2115","3,233,235","3,26207,235","3,467,235","3,493,235","3,805,235","3,896,235","6,4471,1185","651,49859,50995","9,629,705"]}]},{"i":3117,"a":"909991667171320","b":"1341808142319623","r":["388","-21","-2"],"local":62,"vertices":[["192","-10","-1"],["7956","-431","-41"]],"sides":[{"side":1,"supports":31,"events":["10,183,25","110,2039,275","114,2159,285","12,221,30","123,2193,1025","124,2279,310","135,2374,1710","14,171,966","14,187,803","14,264,35","154,2907,385","158,2907,395","160,2941,400","168,3085,1400","2,33,45","2,37,5","21,373,175","27,472,360","27,493,225","280,4929,2520","288,629,49096","29,519,261","3,40,172","3,49,68","3,53,27","3,53,38","3,53,40","31,549,279","33,313,3119","394,7264,985","394,7439,985","4,59,175","45,817,405","614,11440,1535","69,1258,575","74,1075,3254","807,14309,6725","87,835,8213","9,164,81"]},{"side":-1,"supports":29,"events":["10,131,571","12,211,152","132,2363,1672","16,231,705","16,233,703","16,285,144","176,3213,1584","213,3740,2698","22,413,55","24,353,1051","24,421,320","264,4709,3520","284,5049,2556","32,415,1907","352,6647,880","38,555,1668","426,7463,5680","48,857,400","528,9673,4400","609,10561,8120","734,13726,1835","852,15181,7100","87,1511,1102"]}]}];
console.log(JSON.stringify(replay(data,rows),null,2));
```

## Actual output

```json
{
  "output": [
    {
      "i": 893,
      "side": 1,
      "supports": 29,
      "events": 23,
      "distinct": 23,
      "results": [
        {
          "kind": "open",
          "r": [
            "7280",
            "887",
            "-257"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "42874",
            "5221",
            "-1513"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "13223",
            "1607",
            "-466"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "10018",
            "1207",
            "-351"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7915",
            "952",
            "-277"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5812",
            "697",
            "-203"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7073",
            "848",
            "-247"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1261",
            "151",
            "-44"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "40945",
            "4792",
            "-1407"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "39684",
            "4641",
            "-1363"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "19915",
            "2329",
            "-684"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "146",
            "17",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9869",
            "1139",
            "-336"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "88675",
            "10234",
            "-3019"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5927",
            "680",
            "-201"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "89135",
            "10166",
            "-3011"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "236127",
            "26775",
            "-7946"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "146992",
            "16609",
            "-4935"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2715",
            "306",
            "-91"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "15908",
            "1751",
            "-525"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9246",
            "1017",
            "-305"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2584",
            "283",
            "-85"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5803",
            "631",
            "-190"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "9022",
            "979",
            "-295"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2345",
            "251",
            "-76"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5048",
            "527",
            "-161"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "817",
            "85",
            "-26"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6390",
            "663",
            "-203"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6517",
            "676",
            "-207"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "127",
            "13",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "39851",
            "4058",
            "-1251"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "39724",
            "4045",
            "-1247"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "126085",
            "12757",
            "-3942"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "212446",
            "21469",
            "-6637"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8323",
            "841",
            "-260"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3952",
            "397",
            "-123"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "453",
            "45",
            "-14"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1937",
            "188",
            "-59"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "33987",
            "3231",
            "-1022"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "32050",
            "3043",
            "-963"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "33003",
            "3120",
            "-989"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "33956",
            "3197",
            "-1015"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "20087",
            "1889",
            "-600"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6218",
            "581",
            "-185"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "425787",
            "39477",
            "-12608"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "419569",
            "38896",
            "-12423"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "420147",
            "38949",
            "-12440"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 1213,
      "side": 1,
      "supports": 29,
      "events": 23,
      "distinct": 20,
      "results": [
        {
          "kind": "open",
          "r": [
            "-310242",
            "34755",
            "-37"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-310233",
            "34754",
            "-37"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-157359",
            "17630",
            "-19"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-4485",
            "506",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-8853",
            "999",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-4368",
            "493",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-3549",
            "402",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-2730",
            "311",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-4569",
            "523",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1839",
            "212",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-3633",
            "419",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1794",
            "207",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-4914",
            "569",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-8034",
            "931",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-4779",
            "554",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1524",
            "177",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-152331",
            "17723",
            "-104"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-150807",
            "17546",
            "-103"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-152133",
            "17701",
            "-104"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1326",
            "155",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-8499",
            "998",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-15672",
            "1841",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-4521",
            "533",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-11454",
            "1357",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-46671",
            "5569",
            "-50"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-221901",
            "26488",
            "-239"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-80658",
            "9629",
            "-87"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-20073",
            "2399",
            "-22"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-20967",
            "2506",
            "-23"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-894",
            "107",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-831",
            "100",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-4092",
            "493",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-786",
            "95",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-624",
            "77",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-597",
            "74",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-17286",
            "2143",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-23709",
            "2941",
            "-40"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-6423",
            "798",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-37890",
            "4739",
            "-69"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-31467",
            "3941",
            "-58"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-16779",
            "2102",
            "-31"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 2967,
      "side": -1,
      "supports": 27,
      "events": 23,
      "distinct": 22,
      "results": [
        {
          "kind": "open",
          "r": [
            "30727",
            "1",
            "-504"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "30666",
            "1",
            "-503"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "24810",
            "1",
            "-407"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "18954",
            "1",
            "-311"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7242",
            "1",
            "-119"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "24498",
            "5",
            "-403"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3155",
            "1",
            "-52"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3897",
            "4",
            "-65"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2816",
            "3",
            "-47"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1735",
            "2",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "715",
            "1",
            "-12"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1125",
            "2",
            "-19"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "532",
            "1",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1003",
            "2",
            "-17"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1474",
            "3",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "471",
            "1",
            "-8"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "253057",
            "820",
            "-4377"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "252586",
            "819",
            "-4369"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "126437",
            "410",
            "-2187"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "288",
            "1",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9443",
            "33",
            "-164"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "18598",
            "65",
            "-323"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3395",
            "12",
            "-59"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1772",
            "7",
            "-31"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1257",
            "5",
            "-22"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3256",
            "13",
            "-57"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3073",
            "13",
            "-54"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2890",
            "13",
            "-51"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4811",
            "22",
            "-85"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6732",
            "31",
            "-119"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "14477",
            "67",
            "-256"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7745",
            "36",
            "-137"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8819",
            "41",
            "-156"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1074",
            "5",
            "-19"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1467",
            "7",
            "-26"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "393",
            "2",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "14070",
            "73",
            "-251"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "41817",
            "217",
            "-746"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1345",
            "7",
            "-24"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "52333",
            "273",
            "-934"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1511",
            "8",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6596",
            "39",
            "-119"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "17203",
            "104",
            "-311"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "10607",
            "65",
            "-192"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "12206",
            "75",
            "-221"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 3117,
      "side": -1,
      "supports": 29,
      "events": 23,
      "distinct": 23,
      "results": [
        {
          "kind": "open",
          "r": [
            "9028",
            "-471",
            "-47"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "53976",
            "-2816",
            "-281"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "101616",
            "-5302",
            "-529"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "352488",
            "-18392",
            "-1835"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "32464",
            "-1694",
            "-169"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "37080",
            "-1936",
            "-193"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "744888",
            "-38896",
            "-3877"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1452696",
            "-75856",
            "-7561"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "34776",
            "-1816",
            "-181"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "77448",
            "-4048",
            "-403"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8460",
            "-443",
            "-44"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "49452",
            "-2597",
            "-257"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9044",
            "-475",
            "-47"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4812",
            "-253",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "18304",
            "-966",
            "-95"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "159924",
            "-8441",
            "-830"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7900",
            "-417",
            "-41"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5976",
            "-316",
            "-31"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8484",
            "-449",
            "-44"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2508",
            "-133",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7332",
            "-389",
            "-38"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4824",
            "-256",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7528",
            "-400",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "85512",
            "-4544",
            "-443"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "19496",
            "-1036",
            "-101"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "31464",
            "-1672",
            "-163"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "46140",
            "-2453",
            "-239"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "14676",
            "-781",
            "-76"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "23376",
            "-1246",
            "-121"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "55452",
            "-2957",
            "-287"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "43872",
            "-2342",
            "-227"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "32292",
            "-1727",
            "-167"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "35580",
            "-1903",
            "-184"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3288",
            "-176",
            "-17"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "65976",
            "-3536",
            "-341"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "128664",
            "-6896",
            "-665"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "31152",
            "-1670",
            "-161"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "58248",
            "-3124",
            "-301"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "89616",
            "-4810",
            "-463"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "120984",
            "-6496",
            "-625"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1200048",
            "-64450",
            "-6199"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2279112",
            "-122404",
            "-11773"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "59628",
            "-3203",
            "-308"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "225264",
            "-12122",
            "-1163"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "5036",
            "-271",
            "-26"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1356",
            "-73",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "388",
            "-21",
            "-2"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    }
  ],
  "totalPatterns": 281182,
  "excluded": [
    893,
    1213,
    2967,
    3117
  ],
  "strata": 180
}
```
