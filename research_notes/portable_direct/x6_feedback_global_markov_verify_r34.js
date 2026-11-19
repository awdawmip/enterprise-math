#!/usr/bin/env node
'use strict';
const v=require('./x6_feedback_product_brc_verify_r33.js');
const T=v.toy||v.toyStep;
const lang=v.language||v.directLanguage;
const A=['Q0','Q1'],states=[];
for(let t=0;t<4;t++){
 const q=[1],seen=new Set([1]);
 for(let i=0;i<q.length;i++)for(const a of A){
  const z=T(t,q[i],a);if(z!==null&&!seen.has(z)){seen.add(z);q.push(z)}
 }
 for(const s of q)states.push([t,s])
}
const sig=(t,s)=>JSON.stringify([...lang(t,s,A,T,12)].sort());
const groups=new Map();
for(const [t,s] of states){const k=sig(t,s);if(!groups.has(k))groups.set(k,[]);groups.get(k).push([t,s])}
if(states.length!==12||groups.size!==5)throw Error('unexpected state/class count');
for(const [k,g] of groups)for(const a of A){
 const first=g[0],z=T(first[0],first[1],a);
 for(const [t,s] of g){const w=T(t,s,a);
  if((z===null)!==(w===null))throw Error('enabledness');
  if(z!==null&&sig(first[0],z)!==sig(t,w))throw Error('not right-congruent')
 }
}
const init=[0,1,2,3].map(t=>sig(t,1));
if(new Set(init).size!==3)throw Error('initial fiber');
const out={schema:'X6_R34_GLOBAL_MARKOV_LANGUAGE_QUOTIENT_VERIFY_V1',observer:'fully labelled successful event words; no independent public-state readout',initial_public_state:1,hidden_histories:4,reachable_decorated_states:states.length,initial_history_language_classes:3,global_reachable_markov_language_classes:5,classes:[...groups.entries()].sort((x,y)=>x[0].localeCompare(y[0])).map(([k,g])=>({language:JSON.parse(k),decorated_states:g})),right_congruence_checked:true,pass:true};
if(require.main===module)console.log(JSON.stringify(out,null,2));
module.exports={out};
