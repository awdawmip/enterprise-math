# X6 R220 / R217 independent informed Driver audit — exact quadratic-depth closure

2026-11-26. Same frozen Port 10, w=(17t,B,22t,D)>0, 1935 directions modulo sign, six BRC gap/capacity relations, fixed leaf output one of 15 legal optimizer terms and full strict 3/2-near direction mask. Original author EM-DIRECT-AE5AD5 retained. This audit reuses the already independently proved R168 linear upper tree and R216 lower bound (ff51e44cfd5093eb9f1b153fd24e10077f4231f9:research_notes/driver/2026-11-26_x6_r216_independent_sharpness_audit.md), not the author's reduced-bank completeness. Informed nonauthor, not blind.

## Proof
Normalize by positive scaling to the open projective triangle. Form the common arrangement of the linear reference tree's actually used predicates, all 47 product factors, and all pairwise equality forms of the 15 optimizer terms. Every relatively open face has constant signs, including zero. Exact polygon clipping partitions the closed triangle, and positive primitive representatives of each polygon, each edge and each vertex exhaust the open domain's faces. Every polygon barycenter/edge midpoint is represented by a positive sum of its homogeneous vertex rays; equality and strict sign are invariant under positive scaling. At each representative evaluate both fixed trees using exact integer signs (zero follows no). Verify equal near mask and cross-multiplied equality of the two returned optimizer terms. As the equality forms are in the arrangement, agreement at one representative proves agreement over the entire face. The independently proved linear tree is correct on the entire cone; the fixed quadratic tree therefore inherits correctness on the entire cone, without a new bank-coverage assumption or sampled extrapolation.

Independently enumerate the entire Port10 direction population and evaluate all 35 R217 witness points with common-denominator integer arithmetic. Each point forces exactly one of the 15 permitted terms and the indicated complete near mask. The 35 distinct pairs force at least 35 leaves, hence binary depth at least 6 even for arbitrary tests. The verified fixed product tree has depth at most 6 and uses exactly 35 distinct outputs; therefore minimum output cover is 35 and D_quadratic=D_Boolean=6. R217 affine argument independently valid: on t+B+D=1 any affine predicate a·p+b becomes (a+b(1,1,1))·p, preserving strict and equality cases; scaling transfers correctness. Thus D_affine=D_linear=7 using previous R216 audit. The comparison counts oracle calls, not cost of evaluating products. No native dynamics or formal admission asserted.

## Inputs
- linear: 970a1f004df5e8f0eb7ea581fb3168f8db66ef00:research_notes/driver/2026-11-26_x6_r168_independent_full_direction_upper_audit.json
- quad: fc01363a177cea3e107d701741022e72e7a29368:research_notes/portable_direct/2026-11-26_r2_x6_r220_quadratic_tree_raw_arrangement_audit.md
- lower: c7d78ae72c2dcb4970f9b830397f6be65e359fb1:research_notes/portable_direct/2026-11-26_r2_x6_r217_exact_output_cover_affine_extension.md

## Exact result
```json
{
  "linearPredicatesUsed": 55,
  "productFactors": 47,
  "refinementLines": 88,
  "polygons": 1471,
  "positiveFaceRepresentatives": 5425,
  "depthCounts": {
    "5": 919,
    "6": 4506
  },
  "feasibleLeaves": 55,
  "distinctOutputs": 35,
  "tieCounts": {
    "sameTerm": 5238,
    "differentEqualTerm": 187
  },
  "productZeroCounts": {
    "zeroQueryEncountered": 1088
  },
  "forcedOutputs": 35,
  "directions": 1935,
  "fullWitnessDirectionChecks": 67725,
  "witnesses": [
    {
      "p": [
        "18",
        "26",
        "1241"
      ],
      "near": 49,
      "termMask": 1024
    },
    {
      "p": [
        "3",
        "53",
        "1821"
      ],
      "near": 64,
      "termMask": 512
    },
    {
      "p": [
        "3",
        "1",
        "935"
      ],
      "near": 64,
      "termMask": 8192
    },
    {
      "p": [
        "7",
        "123",
        "2783"
      ],
      "near": 72,
      "termMask": 1
    },
    {
      "p": [
        "2",
        "1049",
        "395"
      ],
      "near": 72,
      "termMask": 256
    },
    {
      "p": [
        "8",
        "140",
        "3797"
      ],
      "near": 72,
      "termMask": 512
    },
    {
      "p": [
        "43",
        "1520",
        "8542"
      ],
      "near": 72,
      "termMask": 8192
    },
    {
      "p": [
        "4",
        "1",
        "620"
      ],
      "near": 89,
      "termMask": 8192
    },
    {
      "p": [
        "41",
        "51",
        "3776"
      ],
      "near": 121,
      "termMask": 1024
    },
    {
      "p": [
        "9",
        "147",
        "1943"
      ],
      "near": 121,
      "termMask": 8192
    },
    {
      "p": [
        "6",
        "1",
        "11"
      ],
      "near": 132,
      "termMask": 4
    },
    {
      "p": [
        "3",
        "10",
        "9"
      ],
      "near": 132,
      "termMask": 16
    },
    {
      "p": [
        "7",
        "2",
        "1"
      ],
      "near": 132,
      "termMask": 32
    },
    {
      "p": [
        "11",
        "193",
        "97"
      ],
      "near": 164,
      "termMask": 16
    },
    {
      "p": [
        "4",
        "35",
        "275"
      ],
      "near": 561,
      "termMask": 2
    },
    {
      "p": [
        "12",
        "1552",
        "775"
      ],
      "near": 561,
      "termMask": 8
    },
    {
      "p": [
        "2",
        "44",
        "83"
      ],
      "near": 561,
      "termMask": 64
    },
    {
      "p": [
        "74",
        "439",
        "4809"
      ],
      "near": 561,
      "termMask": 128
    },
    {
      "p": [
        "36",
        "610",
        "2195"
      ],
      "near": 561,
      "termMask": 2048
    },
    {
      "p": [
        "2",
        "18",
        "99"
      ],
      "near": 561,
      "termMask": 4096
    },
    {
      "p": [
        "44",
        "500",
        "2509"
      ],
      "near": 561,
      "termMask": 16384
    },
    {
      "p": [
        "2",
        "352",
        "159"
      ],
      "near": 569,
      "termMask": 8
    },
    {
      "p": [
        "13",
        "2514",
        "1132"
      ],
      "near": 633,
      "termMask": 8
    },
    {
      "p": [
        "2",
        "795",
        "265"
      ],
      "near": 633,
      "termMask": 256
    },
    {
      "p": [
        "9",
        "260",
        "1202"
      ],
      "near": 633,
      "termMask": 8192
    },
    {
      "p": [
        "53",
        "745",
        "646"
      ],
      "near": 676,
      "termMask": 16
    },
    {
      "p": [
        "8",
        "20",
        "421"
      ],
      "near": 689,
      "termMask": 4096
    },
    {
      "p": [
        "35",
        "488",
        "444"
      ],
      "near": 692,
      "termMask": 16
    },
    {
      "p": [
        "5",
        "8",
        "117"
      ],
      "near": 693,
      "termMask": 4
    },
    {
      "p": [
        "11",
        "97",
        "191"
      ],
      "near": 693,
      "termMask": 16
    },
    {
      "p": [
        "7",
        "123",
        "156"
      ],
      "near": 693,
      "termMask": 64
    },
    {
      "p": [
        "90",
        "204",
        "3319"
      ],
      "near": 693,
      "termMask": 4096
    },
    {
      "p": [
        "104",
        "149",
        "2437"
      ],
      "near": 695,
      "termMask": 4
    },
    {
      "p": [
        "10",
        "1",
        "228"
      ],
      "near": 951,
      "termMask": 4
    },
    {
      "p": [
        "7",
        "2",
        "242"
      ],
      "near": 951,
      "termMask": 4096
    }
  ]
}
```

## Reproduction
Extract the fixed tree and R factors from R220, parse the R217 first JSON block and the independent R168 JSON as above; invoke this exact standalone verification function. No search or new tree generation.
```javascript
function verify(lin,quad,R,low){
const E=[[17,1,0],[39,0,0],[17,0,1],[22,1,0],[0,1,1],[22,0,1]].map(x=>x.map(BigInt)),T=lin.terms.map(([j,g])=>[j,BigInt(g)]),P=lin.predForms.map(x=>x.map(BigInt));R=R.map(x=>x.map(BigInt));
const abs=x=>x<0n?-x:x,gcd=(a,b)=>{a=abs(a);b=abs(b);while(b){[a,b]=[b,a%b]}return a},norm=a=>{let d=a.reduce(gcd,0n);return d?a.map(x=>x/d):a},dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n),sum=a=>[0,1,2].map(i=>a.reduce((s,x)=>s+x[i],0n)),neg=a=>a.map(x=>-x);
const lines=new Map();function add(a){a=norm(a);if(!a.some(x=>x>0n)||!a.some(x=>x<0n))return;if(a.find(x=>x!==0n)<0n)a=neg(a);lines.set(a.join(),a)}
const used=new Set();function visit(t){if(t.leaf)return;used.add(t.q);visit(t.yes);visit(t.no)}visit(lin.tree);for(let i of used)add(P[i]);for(let r of R)add(r);
for(let i=0;i<T.length;i++)for(let j=i+1;j<T.length;j++){let [a,g]=T[i],[b,h]=T[j];add(E[b].map((x,k)=>g*x-h*E[a][k]))}
let cells=[[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]]];for(let l of lines.values()){let next=[];for(let c of cells){let s=c.map(x=>dot(l,x));if(!s.some(x=>x>0n)||!s.some(x=>x<0n)){next.push(c);continue}let pos=[],ne=[];for(let i=0;i<c.length;i++){let j=(i+1)%c.length,a=s[i],b=s[j];if(a>=0n)pos.push(c[i]);if(a<=0n)ne.push(c[i]);if(a*b<0n){let z=norm(c[i].map((x,k)=>abs(b)*x+abs(a)*c[j][k]));pos.push(z);ne.push(z)}}next.push(pos,ne)}cells=next}
const pts=new Map();function put(x){if(x.every(v=>v>0n)){x=norm(x);pts.set(x.join(),x)}}for(let c of cells){put(sum(c));for(let i=0;i<c.length;i++){put(c[i]);put(sum([c[i],c[(i+1)%c.length]]))}}
const output=new Set(),leafPaths=new Set(),depthCounts={},tieCounts={sameTerm:0,differentEqualTerm:0},productZeroCounts={zeroQueryEncountered:0};
for(let x of pts.values()){let a=lin.tree,b=quad,path="",zero=false;while(!a.leaf)a=dot(P[a.q],x)>0n?a.yes:a.no;while(!b.out){let [i,j,s]=b.q,v=dot(R[i],x)*BigInt(s)*(j<0?1n:dot(R[j],x));if(v===0n)zero=true;path+=v>0n?"1":"0";b=v>0n?b.yes:b.no}
let [li,near]=a.leaf,[n,m]=b.out,qi=Math.log2(m);if(!Number.isInteger(qi)||near!==n)throw Error("near mismatch "+x);let [u,g]=T[li],[v,h]=T[qi];if(g*dot(E[v],x)!==h*dot(E[u],x))throw Error("term mismatch "+x);if(qi===li)tieCounts.sameTerm++;else tieCounts.differentEqualTerm++;if(zero)productZeroCounts.zeroQueryEncountered++;output.add(b.out.join());leafPaths.add(path);depthCounts[path.length]=(depthCounts[path.length]||0)+1}
function gaps([x,y,z]){let h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z];return [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]].map(([i,j])=>BigInt(Math.abs(h[i]-h[j])))}
let D=[];for(let x=-10;x<=10;x++)for(let y=-10;y<=10;y++)for(let z=-10;z<=10;z++){let v=[x,y,z];if((v.find(a=>a!==0)||0)>0&&v.reduce((s,a)=>s+Math.max(a,0),0)<=10&&v.reduce((s,a)=>s+Math.max(-a,0),0)<=10)D.push([v,gaps(v)])}
const vi=new Map(lin.directions.map((v,i)=>[v.join(),i])),forced=new Set(),witnesses=[];let checks=0;for(let row of low.rows)for(let [mask,ps] of row.witnesses){let p=ps.map(BigInt),c=E.map(x=>dot(x,p)),den=c.reduce((a,b)=>a*b,1n),scale=c.map(x=>den/x),f=D.map(([v,g])=>g.map((h,i)=>h*scale[i]).reduce((a,b)=>a>b?a:b)),eta=f.reduce((a,b)=>a<b?a:b),M=0,N=0;T.forEach(([j,g],i)=>{if(g*scale[j]===eta)M|=1<<i});for(let i=0;i<D.length;i++)if(2n*f[i]<3n*eta){let k=vi.get(D[i][0].join());if(k===undefined)throw Error("outsider");N|=1<<k}if(M!==mask||N!==row.near||!M||(M&(M-1)))throw Error("bad forced witness");forced.add([N,M].join());witnesses.push({p:ps,near:N,termMask:M});checks+=D.length}
return {linearPredicatesUsed:used.size,productFactors:R.length,refinementLines:lines.size,polygons:cells.length,positiveFaceRepresentatives:pts.size,depthCounts,feasibleLeaves:leafPaths.size,distinctOutputs:output.size,tieCounts,productZeroCounts,forcedOutputs:forced.size,directions:D.length,fullWitnessDirectionChecks:checks,witnesses};
}
```
