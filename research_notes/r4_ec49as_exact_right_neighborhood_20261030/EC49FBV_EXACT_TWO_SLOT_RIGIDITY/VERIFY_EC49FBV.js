#!/usr/bin/env node
'use strict';
// EC49FBV: frozen signed-X6 primitive-prefix exact 1- and 2-slot exchange audit.
function run(){
const OPS='acdefg', STEP={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const ENC={'-1':'a','1':'A','-2':'b','2':'B','-3':'c','3':'C'};
const T=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],[6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]];
const SIG=[0,0,4,1,16,32,8,2,0];
const REQUIRED={2:[16,32],3:[16,32],4:[1,2,4,8],5:[16,32],6:[1,2,4,8],7:[1,2,4,8],8:[1,2,4,8],9:[16,32]};
const W={2:['fe','ge'],3:['feg','gef'],4:['degf','fegd','cefg','gefc'],5:['feggf','geffg'],6:['aeeddd','dedead','aeeccc','ceceac'],7:['aeeddgf','dedeagf','ceceafg','aeeccfg'],8:['feggfead','geffgaed','geffgaec','feggfeac'],9:['feggfeafg','geffgaegf']};
const assert=(v,m)=>{if(!v)throw Error(m)};
const obs=w=>{let state=0;for(const c of w){state=T[state][OPS.indexOf(c)];if(state===8)return null}return SIG[state]};
const primitive=w=>[...w].flatMap(c=>STEP[c].map(v=>ENC[v])).join('');
const pref=s=>Array.from({length:s.length},(_,i)=>s.slice(0,i+1));
const slots=[],chosen=new Map(),pool=new Map(),expansions=new Map(),prefixes=new Map();
function path(w){if(!expansions.has(w)){const str=primitive(w);expansions.set(w,str);prefixes.set(w,pref(str))}return expansions.get(w)}
function edges(words){const out=new Set();for(const w of words){path(w);for(const p of prefixes.get(w))out.add(p)}return out}
for(let h=2;h<=9;h++)for(const w of W[h]){
 const sig=obs(w);assert(REQUIRED[h].includes(sig),'invalid observer signature '+w);
 const k=h+':'+sig;assert(!chosen.has(k),'duplicate required signature');chosen.set(k,w);path(w);
 const disp=Array(6).fill(0),pos=Array(6).fill(0);
 for(const c of w)for(const a of STEP[c]){disp[Math.abs(a)-1]+=Math.sign(a);if(a>0)pos[a-1]++}
 assert(disp.join()==='2,0,0,0,0,0','native displacement '+w);
 if(h>=4)assert(pos.join()===(h<=5?'4,2,1,0,0,0':'7,3,2,0,0,0'),'full positive BRC key '+w);
}
assert(chosen.size===24,'24 required words');
function generate(h){
 const [x,y,z]=h<=5?[4,2,1]:[7,3,2],b=x+y-(h+1),a=z-1,f=x-b-2*z,g=y-b;
 assert(Math.min(b,a,f,g)>=0,'negative operation multiplicity');
 const out=new Map(REQUIRED[h].map(s=>[s,[]]));
 for(let c=0;c<=b;c++){
  const m={a,c,d:b-c,e:z,f,g};
  function rec(w){
   if(w.length===h){const sig=obs(w);if(out.has(sig))out.get(sig).push(w);return}
   for(const op of OPS)if(m[op]){m[op]--;rec(w+op);m[op]++}
  }rec('');
 }return out;
}
const expected={4:48,5:24,6:120,7:2520,8:10080,9:3360};
for(let h=4;h<=9;h++){
 const g=generate(h);
 for(const sig of REQUIRED[h]){
  const slot=h+':'+sig;slots.push(slot);pool.set(slot,g.get(sig));
  assert(g.get(sig).includes(chosen.get(slot)),'selected word absent from candidate set '+slot);
 }
 const count=REQUIRED[h].reduce((a,s)=>a+g.get(s).length,0);
 assert(count===expected[h],'candidate size error H'+h+': '+count);
}
const baseline=edges(chosen.values());assert(baseline.size===158,'wrong original primitive-edge cost');
const single=[];
for(const slot of slots){
 const rest=edges([...chosen.entries()].filter(([k])=>k!==slot).map(([,w])=>w));
 const costs=new Map();
 for(const w of pool.get(slot)){
  path(w);let added=0;for(const p of prefixes.get(w))if(!rest.has(p))added++;
  const cost=rest.size+added;costs.set(cost,(costs.get(cost)||0)+1);
 }
 const minimum=Math.min(...costs.keys());assert(minimum===158,'single replacement lowers cost '+slot);
 single.push({slot,count:pool.get(slot).length,minimum,neutral_other:(costs.get(158)||0)-1,delta_1:costs.get(159)||0,delta_2:costs.get(160)||0});
}
class Node{constructor(){this.children=new Map();this.terminal=null;this.tail=100000;this.arg=null}}
function build(candidates,rest){
 const root=new Node();
 for(const w of candidates){let node=root;for(const ch of path(w)){
  if(!node.children.has(ch))node.children.set(ch,new Node());
  node=node.children.get(ch);
 }node.terminal=w}
 function solve(node,p){
  if(node.terminal!==null){node.tail=0;node.arg=node.terminal}
  for(const [ch,child] of node.children){
   const next=p+ch;solve(child,next);
   const cost=child.tail+(rest.has(next)?0:1);
   if(cost<node.tail){node.tail=cost;node.arg=child.arg}
  }
 }solve(root,'');return root;
}
const pairs=[];
for(let i=0;i<slots.length;i++)for(let j=i+1;j<slots.length;j++){
 const a=slots[i],b=slots[j];
 const rest=edges([...chosen.entries()].filter(([k])=>k!==a&&k!==b).map(([,w])=>w));
 const root=build(pool.get(b),rest);
 let best=100000,argA=null,argB=null;
 for(const w of pool.get(a)){
  path(w);let added=0;for(const p of prefixes.get(w))if(!rest.has(p))added++;
  let node=root,tail=node.tail,wb=node.arg;
  for(const ch of expansions.get(w)){
   const next=node.children.get(ch);if(!next)break;
   node=next;if(node.tail<tail){tail=node.tail;wb=node.arg}
  }
  const cost=rest.size+added+tail;
  if(cost<best){best=cost;argA=w;argB=wb}
 }
 const chosenPair=new Map(chosen);chosenPair.set(a,argA);chosenPair.set(b,argB);
 assert(edges(chosenPair.values()).size===best,'native primitive direct audit mismatch '+a+','+b);
 assert(best===158,'two-slot improvement found '+a+','+b+': '+best);
 pairs.push({slot_a:a,slot_b:b,min_cost:best,chosen_a:argA,chosen_b:argB});
}
assert(pairs.length===190,'pair count mismatch');
const allCounts=Object.values(expected).reduce((a,b)=>a+b,0);
return {schema:'EC49FBV_EXACT_RADIUS_TWO_AUDIT_V1',date:'2026-11-06',
 scientific_input_pin:'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
 parent_author_commit:'b3b43ef6abe2fd816d979792d18a67ee5d0aad50',
 schedule:{H2_H3:'fixed',H4_H5_L:[4,2,1],H6_H9_M:[7,3,2]},
 witness:W,original_cost:158,candidate_counts:expected,total_candidates:allCounts,
 one_slot_distinct_substitutions:allCounts-20,one_slot_results:single,
 two_slot_combinations:pairs.length,two_slot_results:pairs,
 result:'NO_ONE_OR_TWO_SIGNATURE_SLOT_REPLACEMENT_IMPROVES_158'};
}
if(typeof module!=='undefined' && require.main===module)console.log(JSON.stringify(run(),null,2));
