# X6 R213 — projected joint-observation union capacity on rank three

2026-11-26. AUTHOR PROOF / EXACT NECESSARY-RELAXATION REPLAY / NOT_REVIEWED. Informed static auxiliary BRC weight coefficient chart, not native dynamics. P000 V5 remains locked. Current native query r2-20261126-0807-x6-read SUCCEEDED at Source 2eb9a8d7f28abf28c6b5052dfbe9cd6d9d937b90; publication directory absent only, no owner projection, no CLAIM, own native researcher binding unconfirmed.

Frozen sources: R209 32592df7bff1a87649e3541f12c22b99b6a0cd71:research_notes/portable_direct/2026-11-26_r2_x6_r209_bilinear_joint_capacity_envelope.md blob 6f634f0a0679e23d95b0e96a99dbdc33c541a746; R181 census eb87794b9f9b2a6d600a2d12c37d49855b436bca blob d221356b478797a2869a19f0c0261ea412ec7081; R210 d13689252667fcacfc95b30dec0524adba24980d replay solver (unchanged exact function text extracted); R211 97a072b666d6c1e74f108a1327a529b4b133c7ac and R212 c710e8ec583d510e813ca0714fd1886b2d69d1b7. Port 10, 1935 directions, C/A=22/17, six joint BRC relations, 47 labeled supports, 49 components, 51 original endpoint rays. Selected sides from R212 low root passing counts: [[768,1],[769,1],[852,-1],[1947,-1],[2512,-1]].

## Soundness
For a fixed root class C and side, every actual first-child clipped labeled endpoint is either a fixed original endpoint or a moving point with sign equal to s_k sign(w dot n_k), w=r cross q, as R209 proves. Enumerate all static q sign classes, up to simultaneous reversal of all q signs and w signs. Project the entire oriented R209 support-normal arrangement plus zero onto the moving labels of this side, deduplicate identical projections, and retain every pattern compatible with R209's extreme-pair masks for C and q. This preserves every actual clipped endpoint sign tuple for every r in C, including equalities and w=0. Store all four sign masks on the labeled ordered endpoint pairs, canonicalizing only simultaneous sign reversal, which exchanges positive/negative successor states. Fixed endpoint masks keep their actual q signs. No root-budget filter is applied during bank construction, since observations that cannot be used at the root may still be useful at deeper states.

The union bank is a superset of the true fixed-r endpoint sign bank for every r in C. R204 observation-set monotonicity therefore allows us to solve the fixed-endpoint capacity necessary relaxation once with this enlarged bank, using the original solver and R206 antichain solver. Failure excludes the entire side by R182 single-side sufficiency. This argument applies regardless of root rank. Success establishes only feasibility of the enlarged relaxation, not a realizable tree. We do not assert that every bank entry lifts under R212. Projection is exact for the declared moving-normal sign list only, and retains all fixed endpoint labels in the masks.

## Actual results
{
  "P": 51,
  "bank": 4249,
  "wBank": 3445,
  "orientedW": 6891,
  "rows": [
    {
      "i": 768,
      "side": 1,
      "supports": 30,
      "moving": 9,
      "projectedW": 207,
      "attempts": 879543,
      "accepted": 9227,
      "extremePairs": 28572,
      "unionPatterns": 2963,
      "union": {
        "feasible": false,
        "states": 2,
        "rootLegal": 1
      },
      "antichain": {
        "feasible": false,
        "states": 2,
        "eligible": 1,
        "minimal": 1,
        "rootEligible": 1,
        "rootMinimal": 1
      },
      "excluded": true
    },
    {
      "i": 769,
      "side": 1,
      "supports": 29,
      "moving": 9,
      "projectedW": 231,
      "attempts": 981519,
      "accepted": 9459,
      "extremePairs": 38096,
      "unionPatterns": 3097,
      "union": {
        "feasible": false,
        "states": 6,
        "rootLegal": 1
      },
      "antichain": {
        "feasible": false,
        "states": 6,
        "eligible": 5,
        "minimal": 5,
        "rootEligible": 1,
        "rootMinimal": 1
      },
      "excluded": true
    },
    {
      "i": 852,
      "side": -1,
      "supports": 30,
      "moving": 10,
      "projectedW": 319,
      "attempts": 1355431,
      "accepted": 12355,
      "extremePairs": 38096,
      "unionPatterns": 4745,
      "union": {
        "feasible": false,
        "states": 2,
        "rootLegal": 1
      },
      "antichain": {
        "feasible": false,
        "states": 2,
        "eligible": 1,
        "minimal": 1,
        "rootEligible": 1,
        "rootMinimal": 1
      },
      "excluded": true
    },
    {
      "i": 1947,
      "side": -1,
      "supports": 28,
      "moving": 8,
      "projectedW": 195,
      "attempts": 828555,
      "accepted": 8467,
      "extremePairs": 38096,
      "unionPatterns": 3513,
      "union": {
        "feasible": false,
        "states": 2,
        "rootLegal": 1
      },
      "antichain": {
        "feasible": false,
        "states": 2,
        "eligible": 1,
        "minimal": 1,
        "rootEligible": 1,
        "rootMinimal": 1
      },
      "excluded": true
    },
    {
      "i": 2512,
      "side": -1,
      "supports": 31,
      "moving": 11,
      "projectedW": 411,
      "attempts": 1746339,
      "accepted": 13567,
      "extremePairs": 38096,
      "unionPatterns": 5739,
      "union": {
        "feasible": false,
        "states": 2,
        "rootLegal": 1
      },
      "antichain": {
        "feasible": false,
        "states": 2,
        "eligible": 1,
        "minimal": 1,
        "rootEligible": 1,
        "rootMinimal": 1
      },
      "excluded": true
    }
  ],
  "excluded": [
    768,
    769,
    852,
    1947,
    2512
  ]
}
Executed exact BigInt sign geometry and integer mask recurrence; checked original and antichain solver agreement. No dynamic parameter divisions. Conditional cumulative remaining after R211/R212/R213: 41 (17 rank two and 24 rank three), bound 6<=D_linear<=7 unchanged. Independent review pending. No formal Result or shared-state mutation.

## Standalone reproduction
```javascript
function compute(data,rows,selected){
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

const pc=x=>{x=x-((x>>>1)&0x55555555);x=(x&0x33333333)+((x>>>2)&0x33333333);return (((x+(x>>>4))&0x0F0F0F0F)*0x01010101)>>>24};
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

 const res=[];
 for(const row of rows){
  let a=BigInt(row.a),b=BigInt(row.b),rr=row.r.map(BigInt),rs=P.map((p,i)=>{let x=sg(dot(rr,p)),y=a&(1n<<BigInt(i))?1:b&(1n<<BigInt(i))?-1:0;if(x!==y)throw Error("root mask mismatch");return x});
  const [key,flip]=canon(rs),rentry=bank.get(key);if(!rentry)throw Error("root missing");
  let R=rentry.rays.map(r=>flip===1?r:neg(r));
  for(let side of selected.filter(x=>x[0]===row.i).map(x=>x[1])){
   const clipped=[];
   function descriptor(i,j,k){if(i===j)return {fixed:i};const v=cross(P[i],P[j]),n=N[k],s=sg(dot(v,n))*rs[i];if(!s||rs[i]*rs[j]!==-1||cross(v,n).some(Boolean))throw Error("bad moving orientation");return {i,j,k,s}}
   for(let k=0;k<comps.length;k++){let keep=[];for(let [i,j] of comps[k]){let x=rs[i]*side,y=rs[j]*side;if(x<=0&&y<=0)continue;keep.push([x<0?descriptor(i,j,k):{fixed:i},y<0?descriptor(i,j,k):{fixed:j}])}if(keep.length)clipped.push([keep[0][0],keep.at(-1)[1]])}
   if(clipped.length<=5||clipped.length>31)throw Error("bad support count");

   const moving=[...new Set(clipped.flat().filter(x=>x.fixed===undefined).map(x=>x.k))],idxM=new Map(moving.map((k,i)=>[k,i]));
   const proj=[...new Map(W.map(w=>{let x=moving.map(k=>w[k]);return [x.join(),x]})).values()];
   const bankQ=new Map();let accepted=0,attempts=0,extremePairs=0;
   for(const q of bank.values()){
    const masks=Array(N.length).fill(0);
    for(const r of R)for(const z of q.rays){let w=cross(r,z);extremePairs++;for(let k of moving)masks[k]|=bit(sg(dot(w,N[k])))}
    for(let k of moving){let m=masks[k];masks[k]=(m&1)&&(m&4)?7:(m&1)?1:(m&4)?4:2}
    let fixed=[0,0,0,0],dyn=[];
    for(let i=0;i<clipped.length;i++)for(let j=0;j<2;j++){
      let x=clipped[i][j],z=1<<i;
      if(x.fixed===undefined)dyn.push([idxM.get(x.k),x.s,j,z]);
      else{let v=q.s[x.fixed];if(v)fixed[j+(v<0?2:0)]|=z}
    }
    for(const w of proj){
      attempts++;if(!moving.every((k,i)=>masks[k]&bit(w[i])))continue;accepted++;
      let m=fixed.slice();for(const [k,s,j,z] of dyn){let v=w[k]*s;if(v)m[j+(v<0?2:0)]|=z}
      m=canonical(m);bankQ.set(m.join(),m);
    }
   }
   let qs=[...bankQ.values()],union=solvePatterns(clipped.length,qs),antichain=solveAntichain(clipped.length,qs);
   if(union.feasible!==antichain.feasible)throw Error("solver mismatch");
   res.push({i:row.i,side,supports:clipped.length,moving:moving.length,projectedW:proj.length,attempts,accepted,extremePairs,unionPatterns:qs.length,union,antichain,excluded:!union.feasible});
  }
 }
 return {P:P.length,bank:bank.size,wBank:wBank.size,orientedW:W.length,rows:res,excluded:res.filter(x=>x.excluded).map(x=>x.i)};
}
const data=[{"normal":["187","12","-1"],"segments":9,"endpoints":[["0","1","12"],["1","17","391"]]},{"normal":["204","11","-1"],"segments":9,"endpoints":[["0","1","11"],["1","17","391"]]},{"normal":["5","-2","0"],"segments":51,"endpoints":[["2","5","73"],["2","5","5"]]},{"normal":["9","-1","0"],"segments":4,"endpoints":[["1","9","74"],["1","9","69"]]},{"normal":["85","7","-2"],"segments":10,"endpoints":[["1","9","74"],["3","17","187"]]},{"normal":["51","2","-1"],"segments":9,"endpoints":[["1","9","69"],["1","0","51"]]},{"normal":["0","1","-1"],"segments":2,"endpoints":[["2","5","5"],["1","0","0"]]},{"normal":["34","1","-1"],"segments":7,"endpoints":[["2","5","73"],["1","0","34"]]},{"normal":["187","20","-9"],"segments":5,"endpoints":[["6","15","158"],["1","1","23"]]},{"normal":["68","1","-3"],"segments":8,"endpoints":[["2","5","47"],["3","0","68"]]},{"normal":["176","22","-9"],"segments":4,"endpoints":[["6","15","154"],["19","28","440"]]},{"normal":["22","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","22"]]},{"normal":["61","0","-1"],"segments":78,"endpoints":[["0","1","0"],["1","17","61"]]},{"normal":["74","0","-1"],"segments":14,"endpoints":[["1","9","74"],["1","4","74"]]},{"normal":["126","0","-1"],"segments":103,"endpoints":[["0","1","0"],["1","30","126"]]},{"normal":["4","-1","0"],"segments":35,"endpoints":[["1","4","152"],["1","4","74"]]},{"normal":["17","-1","0"],"segments":44,"endpoints":[["0","0","1"],["1","17","22"]]},{"normal":["156","-1","-1"],"segments":46,"endpoints":[["1","4","152"],["1","30","126"]]},{"normal":["69","0","-1"],"segments":16,"endpoints":[["1","17","69"],["1","9","69"]]},{"normal":["9","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","9"]]},{"normal":["235","0","-3"],"segments":84,"endpoints":[["0","1","0"],["3","77","235"]]},{"normal":["87","0","-1"],"segments":107,"endpoints":[["0","1","0"],["1","17","87"]]},{"normal":["104","-1","-1"],"segments":60,"endpoints":[["1","4","100"],["3","77","235"]]},{"normal":["38","0","-3"],"segments":57,"endpoints":[["0","1","0"],["3","40","38"]]},{"normal":["5","0","-2"],"segments":72,"endpoints":[["0","1","0"],["2","5","5"]]},{"normal":["39","-1","-1"],"segments":50,"endpoints":[["3","1","116"],["1","17","22"]]},{"normal":["40","0","-3"],"segments":63,"endpoints":[["0","1","0"],["3","38","40"]]},{"normal":["26","-1","-1"],"segments":39,"endpoints":[["2","5","47"],["3","53","25"]]},{"normal":["25","0","-3"],"segments":52,"endpoints":[["0","1","0"],["3","53","25"]]},{"normal":["83","0","-2"],"segments":69,"endpoints":[["0","1","0"],["2","34","83"]]},{"normal":["102","-7","-1"],"segments":14,"endpoints":[["1","4","74"],["3","17","187"]]},{"normal":["204","-11","1"],"segments":51,"endpoints":[["0","1","11"],["1","30","126"]]},{"normal":["395","0","-2"],"segments":119,"endpoints":[["0","1","0"],["2","73","395"]]},{"normal":["289","18","-1"],"segments":10,"endpoints":[["0","1","18"],["1","17","595"]]},{"normal":["66","2","-1"],"segments":11,"endpoints":[["1","4","74"],["1","0","66"]]},{"normal":["132","5","-1"],"segments":16,"endpoints":[["1","17","217"],["1","0","132"]]},{"normal":["44","1","-1"],"segments":9,"endpoints":[["1","17","61"],["1","11","55"]]},{"normal":["88","3","-1"],"segments":7,"endpoints":[["1","4","100"],["1","0","88"]]},{"normal":["88","7","-3"],"segments":5,"endpoints":[["1","17","69"],["1","11","55"]]},{"normal":["132","-7","-1"],"segments":14,"endpoints":[["1","9","69"],["1","11","55"]]},{"normal":["153","8","-1"],"segments":7,"endpoints":[["1","9","225"],["1","0","153"]]},{"normal":["153","5","-4"],"segments":1,"endpoints":[["3","1","116"],["4","0","153"]]},{"normal":["117","-2","-2"],"segments":42,"endpoints":[["2","5","112"],["2","34","83"]]},{"normal":["198","8","-1"],"segments":5,"endpoints":[["1","4","230"],["1","0","198"]]},{"normal":["198","5","-4"],"segments":11,"endpoints":[["2","8","109"],["2","0","99"]]},{"normal":["306","17","-1"],"segments":8,"endpoints":[["1","17","595"],["1","0","306"]]},{"normal":["234","-1","-1"],"segments":43,"endpoints":[["1","4","230"],["2","73","395"]]}];

const rows=[{"i":768,"dim":3,"vertices":3,"r":["3183","584","-124"],"a":"1132515555864","b":"2250667298129383","global":111,"local":36,"events":["103,238,3740","2,45,267","18,397,2411","23,211,1587","3,41,271","3,7,110","75,2783,15313","8,45,423","99,3568,19598","76,187,2771","20,47,727","35,68,1258","21,46,760","241,561,8755","1,2,36","1049,2057,37723","115,268,4178","49,1098,6546","7,157,935","3,67,401","78,727,5382","156,1429,10764","124,1161,8556","232,2133,16008","110,271,4019","8,19,293","5,11,184","508,1187,18625","105,3859,21029","11,402,2178","176,1029,9267","6,34,317","332,1913,17509","28,165,1473","87,3149,17209","1,36,198"]},{"i":769,"dim":3,"vertices":4,"r":["7277","1515","-315"],"a":"1132515555856","b":"2250667298129391","global":120,"local":42,"events":["6,15,211","2,45,267","18,397,2411","23,211,1587","3,41,271","3,40,272","75,2783,15313","99,3568,19598","61,2099,12175","4,10,143","1,22,134","49,1098,6546","87,1901,11671","7,157,935","3,67,401","78,727,5382","79,756,5451","156,1429,10764","124,1161,8556","232,2133,16008","7,93,635","4,11,145","9,23,328","33,89,1198","3,8,109","1,38,214","105,3859,21029","21,799,4505","11,421,2387","11,402,2178","121,1114,8174","169,1566,11346","176,1029,9267","216,1319,11317","332,1913,17509","260,1581,13629","28,165,1473","94,558,4941","1,35,199","87,3149,17209","19,661,3785","1,36,198"]},{"i":852,"dim":3,"vertices":4,"r":["207","28","-8"],"a":"1115201468944","b":"2250684612216303","global":249,"local":92,"events":["2,5,64","6,15,211","81,2392,10244","1,28,128","15,199,1035","3,40,207","3,38,207","5,87,435","169,3071,14703","167,3073,14529","3,53,261","3,52,260","10,181,859","3,53,259","173,585,6162","13,45,462","10,29,361","93,2828,12136","6,305,1185","42,1975,8295","138,6715,27255","92,4575,18170","206,10327,40685","82,4033,16195","42,2077,8295","62,3147,12245","1204,59715,237790","1954,97373,385915","114,5279,22515","142,6977,28045","394,18931,77815","2,99,395","7,71,427","15,151,923","4,29,205","2,5,68","4,10,143","34,85,1085","16,40,545","5,143,637","32,945,4047","49,1390,6254","67,1917,8535","1,29,127","35,1037,4423","12,355,1517","14,171,966","395,5037,27255","19,237,1311","1,18,87","13,225,1131","19,327,1649","39,134,1387","1,3,36","233,763,8324","4,13,143","178,543,6399","4,11,145","38,113,1369","369,1307,13084","9,23,328","6,17,217","49,155,1756","9,31,320","63,190,2267","93,265,3362","33,89,1198","3,8,109","109,3361,14735","76,2295,9741","107,3290,14362","149,4563,19797","27,823,3545","67,2023,8585","11,336,1452","28,845,3583","202,9843,39895","82,3822,16195","18,187,1067","21,209,1309","7,72,420","1,10,62","26,185,1336","2,15,102","24,167,1237","8,59,409","38,293,1930","302,2326,15341","38,303,1920","2,16,101","14,108,711","38,295,1928"]},{"i":1947,"dim":3,"vertices":4,"r":["2435","50","-48"],"a":"863133305404952","b":"1388666508280295","global":117,"local":74,"events":["11,775,1386","72,6125,9072","1,82,126","5,351,630","17,289,1157","11,187,731","147,4007,11515","36,1105,2820","81,2261,6345","30,777,2350","201,6017,15745","21,629,1645","21,551,1645","201,5291,15745","12,407,1044","83,2958,7221","1,37,87","67,2439,5829","7,255,609","1,39,87","2,327,395","2,295,395","44,6715,8690","14,2326,2765","74,11242,14615","6,856,1185","36,5245,7110","226,35666,44635","190,30374,37525","1394,207778,275315","2,307,395","137,2047,8795","61,1031,4195","125,2059,8471","7,71,427","4,15,219","28,109,1529","4,341,504","6,425,756","82,5775,10332","14,979,1764","26,2095,3276","134,10065,16884","1,17,66","36,937,2820","72,1913,5640","27,697,2115","3,90,235","54,1477,4230","39,1069,3055","108,3227,8460","2,73,174","1,34,87","41,1386,3567","7,249,609","11,421,957","4,159,348","7,236,609","13,482,1131","67,2322,5829","16,2367,3160","36,4981,7110","164,22561,32390","28,3817,5530","52,8337,10270","268,40007,52930","29,439,1875","13,194,834","105,1584,6776","7,110,462","47,745,3117","15,151,923","664,2591,36253","54,203,2956"]},{"i":2512,"dim":3,"vertices":4,"r":["27407","8191","-1698"],"a":"1115335666192","b":"2250684478019055","global":347,"local":160,"events":["2615,3749,62665","50,77,1210","40,49,940","607,778,14341","29,47,707","1770,3381,44290","380,407,8800","6098,6611,141394","8321,9887,194863","727,862,17021","8900,10547,208360","2005,2383,46955","19,28,457","537,603,12373","681,963,15757","2391,2433,55007","549,807,12713","2427,3357,56131","99,2437,13007","61,1436,8080","2,51,261","1,26,130","451,12191,58165","3,80,388","35,943,4517","29,788,3736","2,47,265","3,77,391","19,479,2485","1,11,69","25,261,1725","61,994,5350","3,50,262","5,84,436","15,241,1319","4,15,141","1,4,35","25,867,4437","1,34,170","593,19129,89447","24,785,3739","589,19061,89515","254,8153,37867","17,601,3143","23,820,4328","174,6715,34365","2,79,395","56,2431,11060","254,10727,50165","736,31739,145360","2426,106437,479135","16,623,3160","2,88,395","10,443,1975","18,683,3555","68,2755,13430","2,82,395","706,26471,139435","16,649,3160","14,550,2765","32,1207,6320","346,12746,68335","7,71,427","5,48,324","15,151,923","4,29,205","2,5,60","2,5,55","10,25,287","176,257,4228","2725,2941,63155","79,106,1877","158,185,3694","284,527,7072","2669,4019,64387","557,935,13651","142,169,3326","293,374,6919","244,343,5832","142,187,3366","4561,7531,111503","185,293,4495","107,134,2521","908,935,20944","821,1496,20383","70,97,1619","1981,2125,45611","32,41,739","64,73,1475","527,752,12196","53,62,1222","109,136,2516","87,120,2012","53,68,1224","77,95,1777","331,340,7616","9,227,1177","66,1543,8753","179,4239,23685","49,1171,6473","22,549,2883","3,79,389","53,1413,6855","3,73,395","1,24,132","14,171,966","23,258,1587","19,237,1311","32,477,2851","7,102,626","67,981,5987","9,133,803","53,789,4723","3,47,265","111,1853,9691","9,146,790","1,16,88","36,545,3199","83,351,2886","57,236,1987","83,306,2931","369,1307,13084","59,245,2056","15,493,2363","59,2142,11526","90,3137,16147","253,8721,44319","71,2429,12235","32,1071,5253","5,161,751","91,2907,13413","9,323,1717","11,356,1672","49,1769,9463","11,357,1683","37,1292,6664","14,620,2765","80,2943,15800","106,4165,20935","22,882,4345","6,244,1185","70,2943,13825","34,1274,6715","190,7052,37525","10,392,1975","43,412,2792","61,594,3894","21,209,1309","7,72,420","1,10,62","26,185,1336","2,15,102","24,167,1237","8,59,409","38,293,1930","302,2326,15341","38,303,1920","2,16,101","14,108,711","38,295,1928"]}];
const selected=[[768,1],[769,1],[852,-1],[1947,-1],[2512,-1]];
console.log(JSON.stringify(compute(data,rows,selected),null,2));
```

## Next
Apply the same projected bank to further rank-three sides, prioritizing small root legal counts. If union relaxation passes, restrict root candidates to the exact R212 local lift and preserve the deeper union as a safe overapproximation; only then refine by a common root parameter. Rank-two next 2510. Do not redo completed R211–R213.
