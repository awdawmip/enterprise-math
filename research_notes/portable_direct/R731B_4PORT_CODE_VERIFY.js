/** R731b: four-port off-diagonal V29 PASS fixed-length code for 15 BRC arcs.
 * Pure exact integer finite check; candidate triad updates remain separate.
 * Run: node R731B_4PORT_CODE_VERIFY.js
 */
'use strict';
const triads=['012','013','014','023','024','034','123','124','134','234'];
const universe=[];
for(const u of triads) for(const v of triads) if([...u].filter(c=>v.includes(c)).length===2) universe.push(u+'>'+v);
if(universe.length!==60)throw Error('60 arcs');
const alphabet=[];
for(let a=0;a<4;a++)for(let b=0;b<4;b++)if(a!==b) alphabet.push([a,b]);
if(alphabet.length!==12 || !(alphabet.length<15 && alphabet.length**2>=15))throw Error('coding bound');
const masks={A:'211733226574',B:'5363347296468'};
const out={schema:'R731B_V29_FOUR_PORT_CODE_CERT_V1',port_count:4,off_diagonal_PASS_alphabet_size:12,arc_count:15,one_PASS_injective_code_possible:false,minimum_fixed_PASS_word_length:2,systems:{}};
function frames(path){const f={0:0,1:1,2:2};for(let k=1;k<path.length;k++){
  const u=path[k-1],v=path[k],leave=[...u].find(x=>!v.includes(x)),enter=[...v].find(x=>!u.includes(x));f[enter]=f[leave];delete f[leave];
}return path.at(-1).split('').map(x=>f[x]).join('');}
function order(s){const p=[...s].map(Number);let x=[0,1,2];for(let k=1;k<=6;k++){x=x.map(a=>p[a]);if(x.join('')==='012')return k;}throw Error('permutation order');}
function wordMap(arcs){const code=arcs.map((_,i)=>[Math.floor(i/12),i%12]);if(new Set(code.map(x=>x.join(','))).size!==15)throw Error('noninjective code');return code;}
function encodePath(path,arcs,code){const idx=new Map(arcs.map((x,i)=>[x,i]));const stream=[];const M=Array.from({length:4},()=>Array(4).fill(0));const recovered=[];
  for(let k=1;k<path.length;k++){
   const u=path[k-1],v=path[k],e=u+'>'+v;if(!idx.has(e)||(k>=2&&path[k-2]===v))throw Error('bad arc/path');
   for(const c of code[idx.get(e)]){const [a,b]=alphabet[c];M[a][b]++;stream.push(c);}
  }
  if(stream.length!==2*(path.length-1))throw Error('wrong grade');
  const rev=new Map(code.map((c,i)=>[c.join(','),i]));
  for(let j=0;j<stream.length;j+=2){const decoded=rev.get(stream[j]+','+stream[j+1]);if(decoded===undefined)throw Error('decoding error');recovered.push(arcs[decoded]);}
  const trueWords=path.slice(1).map((v,k)=>path[k]+'>'+v);
  if(recovered.join('|')!==trueWords.join('|'))throw Error('wrong recovered path');
  if(M.flat().reduce((a,b)=>a+b,0)!==stream.length)throw Error('grade mismatch');
  return {frame:frames(path),PASS_events:stream.length,unique_symbols_used:new Set(stream).size};
}
function prefixCount(arcs,code){const outgoing={};for(const e of arcs){const [u,v]=e.split('>');(outgoing[u]??=[]).push(v);}let count=0;
 const rec=p=>{encodePath(p,arcs,code);count++;if(p.length===8)return;for(const v of outgoing[p.at(-1)]??[])if(p.length<2||v!==p.at(-2))rec([...p,v]);};rec(['012']);return count;
}
for(const [name,mask] of Object.entries(masks)){
 const big=BigInt(mask),arcs=universe.filter((_,i)=>(big&(1n<<BigInt(i)))!==0n),code=wordMap(arcs);if(arcs.length!==15)throw Error('arc count');
 const loop=name==='A'?['012','023','123']:['012','023','123','013'];
 for(let k=0;k<loop.length;k++)if(loop[(k+loop.length-1)%loop.length]===loop[(k+1)%loop.length])throw Error('seam');
 const one=encodePath([...loop,'012'],arcs,code),o=order(one.frame);
 const repeat=Array.from({length:o},()=>loop).flat(),full=encodePath([...repeat,'012'],arcs,code);
 if(full.frame!=='012'||full.PASS_events!==2*loop.length*o)throw Error('relation return');
 out.systems[name]={arc_mask:mask,arcs:15,codebook:code.map((c,i)=>({arc:arcs[i],PASS_pair_indices:c})),
  cyclic_loop:loop.concat('012'),one_loop_holonomy:one.frame,holonomy_order:o,rooted_CNB_prefixes_tested_to_7_steps:prefixCount(arcs,code),
  abstract_relation_return_arc_steps:loop.length*o,actual_V29_PASS_events_at_relation_return:full.PASS_events,native_ledger_grade_increment:full.PASS_events};
}
out.status='PASS';
process.stdout.write(JSON.stringify(out,null,2)+'\n');
