# X6 R209 — Bilinear cone extreme-ray and joint cross-product capacity envelope

2026-11-26. AUTHOR PROOF AND EXECUTED EXACT COMPUTATION / NOT_REVIEWED. Informed auxiliary coefficient-chart research, not native dynamics. Frozen inputs unchanged: Port 10, 1,935 integer directions, six joint BRC pair relations, strict 3/2, w=(17t,B,22t,D), 47 support labels, 49 actual components, 51 original endpoint rays. Source R208 11a060742f69b49199477a7fa0cb42101eac4d7d:research_notes/portable_direct/2026-11-26_r2_x6_r208_rank_three_static_envelope.md, blob 8cd94f48ad46efbe94b5a01077c91719abe66093; frozen R181 census eb87794b9f9b2a6d600a2d12c37d49855b436bca:research_notes/portable_direct/x6_r181_local_event_census.json, blob d221356b478797a2869a19f0c0261ea412ec7081; R207 1b39b52429981b357c13f7ea3e8511f57347d244. R208 remaining 65 IDs only; no repin. R182 one-child theorem 502d7abb2fe8470ed2cdabf242c2cc59a0c302ac, R205 root budget 37258ff0d0fa6602eb16a4bd9b499f2fcb0e9f8f. Current task query r2-20261126-0607-x6-read SUCCEEDED Source 0b29b31491a5feae7416aab23bda0842e29586ae, directory absent only, no native owner projection, no CLAIM or shared state change; own researcher binding unconfirmed. P000 V5 and ACTIVE worldview unchanged.

## Proof
Fix the root ternary class C and one child side with retained endpoint origin descriptors from R207. The second nonzero normal q belongs to an oriented ternary class D of the same static 51-ray arrangement (choose one sign orientation because reversing q swaps its children). Both closed cones are pointed, since the common kernel of the spanning 51 rays is zero. Each extreme ray lies on two independent original walls; conversely every ray used by the R207 lexicographic perturbation is a closure ray of the produced class. Enumerating all pairwise cross products and all tangent boundary directions/sectors as R207 therefore records every extreme ray of each cone up to oriented positive scaling. The code additionally verifies closure membership and that the sum is in the relative interior. Every r in C can be expressed as a linear combination with strictly positive coefficients on *all* recorded extreme rays R_i: subtract sufficiently small positive multiples of all rays, staying in the closed cone by relative interior, then express the remainder nonnegatively. Likewise q in D with Q_j. Thus r cross q = sum_{i,j} alpha_i beta_j (R_i cross Q_j), all products strictly positive.

For original endpoints a,b whose root signs are opposite, a positive moving representative is sign(r dot a)*[(r dot a)b-(r dot b)a]. Its q-observation is sign(r dot a)*(r cross q) dot (a cross b). This formula includes either ordering of endpoints, either child, and q parallel r. For support normal n_k parallel to a cross b, moving sign is epsilon_k sign((r cross q) dot n_k), with epsilon_k=sign(r dot a)*sign((a cross b) dot n_k). Exact proportionality is checked. Fixed endpoints retain q's static sign. For each moving label k inspect the finite values (R_i cross Q_j) dot n_k. If all zero the actual sign is zero; if all weakly positive and some strict, actual sign is positive (analogously negative). If both strict signs occur allow all three. The mixed case indeed permits each sign individually by approaching the two extreme pairs from relative interiors and continuity, but choices across labels are coupled. Hence the extreme-pair envelope is sound, refines R207, and handles all root parameter equalities internal to the class. It is exact for a single moving sign, not necessarily jointly exact.

For a further sound relaxation, enumerate the entire central arrangement of the 47 support normals in auxiliary three-space, both orientations and the zero sign vector (r cross q can vanish). The same R207 completeness proof applies. Keep only patterns respecting every extreme-pair mask for this root/observer cone pair. All actual moving signs appear in this joint bank, regardless of feasibility of lifting a pattern to the specific r and q. For each candidate, compute positive and negative successor support counts using the labeled retained endpoints; if no pattern has both <=15 for any q class, the child depth-five necessary capacity fails globally. By R182 the whole root class is excluded. No claim that surviving patterns lift, or that a passing root admits a decision tree. No parameter subdivisions or recursive capacity calls. No support identity, disconnected-component origin, or joint BRC relationship is erased.

## Executed evidence
Executed in JavaScript tool runtime; all vector operations BigInt, counts small exact integers. Enumerated all 65 R208 survivor IDs both sides; root masks, support normal proportionality, arrangement span, closure membership, relative-interior sum, static forced sign preservation, and rank counts checked. Full output below; inherited proofs not independently reviewed. New exclusions 15; extreme-envelope-only exclusions 15; remaining 50. Overall bound 6<=D_linear<=7 unless all classes exhausted (not claimed). Passing joint patterns may still violate cross-product lift or later depth constraints. Next: examine the residual pairs using exact projective line-transversal feasibility for r cross q, or R204/R206 recursive union certificates. No runtime speedup claimed.

## Reproduction
Extract the JS below to a .cjs file, use the immutable census named x6_r181_local_event_census.json in the same directory. Embedded static data and survivor IDs originate from R208; full output follows.

```javascript
function compute(data,census,ids){
 const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],sg=x=>x>0n?1:x<0n?-1:0, neg=a=>a.map(x=>-x),gcd=(a,b)=>b===0n?(a<0n?-a:a):gcd(b,a%b),primitive=a=>{let d=a.reduce(gcd,0n);return a.map(x=>x/d)}, canon=s=>{let a=s.join(),b=neg(s).join();return b<a?[b,-1]:[a,1]};
 const P=[...new Map(data.flatMap(e=>e.endpoints).map(p=>[p.join(),p.map(BigInt)])).values()],idx=new Map(P.map((p,i)=>[p.join(),i])),N=data.map(e=>e.normal.map(BigInt));
 const comps=data.map(e=>e.normal.join()==="51,2,-1"?[[["1","9","69"],["3","17","187"]],[["2","5","112"],["1","0","51"]]]:e.normal.join()==="17,-1,0"?[[["0","0","1"],["1","17","391"]],[["1","17","69"],["1","17","22"]]]:[e.endpoints]).map(parts=>parts.map(pair=>pair.map(p=>{let i=idx.get(p.join());if(i===undefined)throw Error("missing endpoint");return i})));
 function arrangement(P){
  if(!P.some(a=>P.some(b=>P.some(c=>dot(a,cross(b,c))!==0n))))throw Error("not rank three");
  const bank=new Map();
  function rec(r,t=null,p=null,s=1,u=1){let signs=P.map(x=>sg(dot(r,x))||(t?s*sg(dot(t,x)):0)||(p?u*sg(dot(p,x)):0));const [key,flip]=canon(signs);let entry=bank.get(key);if(!entry){entry={s:signs.map(x=>x*flip),rays:new Map()};bank.set(key,entry)}let z=primitive(r.map(x=>x*BigInt(flip)));entry.rays.set(z.join(),z)}
  for(let i=0;i<P.length;i++)for(let j=i+1;j<P.length;j++){let r=cross(P[i],P[j]);if(!r.some(Boolean))continue;rec(r);for(let k=0;k<P.length;k++)if(!dot(r,P[k])){let t=cross(r,P[k]);for(let s of [-1,1]){rec(r,t,null,s);for(let u of [-1,1])rec(r,t,P[k],s,u)}}}
  for(let entry of bank.values()){entry.rays=[...entry.rays.values()];let sum=[0n,0n,0n];for(const r of entry.rays){P.forEach((p,i)=>{let x=sg(dot(r,p));if(x&&x!==entry.s[i])throw Error("ray not in closure")});sum=sum.map((x,i)=>x+r[i])}if(P.some((p,i)=>sg(dot(sum,p))!==entry.s[i]))throw Error("sum not relative interior")}
  return bank
 }
 const bank=arrangement(P),wBank=arrangement(N);
 if(P.length!==51||N.length!==47||bank.size!==4249)throw Error("bank mismatch");
 // All oriented w sign patterns and zero; sign bits -/0/+ are 1/2/4.
 const W=[[...N.map(()=>0)],...[...wBank.values()].flatMap(x=>[x.s,neg(x.s)])],bit=s=>1<<(s+1);
 const rows=ids.map(id=>{let row=census.details.find(x=>x.i===id);if(!row)throw Error("missing root "+id);return row});
 if(new Set(ids).size!==65||rows.filter(x=>x.dim===2).length!==28||rows.filter(x=>x.dim===3).length!==37)throw Error("frontier mismatch");
 let res=[],pairCount=0,wChecks=0,strictMaskChecks=0;
 for(const row of rows){
  let a=BigInt(row.a),b=BigInt(row.b),rr=row.r.map(BigInt),rs=P.map((p,i)=>{let x=sg(dot(rr,p)),y=a&(1n<<BigInt(i))?1:b&(1n<<BigInt(i))?-1:0;if(x!==y)throw Error("root mask mismatch");return x});
  const [key,flip]=canon(rs),rentry=bank.get(key);if(!rentry)throw Error("root missing");
  let R=rentry.rays.map(r=>flip===1?r:neg(r));
  for(let side of [1,-1]){
   const clipped=[];
   function descriptor(i,j,k){if(i===j)return {fixed:i};const v=cross(P[i],P[j]),n=N[k],s=sg(dot(v,n))*rs[i];if(!s||rs[i]*rs[j]!==-1||cross(v,n).some(Boolean))throw Error("bad moving orientation");return {i,j,k,s}}
   for(let k=0;k<comps.length;k++){let keep=[];for(let [i,j] of comps[k]){let x=rs[i]*side,y=rs[j]*side;if(x<=0&&y<=0)continue;keep.push([x<0?descriptor(i,j,k):{fixed:i},y<0?descriptor(i,j,k):{fixed:j}])}if(keep.length)clipped.push([keep[0][0],keep.at(-1)[1]])}
   if(clipped.length<=5||clipped.length>31)throw Error("bad support count");
   let staticPass=0,extremePass=0,jointPass=0,extremePairs=0,localW=0;const moving=[...new Set(clipped.flat().filter(x=>x.fixed===undefined).map(x=>x.k))];
   for(let q of bank.values()){
    const force=x=>{if(x.fixed!==undefined)return q.s[x.fixed];let a=q.s[x.i],b=q.s[x.j];return a*b<0?0:a||b};
    const counts=fn=>{let pos=0,neg=0;for(let [a,b] of clipped){let x=fn(a),y=fn(b);pos+=x===1||y===1;neg+=x===-1||y===-1}return [pos,neg]};
    const feasible=a=>a[0]<=15&&a[1]<=15;
    if(!feasible(counts(force)))continue;staticPass++;
    let masks=Array(N.length).fill(0);
    for(const r of R)for(const z of q.rays){let w=cross(r,z);extremePairs++;for(let k of moving)masks[k]|=bit(sg(dot(w,N[k])))}
    // A positive mixture of all pair values: mixed strict signs => -/0/+;
    // otherwise a nonzero same-sign pair forces that strict sign.
    for(let k of moving){let m=masks[k];masks[k]=(m&1)&&(m&4)?7:(m&1)?1:(m&4)?4:2}
    const force2=x=>{if(x.fixed!==undefined)return q.s[x.fixed];let m=masks[x.k],t=(m===1?-1:m===4?1:0)*x.s;let old=force(x);strictMaskChecks++;if(old&&old!==t)throw Error("extreme loses static sign");return t};
    if(!feasible(counts(force2)))continue;extremePass++;
    // Exact joint w-arrangement relaxation, not full (r,q) feasibility.
    let possible=false;
    for(const w of W){localW++;if(!moving.every(k=>masks[k]&bit(w[k])))continue;let c=counts(x=>x.fixed!==undefined?q.s[x.fixed]:x.s*w[x.k]);if(feasible(c)){possible=true;break}}
    if(possible)jointPass++;
   }
   pairCount+=extremePairs;wChecks+=localW;
   res.push({i:row.i,dim:row.dim,side,N:clipped.length,moving:moving.length,staticPass,extremePass,jointPass,extremePairs,wChecks:localW});
  }
 }
 const excluded=ids.filter(i=>res.some(x=>x.i===i&&x.jointPass===0)),extremeExcluded=ids.filter(i=>res.some(x=>x.i===i&&x.extremePass===0));
 return {P:P.length,bank:bank.size,wBank:wBank.size,orientedW:W.length,extremePairs:pairCount,wChecks,strictMaskChecks,extremeExcluded,excluded,survivors:ids.filter(i=>!excluded.includes(i)),rows:res}
}
const data=[{"normal":["187","12","-1"],"segments":9,"endpoints":[["0","1","12"],["1","17","391"]]},{"normal":["204","11","-1"],"segments":9,"endpoints":[["0","1","11"],["1","17","391"]]},{"normal":["5","-2","0"],"segments":51,"endpoints":[["2","5","73"],["2","5","5"]]},{"normal":["9","-1","0"],"segments":4,"endpoints":[["1","9","74"],["1","9","69"]]},{"normal":["85","7","-2"],"segments":10,"endpoints":[["1","9","74"],["3","17","187"]]},{"normal":["51","2","-1"],"segments":9,"endpoints":[["1","9","69"],["1","0","51"]]},{"normal":["0","1","-1"],"segments":2,"endpoints":[["2","5","5"],["1","0","0"]]},{"normal":["34","1","-1"],"segments":7,"endpoints":[["2","5","73"],["1","0","34"]]},{"normal":["187","20","-9"],"segments":5,"endpoints":[["6","15","158"],["1","1","23"]]},{"normal":["68","1","-3"],"segments":8,"endpoints":[["2","5","47"],["3","0","68"]]},{"normal":["176","22","-9"],"segments":4,"endpoints":[["6","15","154"],["19","28","440"]]},{"normal":["22","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","22"]]},{"normal":["61","0","-1"],"segments":78,"endpoints":[["0","1","0"],["1","17","61"]]},{"normal":["74","0","-1"],"segments":14,"endpoints":[["1","9","74"],["1","4","74"]]},{"normal":["126","0","-1"],"segments":103,"endpoints":[["0","1","0"],["1","30","126"]]},{"normal":["4","-1","0"],"segments":35,"endpoints":[["1","4","152"],["1","4","74"]]},{"normal":["17","-1","0"],"segments":44,"endpoints":[["0","0","1"],["1","17","22"]]},{"normal":["156","-1","-1"],"segments":46,"endpoints":[["1","4","152"],["1","30","126"]]},{"normal":["69","0","-1"],"segments":16,"endpoints":[["1","17","69"],["1","9","69"]]},{"normal":["9","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","9"]]},{"normal":["235","0","-3"],"segments":84,"endpoints":[["0","1","0"],["3","77","235"]]},{"normal":["87","0","-1"],"segments":107,"endpoints":[["0","1","0"],["1","17","87"]]},{"normal":["104","-1","-1"],"segments":60,"endpoints":[["1","4","100"],["3","77","235"]]},{"normal":["38","0","-3"],"segments":57,"endpoints":[["0","1","0"],["3","40","38"]]},{"normal":["5","0","-2"],"segments":72,"endpoints":[["0","1","0"],["2","5","5"]]},{"normal":["39","-1","-1"],"segments":50,"endpoints":[["3","1","116"],["1","17","22"]]},{"normal":["40","0","-3"],"segments":63,"endpoints":[["0","1","0"],["3","38","40"]]},{"normal":["26","-1","-1"],"segments":39,"endpoints":[["2","5","47"],["3","53","25"]]},{"normal":["25","0","-3"],"segments":52,"endpoints":[["0","1","0"],["3","53","25"]]},{"normal":["83","0","-2"],"segments":69,"endpoints":[["0","1","0"],["2","34","83"]]},{"normal":["102","-7","-1"],"segments":14,"endpoints":[["1","4","74"],["3","17","187"]]},{"normal":["204","-11","1"],"segments":51,"endpoints":[["0","1","11"],["1","30","126"]]},{"normal":["395","0","-2"],"segments":119,"endpoints":[["0","1","0"],["2","73","395"]]},{"normal":["289","18","-1"],"segments":10,"endpoints":[["0","1","18"],["1","17","595"]]},{"normal":["66","2","-1"],"segments":11,"endpoints":[["1","4","74"],["1","0","66"]]},{"normal":["132","5","-1"],"segments":16,"endpoints":[["1","17","217"],["1","0","132"]]},{"normal":["44","1","-1"],"segments":9,"endpoints":[["1","17","61"],["1","11","55"]]},{"normal":["88","3","-1"],"segments":7,"endpoints":[["1","4","100"],["1","0","88"]]},{"normal":["88","7","-3"],"segments":5,"endpoints":[["1","17","69"],["1","11","55"]]},{"normal":["132","-7","-1"],"segments":14,"endpoints":[["1","9","69"],["1","11","55"]]},{"normal":["153","8","-1"],"segments":7,"endpoints":[["1","9","225"],["1","0","153"]]},{"normal":["153","5","-4"],"segments":1,"endpoints":[["3","1","116"],["4","0","153"]]},{"normal":["117","-2","-2"],"segments":42,"endpoints":[["2","5","112"],["2","34","83"]]},{"normal":["198","8","-1"],"segments":5,"endpoints":[["1","4","230"],["1","0","198"]]},{"normal":["198","5","-4"],"segments":11,"endpoints":[["2","8","109"],["2","0","99"]]},{"normal":["306","17","-1"],"segments":8,"endpoints":[["1","17","595"],["1","0","306"]]},{"normal":["234","-1","-1"],"segments":43,"endpoints":[["1","4","230"],["2","73","395"]]}];
const ids=[889,1205,1215,1219,1361,1364,1406,1439,1477,1607,1659,1914,2015,2187,2510,2775,2912,3073,3266,3282,3535,3609,3610,3635,3638,3639,3826,3996,768,769,851,852,890,891,1206,1214,1216,1363,1476,1486,1488,1661,1915,1916,1944,1946,1947,2186,2188,2473,2511,2512,2966,3248,3395,3409,3454,3488,3591,3607,3608,3636,3637,3652,3911];
const census=require('./x6_r181_local_event_census.json');
console.log(JSON.stringify(compute(data,census,ids),null,2));
```

```json
{
  "P": 51,
  "bank": 4249,
  "wBank": 3445,
  "orientedW": 6891,
  "extremePairs": 14025,
  "wChecks": 1589222,
  "strictMaskChecks": 18116,
  "extremeExcluded": [
    1361,
    1364,
    1406,
    1914,
    3073,
    3282,
    3535,
    1363,
    1915,
    1916,
    2473,
    2966,
    3248,
    3488,
    3911
  ],
  "excluded": [
    1361,
    1364,
    1406,
    1914,
    3073,
    3282,
    3535,
    1363,
    1915,
    1916,
    2473,
    2966,
    3248,
    3488,
    3911
  ],
  "survivors": [
    889,
    1205,
    1215,
    1219,
    1439,
    1477,
    1607,
    1659,
    2015,
    2187,
    2510,
    2775,
    2912,
    3266,
    3609,
    3610,
    3635,
    3638,
    3639,
    3826,
    3996,
    768,
    769,
    851,
    852,
    890,
    891,
    1206,
    1214,
    1216,
    1476,
    1486,
    1488,
    1661,
    1944,
    1946,
    1947,
    2186,
    2188,
    2511,
    2512,
    3395,
    3409,
    3454,
    3591,
    3607,
    3608,
    3636,
    3637,
    3652
  ],
  "rows": [
    {
      "i": 889,
      "dim": 2,
      "side": 1,
      "N": 28,
      "moving": 8,
      "staticPass": 7,
      "extremePass": 7,
      "jointPass": 7,
      "extremePairs": 20,
      "wChecks": 1390
    },
    {
      "i": 889,
      "dim": 2,
      "side": -1,
      "N": 28,
      "moving": 8,
      "staticPass": 77,
      "extremePass": 69,
      "jointPass": 69,
      "extremePairs": 320,
      "wChecks": 85552
    },
    {
      "i": 1205,
      "dim": 2,
      "side": 1,
      "N": 30,
      "moving": 12,
      "staticPass": 1,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 2,
      "wChecks": 1514
    },
    {
      "i": 1205,
      "dim": 2,
      "side": -1,
      "N": 29,
      "moving": 12,
      "staticPass": 3,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 6,
      "wChecks": 1468
    },
    {
      "i": 1215,
      "dim": 2,
      "side": 1,
      "N": 29,
      "moving": 11,
      "staticPass": 1,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 2,
      "wChecks": 1514
    },
    {
      "i": 1215,
      "dim": 2,
      "side": -1,
      "N": 29,
      "moving": 11,
      "staticPass": 3,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 6,
      "wChecks": 1468
    },
    {
      "i": 1219,
      "dim": 2,
      "side": 1,
      "N": 29,
      "moving": 11,
      "staticPass": 1,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 2,
      "wChecks": 1514
    },
    {
      "i": 1219,
      "dim": 2,
      "side": -1,
      "N": 29,
      "moving": 11,
      "staticPass": 3,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 6,
      "wChecks": 1468
    },
    {
      "i": 1361,
      "dim": 2,
      "side": 1,
      "N": 31,
      "moving": 13,
      "staticPass": 1,
      "extremePass": 0,
      "jointPass": 0,
      "extremePairs": 2,
      "wChecks": 0
    },
    {
      "i": 1361,
      "dim": 2,
      "side": -1,
      "N": 29,
      "moving": 13,
      "staticPass": 2,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 6,
      "wChecks": 1469
    },
    {
      "i": 1364,
      "dim": 2,
      "side": 1,
      "N": 30,
      "moving": 12,
      "staticPass": 4,
      "extremePass": 0,
      "jointPass": 0,
      "extremePairs": 12,
      "wChecks": 0
    },
    {
      "i": 1364,
      "dim": 2,
      "side": -1,
      "N": 29,
      "moving": 12,
      "staticPass": 1,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 2,
      "wChecks": 5
    },
    {
      "i": 1406,
      "dim": 2,
      "side": 1,
      "N": 31,
      "moving": 13,
      "staticPass": 1,
      "extremePass": 0,
      "jointPass": 0,
      "extremePairs": 2,
      "wChecks": 0
    },
    {
      "i": 1406,
      "dim": 2,
      "side": -1,
      "N": 29,
      "moving": 13,
      "staticPass": 2,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 6,
      "wChecks": 1469
    },
    {
      "i": 1439,
      "dim": 2,
      "side": 1,
      "N": 30,
      "moving": 11,
      "staticPass": 1,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 2,
      "wChecks": 1514
    },
    {
      "i": 1439,
      "dim": 2,
      "side": -1,
      "N": 28,
      "moving": 11,
      "staticPass": 21,
      "extremePass": 7,
      "jointPass": 7,
      "extremePairs": 70,
      "wChecks": 8980
    },
    {
      "i": 1477,
      "dim": 2,
      "side": 1,
      "N": 29,
      "moving": 8,
      "staticPass": 7,
      "extremePass": 6,
      "jointPass": 6,
      "extremePairs": 20,
      "wChecks": 1032
    },
    {
      "i": 1477,
      "dim": 2,
      "side": -1,
      "N": 27,
      "moving": 8,
      "staticPass": 125,
      "extremePass": 111,
      "jointPass": 111,
      "extremePairs": 530,
      "wChecks": 108947
    },
    {
      "i": 1607,
      "dim": 2,
      "side": 1,
      "N": 28,
      "moving": 11,
      "staticPass": 7,
      "extremePass": 7,
      "jointPass": 7,
      "extremePairs": 20,
      "wChecks": 10610
    },
    {
      "i": 1607,
      "dim": 2,
      "side": -1,
      "N": 30,
      "moving": 11,
      "staticPass": 1,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 2,
      "wChecks": 1468
    },
    {
      "i": 1659,
      "dim": 2,
      "side": 1,
      "N": 28,
      "moving": 7,
      "staticPass": 3,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 8,
      "wChecks": 300
    },
    {
      "i": 1659,
      "dim": 2,
      "side": -1,
      "N": 27,
      "moving": 7,
      "staticPass": 17,
      "extremePass": 11,
      "jointPass": 11,
      "extremePairs": 62,
      "wChecks": 27375
    },
    {
      "i": 1914,
      "dim": 2,
      "side": 1,
      "N": 27,
      "moving": 9,
      "staticPass": 8,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 22,
      "wChecks": 516
    },
    {
      "i": 1914,
      "dim": 2,
      "side": -1,
      "N": 29,
      "moving": 9,
      "staticPass": 1,
      "extremePass": 0,
      "jointPass": 0,
      "extremePairs": 2,
      "wChecks": 0
    },
    {
      "i": 2015,
      "dim": 2,
      "side": 1,
      "N": 28,
      "moving": 9,
      "staticPass": 3,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 8,
      "wChecks": 324
    },
    {
      "i": 2015,
      "dim": 2,
      "side": -1,
      "N": 28,
      "moving": 9,
      "staticPass": 3,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 8,
      "wChecks": 109
    },
    {
      "i": 2187,
      "dim": 2,
      "side": 1,
      "N": 27,
      "moving": 8,
      "staticPass": 11,
      "extremePass": 7,
      "jointPass": 7,
      "extremePairs": 32,
      "wChecks": 864
    },
    {
      "i": 2187,
      "dim": 2,
      "side": -1,
      "N": 29,
      "moving": 8,
      "staticPass": 22,
      "extremePass": 2,
      "jointPass": 2,
      "extremePairs": 88,
      "wChecks": 2457
    },
    {
      "i": 2510,
      "dim": 2,
      "side": 1,
      "N": 28,
      "moving": 10,
      "staticPass": 11,
      "extremePass": 8,
      "jointPass": 8,
      "extremePairs": 32,
      "wChecks": 8256
    },
    {
      "i": 2510,
      "dim": 2,
      "side": -1,
      "N": 30,
      "moving": 10,
      "staticPass": 8,
      "extremePass": 7,
      "jointPass": 7,
      "extremePairs": 22,
      "wChecks": 10028
    },
    {
      "i": 2775,
      "dim": 2,
      "side": 1,
      "N": 28,
      "moving": 9,
      "staticPass": 11,
      "extremePass": 8,
      "jointPass": 8,
      "extremePairs": 32,
      "wChecks": 8252
    },
    {
      "i": 2775,
      "dim": 2,
      "side": -1,
      "N": 29,
      "moving": 9,
      "staticPass": 45,
      "extremePass": 37,
      "jointPass": 37,
      "extremePairs": 180,
      "wChecks": 53820
    },
    {
      "i": 2912,
      "dim": 2,
      "side": 1,
      "N": 28,
      "moving": 11,
      "staticPass": 11,
      "extremePass": 8,
      "jointPass": 8,
      "extremePairs": 32,
      "wChecks": 8256
    },
    {
      "i": 2912,
      "dim": 2,
      "side": -1,
      "N": 31,
      "moving": 11,
      "staticPass": 2,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 4,
      "wChecks": 1468
    },
    {
      "i": 3073,
      "dim": 2,
      "side": 1,
      "N": 28,
      "moving": 9,
      "staticPass": 4,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 10,
      "wChecks": 522
    },
    {
      "i": 3073,
      "dim": 2,
      "side": -1,
      "N": 29,
      "moving": 9,
      "staticPass": 1,
      "extremePass": 0,
      "jointPass": 0,
      "extremePairs": 2,
      "wChecks": 0
    },
    {
      "i": 3266,
      "dim": 2,
      "side": 1,
      "N": 28,
      "moving": 7,
      "staticPass": 3,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 8,
      "wChecks": 300
    },
    {
      "i": 3266,
      "dim": 2,
      "side": -1,
      "N": 27,
      "moving": 7,
      "staticPass": 17,
      "extremePass": 11,
      "jointPass": 11,
      "extremePairs": 62,
      "wChecks": 27375
    },
    {
      "i": 3282,
      "dim": 2,
      "side": 1,
      "N": 26,
      "moving": 8,
      "staticPass": 17,
      "extremePass": 8,
      "jointPass": 8,
      "extremePairs": 50,
      "wChecks": 3349
    },
    {
      "i": 3282,
      "dim": 2,
      "side": -1,
      "N": 29,
      "moving": 8,
      "staticPass": 1,
      "extremePass": 0,
      "jointPass": 0,
      "extremePairs": 2,
      "wChecks": 0
    },
    {
      "i": 3535,
      "dim": 2,
      "side": 1,
      "N": 30,
      "moving": 13,
      "staticPass": 2,
      "extremePass": 0,
      "jointPass": 0,
      "extremePairs": 4,
      "wChecks": 0
    },
    {
      "i": 3535,
      "dim": 2,
      "side": -1,
      "N": 30,
      "moving": 13,
      "staticPass": 1,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 2,
      "wChecks": 191
    },
    {
      "i": 3609,
      "dim": 2,
      "side": 1,
      "N": 27,
      "moving": 7,
      "staticPass": 7,
      "extremePass": 7,
      "jointPass": 7,
      "extremePairs": 20,
      "wChecks": 14
    },
    {
      "i": 3609,
      "dim": 2,
      "side": -1,
      "N": 28,
      "moving": 7,
      "staticPass": 74,
      "extremePass": 18,
      "jointPass": 18,
      "extremePairs": 302,
      "wChecks": 20045
    },
    {
      "i": 3610,
      "dim": 2,
      "side": 1,
      "N": 26,
      "moving": 8,
      "staticPass": 16,
      "extremePass": 12,
      "jointPass": 12,
      "extremePairs": 44,
      "wChecks": 4186
    },
    {
      "i": 3610,
      "dim": 2,
      "side": -1,
      "N": 29,
      "moving": 8,
      "staticPass": 2,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 4,
      "wChecks": 2814
    },
    {
      "i": 3635,
      "dim": 2,
      "side": 1,
      "N": 27,
      "moving": 6,
      "staticPass": 3,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 8,
      "wChecks": 6
    },
    {
      "i": 3635,
      "dim": 2,
      "side": -1,
      "N": 27,
      "moving": 6,
      "staticPass": 65,
      "extremePass": 33,
      "jointPass": 33,
      "extremePairs": 246,
      "wChecks": 42244
    },
    {
      "i": 3638,
      "dim": 2,
      "side": 1,
      "N": 28,
      "moving": 7,
      "staticPass": 3,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 8,
      "wChecks": 6
    },
    {
      "i": 3638,
      "dim": 2,
      "side": -1,
      "N": 27,
      "moving": 7,
      "staticPass": 127,
      "extremePass": 45,
      "jointPass": 45,
      "extremePairs": 530,
      "wChecks": 50148
    },
    {
      "i": 3639,
      "dim": 2,
      "side": 1,
      "N": 27,
      "moving": 8,
      "staticPass": 7,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 20,
      "wChecks": 300
    },
    {
      "i": 3639,
      "dim": 2,
      "side": -1,
      "N": 28,
      "moving": 8,
      "staticPass": 10,
      "extremePass": 2,
      "jointPass": 2,
      "extremePairs": 34,
      "wChecks": 2915
    },
    {
      "i": 3826,
      "dim": 2,
      "side": 1,
      "N": 28,
      "moving": 7,
      "staticPass": 3,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 8,
      "wChecks": 6
    },
    {
      "i": 3826,
      "dim": 2,
      "side": -1,
      "N": 27,
      "moving": 7,
      "staticPass": 127,
      "extremePass": 45,
      "jointPass": 45,
      "extremePairs": 530,
      "wChecks": 50148
    },
    {
      "i": 3996,
      "dim": 2,
      "side": 1,
      "N": 29,
      "moving": 11,
      "staticPass": 5,
      "extremePass": 5,
      "jointPass": 5,
      "extremePairs": 14,
      "wChecks": 1016
    },
    {
      "i": 3996,
      "dim": 2,
      "side": -1,
      "N": 29,
      "moving": 11,
      "staticPass": 3,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 6,
      "wChecks": 190
    },
    {
      "i": 768,
      "dim": 3,
      "side": 1,
      "N": 30,
      "moving": 9,
      "staticPass": 1,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 3,
      "wChecks": 172
    },
    {
      "i": 768,
      "dim": 3,
      "side": -1,
      "N": 27,
      "moving": 9,
      "staticPass": 92,
      "extremePass": 73,
      "jointPass": 73,
      "extremePairs": 582,
      "wChecks": 90761
    },
    {
      "i": 769,
      "dim": 3,
      "side": 1,
      "N": 29,
      "moving": 9,
      "staticPass": 1,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 4,
      "wChecks": 1032
    },
    {
      "i": 769,
      "dim": 3,
      "side": -1,
      "N": 28,
      "moving": 9,
      "staticPass": 56,
      "extremePass": 40,
      "jointPass": 40,
      "extremePairs": 464,
      "wChecks": 53928
    },
    {
      "i": 851,
      "dim": 3,
      "side": 1,
      "N": 29,
      "moving": 10,
      "staticPass": 7,
      "extremePass": 6,
      "jointPass": 6,
      "extremePairs": 40,
      "wChecks": 1032
    },
    {
      "i": 851,
      "dim": 3,
      "side": -1,
      "N": 29,
      "moving": 10,
      "staticPass": 28,
      "extremePass": 10,
      "jointPass": 10,
      "extremePairs": 200,
      "wChecks": 12950
    },
    {
      "i": 852,
      "dim": 3,
      "side": 1,
      "N": 28,
      "moving": 10,
      "staticPass": 11,
      "extremePass": 8,
      "jointPass": 8,
      "extremePairs": 64,
      "wChecks": 8252
    },
    {
      "i": 852,
      "dim": 3,
      "side": -1,
      "N": 30,
      "moving": 10,
      "staticPass": 5,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 24,
      "wChecks": 1220
    },
    {
      "i": 890,
      "dim": 3,
      "side": 1,
      "N": 29,
      "moving": 9,
      "staticPass": 7,
      "extremePass": 6,
      "jointPass": 6,
      "extremePairs": 50,
      "wChecks": 1032
    },
    {
      "i": 890,
      "dim": 3,
      "side": -1,
      "N": 28,
      "moving": 9,
      "staticPass": 77,
      "extremePass": 69,
      "jointPass": 69,
      "extremePairs": 800,
      "wChecks": 85552
    },
    {
      "i": 891,
      "dim": 3,
      "side": 1,
      "N": 28,
      "moving": 9,
      "staticPass": 11,
      "extremePass": 8,
      "jointPass": 8,
      "extremePairs": 64,
      "wChecks": 8252
    },
    {
      "i": 891,
      "dim": 3,
      "side": -1,
      "N": 29,
      "moving": 9,
      "staticPass": 45,
      "extremePass": 37,
      "jointPass": 37,
      "extremePairs": 360,
      "wChecks": 53820
    },
    {
      "i": 1206,
      "dim": 3,
      "side": 1,
      "N": 30,
      "moving": 12,
      "staticPass": 1,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 4,
      "wChecks": 1514
    },
    {
      "i": 1206,
      "dim": 3,
      "side": -1,
      "N": 29,
      "moving": 12,
      "staticPass": 3,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 12,
      "wChecks": 1468
    },
    {
      "i": 1214,
      "dim": 3,
      "side": 1,
      "N": 29,
      "moving": 12,
      "staticPass": 1,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 4,
      "wChecks": 1514
    },
    {
      "i": 1214,
      "dim": 3,
      "side": -1,
      "N": 30,
      "moving": 12,
      "staticPass": 1,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 4,
      "wChecks": 1468
    },
    {
      "i": 1216,
      "dim": 3,
      "side": 1,
      "N": 29,
      "moving": 11,
      "staticPass": 1,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 3,
      "wChecks": 1514
    },
    {
      "i": 1216,
      "dim": 3,
      "side": -1,
      "N": 29,
      "moving": 11,
      "staticPass": 3,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 9,
      "wChecks": 1468
    },
    {
      "i": 1363,
      "dim": 3,
      "side": 1,
      "N": 31,
      "moving": 13,
      "staticPass": 1,
      "extremePass": 0,
      "jointPass": 0,
      "extremePairs": 4,
      "wChecks": 0
    },
    {
      "i": 1363,
      "dim": 3,
      "side": -1,
      "N": 29,
      "moving": 13,
      "staticPass": 2,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 12,
      "wChecks": 1469
    },
    {
      "i": 1476,
      "dim": 3,
      "side": 1,
      "N": 29,
      "moving": 8,
      "staticPass": 7,
      "extremePass": 6,
      "jointPass": 6,
      "extremePairs": 50,
      "wChecks": 1032
    },
    {
      "i": 1476,
      "dim": 3,
      "side": -1,
      "N": 27,
      "moving": 8,
      "staticPass": 125,
      "extremePass": 111,
      "jointPass": 111,
      "extremePairs": 1325,
      "wChecks": 108947
    },
    {
      "i": 1486,
      "dim": 3,
      "side": 1,
      "N": 29,
      "moving": 11,
      "staticPass": 1,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 4,
      "wChecks": 1032
    },
    {
      "i": 1486,
      "dim": 3,
      "side": -1,
      "N": 30,
      "moving": 11,
      "staticPass": 6,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 32,
      "wChecks": 1468
    },
    {
      "i": 1488,
      "dim": 3,
      "side": 1,
      "N": 29,
      "moving": 10,
      "staticPass": 1,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 4,
      "wChecks": 1032
    },
    {
      "i": 1488,
      "dim": 3,
      "side": -1,
      "N": 29,
      "moving": 10,
      "staticPass": 11,
      "extremePass": 8,
      "jointPass": 8,
      "extremePairs": 64,
      "wChecks": 11248
    },
    {
      "i": 1661,
      "dim": 3,
      "side": 1,
      "N": 28,
      "moving": 7,
      "staticPass": 3,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 20,
      "wChecks": 300
    },
    {
      "i": 1661,
      "dim": 3,
      "side": -1,
      "N": 27,
      "moving": 7,
      "staticPass": 17,
      "extremePass": 11,
      "jointPass": 11,
      "extremePairs": 155,
      "wChecks": 27375
    },
    {
      "i": 1915,
      "dim": 3,
      "side": 1,
      "N": 28,
      "moving": 10,
      "staticPass": 3,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 12,
      "wChecks": 516
    },
    {
      "i": 1915,
      "dim": 3,
      "side": -1,
      "N": 29,
      "moving": 10,
      "staticPass": 1,
      "extremePass": 0,
      "jointPass": 0,
      "extremePairs": 3,
      "wChecks": 0
    },
    {
      "i": 1916,
      "dim": 3,
      "side": 1,
      "N": 27,
      "moving": 9,
      "staticPass": 8,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 55,
      "wChecks": 516
    },
    {
      "i": 1916,
      "dim": 3,
      "side": -1,
      "N": 29,
      "moving": 9,
      "staticPass": 1,
      "extremePass": 0,
      "jointPass": 0,
      "extremePairs": 5,
      "wChecks": 0
    },
    {
      "i": 1944,
      "dim": 3,
      "side": 1,
      "N": 28,
      "moving": 7,
      "staticPass": 3,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 12,
      "wChecks": 6
    },
    {
      "i": 1944,
      "dim": 3,
      "side": -1,
      "N": 27,
      "moving": 7,
      "staticPass": 28,
      "extremePass": 20,
      "jointPass": 20,
      "extremePairs": 153,
      "wChecks": 16874
    },
    {
      "i": 1946,
      "dim": 3,
      "side": 1,
      "N": 28,
      "moving": 9,
      "staticPass": 3,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 20,
      "wChecks": 324
    },
    {
      "i": 1946,
      "dim": 3,
      "side": -1,
      "N": 28,
      "moving": 9,
      "staticPass": 3,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 20,
      "wChecks": 109
    },
    {
      "i": 1947,
      "dim": 3,
      "side": 1,
      "N": 27,
      "moving": 8,
      "staticPass": 8,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 44,
      "wChecks": 300
    },
    {
      "i": 1947,
      "dim": 3,
      "side": -1,
      "N": 28,
      "moving": 8,
      "staticPass": 3,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 16,
      "wChecks": 101
    },
    {
      "i": 2186,
      "dim": 3,
      "side": 1,
      "N": 29,
      "moving": 9,
      "staticPass": 7,
      "extremePass": 6,
      "jointPass": 6,
      "extremePairs": 30,
      "wChecks": 1032
    },
    {
      "i": 2186,
      "dim": 3,
      "side": -1,
      "N": 28,
      "moving": 9,
      "staticPass": 54,
      "extremePass": 38,
      "jointPass": 38,
      "extremePairs": 327,
      "wChecks": 39312
    },
    {
      "i": 2188,
      "dim": 3,
      "side": 1,
      "N": 27,
      "moving": 8,
      "staticPass": 11,
      "extremePass": 7,
      "jointPass": 7,
      "extremePairs": 80,
      "wChecks": 524
    },
    {
      "i": 2188,
      "dim": 3,
      "side": -1,
      "N": 29,
      "moving": 8,
      "staticPass": 22,
      "extremePass": 2,
      "jointPass": 2,
      "extremePairs": 220,
      "wChecks": 2457
    },
    {
      "i": 2473,
      "dim": 3,
      "side": 1,
      "N": 28,
      "moving": 11,
      "staticPass": 11,
      "extremePass": 8,
      "jointPass": 8,
      "extremePairs": 64,
      "wChecks": 8256
    },
    {
      "i": 2473,
      "dim": 3,
      "side": -1,
      "N": 31,
      "moving": 11,
      "staticPass": 1,
      "extremePass": 0,
      "jointPass": 0,
      "extremePairs": 4,
      "wChecks": 0
    },
    {
      "i": 2511,
      "dim": 3,
      "side": 1,
      "N": 28,
      "moving": 10,
      "staticPass": 11,
      "extremePass": 8,
      "jointPass": 8,
      "extremePairs": 64,
      "wChecks": 8252
    },
    {
      "i": 2511,
      "dim": 3,
      "side": -1,
      "N": 30,
      "moving": 10,
      "staticPass": 8,
      "extremePass": 7,
      "jointPass": 7,
      "extremePairs": 44,
      "wChecks": 10028
    },
    {
      "i": 2512,
      "dim": 3,
      "side": 1,
      "N": 28,
      "moving": 11,
      "staticPass": 11,
      "extremePass": 8,
      "jointPass": 8,
      "extremePairs": 64,
      "wChecks": 8256
    },
    {
      "i": 2512,
      "dim": 3,
      "side": -1,
      "N": 31,
      "moving": 11,
      "staticPass": 2,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 8,
      "wChecks": 1468
    },
    {
      "i": 2966,
      "dim": 3,
      "side": 1,
      "N": 28,
      "moving": 9,
      "staticPass": 4,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 15,
      "wChecks": 522
    },
    {
      "i": 2966,
      "dim": 3,
      "side": -1,
      "N": 29,
      "moving": 9,
      "staticPass": 1,
      "extremePass": 0,
      "jointPass": 0,
      "extremePairs": 3,
      "wChecks": 0
    },
    {
      "i": 3248,
      "dim": 3,
      "side": 1,
      "N": 26,
      "moving": 8,
      "staticPass": 17,
      "extremePass": 8,
      "jointPass": 8,
      "extremePairs": 125,
      "wChecks": 3349
    },
    {
      "i": 3248,
      "dim": 3,
      "side": -1,
      "N": 29,
      "moving": 8,
      "staticPass": 1,
      "extremePass": 0,
      "jointPass": 0,
      "extremePairs": 5,
      "wChecks": 0
    },
    {
      "i": 3395,
      "dim": 3,
      "side": 1,
      "N": 27,
      "moving": 7,
      "staticPass": 11,
      "extremePass": 7,
      "jointPass": 7,
      "extremePairs": 48,
      "wChecks": 524
    },
    {
      "i": 3395,
      "dim": 3,
      "side": -1,
      "N": 28,
      "moving": 7,
      "staticPass": 46,
      "extremePass": 41,
      "jointPass": 41,
      "extremePairs": 264,
      "wChecks": 52312
    },
    {
      "i": 3409,
      "dim": 3,
      "side": 1,
      "N": 28,
      "moving": 7,
      "staticPass": 4,
      "extremePass": 4,
      "jointPass": 4,
      "extremePairs": 24,
      "wChecks": 8
    },
    {
      "i": 3409,
      "dim": 3,
      "side": -1,
      "N": 27,
      "moving": 7,
      "staticPass": 97,
      "extremePass": 73,
      "jointPass": 73,
      "extremePairs": 780,
      "wChecks": 89249
    },
    {
      "i": 3454,
      "dim": 3,
      "side": 1,
      "N": 28,
      "moving": 6,
      "staticPass": 3,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 16,
      "wChecks": 6
    },
    {
      "i": 3454,
      "dim": 3,
      "side": -1,
      "N": 26,
      "moving": 6,
      "staticPass": 147,
      "extremePass": 143,
      "jointPass": 143,
      "extremePairs": 1212,
      "wChecks": 182461
    },
    {
      "i": 3488,
      "dim": 3,
      "side": 1,
      "N": 30,
      "moving": 13,
      "staticPass": 2,
      "extremePass": 0,
      "jointPass": 0,
      "extremePairs": 6,
      "wChecks": 0
    },
    {
      "i": 3488,
      "dim": 3,
      "side": -1,
      "N": 30,
      "moving": 13,
      "staticPass": 1,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 3,
      "wChecks": 191
    },
    {
      "i": 3591,
      "dim": 3,
      "side": 1,
      "N": 28,
      "moving": 8,
      "staticPass": 3,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 12,
      "wChecks": 300
    },
    {
      "i": 3591,
      "dim": 3,
      "side": -1,
      "N": 27,
      "moving": 8,
      "staticPass": 33,
      "extremePass": 16,
      "jointPass": 16,
      "extremePairs": 186,
      "wChecks": 40835
    },
    {
      "i": 3607,
      "dim": 3,
      "side": 1,
      "N": 27,
      "moving": 9,
      "staticPass": 8,
      "extremePass": 4,
      "jointPass": 4,
      "extremePairs": 48,
      "wChecks": 472
    },
    {
      "i": 3607,
      "dim": 3,
      "side": -1,
      "N": 29,
      "moving": 9,
      "staticPass": 2,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 8,
      "wChecks": 3512
    },
    {
      "i": 3608,
      "dim": 3,
      "side": 1,
      "N": 28,
      "moving": 8,
      "staticPass": 4,
      "extremePass": 4,
      "jointPass": 4,
      "extremePairs": 24,
      "wChecks": 8
    },
    {
      "i": 3608,
      "dim": 3,
      "side": -1,
      "N": 28,
      "moving": 8,
      "staticPass": 74,
      "extremePass": 18,
      "jointPass": 18,
      "extremePairs": 604,
      "wChecks": 20045
    },
    {
      "i": 3636,
      "dim": 3,
      "side": 1,
      "N": 27,
      "moving": 8,
      "staticPass": 7,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 40,
      "wChecks": 300
    },
    {
      "i": 3636,
      "dim": 3,
      "side": -1,
      "N": 28,
      "moving": 8,
      "staticPass": 10,
      "extremePass": 2,
      "jointPass": 2,
      "extremePairs": 68,
      "wChecks": 2915
    },
    {
      "i": 3637,
      "dim": 3,
      "side": 1,
      "N": 28,
      "moving": 7,
      "staticPass": 3,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 20,
      "wChecks": 6
    },
    {
      "i": 3637,
      "dim": 3,
      "side": -1,
      "N": 27,
      "moving": 7,
      "staticPass": 127,
      "extremePass": 45,
      "jointPass": 45,
      "extremePairs": 1325,
      "wChecks": 50148
    },
    {
      "i": 3652,
      "dim": 3,
      "side": 1,
      "N": 28,
      "moving": 9,
      "staticPass": 3,
      "extremePass": 3,
      "jointPass": 3,
      "extremePairs": 16,
      "wChecks": 516
    },
    {
      "i": 3652,
      "dim": 3,
      "side": -1,
      "N": 28,
      "moving": 9,
      "staticPass": 10,
      "extremePass": 2,
      "jointPass": 2,
      "extremePairs": 68,
      "wChecks": 2987
    },
    {
      "i": 3911,
      "dim": 3,
      "side": 1,
      "N": 30,
      "moving": 13,
      "staticPass": 3,
      "extremePass": 0,
      "jointPass": 0,
      "extremePairs": 12,
      "wChecks": 0
    },
    {
      "i": 3911,
      "dim": 3,
      "side": -1,
      "N": 30,
      "moving": 13,
      "staticPass": 1,
      "extremePass": 1,
      "jointPass": 1,
      "extremePairs": 3,
      "wChecks": 191
    }
  ]
}
```
