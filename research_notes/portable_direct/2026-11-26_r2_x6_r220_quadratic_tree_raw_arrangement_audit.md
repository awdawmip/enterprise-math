# X6 R220 — fixed six-query quadratic tree, raw arrangement replay

2026-11-26. AUTHOR CHECK / EXACT BIGINT / NOT_REVIEWED. R219 frozen tree at 180042eca43ea1f5bbc0c6e0f409db70b53ebd42:research_notes/portable_direct/2026-11-26_r2_x6_r219_support_product_query_experiment.md. R217@c7d78ae72c2dcb4970f9b830397f6be65e359fb1 supplies 35 mandatory output witnesses and hence binary depth >=6. R168@ee8eb26824479ec56924b81871b0cd7b38bee8ce and R162–R165 supply inherited bank coverage. R216@0b5f89c35844559a07c3cd49c25f882ae1c7472f gives author-level arbitrary linear lower bound 7. Same Port 10, weights (17t,B,22t,D)>0, original six BRC gap/capacity relations, 1935 unoriented directions, strict 3/2 near set and legal eta term. P000/ACTIVE retained; auxiliary parameter chart, not a native spatial plane or dynamic claim.

## Conclusion

D_quadratic=6 for the declared binary sign test model of degree at most two, conditional only on the inherited bank proofs and exact witness lower bound. Each query is a fixed single polynomial sign, not a Boolean oracle. In fact products of the original mandatory support linear forms suffice. R219 generated a depth-six tree; this replay reads the fixed tree, does not search it, and uses the expanded raw threshold arrangement (all nonzero channels for V rather than reduced masks), independent cross-product intersection implementation and a common denominator exact integer scoring method. Every query factor is in this arrangement. Its faces carry constant term order and near membership. All positive face representatives (vertices, edges, cells) are checked, including zero-product cases. The full direction check at one representative per complete support-sign pattern is additional sampled validation, not a replacement for the inherited bank proof on the continuum. No independent reviewer or formal acceptance claimed.

Root polynomial: (204t+11B-D)(83t-2D)>0. Both factors are mandatory support forms from R176; 47 factors are used throughout. The two-factor queries preserve joint sign structure. Arithmetic and multiplication costs are not part of the binary observation depth. If a model requires exactly degree two rather than at most two, multiply the single linear query by t>0. All polynomials are homogeneous in the three auxiliary weight coordinates.

## Exact observed output

```json
{
  "rawLines": 256,
  "cells": 11487,
  "positiveRepresentatives": 43685,
  "treeReplay": "PASS",
  "depthCounts": {
    "5": 7871,
    "6": 35814
  },
  "uniqueOutputs": 35,
  "fullPopulation": 1935,
  "fullPatternRepresentatives": 1925,
  "fullDirectionChecks": 3724875,
  "stats": {
    "nodes": 54,
    "leaves": 55,
    "linear": 1,
    "quadratic": 53,
    "leafDepths": {
      "5": 9,
      "6": 46
    },
    "outputs": 35,
    "factors": 47
  }
}
```

## Standalone audit (fixed tree, no search)

```javascript
function audit(tree){
const R="187,12,-1;204,11,-1;5,-2,0;9,-1,0;85,7,-2;51,2,-1;0,1,-1;34,1,-1;187,20,-9;68,1,-3;176,22,-9;22,0,-1;61,0,-1;74,0,-1;126,0,-1;4,-1,0;17,-1,0;156,-1,-1;69,0,-1;9,0,-1;235,0,-3;87,0,-1;104,-1,-1;38,0,-3;5,0,-2;39,-1,-1;40,0,-3;26,-1,-1;25,0,-3;83,0,-2;102,-7,-1;204,-11,1;395,0,-2;289,18,-1;66,2,-1;132,5,-1;44,1,-1;88,3,-1;88,7,-3;132,-7,-1;153,8,-1;153,5,-4;117,-2,-2;198,8,-1;198,5,-4;306,17,-1;234,-1,-1".split(";").map(s=>s.split(",").map(BigInt));
const V=[[1,0,0],[1,3,-1],[4,-4,1],[4,-1,0],[5,-4,1],[5,-1,0],[6,-4,1],[6,-1,0],[7,-1,0],[9,-5,1]],T=[[0,1],[0,2],[0,3],[1,3],[1,6],[2,3],[2,6],[2,7],[2,11],[2,12],[3,2],[3,3],[4,6],[4,12],[5,7]],E=[[17n,1n,0n],[39n,0n,0n],[17n,0n,1n],[22n,1n,0n],[0n,1n,1n],[22n,0n,1n]];
function gaps(v){let [x,y,z]=v,h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z];return [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]].map(([i,j])=>BigInt(Math.abs(h[i]-h[j])))}
const G=V.map(gaps),W=[0,3,5,6,7,9],D=[];
for(let x=-10;x<=10;x++)for(let y=-10;y<=10;y++)for(let z=-10;z<=10;z++){let v=[x,y,z];if((v.find(a=>a!==0)||0)>0&&v.reduce((s,a)=>s+Math.max(a,0),0)<=10&&v.reduce((s,a)=>s+Math.max(-a,0),0)<=10)D.push([v,gaps(v)])}
const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){let t=a%b;a=b;b=t}return a}
function norm(a,unoriented=false){let d=gcd(gcd(a[0],a[1]),a[2]);if(!d)return a;a=a.map(x=>x/d);if(unoriented&&a.find(x=>x!==0n)<0n)a=a.map(x=>-x);return a}
let raw=new Map();function addLine(a){a=norm(a,true);if(a.some(x=>x>0n)&&a.some(x=>x<0n))raw.set(a.join(),a)}
for(let i=0;i<T.length;i++){let [j,g]=T[i];for(let k=i+1;k<T.length;k++){let [h,f]=T[k];addLine(E[h].map((x,s)=>BigInt(g)*x-BigInt(f)*E[j][s]))}for(let gg of G)for(let h=0;h<6;h++)if(gg[h])addLine(E[h].map((x,s)=>3n*BigInt(g)*x-2n*gg[h]*E[j][s]))}
let L=[...raw.values()];for(let r of R)if(!raw.has(norm(r,true).join()))throw Error("support absent");
let cells=[[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]]];
for(let l of L){let next=[];for(let cell of cells){let sig=cell.map(x=>dot(l,x));if(!sig.some(x=>x>0n)||!sig.some(x=>x<0n)){next.push(cell);continue}for(let side of [1n,-1n]){let out=[];for(let i=0;i<cell.length;i++){let j=(i+1)%cell.length,a=sig[i],b=sig[j];if(a*side>=0n)out.push(cell[i]);if(a*b<0n){let r=cross(cross(cell[i],cell[j]),l);if(r.some(x=>x<0n))r=r.map(x=>-x);if(r.some(x=>x<0n)||!r.some(x=>x>0n)||dot(r,l)!==0n)throw Error("bad intersection");out.push(norm(r))}}next.push(out)}}cells=next}
const pts=new Map();function put(a){if(a.every(x=>x>0n)){a=norm(a);pts.set(a.join(),a)}}function sum(a){return [0,1,2].map(i=>a.reduce((s,x)=>s+x[i],0n))}
for(let c of cells){put(sum(c));for(let i=0;i<c.length;i++){put(c[i]);put(sum([c[i],c[(i+1)%c.length]]))}}
function runTree(p){let node=tree,d=0;while(node.q){let [i,j,sg]=node.q;let x=dot(R[i],p)*BigInt(sg);if(j!==-1)x*=dot(R[j],p);node=x>0n?node.yes:node.no;d++}return [node.out,d]}
const vi=new Map(V.map((v,i)=>[v.join(),i])),covered=new Set();let exactFull=0,outs=new Set(),depthCounts={},fullMasks=0,fullChecks=0;
function max(a){return a.reduce((x,y)=>x>y?x:y)}
function min(a){return a.reduce((x,y)=>x<y?x:y)}
for(let p of pts.values()){
let c=E.map(e=>dot(e,p)),prod=c.reduce((s,x)=>s*x,1n),scale=c.map(x=>prod/x),scores=G.map(g=>max(g.map((a,i)=>a*scale[i]))),eta=min(W.map(i=>scores[i])),near=0;
for(let i=0;i<scores.length;i++)if(2n*scores[i]<3n*eta)near|=1<<i;
let [[n,m],depth]=runTree(p),i=Math.log2(m),[j,g]=T[i];if(n!==near||BigInt(g)*scale[j]!==eta)throw Error("tree mismatch");
outs.add([n,m].join());depthCounts[depth]=(depthCounts[depth]||0)+1;
let k=R.map(r=>{let x=dot(r,p);return x>0n?1:x<0n?-1:0}).join();if(!covered.has(k)){covered.add(k);let s=D.map(([v,g])=>max(g.map((a,i)=>a*scale[i]))),f=min(s),mask=0;if(f!==eta)throw Error("full optimum mismatch");for(let i=0;i<s.length;i++)if(2n*s[i]<3n*f){let j=vi.get(D[i][0].join());if(j===undefined)throw Error("full outsider");mask|=1<<j}if(mask!==n)throw Error("full near mismatch");fullChecks+=D.length;exactFull++;}}
let stats={nodes:0,leaves:0,linear:0,quadratic:0,leafDepths:{},outputs:new Set(),factors:new Set()};function walk(t,d){if(t.out){stats.leaves++;stats.leafDepths[d]=(stats.leafDepths[d]||0)+1;stats.outputs.add(t.out.join());return}stats.nodes++;let [i,k]=t.q;stats.factors.add(i);if(k<0)stats.linear++;else{stats.quadratic++;stats.factors.add(k)}walk(t.yes,d+1);walk(t.no,d+1)}walk(tree,0);
return {rawLines:L.length,cells:cells.length,positiveRepresentatives:pts.size,treeReplay:"PASS",depthCounts,uniqueOutputs:outs.size,fullPopulation:D.length,fullPatternRepresentatives:exactFull,fullDirectionChecks:fullChecks,stats:{...stats,outputs:stats.outputs.size,factors:stats.factors.size}};
}
const tree={"q":[1,29,1],"yes":{"q":[0,26,-1],"yes":{"q":[2,7,-1],"yes":{"q":[16,27,-1],"yes":{"q":[2,25,1],"yes":{"q":[2,41,1],"yes":{"out":[951,4096]},"no":{"out":[693,4096]}},"no":{"q":[0,2,1],"yes":{"out":[693,4096]},"no":{"out":[693,16]}}},"no":{"q":[0,16,1],"yes":{"out":[132,16]},"no":{"q":[0,11,1],"yes":{"out":[693,16]},"no":{"out":[693,64]}}}},"no":{"q":[9,25,-1],"yes":{"q":[2,8,-1],"yes":{"out":[951,4]},"no":{"q":[2,10,-1],"yes":{"out":[695,4]},"no":{"out":[693,4]}}},"no":{"q":[0,7,1],"yes":{"out":[132,4]},"no":{"q":[0,1,1],"yes":{"out":[693,4096]},"no":{"out":[72,1]}}}}},"no":{"q":[0,24,-1],"yes":{"q":[0,27,1],"yes":{"q":[0,2,1],"yes":{"out":[132,4]},"no":{"out":[132,16]}},"no":{"q":[19,27,1],"yes":{"q":[0,23,-1],"yes":{"out":[692,16]},"no":{"out":[676,16]}},"no":{"q":[27,28,1],"yes":{"out":[164,16]},"no":{"out":[132,16]}}}},"no":{"q":[0,-1,1],"yes":{"q":[0,6,1],"yes":{"out":[132,32]},"no":{"out":[132,4]}},"no":{"q":[1,16,1],"yes":{"q":[1,33,-1],"yes":{"out":[72,512]},"no":{"out":[64,512]}},"no":{"q":[0,45,-1],"yes":{"out":[72,8192]},"no":{"out":[64,8192]}}}}}},"no":{"q":[11,20,1],"yes":{"q":[31,35,1],"yes":{"q":[15,46,-1],"yes":{"q":[17,22,-1],"yes":{"q":[0,21,-1],"yes":{"out":[633,8]},"no":{"out":[569,8]}},"no":{"q":[0,14,1],"yes":{"out":[561,8]},"no":{"out":[633,8192]}}},"no":{"q":[31,37,-1],"yes":{"q":[0,3,1],"yes":{"out":[121,1024]},"no":{"out":[72,8192]}},"no":{"q":[0,3,1],"yes":{"out":[49,1024]},"no":{"out":[72,256]}}}},"no":{"q":[11,31,-1],"yes":{"q":[40,46,1],"yes":{"q":[1,40,1],"yes":{"out":[121,8192]},"no":{"out":[72,8192]}},"no":{"q":[43,46,1],"yes":{"out":[89,8192]},"no":{"out":[72,8192]}}},"no":{"q":[0,14,-1],"yes":{"q":[0,32,1],"yes":{"out":[633,256]},"no":{"out":[72,256]}},"no":{"q":[0,21,-1],"yes":{"out":[633,8]},"no":{"out":[569,8]}}}}},"no":{"q":[5,16,1],"yes":{"q":[18,42,1],"yes":{"q":[0,12,1],"yes":{"q":[0,44,1],"yes":{"out":[693,4096]},"no":{"out":[689,4096]}},"no":{"out":[561,8]}},"no":{"q":[0,38,-1],"yes":{"q":[0,39,1],"yes":{"out":[561,4096]},"no":{"out":[561,16384]}},"no":{"q":[0,36,1],"yes":{"out":[561,4096]},"no":{"out":[561,2048]}}}},"no":{"q":[3,34,1],"yes":{"q":[4,30,1],"yes":{"q":[0,13,1],"yes":{"out":[561,128]},"no":{"out":[561,8]}},"no":{"q":[0,4,-1],"yes":{"out":[561,4096]},"no":{"out":[561,2]}}},"no":{"q":[12,15,1],"yes":{"out":[561,8]},"no":{"q":[0,3,1],"yes":{"out":[49,1024]},"no":{"out":[561,64]}}}}}}};
console.log(JSON.stringify(audit(tree),null,2));
```

## Next

Audit inherited R162–R168 bank proof and R216 linear lower bound independently; extend quadratic comparison model to other ratios and Ports. Consider a weighted arithmetic resource model separately, since one product query can cost more than one linear comparison. Current X6 task read r2-20261126-1015-x6-read SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY; no active owner projection, no CLAIM, current lane identity and Activity association unconfirmed.
