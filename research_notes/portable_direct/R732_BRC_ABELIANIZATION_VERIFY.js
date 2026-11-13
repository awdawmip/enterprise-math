/** R732: exact CNB S3 holonomy / commutative V29-count observer test.
 * Pure Node.js exact integer enumeration; no dependencies.
 * Run: node R732_BRC_ABELIANIZATION_VERIFY.js > R732_BRC_ABELIANIZATION_RESULTS.json
 */
'use strict';
const triads=['012','013','014','023','024','034','123','124','134','234'];
const edges=[];
for (const u of triads) for (const v of triads)
  if ([...u].filter(c=>v.includes(c)).length===2) edges.push(u+'>'+v);
if (edges.length!==60) throw Error('universe is not 60');
const masks={A:211733226574n,B:5363347296468n};
const pairPorts=p=>{let a=[];for(let i=0;i<p;i++)for(let j=0;j<p;j++)if(i!==j)a.push([i,j]);return a;};
function holonomy(path) {
  const frame={0:0,1:1,2:2};
  for (let k=1;k<path.length;k++) {
    const u=path[k-1],v=path[k];
    if([...u].filter(c=>v.includes(c)).length!==2) throw Error('nonadjacent triads');
    const leave=[...u].find(c=>!v.includes(c)),enter=[...v].find(c=>!u.includes(c));
    frame[enter]=frame[leave]; delete frame[leave];
  }
  return [...path.at(-1)].map(c=>frame[c]).join('');
}
function localEdgeFrame(edge){
  const [u,v]=edge.split('>'),frame={};[...u].forEach((c,i)=>frame[c]=i);
  const leave=[...u].find(c=>!v.includes(c)),enter=[...v].find(c=>!u.includes(c));
  frame[enter]=frame[leave];delete frame[leave];
  return [...v].map(c=>frame[c]).join('');
}
function parity(s){let n=0;for(let i=0;i<s.length;i++)for(let j=i+1;j<s.length;j++)if(s[i]>s[j])n++;return n%2;}
function isCNBClosed(path,allowed){
  if(path.length<4||path[0]!=='012'||path.at(-1)!=='012')return false;
  for(let k=1;k<path.length;k++)if(!allowed.has(path[k-1]+'>'+path[k]))return false;
  const m=path.length-1;
  for(let k=0;k<m;k++)if(path[(k+m-1)%m]===path[(k+1)%m])return false;
  return true;
}
const counts=(path,arcIndex)=>{
  const N=Array(arcIndex.size).fill(0);
  for(let k=1;k<path.length;k++)N[arcIndex.get(path[k-1]+'>'+path[k])]++;
  return N;
};
function passLedger(path,arcIndex,p,wordLength){
  const alphabet=pairPorts(p),q=alphabet.length;
  const M=Array(p*p).fill(0);
  for(let k=1;k<path.length;k++) {
    let i=arcIndex.get(path[k-1]+'>'+path[k]);
    const symbols=Array(wordLength).fill(0);
    for(let j=wordLength-1;j>=0;j--){symbols[j]=i%q;i=Math.floor(i/q);}
    if(i!==0)throw Error('insufficient code alphabet');
    for(const sym of symbols){const [a,b]=alphabet[sym];M[a*p+b]++;}
  }
  return M;
}
function enumerateCNB(arcs,maxLength){
  const outgoing=new Map();for(const e of arcs){const[u,v]=e.split('>');if(!outgoing.has(u))outgoing.set(u,[]);outgoing.get(u).push(v);}
  const bins={}; let frontier=[['012']];
  for(let m=1;m<=maxLength;m++){
    const next=[];
    for(const p of frontier)for(const v of outgoing.get(p.at(-1))||[])
      if(p.length<2||v!==p.at(-2))next.push([...p,v]);
    frontier=next;
    bins[m]=next.filter(p=>isCNBClosed(p,new Set(arcs)));
  }
  return bins;
}
function loopWord(X,Y,word){let p=['012'];for(const c of word)p.push(...(c==='X'?X:Y).slice(1));return p;}
const result={schema:'R732_BRC_CNB_NONABELIAN_COUNT_OBSTRUCTION_V1',
 source_masks:{A:String(masks.A),B:String(masks.B)},arithmetic:'exact nonnegative integer; full finite rooted CNB enumeration',
 root:'012',systems:{}};
for (const [name,mask] of Object.entries(masks)){
  const arcs=edges.filter((_,i)=>(mask&(1n<<BigInt(i)))!==0n);
  if(arcs.length!==15)throw Error('bad carrier size');
  const allowed=new Set(arcs),index=new Map(arcs.map((a,i)=>[a,i]));
  const X=['012','023','013','012'];
  const Y=name==='A'?['012','023','123','012']:['012','123','013','012'];
  if(!isCNBClosed(X,allowed)||!isCNBClosed(Y,allowed))throw Error('elementary loop illegal');
  const XY=loopWord(X,Y,'XY'),YX=loopWord(X,Y,'YX');
  const HXY=holonomy(XY),HYX=holonomy(YX);
  if(!isCNBClosed(XY,allowed)||!isCNBClosed(YX,allowed)||HXY===HYX)throw Error('noncommuting loop pair invalid');
  const nXY=counts(XY,index),nYX=counts(YX,index);
  if(JSON.stringify(nXY)!==JSON.stringify(nYX))throw Error('excursion count mismatch');
  const arcParity=arcs.map(e=>parity(localEdgeFrame(e)));
  const parityFromCounts=n=>n.reduce((z,v,i)=>z+v*arcParity[i],0)%2;
  if(parity(HXY)!==parityFromCounts(nXY)||parity(HYX)!==parityFromCounts(nYX))throw Error('parity mismatch');
  const fourPassEqual=JSON.stringify(passLedger(XY,index,4,2))===JSON.stringify(passLedger(YX,index,4,2));
  const fivePassEqual=JSON.stringify(passLedger(XY,index,5,1))===JSON.stringify(passLedger(YX,index,5,1));
  if(!fourPassEqual||!fivePassEqual)throw Error('V29 ledger not same');
  const bins=enumerateCNB(arcs,6);
  const coverage={};
  for(let m=1;m<=6;m++){
    const groups=new Map();
    for(const p of bins[m]){
      const N=counts(p,index),k=N.join(','),h=holonomy(p);
      if(parity(h)!==parityFromCounts(N))throw Error('enumeration parity mismatch');
      if(!groups.has(k))groups.set(k,new Set());groups.get(k).add(h);
    }
    const maxFiber=Math.max(0,...[...groups.values()].map(s=>s.size));
    coverage[m]={rooted_cnb_histories:bins[m].length,distinct_arc_multisets:groups.size,max_named_holonomies_per_multiset:maxFiber};
    if(m<=5&&maxFiber>1)throw Error('shorter counterexample exists');
  }
  if(coverage[6].max_named_holonomies_per_multiset<2)throw Error('six-step witness missing');
  const words=['XXYY','XYXY','XYYX','YXXY','YXYX','YYXX'];
  const fibers=words.map(word=>{const p=loopWord(X,Y,word);if(!isCNBClosed(p,allowed))throw Error('4 excursion word invalid');return {word,holonomy:holonomy(p),arc_counts:counts(p,index)};});
  for(let i=1;i<fibers.length;i++)if(JSON.stringify(fibers[i].arc_counts)!==JSON.stringify(fibers[0].arc_counts))throw Error('four-excursion multiset mismatch');
  const distinct=[...new Set(fibers.map(x=>x.holonomy))].sort();
  if(distinct.join(',')!=='012,120,201')throw Error('not all 3 even permutations');
  for(const x of fibers){if(parity(x.holonomy)!==parityFromCounts(x.arc_counts))throw Error('four-excursion parity mismatch');}
  // Any fixed per-arc additive ledger factors through the verified 15-component arc-count vector.
  result.systems[name]={arcs,elementary_excursions:{X,Y,X_holonomy:holonomy(X),Y_holonomy:holonomy(Y)},
    first_collision_length:6,
    first_collision:{XY:{path:XY,holonomy:HXY},YX:{path:YX,holonomy:HYX},identical_edge_counts:nXY,
      four_port_two_PASS_count_matrix:passLedger(XY,index,4,2),five_port_one_PASS_count_matrix:passLedger(XY,index,5,1),
      four_port_equal:fourPassEqual,five_port_equal:fivePassEqual},
    rooted_CNB_exact_coverage_to_6:coverage,
    four_excursions:{length:12,words: fibers.map(({word,holonomy})=>({word,holonomy})),
      common_arc_counts:fibers[0].arc_counts,distinct_even_holonomies:distinct,
      four_port_two_PASS_count_matrix:passLedger(loopWord(X,Y,'XXYY'),index,4,2),
      five_port_one_PASS_count_matrix:passLedger(loopWord(X,Y,'XXYY'),index,5,1)},
    edge_signs:arcs.map((arc,i)=>({arc,parity:arcParity[i]}))};
}
result.status='PASS';
console.log(JSON.stringify(result,null,2));