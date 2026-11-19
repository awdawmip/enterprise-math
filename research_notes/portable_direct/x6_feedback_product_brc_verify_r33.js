#!/usr/bin/env node
'use strict';
function key(s){return String(s)}
function toy(t,s,a){
 const x=s&1,u=s>>1;
 if(a==='Q0'){if((u&1)||!(t&1))return null;return (u|1)<<1}
 if(a==='Q1'){if((u&2)||!((t&2)||x))return null;return ((u|2)<<1)|x}
 throw Error('label')
}
function shortest(t,e,start,A,step){
 const q=[[start,start,[]]],seen=new Set([key(start)+'|'+key(start)]);
 for(let i=0;i<q.length;i++){
  const [x,y,p]=q[i];
  for(const a of A){
   const z=step(t,x,a),w=step(e,y,a);
   if((z===null)!==(w===null))return {length:p.length+1,witness:p.concat([a])};
   if(z!==null){const k=key(z)+'|'+key(w);
    if(!seen.has(k)){seen.add(k);q.push([z,w,p.concat([a])])}}
  }
 }
 return {length:null,witness:null}
}
function language(t,start,A,step,h){
 const out=new Set(['']);let curr=[[start,'']];
 for(let d=0;d<h;d++){
  const next=[];
  for(const [s,p] of curr)for(const a of A){
   const z=step(t,s,a);
   if(z!==null){const w=p+a+';';out.add(w);next.push([z,w])}
  }
  curr=next
 }
 return out
}
function equal(a,b){return a.size===b.size&&[...a].every(x=>b.has(x))}
function partition(h,step,start,A){
 const L=[0,1,2,3].map(i=>language(i,start,A,step,h)),groups=[];
 for(let i=0;i<4;i++){let g=groups.find(x=>equal(L[x[0]],L[i]));
  if(g)g.push(i);else groups.push([i])}
 return groups
}
function rng(seed){return ()=>{let t=seed+=0x6D2B79F5;t=Math.imul(t^t>>>15,t|1);
 t^=t+Math.imul(t^t>>>7,t|61);return ((t^t>>>14)>>>0)/4294967296}}
function main(){
 const A=['Q0','Q1'],expected=[[[0,1,2,3]],[[0,2],[1,3]],[[0,2],[1],[3]]];
 let comparisons=0;
 for(let h=0;h<=4;h++){
  const p=partition(h,toy,1,A),e=h===0?expected[0]:h===1?expected[1]:expected[2];
  if(JSON.stringify(p)!==JSON.stringify(e))throw Error('toy h='+h);
  for(let x=0;x<4;x++)for(let y=x+1;y<4;y++){
   const d=shortest(x,y,1,A,toy).length;
   const same=equal(language(x,1,A,toy,h),language(y,1,A,toy,h));
   if(same!==(d===null||d>h))throw Error('toy comparison');comparisons++
  }
 }
 if(shortest(1,3,1,A,toy).length!==2||shortest(0,2,1,A,toy).length!==null)throw Error('toy witness');
 const random=rng(0x33C0FFEE),N=3,CASES=96;
 let tested=0,finite=0,infinite=0,max=0;
 for(let k=0;k<CASES;k++){
  const T=Array.from({length:4},()=>Array.from({length:N},()=>A.map(()=>{
   const j=Math.floor(random()*4);return j===3?null:j
  })));
  const step=(t,s,a)=>T[t][s][a==='Q0'?0:1];
  for(let x=0;x<4;x++)for(let y=x+1;y<4;y++){
   const d=shortest(x,y,0,A,step).length;
   if(d===null)infinite++;else{finite++;max=Math.max(max,d);if(d>N*N)throw Error('bound')}
   let f=null;
   for(let h=0;h<=N*N;h++){
    if(!equal(language(x,0,A,step,h),language(y,0,A,step,h))){f=h;break}
   }
   if(f!==d)throw Error('BFS/direct disagreement');tested++
  }
 }
 return {schema:'X6_R33_FEEDBACK_PAIR_LANGUAGE_VERIFY_V1',
  seed:'0x33C0FFEE',model:'exact finite deterministic partial labelled success languages',
  toy:{history_count:4,depths_checked:[0,1,2,3,4],classes_by_depth:[1,2,3,3,3],
    fibers:[[0,2],[1],[3]],witness:{histories:[1,3],word:['Q0','Q1'],length:2},
    forever_equivalent_histories:[0,2],pair_depth_comparisons:comparisons,pass:true},
  crosscheck:{controllers:CASES,states_per_history:N,labels:A,history_pairs_checked:tested,
   direct_language_max_depth:N*N,finiteWitnesses:finite,unreachablePairs:infinite,maxWitness:max,pass:true},
  symbolic_claim:'pair-product BFS shortest mismatch; finite deterministic; N^2 distinction bound'}
}
const result=main();
if(require.main===module)process.stdout.write(JSON.stringify(result,null,2)+'\n');
module.exports={main,shortest,language,toy};
