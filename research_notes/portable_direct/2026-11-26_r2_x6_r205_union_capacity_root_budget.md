# X6 R205 — Union-capacity continuation and exact root crossing/zero budget

2026-11-26 Asia/Shanghai. AUTHOR EXACT FINITE NECESSARY-RELAXATION REPLAY / NOT_REVIEWED. Informed static auxiliary BRC weight-chart research, not a native dynamical calculation. Live Researcher identity unconfirmed (historical predecessor EM-DIRECT-AE5AD5). X6 lookup r2-20261126-0314-x6-read: SUCCEEDED, observed 2026-11-25T19:15:09.553445Z, Source c6dc1e65ca390aa54e84d56cc6bc340471972bfe, NO_CANONICAL_PUBLICATION_DIRECTORY. Directory observation only; not native owner projection. No CLAIM or formal Result. No change to P000 V5, ACTIVE worldview or joint-relation observer preservation.

## Frozen sources and exact scope

R204@cc3e3921322d4f4dba2cc218807fc952f64d0ff2:research_notes/portable_direct/2026-11-26_r2_x6_r204_union_capacity_rank_two.md (blob 78a646bc43fc3c3f17762f3d52fc77edd8be90d2); R182 census@6945e591116377f9386c7419b6ce31a2b9e8a146:research_notes/portable_direct/x6_r182_rank_two_side_census.json (blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82); R182 theorem@502d7abb2fe8470ed2cdabf242c2cc59a0c302ac; R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd, R122@1e4ab68c4f9c91bc60c07017acc57be20829832f. Port 10, 1935 unoriented integer directions, six joint BRC denominators, strict 3/2, w=(17t,B,22t,D), 47 necessary support lines and 49 actual components. R204 union of pattern banks on identical ordered labels is a necessary relaxation. Reuse its geometry, clipping, ternary enumeration and recurrence verbatim; only add diagnostic root identity and counts. Exact function equality with R204 checked after removing the diagnostic additions. Both open and equality strata retained; no previous exclusion rerun. Existing proofs remain dependencies, not independently re-reviewed here.

## Root crossing/zero budget (explicit corollary of the R204 recurrence)

For the depth-d fixed-endpoint state (u,v)=(all,all), let N be the number of labeled supports, and a quadruple (au,av,bu,bv) encode positive and negative endpoint masks. Set P=au|av and M=bu|bv; z=N-|P union M| is the number of supports having both endpoints zero; c=|P intersection M| is the number with both a positive and a negative endpoint. The R204 successor formula gives positive support set P and negative support set M at this root: if a support has a positive endpoint, that endpoint cannot also have a negative sign and therefore survives the corresponding positive successor; conversely a surviving positive endpoint requires membership in P. The negative statement is symmetric. Thus n_plus+n_minus=N-z+c exactly. Each child has capacity L=2^(d-1)-1. Consequently a necessary root condition is c-z<=2L-N, together with the separate balance inequalities |P|,|M|<=L. At d=5 this is c-z<=30-N; at N=30 and c=z, any legal root split must be exactly 15/15. For N=31 a legal root requires z>=c+1. The sum inequality is not sufficient: e.g. N=30 with 20 positive-only and 10 negative-only supports satisfies it but exceeds the positive capacity. This is a diagnostic consequence of the existing recurrence, not a claim of historical novelty. It is checked against the actual successor masks for every canonical union pattern. No support label is dropped. The count of distinct unordered root successor-state pairs is an exact potential root-only deduplication statistic: feasibility of a root candidate depends only on those two successor states, so duplicate pairs can be merged at that root without changing the answer. This does not license discarding the corresponding masks from descendant banks.

## Executed summary

```json
[
  {
    "id": 3509,
    "side": -1,
    "supports": 30,
    "events": 31,
    "distinct": 31,
    "strata": 63,
    "passing": 0,
    "unionPatterns": 2033,
    "union": {
      "feasible": false,
      "states": 1,
      "rootLegal": 0
    },
    "root": {
      "checks": 2033,
      "minExcess": -1,
      "minLargest": 16,
      "sumGatePass": 29,
      "totalPass": 0,
      "distinctRootSuccessorPairs": 0,
      "histogram": {
        "0": 23,
        "1": 51,
        "2": 90,
        "3": 111,
        "4": 143,
        "5": 163,
        "6": 151,
        "7": 158,
        "8": 149,
        "9": 145,
        "10": 133,
        "11": 140,
        "12": 143,
        "13": 150,
        "14": 136,
        "15": 88,
        "16": 40,
        "17": 12,
        "18": 1,
        "-1": 6
      }
    },
    "excluded": true,
    "individualSolves": 0
  },
  {
    "id": 4002,
    "side": 1,
    "supports": 28,
    "events": 32,
    "distinct": 32,
    "strata": 65,
    "passing": 0,
    "unionPatterns": 1723,
    "union": {
      "feasible": false,
      "states": 11,
      "rootLegal": 3
    },
    "root": {
      "checks": 1723,
      "minExcess": -1,
      "minLargest": 14,
      "sumGatePass": 123,
      "totalPass": 3,
      "distinctRootSuccessorPairs": 3,
      "histogram": {
        "0": 23,
        "1": 40,
        "2": 57,
        "3": 65,
        "4": 83,
        "5": 104,
        "6": 101,
        "7": 111,
        "8": 114,
        "9": 120,
        "10": 150,
        "11": 182,
        "12": 175,
        "13": 149,
        "14": 126,
        "15": 80,
        "16": 34,
        "17": 6,
        "-1": 3
      }
    },
    "excluded": true,
    "individualSolves": 0
  },
  {
    "id": 3771,
    "side": 1,
    "supports": 26,
    "events": 33,
    "distinct": 33,
    "strata": 67,
    "passing": 0,
    "unionPatterns": 1643,
    "union": {
      "feasible": false,
      "states": 16,
      "rootLegal": 7
    },
    "root": {
      "checks": 1643,
      "minExcess": -1,
      "minLargest": 15,
      "sumGatePass": 446,
      "totalPass": 7,
      "distinctRootSuccessorPairs": 3,
      "histogram": {
        "0": 25,
        "1": 39,
        "2": 65,
        "3": 119,
        "4": 193,
        "5": 268,
        "6": 263,
        "7": 216,
        "8": 179,
        "9": 127,
        "10": 81,
        "11": 44,
        "12": 15,
        "13": 4,
        "-1": 5
      }
    },
    "excluded": true,
    "individualSolves": 0
  },
  {
    "id": 3993,
    "side": 1,
    "supports": 29,
    "events": 33,
    "distinct": 33,
    "strata": 67,
    "passing": 0,
    "unionPatterns": 1789,
    "union": {
      "feasible": false,
      "states": 11,
      "rootLegal": 3
    },
    "root": {
      "checks": 1789,
      "minExcess": -1,
      "minLargest": 15,
      "sumGatePass": 68,
      "totalPass": 3,
      "distinctRootSuccessorPairs": 3,
      "histogram": {
        "0": 21,
        "1": 43,
        "2": 82,
        "3": 112,
        "4": 117,
        "5": 120,
        "6": 107,
        "7": 106,
        "8": 97,
        "9": 92,
        "10": 110,
        "11": 126,
        "12": 134,
        "13": 165,
        "14": 164,
        "15": 123,
        "16": 55,
        "17": 11,
        "-1": 4
      }
    },
    "excluded": true,
    "individualSolves": 0
  }
]
```

Strata=262; total distinct endpoint pattern counts (summed per stratum)=408226; new exclusions=[3509,4002,3771,3993]. Conditional on R204: remaining 153=65 rank-two + 88 rank-three. 6<=D_linear<=7 unchanged. A feasible necessary relaxation is not an actual tree. Root stats count all union patterns; rootLegal in a successful solver is only the visited prefix before early return. For an infeasible union these counts agree (checked). Next min-34 rows: [{"i":1530,"sides":[[1,34],[-1,58]]},{"i":2014,"sides":[[1,34],[-1,34]]}]. Any tested but not excluded row remains open; consider correlated sub-banks if a union passes. Activity association and independent review outstanding.

## Standalone Node.js reproduction

```javascript
function replayUnion(data,rows){
const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],sg=x=>x>0n?1:x<0n?-1:0,abs=x=>x<0n?-x:x,gcd=(a,b)=>b?gcd(b,a%b):abs(a),norm=p=>{let d=p.reduce(gcd,0n);return d?p.map(x=>x/d):p},uniq=a=>[...new Map(a.map(p=>[p.join(),p])).values()],add=(a,b)=>norm(a.map((x,j)=>x+b[j]));
const P=uniq(data.flatMap(e=>e.endpoints.map(p=>p.map(BigInt))));
const comps=data.map(e=>({parts:e.normal.join()==="51,2,-1"?[[["1","9","69"],["3","17","187"]],[["2","5","112"],["1","0","51"]]]:e.normal.join()==="17,-1,0"?[[["0","0","1"],["1","17","391"]],[["1","17","69"],["1","17","22"]]]:[e.endpoints]})).map(e=>e.parts.map(pair=>pair.map(p=>p.map(BigInt))));
function clip(r,side){let ret=[],labels=[];for(let i=0;i<comps.length;i++){let e=comps[i],parts=[];for(let [u,v] of e){let a=BigInt(side)*dot(r,u),b=BigInt(side)*dot(r,v);if(a<=0n&&b<=0n)continue;let d=(a<0n||b<0n)?norm(a<0n?u.map((x,j)=>b*x-a*v[j]):v.map((x,j)=>a*x-b*u[j])):null;parts.push([a<0n?d:u,b<0n?d:v])}if(parts.length){ret.push([parts[0][0],parts.at(-1)[1]]);labels.push(i)}}return {pairs:ret,labels}}
const pc=x=>{x=x-((x>>>1)&0x55555555);x=(x&0x33333333)+((x>>>2)&0x33333333);return (((x+(x>>>4))&0x0F0F0F0F)*0x01010101)>>>24};
function patterns(pairs){const N=pairs.length;if(N>31||N<=5)throw Error("unexpected support count");const pp=uniq(pairs.flat()),idx=new Map(pp.map((p,i)=>[p.join(),i])),Q=new Map();
function rec(r,t=null,p=null,s=1,u=1){let a=0n,b=0n;for(let i=0;i<pp.length;i++){let x=sg(dot(r,pp[i]));if(!x&&t)x=s*sg(dot(t,pp[i]));if(!x&&p)x=u*sg(dot(p,pp[i]));if(x>0)a|=1n<<BigInt(i);if(x<0)b|=1n<<BigInt(i)}if(a>b)[a,b]=[b,a];let key=`${a},${b}`;if(Q.has(key))return;let au=0,av=0,bu=0,bv=0;pairs.forEach(([p,q],i)=>{let x=1n<<BigInt(idx.get(p.join())),y=1n<<BigInt(idx.get(q.join())),z=1<<i;if(a&x)au|=z;if(a&y)av|=z;if(b&x)bu|=z;if(b&y)bv|=z});Q.set(key,[au,av,bu,bv])}
for(let i=0;i<pp.length;i++)for(let j=i+1;j<pp.length;j++){let r=cross(pp[i],pp[j]);if(!r.some(Boolean))continue;rec(r);for(let k=0;k<pp.length;k++)if(!dot(r,pp[k])){let t=cross(r,pp[k]);for(let s of [-1,1]){rec(r,t,null,s);for(let u of [-1,1])rec(r,t,pp[k],s,u)}}}
if(!Q.size)throw Error("unexpected rank-one carrier");return [...Q.values()]}
function canonical(q){let [a,b,c,d]=q;return a<c||(a===c&&b<=d)?q:[c,d,a,b]}
function solvePatterns(N,qs){const all=2**N-1,cache=new Map();let states=0,rootLegal=0;
function solve(u,v,d){let n=pc(u|v);if(n>2**d-1)return false;if(n<=d)return true;let key=`${u},${v},${d}`;if(cache.has(key))return cache.get(key);states++;let ans=false,limit=2**(d-1)-1;for(let [au,av,bu,bv] of qs){let pa=(u&au)|(v&av),pb=(u&bu)|(v&bv),a=u&~bu&pa,b=v&~bv&pa,c=u&~au&pb,e=v&~av&pb;if(pc(a|b)>limit||pc(c|e)>limit)continue;if(d===5)rootLegal++;if(solve(a,b,d-1)&&solve(c,e,d-1)){ans=true;break}}cache.set(key,ans);return ans}
return {feasible:solve(all,all,5),states,rootLegal}}
function rootStats(N,qs){const all=2**N-1,rootPairs=new Set();let minExcess=Infinity,minLargest=Infinity,totalPass=0,checks=0,sumGatePass=0;const histogram={};
for(let [au,av,bu,bv] of qs){const pa=au|av,pb=bu|bv,zero=pc(all&~(pa|pb)),crossing=pc(pa&pb);const nplus=pc((all&~bu&pa)|(all&~bv&pa)),nminus=pc((all&~au&pb)|(all&~av&pb));if(nplus!==pc(pa)||nminus!==pc(pb)||nplus+nminus!==N-zero+crossing)throw Error("root identity failed");checks++;let excess=crossing-zero;minExcess=Math.min(minExcess,excess);minLargest=Math.min(minLargest,Math.max(nplus,nminus));histogram[excess]=(histogram[excess]||0)+1;if(excess<=30-N)sumGatePass++;if(nplus<=15&&nminus<=15){totalPass++;let x=[all&~bu&pa,all&~bv&pa].join(),y=[all&~au&pb,all&~av&pb].join();rootPairs.add([x,y].sort().join(";"))}}
return {checks,minExcess,minLargest,sumGatePass,totalPass,distinctRootSuccessorPairs:rootPairs.size,histogram}}
function side(c,s){let a=BigInt(c.a),b=BigInt(c.b);function valid(r,strict=false){return P.every((p,i)=>{let x=sg(dot(r,p)),bit=1n<<BigInt(i);return (a&bit)?(strict?x===1:x>=0):(b&bit)?(strict?x===-1:x<=0):x===0})}
let [u,v]=c.vertices.map(p=>p.map(BigInt));if(!valid(u)||!valid(v))throw Error("bad vertex");let events=new Map();for(let z of s.events){let x=z.split(",").map(BigInt),A=dot(x,u),B=dot(x,v);if(A*B>=0n)throw Error("not varying");let alpha=abs(B),beta=abs(A),r=norm(u.map((x,j)=>alpha*x+beta*v[j]));events.set(r.join(),{r,alpha,beta})}
let list=[{r:u,alpha:1n,beta:0n},...[...events.values()].sort((a,b)=>sg(a.beta*b.alpha-b.beta*a.alpha)),{r:v,alpha:0n,beta:1n}],reps=[];for(let i=0;i+1<list.length;i++){reps.push({kind:"open",r:add(list[i].r,list[i+1].r)});if(i+1<list.length-1)reps.push({kind:"event",r:list[i+1].r})}
let results=[],bank=new Map(),allQ=[],labels=null;
for(let q of reps){if(!valid(q.r,true))throw Error("representative outside class");let clipped=clip(q.r,s.side);if(clipped.pairs.length!==s.supports)throw Error("support count mismatch");if(labels===null)labels=clipped.labels;else if(labels.join()!==clipped.labels.join())throw Error("support labels changed");let Q=patterns(clipped.pairs);let local=new Map();for(let m of Q){let n=canonical(m);local.set(n.join(),n);bank.set(n.join(),n)}allQ.push([...local.values()]);results.push({kind:q.kind,r:q.r.map(String),patterns:Q.length,distinctMaskPatterns:local.size})}
let union=solvePatterns(s.supports,[...bank.values()]),root=rootStats(s.supports,[...bank.values()]);
if(!union.feasible){if(root.totalPass!==union.rootLegal)throw Error("root count mismatch");for(let x of results){x.feasible=false;x.proof="union"}}
else for(let i=0;i<results.length;i++){let y=solvePatterns(s.supports,allQ[i]);Object.assign(results[i],y,{proof:"individual"})}
return {i:c.i,side:s.side,supports:s.supports,labels,events:s.events.length,distinct:events.size,unionPatterns:bank.size,union,root,results,excluded:results.every(x=>!x.feasible)}}
let output=[];for(let c of rows){let s=[...c.sides].sort((a,b)=>a.events.length-b.events.length);let q=side(c,s[0]);output.push(q);if(!q.excluded)output.push(side(c,s[1]))}
return {output,excluded:[...new Set(output.filter(x=>x.excluded).map(x=>x.i))],strata:output.reduce((n,x)=>n+x.results.length,0),totalPatterns:output.reduce((n,x)=>n+x.results.reduce((m,y)=>m+y.patterns,0),0)}}
const data=[{"normal":["187","12","-1"],"segments":9,"endpoints":[["0","1","12"],["1","17","391"]]},{"normal":["204","11","-1"],"segments":9,"endpoints":[["0","1","11"],["1","17","391"]]},{"normal":["5","-2","0"],"segments":51,"endpoints":[["2","5","73"],["2","5","5"]]},{"normal":["9","-1","0"],"segments":4,"endpoints":[["1","9","74"],["1","9","69"]]},{"normal":["85","7","-2"],"segments":10,"endpoints":[["1","9","74"],["3","17","187"]]},{"normal":["51","2","-1"],"segments":9,"endpoints":[["1","9","69"],["1","0","51"]]},{"normal":["0","1","-1"],"segments":2,"endpoints":[["2","5","5"],["1","0","0"]]},{"normal":["34","1","-1"],"segments":7,"endpoints":[["2","5","73"],["1","0","34"]]},{"normal":["187","20","-9"],"segments":5,"endpoints":[["6","15","158"],["1","1","23"]]},{"normal":["68","1","-3"],"segments":8,"endpoints":[["2","5","47"],["3","0","68"]]},{"normal":["176","22","-9"],"segments":4,"endpoints":[["6","15","154"],["19","28","440"]]},{"normal":["22","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","22"]]},{"normal":["61","0","-1"],"segments":78,"endpoints":[["0","1","0"],["1","17","61"]]},{"normal":["74","0","-1"],"segments":14,"endpoints":[["1","9","74"],["1","4","74"]]},{"normal":["126","0","-1"],"segments":103,"endpoints":[["0","1","0"],["1","30","126"]]},{"normal":["4","-1","0"],"segments":35,"endpoints":[["1","4","152"],["1","4","74"]]},{"normal":["17","-1","0"],"segments":44,"endpoints":[["0","0","1"],["1","17","22"]]},{"normal":["156","-1","-1"],"segments":46,"endpoints":[["1","4","152"],["1","30","126"]]},{"normal":["69","0","-1"],"segments":16,"endpoints":[["1","17","69"],["1","9","69"]]},{"normal":["9","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","9"]]},{"normal":["235","0","-3"],"segments":84,"endpoints":[["0","1","0"],["3","77","235"]]},{"normal":["87","0","-1"],"segments":107,"endpoints":[["0","1","0"],["1","17","87"]]},{"normal":["104","-1","-1"],"segments":60,"endpoints":[["1","4","100"],["3","77","235"]]},{"normal":["38","0","-3"],"segments":57,"endpoints":[["0","1","0"],["3","40","38"]]},{"normal":["5","0","-2"],"segments":72,"endpoints":[["0","1","0"],["2","5","5"]]},{"normal":["39","-1","-1"],"segments":50,"endpoints":[["3","1","116"],["1","17","22"]]},{"normal":["40","0","-3"],"segments":63,"endpoints":[["0","1","0"],["3","38","40"]]},{"normal":["26","-1","-1"],"segments":39,"endpoints":[["2","5","47"],["3","53","25"]]},{"normal":["25","0","-3"],"segments":52,"endpoints":[["0","1","0"],["3","53","25"]]},{"normal":["83","0","-2"],"segments":69,"endpoints":[["0","1","0"],["2","34","83"]]},{"normal":["102","-7","-1"],"segments":14,"endpoints":[["1","4","74"],["3","17","187"]]},{"normal":["204","-11","1"],"segments":51,"endpoints":[["0","1","11"],["1","30","126"]]},{"normal":["395","0","-2"],"segments":119,"endpoints":[["0","1","0"],["2","73","395"]]},{"normal":["289","18","-1"],"segments":10,"endpoints":[["0","1","18"],["1","17","595"]]},{"normal":["66","2","-1"],"segments":11,"endpoints":[["1","4","74"],["1","0","66"]]},{"normal":["132","5","-1"],"segments":16,"endpoints":[["1","17","217"],["1","0","132"]]},{"normal":["44","1","-1"],"segments":9,"endpoints":[["1","17","61"],["1","11","55"]]},{"normal":["88","3","-1"],"segments":7,"endpoints":[["1","4","100"],["1","0","88"]]},{"normal":["88","7","-3"],"segments":5,"endpoints":[["1","17","69"],["1","11","55"]]},{"normal":["132","-7","-1"],"segments":14,"endpoints":[["1","9","69"],["1","11","55"]]},{"normal":["153","8","-1"],"segments":7,"endpoints":[["1","9","225"],["1","0","153"]]},{"normal":["153","5","-4"],"segments":1,"endpoints":[["3","1","116"],["4","0","153"]]},{"normal":["117","-2","-2"],"segments":42,"endpoints":[["2","5","112"],["2","34","83"]]},{"normal":["198","8","-1"],"segments":5,"endpoints":[["1","4","230"],["1","0","198"]]},{"normal":["198","5","-4"],"segments":11,"endpoints":[["2","8","109"],["2","0","99"]]},{"normal":["306","17","-1"],"segments":8,"endpoints":[["1","17","595"],["1","0","306"]]},{"normal":["234","-1","-1"],"segments":43,"endpoints":[["1","4","230"],["2","73","395"]]}];
const rows=[{"i":3509,"a":"909987372204024","b":"1341808146513927","r":["16065","-865","-94"],"local":83,"vertices":[["7956","-431","-41"],["8109","-434","-53"]],"sides":[{"side":1,"supports":30,"events":["1,1,161","1,11,69","1,12,56","1,16,23","1,3,147","1,4,132","1,4,134","1,9,95","10,183,25","11,44,1594","113,1372,6516","12,113,1135","12,17,1972","129,328,18668","13,120,1232","13,52,1882","162,1315,15533","173,1560,16432","19,28,3131","2,15,193","2,27,90","2,5,289","2,8,243","21,157,2027","21,176,2008","215,1952,20408","23,183,2209","245,2972,13752","249,902,37378","25,261,1725","27,212,2596","288,629,49096","29,55,4103","3,1,467","3,26,286","3,38,170","31,384,1748","33,244,3188","35,13,5459","37,135,5559","38,607,875","50,671,2254","57,422,5506","57,436,5492","6,41,583","6,43,581","6,80,271","60,527,5713","618,5653,58619","69,146,9838","7,11,1159","7,50,678","705,6047,67273","717,6115,68453","76,935,4411","9,11,1465","9,114,530","9,64,872","9,68,868"]},{"side":-1,"supports":30,"events":["1,11,69","1,2,169","1,4,126","1,4,135","1,4,140","1,7,97","1,8,96","1,9,95","13,19,2141","13,47,1951","14,186,633","17,29,2833","19,21,3075","2,27,90","21,188,1996","23,258,1587","24,317,1087","25,308,1408","29,51,4845","3,1,467","3,26,286","35,88,5060","38,607,875","4,16,485","4,55,179","5,9,837","592,7919,26713","6,13,1022","7,15,999","83,1012,4796","9,68,868"]}]},{"i":4002,"a":"410969309191","b":"2246990797864952","r":["-765","60","1"],"local":65,"vertices":[["-8190","635","11"],["-990","85","1"]],"sides":[{"side":1,"supports":28,"events":["1,11,69","1,12,14","1,12,27","108,1303,270","108,1379,270","12,139,329","13,161,177","172,1989,8073","22,257,55","22,273,55","2218,26747,5545","2266,28421,5665","28,333,1305","290,3643,725","3,34,83","334,3949,835","338,4283,845","34,409,85","346,4166,865","36,443,90","4,45,189","446,5723,1115","5,58,282","6,76,15","68,805,170","698,8785,1745","7,80,388","72,847,180","72,899,180","8,97,20","8,97,215","94,1169,235"]},{"side":-1,"supports":31,"events":["1,10,146","1,11,69","1,11,93","10,118,467","12,139,563","124,829,52037","16,179,887","16,181,755","173,1076,71230","189,1907,27577","2,23,55","23,258,1587","237,2772,13420","3,37,41","300,3339,16591","32,363,1509","34,404,1585","4,43,373","4,49,107","40,477,1083","464,5463,1160","50,567,2358","58,679,2714","58,693,2700","62,701,2926","67,792,3740","7,80,392","73,877,1970","8,93,375","8,97,215","80,979,2141","83,936,7696","88,981,4853","9,101,497","9,101,835"]}]},{"i":3771,"a":"18708375272984","b":"2233091371303399","r":["3234","109","-77"],"local":103,"vertices":[["11781","481","-308"],["7623","173","-154"]],"sides":[{"side":1,"supports":26,"events":["10,1274,1975","11,187,731","125,2059,8471","134,14014,26465","134,15928,26465","137,2047,8795","16,943,2016","17,289,1157","18,1853,3555","196,1075,10391","2,238,395","20,89,1081","26,135,1386","267,3768,16624","27,1564,3402","27,901,2349","346,1755,18486","4,29,205","4,419,790","44,5245,8690","49,1563,4263","49,1587,4263","49,2811,6174","67,2145,5829","67,3861,8442","67,4389,8442","7,405,882","7,459,882","7,95,427","8,45,423","9,114,530","9,120,544","98,10198,19355"]},{"side":-1,"supports":28,"events":["1,17,66","10,1184,1975","10,63,522","10,66,519","103,1122,5742","105,1584,6776","113,1372,6516","128,833,6655","13,194,834","13,425,1131","13,867,1638","14,108,711","14,74,745","15,198,902","151,1606,8690","16,89,847","166,1053,8658","166,833,8878","166,909,8802","176,1029,9267","18,187,1067","18,98,955","2,135,252","2,15,102","2,255,395","2,9,108","20,107,1063","20,93,1077","202,990,10827","21,297,1309","216,1319,11317","217,13140,27342","237,2772,13420","24,167,1237","26,185,1336","260,1581,13629","265,8457,23055","28,165,1473","29,439,1875","29,961,2523","302,2326,15341","32,175,1697","32,415,1907","332,1913,17509","38,165,2058","38,293,1930","38,295,1928","4,17,217","4,27,207","4,29,205","42,4471,8295","47,745,3117","5,306,630","5,58,282","5,73,317","50,252,2673","6,31,320","6,34,317","604,2741,32593","7,104,448","7,110,462","7,72,420","7,76,392","76,935,4411","78,10064,15405","78,385,4178","8,136,527","8,39,429","8,45,423","8,59,409","83,1012,4796","94,558,4941"]}]},{"i":3993,"a":"4806868336647","b":"2246990797864952","r":["-710","55","1"],"local":156,"vertices":[["-330","25","1"],["-8190","635","11"]],"sides":[{"side":1,"supports":29,"events":["1,11,69","1,5,391","1,7,227","1,8,217","1,9,147","1,9,177","11,60,4386","11,61,4403","113,393,41259","137,297,46971","16,89,3160","17,159,3039","172,1989,8073","19,145,4067","19,149,4297","19,156,2808","19,193,1783","2,13,455","22,81,8109","25,43,8381","25,69,8823","28,333,1305","3,17,595","3,22,506","4,5,1309","5,34,1037","5,58,282","55,431,9415","63,463,9365","7,24,2550","7,80,388","71,223,25517","73,189,25551"]},{"side":-1,"supports":31,"events":["1,1,323","1,10,146","1,10,94","1,11,69","1,11,93","1,4,374","1,5,229","1,6,228","1,7,227","1,8,148","1,9,147","1,9,177","10,118,467","10,49,2291","10,79,1715","101,512,39610","103,667,21095","1069,5572,421838","1073,5588,423334","109,612,21573","109,852,16152","11,34,3944","11,60,4386","11,86,2488","119,809,24679","12,139,563","121,1108,21512","129,1088,22468","13,100,1928","147,634,33764","15,112,3398","15,122,2218","151,721,34613","157,1044,35694","16,179,887","160,1423,35864","166,2159,415","167,1500,29544","17,131,2899","17,146,3832","178,1297,29981","181,940,71366","189,1907,27577","19,180,2784","19,28,6290","2,11,457","2,13,455","2,17,295","2,17,451","2,5,697","214,1855,47582","214,1909,48167","218,1871,48322","22,127,5021","22,133,4430","23,136,4607","23,196,4016","23,200,5182","23,258,1587","237,2772,13420","241,1666,40142","241,244,77894","245,1682,40750","269,2096,57925","28,247,4121","29,220,4928","29,236,6550","295,2584,66446","3,17,1207","3,17,595","3,17,685","3,22,506","3,25,443","3,28,440","300,3339,16591","32,363,1509","33,197,7525","33,313,3119","34,404,1585","35,244,7946","356,3179,52357","4,29,673","4,43,373","4,49,107","41,44,13294","43,238,8483","43,257,8635","43,289,7121","43,328,7316","43,400,6308","451,2974,102560","47,276,9399","49,136,17306","5,26,1144","50,317,11383","50,567,2358","53,420,7848","53,467,11845","57,313,11225","58,679,2714","58,693,2700","59,290,13516","59,51,18921","6,61,563","61,400,13874","64,511,13880","67,792,3740","7,37,2771","7,46,1592","7,58,1580","7,80,392","71,492,16122","73,526,16556","74,449,14914","763,3754,174788","77,641,16909","8,45,1584","8,59,1696","8,65,1744","8,71,1801","8,93,375","80,979,2141","83,800,12148","83,936,7696","84,457,16508","87,835,8213","88,981,4853","9,101,497","9,101,835","9,58,1841","9,58,2048"]}]}];
console.log(JSON.stringify(replayUnion(data,rows),null,2));
```

## Complete actual output

```json
{
  "output": [
    {
      "i": 3509,
      "side": -1,
      "supports": 30,
      "labels": [
        0,
        1,
        11,
        12,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        28,
        29,
        31,
        32,
        33,
        35,
        36,
        38,
        40,
        42,
        43,
        45,
        46
      ],
      "events": 31,
      "distinct": 31,
      "unionPatterns": 2033,
      "union": {
        "feasible": false,
        "states": 1,
        "rootLegal": 0
      },
      "root": {
        "checks": 2033,
        "minExcess": -1,
        "minLargest": 16,
        "sumGatePass": 29,
        "totalPass": 0,
        "distinctRootSuccessorPairs": 0,
        "histogram": {
          "0": 23,
          "1": 51,
          "2": 90,
          "3": 111,
          "4": 143,
          "5": 163,
          "6": 151,
          "7": 158,
          "8": 149,
          "9": 145,
          "10": 133,
          "11": 140,
          "12": 143,
          "13": 150,
          "14": 136,
          "15": 88,
          "16": 40,
          "17": 12,
          "18": 1,
          "-1": 6
        }
      },
      "results": [
        {
          "kind": "open",
          "r": [
            "25903",
            "-1403",
            "-134"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "17947",
            "-972",
            "-93"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "13427",
            "-727",
            "-70"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "8907",
            "-482",
            "-47"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "4308",
            "-233",
            "-23"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "25557",
            "-1382",
            "-137"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "47625",
            "-2575",
            "-256"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "22068",
            "-1193",
            "-119"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "22253",
            "-1203",
            "-120"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "185",
            "-10",
            "-1"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "127940",
            "-6915",
            "-693"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "127755",
            "-6905",
            "-692"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "46329",
            "-2504",
            "-251"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "11232",
            "-607",
            "-61"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "9012",
            "-487",
            "-49"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "6792",
            "-367",
            "-37"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "4202",
            "-227",
            "-23"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1612",
            "-87",
            "-9"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "58111",
            "-3136",
            "-325"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "56499",
            "-3049",
            "-316"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "3039",
            "-164",
            "-17"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "7320",
            "-395",
            "-41"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "28327",
            "-1527",
            "-162"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "77661",
            "-4186",
            "-445"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "28591",
            "-1541",
            "-164"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "8112",
            "-437",
            "-47"
          ],
          "patterns": 1805,
          "distinctMaskPatterns": 1805,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "29779",
            "-1604",
            "-173"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "81225",
            "-4375",
            "-472"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "88280",
            "-4755",
            "-513"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "7055",
            "-380",
            "-41"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "8746",
            "-471",
            "-51"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1691",
            "-91",
            "-10"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "2193",
            "-118",
            "-13"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "4888",
            "-263",
            "-29"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "14611",
            "-786",
            "-87"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "228888",
            "-12313",
            "-1363"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "247434",
            "-13309",
            "-1477"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "265980",
            "-14305",
            "-1591"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "13871",
            "-746",
            "-83"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "66924",
            "-3599",
            "-401"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "67743",
            "-3643",
            "-406"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "819",
            "-44",
            "-5"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "1955",
            "-105",
            "-12"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1136",
            "-61",
            "-7"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "4042",
            "-217",
            "-25"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "31200",
            "-1675",
            "-193"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "28743",
            "-1543",
            "-178"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "26286",
            "-1411",
            "-163"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "8216",
            "-441",
            "-51"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "6578",
            "-353",
            "-41"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "306098",
            "-16423",
            "-1915"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1217814",
            "-65339",
            "-7619"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "1218131",
            "-65356",
            "-7621"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "317",
            "-17",
            "-2"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "14608",
            "-783",
            "-93"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "28899",
            "-1549",
            "-184"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "15691",
            "-841",
            "-100"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "2483",
            "-133",
            "-16"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "19045",
            "-1020",
            "-123"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "16562",
            "-887",
            "-107"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "41867",
            "-2242",
            "-271"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "25305",
            "-1355",
            "-164"
          ],
          "patterns": 1811,
          "distinctMaskPatterns": 1811,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "33414",
            "-1789",
            "-217"
          ],
          "patterns": 1817,
          "distinctMaskPatterns": 1817,
          "feasible": false,
          "proof": "union"
        }
      ],
      "excluded": true
    },
    {
      "i": 4002,
      "side": 1,
      "supports": 28,
      "labels": [
        0,
        1,
        11,
        12,
        14,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        31,
        32,
        33,
        35,
        36,
        38,
        42,
        45,
        46
      ],
      "events": 32,
      "distinct": 32,
      "unionPatterns": 1723,
      "union": {
        "feasible": false,
        "states": 11,
        "rootLegal": 3
      },
      "root": {
        "checks": 1723,
        "minExcess": -1,
        "minLargest": 14,
        "sumGatePass": 123,
        "totalPass": 3,
        "distinctRootSuccessorPairs": 3,
        "histogram": {
          "0": 23,
          "1": 40,
          "2": 57,
          "3": 65,
          "4": 83,
          "5": 104,
          "6": 101,
          "7": 111,
          "8": 114,
          "9": 120,
          "10": 150,
          "11": 182,
          "12": 175,
          "13": 149,
          "14": 126,
          "15": 80,
          "16": 34,
          "17": 6,
          "-1": 3
        }
      },
      "results": [
        {
          "kind": "open",
          "r": [
            "-128583",
            "9987",
            "172"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-1277640",
            "99235",
            "1709"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-1585485",
            "123265",
            "2116"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-307845",
            "24030",
            "407"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-1263915",
            "99235",
            "1648"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-956070",
            "75205",
            "1241"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-973035",
            "76540",
            "1263"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-16965",
            "1335",
            "22"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-3861",
            "304",
            "5"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-2340",
            "185",
            "3"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-981630",
            "77745",
            "1253"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-1960920",
            "155305",
            "2503"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-984789",
            "77996",
            "1257"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-8658",
            "687",
            "11"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-205452",
            "16303",
            "261"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-813150",
            "64525",
            "1033"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-238563",
            "18957",
            "302"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-6343740",
            "504185",
            "8027"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-3173859",
            "252251",
            "4016"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-3978",
            "317",
            "5"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-204633",
            "16337",
            "256"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-200655",
            "16020",
            "251"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-461565",
            "36935",
            "574"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-260910",
            "20915",
            "323"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-135711",
            "10879",
            "168"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-10512",
            "843",
            "13"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-11349",
            "911",
            "14"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-12186",
            "979",
            "15"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-13005",
            "1045",
            "16"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-819",
            "66",
            "1"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-8307",
            "673",
            "10"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-98865",
            "8010",
            "119"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-140517",
            "11413",
            "168"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-41652",
            "3403",
            "49"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-9360",
            "765",
            "11"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-14508",
            "1187",
            "17"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-8541",
            "699",
            "10"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-2574",
            "211",
            "3"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-6903",
            "567",
            "8"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-4329",
            "356",
            "5"
          ],
          "patterns": 1467,
          "distinctMaskPatterns": 1467,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-147537",
            "12193",
            "168"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-290745",
            "24030",
            "331"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-1484379",
            "122731",
            "1688"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-1193634",
            "98701",
            "1357"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-707733",
            "58562",
            "803"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-929565",
            "76985",
            "1052"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-204165",
            "16910",
            "231"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-91260",
            "7565",
            "103"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-59787",
            "4968",
            "67"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-28314",
            "2371",
            "31"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-29241",
            "2449",
            "32"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-927",
            "78",
            "1"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-90261",
            "7604",
            "97"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-179595",
            "15130",
            "193"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-1060605",
            "89445",
            "1136"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-881010",
            "74315",
            "943"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-440973",
            "37197",
            "472"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-936",
            "79",
            "1"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-189891",
            "16099",
            "200"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-188955",
            "16020",
            "199"
          ],
          "patterns": 1473,
          "distinctMaskPatterns": 1473,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-246285",
            "20915",
            "258"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-57330",
            "4895",
            "59"
          ],
          "patterns": 1469,
          "distinctMaskPatterns": 1469,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-21411",
            "1829",
            "22"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-6903",
            "592",
            "7"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-7893",
            "677",
            "8"
          ],
          "patterns": 1479,
          "distinctMaskPatterns": 1479,
          "feasible": false,
          "proof": "union"
        }
      ],
      "excluded": true
    },
    {
      "i": 3771,
      "side": 1,
      "supports": 26,
      "labels": [
        2,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        14,
        16,
        19,
        20,
        21,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        32,
        36,
        38,
        39,
        41,
        42
      ],
      "events": 33,
      "distinct": 33,
      "unionPatterns": 1643,
      "union": {
        "feasible": false,
        "states": 16,
        "rootLegal": 7
      },
      "root": {
        "checks": 1643,
        "minExcess": -1,
        "minLargest": 15,
        "sumGatePass": 446,
        "totalPass": 7,
        "distinctRootSuccessorPairs": 3,
        "histogram": {
          "0": 25,
          "1": 39,
          "2": 65,
          "3": 119,
          "4": 193,
          "5": 268,
          "6": 263,
          "7": 216,
          "8": 179,
          "9": 127,
          "10": 81,
          "11": 44,
          "12": 15,
          "13": 4,
          "-1": 5
        }
      },
      "results": [
        {
          "kind": "open",
          "r": [
            "24221",
            "976",
            "-629"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "12440",
            "495",
            "-321"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "918635",
            "35530",
            "-23369"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "906195",
            "35035",
            "-23048"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "170055",
            "6565",
            "-4322"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "114135",
            "4355",
            "-2884"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "117030",
            "4465",
            "-2957"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "2895",
            "110",
            "-73"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "188082",
            "7117",
            "-4733"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "185187",
            "7007",
            "-4660"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "199207",
            "7532",
            "-5011"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "14020",
            "525",
            "-351"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "37411",
            "1396",
            "-935"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "23391",
            "871",
            "-584"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "2124",
            "79",
            "-53"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "2097",
            "77",
            "-52"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "929",
            "34",
            "-23"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "8122",
            "297",
            "-201"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "4406",
            "161",
            "-109"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "690",
            "25",
            "-17"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "7189",
            "254",
            "-175"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "13688",
            "483",
            "-333"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "3793",
            "133",
            "-92"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "5277",
            "182",
            "-127"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "35825",
            "1235",
            "-862"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "66373",
            "2288",
            "-1597"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "460941",
            "15161",
            "-10852"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "394568",
            "12873",
            "-9255"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "414095",
            "13510",
            "-9713"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "19527",
            "637",
            "-458"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "25698",
            "833",
            "-601"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "6171",
            "196",
            "-143"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "3072",
            "97",
            "-71"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "27621",
            "871",
            "-638"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "62853",
            "1888",
            "-1421"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "98085",
            "2905",
            "-2204"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "49902",
            "1477",
            "-1121"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1719",
            "49",
            "-38"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "1137",
            "32",
            "-25"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "11925",
            "335",
            "-262"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "8514",
            "239",
            "-187"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "5103",
            "143",
            "-112"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "189516",
            "5291",
            "-4153"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "563445",
            "15730",
            "-12347"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "62793",
            "1753",
            "-1376"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1692",
            "47",
            "-37"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "91529",
            "2489",
            "-1984"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "547482",
            "14887",
            "-11867"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "207493",
            "5613",
            "-4488"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "74997",
            "1952",
            "-1597"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "25857",
            "662",
            "-547"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1010997",
            "25852",
            "-21377"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "1013664",
            "25919",
            "-21433"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "2667",
            "67",
            "-56"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "7103",
            "178",
            "-149"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "39951",
            "1001",
            "-838"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "16846",
            "421",
            "-353"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "10587",
            "262",
            "-221"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "52634",
            "1279",
            "-1091"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "147315",
            "3575",
            "-3052"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "19293",
            "463",
            "-398"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "84201",
            "1981",
            "-1724"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "48841",
            "1146",
            "-999"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "62322",
            "1457",
            "-1273"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "63509",
            "1484",
            "-1297"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1187",
            "27",
            "-24"
          ],
          "patterns": 1389,
          "distinctMaskPatterns": 1389,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "4405",
            "100",
            "-89"
          ],
          "patterns": 1395,
          "distinctMaskPatterns": 1395,
          "feasible": false,
          "proof": "union"
        }
      ],
      "excluded": true
    },
    {
      "i": 3993,
      "side": 1,
      "supports": 29,
      "labels": [
        0,
        1,
        11,
        12,
        14,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        31,
        32,
        33,
        35,
        36,
        38,
        40,
        42,
        45,
        46
      ],
      "events": 33,
      "distinct": 33,
      "unionPatterns": 1789,
      "union": {
        "feasible": false,
        "states": 11,
        "rootLegal": 3
      },
      "root": {
        "checks": 1789,
        "minExcess": -1,
        "minLargest": 15,
        "sumGatePass": 68,
        "totalPass": 3,
        "distinctRootSuccessorPairs": 3,
        "histogram": {
          "0": 21,
          "1": 43,
          "2": 82,
          "3": 112,
          "4": 117,
          "5": 120,
          "6": 107,
          "7": 106,
          "8": 97,
          "9": 92,
          "10": 110,
          "11": 126,
          "12": 134,
          "13": 165,
          "14": 164,
          "15": 123,
          "16": 55,
          "17": 11,
          "-1": 4
        }
      },
      "results": [
        {
          "kind": "open",
          "r": [
            "-11410",
            "865",
            "34"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-22490",
            "1705",
            "67"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-139010",
            "10545",
            "408"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-116520",
            "8840",
            "341"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-123830",
            "9395",
            "362"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-7310",
            "555",
            "21"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-28426",
            "2161",
            "79"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-49542",
            "3767",
            "137"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-10520",
            "800",
            "29"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-3058",
            "233",
            "8"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-319816",
            "24376",
            "829"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-316758",
            "24143",
            "821"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-122330",
            "9325",
            "316"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-50232",
            "3832",
            "127"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-92482",
            "7057",
            "232"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-227214",
            "17339",
            "569"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-166686",
            "12731",
            "407"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-1773018",
            "135433",
            "4315"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-126974",
            "9699",
            "309"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-4618",
            "353",
            "11"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-172574",
            "13199",
            "404"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-340530",
            "26045",
            "797"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-126192",
            "9652",
            "295"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-38046",
            "2911",
            "88"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-40228",
            "3078",
            "93"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-2182",
            "167",
            "5"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-241390",
            "18475",
            "553"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-963378",
            "73733",
            "2207"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-321274",
            "24589",
            "736"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-444",
            "34",
            "1"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-110986",
            "8501",
            "248"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-332514",
            "25469",
            "743"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-4478",
            "343",
            "10"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-16770",
            "1285",
            "37"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-488748",
            "37498",
            "1033"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-960726",
            "73711",
            "2029"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-40248",
            "3088",
            "85"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-5226",
            "401",
            "11"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-6786",
            "521",
            "14"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-8346",
            "641",
            "17"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-9386",
            "721",
            "19"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-47970",
            "3685",
            "97"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-800046",
            "61471",
            "1606"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-1552122",
            "119257",
            "3115"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-51584",
            "3964",
            "103"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-304902",
            "23447",
            "593"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-56706",
            "4361",
            "110"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-148746",
            "11441",
            "287"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-152944",
            "11764",
            "295"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-4198",
            "323",
            "8"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-4756",
            "366",
            "9"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-558",
            "43",
            "1"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-2828",
            "218",
            "5"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-7926",
            "611",
            "14"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-165252",
            "12742",
            "289"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-157326",
            "12131",
            "275"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-81846",
            "6311",
            "143"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-6366",
            "491",
            "11"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-10512",
            "812",
            "17"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-14658",
            "1133",
            "23"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-3842",
            "297",
            "6"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-8394",
            "649",
            "13"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-7544",
            "584",
            "11"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-82134",
            "6359",
            "119"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-41168",
            "3188",
            "59"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "-164874",
            "12769",
            "235"
          ],
          "patterns": 1559,
          "distinctMaskPatterns": 1559,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "-28844",
            "2234",
            "41"
          ],
          "patterns": 1565,
          "distinctMaskPatterns": 1565,
          "feasible": false,
          "proof": "union"
        }
      ],
      "excluded": true
    }
  ],
  "excluded": [
    3509,
    4002,
    3771,
    3993
  ],
  "strata": 262,
  "totalPatterns": 408226
}
```
