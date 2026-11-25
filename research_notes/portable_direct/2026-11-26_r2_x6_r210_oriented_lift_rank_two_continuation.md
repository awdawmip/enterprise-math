# X6 R210 — Oriented cross-product lifting and exact rank-two continuation

2026-11-26. AUTHOR PROOF / EXACT NECESSARY-RELAXATION REPLAY / NOT_REVIEWED. Informed static auxiliary BRC weight-chart research, not native dynamical arithmetic. P000 V5 remains locked. No own current native researcher identity confirmed; no CLAIM or formal Result. Task read r2-20261126-0713-x6-read returned SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY at Source 0ec1e7a56fdbed4d14c4449437e60a60f73c2643; no owner projection.

## Frozen sources
R209@32592df7bff1a87649e3541f12c22b99b6a0cd71:research_notes/portable_direct/2026-11-26_r2_x6_r209_bilinear_joint_capacity_envelope.md (blob 6f634f0a0679e23d95b0e96a99dbdc33c541a746); R206@5b836df9a9622701adf2d3cddef04ba652b49774:research_notes/portable_direct/2026-11-26_r2_x6_r206_successor_antichain_min34.md (blob cd71f06ec29c1901e4a86c896e758ccc8f1baaa0); R182 census@6945e591116377f9386c7419b6ce31a2b9e8a146:research_notes/portable_direct/x6_r182_rank_two_side_census.json (blob f9fbd86dcf810e3f73004db8d5011c7af59e2d82). Port 10, 1935 directions, six joint BRC relations, C/A=22/17, 47 supports, 49 components as inherited. R209 survivors used exactly.

## Theorem: exact oriented cross-product lift by the endpoint-pair determinant arrangement
Let P=(p_i) be a finite list of nonzero vectors spanning the auxiliary real three-space; let s,t be sign vectors on P. C_s={r: sign(r dot p_i)=s_i for all i}, C_t similarly. Exclude zero from each. For a given nonzero w, put H=w^perp and B_ij=sign(w dot (p_i cross p_j)). Then existence of r in C_s and q in C_t with r cross q a strictly positive multiple of w is determined by B alone, using the following finite criterion.

Form the oriented rays u_(i,e)=e(w cross p_i), e=+1,-1, discarding i whose B row is identically zero. This discard is exact: the row vanishes iff w cross p_i=0, since P spans. The sign pattern of u_(i,e) on P is e B_ij. Define A_s to contain rays whose signs agree weakly with s (zero where s is zero; either zero or s_j elsewhere); A_t analogously. A_s spans the closed section of the weak sign cone in H: the section is pointed because a vector in its lineality has all P dots zero. A nonzero extreme ray in the section lies on at least one nontrivial restricting line p_i dot x=0 in H; otherwise it would be interior to the two-dimensional ambient H. The same holds if the section has dimension one, since its direction must lie on such a line. Each such ray is in the enumerated list. The trivial section has no rays. Thus C_s intersect H is nonempty with a nonzero vector iff A_s is nonempty and for every j with s_j nonzero at least one ray in A_s has that strict sign. Sufficiency follows by summing the ray representatives, since no cancellation of a weakly fixed sign occurs. Necessity follows from conic generation. Same for t.

If both strict sections are nonempty, the exact additional test for positive cross orientation is: some u_(i,e) in A_s and u_(j,f) in A_t satisfies e f B_ij>0. Indeed (w cross p_i) cross (w cross p_j)=(w dot (p_i cross p_j))w. Necessity follows by expanding r,q in nonnegative ray combinations and bilinearity. Sufficiency follows by taking the witnessing pair, then adding small positive multiples of strict-section vectors to each. Strict sign constraints become satisfied, and positive determinant persists by continuity. These two tests are necessary and sufficient for the stated nonzero lift. Positive rescaling then gives r cross q=w exactly if desired. w=0 has a separate exact criterion: the nonzero r,q must be parallel, hence t=s or t=-s, with s realizable and nonzero. There is no assumption that C_s or C_t has full dimension.

Corollary: refine the auxiliary w arrangement of R209 by all nonzero p_i cross p_j. For every nonzero oriented stratum (including equality strata), the exact lift predicate is constant and can be evaluated using just its pair determinant signs. Include the zero case separately. This gives an exact finite reduction of the bilinear joint sign lift, including boundary and rank-two cones, without solving a nonlinear feasibility system. If dynamic normals are proportional to endpoint crosses as verified in R209, their signs are already contained in B. This is a sufficiency theorem for the lift, not for the subsequent decision tree. It preserves all labeled endpoint signs and joint BRC relations. General arrangement may be large (at most binomial(51,2)=1275 normals before deduplication); no performance gain claimed. Full frozen refined arrangement has not been generated. This is a proof by auxiliary real coordinates, not a claim of a new native spatial dimension.

## Executed exact continuation
Reused the R206 replay function verbatim on the two smallest-min-event R209 rank-two survivors 2015 and 3639. BigInt geometry, original and antichain capacity solvers, exact census event strata. The R206 event coverage/recurrence proof is inherited, not independently reviewed. New exclusions: [2015,3639]. Computed strata 150; total local patterns 321228. No changes to rank-three exclusions. Conditional remaining 48; bound 6<=D_linear<=7 unchanged. The lift theorem above was not used as an exclusion oracle in this run.

## Reproduction
Standalone exact replay (function copied from immutable R206, frozen two rows and support data below).
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
function solveAntichain(N,qs){
const all=2**N-1,cache=new Map();let states=0,eligible=0,minimal=0,rootEligible=0,rootMinimal=0;
const sub=(x,y)=>(x&~y)===0;
const le=(a,b)=>sub(a[0],b[0])&&sub(a[1],b[1]);
const dominates=(a,b)=>(le(a.slice(0,2),b.slice(0,2))&&le(a.slice(2),b.slice(2)))||(le(a.slice(0,2),b.slice(2))&&le(a.slice(2),b.slice(0,2)));
function solve(u,v,d){let n=pc(u|v);if(n>2**d-1)return false;if(n<=d)return true;
const key=[u,v,d].join();if(cache.has(key))return cache.get(key);states++;
let lim=2**(d-1)-1,front=[],count=0;
for(const [au,av,bu,bv] of qs){let pa=(u&au)|(v&av),pb=(u&bu)|(v&bv),a=u&~bu&pa,b=v&~bv&pa,c=u&~au&pb,e=v&~av&pb;
if(pc(a|b)>lim||pc(c|e)>lim)continue;count++;
let p=[a,b,c,e];if(front.some(q=>dominates(q,p)))continue;
front=front.filter(q=>!dominates(p,q));front.push(p)}
eligible+=count;minimal+=front.length;if(d===5){rootEligible=count;rootMinimal=front.length}
let ans=front.some(([a,b,c,e])=>solve(a,b,d-1)&&solve(c,e,d-1));cache.set(key,ans);return ans}
return {feasible:solve(all,all,5),states,eligible,minimal,rootEligible,rootMinimal}}
function rootStats(N,qs){const all=2**N-1,rootPairs=new Set();let minExcess=Infinity,minLargest=Infinity,totalPass=0,checks=0,sumGatePass=0;const histogram={};
for(let [au,av,bu,bv] of qs){const pa=au|av,pb=bu|bv,zero=pc(all&~(pa|pb)),crossing=pc(pa&pb);const nplus=pc((all&~bu&pa)|(all&~bv&pa)),nminus=pc((all&~au&pb)|(all&~av&pb));if(nplus!==pc(pa)||nminus!==pc(pb)||nplus+nminus!==N-zero+crossing)throw Error("root identity failed");checks++;let excess=crossing-zero;minExcess=Math.min(minExcess,excess);minLargest=Math.min(minLargest,Math.max(nplus,nminus));histogram[excess]=(histogram[excess]||0)+1;if(excess<=30-N)sumGatePass++;if(nplus<=15&&nminus<=15){totalPass++;let x=[all&~bu&pa,all&~bv&pa].join(),y=[all&~au&pb,all&~av&pb].join();rootPairs.add([x,y].sort().join(";"))}}
return {checks,minExcess,minLargest,sumGatePass,totalPass,distinctRootSuccessorPairs:rootPairs.size,histogram}}
function side(c,s){let a=BigInt(c.a),b=BigInt(c.b);function valid(r,strict=false){return P.every((p,i)=>{let x=sg(dot(r,p)),bit=1n<<BigInt(i);return (a&bit)?(strict?x===1:x>=0):(b&bit)?(strict?x===-1:x<=0):x===0})}
let [u,v]=c.vertices.map(p=>p.map(BigInt));if(!valid(u)||!valid(v))throw Error("bad vertex");let events=new Map();for(let z of s.events){let x=z.split(",").map(BigInt),A=dot(x,u),B=dot(x,v);if(A*B>=0n)throw Error("not varying");let alpha=abs(B),beta=abs(A),r=norm(u.map((x,j)=>alpha*x+beta*v[j]));events.set(r.join(),{r,alpha,beta})}
let list=[{r:u,alpha:1n,beta:0n},...[...events.values()].sort((a,b)=>sg(a.beta*b.alpha-b.beta*a.alpha)),{r:v,alpha:0n,beta:1n}],reps=[];for(let i=0;i+1<list.length;i++){reps.push({kind:"open",r:add(list[i].r,list[i+1].r)});if(i+1<list.length-1)reps.push({kind:"event",r:list[i+1].r})}
let results=[],bank=new Map(),allQ=[],labels=null;
for(let q of reps){if(!valid(q.r,true))throw Error("representative outside class");let clipped=clip(q.r,s.side);if(clipped.pairs.length!==s.supports)throw Error("support count mismatch");if(labels===null)labels=clipped.labels;else if(labels.join()!==clipped.labels.join())throw Error("support labels changed");let Q=patterns(clipped.pairs);let local=new Map();for(let m of Q){let n=canonical(m);local.set(n.join(),n);bank.set(n.join(),n)}allQ.push([...local.values()]);results.push({kind:q.kind,r:q.r.map(String),patterns:Q.length,distinctMaskPatterns:local.size})}
let union=solvePatterns(s.supports,[...bank.values()]),root=rootStats(s.supports,[...bank.values()]),antichain=solveAntichain(s.supports,[...bank.values()]);if(union.feasible!==antichain.feasible)throw Error('solver mismatch');if(antichain.rootEligible!==root.totalPass)throw Error('root mismatch');
if(!union.feasible){if(root.totalPass!==union.rootLegal)throw Error("root count mismatch");for(let x of results){x.feasible=false;x.proof="union"}}
else for(let i=0;i<results.length;i++){let y=solvePatterns(s.supports,allQ[i]);Object.assign(results[i],y,{proof:"individual"})}
return {i:c.i,side:s.side,supports:s.supports,labels,events:s.events.length,distinct:events.size,unionPatterns:bank.size,union,root,antichain,results,excluded:results.every(x=>!x.feasible)}}
let output=[];for(let c of rows){let s=[...c.sides].sort((a,b)=>a.events.length-b.events.length);let q=side(c,s[0]);output.push(q);if(!q.excluded)output.push(side(c,s[1]))}
return {output,excluded:[...new Set(output.filter(x=>x.excluded).map(x=>x.i))],strata:output.reduce((n,x)=>n+x.results.length,0),totalPatterns:output.reduce((n,x)=>n+x.results.reduce((m,y)=>m+y.patterns,0),0)}}
const data=[{"normal":["187","12","-1"],"segments":9,"endpoints":[["0","1","12"],["1","17","391"]]},{"normal":["204","11","-1"],"segments":9,"endpoints":[["0","1","11"],["1","17","391"]]},{"normal":["5","-2","0"],"segments":51,"endpoints":[["2","5","73"],["2","5","5"]]},{"normal":["9","-1","0"],"segments":4,"endpoints":[["1","9","74"],["1","9","69"]]},{"normal":["85","7","-2"],"segments":10,"endpoints":[["1","9","74"],["3","17","187"]]},{"normal":["51","2","-1"],"segments":9,"endpoints":[["1","9","69"],["1","0","51"]]},{"normal":["0","1","-1"],"segments":2,"endpoints":[["2","5","5"],["1","0","0"]]},{"normal":["34","1","-1"],"segments":7,"endpoints":[["2","5","73"],["1","0","34"]]},{"normal":["187","20","-9"],"segments":5,"endpoints":[["6","15","158"],["1","1","23"]]},{"normal":["68","1","-3"],"segments":8,"endpoints":[["2","5","47"],["3","0","68"]]},{"normal":["176","22","-9"],"segments":4,"endpoints":[["6","15","154"],["19","28","440"]]},{"normal":["22","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","22"]]},{"normal":["61","0","-1"],"segments":78,"endpoints":[["0","1","0"],["1","17","61"]]},{"normal":["74","0","-1"],"segments":14,"endpoints":[["1","9","74"],["1","4","74"]]},{"normal":["126","0","-1"],"segments":103,"endpoints":[["0","1","0"],["1","30","126"]]},{"normal":["4","-1","0"],"segments":35,"endpoints":[["1","4","152"],["1","4","74"]]},{"normal":["17","-1","0"],"segments":44,"endpoints":[["0","0","1"],["1","17","22"]]},{"normal":["156","-1","-1"],"segments":46,"endpoints":[["1","4","152"],["1","30","126"]]},{"normal":["69","0","-1"],"segments":16,"endpoints":[["1","17","69"],["1","9","69"]]},{"normal":["9","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","9"]]},{"normal":["235","0","-3"],"segments":84,"endpoints":[["0","1","0"],["3","77","235"]]},{"normal":["87","0","-1"],"segments":107,"endpoints":[["0","1","0"],["1","17","87"]]},{"normal":["104","-1","-1"],"segments":60,"endpoints":[["1","4","100"],["3","77","235"]]},{"normal":["38","0","-3"],"segments":57,"endpoints":[["0","1","0"],["3","40","38"]]},{"normal":["5","0","-2"],"segments":72,"endpoints":[["0","1","0"],["2","5","5"]]},{"normal":["39","-1","-1"],"segments":50,"endpoints":[["3","1","116"],["1","17","22"]]},{"normal":["40","0","-3"],"segments":63,"endpoints":[["0","1","0"],["3","38","40"]]},{"normal":["26","-1","-1"],"segments":39,"endpoints":[["2","5","47"],["3","53","25"]]},{"normal":["25","0","-3"],"segments":52,"endpoints":[["0","1","0"],["3","53","25"]]},{"normal":["83","0","-2"],"segments":69,"endpoints":[["0","1","0"],["2","34","83"]]},{"normal":["102","-7","-1"],"segments":14,"endpoints":[["1","4","74"],["3","17","187"]]},{"normal":["204","-11","1"],"segments":51,"endpoints":[["0","1","11"],["1","30","126"]]},{"normal":["395","0","-2"],"segments":119,"endpoints":[["0","1","0"],["2","73","395"]]},{"normal":["289","18","-1"],"segments":10,"endpoints":[["0","1","18"],["1","17","595"]]},{"normal":["66","2","-1"],"segments":11,"endpoints":[["1","4","74"],["1","0","66"]]},{"normal":["132","5","-1"],"segments":16,"endpoints":[["1","17","217"],["1","0","132"]]},{"normal":["44","1","-1"],"segments":9,"endpoints":[["1","17","61"],["1","11","55"]]},{"normal":["88","3","-1"],"segments":7,"endpoints":[["1","4","100"],["1","0","88"]]},{"normal":["88","7","-3"],"segments":5,"endpoints":[["1","17","69"],["1","11","55"]]},{"normal":["132","-7","-1"],"segments":14,"endpoints":[["1","9","69"],["1","11","55"]]},{"normal":["153","8","-1"],"segments":7,"endpoints":[["1","9","225"],["1","0","153"]]},{"normal":["153","5","-4"],"segments":1,"endpoints":[["3","1","116"],["4","0","153"]]},{"normal":["117","-2","-2"],"segments":42,"endpoints":[["2","5","112"],["2","34","83"]]},{"normal":["198","8","-1"],"segments":5,"endpoints":[["1","4","230"],["1","0","198"]]},{"normal":["198","5","-4"],"segments":11,"endpoints":[["2","8","109"],["2","0","99"]]},{"normal":["306","17","-1"],"segments":8,"endpoints":[["1","17","595"],["1","0","306"]]},{"normal":["234","-1","-1"],"segments":43,"endpoints":[["1","4","230"],["2","73","395"]]}];
const rows=[{"i":2015,"a":"581658328694552","b":"1388666508280039","r":["513","8","-10"],"local":104,"vertices":[["408","7","-8"],["105","1","-2"]],"sides":[{"side":1,"supports":28,"events":["1,126,126","1,43,87","1,53,87","1,92,126","10,1197,1260","11,1071,1386","111,5423,8695","113,10540,14238","113,6562,9831","122,25655,24095","123,5926,9635","138,85,7208","14,1369,1764","15,481,1175","15,697,1175","16,272,1027","18,835,1410","18,965,1566","19,2520,2394","190,11147,16530","190,17933,23940","2,121,174","2,255,252","2,371,395","2,395,395","2,99,174","20,4981,3950","216,10081,16920","22,1479,1914","22,374,1411","22,965,1914","23,1275,2001","23,2601,2898","24,771,1880","249,7990,19505","267,3768,16624","28,1191,2436","3,1,155","3,103,235","3,133,235","3,196,261","3,283,378","339,17034,26555","37,2085,3219","37,3333,4662","38,17,1972","38,7900,7505","46,10064,9085","5,306,435","5,592,630","570,28917,44650","6,271,470","61,8180,7686","66,2505,5170","69,2941,5405","697,38694,60639","697,61704,87822","7,95,427","72,3863,6264","8,1501,1580","84,3287,6580","863,71,44155","9,114,530","9,120,544","9,153,550","9,775,1134"]},{"side":-1,"supports":28,"events":["1,108,126","1,59,87","1,63,87","10,1139,1260","12,503,940","129,6145,11223","14,1551,1764","1407,44069,110215","15,198,902","15,493,1175","159,6733,12455","18,187,1067","18,683,1410","20,4709,3950","21,297,1309","21,773,1645","25,17,1309","265,11109,23055","267,11611,20915","28,6677,5530","3,111,235","3,51,187","32,415,1907","36,1795,2820","37,1617,3219","37,34,1955","37,4620,4662","387,18773,30315","4,185,348","5,238,435","5,73,317","6,219,470","74,20251,14615","795,25709,62275","8,1397,1580","89,3723,7743","9,153,554","9,361,705"]}]},{"i":3639,"a":"1116256337432","b":"2233091371303399","r":["7191","302","-188"],"local":93,"vertices":[["2601","123","-68"],["11781","481","-308"]],"sides":[{"side":1,"supports":27,"events":["1,27,87","1,30,87","106,2933,9222","11,187,731","115,3281,10005","119,3713,10353","119,6677,14994","125,2059,8471","137,2047,8795","14,1369,2765","14,1408,2765","16,385,1279","17,289,1157","17,471,1479","19,1012,2394","19,531,1653","19,583,1653","197,5377,17139","2,99,252","21,583,1827","22,607,1914","23,565,1827","235,6699,20445","238,24222,47005","251,13068,31626","251,7647,21837","267,3768,16624","27,667,2141","295,7277,23403","31,760,2464","3145,92673,273615","32,3173,6320","329,9649,28623","35,1089,3045","35,1947,4410","35,991,3045","36,1063,3132","38,3597,7505","39,958,3098","4,29,205","4,97,319","474,13973,41238","49,2718,6174","5,137,435","5,149,435","501,14861,43587","502,46013,99145","61,1031,4195","7,95,427","719,19893,62553","75,2029,6525","8,223,696","83,2074,6558","83,2451,7221","83,4284,10458","9,114,530","9,120,544"]},{"side":-1,"supports":28,"events":["1,17,66","1,30,87","1,56,126","103,1122,5742","105,1584,6776","113,1372,6516","13,194,834","14,108,711","15,198,902","2,15,102","2,203,395","21,297,1309","237,2772,13420","24,655,2088","29,439,1875","302,2326,15341","32,415,1907","36,1093,3132","38,293,1930","38,295,1928","4,101,315","4,29,205","469,14577,40803","47,745,3117","5,58,282","5,73,317","55,1403,4317","6,167,522","7,104,448","7,110,462","7,340,882","7,76,392","73,1853,5739","76,935,4411","8,136,527","8,59,409","83,1012,4796","9,218,718"]}]}];
console.log(JSON.stringify(replayUnion(data,rows),null,2));
```

## Full executed output
```json
{
  "output": [
    {
      "i": 2015,
      "side": -1,
      "supports": 28,
      "labels": [
        0,
        1,
        3,
        4,
        5,
        13,
        14,
        15,
        16,
        17,
        18,
        20,
        21,
        22,
        30,
        31,
        32,
        33,
        34,
        35,
        37,
        38,
        39,
        40,
        42,
        43,
        45,
        46
      ],
      "events": 38,
      "distinct": 38,
      "unionPatterns": 2381,
      "union": {
        "feasible": false,
        "states": 2,
        "rootLegal": 1
      },
      "root": {
        "checks": 2381,
        "minExcess": 0,
        "minLargest": 15,
        "sumGatePass": 210,
        "totalPass": 1,
        "distinctRootSuccessorPairs": 1,
        "histogram": {
          "0": 17,
          "1": 63,
          "2": 130,
          "3": 229,
          "4": 321,
          "5": 393,
          "6": 422,
          "7": 352,
          "8": 239,
          "9": 128,
          "10": 63,
          "11": 21,
          "12": 3
        }
      },
      "antichain": {
        "feasible": false,
        "states": 2,
        "eligible": 1,
        "minimal": 1,
        "rootEligible": 1,
        "rootMinimal": 1
      },
      "results": [
        {
          "kind": "open",
          "r": [
            "4795",
            "82",
            "-94"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "301677",
            "5159",
            "-5914"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "27344",
            "467",
            "-536"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "26451",
            "445",
            "-518"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "17568",
            "295",
            "-344"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "78957",
            "1325",
            "-1546"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "128097",
            "2120",
            "-2506"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "177237",
            "2915",
            "-3466"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "91329",
            "1502",
            "-1786"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "5421",
            "89",
            "-106"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "16162",
            "265",
            "-316"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "10741",
            "176",
            "-210"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "55078",
            "891",
            "-1076"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "44337",
            "715",
            "-866"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "9319",
            "150",
            "-182"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "11577",
            "185",
            "-226"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "16739",
            "257",
            "-326"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "21901",
            "329",
            "-426"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "23238",
            "349",
            "-452"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1337",
            "20",
            "-26"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "206",
            "3",
            "-4"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "11847",
            "172",
            "-230"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "34309",
            "497",
            "-666"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "22462",
            "325",
            "-436"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "67079",
            "970",
            "-1302"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "44617",
            "645",
            "-866"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "46164",
            "667",
            "-896"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1547",
            "22",
            "-30"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "7016",
            "99",
            "-136"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "5469",
            "77",
            "-106"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "3199",
            "45",
            "-62"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "929",
            "13",
            "-18"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "5788",
            "79",
            "-112"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "4859",
            "66",
            "-94"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "517",
            "7",
            "-10"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "828",
            "11",
            "-16"
          ],
          "patterns": 2065,
          "distinctMaskPatterns": 2065,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "4249",
            "55",
            "-82"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "11919",
            "154",
            "-230"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "14512",
            "187",
            "-280"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "2593",
            "33",
            "-50"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "116664",
            "1463",
            "-2248"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "114071",
            "1430",
            "-2198"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "122690",
            "1537",
            "-2364"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "8619",
            "107",
            "-166"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "12258",
            "151",
            "-236"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "3639",
            "44",
            "-70"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "17476",
            "209",
            "-336"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "48789",
            "583",
            "-938"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "530470",
            "6303",
            "-10196"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "481681",
            "5720",
            "-9258"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "165349",
            "1963",
            "-3178"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "14366",
            "169",
            "-276"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "66947",
            "785",
            "-1286"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "52581",
            "616",
            "-1010"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "137064",
            "1595",
            "-2632"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "84483",
            "979",
            "-1622"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "44273",
            "513",
            "-850"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "4063",
            "47",
            "-78"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "39931",
            "454",
            "-766"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "35868",
            "407",
            "-688"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "7403",
            "84",
            "-142"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "1147",
            "13",
            "-22"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "31126",
            "339",
            "-596"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "29979",
            "326",
            "-574"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "36150",
            "391",
            "-692"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "6171",
            "65",
            "-118"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "1151",
            "12",
            "-22"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "12245",
            "127",
            "-234"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "16223",
            "168",
            "-310"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "3978",
            "41",
            "-76"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "142727",
            "1460",
            "-2726"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "138749",
            "1419",
            "-2650"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "27232",
            "277",
            "-520"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "160803",
            "1628",
            "-3070"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "87059",
            "880",
            "-1662"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "13315",
            "132",
            "-254"
          ],
          "patterns": 2079,
          "distinctMaskPatterns": 2079,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "13420",
            "133",
            "-256"
          ],
          "patterns": 2085,
          "distinctMaskPatterns": 2085,
          "feasible": false,
          "proof": "union"
        }
      ],
      "excluded": true
    },
    {
      "i": 3639,
      "side": -1,
      "supports": 28,
      "labels": [
        0,
        1,
        3,
        4,
        5,
        13,
        14,
        15,
        16,
        17,
        18,
        21,
        22,
        30,
        31,
        32,
        33,
        34,
        35,
        37,
        38,
        39,
        40,
        42,
        43,
        44,
        45,
        46
      ],
      "events": 38,
      "distinct": 36,
      "unionPatterns": 2479,
      "union": {
        "feasible": false,
        "states": 10,
        "rootLegal": 2
      },
      "root": {
        "checks": 2479,
        "minExcess": 0,
        "minLargest": 15,
        "sumGatePass": 236,
        "totalPass": 2,
        "distinctRootSuccessorPairs": 2,
        "histogram": {
          "0": 17,
          "1": 56,
          "2": 163,
          "3": 265,
          "4": 355,
          "5": 374,
          "6": 370,
          "7": 305,
          "8": 217,
          "9": 167,
          "10": 114,
          "11": 54,
          "12": 19,
          "13": 3
        }
      },
      "antichain": {
        "feasible": false,
        "states": 10,
        "eligible": 22,
        "minimal": 9,
        "rootEligible": 2,
        "rootMinimal": 2
      },
      "results": [
        {
          "kind": "open",
          "r": [
            "18207",
            "860",
            "-476"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "52020",
            "2457",
            "-1360"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "1377",
            "65",
            "-36"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "4437",
            "208",
            "-116"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "3060",
            "143",
            "-80"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "20043",
            "936",
            "-524"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "44676",
            "2071",
            "-1168"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "113985",
            "5277",
            "-2980"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "43605",
            "2018",
            "-1140"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "16830",
            "777",
            "-440"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "42381",
            "1947",
            "-1108"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "25551",
            "1170",
            "-668"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "153",
            "7",
            "-4"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "9027",
            "412",
            "-236"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "76194",
            "3475",
            "-1992"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "67167",
            "3063",
            "-1756"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "309519",
            "14102",
            "-8092"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "242352",
            "11039",
            "-6336"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "136017",
            "6193",
            "-3556"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "29682",
            "1347",
            "-776"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "22797",
            "1034",
            "-596"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "15912",
            "721",
            "-416"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "9027",
            "408",
            "-236"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "11169",
            "503",
            "-292"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "14841",
            "666",
            "-388"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "33354",
            "1495",
            "-872"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "78795",
            "3518",
            "-2060"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "45441",
            "2023",
            "-1188"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "46206",
            "2057",
            "-1208"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "765",
            "34",
            "-20"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "31059",
            "1347",
            "-812"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "30294",
            "1313",
            "-792"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "93789",
            "4045",
            "-2452"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "63495",
            "2732",
            "-1660"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "75123",
            "3229",
            "-1964"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "11628",
            "497",
            "-304"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "14229",
            "608",
            "-372"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "2601",
            "111",
            "-68"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "18054",
            "769",
            "-472"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "177939",
            "7579",
            "-4652"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "31824",
            "1355",
            "-832"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "44829",
            "1906",
            "-1172"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "45135",
            "1919",
            "-1180"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "306",
            "13",
            "-8"
          ],
          "patterns": 2183,
          "distinctMaskPatterns": 2183,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "143361",
            "6029",
            "-3748"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "143055",
            "6016",
            "-3740"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "31365",
            "1319",
            "-820"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "45135",
            "1898",
            "-1180"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "102357",
            "4301",
            "-2676"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "57222",
            "2403",
            "-1496"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "24939",
            "1047",
            "-652"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "167229",
            "7020",
            "-4372"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "30447",
            "1278",
            "-796"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "15453",
            "648",
            "-404"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "24327",
            "1019",
            "-636"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "154836",
            "6485",
            "-4048"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "91188",
            "3815",
            "-2384"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "209916",
            "8775",
            "-5488"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "164475",
            "6854",
            "-4300"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "283509",
            "11787",
            "-7412"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "62271",
            "2580",
            "-1628"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "214659",
            "8853",
            "-5612"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "638775",
            "26272",
            "-16700"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "424116",
            "17419",
            "-11088"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "428553",
            "17601",
            "-11204"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "4437",
            "182",
            "-116"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "57528",
            "2359",
            "-1504"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "743427",
            "30485",
            "-19436"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "751995",
            "30836",
            "-19660"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "8568",
            "351",
            "-224"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "2907",
            "119",
            "-76"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "event",
          "r": [
            "8874",
            "363",
            "-232"
          ],
          "patterns": 2201,
          "distinctMaskPatterns": 2201,
          "feasible": false,
          "proof": "union"
        },
        {
          "kind": "open",
          "r": [
            "20655",
            "844",
            "-540"
          ],
          "patterns": 2207,
          "distinctMaskPatterns": 2207,
          "feasible": false,
          "proof": "union"
        }
      ],
      "excluded": true
    }
  ],
  "excluded": [
    2015,
    3639
  ],
  "strata": 150,
  "totalPatterns": 321228
}
```

## Next
Apply the exact lift criterion to only capacity-eligible cone pairs by constructing a restricted determinant arrangement; compare candidate loss against R209. Continue rank-two event replay on 2912/3610 or remaining smallest actual event count. Independent review and Activity association pending.
