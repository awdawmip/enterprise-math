"use strict";
// Independent JavaScript/BigInt check: all legal h=2,3 words and conditional h=4.
const OPS={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const ATOMS=[['N',0],['N',1],['N',2],['A',0],['A',2],['B',0],['B',1],['AB',0],['BA',0]];
const LABELS=['N','A','B','AB','BA'];
function native(w){return [...w].flatMap(x=>OPS[x]);}
function positives(w){let x=native(w);return [1,2,3,4,5,6].map(a=>x.filter(v=>v===a).length).join(',');}
function displacement(w){let x=native(w);return [1,2,3,4,5,6].map(a=>x.filter(v=>v===a).length-x.filter(v=>v===-a).length).join(',');}
function transfer(w){let x=native(w);return ATOMS.map(([s,start])=>{
 let prev=start;
 for(const v of x){if(prev===1&&v===2)s=({N:'A',B:'BA'})[s]||s;
 if(prev===2&&v===1)s=({N:'B',A:'AB'})[s]||s;
 prev=v;}return LABELS.indexOf(s);
});}
function rank(W){const P=1000003,rows=Array.from({length:9},()=>[]);
 for(const w of W){let t=transfer(w);for(let b=0;b<5;b++)for(let r=0;r<9;r++)rows[r].push(+ (t[r]===b));}
 let col=0,r=0;const n=rows[0].length;
 for(;col<n&&r<9;col++){
  let pivot=r;while(pivot<9&&rows[pivot][col]===0)pivot++;
  if(pivot===9)continue;
  [rows[pivot],rows[r]]=[rows[r],rows[pivot]];
  let inv=modPow(rows[r][col],P-2,P);
  for(let j=col;j<n;j++)rows[r][j]=(rows[r][j]*inv)%P;
  for(let i=r+1;i<9;i++)if(rows[i][col]){let k=rows[i][col];for(let j=col;j<n;j++)rows[i][j]=(rows[i][j]-k*rows[r][j]%P+P)%P;}
  r++;
 }
 return r;
}
function modPow(a,e,p){let x=1;while(e){if(e%2)x=x*a%p;a=a*a%p;e=Math.floor(e/2);}return x;}
function allWords(h){let out=[''];for(let j=0;j<h;j++)out=out.flatMap(s=>Object.keys(OPS).map(x=>s+x));return out.filter(w=>displacement(w)==='2,0,0,0,0,0');}
function prefixSet(ws){let a=new Set();for(let w of ws){let n=native(w);for(let j=1;j<=n.length;j++)a.add(n.slice(0,j).join(','));}return a;}
function cost(ws){return prefixSet(ws).size;}
function assert(x,t){if(!x)throw Error(t);}
const base=['ce','de','ec','ed'];const two=allWords(2),three=allWords(3),four=allWords(4);
assert(two.length===8&&three.length===51&&four.length===304,'word cardinality');
let h2good=0;for(let m=1;m<(1<<two.length);m++){
 let s=two.filter((_,j)=>(m>>j)&1);
 if(new Set(s.map(positives)).size===1&&rank(s)===9){h2good++;assert(s.join(',')===base.join(','),'h2 forced');}
}
assert(h2good===1,'h2 unique');
const byP=new Map();for(const w of three){let p=positives(w);if(!byP.has(p))byP.set(p,[]);byP.get(p).push(w);}
let tuples=new Map(),fibreMin=[];
for(const [p,ww] of byP){let min=1e10;
 for(let m=1;m<(1<<ww.length);m++){
  let s=ww.filter((_,i)=>(m>>i)&1);
  if(rank(s)!==9)continue;
  let all=base.concat(s),E=cost(all),M=new Set(all.map(positives)).size,S=new Set(all.map(w=>transfer(w).join(','))).size;
  min=Math.min(E,min);let key=`${E},${M},${S}`;if(!tuples.has(key))tuples.set(key,{words3:s});
 }
 if(min<1e10)fibreMin.push({p,min_E:min});
}
let triples=[...tuples].map(([k,v])=>({a:k.split(',').map(Number),...v}));
let front=triples.filter(x=>!triples.some(y=>y!==x&&y.a.every((v,i)=>v<=x.a[i])&&y.a.some((v,i)=>v<x.a[i])))
 .map(x=>x.a).sort((a,b)=>a[0]-b[0]);
assert(JSON.stringify(front)===JSON.stringify([[36,2,4],[42,1,6]]),'H3 Pareto');
const p4='4,2,1,0,0,0',wanted=base.map(x=>transfer(x).join(','));
const groups={};for(let h of [3,4]){
 groups[h]=wanted.map(t=>(h===3?three:four).filter(w=>positives(w)===p4&&transfer(w).join(',')===t));
}
assert(JSON.stringify(groups[3].map(x=>x.length))==='[2,2,1,1]','h3 group sizes');
assert(groups[4].every(x=>x.length===12),'h4 group sizes');
// precompute union of native-prefix edges as bit-masks for independent cost evaluation
let pool=new Set([...base,...groups[3].flat(),...groups[4].flat()]);
let edgeNames=[...prefixSet([...pool])];let edgeIDs=new Map(edgeNames.map((x,j)=>[x,j]));
let masks=new Map([...pool].map(w=>[w,[...prefixSet([w])].reduce((m,x)=>m|(1n<<BigInt(edgeIDs.get(x))),0n)]));
let b=base.reduce((m,w)=>m|masks.get(w),0n);
let min4=999,example=[],candidates=0;
function* cart(gs,i=0,prefix=[]){if(i===gs.length){yield prefix;return;}for(let w of gs[i])yield* cart(gs,i+1,prefix.concat(w));}
for(const ws3 of cart(groups[3])){
 let x=ws3.reduce((m,w)=>m|masks.get(w),b);
 for(const ws4 of cart(groups[4])){
  let y=ws4.reduce((m,w)=>m|masks.get(w),x);candidates++;
  const E=y.toString(2).replace(/0/g,'').length;
  if(E<min4){min4=E;example=[ws3,ws4];}
 }
}
assert(candidates===82944&&min4===56,'H4 conditional exact min');
const family=[];for(let h=2;h<=16;h++){
 const ws=base.map(x=>x+'f'.repeat(h-2));
 assert(rank(ws)===9&&new Set(ws.map(positives)).size===1,'family rank/positive');
 family.push(...ws);
 assert(cost(family)===8*h+12,'family E');
 assert(new Set(family.map(positives)).size===h-1,'family M');
 assert(new Set(family.map(w=>transfer(w).join(','))).size===4,'family S');
}
console.log(JSON.stringify({unit:'EC49EO',status:'PASS',arith:'JS modular Gaussian elimination plus native prefix BigInt',
 h2_return_words:two.length,h2_full_rank_subsets:h2good,h3_return_words:three.length,h4_return_words:four.length,
 h3_full_rank_fibre_minima:fibreMin.sort((a,b)=>a.p.localeCompare(b.p)),h3_pareto:front,
 h4_conditional:{M:2,S:4,E:min4,complete_representative_combinations:candidates,example},
 family:{H_range:[2,16],formula_E:'8H+12',formula_M:'H-1',S:4},
 determinant_bound:'max 9x9 0/1 minor <= 3^9=19683 < 1000003'},null,2));
