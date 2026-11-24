# X6 R178 — Recursive endpoint-closure capacity for arbitrary linear observations

2026-11-25 (Asia/Shanghai). AUTHOR PROOF / EXACT BIGINT FINITE RELAXATION / NOT_REVIEWED. Independent informed static BRC research; no shared Task write or CLAIM. Historical lane EM-DIRECT-AE5AD5 / RA-B60559848FD879270DCA6317, current identity binding unconfirmed.

## Scope and sources
Port 10, six pair capacities, w=(17t,B,22t,D), t,B,D>0, 1935 unoriented directions, simultaneous legal optimizer term and complete strict 3/2 near set. Frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f; R175@eadbd5e26a1a44f2bef376229785e7d2886f5938 establishes seven for the 884-predicate model. R176@c665f671a31d2bfeffb151e06bb308628110029e and R177@2cb3a23a9bd4b92bcbc1a9946b53a4de8f1ba9ca:research_notes/portable_direct/2026-11-24_r2_x6_r177_two_level_support_capacity.md supply the 47 distinct mandatory supports and their 51 extreme closure rays. R177 data are consumed directly, not rederived; no new all-direction score replay. P000 V5 and ACTIVE worldview retained; this is an auxiliary static parameter chart, not native time dynamics.

## Proposition
For an open decision cell C, maintain for each mandatory support i zero, one or two original extreme endpoint rays whose normalized representatives belong to the closure of its active portions in C. Begin with both extremes. A nonempty retained set certifies at least one mandatory internal node in C, by the R176 local boundary argument. For a query r, positive-child update: if any retained endpoint has r·p>0, retain every currently retained endpoint with r·p>=0; otherwise retain none. Negative-child update uses -r.

Proof: a strictly signed retained endpoint has a sequence of actual active points in C with that sign. If a retained zero-sign endpoint has a strictly positive retained companion, then along the entire original support interval between its extremes the sign is positive away from the zero endpoint. Any actual active sequence approaching the zero endpoint in C lies within those original extremes, so the zero endpoint remains a closure point of the positive child. This reasoning remains valid with disconnected active pieces and after arbitrarily many ancestors; it never invents an active interval between endpoints. A single zero endpoint, two zero endpoints, or a discarded crossing point may carry further obligations not represented by this relaxed state. We discard them only for this one-sided lower-bound calculation; the underlying source remains preserved.

Let n(S) count distinct retained supports. A depth d subtree requires n(S)<=2^d-1. Given finite sign classes Q of all nonzero real linear forms on the original rays, define F(S,d,k) for 0<=k<=d: reject if n(S)>2^d-1; accept at k=0; otherwise accept iff some q in Q has both children F(S_+,d-1,k-1) and F(S_-,d-1,k-1). The implication from a correct actual tree to F follows by induction on k, using the closure invariant and mandatory-node bound; signs are ternary even though actual comparisons are binary, since both open children are used for necessary conditions. An actual tree that terminates early has no obligations and may be padded. If n(S)<=d then F is true: querying the normal of each retained support in turn removes that support from both children, and no support is added. Every such normal's sign pattern occurs in Q. No shortcut n>2k is sound in general for child capacity k: a query may remove a support. An initial exploratory implementation made that mistake, reported 332 instead of 537 second-level survivors, and was corrected before this certificate.

Q uses the R177 exact cross-product vertex/tangent lexicographic enumeration: in the dual projective arrangement of the 51 rays, every vertex is a cross product, every adjacent open arc has a tangent direction from a through-vertex circle, and every adjacent chamber is obtained by a further infinitesimal displacement normal to that circle. The signs are computed lexicographically, not by floating point. Antipodal pairing is safe since both children must pass. Hence Q covers every possible actual root and descendant sign pattern. For any root class excluded by the recurrence, all actual root coefficient vectors in that class are excluded. Retained classes are feasible only in this relaxation, not evidence of a correct six-comparison tree.

## Exact results
{
  "points": 51,
  "classes": 4249,
  "stages": [
    {
      "levels": 1,
      "remaining": 611
    },
    {
      "levels": 2,
      "remaining": 537,
      "cache": 632,
      "scans": 942348
    },
    {
      "levels": 3,
      "remaining": 486,
      "cache": 1714,
      "scans": 2483804
    },
    {
      "levels": 4,
      "remaining": 401,
      "cache": 3328,
      "scans": 4709201
    },
    {
      "levels": 5,
      "remaining": 393,
      "cache": 5010,
      "scans": 6857930
    },
    {
      "levels": 6,
      "remaining": 393,
      "cache": 6613,
      "scans": 8825913
    }
  ],
  "survivorRootMasks": 393
}

The first two levels reproduce R176/R177 611 and 537 survivors; level three gives 486. The full recursive finite endpoint relaxation has 393 surviving root classes, excluding 3856 of 4249. Every reported exclusion is a completed exact finite calculation. Root survivor masks are in the replay output, in the order of first occurrence of original endpoint rays in the pinned data; each pair is the positive and negative ray bitmask up to global sign. The full-domain optimum remains 6<=D_linear<=7 unless the relaxation excludes all roots. This is a mathematical lower-bound procedure, not an actual BRC runtime speed measurement.

## Dynamic intersection residual
For r·u=a<0<b=r·v, the actual cut ray is p=bu-av. A later query s has sign determined by b(s·u)-a(s·v) = (r·v)(s·u)-(r·u)(s·v). This bilinear determinant is the exact missing comparison in the fixed-original-endpoint carrier. Retaining it for true clipped intervals, including the two R177 gaps, is the next strengthening route. It is not determined by separate ternary endpoint signs in general. Example u=(1,1,1), v=(1,2,1): r=(-3,2,0) gives (-1,1); s=(-4,3,0) gives (-1,2), determinant=1; s=(-5,3,0) gives (-2,1), determinant=-1. Thus the correct signs are + and -, with same two endpoint sign patterns. This illustrates why a surviving original-ray class cannot be treated as true dynamic-cut feasibility.

## Control
Original request r2-20261125-0010-x6-read returned SUCCEEDED/error=null, observed 2026-11-24T16:10:38.765962Z, Source 0241d53a0f0549c9365421998efa71794f2350eb, NO_CANONICAL_PUBLICATION_DIRECTORY, execution_authorized=false; no native owner projection. Independent research preservation only. Activity association remains pending own verified binding.

## Reproduction
Extract the JS block to a Node file and run. Embedded data are copied from the immutable R177 source. This script was executed on the exact BigInt JS runtime; the output above omits the full survivor mask list, which the script emits.
```js
function solve(data){
const P=[],idx=new Map();for(const e of data)for(const p of e.endpoints){let k=p.join();if(!idx.has(k)){idx.set(k,P.length);P.push(p.map(BigInt));}}
const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],sg=x=>x>0n?1:x<0n?-1:0;
const S=new Map();
function rec(r,t=null,p=null,s=1,u=1){let a=0n,b=0n;for(let i=0;i<P.length;i++){let x=sg(dot(r,P[i]));if(!x&&t)x=s*sg(dot(t,P[i]));if(!x&&p)x=u*sg(dot(p,P[i]));if(x>0)a|=1n<<BigInt(i);if(x<0)b|=1n<<BigInt(i)}let k=a<b?`${a},${b}`:`${b},${a}`;if(!S.has(k))S.set(k,[a,b]);}
for(let i=0;i<P.length;i++)for(let j=i+1;j<P.length;j++){let r=cross(P[i],P[j]);if(!r.some(Boolean))continue;rec(r);for(let k=0;k<P.length;k++)if(!dot(r,P[k])){let t=cross(r,P[k]);for(let s of [-1,1]){rec(r,t,null,s);for(let u of [-1,1])rec(r,t,P[k],s,u)}}}
const Q=[...S.values()].map(([a,b])=>{let au=0n,av=0n,bu=0n,bv=0n;data.forEach((e,i)=>{let x=1n<<BigInt(idx.get(e.endpoints[0].join())),y=1n<<BigInt(idx.get(e.endpoints[1].join())),z=1n<<BigInt(i);if(a&x)au|=z;if(a&y)av|=z;if(b&x)bu|=z;if(b&y)bv|=z});return [au,av,bu,bv]});
const pc32=x=>{x=x-((x>>>1)&0x55555555);x=(x&0x33333333)+((x>>>2)&0x33333333);return (((x+(x>>>4))&0x0F0F0F0F)*0x01010101)>>>24};
const count=x=>pc32(Number(x&0xffffffffn))+pc32(Number(x>>32n));
const all=(1n<<BigInt(data.length))-1n;
function split(u,v,q){let [au,av,bu,bv]=q,pa=(u&au)|(v&av),pb=(u&bu)|(v&bv);return [u&~bu&pa,v&~bv&pa,u&~au&pb,v&~av&pb]}
const roots=Q.map((q,i)=>({i,s:split(all,all,q)})).filter(({s:[a,b,c,d]})=>count(a|b)<=31&&count(c|d)<=31);
const cache=new Map();let scans=0;
function feasible(u,v,d,k){const n=count(u|v);if(n>2**d-1)return false;if(k===0||n<=d)return true;let key=`${u},${v},${d},${k}`;if(cache.has(key))return cache.get(key);let ans=false;for(let q of Q){scans++;let [a,b,c,e]=split(u,v,q);if(count(a|b)>2**(d-1)-1||count(c|e)>2**(d-1)-1)continue;if(feasible(a,b,d-1,k-1)&&feasible(c,e,d-1,k-1)){ans=true;break}}cache.set(key,ans);return ans;}
let remaining=roots,stages=[{levels:1,remaining:remaining.length}];
for(let k=1;k<=5;k++){remaining=remaining.filter(({s:[a,b,c,d]})=>feasible(a,b,5,k)&&feasible(c,d,5,k));stages.push({levels:k+1,remaining:remaining.length,cache:cache.size,scans});}
return {points:P.length,classes:Q.length,stages,survivorRootMasks:remaining.map(({i})=>[...S.values()][i].map(String))};
}
const data=[{"normal":["187","12","-1"],"segments":9,"endpoints":[["0","1","12"],["1","17","391"]]},{"normal":["204","11","-1"],"segments":9,"endpoints":[["0","1","11"],["1","17","391"]]},{"normal":["5","-2","0"],"segments":51,"endpoints":[["2","5","73"],["2","5","5"]]},{"normal":["9","-1","0"],"segments":4,"endpoints":[["1","9","74"],["1","9","69"]]},{"normal":["85","7","-2"],"segments":10,"endpoints":[["1","9","74"],["3","17","187"]]},{"normal":["51","2","-1"],"segments":9,"endpoints":[["1","9","69"],["1","0","51"]]},{"normal":["0","1","-1"],"segments":2,"endpoints":[["2","5","5"],["1","0","0"]]},{"normal":["34","1","-1"],"segments":7,"endpoints":[["2","5","73"],["1","0","34"]]},{"normal":["187","20","-9"],"segments":5,"endpoints":[["6","15","158"],["1","1","23"]]},{"normal":["68","1","-3"],"segments":8,"endpoints":[["2","5","47"],["3","0","68"]]},{"normal":["176","22","-9"],"segments":4,"endpoints":[["6","15","154"],["19","28","440"]]},{"normal":["22","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","22"]]},{"normal":["61","0","-1"],"segments":78,"endpoints":[["0","1","0"],["1","17","61"]]},{"normal":["74","0","-1"],"segments":14,"endpoints":[["1","9","74"],["1","4","74"]]},{"normal":["126","0","-1"],"segments":103,"endpoints":[["0","1","0"],["1","30","126"]]},{"normal":["4","-1","0"],"segments":35,"endpoints":[["1","4","152"],["1","4","74"]]},{"normal":["17","-1","0"],"segments":44,"endpoints":[["0","0","1"],["1","17","22"]]},{"normal":["156","-1","-1"],"segments":46,"endpoints":[["1","4","152"],["1","30","126"]]},{"normal":["69","0","-1"],"segments":16,"endpoints":[["1","17","69"],["1","9","69"]]},{"normal":["9","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","9"]]},{"normal":["235","0","-3"],"segments":84,"endpoints":[["0","1","0"],["3","77","235"]]},{"normal":["87","0","-1"],"segments":107,"endpoints":[["0","1","0"],["1","17","87"]]},{"normal":["104","-1","-1"],"segments":60,"endpoints":[["1","4","100"],["3","77","235"]]},{"normal":["38","0","-3"],"segments":57,"endpoints":[["0","1","0"],["3","40","38"]]},{"normal":["5","0","-2"],"segments":72,"endpoints":[["0","1","0"],["2","5","5"]]},{"normal":["39","-1","-1"],"segments":50,"endpoints":[["3","1","116"],["1","17","22"]]},{"normal":["40","0","-3"],"segments":63,"endpoints":[["0","1","0"],["3","38","40"]]},{"normal":["26","-1","-1"],"segments":39,"endpoints":[["2","5","47"],["3","53","25"]]},{"normal":["25","0","-3"],"segments":52,"endpoints":[["0","1","0"],["3","53","25"]]},{"normal":["83","0","-2"],"segments":69,"endpoints":[["0","1","0"],["2","34","83"]]},{"normal":["102","-7","-1"],"segments":14,"endpoints":[["1","4","74"],["3","17","187"]]},{"normal":["204","-11","1"],"segments":51,"endpoints":[["0","1","11"],["1","30","126"]]},{"normal":["395","0","-2"],"segments":119,"endpoints":[["0","1","0"],["2","73","395"]]},{"normal":["289","18","-1"],"segments":10,"endpoints":[["0","1","18"],["1","17","595"]]},{"normal":["66","2","-1"],"segments":11,"endpoints":[["1","4","74"],["1","0","66"]]},{"normal":["132","5","-1"],"segments":16,"endpoints":[["1","17","217"],["1","0","132"]]},{"normal":["44","1","-1"],"segments":9,"endpoints":[["1","17","61"],["1","11","55"]]},{"normal":["88","3","-1"],"segments":7,"endpoints":[["1","4","100"],["1","0","88"]]},{"normal":["88","7","-3"],"segments":5,"endpoints":[["1","17","69"],["1","11","55"]]},{"normal":["132","-7","-1"],"segments":14,"endpoints":[["1","9","69"],["1","11","55"]]},{"normal":["153","8","-1"],"segments":7,"endpoints":[["1","9","225"],["1","0","153"]]},{"normal":["153","5","-4"],"segments":1,"endpoints":[["3","1","116"],["4","0","153"]]},{"normal":["117","-2","-2"],"segments":42,"endpoints":[["2","5","112"],["2","34","83"]]},{"normal":["198","8","-1"],"segments":5,"endpoints":[["1","4","230"],["1","0","198"]]},{"normal":["198","5","-4"],"segments":11,"endpoints":[["2","8","109"],["2","0","99"]]},{"normal":["306","17","-1"],"segments":8,"endpoints":[["1","17","595"],["1","0","306"]]},{"normal":["234","-1","-1"],"segments":43,"endpoints":[["1","4","230"],["2","73","395"]]}];
const result=solve(data);
console.log(JSON.stringify(result,null,2));
if(JSON.stringify(result.stages.map(x=>x.remaining))!=="[611,537,486,401,393,393]")throw Error("census mismatch");
```
