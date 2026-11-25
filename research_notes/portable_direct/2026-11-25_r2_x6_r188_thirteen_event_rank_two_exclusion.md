# X6 R188 — thirteen-event rank-two replay

2026-11-25. Independent informed static six-pair BRC auxiliary weight study, author calculation, NOT_REVIEWED. Historical lane provenance EM-DIRECT-AE5AD5; current execution binding unconfirmed. X6 task read r2-20261125-1010-x6-read SUCCEEDED 2026-11-25T02:10:43.126973Z at Source 05545398eaabfbab490da218f552d0b7fa61250e: NO_CANONICAL_PUBLICATION_DIRECTORY; native_operational_view_evaluated=false, execution_authorized=false. No CLAIM, no owner mutation. P000 V5, ACTIVE worldview and joint relation preservation maintained. Auxiliary coefficient space is not a native spatial or dynamical model.

Frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f inherited via R187@09debd44dcd0d576a4bd34cd3f717609cfda60f6 (blob 0ecb3df1dea57a1609d7a209b3e2bdb9884c81a7). Port 10, 1935 unoriented directions, six pair BRC observers, weights (17t,B,22t,D), exact optimum and strict 3/2 near set. Read exact embedded support bank and R182 side census at 6945e591116377f9386c7419b6ce31a2b9e8a146:research_notes/portable_direct/x6_r182_rank_two_side_census.json (blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82). All census rows with min side event count 13 selected. No new direction scoring. Reuse R182 single-child sufficient event theorem and R178/R187 endpoint capacity necessary relaxation: for rank-two cone with generators u,v, each varying event x occurs at ratio |x.u|/|x.v|; distinct event rays and intervening positive sums represent all relative strata including equality. Check class masks and support counts, clip disconnected support components before extracting outer endpoints, then enumerate all endpoint sign patterns and evaluate depth-five necessary capacity recursion. A side with zero feasible strata excludes the entire class. Passing strata are only relaxation feasibility. BigInt exact arithmetic with bounded 31-bit support masks. No new general theorem or independent review.

## Actual execution

- 329: side 1, supports 28, events 13, strata 27, passing 0, excluded true
- 1328: side 1, supports 27, events 13, strata 27, passing 0, excluded true
- 1409: side 1, supports 29, events 13, strata 27, passing 0, excluded true
- 1489: side 1, supports 29, events 13, strata 27, passing 0, excluded true
- 3781: side 1, supports 27, events 13, strata 27, passing 0, excluded true

Executed in JavaScript tool runtime. Total strata 135; summed unique sign-pattern counts 249859; newly excluded 329, 1328, 1409, 1489, 3781. Based on R187's 218 remaining, current 213 = 125 rank two + 88 rank three. Global depth remains 6<=D_linear<=7 under inherited proof bank. Activity association pending. Any classes with neither side wholly excluded need exact intersection. Next min-14-event census rows: [{"i":51,"events":[14,21]},{"i":764,"events":[14,31]},{"i":1499,"events":[14,71]},{"i":3651,"events":[14,45]}]. Rank-three strata remain open.

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
const rows=[{"i":329,"a":"1441753071623","b":"2250358060613560","r":["-408","53","-1"],"local":82,"vertices":[["-1173","161","-4"],["-2091","263","-4"]],"sides":[{"side":1,"supports":28,"events":["1,11,187","12,113,1135","13,103,235","19,234,4212","19,425,13141","2,21,291","3,38,664","3,53,1821","3,77,2253","34,266,85","70,579,2151","899,17935,582641","937,18173,597907"]},{"side":-1,"supports":29,"events":["1,12,222","1,17,397","1,17,399","1,17,425","1,17,427","1,17,433","1,17,457","1,17,473","1,17,520","10,121,2219","100,2239,69202","1042,8234,2605","1058,9130,52763","11,187,4835","11,187,6092","12,204,5945","124,3079,91258","128,3095,92702","13,148,2894","13,221,6485","13,314,9409","14,313,9680","142,2867,92644","149,3728,110165","154,1214,385","158,1204,395","16,272,8347","161,3709,113291","167,4012,120479","2,15,5","2,34,1071","2,34,1097","2,34,863","211,4837,148045","23,510,15827","248,2747,46471","256,2779,47687","263,3132,58410","27,212,490","27,459,10931","28,355,6197","29,324,5448","3,32,436","3,38,664","3,51,1301","3,51,1411","3,51,1444","3,51,1535","3,51,1717","33,313,3119","39,663,18311","4,68,1921","43,799,26809","47,1049,32465","5,85,2333","5,85,2489","529,4305,9449","529,4409,16222","6,102,3031","61,660,11352","64,527,1969","7,76,1016","7,80,1558","8,136,3881","87,835,8213","9,153,3553","9,153,4384","9,153,4436","9,98,1678","98,782,245"]}]},{"i":1328,"a":"1049624778506232","b":"1202175030984711","r":["4036","-287","-19"],"local":25,"vertices":[["1072","-78","-5"],["2964","-209","-14"]],"sides":[{"side":1,"supports":27,"events":["1,10,62","1,13,13","124,1161,8556","21,209,1309","230,2511,10944","356,4921,890","4,49,107","4,55,10","57,436,5492","6,79,80","61,594,3894","838,11438,2095","86,1173,215"]},{"side":-1,"supports":31,"events":["1,13,13","182,1987,8660","2,28,5","254,3529,635","326,4489,815","36,469,480","38,413,1810","4,55,10","44,607,110","5,48,324","54,697,720","56,601,2675","8,97,215","80,979,2141"]}]},{"i":1409,"a":"909987338649560","b":"1341812475035655","r":["1696","-98","-11"],"local":30,"vertices":[["319","-19","-2"],["1377","-79","-9"]],"sides":[{"side":1,"supports":29,"events":["11,70,1074","28,473,70","29,418,713","294,4609,3920","294,4631,3724","3,1,467","356,2243,34781","442,7520,1105","46,776,115","5,72,123","58,693,2700","87,1397,865","9,58,878"]},{"side":-1,"supports":31,"events":["1,16,10","108,1667,1440","12,191,121","19,276,465","19,310,184","2,34,5","22,377,55","27,431,342","28,333,1305","3,1,467","3,47,40","36,599,90","39,607,494","4,16,485","454,7757,1135","5,72,123","57,878,760","6,95,76","706,12041,1765"]}]},{"i":1489,"a":"1132515535376","b":"2250667298145775","r":["451","124","-25"],"local":67,"vertices":[["69","23","-4"],["1284","349","-71"]],"sides":[{"side":1,"supports":29,"events":["127,1299,8763","13,45,462","173,585,6162","18,383,2425","18,397,2411","2,45,267","23,211,1587","3,40,272","3,41,271","41,1624,9500","61,2099,12175","75,2783,15313","99,3568,19598"]},{"side":-1,"supports":29,"events":["1,22,134","1,35,199","1,36,198","1,38,214","1,39,225","10,63,522","10,66,519","105,3859,21029","11,402,2178","11,421,2387","11,434,2530","121,1114,8174","124,1161,8556","128,833,6655","156,1429,10764","166,1053,8658","169,1566,11346","179,2367,16249","19,401,2563","19,661,3785","21,799,4505","22,289,1999","22,315,1973","232,2133,16008","233,763,8324","26,259,1794","27,628,3584","28,1139,6817","3,100,602","3,119,697","3,40,272","3,41,271","3,67,401","39,134,1387","4,13,143","4,27,207","41,1700,10336","47,1904,11356","49,1098,6546","49,1585,9881","49,1600,9866","58,567,4002","7,157,935","7,66,462","7,90,638","7,93,635","78,727,5382","79,3060,17544","79,756,5451","81,1052,7372","83,1098,7534","83,1800,11148","83,2853,16569","87,1901,11671","87,3149,17209","9,31,320"]}]},{"i":3781,"a":"581658328694296","b":"1670141417882087","r":["2031","46","-41"],"local":57,"vertices":[["501","11","-10"],["7623","173","-154"]],"sides":[{"side":1,"supports":27,"events":["12,4,599","29,66,1518","3335,518,165730","38,56,1951","4,4,203","45,154,2420","47,182,2554","51,22,2552","51,62,2602","561,322,28172","7,71,427","8,20,421","89,330,4818"]},{"side":-1,"supports":28,"events":["1,2,52","104,60,5223","11,26,577","127,274,6629","133,194,6826","15,22,770","15,38,790","157,290,8134","16,12,807","17,42,894","176,236,9007","18,56,961","1915,5294,101410","193,642,10356","211,550,11132","23,66,1221","25,22,1265","251,614,13192","26,56,1357","281,770,14872","29,1975,3654","29,66,1518","337,802,17684","401,1266,21432","41,138,2202","43,110,2266","43,146,2311","43,94,2246","463,1114,24311","47,110,2464","49,66,2508","5,6,255","569,586,28898","58,7668,11455","67,154,3509","67,190,3554","67,198,3564","67,86,3424","673,2354,36256","7,22,374","773,2962,41966","79,22,3938","8,20,421","845,1982,44305","89,230,4693","95,198,4950"]}]}];
console.log(JSON.stringify(replay(data,rows),null,2));
```

## Actual output

```json
{
  "output": [
    {
      "i": 329,
      "side": 1,
      "supports": 28,
      "events": 13,
      "distinct": 13,
      "results": [
        {
          "kind": "open",
          "r": [
            "-8655",
            "1184",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-7482",
            "1023",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-2709",
            "370",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-3354",
            "457",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-663",
            "89",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-7254",
            "967",
            "-21"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-699",
            "93",
            "-2"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-44472",
            "5915",
            "-127"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-23484",
            "3123",
            "-67"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-2496",
            "331",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1443",
            "191",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-390",
            "51",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-3627",
            "472",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-6864",
            "893",
            "-17"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-2009991",
            "261198",
            "-4939"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-2003127",
            "260305",
            "-4922"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-6645",
            "861",
            "-16"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-2063613",
            "266627",
            "-4870"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-1040601",
            "134444",
            "-2455"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-17589",
            "2261",
            "-40"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-18051",
            "2320",
            "-41"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-462",
            "59",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-480",
            "61",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-2418",
            "307",
            "-5"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-4392",
            "557",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "-6366",
            "807",
            "-13"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "-8457",
            "1070",
            "-17"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 1328,
      "side": 1,
      "supports": 27,
      "events": 13,
      "distinct": 13,
      "results": [
        {
          "kind": "open",
          "r": [
            "178508",
            "-12935",
            "-834"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "177436",
            "-12857",
            "-829"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "310528",
            "-22494",
            "-1451"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "133092",
            "-9637",
            "-622"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7060",
            "-511",
            "-33"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "142248",
            "-10292",
            "-665"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "144172",
            "-10431",
            "-674"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1924",
            "-139",
            "-9"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "9820",
            "-707",
            "-46"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "37356",
            "-2689",
            "-175"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "37996",
            "-2735",
            "-178"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "640",
            "-46",
            "-3"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1492",
            "-107",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "852",
            "-61",
            "-4"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "19372",
            "-1385",
            "-91"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "57264",
            "-4094",
            "-269"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "59604",
            "-4261",
            "-280"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2340",
            "-167",
            "-11"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4676",
            "-333",
            "-22"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "11688",
            "-832",
            "-55"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "174792",
            "-12424",
            "-823"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "337896",
            "-24016",
            "-1591"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "121476",
            "-8633",
            "-572"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "26532",
            "-1883",
            "-125"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "13372",
            "-949",
            "-63"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "212",
            "-15",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3176",
            "-224",
            "-15"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 1409,
      "side": 1,
      "supports": 29,
      "events": 13,
      "distinct": 13,
      "results": [
        {
          "kind": "open",
          "r": [
            "1112",
            "-66",
            "-7"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4129",
            "-245",
            "-26"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "31111",
            "-1837",
            "-197"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "26982",
            "-1592",
            "-171"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "15296",
            "-902",
            "-97"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3610",
            "-212",
            "-23"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7831",
            "-459",
            "-50"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4221",
            "-247",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3592",
            "-210",
            "-23"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "24515",
            "-1433",
            "-157"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4367",
            "-255",
            "-28"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "23522",
            "-1372",
            "-151"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "79911",
            "-4661",
            "-513"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "56389",
            "-3289",
            "-362"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "365567",
            "-21321",
            "-2347"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "309178",
            "-18032",
            "-1985"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "404771",
            "-23605",
            "-2599"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "95593",
            "-5573",
            "-614"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "98237",
            "-5727",
            "-631"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "2644",
            "-154",
            "-17"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "155",
            "-9",
            "-1"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4486",
            "-260",
            "-29"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "4167",
            "-241",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "49685",
            "-2873",
            "-322"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "196732",
            "-11310",
            "-1283"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "147047",
            "-8437",
            "-961"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "74212",
            "-4258",
            "-485"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 1489,
      "side": 1,
      "supports": 29,
      "events": 13,
      "distinct": 13,
      "results": [
        {
          "kind": "open",
          "r": [
            "851",
            "276",
            "-49"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "1633",
            "529",
            "-94"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8017",
            "2540",
            "-459"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6384",
            "2011",
            "-365"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1172",
            "369",
            "-67"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "648",
            "203",
            "-37"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "475",
            "146",
            "-27"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "27852",
            "8557",
            "-1583"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "1566",
            "481",
            "-89"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "336",
            "101",
            "-19"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "7629",
            "2284",
            "-431"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "7293",
            "2183",
            "-412"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "2816",
            "841",
            "-159"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "18051",
            "5386",
            "-1019"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "8257",
            "2461",
            "-466"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "6720",
            "1997",
            "-379"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3744",
            "1109",
            "-211"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "768",
            "221",
            "-43"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "447",
            "128",
            "-25"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "573",
            "163",
            "-32"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "12747",
            "3560",
            "-709"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "12174",
            "3397",
            "-677"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "12440",
            "3453",
            "-691"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "62466",
            "17321",
            "-3469"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "73023",
            "20242",
            "-4055"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "10557",
            "2921",
            "-586"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "3947",
            "1090",
            "-219"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    },
    {
      "i": 3781,
      "side": 1,
      "supports": 27,
      "events": 13,
      "distinct": 13,
      "results": [
        {
          "kind": "open",
          "r": [
            "154389",
            "3394",
            "-3083"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "153888",
            "3383",
            "-3073"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "44115",
            "970",
            "-881"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "22572",
            "497",
            "-451"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "13211",
            "291",
            "-264"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "3850",
            "85",
            "-77"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "31567",
            "702",
            "-633"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "27717",
            "617",
            "-556"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "129093",
            "2878",
            "-2591"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "101376",
            "2261",
            "-2035"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "238443",
            "5338",
            "-4793"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "137067",
            "3077",
            "-2758"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "145164",
            "3259",
            "-2921"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "8097",
            "182",
            "-163"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "14005",
            "315",
            "-282"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "61928",
            "1393",
            "-1247"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "76619",
            "1724",
            "-1543"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "14691",
            "331",
            "-296"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "712549",
            "16104",
            "-14373"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "697858",
            "15773",
            "-14077"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "175691",
            "3971",
            "-3544"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "4906",
            "111",
            "-99"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "19967",
            "452",
            "-403"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "15061",
            "341",
            "-304"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "12654541",
            "286876",
            "-255545"
          ],
          "feasible": false
        },
        {
          "kind": "event",
          "r": [
            "12639480",
            "286535",
            "-255241"
          ],
          "feasible": false
        },
        {
          "kind": "open",
          "r": [
            "12647103",
            "286708",
            "-255395"
          ],
          "feasible": false
        }
      ],
      "excluded": true
    }
  ],
  "totalPatterns": 249859,
  "excluded": [
    329,
    1328,
    1409,
    1489,
    3781
  ],
  "strata": 135
}
```
