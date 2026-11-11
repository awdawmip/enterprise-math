#!/usr/bin/env node
/** R733: exact positive BRC arc-count and V29 four-port ledger recovery.
 * Run: node R733_FOUR_PORT_FLOW_VERIFY.js > R733_FOUR_PORT_FLOW_RESULTS.json
 * No floating point, trigonometric or physical-force operations.
 */
'use strict';
const tris=[];
for(let a=0;a<5;a++)for(let b=a+1;b<5;b++)for(let c=b+1;c<5;c++)tris.push(''+a+b+c);
const universe=[];
for(const u of tris)for(const v of tris)if([...u].filter(x=>v.includes(x)).length===2)universe.push(u+'>'+v);
if(universe.length!==60)throw Error('unexpected universe');
function exactDet(input){
 const m=input.map(row=>row.map(BigInt));const n=m.length;
 let prev=1n,sgn=1n;
 for(let k=0;k<n-1;k++){
  if(m[k][k]===0n){let r=k+1;while(r<n&&m[r][k]===0n)r++;
   if(r===n)return 0n;[m[k],m[r]]=[m[r],m[k]];sgn=-sgn;}
  const p=m[k][k];
  for(let i=k+1;i<n;i++)for(let j=k+1;j<n;j++){
   const num=m[i][j]*p-m[i][k]*m[k][j];
   if(num%prev!==0n)throw Error('Bareiss nonintegral');
   m[i][j]=num/prev;
  }
  for(let i=k+1;i<n;i++)m[i][k]=0n;
  prev=p;
 }
 return sgn*m[n-1][n-1];
}
const configs={
 A:{mask:'211733226574',rows:['012','013','014'],expected:'-2',
    X:['012','023','013','012'],Y:['012','023','123','012']},
 B:{mask:'5363347296468',rows:['012','013','123'],expected:'2',
    X:['012','023','013','012'],Y:['012','123','013','012']}
};
const result={schema:'R733_FOUR_PORT_FLOW_INTEGRAL_CERT_V1',status:'PASS',
 source:'R731b PR #2119; R732 nonabelian PR #2124',
 math:'exact nonnegative integer BRC path multiplicities; Z-incidence and ledger matrices',
 bound:'all lengths by exact determinant; prefixes <=10 arcs independently checked',
 systems:{}};
for(const [name,cfg] of Object.entries(configs)){
 const arcs=universe.filter((_,i)=>(BigInt(cfg.mask)&(1n<<BigInt(i)))!==0n);
 if(arcs.length!==15)throw Error('not 15 arcs');
 const vtx=[...new Set(arcs.flatMap(e=>e.split('>')))].sort();
 const C=Array.from({length:12},()=>Array(15).fill(0));
 const B=Array.from({length:vtx.length},()=>Array(15).fill(0));
 const idx=new Map(arcs.map((e,i)=>[e,i])),outgoing={};
 arcs.forEach((e,i)=>{
  C[Math.floor(i/12)][i]++;C[i%12][i]++;
  const [u,v]=e.split('>');
  B[vtx.indexOf(u)][i]--;B[vtx.indexOf(v)][i]++;
  (outgoing[u]??=[]).push(v);
 });
 const d=exactDet(C.concat(cfg.rows.map(v=>B[vtx.indexOf(v)])));
 if(d.toString()!==cfg.expected)throw Error('det mismatch '+name+' '+d);
 const visited=new Map(),holos=new Map();
 let prefixCount=0,maxHolonomies=0;
 function inspect(path,frame,counts,Y){
  prefixCount++;
  const terminal=path.at(-1);
  const key=terminal+'|'+Y.join(','),nkey=counts.join(',');
  if(visited.has(key)&&visited.get(key)!==nkey)throw Error('count not recoverable: '+key);
  visited.set(key,nkey);
  const h=terminal.split('').map(x=>frame[x]).join('');
  if(!holos.has(key))holos.set(key,new Set());
  holos.get(key).add(h);
  maxHolonomies=Math.max(maxHolonomies,holos.get(key).size);
  const countSum=counts.reduce((x,y)=>x+y,0);
  if(Y.reduce((x,y)=>x+y,0)!==2*countSum)throw Error('grade mismatch');
  const flow=Array(vtx.length).fill(0);
  for(let j=0;j<15;j++)for(let i=0;i<vtx.length;i++)flow[i]+=B[i][j]*counts[j];
  for(let i=0;i<vtx.length;i++){
   const want=(vtx[i]===terminal?1:0)-(vtx[i]==='012'?1:0);
   if(flow[i]!==want)throw Error('flow mismatch');
  }
  if(countSum===10)return;
  for(const next of outgoing[terminal]||[]){
   if(path.length>1&&next===path[path.length-2])continue;
   const left=[...terminal].find(x=>!next.includes(x));
   const enter=[...next].find(x=>!terminal.includes(x));
   const f={...frame,[enter]:frame[left]};delete f[left];
   const i=idx.get(terminal+'>'+next),c2=counts.slice(),y2=Y.slice();
   c2[i]++;y2[Math.floor(i/12)]++;y2[i%12]++;
   inspect([...path,next],f,c2,y2);
  }
 }
 inspect(['012'],{'0':'0','1':'1','2':'2'},Array(15).fill(0),Array(12).fill(0));
 const words=['XXYY','XYXY','XYYX','YXXY','YXYX','YYXX'];
 const witnesses=[];
 for(const word of words){
  const path=['012'];
  for(const c of word)path.push(...cfg[c].slice(1));
  if(path.at(-1)!=='012')throw Error('nonclosed');
  for(let k=2;k<path.length;k++)if(path[k]===path[k-2])throw Error('backtracking');
  if(path[1]===path[path.length-2])throw Error('cyclic seam');
  const count=Array(15).fill(0),Y=Array(12).fill(0),frame={'0':'0','1':'1','2':'2'};
  for(let k=1;k<path.length;k++){
   const u=path[k-1],v=path[k],i=idx.get(u+'>'+v);
   if(i===undefined)throw Error('arc not allowed');
   count[i]++;Y[Math.floor(i/12)]++;Y[i%12]++;
   const leave=[...u].find(x=>!v.includes(x)),enter=[...v].find(x=>!u.includes(x));
   frame[enter]=frame[leave];delete frame[leave];
  }
  witnesses.push({word,holonomy:path.at(-1).split('').map(x=>frame[x]).join(''),
                  arc_counts:count.join(','),ledger:Y.join(',')});
 }
 if(new Set(witnesses.map(w=>w.ledger)).size!==1||
    new Set(witnesses.map(w=>w.arc_counts)).size!==1||
    new Set(witnesses.map(w=>w.holonomy)).size!==3)throw Error('three-holonomy lower bound');
 result.systems[name]={
  arc_mask:cfg.mask,arcs:arcs.length,vertex_balance_rows:cfg.rows,
  exact_15x15_determinant:d.toString(),rooted_prefixes_tested:prefixCount,
  terminal_ledger_fibers:visited.size,
  maximum_holonomies_in_tested_fiber:maxHolonomies,
  fixed_length_12_same_arc_count_holonomies:witnesses.map(w=>[w.word,w.holonomy]),
  witness_same_full_ledger:true,witness_same_full_arc_counts:true
 };
}
process.stdout.write(JSON.stringify(result,null,2)+'\n');
