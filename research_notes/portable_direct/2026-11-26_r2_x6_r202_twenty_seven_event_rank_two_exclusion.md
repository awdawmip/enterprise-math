# X6 R202 — Twenty-seven-event rank-two exclusion replay

2026-11-26 (Asia/Shanghai). AUTHOR EXACT FINITE NECESSARY-RELAXATION REPLAY / NOT_REVIEWED. Independent informed static BRC auxiliary weight research; current researcher identity unconfirmed, historical predecessor EM-DIRECT-AE5AD5. Native read r2-20261126-0013-x6-read SUCCEEDED 2026-11-25T16:13:44.113005Z, Source b12ce84e48cb428abcaf9a8eea5ea5e5d649c68b, NO_CANONICAL_PUBLICATION_DIRECTORY, execution_authorized=false, native_operational_view_evaluated=false. Owner status unknown; no CLAIM, formal Result or review.

## Scope and proof

Reuse R201@8884f32f402f19fe74d07536643d647cba13427f:research_notes/portable_direct/2026-11-25_r2_x6_r201_twenty_six_event_rank_two_exclusion.md, R182 theorem@502d7abb2fe8470ed2cdabf242c2cc59a0c302ac:research_notes/portable_direct/2026-11-25_r2_x6_r182_one_child_event_refinement.md and census@6945e591116377f9386c7419b6ce31a2b9e8a146:research_notes/portable_direct/x6_r182_rank_two_side_census.json (blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82). Frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f: Port 10, 1935 unoriented integer directions, four positive weights w=(17t,B,22t,D), six joint BRC pair denominators, strict 3/2 near-direction set. P000 V5 and joint relation observer preservation. Auxiliary coefficient chart, not native spatial geometry/dynamics; no fresh physical or classical reference computation. R182 proves that the fixed-endpoint depth-five necessary relaxation is constant on each labeled ternary determinant stratum of one child. In rank two r=alpha*u+beta*v with alpha,beta>0; event locations beta/alpha=|x dot u|/|x dot v|. Exact equality strata and open intervals are represented separately. Equal cuts coalesced without erasing source event identities. If all strata of either child fail, the root class is excluded. Passing does not prove a tree. Executed function matches pinned R201 modulo whitespace; input is full min-27 tranche from frozen census. Exact BigInt geometry and finite bit masks.

## Executed result

```json
[
  {
    "id": 1208,
    "side": 1,
    "supports": 31,
    "events": 27,
    "distinct": 27,
    "strata": 55,
    "passing": 0
  },
  {
    "id": 1481,
    "side": 1,
    "supports": 29,
    "events": 27,
    "distinct": 26,
    "strata": 53,
    "passing": 0
  }
]
```

Total 108 strata; sum of distinct observation pattern counts 162466; newly excluded [1208,1481]. Conditional on inherited R201, remaining 166 = 78 rank two + 88 rank three. Bound 6<=D_linear<=7 unchanged. Next min-28 rows: [{"id":1508,"events":[[1,52],[-1,28]]},{"id":1945,"events":[[1,34],[-1,28]]},{"id":2752,"events":[[1,28],[-1,36]]},{"id":3246,"events":[[1,28],[-1,45]]}]. Activity association and independent review outstanding.

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
const rows=[{"i":1208,"a":"1510472548423","b":"2250289341136792","r":["-2053","261","-4"],"local":100,"vertices":[["-9","1","0"],["-4097","521","-8"]],"sides":[{"side":1,"supports":31,"events":["1,11,223","1,11,493","115,1513,60911","12,97,30","13,116,391","13,132,2376","135,1787,71689","14,121,35","16,183,8007","17,159,3039","175,1649,81583","178,1550,8863","19,169,325","197,3281,116059","2,17,61","267,2195,4747","3,25,53","3,38,1564","3,40,1598","4,35,121","4,35,199","4,39,897","526,4202,1315","54,655,27659","55,872,31654","81,935,40681","89,749,2722"]},{"side":-1,"supports":27,"events":["1,10,146","1,10,224","1,10,476","1,17,1127","1,17,1153","1,17,1738","1,17,1907","1,17,1972","1,17,646","1,17,711","1,17,763","1,17,815","1,17,867","1,17,945","1,17,984","11,187,9992","121,1108,21512","13,120,1232","13,163,6749","15,127,263","16,272,13651","17,179,8245","17,205,8687","173,1560,16432","189,1907,27577","19,180,2784","2,21,369","2,34,1383","2,34,1955","215,1952,20408","226,1879,565","23,233,5149","23,317,12427","24,233,11305","25,228,11526","289,3622,150008","293,3638,151504","3,28,440","3,51,1951","3,51,2081","3,51,2516","3,51,3797","3,51,4343","3,51,6059","3,51,6605","37,340,17102","37,436,18734","38,563,21199","4,39,897","4,68,3247","43,400,6308","5,85,3077","53,867,30957","58,485,145","58,518,145","59,496,1038","6,102,5423","61,634,13640","618,5653,58619","7,102,3876","8,136,10355","8,136,6533","814,6647,2035","83,800,12148","9,153,11170","9,153,11222","9,153,17956","9,153,18008","9,153,6646","9,153,6698","9,88,1628","93,850,42908","94,961,17213","98,782,245"]}]},{"i":1481,"a":"1132515469840","b":"2250667298215343","r":["543","323","-50"],"local":88,"vertices":[["387","256","-39"],["156","67","-11"]],"sides":[{"side":1,"supports":29,"events":["1,30,204","1005,1773,23371","1017,1977,23711","1320,3039,34180","1362,2883,33682","15,33,385","159,366,4117","1629,2670,37814","1641,3030,38206","1770,3381,44290","1938,4323,49874","31,58,748","4,15,141","426,759,10186","44,71,1034","462,1065,11966","465,729,10783","477,861,11099","5658,13047,146554","5754,10917,134063","5778,11793,134899","665,1097,15686","693,1167,16097","876,1695,21274","9,175,1229","9,179,1225","9510,21327,238106"]},{"side":-1,"supports":29,"events":["10,25,287","10,63,522","1024,2293,26372","1049,2057,24463","106,187,2465","107,170,2482","11,510,3366","1141,2761,29843","1259,3041,32917","1579,2992,38192","1613,3179,40579","166,1053,8658","181,271,4202","181,3600,24636","1883,4142,46948","191,380,4456","2,5,55","203,410,4972","205,421,5195","21,263,1921","239,500,5896","241,511,6143","2567,5042,62524","2593,5185,65399","277,556,6776","284,527,7072","284,689,7432","317,578,7378","319,544,7412","35,68,816","359,800,8976","361,811,9303","368,731,8585","369,1307,13084","37,1765,11867","37,73,863","4169,8408,102080","4195,8551,106165","43,88,1056","469,901,10931","49,610,4486","49,976,6668","547,880,12848","556,1123,14048","56,101,1342","5743,11530,140492","5801,11849,146863","641,1037,14875","673,1591,17519","7,16,176","73,109,1691","73,163,1826","79,187,2057","8,17,204","805,1408,19184","821,1496,20383","83,306,2931","88,1741,11987","9,113,823","9064,14743,213290","9473,21029,243559"]}]}];
console.log(JSON.stringify(replay(data,rows),null,2));
```

## Actual full output

```json
{
  "output": [
    {
      "i": 1208,
      "side": 1,
      "supports": 31,
      "events": 27,
      "distinct": 27,
      "results": [
        {
          "kind": "open",
          "r": [
            "-306115",
            "34317",
            "-37"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-612221",
            "68633",
            "-74"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-205762",
            "23068",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-5065",
            "571",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-14646",
            "1652",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-9581",
            "1081",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-12583",
            "1431",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-15585",
            "1781",
            "-6"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-2401",
            "275",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-3623",
            "419",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1762",
            "204",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-5187",
            "601",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-6913",
            "801",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-8639",
            "1001",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1690",
            "196",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1501",
            "175",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-30011",
            "3499",
            "-20"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-58521",
            "6823",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-10156",
            "1186",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-296939",
            "34687",
            "-206"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-6632",
            "778",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-200461",
            "23663",
            "-169"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-40297",
            "4757",
            "-34"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1024",
            "122",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-437261",
            "52523",
            "-479"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-436237",
            "52401",
            "-478"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-48287",
            "5801",
            "-53"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-46633",
            "5609",
            "-52"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-11611",
            "1397",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-11422",
            "1376",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-12221",
            "1473",
            "-14"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-799",
            "97",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-12415",
            "1511",
            "-16"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-11616",
            "1414",
            "-15"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-12325",
            "1501",
            "-16"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-709",
            "87",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-2082",
            "256",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1373",
            "169",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-18153",
            "2239",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-34933",
            "4309",
            "-52"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-35561",
            "4387",
            "-53"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-628",
            "78",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1821",
            "227",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-1193",
            "149",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1785",
            "223",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-7732",
            "966",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-22809",
            "2855",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-220358",
            "27584",
            "-377"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-68013",
            "8519",
            "-117"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-119707",
            "15011",
            "-208"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-20941",
            "2631",
            "-37"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-299113",
            "37609",
            "-532"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-110085",
            "13909",
            "-204"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-801737",
            "101481",
            "-1508"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-402917",
            "51001",
            "-758"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 1481,
      "side": 1,
      "supports": 29,
      "events": 27,
      "distinct": 26,
      "results": [
        {
          "kind": "open",
          "r": [
            "1155",
            "761",
            "-116"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "30798",
            "20291",
            "-3093"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "234063",
            "146125",
            "-22452"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "671391",
            "418084",
            "-64263"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "224784",
            "139957",
            "-21513"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2961",
            "1787",
            "-276"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "204",
            "123",
            "-19"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "507",
            "304",
            "-47"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "209625",
            "122076",
            "-18961"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "418743",
            "243848",
            "-37875"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "18873",
            "10990",
            "-1707"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "34209",
            "19912",
            "-3093"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "22023",
            "12802",
            "-1989"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "97929",
            "56900",
            "-8841"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "432",
            "251",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11799",
            "6854",
            "-1065"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "155031",
            "89939",
            "-13978"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "453294",
            "262963",
            "-40869"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "185835",
            "107753",
            "-16748"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "104211",
            "60296",
            "-9375"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "104289",
            "60341",
            "-9382"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "78",
            "45",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "150657",
            "83893",
            "-13126"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "150579",
            "83848",
            "-13119"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "53649",
            "29873",
            "-4674"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "10368",
            "5771",
            "-903"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1827",
            "1016",
            "-159"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "594",
            "325",
            "-51"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "717",
            "388",
            "-61"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1557",
            "839",
            "-132"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "76068",
            "40009",
            "-6321"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "74511",
            "39170",
            "-6189"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "39504",
            "20719",
            "-3275"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "44001",
            "22987",
            "-3636"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "44211",
            "23094",
            "-3653"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "210",
            "107",
            "-17"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "705",
            "351",
            "-56"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "495",
            "244",
            "-39"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "6633",
            "3242",
            "-519"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "39303",
            "19208",
            "-3075"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "65133",
            "31265",
            "-5022"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "156096",
            "74587",
            "-11991"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "107139",
            "50809",
            "-8180"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "165321",
            "77840",
            "-12549"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "170358",
            "80163",
            "-12925"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "5037",
            "2323",
            "-376"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "14205",
            "6487",
            "-1052"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "23373",
            "10651",
            "-1728"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "24036",
            "10953",
            "-1777"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "663",
            "302",
            "-49"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "501",
            "228",
            "-37"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "339",
            "154",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "495",
            "221",
            "-36"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    }
  ],
  "totalPatterns": 162466,
  "excluded": [
    1208,
    1481
  ],
  "strata": 108
}
```
